# 00 INDEX: the map

## THE WHOLE FOLDER AS A MAP

```
                         MAS2001 MTE ULTRA DECK
                                 │
        ┌────────────────────────┼────────────────────────┐
        │                        │                        │
   ┌────▼─────┐            ┌─────▼──────┐          ┌──────▼──────┐
   │ NOTES/   │            │ REFERENCE  │          │  STUDY      │
   │ (learn)  │            │ (lookup)   │          │  (do)       │
   └────┬─────┘            └─────┬──────┘          └──────┬──────┘
        │                        │                        │
   11 files, full          cheatsheet, terms,      LEARN-ORDER,
   slide rewrites          methods, numbers,       drill set,
   10 chapters             patterns, traps,        exam mechanics
                           distributions
        │                        │                        │
        └────────────────────────┼────────────────────────┘
                                 ▼
                        READ IN THIS ORDER:
                        1. 14-MASTER-STUDY-ORDER
                        2. notes/00-NOTES-INDEX
                        3. notes/01 .. notes/10
                        4. reference as you solve
```

## THE COURSE SPINE, TOP TO BOTTOM

```
   T1 course intro (not examined)
    │
   T2 probability foundations  ──── counting engine ──┐
    │        sets, events, axioms, C(n,r)             │
    ▼                                                 │
   T3 random variables                                │
    │        discrete | continuous | Bernoulli        │
    ▼                                                 │
   T4 pmf / pdf / cdf  ◀─────────────────────────────┘
    │
    ├──────────┬──────────┐
    ▼          ▼          ▼
   T5         T6      distribution shelf
   EXPECTATION VARIANCE  │
    │          │     ┌───┴────┬────────┬────────┐
    │          │     ▼        ▼        ▼        ▼
    │      T6H indep T8 BINOM T9 POIS T10-12 CONT
    │      E(XY)                  │      unif/norm/exp
    │          │                  │
    │          ▼                  │
    │      T7 CHEBYSHEV ◀─────────┘
    │          │
    ▼          ▼
   T13 SAMPLING + STANDARD ERROR  (SE = σ/√n, needs T6)
    │
    ▼
   T14 CLT  ◀── T11 normal supplies the destination
    │
    ▼
   T15 ESTIMATION BASICS  (point vs interval)
    │
    ▼
   T16 ESTIMATOR PROPERTIES  (unbiased/consistent/efficient)
```

## THE HIDDEN LAYER, ON THE SPINE

```
   the nodes the slides UNDER-TAUGHT but the papers ASK:

   T6 ──[H1 independence rules]──▶ T7, T14, T16   <- gates 3 topics
   T7 ──[H2 Chebyshev]───────────▶ graded 9+ times
   T12 ─[H3 memoryless]──────────▶ A2 MCQ5, A2 C1
   T11 ─[H4 68/95/99.7]──────────▶ A2 MCQ11
   T5 ──[H5 N x P count]─────────▶ A1 app, A2 B4, A2 D1
   T3 ──[H6 geometric 1/p]───────▶ A1 short4
   T3 ──[H7 hypergeometric nK/N]─▶ A1 long3
   T11 ─[H8 two table conventions]▶ every normal/CLT numeric

   = the cheapest marks on the paper. See notes/10 + 11-BEYOND-SLIDES.
```

## 1. What the MTE is

```
  paper       MAS2001 Statistics and Probability, mid term
  marks       30
  scope       lectures 1 to 21 (the 16 syllabus lines below)
  shape       Section A MCQ (a few marks each), Section B short answers,
              Section C longer. All compulsory.
  closed book so the sheet below must be in your head
  calculator is allowed on both supplied MTE papers
```

## 2. The 16 syllabus lines and where each is taught

```
  #   syllabus line                                    lecture   file
  1   Introduction of the Course                          1      md/notes-lecture-series-01-09 p001-011
  2   Basic terminology and concepts of probability        2      notes p012-050
  3   Random variables (discrete, continuous)             3-4     notes p051-062, p112
  4   PMF, pdf, CDF                                       5-6     notes p063-087, p112-139
  5   Expectation of random variables                      7      notes p088-094, p140-147
  6   Expectation and Independent random variables        8-9     notes p095-111 (indep rules: hidden, 11)
  7   Chebyshev's inequality                             10-11    deck L10-11 (9 pages)
  8   Binomial distribution                               12      md/ppt3 p001-018
  9   Poisson distribution                                13      md/ppt3 p019-028
  10  Uniform distribution (continuous)                   14      md/ppt4 p001-006
  11  Normal distribution                                 15      md/ppt4 p007-037
  12  Exponential distribution                            16      md/ppt4 p038-043
  13  Sampling concepts, standard error                   17      md/lms-standard-error-clt p001-019
  14  Central limit theorem                               18      md/lms-standard-error-clt p006-018
  15  Theory of estimation: parameter, statistic,
      point and interval estimation                       19      md/ppt5 p001-007, lms-theory p001-015
  16  Characteristics of a good estimator                20-21    md/ppt5 p008-021, lms-theory p016-030
```

