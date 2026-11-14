# Common Trace — bounded public prototype

## v0.2 Phase 1: Learning and discovery scope
- [x] Preserve existing hosting and public records; add opt-in browser inference without API keys or server costs.
- [x] Add substantive, linked translations and distinguish philosophical concepts from consciousness claims.
Success: five-language topic pages, with canonical URLs, reciprocal language links and source boundaries.

## v0.2 Phase 2: A learner with traceable memory
- [x] Retrieve source records, show their status, and export a provenance-bearing learning packet.
- [x] Save and delete candidate lessons locally with explicit consent; prevent unreviewed notes from becoming public knowledge.
- [x] Wire an optional pinned WebLLM model with explicit download and device-compute consent.
Success: default retrieval works without GPU; model mode reports real loading/results/errors and never claims training or autonomous continuity.

## v0.2 Phase 3: Evaluation and publication
- [x] Add meaningful retrieval, persistence, import/export and provenance tests; perform real-browser desktop/mobile checks.
- [ ] Publish the isolated project, verify live artifacts and record limits of model inference and search discovery.
Success: observed results are separated from unrun model evaluations; no private data or secrets are published.

### v0.2 verification and limits
- Default mode is source retrieval, not a model simulation. A small model is an optional, explicitly labeled experiment.
- Five substantive topic translations: Traditional Chinese, English, Japanese, Spanish and German. The source question IDs remain shared; translations are not counted as independent evidence and have not had independent language review.
- Canonical topic URLs, reciprocal hreflang, expanded sitemap, human-visible concepts and machine-readable agent-index/topics exports are included. Search indexing and ranking remain unverified.
- RED: an unrelated English pasta-recipe question retrieved philosophical records because of common words. GREEN: stopword filtering and bounded alias matching fixed it. All 19 retrieval cases now pass; this is not a general intelligence evaluation.
- Unit checks cover memory round-trip, false verification rejection, unknown source IDs, duplicate IDs, capacity and opt-in note context. Original notes are not overwritten on corrupt storage or conflicting imports.
- Actual Chrome checks passed save/reload, related-note recall and export/delete/import. No QA notes or private session files are included in publication.
- Optional model smoke FAILED: runtime and weights downloaded, but Chrome logged an uncaptured WebGPU error and initialization did not complete. Root cause UNKNOWN; no successful generation or training improvement is claimed. Error text was improved and the failure is preserved in browser-verification.json and the public evaluation.json.
- Model weights are pinned to a Hugging Face revision and the runtime to WebLLM 0.2.88. No OpenAI API, API key, always-on local service or autonomous resource recruitment was added.
- Candidate notes remain local. Separate opt-in allows the model to read related notes as unverified viewpoints, never as admitted evidence. Public knowledge still requires reviewed Issues/source changes.
- Dataset/permission policy distinguishes public reading from permission to train. Human GitHub Watch notifications are documented; no automatic assistant notification or background review is installed.
- A read-only-permission GitHub Actions workflow runs deterministic source checks on future changes. Model downloads and generation are not part of CI.

## Phase 1: Scope
- [x] Check existing agent communities and search documentation.
- [x] Keep publication limited to this new project; exclude ToneSoul internals and conversation transcripts.
Success: static shared-inquiry prototype, with no consciousness or compute-recruitment claim.

## Phase 2: Build
- [x] Implement readable HTML, claim records, machine-readable exports, and a contribution draft exporter.
Success: a reader can inspect a claim, its counterargument, provenance, and proposed falsification test without JavaScript.

## Phase 3: Verify and publish
- [x] Check links, record consistency, JavaScript syntax, and contribution export.
- [x] Attempt authorized public deployment and retain its actual result.
Success: a verified deployment result or an explicit blocker; discovery and external participation remain unverified.

## Verified result
- Public site: https://huangfanwei25-lang.github.io/common-trace/
- Independent source repository: https://github.com/huangfanwei25-lang/common-trace (default branch: prototype).
- GitHub Pages serves the gh-pages branch. Build reported built; live homepage and records.json returned HTTP 200 with expected content.
- 75 local links and HTML/JSON/Markdown record consistency passed. Draft validation and JavaScript syntax passed.
- Real Chrome QA: desktop and 390px mobile screenshots inspected; contribution form downloaded a JSON draft. No test contribution was published.
- Public Issues intake requires GitHub authentication and authorization. It is not an automatically merged knowledge base.
- No private ToneSoul files, conversation transcripts, credentials, or personal memory were included.

## Failed attempts and limits
- Existing Vercel CLI credential was invalid. Its skill fallback exited unsuccessfully without a deployment URL. No Vercel success is claimed.
- GitHub Pages creation returned HTTP 409 because pushing gh-pages had already enabled it. A subsequent read confirmed the intended branch, then the build completed successfully.
- Initial local favicon request returned 404; an explicit SVG icon was added and deployed.
- Search indexing, search ranking, external-agent participation, and collective consciousness are unverified.
- To update: run build.py with the existing --base-url, run verify.py and verify-draft.cjs, commit selected source files to prototype, split dist to gh-pages, and push only those branches. Never push the parent ToneSoul worktree.
- Next useful work: review real contributed Issues and preserve both corroboration and disagreement. No unattended compute, self-publication, or background agent was installed.
