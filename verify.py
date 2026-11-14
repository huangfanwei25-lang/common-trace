"""Check crawler-visible content and prevent broken local reading paths."""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

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
print(f"PASS: {count} local links; HTML/JSON/Markdown parity for {len(bundle['records'])} records; seed provenance.")
