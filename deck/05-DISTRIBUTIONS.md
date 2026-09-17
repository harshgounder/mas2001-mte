# 05 DISTRIBUTIONS: all five, all slots, all values

## THE NINE SLOTS, VISUALISED (every distribution)

```
   a distribution is a SHAPE, and the exam asks 9 questions of it:

        f(x)│  ╱‾╲
            │ ╱   ╲
        ┌───┼─┴───┴─┼───┐
        │ 1 │  2    │ 3 │  1 point P(X=k)
        │   │  2    │   │  2 tail  P(X≥k)
        │   │       │   │  3 interval
        └───┴───────┴───┘
            │
        ┌───▼───────────────────────┐
        │ 4 moments  E, Var         │
        │ 5 params   recover λ, p   │
        │ 6 inverse  x for a given P│
        │ 7 count    N x P          │
        │ 8 cond     P(A|B)         │
        │ 9 compose  nest two models│
        └───────────────────────────┘
```

## THE DISTRIBUTION FAMILY TREE

```
                 PROBABILITY DISTRIBUTIONS
                           │
       ┌───────────────────┴───────────────────┐
       │                                       │
   DISCRETE                               CONTINUOUS
       │                                       │
   ┌───┴────┐                    ┌─────────┬────┴────┬──────────┐
   │        │                    │         │         │          │
BINOMIAL POISSON            UNIFORM   NORMAL   EXPONENTIAL
 B(n,p)   Poi(λ)              U(a,b)  N(μ,σ²)     Exp(λ)
   │        ▲
   │        │  n→∞, p→0, np=λ
   └────────┘
   (Poisson is the binomial LIMIT)
```

## MEAN vs VARIANCE, EVERY DISTRIBUTION

```
                       MEAN            VARIANCE
   ┌─────────────────┬───────────────┬──────────────────┐
   │ B(n,p)          │ np            │ npq              │
   │ Poi(λ)          │ λ             │ λ       ← SAME!  │
   │ U(a,b)          │ (a+b)/2       │ (b-a)²/12        │
   │ N(μ,σ²)         │ μ             │ σ²      ← square │
   │ Exp(λ)          │ 1/λ           │ 1/λ²    ← recip  │
   └─────────────────┴───────────────┴──────────────────┘

   the memory hooks:
     binomial  ->  np and npq  (the q is the only extra)
     Poisson   ->  ONE parameter does both jobs
     uniform   ->  span² / 12
     normal    ->  second slot is VARIANCE, square-root it
     exponential -> reciprocal pair: rate in, time out
```

For each distribution: what it models, the setup, pmf/pdf, cdf, mean, variance, sd, the
standardisation if any, the table if any, and every question slot the corpus has used. The
slot names are the same nine in every table so you can see the pattern (full pattern logic in
07-PATTERNS.md).

## 1. Binomial, X ~ B(n, p)

```
  models        number of successes in n independent two-outcome trials
  setup check   two outcomes, finite n, trials independent, p constant (ppt3 p011)
  pmf           P(X=x) = C(n,x) p^x q^(n-x),  q = 1-p,  x = 0..n
  cdf           P(X<=x) = sum_{i=0..x} C(n,i)p^i q^(n-i)
  mean          np
  variance      npq
  sd            sqrt(npq)
  mode          floor((n+1)p), with two adjacent modes if (n+1)p is an integer
  approximation -> Poisson in the limit n->infinity, p->0, np->finite l
```

```
  slot        ask                                    used in
  1 point     P(X=2) out of 12, p=0.1                  ppt3 p013-016 pens
  2 tail      P(X>=2) = 1 - P0 - P1                     ppt3 p013-016 pens
  3 interval  P(2<=X<=4)                                 NOT asked, high risk (see 07)
  4 moments   E=np, Var=npq                             A2 A2, A9, D3
  5 params    p from P(X=5)=2P(X=4) -> 5/8              ppt3 p017-018
  6 inverse   smallest n for a guarantee                NOT asked, high risk
  7 count     N x P, 10000 sets x (3/8)^10 = 0.5499     ppt3 p018
  8 conditional  P(X=k | X>=j)                          sibling drill, not an A2 B5 item
  9 compose   Poisson per minute then binomial over 5   ppt3 p026
```

## 2. Poisson, X ~ Poi(l)

```
  models        counts of rare events in a fixed interval
  setup check   rare, independent in time/space, rate constant
  pmf           P(X=x) = e^-l l^x / x!,  x = 0,1,2,...
  cdf           P(X<=x) = e^-l sum_{i=0..x} l^i/i!
  mean          l
  variance      l          (mean EQUALS variance, the signature)
  sd            sqrt(l)
  additivity    sum of independent Poissons is Poisson with l summed
  from binomial l = np
```

```
  slot        ask                                          used in
  1 point     P(X=4), l=5 -> 0.1755                          ppt3 p027 (slide prints 0.1745)
  2 tail      P(X>2) = 1-P0-P1-P2 = 0.8753                   A2 C3
  2 tail      "rejected" = P(X>=4) = 0.2424 when l=2.5       A2 B1
  3 interval  P(2<=X<=4)                                     NOT asked, medium risk
  4 moments   E=Var=l, the signature test                    MCQ (R25S4-A2)
  5 params    l from P(X=1)=0.2P(X=2) -> l=10                ppt3 p025
  6 inverse   not used                                       low evidence
  7 count     expected defective bottles 0.1 percent         E25SUM-Q17
  9 compose   nest inside binomial, 32 e^-10 = 0.00145       ppt3 p026
```

