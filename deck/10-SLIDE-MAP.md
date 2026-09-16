# 10 SLIDE MAP: every page to topic to question

## THE SLIDE MAP AS A PICTURE

```
   notes-lecture-series-01-09  (147 pages)

   p001├──p011  INTRO (no questions)
   p012├──p022  what statistics is
   p023├──p030  experiments, sample space, events
   p031├──p040  set algebra, Venn, axioms
   p041├──p050  ┌── D1-1 tournament
                ├── D1-2 laptops
                ├── D1-3 basketball
                └── D1-4 camera
   p051├──p062  D1-5 .. D1-10   (Bernoulli, coins, dice, geometric, car)
   p063├──p087  D1-11 .. D1-18  (pmf, cdf, boards, dice max, proof)
   p088├──p094  D1-19 .. D1-21  (E, E[aX+b], the p094 triple)
   p095├──p111  D1-22 .. D1-25  (freezer, magazine, f=2x, cond)
   p112├──p139  D1-26 .. D1-28  (bus triangle, cdf exercise, F->f)
   p140└──p147  D1-29, D1-30    (hospital, Pareto)

   ppt3 (28pp)  ═══ p001-018 BINOMIAL ═══ p019-028 POISSON
   ppt4 (44pp)  ═══ p001-006 UNIFORM ═══ p007-037 NORMAL ═══ p038-043 EXP
   clt  (19pp)  ═══ p001-005 SAMPLING ═══ p006-018 CLT
   ppt5 (26pp)  ═══ p001-021 ESTIMATION ═══ p022-025 numerics
   lms-th (40pp)═══ p001-030 in scope ═══ p031-040 OUT (skip)
```

## WHICH SLIDE CARRIES WHICH EXAMINABLE ITEM

```
   ┌─────────────────────┬──────────────────────────┐
   │ the exam asks...    │ the slide that teaches it │
   ├─────────────────────┼──────────────────────────┤
   │ event probability   │ notes p041-p050           │
   │ pmf / cdf build     │ notes p063-p087           │
   │ E and Var           │ notes p088-p111           │
   │ continuous pdf/cdf  │ notes p112-p147           │
   │ binomial            │ ppt3 p001-p018            │
   │ Poisson             │ ppt3 p019-p028            │
   │ uniform             │ ppt4 p001-p006            │
   │ normal              │ ppt4 p007-p037            │
   │ exponential         │ ppt4 p038-p043            │
   │ SE and CLT          │ clt p001-p018             │
   │ estimation          │ ppt5 p001-p021            │
   │ Chebyshev           │ L10-11 deck (NOT notes!)  │
   │ everything in H1-H8 │ NOTHING (the hidden layer)│
   └─────────────────────┴──────────────────────────┘
```

Page refs are the pipeline page numbers (md/<label>/pNNN.md), which match the PDF page order.

## notes-lecture-series-01-09 (147 pages) = lectures 1 to 9

```
  pages        topic                                          questions there
  p001-011     course intro, syllabus, books                  none
  p012-022     what statistics is, importance, limitations    none examinable
  p023-030     random experiment, sample space, events        display examples only
  p031-040     event algebra, Venn, axioms, rules             none (setup for p041+)
  p041-042     tournament, 4 parts                            D1-1
  p043-045     counting, permutations, combinations           theory
  p046-047     laptops and desktops, 4 parts                  D1-2
  p048-049     basketball lineup, 2 parts                     D1-3
  p050         camera conditional probability                 D1-4
  p051-062     random variables: Bernoulli, counting rv,
               dice sum, two coins, geometric, car life      D1-5..D1-10
  p063-087     pmf, cdf: conditions, find k, build, graphs    D1-11..D1-18
  p088-094     expectation: def, E[h], linearity              D1-19..D1-21
  p095-111     variance: def, shortcut, transforms            D1-22..D1-25, D1-26 (bus triangle)
  p112-139     continuous: pdf, cdf, F'=f, piecewise          D1-26..D1-28
  p140-147     continuous expectation and variance            D1-29, D1-30
```

Detail on the pages that carry the graded skeletons:

