# 04 EXPECTATION AND VARIANCE (notes p086-p111)

## 1. The three parameters (p086-p087)

```
   ┌───────────────────────────────────────────────────────┐
   │  MEAN μ         centre / location                     │
   │  VARIANCE σ²    spread                                │
   │  SD σ           spread, in the ORIGINAL units         │
   └───────────────────────────────────────────────────────┘

   "knowledge of the numerical values of these parameters gives
    the researcher quick insight into the nature of the variable"
```

## 2. Expectation of a discrete rv (p088)

```
   ┌──────────────────────────────────────────────────────────┐
   │  E(X) = μ_X = Σ_{x in D}  x · p(x)                        │
   │                                                            │
   │  "the weighted average of the values, weighted by their   │
   │   probabilities"                                          │
   └──────────────────────────────────────────────────────────┘
```

```
   the picture: a balance beam. values on the x-axis, probabilities as weights.
   the mean is the BALANCE POINT.

              p(x) as weight
       ▁      ▃      █      ▃      ▁
       ●──────●──────●──────●──────●
       1      2      3      4      5
                    ▲
                 balance point = E(X)
```

## 3. Worked: a fair die (p089)

```
   p(x) = 1/6,  x = 1..6

   E(X) = 1(1/6) + 2(1/6) + 3(1/6) + 4(1/6) + 5(1/6) + 6(1/6)
        = (1+2+3+4+5+6)/6 = 21/6 = 7/2 = 3.5
```

```
  ┌──────────────────────────────────────────────────────────┐
  │ 3.5 is not a face on the die. The mean need not be an     │
  │ achievable value. It is the long-run average.             │
  └──────────────────────────────────────────────────────────┘
```

## 4. Expectation of a function of X (p090)

```
   E[h(X)] = Σ_{x} h(x) p(x)      (discrete)
   E[h(X)] = ∫ h(x) f(x) dx       (continuous)
```

```
  ╔═══════════════════════════════════════════════════════════╗
  ║ E[h(X)]  ≠  h(E(X))     in general                        ║
  ║                                                           ║
  ║ you must apply h to EACH value, then weight, then sum.     ║
  ║ you may NOT plug the mean into h.                          ║
  ╚═══════════════════════════════════════════════════════════╝
```

## 5. Properties of the mean (p092-p093)

```
   THEOREM   E[c] = c        E[cX] = c E[X]
```

```
   proof of E[c]:
       E[c] = Σ c f(x) = c Σ f(x) = c(1) = c        ✓
   proof of E[cX]:
       E[cX] = Σ c x f(x) = c Σ x f(x) = c E[X]      ✓
```

```
   EXERCISE (p093):  prove E[aX + b] = a E[X] + b
       E[aX+b] = Σ (ax+b)f(x) = a Σ x f(x) + b Σ f(x)
               = a E[X] + b(1) = a E[X] + b          ✓
```

```
  ┌─────────────────────────────────────────────────────────┐
  │ E is LINEAR, and it is linear with NO independence       │
  │ needed:  E[X+Y] = E[X] + E[Y]  ALWAYS                    │
  │          E[aX+b] = aE[X]+b     ALWAYS                    │
  └─────────────────────────────────────────────────────────┘
```

## 6. Worked: the p094 triple (p094) - re-asked on ETE papers

```
   x     :  -3    6    9
   P(X=x):  1/6  1/2  1/3
```

```
   E(X)   = (-3)(1/6) + 6(1/2) + 9(1/3)
          = -0.5 + 3 + 3 = 11/2 = 5.5

   E(X²)  = 9(1/6) + 36(1/2) + 81(1/3)
          = 1.5 + 18 + 27 = 93/2 = 46.5

   E((2X+1)²) : expand first  = E[4X² + 4X + 1]
                              = 4 E(X²) + 4 E(X) + 1
                              = 4(46.5) + 4(5.5) + 1
                              = 186 + 22 + 1 = 209
```

```
  ┌──────────────────────────────────────────────────────────┐
  │ THE METHOD: EXPAND, then use linearity term by term.      │
  │ Do NOT compute the 3 values of (2x+1)² by hand first      │
  │ (you can, but the algebra route is faster and safer).     │
  └──────────────────────────────────────────────────────────┘
   sanity: (2x+1)² for x=-3,6,9 = 25,169,361
           weighted: 25/6 + 169/2 + 361/3 = 4.17+84.5+120.3 = 209  ✓
```

## 7. Variance (p095-p100)

```
   ┌──────────────────────────────────────────────────────────────┐
   │  Var(X) = σ² = E[(X - μ)²]                                    │
   │  SD     = σ = √Var(X)                                         │
   └──────────────────────────────────────────────────────────────┘
```

```
   Var(X) is ALWAYS non-negative (it is an expectation of a SQUARE).
```

```
   the idea: the SQUARED deviation from the mean, weighted by probability.
   large σ²  <=>  more squared spread around μ
   small σ²  <=>  less squared spread around μ

   Variance measures spread. It is not a universal equivalence to predictability,
   and it is unrelated to the estimator property called consistency.
```

```
   TWO DISTRIBUTIONS, SAME MEAN, DIFFERENT VARIANCE:

     small variance            large variance
        █                         ▃
      ▃ █ ▃           vs        ▃ █ ▃ █ ▃
    ──●──●──●──                 ──●──●──●──●──●──
      ▲ μ                       ▲ μ
    tight around μ             spread out, same centre
```

## 8. The shortcut formula (p101-p103) - and its proof

```
   Var(X) = E[X²] - (E[X])²
```

