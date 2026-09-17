# Skeleton-coverage bank: the pool the MTE draws from, 17 Sep 2026

This is the artifact meant to cover the next paper. The claim is COVERAGE, not forecast: the
MTE is a draw from a fixed skeleton pool (proven across 9 sittings), so a bank that holds every
skeleton plus its mutations contains the next paper with high probability.

The miss probability equals the chance the setter invents a NEW skeleton. Across 9 sittings we
have seen 0 new skeletons, only reskins. That is the basis.

## How to read an entry

```
  SKELn      skeleton id, stable
  pool       how many times seen across all sittings held
  ask        the 9-slot ask type (point / tail / interval / moments / params / inverse /
             count / conditional / composite)
  source     where it comes from (G&K / Walpole / H&T / deck / assignment / MCQ bank)
  muts       the mutations observed, with the exact value deltas
  do         what to drill
```

## TIER 1: guaranteed (seen in every sitting)

### SKEL1 Chebyshev: within-k / find-c / inverse
```
  pool    8 uses (in every sitting held: MTE24, MTE25, ETE S3+S4 both years, re-sess both)
  ask     all three forms appear
  source  G&K (the 21/25 inverse verified in G&K), the L10-11 deck (find-c verbatim)
  muts    M0 reskin: sigma 2 (G&K) -> sigma 3 (24/25) -> generic k=3
          M1 invert:  given k, find the bound   <->   given the bound, find c/k
          M3 retarget: within-k (1-1/k^2)  <->  tail (1/k^2)  <->  inverse (solve for c)
  values  21/25, 24/25, 8/9, 15/16, 1/9, 0.04, mu=10 var=4, k=2, k=2.5, k=3
  do      drill ALL THREE forms. the 1/9-vs-8/9 fork is the trap (errata 15).
```

### SKEL2 One Normal question (count or inverse)
```
  pool    9 uses, every paper has exactly one
  ask     count (N x P) or inverse (find x for a tail)
  source  Devore / ppt4 deck / McClave (L14-15)
  muts    M0: mean 8 sd 5, mean 50 var 100 (sd 10), mean 20 sd 10, N(45, ...)
          M1 invert: "find P(X>8.6)"  <->  "find x with P=0.90"
          M2 two-unknown: solve mean+sd from two percentiles (sigma 28.2, mu 37.2)
          M3 retarget: one-tail -> interval -> the two-unknown system
  values  z=1.5 -> 0.9332, z=-1.5, z=1.2816 -> 62.82, 68/95/99.7, phi table
  do      the TWO-TABLE discipline (phi from 0 vs F cumulative), then the inverse, then
          the two-unknown system. the two-unknown is the hard slot.
```

## TIER 2: high probability (most sittings)

### SKEL3 Poisson parameter recovery
```
  pool    5 of 9 Poisson rows (MTE24 B1, MTE25, ETE25S4)
  ask     params
  source  G&K Poisson chapter, ppt3 deck
  muts    M0: P(X=2)=9P(X=4)+90P(X=6) -> lambda=10;  P(X=1)=0.2P(X=2) -> lambda=10
  do      the ratio equation -> solve for lambda -> then any ask on it.
```

### SKEL4 Poisson point/tail/nesting
```
  pool    5 uses
  ask     point, tail, composite
  source  ppt3 (2 calls/min then 5 min binomial = 0.00145), H&T
  muts    M3: P(X=0)=e^-l  <->  P(X>=4) "rejected"  <->  P(X=2) per window
          M4 compose: Poisson rate then binomial over the window
  values  e^-3=0.0498, 0.8753, 0.2424, lambda=10, 0.00145
  do      the NESTING (M4) is the composite they like. drill it.
```

### SKEL5 Binomial point+tails
```
  pool    7 uses
  ask     point, tail, moments
  source  ppt3 (pens B(12,0.1)), G&K
  muts    M0: pens 1/10 12 -> defective 20% -> B(180,1/3) -> B(50,0.4) -> B(15,0.08)
          M1 invert: "P(X=5)=2P(X=4)" -> p=5/8
          M3 retarget: exactly -> at least -> at most (complement)
  values  0.2301, 0.341, 0.2824, 0.3734, 0.7137, p=5/8, 0.5499, 0.3367
  do      the complement tails (at least / none). the two-sided interval (0.3367) is a
          SIBLING not yet seen.
```

### SKEL6 Exponential
```
  pool   12 uses (telephone/typist/machine phrasings)
  ask     point, conditional, moments
  source  G&K ch5 (telephone), ppt4, McClave
  muts    M0: telephone mean 5 -> 6 -> 4 -> 3 -> 1/4 (the most-mutated value in the corpus)
          M2 memoryless: P(X>s+t | X>s) = P(X>t)
          M3 retarget: P(X>x) -> conditional P -> repair-time pattern
  values  e^-1 = 0.3679, 0.6225 (conditional), 15/hr, lambda=1/3
  do      the conditional via cdf ratio, and memoryless. both hidden-layer items.
```

### SKEL7 Uniform
```
  pool    1 in-syllabus use
  ask     point, interval, moments, inverse
  source  ppt4 (U(2,6), U(0,5)), G&K
  muts    M0: (2,6) -> (0,5) -> (-a,a) -> (-3,3) -> (a,b) mean 1 var 4/3
          M1 invert: "find a so that P(X>1)=1/3"
          M3 retarget: P(X<k) -> P(|X|>k) -> interval
  values  (a+b)/2, (b-a)^2/12, (5-2)/6=0.5, a=1, a=2
  do      length-ratio shortcut + the |X| -> interval move.
```

