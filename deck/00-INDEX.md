# 00 INDEX: the map

## 1. What the MTE is

```
  paper       MAS2001 Statistics and Probability, mid term
  marks       30
  scope       lectures 1 to 21 (the 16 syllabus lines below)
  shape       Section A MCQ (a few marks each), Section B short answers,
              Section C longer. All compulsory.
  closed book so the sheet below must be in your head
  no calculators beyond arithmetic, so numbers are chosen to be clean
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
  instances in the ledger            383 pushed, 502 once the 119-item bundle lands
  traced with a source               37   (20 named/verbatim, 12 lead only, 5 concept check)
  open (verdict logged, no source)    9   (1 MTE composite C1, 8 four-deck blocks)
  unsearched                         337 / 456
  5 of 5 distributions covered, 0 of 502 rows carry a content family id yet
  papers on disk                     15   (2 MTE + 2 schemes + 5 ETE + 2 re-sess + 1 summer)
```

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
