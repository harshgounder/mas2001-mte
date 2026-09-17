# 03 PMF AND CDF (notes p063-p087)

## 1. The probability mass function, pmf (p064)

```
  ┌────────────────────────────────────────────────────────────────────┐
  │ p(x) = P(X = x) = P({s in S : X(s) = x})                           │
  │ "for every possible value x, the probability of observing it"      │
  └────────────────────────────────────────────────────────────────────┘
```

Two conditions (necessary AND sufficient):

```
   (i)  p(x) ≥ 0        every probability is non-negative
   (ii) Σ p(x) = 1      the probabilities over ALL possible x sum to 1
```

```
  ┌──────────────────────────────────────────────────────────────┐
  │ "The probability mass function of a discrete random variable │
  │  describes the behaviour of the variable."                   │
  └──────────────────────────────────────────────────────────────┘
```

## 2. Worked: gas station pumps (p065)

```
   x   :   0     1     2     3     4     5     6
   p(x):  .05   .10   .15   .25   .20   .15   .10       sum = 1.00 ✓
```

```
   P(x)
   .25 │             █
   .20 │             █         █
   .15 │       █     █         █     █
   .10 │  █    █     █         █     █    █
   .05 │  █    █     █   █ █   █  █  █    █  █  █
        └──┬────┬────┬───┬─┬───┬──┬──┬────┬──┬──┬──▶ x
           0    1    2   3 4   5  6  7    8  9  ...
```

```
   (a) at most 2    P(X ≤ 2) = .05+.10+.15 = .30
   (b) at least 3   P(X ≥ 3) = 1 - P(X ≤ 2) = 1 - .30 = .70
                             or .25+.20+.15+.10 = .70
   (c) between 2 and 5 inclusive  P(2 ≤ X ≤ 5) = .15+.25+.20+.15 = .75
```

```
  THE cdf-arithmetic habit:
     "at most k"   =  F(k)   add up to k
     "at least k"  =  1 - F(k-1)   for an integer-valued X
     "between a,b" =  F(b) - F(a-1)   for integer-valued X and integer a,b
```

## 3. Worked: the find-k table (p066) - the batch-1 assignment long Q2

```
   x   :   0    1    2    3    4    5     6      7
   P(x):   0    k   2k   2k   3k   k²   2k²   7k²+k
```

```
  (i) FIND k
       Σ p(x) = k + 2k + 2k + 3k + k² + 2k² + 7k² + k
              = 9k + 10k²
       10k² + 9k = 1  ->  10k² + 9k - 1 = 0
       10k² + 10k - k - 1 = 0  ->  (k+1)(10k-1) = 0
       k = 1/10  (or -1, rejected: probability cannot be negative)

  (ii) with k = 1/10:
       P(X<6)  = p(0)+p(1)+p(2)+p(3)+p(4)+p(5)
               = 0 + k + 2k + 2k + 3k + k²
               = 8k + k²
               = 0.80 + 0.01 = 0.81
       P(X≥6)  = 1 - 0.81 = 0.19
       P(0<X<5) = p(1)+p(2)+p(3)+p(4) = k+2k+2k+3k = 8k = 0.80
```

```
   quick consistency check: P(X<6) + P(X≥6) = 0.81 + 0.19 = 1.00  ✓
```

```
  (iii) DISTRIBUTION FUNCTION: accumulate
        F(x) = 0                         x < 1
               0.1                      1 ≤ x < 2
               0.3                      2 ≤ x < 3
               0.5                      3 ≤ x < 4
               0.8                      4 ≤ x < 5
               0.81                     5 ≤ x < 6
               0.83                     6 ≤ x < 7
               1.0                      x ≥ 7
```

```
  (iv) minimum a with F(a) > 1/2:
       F(4) = 0.8 > 0.5  ->  a = 4
       (F(3) = 0.5 is NOT > 0.5, strict inequality)
```

