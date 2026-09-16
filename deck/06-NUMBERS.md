# 06 NUMBERS: constants, table values, landmarks, identities

## THE NUMBER LINE OF EVERY PROBABILITY YOU WILL WRITE

```
   0 ──────────────────────────────────────────────────── 1
   │        │         │         │        │          │
   e^-10    e^-5     e^-4      e^-2    e^-1        near 1
   4.5e-5  .0067    .0183     .1353   .3679      (.9772, .9987)
   rare ─────────────────────────────────────────▶ common

   the four e-values to have instantly:
        e^-1 = 0.3679        e^-2 = 0.1353
        e^-4 = 0.01832       e^-5 = 0.006738      e^-10 = 4.54e-5
```

## THE STANDARD NORMAL TABLE AS A PICTURE

```
   Φ(z)
   1.0 │                              ╭────
       │                          ╭───╯
   0.84│                      ╭───╯  0.8413 at z=1.0
       │                  ╭───╯
   0.50│          ╭───────╯   <- 0.5000 at z=0
       │      ╭───╯
   0.02│ ╭────╯  <- 0.0228 at z=-2.0
       └─┬────────┬──────┬───────┬──▶ z
        -2       0      1.0     2.0

   values to have cold:
     z=0.12 -> .5478      z=0.84 -> .7995      z=1.00 -> .8413
     z=1.50 -> .9332      z=1.96 -> .9750      z=2.00 -> .9772
     z=2.36 -> .9909      z=2.58 -> .9950      z=3.00 -> .9987

   -2.36 / -0.94 pair (impurity):  .4909 - .3264 = .1645
```

## THE THREE CHEBYSHEV THRESHOLDS, DRAWN

```
   1/k²
   1.0 │█
       │█
   .25 │█ █
       │█ █
   .11 │█ █ █
       │█ █ █
   .06 │█ █ █ █
       │█ █ █ █
   .01 │█ █ █ █  .  .  .  █
       └─┬─┬─┬─┬──────────┬──▶ k
         1 2 3 4          10

   k=2 -> 3/4      k=3 -> 8/9      k=4 -> 15/16
```

Every number that can appear, with what it is and where it comes from. Grouped so you can
find one fast.

## 1. Chebyshev thresholds (exact fractions)

```
  k    bound 1/k^2    complement 1 - 1/k^2
  1    1              0            (vacuous)
  2    1/4 = 0.25     3/4 = 0.75
  3    1/9 = 0.1111   8/9 = 0.8889
  4    1/16 = 0.0625  15/16 = 0.9375
  5    1/25 = 0.04    24/25 = 0.96
  10   1/100 = 0.01   99/100 = 0.99
  sqrt(10) approx 3.1623  -> k^2 = 10 from a 0.1 tail
```

## 2. Distribution moments worth having instantly

```
  one fair die     E = 7/2 = 3.5,  E(X^2) = 91/6, Var = 35/12 = 2.9167
  sum of two dice  E = 7,  Var = 35/6 = 5.8333,  sd = 2.4152
  B(1,p) Bernoulli  E = p,  Var = pq
  B(12, 0.1)  E = 1.2,  Var = 1.08
  B(600, 1/6) E = 100,  Var = 250/3 = 83.3333, sd = 9.1287
  Poi(2)  E = Var = 2,  sd = 1.4142
  Poi(10) E = Var = 10
  U(2,6)  E = 4,  Var = 4/3 = 1.3333
  N(8,5)  E = 8,  Var = 5 (note: the "5" in N(8,5) is the VARIANCE if written sigma^2,
          but this deck's numbers mu=8 sigma=5 are used with sigma = 5 in the arithmetic,
          CHECK the convention on the page, errata 8)
  Exp(l)  E = 1/l,  Var = 1/l^2
  Exp mean 2  -> l = 1/2
```

## 3. Standard normal table values (cumulative, the common ones)

```
  z       Phi(z)      use
  0.00    0.5000      centre
  0.10    0.5398
  0.12    0.5478      the 8.6 question, P(X<8.6)
  0.24    0.5948
  0.50    0.6915
  0.60    0.7257
  0.84    0.7995
  0.8416  0.8000      inverse: a 20 percent lower tail
  1.00    0.8413
  1.28    0.8997      the 90 percent landmark
  1.34    0.9099
  1.50    0.9332
  1.645   0.9500      95 percent one tail
  1.96    0.9750      95 percent two tails
  2.00    0.9772
  2.36    0.9909
  2.576   0.9950      99 percent two tails
  3.00    0.9987
```

```
  negative z, use  Phi(-z) = 1 - Phi(z), or the table's left tail directly.
  the -2.36 / -0.94 pair (impurity):  0.4909 - 0.3264 = 0.1645  (errata 6)
```

