# 05 CONTINUOUS RANDOM VARIABLES (notes p112-p147)

## 1. Why continuous needs new machinery (p113-p116)

```
   T = time of peak electricity demand at a power plant
   - cannot be limited to a countable list of times
   - T can take ANY value in [0, 24)
   - P(peak at exactly 12.013278...) = 0 in a continuous model
```

```
  ┌───────────────────────────────────────────────────────────────┐
  │  A random variable is CONTINUOUS if it can assume any value   │
  │  in some interval, AND the probability of any specific single │
  │  value is 0.                                                  │
  └───────────────────────────────────────────────────────────────┘
```

## 2. The probability density function, pdf (p117)

```
   f(x) is a pdf if:
      (i)   f(x) ≥ 0
      (ii)  ∫_{-∞}^{+∞} f(x) dx = 1
      (iii) P(a ≤ X ≤ b) = ∫_{a}^{b} f(x) dx
```

```
   ┌──────────────────────────────────────────────────────────────┐
   │  f(x) IS A DENSITY, NOT A PROBABILITY.                        │
   │  f(x) can be GREATER THAN 1.                                  │
   │  e.g. uniform on width 0.5  ->  f = 1/0.5 = 2                  │
   │  only its INTEGRAL is a probability.                          │
   └──────────────────────────────────────────────────────────────┘
```

```
   P(a ≤ X ≤ b) = AREA under the density curve between a and b:

        f(x)
         │      ╱‾‾‾╲
         │     ╱     ╲
         │    ╱ ┌───┐ ╲
         │   ╱  │▓▓▓│  ╲
         └──┴───┴───┴───┴──▶ x
            a       b
              the shaded AREA = P(a≤X≤b)
```

## 3. The five remarks (p119-p123) - each is a possible true/false

```
   R1  if ∫ f = k and k ≠ 1, then f(x)/k IS the pdf
       (this is how you "find k" - normalise)

   R2  X takes all values in (a,b), where a,b may be -∞,+∞

   R3  P[X = x0] = ∫ from x0 to x0 f dx = 0    (zero width, zero area)

   R4  probability zero does NOT mean impossible for continuous rv
       P(A) = 0 does NOT imply A = ∅     <- subtle, examinable

   R5  if X only lives in [a,b], set f(x) = 0 for all x outside [a,b]
       (the SUPPORT convention)
```

```
  ╔═══════════════════════════════════════════════════════════╗
  ║ R3 + R4 TOGETHER:                                          ║
  ║   P(X = c) = 0  for every point c                          ║
  ║   yet SOME point must occur                                ║
  ║   so "probability 0" and "impossible" are DIFFERENT here   ║
  ║   and P(a<X<b) = P(a≤X≤b) exactly (endpoints free)         ║
  ╚═══════════════════════════════════════════════════════════╝
```

## 4. Worked: f(x)=2x (p124-p125)

```
   f(x) = 2x,  0 < x < 1,   0 elsewhere
```

```
   CHECK it is a pdf:
      f(x) ≥ 0  ✓
      ∫_{-∞}^{∞} f = ∫_0^1 2x dx = [x²]_0^1 = 1  ✓
```

```
   P[X ≤ 1/2] = ∫_0^{1/2} 2x dx = [x²]_0^{1/2} = 1/4
```

```
   the density f(x)=2x rises linearly:

   f(x)
    2 │          ╱
      │        ╱
      │      ╱
      │    ╱
    0 └──╱────────▶ x
       0            1
      (more mass near 1)
```

## 5. Worked: continuous conditional (p126)

```
   P[X ≤ 1/2 | 1/3 ≤ X ≤ 2/3]

        P[1/3 ≤ X ≤ 1/2]     ∫_{1/3}^{1/2} 2x dx
      = ───────────────── = ────────────────────
        P[1/3 ≤ X ≤ 2/3]     ∫_{1/3}^{2/3} 2x dx

        (1/4 - 1/9)      (5/36)
      = ───────────── = ───────── = 5/12
        (4/9 - 1/9)      (1/3)
```

```
  ┌───────────────────────────────────────────────────────────┐
  │ CONDITIONAL IN THE CONTINUOUS WORLD: fraction of AREAS.    │
  │ Same rule P(A|B)=P(A∩B)/P(B), but P's are integrals.       │
  │ This exact shape is re-asked on the ETE S4 paper.          │
  └───────────────────────────────────────────────────────────┘
```

## 6. Worked: bus waiting time, Y (p127-p129) - the 6-part monster

```
   two buses, each wait ~ U(0,5), total wait Y has pdf:

   f(y) =  y/25          0 ≤ y < 5
          2/5 - y/25     5 ≤ y ≤ 10
          0              otherwise
```

