# mas2001-mte

Exam preparation repo for MAS2001 Statistics and Probability, Mid-Term Examination,
Manipal University Jaipur, B.Tech ECE Semester III, Section B, 2026-27.

Created 2026-09-13. MTE window: Friday 18 September to Friday 25 September 2026.
Paper: 30 marks, 90 minutes, closed book, all questions compulsory, calculator allowed.

## Read this first

```
  new session?        read CONTINUATION.md, then INDEX.md
  studying?           read reports/02-MTE-REPORT.md, then reports/03-FORMULA-SHEET.md
  processing batch 2? read reports/12-NEW-BATCH.md (list + 19-unit queue), then CONTINUATION.md
```

## Why this repo exists

The subject material was spread across folders, and the first batch was missing the
heaviest block. This repo brings every source into one place, converts every slide to
markdown so the maths survives, counts and classifies every question, states what is in
scope with evidence, and keeps a verified drill set (formula sheet, question bank, mock
paper, errata).

Batch 1 (13 Sep): 11 sources, 348 pages converted. Batch 2 (15 Sep): 23 more sources
arrived (papers, assignments, reorganized decks), 283 pages, queued for processing.

## Layout

```
  sources.yaml            36 sources: path, pages, sha256, topic. Single source of truth.
  PROMPT.txt              the transcription prompt, versioned (runtime file, stays at root)
  process/                the briefs handed to opencode for the pipeline (BRIEF-001..003)
  scripts/
    convert.py            render each page to png, read with vision, cache, retry, manifest
    assemble.py           per page markdown into one file per deck, normalises dashes
    audit_conversion.py   coverage audit and fidelity gate (second reader)
  md/<label>/pNNN.md      one slide per file, LaTeX for every equation, Figure: lines for charts
  md/<label>.md           assembled deck in reading order
  md/INDEX.json           per label stats including dashes normalised
  work/text/<label>.txt   pdftotext layer per source, the independent second channel
  work/manifest.jsonl     one record per page: png sha256, status, attempts, latency, chars, model
  work/archive/           superseded logs kept for the record
  reports/                the report set (see INDEX.md), reports/evidence/ raw output,
                          reports/archive/ superseded docs
  reports/11-QUESTION-ATLAS/   the question analysis set (see INDEX.md)
```

## The pipeline, quickly

```
  python3 scripts/convert.py --dry-run                     # plan only, verify sources and shas
  python3 scripts/convert.py --workers 8                   # full run, skips finished pages
  python3 scripts/assemble.py                              # per deck documents and INDEX.json
  python3 scripts/audit_conversion.py                      # coverage audit
  python3 scripts/audit_conversion.py --fidelity 12        # second reader fidelity gate
```

Every page is rendered at 110 dpi and read by `xiaomi/mimo-v2.5` through
`~/.local/bin/vision`. Vision is required, not optional: the PDFs have text layers but
they shatter every equation. The pipeline is resumable and records a sha256 per page.

## Ground rules this repo keeps

- No em dashes or en dashes in any file. Enforced at the prompt and again at assembly.
- No invented URLs, no invented content in any transcription.
- Nothing deleted without approval. Superseded files move to `archive/`, never away.
- Every claim about the material carries a page reference that resolves to a file in `md/`.
- Course-owned evidence only. External question banks are banned as sources (they would
  inject question types this course never asked).