```
  D1-1   p041-042  tournament outcomes 16
  D1-2   p046-047  laptops/desktops
  D1-3   p048-049  basketball lineup
  D1-4   p050      camera conditional
  D1-5   p052      Bernoulli coin
  D1-6   p053      two coin X
  D1-7   p054-055  dice sum pmf
  D1-8   p056      two coin Y
  D1-9   p057-059  geometric N + verify sum = 1
  D1-10  p060      car lifetime
  D1-11  p065      gas station pumps (NO solution)
  D1-12  p066      k probability function (key in A1 long 2)
  D1-13  p067-069  tune-ups
  D1-14  p070-071  contractor forms
  D1-15  p072-073  flashlight batteries
  D1-16  p080-081  boards inspection
  D1-17  p082-083  dice maximum M
  D1-18  p085      cdf nondecreasing proof
  D1-19  p089      die roll E(X)
  D1-20  p093      prove E[aX+b]
  D1-21  p094      E(X), E(X^2), E(2X+1)^2
  D1-22  p107-108  freezer dealer 4 parts
  D1-23  p109-111  magazine orders
  D1-24  p124-125  f(x)=2x verify + P(X<1/2)
  D1-25  p126      continuous conditional 5/12
  D1-26  p127-129  bus waiting 6 parts (errata 13)
  D1-27  p138      two cdfs exercise (NO solution)
  D1-28  p139      distribution function to density (NO solution)
  D1-29  p142      hospitalization E(Y)
  D1-30  p146-147  Pareto pdf 5 parts
```

Pages with NO countable question (do not hunt): p012, p017, p021, p115-116, p133, p136,
plus the boundary "display examples" on p023-027 (random experiment / sample space / mutually
exclusive / independence illustrations).

## ppt3-discrete-prob-dist (28 pages) = lecture 12 binomial, 13 Poisson

```
  p001-018   binomial: derivation, conditions, pmf, moments, pens, irregular die
     p002-007   5-coin derivation, the C(5,3)=10
     p011       recognition checklist
     p013-016   pens B(12,0.1) three parts
     p017-018   irregular die, p=5/8, expected count 0.5499
  p019-028   Poisson
     p022       Poisson as binomial limit
     p025       ratio P(X=1)=0.2P(X=2), l=10
     p026       telephone calls 2/min, THE NESTING 0.00145
     p027       insurance 5000 men, 0.1755 (errata 1)
     p028       tail P(X>2)=0.8753
```

## ppt4-continuous-prob-dist (44 pages) = lecture 14 uniform, 15 normal, 16 exponential

```
  p001-006   uniform: density, moments, length ratio, clipping, |X| intervals
  p007-037   normal
     p010-011   changing mu shifts, changing sigma widens
     p017       Z=2.0 worked
     p027       symmetry facts
     p029-031   P(X<8.6) mu=8 sigma=5, Z=0.12, 0.5478 (p030 figure errata 8)
     p032-033   P(X>8.6)=0.4522
     p034-037   inverse 20 percent tail -> 3.792
  p038-043   exponential
     p040       rate/mean wording inverted (errata 4)
     p041       correct mu = 1/lambda
     p042-043   arrivals 15/hour, P(T<3min)=0.5276
```

## lms-standard-error-clt (19 pages) = lectures 17 to 18

```
  p001-005   population vs sample, parameters vs statistics, SE = sigma/sqrt(n)
     p005       lightbulb SE, n=25 -> 20, n=100 -> 10
  p007-010   the three rules, n=30 boundary
  p011-012   ATM wait, mu=4, sigma=2, n=36, Z=1.50, 0.0668
  p013-014   impurity, mu=4.0, sigma=1.5, n=50, 0.1644 (errata 6, Z2=-0.94)
  p015-016   LED, mu=50000, sigma=8000, n=64, Z=-2.00, 0.0228
  p017-018   machine, normal population, n=9 exact, 0.6898
```

## ppt5-estimation-summary (26 pages) = lectures 19 to 21

```
  p001-007   parameter, statistic, estimator vs estimate, point vs interval
  p008-014   unbiased, force-unbiased, consistency, efficiency, sufficiency
  p015-018   comparison set 1 (t1, t2, t3; lambda 0; t1 wins)
  p019-021   comparison set 2 (T1, T2, T3; T3 wins)
  p022-025   response time 205 ms, packets 0.93, battery CI (boundary)
```

## lms-theory-of-estimation (40 pages)

```
  p001-015   estimation basics (same as ppt5 p001-007, the re-teach)
  p016-030   estimator properties (the 2 UNIQUE items: sufficiency examples, Poisson sum,
             exponential xbar)
  p031-040   confidence interval block, OUT OF MTE SCOPE, do not study
```

## The batch-2 S&P decks (not in md/, text in ~/mas2001-devore/corpus-text/)

```
  L1-7   (108 pp)  re-teach of the notes deck; 13 question blocks
  L8-9   (37 pp)   re-teach; 4 blocks (bus pdf, CDF-to-density, kidney E(Y), Pareto)
  L10-11 (9 pp)    CHEBYSHEV, the only new deck; Q1 and Q2 safe, Q3 mis-transcribed
  L12-13 (28 pp)   re-teach of ppt3; 6 blocks, same pens numbers
  L14-15 (44 pp)   re-teach of ppt4 + McClave; 7 blocks
```
