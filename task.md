# Common Trace — bounded public prototype

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