## TIER 3: estimation properties (the MTE always has one)

### SKEL8 Estimator comparison (unbiased + efficiency + consistency)
```
  pool   21 rows carry an estimation term (largest family)
  ask     composite
  source  ppt5, lms-theory (SAME question, different constants)
  muts    M0 reskin of the T1..T4 set
          M4 compose: unbiasedness + efficiency + consistency in one question
  values  T1 sigma^2, T2 sigma^2/2, T3 sigma^2/3, T4 biased (3mu/2)
  do      the PROTOCOL: check unbiasedness FIRST, eliminate the biased one, THEN minimum
          variance. the T4 trap is selecting it on variance.
```

### SKEL9 Sufficiency
```
  pool    3 uses (MTE25 Q3, ETE25S4, ETE24S4)
  ask     composite / MCQ
  source  H&T section 6.7, lms-theory p024
  muts    M0: Poisson sample mean, exponential sufficient statistic, sufficiency MCQ
  do      Neyman-Fisher / the definition ("contains all information about the parameter").
```

### SKEL10 Unbiasedness of a given statistic
```
  pool    3+ uses
  ask     point / composite
  source  ppt3, G&K
  muts    M0: "is t^2 an unbiased estimator of theta^2" (G&K ex6, VERBATIM)
  do      E(statistic) = parameter check. the t^2 case is verbatim from G&K.
```

## TIER 4: RV / pdf-cdf (foundation, always present)

### SKEL11 Density find-k
```
  pool   14 rows carry a pdf/cdf/pmf/density term
  ask     params
  source  ppt3/ppt4 find-k examples, G&K
  muts    M0: 15k=1 -> 9k+10k^2=1 -> kx^3(4-x)^2 on (0,4) -> 6x(1-x) on (0,1)
  values  k=1/15, k=1/10, k=1/1000, k=5/8, k=2/3
  do      normalize f, solve for k, then mean/variance on the same density.
```

### SKEL12 pmf table + CDF + transformed expectation
```
  pool    5 uses
  ask     point, moments
  source  deck p094 (the -3/6/9 table), assignments
  muts    M0: values -3,6,9 with probs 1/6,1/2,1/3
          M3 retarget: E(X) -> E(X^2) -> E((2X+1)^2) -> min c with F(c)>1/2
  values  E(X)=11/2, E(X^2)=93/2, E(2X+1)^2=209, min c = 6
  do      the full chain. it recurs in deck + 2025-26 assignment + summer paper.
```

### SKEL13 CDF to density
```
  pool    3+ uses
  ask     point
  source  deck p138/139, G&K
  do      differentiate the piecewise cdf, then integrate for probabilities.
```

### SKEL14 CLT / standard error
```
  pool    3 uses
  ask     point
  source  lms-standard-error-clt deck
  muts    M0: var 400 n 100 -> SE halves when n quadruples
          M3 retarget: SE value -> CLT probability -> sampling distribution
  values  sigma/sqrt(n), 2.0 vs 1.0, n>=30 rule
  do      SE = sigma/sqrt(n), then the z with SE denominator. the M25-Q7 machine-life
          question IS a lecture-slide example (verified).
```

### SKEL15 Independence rules (hidden layer)
```
  pool    graded, hidden
  ask     moment / direct
  source  no teaching slide in batch 1
  muts    E(XY)=E(X)E(Y), Var(X+Y)=Var(X)+Var(Y), Var(X-Y)
  values  Var(one die)=35/12, Var(sum)=35/6, dice bound 35/54 vs exact 1/3
  do      drill E(XY)=E(X)E(Y) as a DIRECT ASK (ETE R25S3-A1 did this).
```

## THE COVERAGE TABLE (drill priority, measured)

```
  rank  skeleton                       pool   why first
  1     SKEL1  Chebyshev all 3 forms     8    in every sitting
  2     SKEL2  Normal incl 2-unknown     9    one per paper, hard slot is the inverse
  3     SKEL11 density find-k           14    foundation of every distribution Q
  4     SKEL6  exponential conditional  12    most-mutated value (telephone 5->1/4)
  5     SKEL5  binomial tails            7    complement is the trap
  6     SKEL3  Poisson param recover     5    ratio equation (of 9 Poisson rows)
  7     SKEL4  Poisson nesting           5    the composite they like
  8     SKEL8  estimator comparison     ~9    the estimation staple (biggest family)
  9     SKEL7  uniform                    1    length-ratio + |X| move (in-scope count)
  10    SKEL12 pmf table chain            5    recurs everywhere
  11    SKEL14 CLT / SE                   3    SE formula
  12    SKEL9  sufficiency                3    MCQ form
  13    SKEL10 unbiasedness               3    t^2 verbatim
  14    SKEL13 cdf to density             3    differentiate
  15    SKEL15 independence rules         2    hidden, direct ask possible
```

Pool counts are the number of in-syllabus MTE+ETE rows matching the topic term, measured from
question-instance-ledger-enriched.csv. A row can match several terms, so they are not a
partition. Chebyshev shows 8 rows but appears in every one of the 9 sittings (some sittings
carry it inside a multi-part question).

If you drill these 15 in this order, plus their listed mutations, you have covered every
in-syllabus question shape the department has used in 9 sittings. The remaining risk is the
setter inventing a 16th skeleton, which has not happened once in the sample.
