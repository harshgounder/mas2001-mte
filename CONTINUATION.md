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
                  The 19-unit processing queue is in reports/12-NEW-BATCH.md. U01 NOT started.
  corrections     Chebyshev has slides (S&P L10-11); 14 "not asked" siblings are confirmed
                  asked by real papers; exam format decoded from both MTE papers.
  round 7         a peer codex audit (15 Sep 14:45) plus my own re-verification added errata
                  16, 17 and 18, corrected 5.2 and 15, retracted a false duplicate row and
                  fixed the in-scope drill total to 90. Evidence committed, 24 checks pass.
                  Its 6 pipeline findings and the 2 stale vision defaults are OPEN, code,
                  awaiting an explicit go.
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
  U04  2025-26 assignments 1-5 combined, A1+A2 ONLY (~8p in scope)   17p
  U05  2024-25 assignments 1 and 2  (IN SCOPE, PROMOTED 15 Sep)       4p
  U05b 2024-25 assignments 3, 3-Ep2, 4, 5 (OUT of MTE scope)         11p  <- do last
  U06  Chebyshev deck (critical, 9p)                                  9p
  U07-U08  L12-13 split (check dup vs ppt3)                       15+13p
  U09-U11  L14-15 split (check dup vs ppt4)                      15+15+14p
  U12-U13  L8-9 split                                             19+18p
  U14-U19  L1-7 split (check overlap vs 147p deck)                 18p x6