```
   PROOF:
      Var(X) = E[(X-μ)²]
             = E[X² - 2μX + μ²]            expand the square
             = E[X²] - 2μE[X] + μ²          linearity
             = E[X²] - 2μμ + μ²             since E[X] = μ
             = E[X²] - 2μ² + μ²
             = E[X²] - μ²                   ✓
```

```
  ╔══════════════════════════════════════════════════════════╗
  ║ THE TWO-STEP ROUTINE, ALWAYS:                            ║
  ║   1. E(X)                                                 ║
  ║   2. E(X²)                                                ║
  ║   3. Var = E(X²) - [E(X)]²                                ║
  ║ You almost never use the definition directly.            ║
  ╚══════════════════════════════════════════════════════════╝
```

## 9. Variance transforms (p104-p106)

```
   THEOREM    Var[c] = 0        Var[cX] = c² Var[X]
   PROPOSITION V(aX+b) = a²σ²    σ_{aX+b} = |a| σ_x

   special cases:
       σ_{aX}   = |a| σ_x        scaling changes spread by |a|
       σ_{X+b}  = σ_x            SHIFTING changes nothing
```

```
  ┌────────────────────────────────────────────────────────────┐
  │ WHY |a| AND NOT a                                          │
  │ a may be negative, but a standard deviation cannot be.     │
  │ The sign of a does not affect spread, only scale.          │
  └────────────────────────────────────────────────────────────┘
```

```
   the picture:

      X          shift by b        scale by a
   ──●──●──●──  ─────────▶  ──●──●──●──
     spread s               spread s          <- same spread, moved

   ──●──●──●──  scale by 2  ──────●─────●─────●──────
     spread s                spread 2s         <- doubled
```

## 10. Worked: freezer dealer (p107-p108) - the 6-part chain

```
   x     :  13.5   15.9   19.1     (cubic feet)
   p(x)  :   .2     .5     .3
```

```
   (a) E(X)   = 13.5(.2) + 15.9(.5) + 19.1(.3)
              = 2.70 + 7.95 + 5.73 = 16.38

       E(X²)  = 182.25(.2) + 252.81(.5) + 364.81(.3)
              = 36.45 + 126.405 + 109.443 = 272.298

       V(X)   = 272.298 - (16.38)² = 272.298 - 268.3044 = 3.9936

   (b) price = 25X - 8.5
       E(25X-8.5) = 25(16.38) - 8.5 = 409.5 - 8.5 = 401

   (c) V(25X-8.5) = (25)² V(X) = 625 x 3.9936 = 2496
       (the -8.5 vanishes from the variance)

   (d) actual capacity h(X) = X - .01X²
       E[h(X)] = E(X) - .01 E(X²) = 16.38 - .01(272.298)
               = 16.38 - 2.723 = 13.657 ≈ 13.66
```

```
  ╔═══════════════════════════════════════════════════════════╗
  ║ PART (d) IS THE TRAP PART.                                ║
  ║ E[X - .01X²] is NOT 16.38 - .01(16.38)².                  ║
  ║ You must use E(X²), NOT [E(X)]².                           ║
  ║ This is E[h(X)] ≠ h(E(X)) in numerical form.              ║
  ╚═══════════════════════════════════════════════════════════╝
```

## 11. Worked: magazine orders (p109-p111) - the decision question

```
   x     :  1     2     3     4     5     6
   p(x)  : 1/15  2/15  3/15  4/15  3/15  2/15
```

```
   store pays $1 per copy, sells at $2, leftovers worthless.
   is it better to order 3 or 4?
```

```
   net revenue as a function of demand x:

   x        :   1    2    3    4    5    6
   h3(x)    :  -1    1    3    3    3    3      <- order 3: plateaus at 3
   h4(x)    :  -2    0    2    4    4    4      <- order 4: plateaus at 4
   p(x)     : 1/15 2/15 3/15 4/15 3/15 2/15
```

```
   WHY h3 plateaus: order 3, cost 3, revenue 2 per copy SOLD (max 3 copies)
      x=1: sold 1, revenue 2, cost 3  -> -1
      x=2: sold 2, revenue 4, cost 3  -> +1
      x=3: sold 3, revenue 6, cost 3  -> +3
      x=4: can only sell 3, revenue 6, cost 3 -> +3   (plateau: demand > stock)
```

```
   E[h3(X)] = (-1)(1/15)+(1)(2/15)+(3)(3/15)+(3)(4/15)+(3)(3/15)+(3)(2/15)
            = (-1+2+9+12+9+6)/15 = 37/15 = 2.4667

   E[h4(X)] = (-2)(1/15)+(0)(2/15)+(2)(3/15)+(4)(4/15)+(4)(3/15)+(4)(2/15)
            = (-2+0+6+16+12+8)/15 = 40/15 = 2.6667
```

```
   ┌───────────────────────────────────────────────────────────┐
   │ ORDER 4: higher expected revenue (2.67 vs 2.47)            │
   │ This is a DECISION question: express profit as h(X),       │
   │ take E of each option, compare.                            │
   └───────────────────────────────────────────────────────────┘
```

```
   the two profit curves:

   h(x)
    4 │               ┌──────  h4
    3 │        ┌──────┘
    2 │   ┌────┘
    1 │─┐ │
    0 │ │ │
   -1 │ ▒ │
   -2 │ ▓▒│
      └─┬─┬─┬─┬─┬─┬──▶ x
        1 2 3 4 5 6
      ▓ = h4 only   ▒ = both
```

---
Expectation and variance done. Next: continuous random variables (p112-p147).