## 4. The 68 / 95 / 99.7 landmarks

```
  within 1 sigma   68.27 percent
  within 2 sigma   95.45 percent
  within 3 sigma   99.73 percent
  (the ppt4 slides round these to 68.3, 95.4, 99.7)
  used by: A2 MCQ Q11, and any "approximately what fraction" question
```

## 5. Worked corpus values (the ones that reappear)

```
  pens B(12,0.1)        P(X=2) 0.2301   P(X>=2) 0.3410   P(X=0) 0.2824
  irregular die         p = 5/8, P(X=0) over 10 = 5.499e-5, count over 10000 = 0.5499
  insurance Poi(5)      P(X=4) 0.1755  (slide 0.1745 is wrong, errata 1)
  calls nesting         32 e^-10 = 0.0014528
  Poisson ratio         l = 10, P(X=0) = 4.54e-5
  uniform U(2,6)        P(3<X<5) 0.50
  normal N(8,5)         P(X<8.6) 0.5478   P(X>8.6) 0.4522   inverse 20 percent 3.792
  two-unknown normal    sigma 28.2, mu 37.2, cutoff 30.4  (errata 10)
  exponential 15/hr     P(T<3 min) 0.5276
  exponential mean 2    P(X<1|X<2) 0.6225  (slide 0.5679 wrong, errata 9)
  exponential lifetime  P(X>12) with f = x e^-x/3 / 9 -> 5e^-4 = 0.0916 (errata 3)
  clt lightbulbs        SE 20 at n=25, SE 10 at n=100
  clt ATM               Z = 1.50, P = 0.0668
  clt impurity          Z1 -2.36, Z2 -0.94, answer 0.1644  (errata 6)
  clt LED               Z = -2.00, P = 0.0228
  clt machine n=9       Z1 -1.80, Z2 0.60, answer 0.6898
  estimator set 1       lambda 0, Var(t1) 0.2s^2, t2 1.5s^2, t3 0.5556s^2, best t1
  estimator set 2       Var(T1) 3s^2, Var(T2) 29s^2, Var(T3) s^2/3, best T3
  dice Chebyshev        sigma^2 35/6, k=3, bound 35/54 = 0.6481, exact 1/3
  600 throws            1 - 5/24 = 19/24 = 0.7917, exact binomial 0.9754
  marks Chebyshev       k=2, P >= 0.75
  tube (errata 16)      P(X<150)=1/3, P(X>150)=2/3, all three 1/27, none 8/27 (key 2/3 WRONG)
  hypergeometric lot    mean nK/N = 4 x 5/25 = 0.80 exactly, same as binomial mean
  battery sd            Var 0.9475, exact sd 0.9734 -> 0.97 (key's 0.975 wrong, errata 12)
```

## 6. Identities and algebra shortcuts

```
  e^0 = 1
  e^-1 = 0.3679    e^-2 = 0.1353    e^-4 = 0.01832    e^-5 = 0.006738    e^-10 = 4.54e-5
  C(n,r) = C(n,n-r)
  sum p(x) = 1  (algebraic check, use it on find-k questions)
  35/12 and 35/6  (one die, two dice variance)
  (b-a)^2/12  uniform variance, 12 is fixed
  Var(X-Y) = Var(X)+Var(Y) when independent, the minus stays plus
  Phi(-z) = 1 - Phi(z)
  relative efficiency = Var(T2)/Var(T1)
  MSE = Var + Bias^2
```

## 7. The exact-vs-rounded values (write the exact one)

```
  question                     write         not
  insurance P(X=4)             0.1755        0.1745 (slide)
  irregular die count          0.5499 -> .55 0.549 (slide)
  assignment Q2 P(X>12)        0.0916        0.0915 (key truncates)
  battery sd                   0.97           0.975 or 0.98 (key rounds twice)
  A2 C3 P(X>2)                 0.8753        0.8754 (key sums rounded terms)
  exponential conditional      0.6225        0.5679 (key wrong)
  MTE 2024 CDF                 option D      option B (scheme wrong)
  MTE 2025 Q8(ii)              E(t^2)!=theta^2  E(t^2)!=0 (scheme drops theta^2)
```

## 8. Unit conversions that decide marks

```
  15 per hour  ->  3 minutes = 0.05 hour   (rate in hours, time in hours)
  mean 2 (hours) -> l = 1/2 per hour
  4 minutes mean gap at 15/hour:  1/l = 1/15 hour = 4 minutes
  days and hours: convert to ONE unit before substituting
  RULE: the rate and the time MUST share a unit. Convert the odd one first.
```
