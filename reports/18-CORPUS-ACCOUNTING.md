# Corpus accounting: every question we hold, as of 16 Sep 2026

Counting rule: same as the count register (one block per numbered question, example or
exercise; multi-part counts once; display-only illustrations do not count). This report
extends the register beyond its "MTE scope only" frame: it counts ALL question blocks we
hold, with scope notes, because the user asked for the complete count.

## Exact counts (enumerated, reproducible from disk)

| # | corpus | pages | blocks | basis |
|---|---|---|---:|---|
| 1 | notes-lecture-series-01-09 | 147 | 30 | locked register |
| 2 | ppt3-discrete-prob-dist | 28 | 6 | locked register |
| 3 | ppt4-continuous-prob-dist | 44 | 7 | locked register |
| 4 | lms-standard-error-clt | 19 | 5 | locked register |
| 5 | ppt5-estimation-summary | 26 | 5 | locked register |
| 6 | lms-theory-of-estimation | 40 | 7 (2 unique) | locked register |
| 7 | L10-11 Chebyshev deck | 9 | 3 | text layer, counted 16 Sep (Q1, Q2, Q3) |
| 8 | assignment 2025-26 #1 | 6 | 24 | locked register |
| 9 | assignment 2025-26 #2 | 4 | 28 | locked register |
| 10 | MTE papers 2024-25 + 2025-26 | 5 question pages | 16 | locked register |
| 11 | ETE, summer, re-sess papers (7 papers) | 15 | 97 | report 17, counted 16 Sep |
| 12 | assignment 2024-25 #1, #2, #3, #3-ep2, #4, #5 | 15 | 125 | counted 16 Sep (15+20+25+25+16+24) |
| 13 | S&P L1-7 / L8-9 / L12-13 / L14-15 decks | 217 | 30 | page and block audit, 16 Sep (13+4+6+7) |
| | TOTAL GROSS INSTANCES | | 383 | |

Note on row 12: converted by the parallel working session; counted read-only from its
working tree (uncommitted at the time of writing). The total is a gross count of question
instances. Row 5 and row 6 alone contain five duplicated problem families, so 383 must not
be described as a deduplicated content count. Removing only that verified overlap gives an
upper bound of 378 content families before the remaining cross-corpus duplicates are
resolved.

## Deck recount and pending enumeration

The four lecture decks were fully read in the evening pass; their rows below carry final
counts. The 2025-26 assignment bundle (#3 to #5) remains as near-duplicate material.

| corpus | pages | estimate | note |
|---|---|---:|---|
| S&P L1-7 deck | 108 | 13 | page audit: 13 blocks, including two image-based blocks missed by text-marker counting |
| S&P L8-9 deck | 37 | 4 | page audit: bus waiting-time pdf, CDF-to-pdf, hospitalization E(Y), Pareto moments |
| S&P L12-13 deck | 28 | 6 | page audit: 5-coin, pens problem, irregular die, Poisson examples 1 to 3 |
| S&P L14-15 deck | 44 | 7 | page audit: uniform example; two standard-normal examples; two N(8,5) probability examples; inverse 20% cutoff; exponential 15/hr |
| 2025-26 assignment bundle #3, #4, #5 | (17-page bundle) | ~65 | near-duplicate sets of the 2024-25 assignments; spot checks match |
| lms-MLE (out of scope) | 16 | ~6 | labeled examples, out of MTE syllabus |
| lms-MOM (out of scope) | 11 | unlabeled | not counted by rule |

Key finding: all of these PDFs carry clean text layers. The vision conversion pipeline is
not required for most text, but it is required to verify image-based blocks that the text
layer omits. The earlier marker-only pass missed three such blocks. The four decks are now
read (30 blocks). Only the bundle's #3 to #5
(~65 near-duplicate blocks) remains from this table.

## Totals

- Exact gross instances enumerated now: 383 blocks (353 from the daytime pass plus 30 from the four
  lecture decks read in the evening pass).
- Pending: the 2025-26 assignment bundle #3 to #5, about 65 blocks, near-duplicates of the
  2024-25 sets (spot checks match on airframes, Bayes, hotel rates).
- Corpus-wide: 383 exact gross instances now; adding the bundle's near-duplicate ~65
  arrives at roughly 448 gross. A net unique-content total is not yet defensible. The only
  current bound is at most 378 after removing the five verified row-5/row-6 overlaps, and
  it will fall as the remaining duplicate families are mapped.

## MTE-scope running figure (what the current study pool can draw on)

128 gross instances (U01 lock: 60 teaching + 52 assignments + 16 papers) + 56 IN from the ETE intake
(+3 boundary, +3 partial) + the in-scope part of the 2024-25 assignments (probability and
distribution sets #1 and #2, 35 blocks, plus estimation-property parts of #3) + the 30
blocks from the four decks read tonight (all four decks are MTE-syllabus material)
= roughly 250 to 260 gross usable instances. The unique-content count remains pending.

## Known duplicates

- asgn-copy equals assignment-2 (sha-verified earlier).
- SE/CLT trash "(1)" twin (sha-verified earlier).
- 2025-26 assignment bundle #3 to #5 versus 2024-25 #3, #3-ep2, #4, #5: same sets
  recycled across years; spot checks show minor wording edits.
- L-deck questions versus notes/PPT decks: overlap not yet assessed (ledger pass).

These duplicates are present in the gross total above. They are listed here so a later
content-family ledger can remove them once, with evidence, rather than mixing gross and
net figures.

## Rules held

1. External sources (Devore, Gupta and Kapoor, Palaniammal, Sundarapandian and any web
   found material) are a reference layer only. They never enter the corpus, the question
   bank, or any md/ page. Provenance mapping points; it does not import.
2. This accounting counts OUR material only: course slides, our assignments, our papers.
3. All numbers above are reproducible from the files named; the pending rows carry
   estimates and are labeled as such.

---
Report 18, added 16 Sep 2026.
