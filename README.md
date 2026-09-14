# mas2001-mte

Exam preparation repo for MAS2001 Statistics and Probability, Mid-Term Examination,
Manipal University Jaipur, B.Tech ECE Semester III, Section B, 2026-27.

Created 2026-09-13. MTE window: Friday 18 September to Friday 25 September 2026.
Paper: 30 marks, closed book. Scope: lectures 1 to 21.

## Why this repo exists

The subject material was spread across three folders and one of them was missing the
heaviest block. `~/PS` holds the estimation and limit theorem decks plus the two
distribution decks, which is lectures 12 to 21. Lectures 2 to 11 (probability theory, random
variables, expectation, variance) exist only in a 147 page deck in
`~/muj-academics/handouts/`. This repo brings every source into one place, converts every
slide to markdown so the maths survives, and states what is in scope with evidence.

Read `reports/02-MTE-REPORT.md` first. It is the summary and it cites everything else.

## Layout

```
  sources.yaml            the 11 sources: path, page count, sha256, topic. Everything is derived from this
  PROMPT.txt              the transcription prompt, versioned, bans invented URLs and em dashes
  BRIEF-001..003.md       the briefs given to the opencode CLI to build the pipeline
  scripts/
    convert.py            render each page to png, read it with vision, cache, retry, log to manifest
    assemble.py           per page markdown into one file per deck, normalises dashes
    audit_conversion.py   coverage audit (did we miss anything) and fidelity gate (second reader)
  md/<label>/pNNN.md      one slide per file, LaTeX for every equation, Figure: lines for every chart
  md/<label>.md           assembled deck in reading order
  md/INDEX.json           per label stats including dashes normalised
  work/text/<label>.txt   pdftotext layer per source, the independent second channel
  work/manifest.jsonl     one record per page: png sha256, status, attempts, latency, chars, model, url flag
  work/AUDIT.md           coverage audit result
  work/FIDELITY.md        second reader agreement result
  reports/                the report set, numbered, plus reports/evidence/ raw output
```

## The reports

```
  00  exam facts and scope, every line sourced
  01  coverage map, source page to lecture, plus the gaps
  02  the main report: what is on disk, what is in scope, weak spots, risks, plan
  03  formula sheet, closed book, every line inside MTE scope
  04  question bank, the corpus's own problems with verified answers
  05  five day plan, 13 to 17 September, plus the 14 September re-pin
  06  verification record, all three layers, with the failures that were caught
  07  mock MTE paper, 30 marks, same shape as the real one
  08  mock worked solutions, every number computed
  09  errata found in the source material, at the claim site where possible
  10  slides vs the MTE syllabus, lecture by lecture, with the two real gaps
  evidence/  raw verification output, copied verbatim
```

## The sources

```
  label                        pages  what it is
  ppt3-discrete-prob-dist         28  binomial and Poisson, Dr. Ashish Kumar
  ppt4-continuous-prob-dist       44  uniform, normal, exponential
  ppt5-estimation-summary         26  estimation, estimator properties (subset of lms-theory)
  lms-theory-of-estimation        40  same estimation deck, extended, plus confidence intervals
  lms-standard-error-clt          19  sampling, standard error, central limit theorem
  lms-method-of-moments           11  method of moments, OUT of MTE scope
  lms-maximum-likelihood          16  maximum likelihood, OUT of MTE scope
  notes-lecture-series-01-09     147  Dr. Vivek Singh, lectures 1 to 9, the units 1 and 2 block
  mas2001-course-handout           7  assessment scheme and the lecture plan with MTE tags
  mas2001-assignment-1             6  question paper plus the official answer key
  mas2001-assignment-2             4  second problem set
  ---------------------------------------------------------------------------------
  total                          348
```

Nothing was moved or deleted. The two duplicate decks and the duplicated PPT files elsewhere
on disk are listed as YOUR-CALL items in the report, not touched.

## How the conversion works

Every page is rendered at 110 dpi and read by `xiaomi/mimo-v2.5` through
`~/.local/bin/vision`. Vision was required, not optional: the PDFs have text layers but they
shatter every equation, so the text layer is kept only as an independent check. The pipeline
is resumable, so a killed run loses nothing, and it records a sha256 per page image.

```
  python3 scripts/convert.py --dry-run                     # plan only, verify sources and shas
  python3 scripts/convert.py --label ppt3-discrete-prob-dist --workers 8
  python3 scripts/convert.py --workers 8                   # full run, skips finished pages
  python3 scripts/assemble.py                              # per deck documents and INDEX.json
  python3 scripts/audit_conversion.py                      # coverage audit
  python3 scripts/audit_conversion.py --fidelity 12        # second reader fidelity gate
```

## Ground rules this repo keeps

- No em dashes or en dashes in any file. Enforced at the prompt and again at assembly.
- No invented URLs, no invented content in any transcription.
- Nothing deleted without approval.
- Every claim about the material carries a page reference that resolves to a file in `md/`.