```
   the triangular density:

   f(y)
   0.2 │            ▲
       │           ╱ ╲
       │          ╱   ╲
       │         ╱     ╲
       │        ╱       ╲
     0 └───────╱─────────╲──────▶ y
       0       5         10
       rising      falling
```

```
   (b) VERIFY total area = 1:
       ∫_0^5 y/25 dy + ∫_5^10 (2/5 - y/25) dy
       = [y²/50]_0^5 + [2y/5 - y²/50]_5^10
       = (25/50) + [(4 - 2) - (2 - 1/2)]
       = 1/2 + [2 - 1.5] = 1/2 + 1/2 = 1  ✓

   (c) P(Y ≤ 3) = ∫_0^3 y/25 dy = [y²/50]_0^3 = 9/50 = 0.18

   (d) P(Y ≤ 8) = ∫_0^5 y/25 + ∫_5^8 (2/5 - y/25)
                = 1/2 + [2y/5 - y²/50]_5^8
                = 1/2 + [(3.2-1.28) - (2-0.5)]
                = 1/2 + [1.92 - 1.5] = 1/2 + 0.42 = 0.92

   (e) P(3 ≤ Y ≤ 8) = P(Y≤8) - P(Y<3) = 46/50 - 9/50 = 37/50 = 0.74

   (f) P(Y<2 or Y>6) = ∫_0^2 y/25 dy + ∫_6^10 (2/5 - y/25) dy
                     = 4/50 + 32/50 = 0.08 + 0.32 = 0.40 = 2/5
```

```
  ╔══════════════════════════════════════════════════════════════╗
  ║ ERRATA 13: the slide's working for (f) prints the first       ║
  ║ integral bound as 3, not 2, which contradicts its own stated  ║
  ║ event "Y<2". The final answer 2/5 = 0.40 is still correct     ║
  ║ for "Y<2 or Y>6". Use 0.08 + 0.32 = 0.40.                     ║
  ╚══════════════════════════════════════════════════════════════╝
```

```
   the (e) picture:

   f(y)
       │      ▲
       │     ╱ ╲
       │    ╱   ╲
       │   ╱     ╲
       │  ╱       ╲
       └─┬──┬──────┬─┬──▶ y
         3  5      8
         └───▓▓▓▓▓▓──┘
           P(3≤Y≤8) = 0.74
```

## 7. The cdf for continuous (p131-p134)

```
   F(x) = P(X ≤ x) = ∫_{-∞}^{x} f(y) dy
```

```
   F(x) = the AREA to the LEFT of x

        f(x)
         │    ╱‾‾╲
         │   ╱    ╲
         │  ╱ ┌────╲
         │ ╱  │▓▓▓▓▓╲
         └─┴──┴─────┴──▶ x
                ▲ x
           the shaded area = F(x)
```

```
   F(x) is a smooth S-curve (not a staircase like the discrete cdf):

   F(x)
   1.0 │              ┌────────
       │           ╱‾‾
   0.5 │        ╱
       │     ╱‾
   0.0 ├────╱
       └──────────────▶ x
           smooth rise, no jumps
```

## 8. Using F(x) (p134-p135)

```
   P(X > a)     = 1 - F(a)
   P(a ≤ X ≤ b) = F(b) - F(a)
```

```
  ╔═══════════════════════════════════════════════════════════╗
  ║ CONTINUOUS vs INTEGER: the SAME theorem has two forms      ║
  ║   continuous :  P(a ≤ X ≤ b) = F(b) - F(a)                 ║
  ║   integer rv :  P(a ≤ X ≤ b) = F(b) - F(a-1)    <- the a-1 ║
  ╚═══════════════════════════════════════════════════════════╝
```

```
   why the a-1:
       continuous: F(a) excludes the zero-width point a  -> fine
       integer   : F(a) INCLUDES the value a             -> must drop it
```

## 9. Getting f from F (p136-p137)

```
   for discrete : pmf = DIFFERENCE of two cdf values
   for an absolutely continuous distribution: pdf = DERIVATIVE of the cdf

        F'(x) = f(x)          where F is differentiable
```

## 10. Worked: find the cdf, exercise 1 (p138)

```
  (i) f(x) = 1/3  0 ≤ x ≤ 1
             2/3  1 < x ≤ 2
             0    elsewhere
```

```
   CHECK: ∫_0^1 1/3 dx + ∫_1^2 2/3 dx = 1/3 + 2/3 = 1  ✓

   F(x) = 0                 x < 0
          x/3               0 ≤ x ≤ 1     (∫_0^x 1/3 du = x/3)
          1/3 + 2(x-1)/3    1 < x ≤ 2     (1/3 + ∫_1^x 2/3 du)
          1                 x > 2
```

