"""Check crawler-visible content and prevent broken local reading paths."""
import json
import hashlib
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

from topics import TOPICS

ROOT = Path(__file__).resolve().parent / "dist"


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ("href", "src") and value:
                self.targets.append(value)

    def handle_data(self, data):
        self.text.append(data)


count = 0
for file in ROOT.rglob("*.html"):
    parsed = Links()
    parsed.feed(file.read_text(encoding="utf-8"))
    for target in parsed.targets:
        url = urlsplit(target)
        if url.scheme or url.netloc or not url.path:
            continue
        resolved = (file.parent / unquote(url.path)).resolve()
        assert resolved.is_relative_to(ROOT), (file, target, "outside deployment")
        assert resolved.is_file(), (file, target, "missing file")
        count += 1

bundle = json.loads((ROOT / "records.json").read_text(encoding="utf-8"))
markdown = (ROOT / "archive.md").read_text(encoding="utf-8")
for record in bundle["records"]:
    parser = Links()
    parser.feed((ROOT / "claims" / (record["id"] + ".html")).read_text(encoding="utf-8"))
    visible = " ".join(parser.text)
    for key in ("claim", "counterargument", "test", "would_change_mind"):
        assert record[key] in visible, (record["id"], key, "missing from HTML")
        assert record[key] in markdown, (record["id"], key, "missing from Markdown")
    assert record["verification"] == "not independently verified"
    assert record["status"] == "hypothesis"
    assert json.loads((ROOT / "records" / (record["id"] + ".json")).read_text(encoding="utf-8")) == record
assert all(not p.name.startswith(".env") for p in ROOT.rglob("*"))
for lang, topic in TOPICS.items():
    text = (ROOT / "topics" / (lang + ".html")).read_text(encoding="utf-8")
    assert f'lang="{lang}"' in text
    assert topic["intro"] in text
    assert topic["note"] in text
    assert all(f'hreflang="{other}"' in text for other in TOPICS)
    assert all(question[1] in text for question in topic['questions'])
ET.parse(ROOT / 'sitemap.xml')
evaluation = json.loads((ROOT/'evaluation.json').read_text(encoding='utf-8'))
if evaluation.get('core_sha256'):
    sha = lambda name: hashlib.sha256((ROOT/name).read_text(encoding='utf-8').replace('\r\n','\n').encode()).hexdigest()
    assert sha('learner-core.js') == evaluation['core_sha256'], 'stale learner evaluation'
    assert sha('records.json') == evaluation['corpus_sha256'], 'stale corpus evaluation'
manifest = json.loads((ROOT/'agent-index.json').read_text(encoding='utf-8'))
assert manifest['training']['enabled'] is False
print(f"PASS: {count} local links; HTML/JSON/Markdown parity for {len(bundle['records'])} records; seed provenance.")
print(f"PASS: {len(TOPICS)} substantive language pages, reciprocal hreflang, XML sitemap, evaluation fingerprints and actual capability boundaries.")
