# Final learn plan, MTE MAS2001

Built 15 September 2026, 02:00 IST. Supersedes the 14 September re-pin in
`reports/05-FIVE-DAY-PLAN.md` (same days, but this one carries the full dependency order
and the hidden blocks explicitly).

Facts: MTE window opens Friday 18 Sep, closes Friday 25 Sep. Paper 30 marks, closed book.
Scope lectures 1 to 21. Clear slots left: Tuesday 15, Wednesday 16, Thursday 17, plus
whatever Friday gives before the paper.

## The order rule

Everything hangs off this chain. Do not read below a block until the blocks above it are
warm, because every question in the paper is 2 or 3 of these stacked:

```
  counting + events (L2)
      -> random variables, pmf/cdf (L3-6)
          -> expectation + variance (L7)
              -> [INDEPENDENCE RULES OF RVs]  (L8-9, hidden, do not skip)
                  -> [CHEBYSHEV]              (L10-11, deck exists as of 15 Sep)
                  -> distributions (L12-16)
                      -> sampling + standard error (L17)
                          -> CLT (L18)
                              -> estimation (L19-21)
```

## Stage 0, hidden blocks first, 2.5 hours total

These carry marks in every past graded set. Chebyshev's deck arrived 15 Sep (S&P L10-11). The
rest have no teaching slide in batch 1, and the batch-2 decks are still unconverted, so their
status stays unconfirmed until the U12 to U19 dedup pass. Do them all while fresh.

```
0.1  CHEBYSHEV, 75 min
     read: S&P L10-11 deck (theory), then sheet section E, bank section 6, mock B1
     drill: k from interval (60/80 mu 70 sd 5 -> k 2 -> 3/4)
            tail vs complement (the 1/9 vs 8/9 fork)
            sum of dice (find Var = 35/6 first, then k, bound 35/54)
            600 throws (k = 2.19, 1 - 1/k^2 = 19/24)
     gate: write both inequality forms from memory, say why distribution-free,
           reproduce 35/54 and 19/24 on paper, no notes
0.2  INDEPENDENCE RULES OF RVs, 40 min
     E(XY) = E(X)E(Y) under independence
     Var(X+Y) = Var(X) + Var(Y) (and X-Y same: plus)
     contrast: E(X+Y) = E(X)+E(Y) always
     drill: Var(sum of two dice) = 35/6 from Var(one) = 35/12
            Var(linear combination) = sigma^2 times sum of squared coefficients
     gate: from memory, state all three rules with their conditions
0.3  THE SMALL HIDDEN SET, 35 min
     memoryless: P(T>s+t | T>s) = P(T>t), exponential only; A2 C1 and MCQ Q5
     landmarks: 68.27 / 95.45 / 99.73 within 1 / 2 / 3 sigma
     expected count: E = N x P (bulbs 7888, batteries 274/576/4487, sets 0.5499)
     geometric expectation: E(N) = 1/p (A1 short 4: 1/(1/2) = 2)
     hypergeometric mean: E = n times K/N (A1 long 3: 4 x 5/25 = 0.8, both cases)
     gate: each one reproduced with its graded example
```

## Stage 1, foundations, 2 hours (Tue morning)

```
read: deck p012 to p062 with the formula sheet open
core: events, set ops, axioms, addition/complement rules, conditional definition,
      counting C(n,r), event independence, rv definition, discrete vs continuous
drills: tournament coding (16 outcomes), C(6,2)=15 laptop question, complement turn
gate: conditional probability question solved from definition; "at least one" solved
      by complement with a disjointness check
```

## Stage 2, pmf/cdf, 2 hours (Tue midday)

```
read: deck p063 to p087, p112 to p139
core: pmf conditions, find k (15k=1, 10k^2+9k=1), cdf step construction, F(b)-F(a-1),
      pdf conditions, F'(x)=f(x), area interpretation, piecewise integration
drills: boards inspection cdf, dice maximum cdf, F=(x-1)^4/16 to density, bus triangle
gate: build a cdf table from a pmf and back; integrate a piecewise pdf without breaking
      the limits
```

## Stage 3, expectation + variance, 1.5 hours (Tue afternoon)

```
read: deck p088 to p111, p140 to p147
core: E(X), E[h(X)], E(aX+b) proof, E(X^2), Var definitions, shortcut formula,
      V(aX+b) = a^2 V(X), sd
drills: freezer 4-part chain, magazine revenue h3/h4, Pareto E and Var with conditions
gate: the p094 style question (E, E(X^2), E(2X+1)^2) end to end
```

## Stage 4, the distribution shelf, 4 hours (Wed)