## 3. Uniform, X ~ U(a, b)

```
  models        a random point in an interval, all lengths equally likely
  pdf           f(x) = 1/(b-a),  a <= x <= b
  cdf           F(x) = 0 below a,  (x-a)/(b-a) inside,  1 above b
  mean          (a+b)/2
  variance      (b-a)^2 / 12
  sd            (b-a)/sqrt(12)
  shortcut      probability = length ratio, no integration needed
```

```
  slot        ask                                    used in
  1 point     f(x) value, and mean/variance           ppt4 p003-006
  2 tail      P(X>k) as a length ratio                ppt4 p006
  3 interval  P(3<X<5) = 2/4 = 0.50                    ppt4 p006
  4 moments   E=(a+b)/2, Var=(b-a)^2/12                A2 A4
  5 params    solve a,b from mean and variance         A2 A10 variant
  6 inverse   K such that P(X<K)=p                     NOT asked, medium risk
  9 compose   sum of two stated uniforms                notes p126 example
```

## 4. Normal, X ~ N(mu, sigma^2)

```
  models        heights, weights, marks, measurement error, and the CLT destination
  pdf           f(x) = 1/(sigma sqrt(2pi)) exp(-(x-mu)^2/(2 sigma^2))
  notation      X ~ N(mu, sigma^2), the SECOND slot is VARIANCE
  standardise   Z = (X-mu)/sigma,  Z ~ N(0,1)
  probability   P(a<X<b) = Phi((b-mu)/sigma) - Phi((a-mu)/sigma)
  inverse       X = mu + Z sigma
  symmetry      Phi(-z) = 1 - Phi(z),  P(Z>z) = 1 - Phi(z)
  shape         mean = median = mode = mu, tails never touch, sigma widens the curve
  landmarks     68.27 within 1s, 95.45 within 2s, 99.73 within 3s
```

```
  slot        ask                                     used in
  1 point     density value, symmetry facts             ppt4 p010-011
  2 tail      P(X>8.6) = 0.4522                         ppt4 p032-033
  3 interval  P(45<X<62), impurity=0.1645 by rounded table A2 B3, clt p013 (errata 6)
  4 moments   E=mu, Var=sigma^2, identify both          E25S4-A4, E25S3-A5
  5 params    two unknowns from two probabilities       A2 C2 (errata 10: mu 37.2)
  6 inverse   x for a 20 percent lower tail = 3.792     ppt4 p034-037
  7 count     N x P, 5000 batteries, 10000 bulbs        A2 B4, D1
  8 conditional  P(X>a | X>... ) normal ratio           not used, low evidence
  9 compose   CLT -> normal, then a table read          clt p013, p015
```

## 5. Exponential, T ~ Exp(l)

```
  models        waiting time between events, lifetimes, "until failure"
  pdf           f(t) = l e^{-l t},  t > 0            (l is a RATE)
  cdf           F(t) = 0 for t<=0; 1 - e^{-l t} for t>0
  tail          P(T>t) = 1 for t<0; e^{-l t} for t>=0
  mean          1/l
  variance      1/l^2
  sd            1/l
  memoryless    P(T>s+t | T>s) = P(T>t)
  mean-first form  f(t) = (1/mu) e^{-t/mu} when the question gives mu, then l = 1/mu
```

```
  slot        ask                                     used in
  1 point     f value, pdf identification               E24S4-A4
  2 tail      P(T>12) = 5e^-4 = 0.0916                  A1 short Q2 (errata 3)
  3 interval  P(T<3min) = 0.5276 at 15/hour             ppt4 p042-043
  4 moments   E=1/l, Var=1/l^2                          ppt4 p043
  5 params    l from a mean, or mean from l             A2 D2
  6 inverse   not used, medium risk
  7 count     not used
  8 conditional  P(X<1 | X<2) = 0.6225                  A2 B5 (errata 9: prints 0.5679)
  9 compose   repair-time, memoryless, unit conversion  A2 MCQ5, C1

  ERRATUM 4: the ppt4 p040 slide says "1/l is the mean number per unit time", backwards.
  lambda is the rate, 1/lambda is the mean TIME. p041 states it correctly.
```

## The one-table summary (memorise this block)

```
              pmf / pdf                     mean      variance
  B(n,p)      C(n,x) p^x q^(n-x)             np        npq
  Poi(l)      e^-l l^x / x!                  l         l
  U(a,b)      1/(b-a)                        (a+b)/2   (b-a)^2/12
  N(mu,s^2)   1/(s sqrt(2pi)) e^-(x-mu)^2/2s^2  mu    s^2
  Exp(l)      l e^-l t                       1/l       1/l^2

  memory hooks:
    binomial: np and npq, the q is the only extra
    Poisson: mean IS variance, necessary but not enough to identify the family
    uniform: centre and span squared over 12
    normal: mu and sigma SQUARED, the second slot is variance
    exponential: reciprocal pair, rate in, time out
```
