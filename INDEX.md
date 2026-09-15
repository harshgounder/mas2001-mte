# INDEX: every file in this repo, one line each

Built 15 September 2026. If a file is not on this list, it does not exist (audit rule).

Coverage rule: the 348 `md/<label>/pNNN.md` page files are covered by their directory line,
and `work/text/<label>.txt` plus `work/fidelity/<label>/pNNN.md` are covered by their
directory lines and by `work/manifest.jsonl`, so they are not listed one by one. Every
other tracked file appears below by name.

## Root

```
  README.md               what this repo is, layout, pipeline, ground rules
  CONTINUATION.md         new-window entry point: state, queue, next moves
  INDEX.md                this file
  sources.yaml            36 sources (11 batch 1 + 23 batch 2 + 2 extras), sha256 each
  PROMPT.txt              transcription prompt (runtime, read by scripts)
  .gitignore              work/pages, work/*.png, pycache
```

## process/

```
  BRIEF-001-conversion-pipeline.md    the build brief for convert.py + assemble.py
  BRIEF-002-dash-and-robustness.md    fix brief: dashes + failure modes
  BRIEF-003-audit-and-fidelity.md     the build brief for audit_conversion.py
```

## scripts/

```
  convert.py              PDF -> png -> vision -> per-page md, resumable, manifest
  assemble.py             per-page md -> per-deck document + INDEX.json, dash normalise
  audit_conversion.py     coverage audit + fidelity gate (second reader model)
```

## md/ (348 batch-1 pages converted; batch-2 conversion pending)

```
  notes-lecture-series-01-09/   147p  Dr. Vivek Singh deck, lectures 1-9 (batch 1)
  ppt3-discrete-prob-dist/       28p  binomial + Poisson (batch 1)
  ppt4-continuous-prob-dist/     44p  uniform, normal, exponential (batch 1)
  ppt5-estimation-summary/       26p  estimation (batch 1)
  lms-theory-of-estimation/      40p  estimation extended (batch 1)
  lms-standard-error-clt/        19p  sampling, SE, CLT (batch 1)
  lms-method-of-moments/         11p  MoM, OUT of MTE (batch 1)
  lms-maximum-likelihood/        16p  MLE, OUT of MTE (batch 1)
  mas2001-course-handout/         7p  assessment scheme, lecture plan (batch 1)
  mas2001-assignment-1/           6p  assignment + key (batch 1)
  mas2001-assignment-2/           4p  second set (batch 1)
  (assembled .md + INDEX.json at md/ root)
  Batch-2 sources are in sources.yaml, not yet converted; conversion is queue U01-U19.
```

## work/

```
  text/                   11 pdftotext layers (batch 1), the independent second channel
  manifest.jsonl          one record per converted page (batch 1)
  audit.jsonl             coverage audit records
  AUDIT.md, FIDELITY.md, SUMMARY.md        run outputs, all batch 1
  FIDELITY-void-pro-404.md                the void first fidelity attempt (archived reason)
  fidelity-run-deepseek.log               the real fidelity run (11 PASS + 1 REVIEW)
  fidelity-run-pro-404.log                the void pro-model run log (nothing cites it)
  fidelity/<label>/pNNN.md                the 12 second-reader readings, kept per page
  run-full-1.log, run-resume-verify.log   conversion run logs
  atlas-census.jsonl      the 348-page question-marker census (atlas input)
  archive/                superseded logs (fidelity-run-void-original.log)
  fidelity/, pages/       second readings; page images (gitignored)
```

## reports/ (batch-1 report set; corrections of 15 Sep are in-line, marked CORRECTED)

```
  00-SCOPE-AND-EXAM-FACTS.md    exam facts, scope, every line sourced
  01-COVERAGE-MAP.md            source page -> lecture map, gaps (Chebyshev corrected)
  02-MTE-REPORT.md              the main report (Chebyshev section corrected 15 Sep)
  03-FORMULA-SHEET.md           closed-book sheet, MTE scope only
  04-QUESTION-BANK.md           corpus problems with verified answers
  05-FIVE-DAY-PLAN.md           13-17 Sep plan + 14 Sep re-pin
  06-VERIFICATION.md            verification record, three layers
  07-MOCK-PAPER.md              mock MTE, 30 marks
  08-MOCK-SOLUTIONS.md          mock worked solutions
  09-ERRATA.md                  15 errata, at the claim site
  10-SLIDES-VS-SYLLABUS.md      lecture-by-lecture slides audit (Chebyshev corrected)
  12-NEW-BATCH.md               THE batch-2 doc: list + 19-unit processing queue + scout findings
  evidence/                     raw verification output
                                (verify-formula-sheet-20260913.txt = the 79-check run)
  archive/12-NEW-BATCH-SCOUT-v1.md   superseded by 12-NEW-BATCH.md
```

## reports/11-QUESTION-ATLAS/ (the question analysis set)

```
  00-FRAMEWORK.md            entry schema, taxonomy definitions, method
  00-COUNT-REGISTER.md       locked counts: 112 items / 107 unique (batch 1), manifests
  00-MASTER-SYLLABUS.md      the master tree: topics, hidden layers, errata map
  00-SYLLABUS-FULL-EXPANDED.md   deepest tree, atomic facts, all 21 lecture slots
  00-TOPIC-FLOW.md           prerequisite edges, cross-links, broken links, composites
  00-MUTATION-ANALYSIS.md    radical vs incidental: which changes make new types
  00-TYPE-SPACE-AUDIT.md     full method inventory per topic + sibling matrix
  00-LEARN-PLAN.md           the staged study plan (Stage 0-7)
  01-deck-lec01-09.md        deck-01 entries (D1-Q001, D1-Q002 written; census done)
  evidence/                  pixel-forensics crops for the bus-example errata
                             (p127-f-digit-crop.png, p129-f-line-crop.png)
  archive/00-TOPIC-TREE-v1.md    superseded by 00-MASTER-SYLLABUS.md
```

## State summary (15 Sep 2026)

```
  batch 1: converted, audited, fidelity-gated, counted, classified. 112 items / 107 unique.
  batch 2: listed, hashed, in sources.yaml. Nothing converted yet. 19-unit queue in
           reports/12-NEW-BATCH.md. START HERE in a new window: queue U01.
  corrections applied 15 Sep: Chebyshev has a deck (S&P L10-11); siblings confirmed by
           real papers (14 items, see 12-NEW-BATCH.md section 6); exam format known now.
```