```
  ╔═══════════════════════════════════════════════════════════════╗
  ║ WATCH THE P(x)=0 ROW                                          ║
  ║ The batch-1 edition has P(X=0)=0, giving 10k²+9k=1 -> k=1/10. ║
  ║ The SECOND edition changed P(X=0) to k, giving 12k+10k²=1     ║
  ║ -> k=0.0782, but its own key still prints k=1/10 which does   ║
  ║ NOT satisfy its own table. The second edition is broken        ║
  ║ (errata 5.1). Study the batch-1 edition.                      ║
  ╚═══════════════════════════════════════════════════════════════╝
```

## 4. Worked: tune-ups, cylinders (p067-p069)

```
   45% four-cylinder, 40% six-cylinder, 15% eight-cylinder
   X = number of cylinders of the next car

   x  :   4     6     8
   p(x): .45   .40   .15          sum 1.00 ✓
```

```
   histogram picture:

   .50 │
   .45 │  █
   .40 │  █          █
   .35 │  █          █
   .15 │  █          █          █
       └──┬──────────┬──────────┬──▶
          4          6          8

   P(X ≥ 6) = .40 + .15 = .55
   P(X > 6) = .15              <- the boundary moved
```

## 5. Worked: building permits, proportional pmf (p070-p071)

```
   Y = number of forms required, p(y) = k y,  y = 1,...,5
```

```
   (a) Σ p(y) = k(1+2+3+4+5) = 15k = 1  ->  k = 1/15

   (b) P(Y ≤ 3) = (1+2+3)/15 = 6/15 = 0.4

   (c) P(2 ≤ Y ≤ 4) = (2+3+4)/15 = 9/15 = 0.6

   (d) is p(y) = y²/50 a pmf?  Σ = (1+4+9+16+25)/50 = 55/50 ≠ 1  -> NO
```

```
  ┌─────────────────────────────────────────────────────────────┐
  │ THE VALID-PMF TEST IS ALWAYS: sum over the support = 1 ?    │
  │ If it does not sum to 1, it is not a pmf. Period.           │
  └─────────────────────────────────────────────────────────────┘
```

## 6. Worked: flashlight batteries (p072-p073) - a pmf built from a process

```
   90% of batteries acceptable (A), need 2 acceptable to work.
   Y = number of batteries tested.
```

```
   (a) p(2) = P(AA) = (.9)(.9) = .81

   (b) p(3) = P(UAA or AUA) = (.1)(.9)(.9) + (.9)(.1)(.9)
            = 2(.1)(.9)² = .162

   (c) p(5): the 5th must be A, exactly one of the first four also A
       AUUUA, UAUUA, UUAUA, UUUAA   = 4 outcomes
       p(5) = 4(.1)³(.9)² = .00324

   (d) general: P(Y=y) = (y-1)(.1)^(y-2)(.9)²,  y = 2,3,4,...
```

The tree for part (b):

```
              start
             /     \
          A(.9)    U(.1)
          |          |
          A(.9)      A(.9)  <- UAA
          |          |
       done        A(.9)   <- UAA done
      p(.81)        |
                 done (AUA) .9*.1*.9=.081
      total for y=3: .081 + .081 = .162
```

## 7. The cumulative distribution function, cdf (p074-p078)

```
  ┌─────────────────────────────────────────────────────────────────┐
  │ F(x) = P(X ≤ x) = Σ_{y: y ≤ x} p(y)        (discrete)           │
  │ F(x) = P(X ≤ x) = ∫_{-∞}^{x} f(y) dy       (continuous)         │
  └─────────────────────────────────────────────────────────────────┘
```

```
  PROPERTIES OF F
     non-decreasing     (it only accumulates)
     0 ≤ F(x) ≤ 1
     F(-∞) = 0,  F(+∞) = 1
     right-continuous
```

```
  THE STEP-FUNCTION PICTURE (discrete cdf)

   F(x)
   1.0 │                          ┌────────────
   0.8 │                    ┌─────┘
   0.6 │              ┌─────┘
   0.4 │        ┌─────┘
   0.2 │  ┌─────┘
   0.0 ├──┘
       └──┬────┬────┬────┬────┬────▶ x
          1    2    3    4    5
             ^ each jump = a pmf value p(x)
```

