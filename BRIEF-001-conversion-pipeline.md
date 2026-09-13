# BRIEF 001: slide-to-markdown conversion pipeline

Owner: Hermes (architect/reviewer). Implementer: opencode CLI. Repo: /home/liebert511/mas2001-mte

## Goal

Build `scripts/convert.py`, a resumable, parallel pipeline that turns 348 PDF slide
pages into exam-grade markdown. No new dependencies beyond the Python standard
library and the system tools already on the box (`pdftoppm`, `pdfinfo`).

## Hard inputs

- Source list: `sources.yaml` in the repo root. Do not edit it. Read it with a
  tiny hand-rolled parser or `json.loads` after converting, but do not add PyYAML.
  Simplest acceptable approach: the file is yours to parse, but treat it as
  read-only input.
- The reader is an existing, proven CLI: `/home/liebert511/.local/bin/vision`
  (arg: `IMAGE "question"`, optional `--model`). It calls an OpenAI-compatible
  chat endpoint and prints markdown on stdout. It reads `COMMANDCODE_API_KEY`
  from the environment or `~/.hermes/.env`. It honours `VISION_MAX_TOKENS`.
  Reuse it as a subprocess. Do not reimplement the HTTP call.
- Never call it without a real answer: if stdout is empty, that is a failure.

## What convert.py must do

1. For each source in `sources.yaml`:
   - verify the file exists and its sha256 matches the manifest when a sha256 is
     given. Mismatch is a fatal error for that source, not a crash for the run.
   - render pages with `pdftoppm -r <dpi> -png -f N -l N` into
     `work/pages/<label>/p<NNN>.png`, skipping pages whose PNG already exists.
2. For each rendered page, call the vision CLI with the prompt in
   `PROMPT.txt` (repo root, read at runtime, do not hardcode a second copy) and
   the PNG path. Capture stdout as the page markdown.
3. Write `md/<label>/p<NNN>.md`. A page is DONE when that file exists and is
   non-empty. Re-runs must skip DONE pages (resume support).
4. Append one JSON object per page to `work/manifest.jsonl`:
   `label, page, png_sha256, status, attempts, latency_s, chars,
   stderr_note, model, ts`. `status` is one of `ok`, `truncated`, `empty`,
   `error`. A rerun of a page appends a new line, never rewrites history.
5. Concurrency: `--workers N` (default 6) using `concurrent.futures.ThreadPoolExecutor`.
   Each worker shells out to the vision CLI, so the work is IO bound. No shared
   mutable state outside the manifest lock.
6. Retries: on empty stdout, non-zero exit, or an exception, retry up to 3 times
   with exponential backoff (2s, 6s, 18s). If the CLI prints the literal string
   `[truncated` to stderr, mark `truncated`, retry once with
   `VISION_MAX_TOKENS` doubled, and keep the longer of the two answers.
7. Report banned output: if a page markdown contains `example.com`, `](http`,
   or `https://`, log `banned_url=true` in the manifest entry. Do not strip the
   text, just flag it so the reviewer can see how often the reader invents links.
8. CLI flags: `--label L` (repeatable, default all), `--limit N` (first N pages
   per label, for pilots), `--force`, `--workers N`, `--dpi N`, `--dry-run`.
9. Final summary to stdout: per label, pages total / done / failed, and the
   number of pages flagged `banned_url` or `truncated`. Also write
   `work/SUMMARY.md` with the same table plus total wall time.

## Also build `scripts/assemble.py`

Takes `md/<label>/p*.md` in page order and emits:

- `md/<label>.md`: a single document, one `---` separator between pages, a
  heading line `# <label>` at the top, and each page body underneath.
- `md/INDEX.json`: `{label: {pages, chars, done, flagged}}`.

Idempotent. Re-running it must produce byte-identical output for unchanged input.

## Constraints

- Python 3.13+ standard library only. No pip, no uv, no new packages.
- Absolute paths. The repo will be run from the repo root, but do not rely on cwd.
- No em dashes anywhere in code, comments, docs, or output strings. Use commas,
  periods, or colons.
- Do not print a progress line per page to stdout. One line per completed label
  and a final table. Page-level detail belongs in the manifest.
- Idempotent and crash-safe: killing the process at any moment must leave the
  repo in a state where a rerun resumes rather than restarts.

## Acceptance (Hermes runs these, not you)

```
python3 scripts/convert.py --dry-run
python3 scripts/convert.py --label lms-method-of-moments --dpi 110
python3 scripts/assemble.py
python3 scripts/convert.py --label lms-method-of-moments
```
The third command must do nothing (resume works) and the manifest must gain no
new lines. A second `--dry-run` must list zero pending pages for that label.

Do not run the full 348 page job. That is Hermes's call after the pilot passes.