One pass per distribution, same template each time: setup conditions, pmf/pdf, mean,
variance, the corpus question, the traps.

```
4.1  BINOMIAL (60 min): conditions, pmf, np, npq, complement tails, ratio recovery (p=5/8),
     expected sets 0.5499. Drills: pens 3 parts, die problem both parts.
4.2  POISSON (60 min): pmf, mean=var=lambda, ratio recovery (lambda=10), rejected = tail,
     approximation from binomial, THE NESTING (calls per minute then binomial over 5 min),
     additivity. Drills: pens none, calls 32e^-10, insurance (use 0.1755).
4.3  UNIFORM (30 min): density, mean, variance, length ratio, clipping, |X-2|<2 -> interval,
     inverse K. Drills: 2-to-6, rounding error, 10-to-20.
4.4  NORMAL (75 min): standardization both directions, the TWO TABLE CONVENTIONS (phi vs F,
     identify before substituting), negative z reflection, intervals, inverse 20 percent,
     landmarks, expected count. Drills: 8.6 chain, 45-62, 5000 batteries, 10000 bulbs.
     Then the A2 C2 style two-unknown system (sigma 28.2, mu 37.2, cutoff 30.4).
4.5  EXPONENTIAL (45 min): pdf, cdf, survival, mean 1/lambda, memoryless, conditionals,
     unit conversion. Drills: 15/hr under 3 min = 0.05 hr, repair e^-1 / e^-1.5,
     P(X<1|X<2) = 0.6225 (use the corrected value), buses 0.1353.
     Trap: slide p040 inverts lambda wording, ignore it.
gate: one mixed question per distribution, closed book, before moving on
```

## Stage 5, sampling + CLT, 2 hours (Thu morning)

```
read: clt p001 to p018
core: population vs sample, SE = sigma/sqrt(n), scaling law, CLT conditions. Treat n>=30
      as the course heuristic, not a theorem cutoff; normal populations work at any n,
      while skew and tail behaviour still matter. Use the SE denominator for averages.
drills: lightbulbs 20->10, ATM, impurity (Z2 = -0.94, table answer 0.1645), LED, machines n=9
      exact-normal fallback
gate: the impurity question reproduced with the corrected Z, closed book
```

## Stage 6, estimation, 2.5 hours (Thu midday)

```
read: p5 p001 to p007, p008 to p021, lt p016 to p030
core: parameter/statistic/estimator/estimate, point vs interval, CI shape with z(alpha/2),
      unbiasedness + bias formula, consistency two conditions, efficiency,
      THE PROTOCOL (filter unbiased first, then min variance), sufficiency idea
drills: lambda=0 set (t1 wins), lambda=1 set (T3 wins, vars 3 / 29 / 1/3),
      battery CI (7.81, 8.99), response time 205 ms, packets 0.93
gate: reproduce both comparison sets fully, and the mock B4 layout (T4 trap)
```

## Stage 7, integration, Thu evening (3 hours)

```
7.1  sit reports/07-MOCK-PAPER.md closed book, 90 min, no notes
7.2  mark it against 08, list every miss by stage number above
7.3  repair only the misses, then one redo of the failed parts
7.4  cheat-sheet pass: sheet sections A to I read aloud, 40 min
gate: 24/30 or better. 18-23: Friday morning goes to the weakest stage only.
      Below 18: Friday morning goes to units 1-2 block (deck) or CLT, whichever the
      misses point at
```

## Friday 18, before the paper

```
1  formula sheet, two passes, 40 min
2  the three Chebyshev values and every distribution mean/variance pair from memory
3  the hidden set (memoryless, landmarks, NxP, 1/p, nK/N) from memory, 15 min
4  no new material, nothing below lecture 22
```

## What to skip, permanently for MTE

```
MLE, method of moments, Bayesian estimation, confidence intervals beyond the CI shape,
hypothesis testing, t/F/chi-square, ANOVA, the lms-theory CI block p031+. All out of MTE.
```

## Trap list to reread before the exam

```
1  Chebyshev: tail form vs complement form (1/9 not 8/9)
2  normal: which table, and phi is area-from-0 not cumulative
3  exponential: lambda is rate per unit time, 1/lambda is the mean time
4  complement discipline: at least, none, rejected, more than
5  ratio recovery: cancel, solve, check q = 1 - p
6  rounding: exact until the end (battery sd 0.9734 -> 0.97, not 0.98)
7  N x P for expected counts, never forget the multiply
8  independence: only E(XY) and Var(sum) need it, E(sum) never does
9  "between" inclusive or not, read twice
10 CI: z(alpha/2) = 1.96 at 95 percent, margin = 1.96 x sigma/sqrt(n)
```