```

SCOPE CORRECTION 15 Sep, read section 6.1 of reports/12-NEW-BATCH.md before U04/U05: the
2024-25 assignment 1 and 2 cover lectures 1-11 and 12-18, which are IN MTE scope. The old
plan had all of U05 as out-of-scope revision. They are in fact 35 fresh in-scope question
blocks, and the 2025-26 set adds 55 more (36 of them with printed answers). Total new MTE
drill from the assignment files: 90 blocks. U05 is promoted ahead of the ETE papers.

~/PS now holds 34 files, of which 32 are sources.yaml entries (the other two are
`.directory` and `syllabus.txt`, which is the MTE syllabus in text form). The 36 sources
resolve across ~/PS (32), ~/Videos (1) and ~/muj-academics (3). Duplicates, sha-verified on
15 Sep, are exactly two and no more: `asgn-copy-2025-26` in ~/PS is byte-identical to
`mas2001-assignment-2` in ~/Videos (sha 5ff197311b60), and `lms-standard-error-clt`'s "(1)"
twin, moved to the trash on 14 Sep, is byte-identical to it (sha e48f4981ed69). An earlier
revision of this file claimed three extra paper copies plus an extras count of six; those
files do not exist on disk and the claim is retracted. `MAS2001-Assignment 1 .pdf` is a
second EDITION, not a duplicate: different faculty name and a different pmf row.

Per-unit protocol (mandatory, this is how "nothing missed" is enforced): read every page;
give every question a full entry per reports/11-QUESTION-ATLAS/00-FRAMEWORK.md schema;
give every page a dedup verdict vs the existing corpus (NEW / DUPLICATE / UPDATED); update
counts; append the unit summary to a processing log; commit. Scan-heavy files (both MTE
schemes, Assignment 3 Episode 2) need a vision pass, no skipping.

## 5. Order of work for the new window

```
  1  read this file, INDEX.md, reports/12-NEW-BATCH.md (10 min)
  2  verify claims: git log --oneline -5, sources.yaml parses (36 sources), repo clean
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
  ls ~/PS | wc -l                                  # 34 files in ~/PS (33 belong to this repo's
                                                   # corpus; the count is checked loosely)
  find ~/PS -maxdepth 1 -newermt '2026-09-15 00:00' -type f | wc -l   # 24 arrivals since 15 Sep (23 are batch-2)
  grep -c 'CORRECTED' ~/mas2001-mte/reports/*.md   # the 15 Sep corrections are in place
  python3 -B ~/mas2001-mte/reports/evidence/verify-audit-round7-20260915.py
                                                   # expect ALL CHECKS PASS, 24 checks:
                                                   # errata 16-18, the counts, the false
                                                   # duplicate row, the Chebyshev text layer
```

Note on the extras found during the 15 Sep hygiene pass. `Assignment 2_MAS2001-2.pdf` is
byte-identical to batch-1's assignment-2 source (sha 5ff197311b60, provenance kept, no
conversion needed); it is NOT the assignment-1 copy (that is sha 2ab4f651), checked 15 Sep.
`MAS2001-Assignment 1 .pdf` is a second edition of assignment 1: faculty name Dr. Ruchika
Mehta (batch-1 copy is Dr. Vivek Singh) AND a different long-Q2 pmf row, p(x) = k, 2k, 2k,
3k, 3k, k^2, 2k^2, 7k^2 + k, which normalises to 12k + 10k^2 = 1 with root 0.0782, where the
batch-1 row (0, k, 2k, 2k, 3k, k^2, 2k^2, 7k^2 + k) gives 10k^2 + 9k = 1 with root 1/10. Its
key column prints different digits, so it is a compare-and-keep at U05, not a dedup. An
earlier revision of this note also claimed three byte-identical paper repeats in ~/PS with
"(1)" and "(2)" suffixes: those files do not exist on disk and the claim is retracted. Both
extra sources are logged in sources.yaml.

## 8. Open items inherited

```
  YOUR-CALL    1  ~/MUJ byte-identical PPT3/4/5: keep or remove (deletion needs approval).
                  CONFIRMED REAL 15 Sep: sha256 of all three match the ~/PS copies exactly
                  (9cc7f631, b3de25d8, 2af21af1). It is a genuine duplicate set, not a
                  near-copy.
               2  ~/Music/MAS2001_remake August pipeline: untouched, out of scope
               3  subject-wise MTE sitting day: only the window is known
               4  mujstella.in watermarks: reseller mark on batch-2 PDFs, nothing to do.
                  NOTE 15 Sep: the Chebyshev deck carries a DIFFERENT reseller tag,
                  MSV1RXZXSVM3TK2VFV6K, which also appears in every batch-2 assignment and
                  paper text layer. Same class of mark, two different tags, filter both.
  PENDING      5  Google OAuth refresh token dead -> Drive sweep still blocked
               5b the Chebyshev deck (S&P L10-11) DOES have a text layer: 3453 non-space
                  characters, page 8 extracts in full, real embedded fonts, watermark
                  MSV1RXZXSVM3TK2VFV6K. CORRECTED 15 Sep; item 5b previously said
                  "0 chars, pypdf vector", which was false (see errata 5.2).
               5c errata 15: the Chebyshev deck's Q3 slide states one distribution and works
                  another (real defect, now proven from the text layer), and page 8's
                  DISPLAYED template line inverts the inequality. CORRECTED 15 Sep: the
                  deck's theorem slide states both standard forms correctly, so an earlier
                  note calling its k-sigma form "not the standard form" was itself wrong
                  and is retracted. The printed variance and the final bound are internally
                  consistent. Q1 and Q2 are sound and Q2 is the official MTE 2025-26 Q5.
                  Teach from Q1/Q2, treat Q3 as mis-transcribed.
               6  the second edition of assignment 1 (asgn-faculty-variant) is internally
                  broken: its own row gives k = 0.0782 while its key prints k = 1/10.
                  Full transcription and a question-by-question comparison are owed at U05
               7  fidelity gate: run again after batch-2 conversion (deepseek reader)
               8  count register update after U04/U05: the in-scope assignment corpus grows
                  by 90 blocks (15 + 20 + 19 + 36), more than the 52 already counted.
                  CORRECTED 15 Sep: 90, not 91; 2024-25 A1 has 15 blocks, not 16.
               9  DONE 16 Sep: mock v2 uses the real 3x2, 4x4, 8-mark A/B/C structure.
                  The original mock remains as the v1 content drill.
```

## 9. Key file map (quick)

```
  reports/12-NEW-BATCH.md        batch-2 list + queue + scout findings  <- read after this
  reports/11-QUESTION-ATLAS/     all question analysis (framework, counts, trees, plans)
  reports/02-MTE-REPORT.md       main summary of batch-1 work
  reports/05-FIVE-DAY-PLAN.md    the study plan (will be re-pinned with real format)
  reports/09-ERRATA.md           18 errata, claim-site recorded
  md/<label>/pNNN.md             converted slides (batch 1 complete; batch 2 pending)
  work/manifest.jsonl            per-page provenance for everything converted
```