```
  (ii) f(x) = |x|,  -1 < x < 1

   split at 0 because of the absolute value:

   F(x) = 0                       x ≤ -1
          ∫_{-1}^{x} (-u) du       -1 < x ≤ 0    = (1 - x²)/2
          ∫_{-1}^{0}(-u)du + ∫_0^x u du  0 < x < 1  = (1 + x²)/2
          1                       x ≥ 1
```

```
   the |x| density is a V:

   f(x)
    1 │╲          ╱
      │ ╲        ╱
      │  ╲      ╱
      │   ╲    ╱
    0 └────╲╱──────▶ x
        -1   0   1
```

## 11. Worked: cdf to pdf (p139) - the reverse direction

```
   F(x) = 0                 x < 1
          (x-1)^4 / 16      1 ≤ x ≤ 3
          1                 x > 3
```

```
   (i) DENSITY = derivative:
       f(x) = d/dx [ (x-1)^4/16 ] = 4(x-1)³/16 = (x-1)³/4,   1 ≤ x ≤ 3
              0 elsewhere

   (ii) P(2 ≤ X ≤ 3) = F(3) - F(2)
                     = 1 - (2-1)^4/16
                     = 1 - 1/16 = 15/16
```

```
  ┌──────────────────────────────────────────────────────────┐
  │ USING F IS THE FAST ROUTE. If the question gives F, do    │
  │ NOT integrate the density you just found. Just subtract   │
  │ two F values.                                             │
  └──────────────────────────────────────────────────────────┘
```

## 12. Expected values, continuous (p140-p144)

```
   summation  ->  integration
   pmf        ->  pdf

   E(X)     = ∫_{-∞}^{∞} x f(x) dx
   E[h(X)]  = ∫_{-∞}^{∞} h(x) f(x) dx
   E(aX+b)  = a E(X) + b            (same linear rule)
   Var(X)   = ∫ (x-μ)² f(x) dx = E(X²) - [E(X)]²
   σ        = √Var(X)
```

## 13. Worked: hospitalization, Y=X+4 (p142) - and its ETE sibling

```
   Y = X + 4, where f(x) = 32/(x+4)³,  x > 0
   find E(Y)
```

```
   E(Y) = E(X+4) = E(X) + 4

   E(X) = ∫_0^∞ x · 32/(x+4)³ dx

   substitute u = x+4, x = u-4, dx = du,  limits 4 → ∞:

        = 32 ∫_4^∞ (u-4)/u³ du
        = 32 ∫_4^∞ (u^{-2} - 4u^{-3}) du
        = 32 [ -u^{-1} + 2u^{-2} ]_4^∞
        = 32 [ 0 - (-1/4 + 2/16) ]
        = 32 [ 1/4 - 1/8 ] = 32 (1/8) = 4

   E(Y) = 4 + 4 = 8 days
```

```
  ┌──────────────────────────────────────────────────────────┐
  │ THE TRICK:  Y = X + 4, so use the SHIFT rule.              │
  │ Do NOT integrate (x+4) against the density.                │
  │ E(X+4) = E(X) + 4 is one line.                             │
  └──────────────────────────────────────────────────────────┘
```

## 14. Worked: Pareto density (p146-p147)

```
   f(x) = k/x^(k+1),  x ≥ 1,   k > 0
```

```
   normalise: ∫_1^∞ k x^{-(k+1)} dx = k [ -x^{-k}/k ]_1^∞ = 1  ✓

   E(X) exists only if k > 1    (otherwise the integral diverges)
   Var exists only if k > 2
```

```
  ╔═════════════════════════════════════════════════════════════╗
  ║ THE CONVERGENCE CONDITION IS EXAMINABLE.                     ║
  ║ A heavy tail can make E(X) or Var(X) INFINITE.               ║
  ║ Always check the exponent condition before claiming a mean.  ║
  ╚═════════════════════════════════════════════════════════════╝
```

## 15. The continuous toolkit, one block

```
   ┌──────────────────┬──────────────────────────────────────┐
   │ check a pdf      │ ∫ over support = 1                    │
   │ find k           │ set up that integral = 1, solve       │
   │ P(a≤X≤b)         │ ∫_a^b f, or F(b)-F(a)                 │
   │ cdf              │ ∫_{-∞}^{x} f                          │
   │ pdf from cdf     │ f = F'                                │
   │ E(X)             │ ∫ x f(x) dx                           │
   │ Var(X)           │ E(X²) - [E(X)]²                       │
   │ conditional      │ ratio of two integrals                │
   └──────────────────┴──────────────────────────────────────┘
```

---
That is the whole continuous part. Next: the two named discrete distributions.
