# Wave A self-audit, 16 Sep 2026

An adversarial audit of my own sweep, run before trusting any number it produced. Four
defects were found in my first pass and fixed. Two real ledger defects were surfaced that
predate this work.

## Defects I found in my own sweep (all fixed)

1. CLOBBERED HUMAN VERDICTS. The first version wrote a machine verdict onto every row,
   including the 16 MTE rows that were hand-researched and web-verified. Fixed: FROZEN
   groups (mte, four-decks) are never touched. Verified no frozen row changed value.

2. CIRCULAR ETE MATCHING. A first fix fed the WHOLE paper text as the search string for
   every ETE row, so all rows matched the same boilerplate and reported "strong". That is
   a false positive by construction. Fixed: an ETE row searches only its own block, and
   falls back to unsearched when no block exists. Detected by eyeballing 16 "strong"
   verdicts and seeing them all cite the same phrases.

3. GENERIC PHRASES COUNTED AS EVIDENCE. "random variable probability density function"
   hits every book. Fixed: a phrase only counts when it hits the claimed source and NOT
   the other three corpora (distinctive matching). This dropped traced from 67 to 44, all
   of the drop being shared phrasing that was never real evidence.

4. EVIDENCE ACCUMULATION. The evidence_locator appended a new clause every run, so a row
   showed stale matches from earlier passes. Fixed: a fresh locator each run.

## Real ledger defects surfaced (predate this work, now recorded)

5. asgn 2024-25 #4 AND #5 ARE OUT OF MTE SCOPE. Both are hypothesis testing (t-test,
   F-test, type I/II errors, ANOVA). 40 rows were sitting in the ledger as pending. Now
   marked scope=OUT (a relabel, nothing deleted).

6. asgn 2024-25 #3 IS OUT OF SCOPE TOO. MLE, method of moments, Bayesian estimation, CI
   theory. 25 rows, now scope=OUT.

7. asgn-2024-25-3-ep2 IS AN EMPTY FILE. The extracted text is whitespace only. Its 25
   rows cannot be sourced. Acquisition needed before those rows mean anything.

8. OFF-BY-ONE in asgn 2024-25 #1. The source text numbers Q1 to Q16 (16 items); the
   ledger declares 15. Rows Q14/Q15 carry the text of source Q15/Q16. The ledger
   under-counts this assignment by one.

9. assignments-2025 (52 rows) DOUBLE-COUNTS the 2025-26 bundle. The group declares 52
   (24+28) but the single bundle file holds 19+36 for assignments 1 and 2. Five rows
   (asn2025-1-LONG-04, APP-01 to APP-04) have no counterpart in the bundle text. This is
   the same double-count PR14's report 19 flagged.

## The honest numbers after the audit

```
  rows                  383
  traced (source-level)  44    was 37 before, +7 real new matches
  family (shared only)   10
  unsearched            119    was 337
  open                  210
  scope OUT             125    (90 mine, 35 pre-existing ETE OUT)
```

Note the traced count DROPPED from the pre-audit 55/67 to 44 because the false positives
were removed. That is the correct direction: fewer, truer verdicts.

## Real new source matches (distinctive, verified against all four corpora)

```
  asn2024-1-Q14  verbatim  G&K  "a man with n keys wants to open his door"
  asn2024-2-Q05  strong    G&K  "in a book of 520 pages, 390 typographical errors"
  asn2024-1-Q08  strong    G&K  "positive real number, show the function ... probability"
  asn2024-2-Q11  strong    G&K  "a car hire firm has two cars"
  asn2025-1-SHORT-04 / asn2024-1-Q12  family  G&K  radio tube life
  asn2025-1-MCQ-03 / asn2024-1-Q03    family  G&K  electric cable 6x(1-x)
  + the two ETE strong, two ETE family
```

## What still blocks a full trace

```
  119 unsearched, in three buckets:
    74  the out-of-scope assignment rows (3, 3-ep2, 5, 4). No match expected.
    30  ppt/lms teaching rows with empty summaries. The decks use varied markers
        (Example N, Example N:, no marker) and the declared counts do not align
        cleanly, so these stay blank rather than force a bad alignment.
    15  ETE tail rows with no block in the dump.
```

The ETE tail and the teaching rows need a rebuilt extraction, which is wave A step 6
(separate from this sweep).

## Files

```
  scripts/sweep_provenance.py                      the engine, with all 4 fixes
  reports/21-WAVE-A-SWEEP.md                       the pass summary
  reports/22-WAVE-A-SELF-AUDIT.md                  this audit
  reports/evidence/wave-a-sweep-20260916.json      run record
  reports/evidence/question-instance-ledger.csv    updated
```

Repo tests: 43 of 43 pass, 383 rows. No em dashes.
