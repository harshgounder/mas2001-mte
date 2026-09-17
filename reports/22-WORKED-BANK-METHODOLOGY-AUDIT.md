# Worked-bank methodology audit, 17 Sep 2026

## Result

This pass corrected stale counts, prediction overclaims, and confirmed formula errors in the
worked-bank index, methodology note, drill, and decision manual. F1-F15 were not edited AT THE
TIME OF THE ORIGINAL PASS; a follow-up extension then corrected 10 of those files (F1, F2, F5,
F6, F7, F8, F9, F10, F11, F12), and their corrected text is included in this commit.

## Count reconciliation

| count | unit | audit result |
|---:|---|---|
| 160 | literal `QUESTION` headers | includes pointer-only headers and omits MCQs stored only in tables |
| 179 | solved-content items | content-level ledger after expanding embedded material and removing pointer-only or repeated content |
| 183 | source-question units | splits worked blocks that combine several numbered source questions |
| 168 | prior drill units | did not expose the 12 F13 Section A MCQs as drill entries |
| 180 | current drill units | prior drill plus those 12 MCQs, with pointers to the F13.1 answer table |

The header count is mechanically reproducible:

```sh
rg '^QUESTION ' deck/worked/F*.md | wc -l
```

The content and source-unit totals are ledger counts, not grep counts. The rules differ
because tables can contain several solved items, pointers are not fresh solutions, and some
worked blocks combine more than one numbered source question.

## Paper wording

The inspected exam set has nine papers total: two MTE papers and seven ETE-family papers.
Earlier wording that said "two MTE papers" plus "nine ETE sittings" overstated the corpus.

## Category status

The decision manual lists 16 in-MTE categories and 20 recall-gap categories, 36 total. This
is a working study taxonomy. It is not evidence that the question space contains exactly 36
forms, that all forms have been found, or that a future paper must fit the checklist.

## Prediction-method limits

The available material does not support a calibrated future-paper success percentage:

- only two MTE papers are available;
- the seven ETE-family papers cover a broader syllabus;
- assignments and decks are not independent exam outcomes;
- repeats and near-duplicates make raw frequency counts dependent;
- retrospective representation of known papers is not an out-of-sample backtest.

Accordingly, this audit removes or qualifies claims of a 100 percent backtest, exhaustive
coverage, guaranteed marks, exact future-topic probabilities, and complete machine checking.

## Mathematical corrections in the decision manual

- corrected the adjacent-binomial ratio for `P(X=5)=2P(X=4)`;
- corrected the Poisson probability equation and removed the invalid rate 10 root;
- described the five-minute Poisson example as five Bernoulli interval events, not a
  Poisson count used as the binomial trial count;
- corrected the Poisson capacity example from rate 3 to rate 2.5;
- replaced an invalid exponential survival ratio with the correct lower-tail ratio;
- corrected the uniform mean/variance and inverse-bound examples;
- replaced the universal `n>30` CLT rule with a course-heuristic warning;
- corrected the claim that both "at least" and "at most" must use a complement;
- marked confidence intervals as outside the stated MTE lecture boundary and stated the
  distribution or approximation conditions for z and t intervals;
- corrected the category labels from 14 plus 20 and 34 total to 16 plus 20 and 36 total.

## Files covered

```text
deck/worked/00-INDEX.md
deck/worked/00-HOW-AND-WHY.md
deck/worked/00-QUESTIONS-ONLY.md
deck/15-DECISION-MANUAL.md
reports/22-WORKED-BANK-METHODOLOGY-AUDIT.md
```
