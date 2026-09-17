# Deck and notes audit, 16 Sep 2026

## Purpose

This report audits the 27 Markdown files under `deck/`, including the 11 files under
`deck/notes/`. It checks mathematical statements, exam facts, corpus counts, provenance
language, scope boundaries, internal links, and study usability.

This is a checkpoint, not a claim that corpus-wide source matching is complete. The 502 gross
instances still need content-family ids and per-item source verdicts.

## Evidence boundary

```
   official fact         supplied handout or exam paper
          |
   checked result        recomputation or audit report with evidence
          |
   source lead           similar or matching external problem family
          |
   concept check         generic definition or standard result
          |
   open                  no source attribution established
```

These states must not be merged. In particular, a concept check does not identify the source
of a question, and enumeration does not establish either uniqueness or provenance.

## Corrected in this checkpoint

| area | defect | correction |
|---|---|---|
| MTE provenance | deck claimed 15 of 16 blocks were traced | now reports 10 source or family leads, 5 concept checks, 1 open composite |
| corpus accounting | mixed 383, 456, and 502 denominators | now separates the 383-row base ledger from the 119-row PR 14 addition and the 502 combined gross count |
| paper inventory | claimed 15 papers while listing 11 files and mixing schemes with papers | now reports 9 exam papers and 2 marking schemes |
| calculator rule | claimed calculators were limited to arithmetic | both supplied MTE papers explicitly allow calculators |
| machine-life item | labelled M25-Q7 as exponential | corrected to a normal sample-mean problem, matching Walpole Problem 8.25 |
| normal notation | wrote `N(8,5)` while calculations treated 5 as the standard deviation | now states mean 8 and sd 5, or equivalently `N(8,25)` |
| CLT | treated 30 as a universal theorem boundary | now labels 30 as the course heuristic and requires shape or tail justification for small non-normal samples |
| dependence | said a dependent-variable product question could not be asked | now preserves the covariance or joint-distribution route |
| CDF boundaries | used one ambiguous formula for open intervals | now separates continuous and integer-valued cases |
| sufficiency | described it only as “uses all information” | now gives the parameter-free conditional-distribution meaning and factorisation test |
| mortality density | placed `x exp(-x/3)/9` under exponential drills | now identifies it as gamma-shaped, not exponential |
| confidence interval | mixed a lecture-25 mechanics problem into the MTE drill without a boundary | now marks the item as boundary material and states the normality or approximation assumption |
| mutation claims | claimed every question is copied and every paper fits five distributions | now limits the statement to confirmed matches and keeps foundations, Chebyshev, estimation, and mixed models outside the nine-slot grid |
| study entry point | README pointed first to the older atlas order | now points first to `deck/14-MASTER-STUDY-ORDER.md` |
| external sources | heading said every source was in the repo | now marks `~/mas2001-devore/` as an external reference layer |

## Second-pass mathematical corrections, 17 Sep

| area | defect | correction |
|---|---|---|
| estimator algebra | wrote `E(T3)=lambda*mu` for `(lambda*X1+X2+X3)/3` | corrected to `((lambda+2)/3)mu`; the unbiased value remains `lambda=1` |
| consistency | treated one sample mean at fixed `n=3` as proof of consistency | now distinguishes the fixed statistic from the sequence `Xbar_n` |
| Chebyshev Q1 | replaced the source event `-2<X<8` with a different radius | restored radius 5 and the `21/25` lower bound |
| binomial Chebyshev event | equated `80<=X<=120` with a strict absolute-value event | corrected to `abs(X-100)<=20` |
| normal tables | reversed the page 22 cumulative table and page 23 centre-area table | page labels and notation now match the converted sources |
| impurity probability | repeated the slide's `0.1644` arithmetic error | rounded table values give `0.1645`; unrounded z values give about `0.1637` |
| distribution support | omitted the outside-support CDF branches for uniform and exponential | restored the piecewise branches and clipped uniform intervals to their support |
| Poisson recognition | treated equal mean and variance as sufficient proof of a Poisson law | now states it is necessary, not sufficient |
| discrete CDF | used `F(a-1)` based only on integer endpoints | now requires an integer-valued random variable |
| dice maximum CDF | wrote `F(m)=m^2/36` for every real `m` | restricts that formula to integer support points and uses `floor(m)^2/36` between them |
| drill constants | printed `0.2424`, `e^-1`, `n=22`, and `n=35` without the parameters that determine them | supplied the missing parameter where known and removed unsupported fixed answers |
| study timing | four pass and fallback labels disagreed with their listed minutes | labels now match the arithmetic or state the review reserve |

## Confirmed exam facts

The two supplied MTE papers support these facts:

```
   marks             30
   duration          90 minutes
   questions         all compulsory
   calculator        allowed
   observed shape    3 x 2 marks, 4 x 4 marks, 1 x 8 marks
```

The course handout supports closed-book status and lectures 1 to 21 as the MTE scope. The
observed section shape is evidence from two papers, not a promise that every future paper will
use the same topics.

## Current accounting truth

```
   base question-instance ledger       383
   assignment bundle on PR 14          119
                                      ----
   combined gross instances            502

   content-family ids assigned           0
   unique-question total             unknown
   corpus-wide sourced percentage    unknown
```

PR 14 now carries reviewed summaries and the 62 in-scope, 7 boundary, 50 out-of-scope
split. Per-row year-over-year source matching remains unfinished.

## Remaining audit work

1. Assign a stable content-family id to all 502 rows, then compute the deduplicated count.
2. Give every row one source state: exact, strong family, weak lead, concept only, open, or not
   searched.
3. Finish line-level numerical recomputation of the 50-item drill and every worked example in
   the 10 teaching-note chapters.
4. Verify every “no slide” and “hidden” label against the full source page ledger, not only the
   converted text search.
5. Review PR 14's still-unassessed year-over-year matches. Its item-level scope and all 17
   layout-split summaries are now corrected and production-validated.
6. Continue broad source searching for the rain plus binomial composite, the pens problem,
   and the remaining open four-deck blocks. Similarity is a lead until the originating source
   or a strong family match is established.

## Audit status

```
   inventory and file map             complete for deck tree
   known cross-file contradictions    corrected in this checkpoint
   MTE fact and provenance wording    corrected in this checkpoint
   targeted mathematical defects      corrected in this checkpoint
   every worked number recomputed     in progress
   502-row provenance matching        in progress
   deduplication by content family    not started
```

Do not describe this audit as finished until the final three lines are closed.