```
  ╔══════════════════════════════════════════════════════════╗
  ║ pmf AND cdf DETERMINE EACH OTHER                          ║
  ║   discrete:   p(x) = F(x) - F(x-)    (the JUMP at x)      ║
  ║   integer rv: p(n) = F(n) - F(n-1)                        ║
  ║   continuous: f(x) = F'(x)   (derivative)                 ║
  ╚══════════════════════════════════════════════════════════╝
```

## 8. THE key cdf theorem (p079)

```
   for a < b:
        P(a < X ≤ b) = F(b) - F(a)
```

```
  and the integer-valued version that catches people (p135):

        P(a ≤ X ≤ b) = F(b) - F(a-1)
        when X is integer-valued and a, b are integers

        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        the a-1 because F(a-1) INCLUDES the value a-1, and
        P(a ≤ X) must EXCLUDE everything below a
```

```
   picture:

   F(b)  = area/include everything up to and INCLUDING b
   F(a)  = everything up to and including a     <- but P(a<X) excludes a
   F(a-1)= everything up to a-1                 <- so this is the right one

        ... a-1 | a | ... | b
        ├───────┘   │       │
          drop this  keep     keep
```

## 9. Worked: boards inspection (p080-p081)

```
   Lots of 5 boards, 2 inspected. Boards 1,2 are the only defectives.
   X = number of defective boards among the 2 inspected.
```

```
   (a) all 10 selections: (1,2)(1,3)(1,4)(1,5)(2,3)(2,4)(2,5)(3,4)(3,5)(4,5)

   (b) P(X=0) = P{(3,4)(3,5)(4,5)} = 3/10 = .3
       P(X=2) = P{(1,2)} = 1/10 = .1
       P(X=1) = 1 - (.3 + .1) = .6

   (c) F(0) = .30
       F(1) = .90
       F(2) = 1.00

       F(x) = 0     x<0
              .30   0≤x<1
              .90   1≤x<2
              1     2≤x
```

## 10. Worked: dice maximum M (p082-p083) - the elegant one

```
   M = max of two dice
```

```
   pmf: p(1)=1/36, p(2)=3/36, p(3)=5/36, p(4)=7/36, p(5)=9/36, p(6)=11/36
```

```
   WHY the odd numbers? M ≤ m  iff  BOTH dice ≤ m  -> m² outcomes
       p(M = m) = [m² - (m-1)²]/36 = (2m-1)/36
       check m=3: (2*3-1)/36 = 5/36 ✓
```

```
   cdf:
   F(m) = 0      m<1
          1/36   1≤m<2
          4/36   2≤m<3
          9/36   3≤m<4
         16/36   4≤m<5
         25/36   5≤m<6
           1     m≥6

   ^ at integer support points m=1,...,6, F(m)=m²/36.
     For real 1≤m<6, F(m)=floor(m)²/36, as the steps above show.
```

```
   F(m)
   1.0 │                          ┌──────
   0.69│                    ┌─────┘
   0.44│              ┌─────┘
   0.25│        ┌─────┘
   0.11│  ┌─────┘
   0.03├──┘
       └──┬────┬────┬────┬────┬────┬───▶ m
          1    2    3    4    5    6
     squares!/36: 1  4  9  16  25 36
```

## 11. Worked: cdf is non-decreasing (p085) - the proof question

```
   SHOW: x1 < x2  ->  F(x1) ≤ F(x2)

   proof:
      F(x2) = P(X ≤ x2)
            = P({X ≤ x1} ∪ {x1 < X ≤ x2})       split the event
            = P(X ≤ x1) + P(x1 < X ≤ x2)        disjoint, so add
            ≥ P(X ≤ x1)                          a probability is ≥ 0
            = F(x1)                                ✓
```

```
   AND: F(x1) = F(x2) exactly when P(x1 < X ≤ x2) = 0
        (the interval between them carries no probability)
```

---
pmf and cdf are done. Next: expectation and variance (notes p086-p111).
