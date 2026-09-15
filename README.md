# mas2001-mte

Exam preparation repository for **MAS2001 Statistics and Probability**, Mid-Term Examination,
Manipal University Jaipur, B.Tech ECE Semester III, Section B, 2026-27.

Created 2026-09-13. MTE window: Friday 18 September to Friday 25 September 2026.
Paper: 30 marks, 90 minutes, closed book, all questions compulsory, calculator allowed.
Scope: lectures 1 to 21. Repo is private.

---

## Table of contents

1. [What this repo is](#1-what-this-repo-is)
2. [Quick start (pick your lane)](#2-quick-start-pick-your-lane)
3. [What is inside, folder by folder](#3-what-is-inside-folder-by-folder)
4. [The report set, annotated](#4-the-report-set-annotated)
5. [The question atlas, annotated](#5-the-question-atlas-annotated)
6. [The source corpus, annotated](#6-the-source-corpus-annotated)
7. [The conversion pipeline](#7-the-conversion-pipeline)
8. [Verification discipline](#8-verification-discipline)
9. [Known errata in the source material](#9-known-errata-in-the-source-material)
10. [Ground rules this repo keeps](#10-ground-rules-this-repo-keeps)
11. [Status and what comes next](#11-status-and-what-comes-next)

---

## 1. What this repo is

This is a single place that holds:

- **every source of MAS2001 on disk**, catalogued with sha256 in `sources.yaml`,
- **every slide converted to markdown with real LaTeX**, so the maths survives copy, grep
  and printing (the PDFs shatter equations in their text layers),
- **the full slide and question atlas**: what is in MTE scope, what each question tests, and
  every hidden subtopic the papers lean on,
- **verification evidence**: every numeric claim computed on the machine, with raw outputs
  kept verbatim, and every failure recorded rather than hidden.

The short version of why it exists: the subject material was scattered across three folders,
one whole block of lectures was missing from the obvious one, the PDFs' text layers destroy
equations, and the setter reuses question skeletons with new numbers. This repo fixes all
four problems in one place.

Read `CONTINUATION.md` first if you are starting a fresh session.

---

## 2. Quick start (pick your lane)

**If you are a new session picking up the work:**

```bash
cd ~/mas2001-mte
cat CONTINUATION.md          # state, queue, rules, verification checklist
cat INDEX.md                 # every file, one line each
```

**If you are studying (the actual point):**

```bash
# the whole picture
reports/02-MTE-REPORT.md     # start here: scope, weak spots, plan
reports/03-FORMULA-SHEET.md  # the closed-book sheet
reports/05-FIVE-DAY-PLAN.md  # day by day, plus the 14 Sep re-pin
reports/10-SLIDES-VS-SYLLABUS.md  # lecture by lecture: what exists, what is missing

# drilling
reports/04-QUESTION-BANK.md  # the corpus's own problems, verified answers
reports/07-MOCK-PAPER.md     # 30-mark mock, sit it closed book
reports/08-MOCK-SOLUTIONS.md # every number computed

# the deep map (the "no ambiguity" files)
reports/11-QUESTION-ATLAS/00-SYLLABUS-FULL-EXPANDED.md  # every topic to atomic facts
reports/11-QUESTION-ATLAS/00-TYPE-SPACE-AUDIT.md        # every question type, asked vs not
reports/11-QUESTION-ATLAS/00-MUTATION-ANALYSIS.md       # what value changes make a new type
reports/11-QUESTION-ATLAS/00-LEARN-PLAN.md              # what after what
```

**If you are processing the new batch (batch 2):**

```bash
reports/12-NEW-BATCH.md      # the 23-file list, 19-unit queue, per-unit protocol
# start at U01: the four MTE documents, 15 pages, one at a time
```

**If you are reading raw converted slides:**

```bash
md/<label>.md                # a whole deck in reading order
md/<label>/pNNN.md           # one slide, LaTeX for every equation
```

---

## 3. What is inside, folder by folder

```
mas2001-mte/
├── README.md                  this file
├── CONTINUATION.md            new-window entry point (read this first in a new session)
├── INDEX.md                   every file in the repo, one line each
├── sources.yaml               36 sources: absolute path, pages, sha256, topic, author.
│                              single source of truth; the pipeline reads it, nothing hardcodes
├── PROMPT.txt                 the transcription prompt (runtime: the scripts read it here)
├── process/                   how the pipeline was built
│   ├── BRIEF-001-conversion-pipeline.md    the brief for convert.py + assemble.py
│   ├── BRIEF-002-dash-and-robustness.md    the brief for the dash normalisation fixes
│   └── BRIEF-003-audit-and-fidelity.md     the brief for audit_conversion.py
├── scripts/
│   ├── convert.py             render each page to png, read with a vision model, cache,
│   │                          retry, log to manifest. resumable, stdlib only
│   ├── assemble.py            per-page markdown into one deck document, normalises dashes
│   └── audit_conversion.py    coverage audit + fidelity gate (second reader) + dash audit
├── md/                        the converted corpus: 348 pages across 11 labels (batch 1)
│   ├── INDEX.json             per label: pages, chars, done, flagged, dashes fixed
│   └── <label>/pNNN.md        one slide per file
├── work/                      pipeline state and evidence
│   ├── text/<label>.txt       pdftotext layer per source, the independent second channel
│   ├── manifest.jsonl         one record per page: sha256, status, latency, model, chars
│   ├── audit.jsonl            the coverage audit records
│   ├── AUDIT.md               coverage audit summary: per-label buckets, flagged pages
│   ├── FIDELITY.md            second reader agreement (11 PASS, 1 REVIEW, explained)
│   ├── summary and logs       run logs for full conversion, resume, fidelity
│   ├── archive/               superseded artifacts (void fidelity run, etc)
│   └── pages/                 page PNGs (gitignored)
└── reports/                   the report set (see section 4)
    ├── 00 to 10               numbered main reports
    ├── 11-QUESTION-ATLAS/     the deep question work (see section 5)
    ├── 12-NEW-BATCH.md        batch 2 inventory + processing queue
    ├── archive/               superseded reports, versioned, never deleted
    └── evidence/              raw verification outputs, verbatim
```

---

## 4. The report set, annotated

| file | what it is | read when |
|---|---|---|
| `00-SCOPE-AND-EXAM-FACTS.md` | exam facts (30 marks, 90 min, window, assessment split), every line sourced from a page on disk | to confirm scope |
| `01-COVERAGE-MAP.md` | every source page mapped to the lecture plan, plus gaps and duplication, with grep evidence | understanding what exists |
| `02-MTE-REPORT.md` | the main report: what is on disk, what is in scope, weak spots, risks, the plan | first read |
| `03-FORMULA-SHEET.md` | closed-book formula sheet, every line inside MTE scope, with worked corpus examples | revision core |
| `04-QUESTION-BANK.md` | the corpus's own problems with verified answers, organised by distribution | drilling |
| `05-FIVE-DAY-PLAN.md` | the day-by-day plan from 13 Sep, plus the 14 Sep evening re-pin | planning |
| `06-VERIFICATION.md` | three verification layers, the failures that were caught, adjustments visible | trust audit |
| `07-MOCK-PAPER.md` | 30-mark mock in the real format | self-test |
| `08-MOCK-SOLUTIONS.md` | every number computed and cross-checked against a slide | after the mock |
| `09-ERRATA.md` | 15 errors found in the source material, each with the computed value | before memorising anything |
| `10-SLIDES-VS-SYLLABUS.md` | lecture-by-lecture slides audit (8-9 half, 10-11 corrected 15 Sep) | coverage questions |
| `12-NEW-BATCH.md` | batch 2: 23 files catalogued, 19-unit processing queue, quality traps | batch 2 work |

---

## 5. The question atlas, annotated

Built over 14-15 September. The idea: classify every question in the corpus so the MTE
pattern is known, not guessed.

| file | what it is |
|---|---|
| `00-FRAMEWORK.md` | the entry schema (19 fields) and every taxonomy defined (Bloom revised, Webb DOK, MATH groups, SOLO, GAISE, Smith+Stein, variation theory, AIG radical/incidental) |
| `00-COUNT-REGISTER.md` | the locked counts: 112 items, 107 unique, exclusions explicit, deck 01 manifest of all 30 items |
| `00-SYLLABUS-FULL-EXPANDED.md` | every topic down to atomic facts, with page refs, values, traps (770 lines) |
| `00-MASTER-SYLLABUS.md` | the master map: scope table, hidden layer, errata map, inventory recap |
| `archive/00-TOPIC-TREE-v1.md`, `00-TOPIC-FLOW.md` | the v1 tree and the flow art (prerequisite edges, broken links, composite question map) |
| `00-TYPE-SPACE-AUDIT.md` | every question TYPE per topic: asked vs sibling vs hypothetical, with a self-audit |
| `00-MUTATION-ANALYSIS.md` | what changes make a new question type: radical vs incidental, the M0-M4 scale, new type nodes |
| `00-LEARN-PLAN.md` | the staged learn order (what after what), with gates per stage |
| `01-deck-lec01-09.md` | per-question entries for the 147-page deck (in progress, 2 of 30 done) |
| `archive/` | superseded versions (v1 tree etc), kept for the record |

---

## 6. The source corpus, annotated

Batch 1 (11 sources, 348 pages, fully converted):

| label | pages | what it is |
|---|---|---|
| `ppt3-discrete-prob-dist` | 28 | binomial, Poisson. Dr. Ashish Kumar |
| `ppt4-continuous-prob-dist` | 44 | uniform, normal, exponential |
| `ppt5-estimation-summary` | 26 | estimation, estimator properties |
| `lms-theory-of-estimation` | 40 | same estimation deck extended, + confidence intervals (out of scope) |
| `lms-standard-error-clt` | 19 | sampling, standard error, CLT |
| `lms-method-of-moments` | 11 | method of moments (out of MTE scope) |
| `lms-maximum-likelihood` | 16 | MLE (out of MTE scope) |
| `notes-lecture-series-01-09` | 147 | Dr. Vivek Singh, lectures 1 to 9, units 1-2 |
| `mas2001-course-handout` | 7 | assessment scheme, lecture plan with MTE tags |
| `mas2001-assignment-1` | 6 | question paper + official answer key |
| `mas2001-assignment-2` | 4 | second problem set |

Batch 2 (23 files catalogued in `sources.yaml`, plus 2 extra sources, processing queued):

- 5 slide decks: L1-7, L8-9, **L10-11 Chebyshev (the missing block)**, L12-13, L14-15
- 6 assignments: 2024-25 series (1,2,3,3-Ep2,4,5), one of which is the image-only scan, plus
  the 2025-26 combined set. All read 15 Sep:
  the 2024-25 assignments 1 and 2 and the 2025-26 assignments 1 and 2 are IN MTE scope (90
  question blocks, 36 with printed answers); assignments 3 onwards cover lectures 22+ and are
  out of scope. Detail in `reports/12-NEW-BATCH.md` section 6.1
- 11 papers: MTE 2024-25 + 2025-26 (both with solution schemes), ETE sem 3 and 4 (both
  years), summer, re-sessional (both semesters). 2 of the 11 are mark schemes, so 9 papers.
- 2 extra sources: `Assignment 2_MAS2001-2.pdf` (byte-identical to the batch-1 assignment-2
  source at sha 5ff197311b60) and `MAS2001-Assignment 1 .pdf` (a second EDITION of assignment 1:
  different faculty name, and a different pmf row in long Q2 that normalises to
  12k + 10k^2 = 1 instead of 9k + 10k^2 = 1, see errata 5.1)
- no further paper duplicates exist: every paper in ~/PS is a distinct file (sha-checked)

---

## 7. The conversion pipeline

Every page is rendered at 110 dpi and read by `xiaomi/mimo-v2.5` through `~/.local/bin/vision`.
Vision was required, not optional: the PDFs have text layers but they shatter every equation,
so the text layer is kept as an independent second channel for auditing.

```bash
python3 scripts/convert.py --dry-run                      # plan only: verify paths + shas
python3 scripts/convert.py --label ppt3-discrete-prob-dist --workers 8
python3 scripts/convert.py --workers 8                    # full run, resumable
python3 scripts/assemble.py                               # per-deck documents + INDEX.json
python3 scripts/audit_conversion.py                       # coverage audit
python3 scripts/audit_conversion.py --fidelity 12 --fidelity-model deepseek/deepseek-v4.1-flash
```

Properties:

- **resumable**: a killed run loses nothing; finished pages are skipped on re-run
- **provenance**: one manifest record per page (png sha256, status, attempts, latency,
  chars, model, timestamp)
- **audited**: every page gets a bucket (OK / MISSING_TEXT / NO_MATH / DASH / EMPTY) with
  the reason checkable against the raw text layer
- **second reader**: the fidelity gate re-reads 12 pages with a different model and compares
  the number sets; results and the void run are kept in `work/`

---

## 8. Verification discipline

Three layers, all with raw output kept:

1. **source identity**: every sha256 and page count recomputed against `sources.yaml`
2. **numeric**: 79 checks over every closed form in the formula sheet and the answer keys,
   raw output in `reports/evidence/verify-formula-sheet-20260913.txt`
3. **fidelity gate**: second reader over sampled pages (11 PASS, 1 REVIEW, artifact explained;
   the void pro-model run archived so its number is never cited)

Then the corrections layer: the first checker pass had 4 failing checks; all four were my
own thresholds, and the fixes are recorded in `06-VERIFICATION.md` because a gate that was
quietly loosened is worth less than one whose adjustments are visible.

---

## 9. Known errata in the source material

18 entries in `reports/09-ERRATA.md`. Highlights (16, 17 and 18 added 15 Sep by the
round-7 audit):

```
  insurance example            prints 0.1745, value 0.1755
  irregular die sets           prints 0.549, value 0.5499
  assignment 1 key            truncates 0.0915, value 0.0916
  exp slide p040               inverts the lambda wording (p041 corrects it)
  assignment 1 long Q2         normalisation root is 1/10 (9k + 10k^2 = 1)
  clt impurity                 prints Z = -0.4, must be -0.94
  ppt4 p030 figure             sigma label 10, real value 5.0
  assignment 2 B5              prints 0.5679, value 0.6225
  assignment 2 C2              prints mu 37.5; mu 37.2 is the consistent value
  assignment 1 long Q3         prints 0.808, both cases exactly 0.8
  assignment 1 app Q3          SD chain rounds twice (0.975/0.98 vs exact 0.97)
  deck bus example             integral bound contradicts its own event
  assignment 2 C3              last-digit rounding (0.8754 vs exact 0.8753)
  Chebyshev deck Q3            statement row and worked row disagree; page 8's displayed
                               template inverts the inequality (the deck's theorem slide is
                               correct). Variance and final bound are correct, errata 15
  tube key part (ii)           prints 2/3, value is 8/27, errata 16
  2024-25 A1 Q16 pmf row       sums to 0.9, not 1, errata 17
  mock B4 Note                 claims T4 smallest variance, it is third of four, errata 18
  normal notation note         N(mu, sigma^2), second slot is the variancevariance
```

Do not memorise the printed values; the computed ones are in the file.

---

## 10. Ground rules this repo keeps

- **No em dashes or en dashes** in any authored file. Enforced at the prompt and at assembly.
- **No invented URLs**, no invented content in any transcription. The prompt bans URLs.
- **Nothing deleted without approval.** Superseded files move to `archive/` and gain `-v1`
  style names. The trash is a place, not a process.
- **Every claim carries a page reference** that resolves to a file in `md/`.
- **Course-owned evidence only.** No external question banks: they pollute the question
  space with types this course never set. Method frameworks (taxonomies) come from research;
  question content comes from this course's own materials.
- **Corrections are visible.** When a claim flips (Chebyshev's deck arriving on 15 Sep), the
  old claim is not silently overwritten; it carries an inline CORRECTED note with the date.

---

## 11. Status and what comes next

**Batch 1: complete.** 348 pages converted, audited, verified; report set 00-10 written.

**Batch 2: catalogued, queued.** 23 files listed, 19 processing units at 10-20 pages each,
per-unit protocol defined (every page read, every question entered, dedup verdict, count,
log, commit). Starts at U01: the four MTE documents (paper + scheme, both years), 15 pages.

**The standing question the atlases answer:** can a value change make a new type? No (M0),
but inversion, re-conditioning, re-targeting and composition do (M1-M4), and the type space
audit lists every sibling already implied by this course's own papers.

**Next window:** read `CONTINUATION.md`, run the verification checklist, start U01.
