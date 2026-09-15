# CONTINUATION: new window entry point

Written 15 September 2026, ~09:45 IST. If you are a fresh session: read this file fully,
then INDEX.md, then start at section 5 (the order of work). Verify everything you rely on
before acting (section 7).

## 1. Where things stand

```
  repo            ~/mas2001-mte, github.com/harshgounder/mas2001-mte (PRIVATE), branch master
  batch 1         11 sources fully processed: converted (348p), audited, fidelity-gated,
                  counted (112 items / 107 unique), classified, reports 00-10 written
  batch 2         23 sources arrived 15 Sep, listed + hashed in sources.yaml, NOT converted.
                  The 19-unit processing queue is in reports/12-NEW-BATCH.md.
  corrections     Chebyshev has slides (S&P L10-11); 14 "not asked" siblings are confirmed
                  asked by real papers; exam format decoded from both MTE papers.
  deadline        17 Sep 2025 was last year's MTE date; THIS year's window: Fri 18 to Fri 25
                  Sep 2026. Sitting day per subject not yet known (user knowledge item).
```

## 2. The one big correction (do not propagate the old claim)

Earlier reports said "Chebyshev has no slides anywhere". That was true of batch 1 only.
Batch 2 contains `~/PS/S&P L10-11 Chebyshev's inequality.pdf` (9 pages): theorem, k-sigma
restatement, complement form, two worked questions. Its Q2 is MTE 2025-26 Q5 verbatim
(mu=10, sigma^2=4, find C with P(|X-10|>=C) <= 0.04). All affected reports (01, 02, 03, 04,
08, 10, atlas files) carry inline CORRECTED notes as of 15 Sep. If any other file still
says "no slides" for Chebyshev, it is stale: report it.

## 3. What the past papers proved (batch 2 scout, details in reports/12-NEW-BATCH.md s6)

```
  - 14 siblings previously listed as "not asked" ARE asked in real papers (Var(X-2Y),
    E(XY) MCQ, Chebyshev find-C, bound-vs-actual, exp interval, uniform wait, n=9 normal,
    sufficiency MCQ, consistency-with-bias, SE direction, statement-spotting, k from
    E(X),E(X^2), Var(2X-5Y), exp mean-and-var).
  - exam format: 30 marks, 90 min, ALL compulsory, calculator allowed,
    "missing data may be assumed suitably", sections A (MCQ 2mk) B (4mk) C (8mk combined),
    useful phi/z values printed in the paper.
  - re-sess and ETE papers re-use the same skeletons (pens question appears again in ETE).
```

## 4. The batch-2 queue (19 units, 10-20 pages each, one at a time)

Full list with page ranges in reports/12-NEW-BATCH.md section 3. Order:

```
  U01  MTE 2025-26 paper + scheme + MTE 2024-25 paper + scheme       15p  START HERE
  U02  ETE S3 x2 + re-sess S3                                         6p
  U03  ETE S4 x2 + summer + re-sess S4                                9p
  U04  2025-26 assignments 1-5 combined                              17p
  U05  2024-25 assignments + Episode 2 (Ep2 is image-only, vision)   15p
  U06  Chebyshev deck (critical, 9p)                                  9p
  U07-U08  L12-13 split (check dup vs ppt3)                       15+13p
  U09-U11  L14-15 split (check dup vs ppt4)                      15+15+14p
  U12-U13  L8-9 split                                             19+18p
  U14-U19  L1-7 split (check overlap vs 147p deck)                 18p x6
```

Per-unit protocol (mandatory, this is how "nothing missed" is enforced): read every page;
give every question a full entry per reports/11-QUESTION-ATLAS/00-FRAMEWORK.md schema;
give every page a dedup verdict vs the existing corpus (NEW / DUPLICATE / UPDATED); update
counts; append the unit summary to a processing log; commit. Scan-heavy files (both MTE
schemes, Assignment 3 Episode 2) need a vision pass, no skipping.

## 5. Order of work for the new window

