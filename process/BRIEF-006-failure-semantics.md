# BRIEF 006: conversion failure semantics

Owner: Codex, auditor. Implementer: opencode CLI. Repo: `/home/liebert511/mas2001-mte`.

Four new regression tests expose four real failure paths in `scripts/convert.py`. All four
fail on the current branch. Make the smallest source change that makes them pass.

## Scope

Modify only `scripts/convert.py`. Do not edit tests, docs, converted markdown, the manifest,
or any other file. Do not commit or push. Standard library only. Do not use em or en dashes.

Run this before and after:

```
python -B -m unittest -v \
  tests.test_pipeline_audit.TranscribeExitChecks.test_truncation_retry_uses_second_exit_code \
  tests.test_pipeline_audit.FailureSemanticsChecks
```

Starting result: 4 tests fail.

## Required behavior

### F1: use the second retry's return code

In `transcribe`, the longer truncation retry is classified with the first call's return code.
Capture the second call's return code and pass it to `_read_status`. If the second call raises,
use a nonzero synthetic return code. The test expects a second exit code of 9 to yield
`exit_9`, not `ok`.

### F2: never reuse a stale final PNG after a failed render

`render_page` removes numbered intermediate PNGs but leaves the final `png_path`. A failed
forced render can therefore pass the final `is_file()` check using an image from an older run.
Remove the final target before invoking `pdftoppm`, and require both a zero process return code
and a newly produced numbered PNG. A failure must raise `RuntimeError`.

### F3: non-ok text must not overwrite verified markdown

`process_page` currently writes any nonempty stdout even when `transcribe` returns `exit_1`,
`truncated`, or another non-ok status. Write markdown only when status is exactly `ok`.
Return `done=True` only for status `ok` with nonempty text. Keep the failed text length and
status in the manifest so the failure remains inspectable.

### F4: failed pages must make the command fail

After processing, `main` prints failed counts but returns zero unless a source was skipped.
Return nonzero when any summary row has `failed > 0`. Keep the existing nonzero behavior for
skipped sources.

## Acceptance

1. The four focused tests pass.
2. `python -B -m unittest -v tests.test_pipeline_audit` passes all 34 tests.
3. `git diff --check` passes.
4. `git status --short` shows only the pre-existing untracked `work/opencode/`, the new tests
   and brief written by Codex, and your change to `scripts/convert.py`.
5. Report the exact source diff and test results. Do not commit.