## 3. The 16-topic tree (full detail in 05 and 10)

```
  T1  course intro (not examined)
  T2  probability foundations: sets, events, axioms, counting, conditional, independence
  T3  random variables: definition, discrete, continuous, functions of an rv
  T4  pmf, pdf, cdf: conditions, build, read, invert
  T5  expectation: definition, E[h(X)], linearity, expected count
  T6  variance: definition, shortcut, transforms; independent rvs (E(XY), Var of sum)
  T7  Chebyshev: tail form, complement form, k extraction, apply, inverse
  T8  binomial
  T9  Poisson
  T10 uniform
  T11 normal
  T12 exponential
  T13 sampling and standard error
  T14 central limit theorem
  T15 estimation basics
  T16 estimator properties
```

## 4. The learning order (why, and the evidence)

The batch-2 S&P decks are re-teaches, proved by shared-phrase counts:

```
  L1-7   vs notes deck   1,129 shared 5-grams (54 percent of the smaller)
  L8-9   vs notes deck     456 shared (55 percent)
  L12-13 vs ppt3           874 shared (53 percent), same pens numbers 0.2301, 0.2824, 0.3766
  L14-15 vs ppt4           630 shared (40 percent)
  L10-11 vs notes deck      12 shared (2 percent)   <- the only genuinely new deck
```

So the order is: Chebyshev and the hidden layer first (nothing else teaches them, they gate
four downstream topics), then the main theory, with each S&P re-teach used as the second pass
on its topic, then the papers, then the assignments.

```
  PASS 0  Chebyshev deck + independence rules + the hidden set + formula sheet   1h40
  PASS 1  notes p012-087 (foundations, rvs, pmf/cdf) + its questions             3h
  PASS 2  notes p088-147 (expectation, variance) + S&P L1-7 and L8-9 questions   3h15
  PASS 3  binomial, Poisson, uniform, normal, exponential + their re-teach blocks 4h
  PASS 4  sampling and CLT + questions                                            2h
  PASS 5  estimation (ppt5 full, lms-theory 2 items only) + questions             2h30
  PASS 6  mock paper, closed book, timed, then mark it                            3h
  PASS 7  MTE papers, then assignments, then ETE IN blocks                        several days
  PASS 8  sheet, landmarks, hidden set, traps, from memory                       last day
```

Full per-question sequencing: `../reports/11-QUESTION-ATLAS/00-LEARN-ORDER.md`.

## 5. The counts you can trust (as of 16 Sep 2026)

```
  base branch ledger                 383 instances
  assignment-bundle addition         119 instances on PR 14
  combined enumerated total          502 instances after PR 14 is merged
  MTE source/family leads             10 of 16 blocks
  MTE generic concept checks           5 of 16 blocks
  MTE open composite                   1 of 16 blocks
  content family ids                   0 of 502 rows, dedup remains unfinished
  exam papers on disk                 10   (2 MTE + 5 ETE + 2 re-sess + 1 summer)
  marking schemes on disk              2   (kept separate from exam-paper count)
```

The 16 MTE blocks have all been searched. “Searched” is not the same as “traced”. A generic
definition match is not evidence that a question was copied from a particular source.

## 6. The hidden layer, one line each (full detail in 11)

```
  H1  independence rules of rvs: E(XY), Var(X+Y), Var(X-Y)      no teaching slide
  H2  Chebyshev entire topic                                     taught only in the L10-11 deck
  H3  memoryless property of the exponential                     no slide
  H4  the 68.27 / 95.45 / 99.73 landmarks                        no slide
  H5  expected count, N x P                                      no slide
  H6  geometric mean 1/p                                         no slide
  H7  hypergeometric mean nK/N                                   no slide
  H8  two normal table conventions (phi vs F)                    no slide
```
