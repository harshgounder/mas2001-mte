# MTE topic flow: what leads to what

Built 14 September 2026. Companion to the v1 tree (now at `archive/00-TOPIC-TREE-v1.md`,
superseded by `00-MASTER-SYLLABUS.md`). This file draws the edges between
topics: prerequisites, cross-links, and the broken links (edges the questions walk that no
slide teaches).

Legend:

```
  -->   prerequisite / leads to
  <==>  strong cross-link (a question jumps between them)
  [H]   hidden node or hidden subtopic (no teaching slide in the converted batch 1)
  [!]   already graded in assignment 1 or 2
  [~]   used by questions, not named in the MTE syllabus list
```

## Diagram A: the spine (learn top to bottom)

```
   T1  COURSE INTRO ............ dead end, no questions
    |
    v
   T2  PROBABILITY FOUNDATIONS
       sets | events | axioms | COUNTING | conditional | indep events
    |
    |             \
    |              \ counting engine --> T8/T9 coefficients, T2 questions
    v               \
   T3  RANDOM VARIABLES
       discrete | continuous | Bernoulli
    |
    v
   T4  PMF / PDF / CDF
    |
    +--------+---------+
    |        |         |
    v        v         v
   T5       T6        (distribution shelf, diagram B)
   EXPECT   VARIANCE
    |        | + INDEPENDENCE RULES OF RVs [H][!]
    |        |
    |        +---------------> T7  CHEBYSHEV [~]   (needs mu + sigma; deck arrived 15 Sep)
    |        |
    v        v
   T13  SAMPLING + STANDARD ERROR   (SE = sigma/sqrt(n), needs T6)
    |
    v
   T14  CLT   <== T11 normal supplies the destination distribution
    |             T6H supplies the variance of the mean
    v
   T15  ESTIMATION BASICS  (point vs interval, CI shape)
    |
    v
   T16  ESTIMATOR PROPERTIES  (unbiasedness: T5; efficiency: T6; combos: T6H)
```

## Diagram B: the distribution shelf (all hang off T4 + T2 counting)

```
   T4 pmf/pdf/cdf
    |
    +--> T8  BINOMIAL --limit (n up, p down, np=lambda)--> T9  POISSON
    |      needs: counting C(n,x), indep trials          needs: tails, rare events
    |                                                       |
    |                                                       | process story
    |                                                       v
    |                                                    T12  EXPONENTIAL [H memoryless]
    |                                                    needs: cdf, conditionals, survival
    |
    +--> T10  UNIFORM (standalone; needs abs-value -> interval skill)
    |
    +--> T11  NORMAL [H: two tables][H: 68/95/99.7] --CLT answer world--> T14

   nesting already graded: T9 INSIDE T8   (p026: 2 calls/min, then 5 minutes binomial)
   every shelf item also needs T2 counting + T5/T6 for its mean/variance questions
```

## Diagram C: broken links (questions use these; no batch-1 slide teaches them)

```
   T6H  independence rules of rvs (E(XY), Var(X+Y))
    |
    +--> T7   dice-sum Chebyshev           A1 short 5       [!] already graded
    +--> T14  every CLT question           SE derivation
    +--> T16  Var(linear combinations)     ppt5/lms comparisons

   T7   Chebyshev (deck arrived 15 Sep; was [H] in the old batch)
    |
    +--> A1 MCQ 5, MCQ 10  +  A1 short 5 (35/54), short 6 (19/24)  +  A1 app 4 (75%)
         + MTE 2024-25 QA3/QB3 + MTE 2025-26 Q5: graded 8+ uses, deck now exists

   T12H memoryless property
    +--> A2 MCQ Q5      +--> A2 section C Q1

   T11H 68/95/99.7 landmarks ----> A2 MCQ Q11

   T11H two table conventions (cumulative vs area-from-0) ----> every normal/CLT question

   X-cutting [H]: complement discipline (T7/T8/T9), N*P expected count (T8/T9/T11),
                  unit conversion (T9/T12/T14), |.| -> interval (T10), piecewise (T4/T5)
```

## Diagram D: edge list (from -> to : why)

```
   T2 -> T3    rv is a function on the sample space
   T2 -> T8    binomial coefficient needs counting
   T2 -> T9    poisson derived as a binomial limit
   T4 -> T5    expectation sums/integrates over the distribution
   T4 -> T6    variance same
   T4 -> T8..12  every distribution is a named pmf/pdf
   T5 -> T6    E(X^2) and E[(X-mu)^2] start at expectation
   T6 -> T7    Chebyshev needs mu and sigma
   T6 -> T13   SE needs sigma
   T9 <-> T12  poisson process and exponential interarrival, two faces of one story
   T11 -> T14  CLT lands in the normal world (tables)
   T13 -> T14  CLT is a sampling distribution statement
   T14 -> T15  inference pipeline
   T15 -> T16  estimator theory builds on estimation basics
   T5, T6, T6H -> T16  unbiasedness, efficiency, combos
   T6H -> T7, T14, T16  THE BROKEN EDGE
```

## Diagram E: composite questions (one question, several topics; the real MTE shape)

```
   A1 short 5   dice sum 35/54     : T2 + T6H + T7
   A1 short 6   600 throws 19/24   : T8 + T7
   A2 B4        5000 batteries     : T11 tables + N*P expected count
   A2 C2        two percentiles    : T11 inverse + simultaneous equations
   clt p013     impurity           : T13 + T14 + T11 tables + T6H
   ppt3 p026    calls per minute   : T9 + T8 nested
   ppt5 p015    estimator compare  : T5 + T6H + T16
   ppt5 p019    T3 consistency     : T5 + T6 + T16
   A1 long Q3   oranges/items      : T2 counting + T4 pmf (combination heavy)
```

## Topic numbering

T1 intro, T2 probability foundations, T3 random variables, T4 pmf/pdf/cdf, T5 expectation,
T6 variance and independent rvs, T7 Chebyshev, T8 binomial, T9 Poisson, T10 uniform,
T11 normal, T12 exponential, T13 sampling and standard error, T14 CLT, T15 estimation
basics, T16 estimator properties. Full detail in `archive/00-TOPIC-TREE-v1.md` and the
current master at `00-MASTER-SYLLABUS.md`.