```
  1  read this file, INDEX.md, reports/12-NEW-BATCH.md (10 min)
  2  verify claims: git log --oneline -5, sources.yaml parses (34 sources), repo clean
  3  U01: process the four MTE documents (15 pages, one at a time) -> log -> commit
  4  U02..U06 in order; stop after each unit for user review if the user is present
  5  after the papers + assignments + Chebyshev deck: rebuild the atlas type space with
     CONFIRMED vs HYPOTHETICAL siblings (00-TYPE-SPACE-AUDIT.md gets the real evidence)
  6  then the decks U07-U19 (dedup verdicts decide whether they replace or join batch-1 md/)
  7  finally: update 09-ERRATA (schemes may add entries), 05-FIVE-DAY-PLAN (exam format
     now known), 07-MOCK-PAPER (reshape to the real A/B/C format), and 13-PROCESSING log
```

New files expected: `reports/13-PROCESSING-LOG.md` (created at U01), `md/` entries for
batch-2 sources (labels already reserved in sources.yaml).

## 6. Rules that bind this repo (do not relearn the hard way)

```
  - course-owned evidence only. NEVER fetch external question banks as "what setters ask"
    (user order 15 Sep: they pollute the space with questions this course never asked).
    Method-framework research (isomorphs, AIG, variation theory) was fine and is done.
  - no em dashes anywhere. No AI-tell vocabulary. User persona rules apply to all output.
  - nothing deleted without per-item approval; superseded -> archive/.
  - every page reference must resolve to a file in md/.
  - the MTE scope is lectures 1-21. MoM, MLE, Bayesian, CI mechanics, hypothesis tests,
    ANOVA: OUT. Do not let batch-2 papers drag out-of-scope work into scope, but DO note
    where ETE papers touch lecture 22+ content for later planning.
  - watermark caveat: batch-2 PDFs carry mujstella.in reseller watermarks; filter during
    extraction, they are not course content.
```

## 7. Verification checklist (run before trusting anything)

```
  git -C ~/mas2001-mte log --oneline -5            # see the real HEAD
  git -C ~/mas2001-mte status --porcelain          # clean tree expected
  python3 -c "import sys; sys.path.insert(0,'~/mas2001-mte/scripts'); from convert import
    parse_sources_yaml; _, s = parse_sources_yaml(open('~/mas2001-mte/sources.yaml').read());
    print(len(s))"                                  # expect 36 (11 + 23 batch-2 + 2 extras)
  ls ~/PS | wc -l                                  # 33 files total in ~/PS
  find ~/PS -maxdepth 1 -newermt '2026-09-15 00:00' -type f | wc -l   # 23 batch-2 arrival
  grep -c 'CORRECTED' ~/mas2001-mte/reports/*.md   # the 15 Sep corrections are in place
```

Note on the two extras found during the 15 Sep hygiene pass: `Assignment 2_MAS2001-2.pdf`
is byte-identical to batch-1's assignment-2 source (provenance kept, no conversion needed);
`MAS2001-Assignment 1 .pdf` is a faculty variant of assignment 1 (same questions, faculty
name differs: Dr. Ruchika Mehta vs Dr. Vivek Singh). Both are logged in sources.yaml.

## 8. Open items inherited

```
  YOUR-CALL    1  ~/MUJ byte-identical PPT3/4/5: keep or remove (deletion needs approval)
               2  ~/Music/MAS2001_remake August pipeline: untouched, out of scope
               3  subject-wise MTE sitting day: only the window is known
               4  mujstella.in watermarks: reseller mark on batch-2 PDFs, nothing to do
  PENDING      5  Google OAuth refresh token dead -> Drive sweep still blocked
               6  fidelity gate: run again after batch-2 conversion (deepseek reader)
               7  count register update after U04/U05 (assignment counts will grow)
               8  mock paper reshape to real A/B/C format (after U01)
```

## 9. Key file map (quick)

```
  reports/12-NEW-BATCH.md        batch-2 list + queue + scout findings  <- read after this
  reports/11-QUESTION-ATLAS/     all question analysis (framework, counts, trees, plans)
  reports/02-MTE-REPORT.md       main summary of batch-1 work
  reports/05-FIVE-DAY-PLAN.md    the study plan (will be re-pinned with real format)
  reports/09-ERRATA.md           15 errata, claim-site recorded
  md/<label>/pNNN.md             converted slides (batch 1 complete; batch 2 pending)
  work/manifest.jsonl            per-page provenance for everything converted
```
