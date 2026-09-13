# BRIEF 003: conversion audit and fidelity gate

Owner: Hermes. Implementer: opencode CLI. Repo: /home/liebert511/mas2001-mte

Build one tool, `scripts/audit_conversion.py`, standard library only, that answers two
questions with evidence: did the conversion miss anything, and can a second reader agree
with the first.

## Part 1: coverage audit (default mode)

For every label in `sources.yaml`, for every page present in `md/<label>/pNNN.md`:

1. Read the page markdown.
2. Extract that page's own PDF text layer with `pdftotext -layout -f N -l N <pdf> -`.
3. Compute and record:

```
  label, page, md_chars, textlayer_chars, ratio (md/textlayer, textlayer > 0),
  latex_inline (count of "$"), display_math (count of "$$"), figure_lines (count of lines starting "Figure:"),
  banned_url (any of example.com, ](http, https://), dashes (any of U+2014, U+2013),
  empty (md file missing or zero bytes)
```

4. Flag a page into one of these buckets, first match wins:

```
  EMPTY           md missing or empty
  MISSING_TEXT    textlayer_chars > 250 and ratio < 0.5
  NO_MATH         textlayer contains "=" or a greek letter and md has zero "$"
  BANNED_URL      banned_url true
  DASH            dashes true
  OK              none of the above
```

5. Write `work/audit.jsonl`, one JSON object per page, and `work/AUDIT.md` containing:
   - a per label table: pages, OK, EMPTY, MISSING_TEXT, NO_MATH, BANNED_URL, DASH
   - a section listing every non OK page with its label, page, bucket, and the two char counts
   - a headline line: total pages, total flagged, percentage flagged

Exit code 0 if total EMPTY is zero, else 1. Nothing else may fail the run.

## Part 2: fidelity gate (`--fidelity N`)

1. Choose N pages at random from the converted set, deterministic by `--seed` (default 20260913),
   sampling across labels rather than within one label.
2. Re-read each chosen PNG with a different reader model than the primary:
   `--fidelity-model xiaomi/mimo-v2.5-pro` by default, calling the same
   `/home/liebert511/.local/bin/vision` CLI, prompt from `PROMPT.txt`.
3. Save the second reading to `work/fidelity/<label>/pNNN.md`. Skip if it already exists.
4. Compare the two readings and record per page:
   - numeric token agreement: pull every number-like token from each reading with a regex,
     count how many of the primary's numeric tokens also appear in the second reading,
     as a fraction
   - `Figure:` count in each
   - whether the second reading independently produced a `## ` title
5. Write `work/FIDELITY.md`: per page, label, page, numeric agreement, figure counts, and a
   PASS or REVIEW verdict (PASS when numeric agreement is at least 0.8).

## Constraints

- Python 3 standard library only, absolute paths, no cwd reliance.
- No em dashes or en dashes anywhere in the code, comments, or output.
- Idempotent and resumable: a second run must not redo finished fidelity reads.
- Do not modify `md/`, `sources.yaml`, `PROMPT.txt`, or `scripts/convert.py`.
- Do not run the full audit yet, that is Hermes's call after the conversion finishes.

## Acceptance

```
python3 -c "import ast; ast.parse(open('scripts/audit_conversion.py').read())"
python3 scripts/audit_conversion.py --help
```

Report the file created, its line count, and any deviation from this brief.
