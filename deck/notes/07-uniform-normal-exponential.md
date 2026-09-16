# 07 UNIFORM, NORMAL, EXPONENTIAL (ppt4, 44 pages, lectures 14-16)

## The family tree first (p001)

```
                    PROBABILITY DISTRIBUTIONS
                              │
        ┌─────────────────────┴─────────────────────┐
        │                                           │
   DISCRETE                                   CONTINUOUS
        │                                           │
   ┌────┴────┐                        ┌─────────┬────┴────┬──────────┐
   │         │                        │         │         │          │
 BINOMIAL  POISSON                UNIFORM   NORMAL   EXPONENTIAL
 (lect 12) (lect 13)              (lect 14) (lect 15)  (lect 16)
```

## PART A: UNIFORM (p002-p006) - lecture 14

### 1. Definition

```
  ┌───────────────────────────────────────────────────────────────┐
  │ "equal probabilities for all possible outcomes"                │
  │                                                                │
  │   f(x) = 1/(b-a)      a ≤ x ≤ b                                │
  │   f(x) = 0            otherwise                                │
  └───────────────────────────────────────────────────────────────┘
```

```
   the flat rectangle:

   f(x)
   1/(b-a) ┌─────────────────────┐
           │                     │
           │    area = 1.0       │
           │                     │
         0 └─────────────────────┴──▶ x
           a                     b

   the area is width x height = (b-a) x 1/(b-a) = 1  ✓
```

### 2. Properties

```
        μ = (a + b)/2
        σ² = (b - a)²/12          (the 12 is FIXED)
```

```
  ┌──────────────────────────────────────────────────────────┐
  │ THE LENGTH-RATIO SHORTCUT: probability = interval length   │
  │ divided by total length. No integration needed.            │
  │   P(c ≤ X ≤ d) = (d - c)/(b - a)                           │
  └──────────────────────────────────────────────────────────┘
```

### 3. WORKED: U(2,6) (p004-p006)

```
   f(x) = 1/(6-2) = 0.25,   2 ≤ x ≤ 6

   μ  = (2+6)/2 = 4
   σ² = (6-2)²/12 = 16/12 = 1.333
```

```
   P(3 < X < 5) = length ratio = (5-3)/(6-2) = 2/4 = 0.50
```

```
   ┌────────────────────────────────────────┐
   │                                        │
 0.25│      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓              │
   │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓              │
   │      ░░░░▓▓▓▓▓▓▓▓▓▓▓▓░░░   <- shaded   │
   └──────┴────┴─────────┴────┴────▶ x
          2    3         5    6

   P = shaded / total = 2/4 = 0.50
```

## PART B: NORMAL (p007-p037) - lecture 15

### 4. Shape facts (p008-p010)

```
  ┌──────────────────────────────────────────────────────────────┐
  │  BELL SHAPED                                                 │
  │  SYMMETRICAL                                                 │
  │  MEAN = MEDIAN = MODE = μ                                    │
  │  range: -∞ to +∞                                             │
  │  location set by μ, spread set by σ                          │
  └──────────────────────────────────────────────────────────────┘
```

```
   changing μ shifts:            changing σ widens:

      ╱‾╲        ╱‾╲                  ╱╲         ╱‾‾╲
     ╱   ╲      ╱   ╲               ╱  ╲       ╱    ╲
   ──┴─────┴─────────────         ──┴──────────┴──────
     μ1    μ2                        tall,narrow  short,wide
     (same shape, moved)            (same centre, different spread)
```

### 5. The notation and the density (p010-p011)

```
        X ~ N(μ, σ²)

        ╔═══════════════════════════════════════════════════╗
        ║  THE SECOND SLOT IS THE **VARIANCE**, not the SD   ║
        ║  "mean 70, variance 25"  ->  μ=70, σ²=25, σ=5      ║
        ║  ALWAYS square-root it before a z-score.           ║
        ╚═══════════════════════════════════════════════════╝

        f(x) = 1/(σ√(2π)) · e^{-(x-μ)²/(2σ²)}
```

### 6. The cdf and interval (p012-p013)

```
        F(x₀) = P(X ≤ x₀)          (area to the left)

        P(a < X < b) = F(b) - F(a)
```

```
   the subtraction picture:

      ╱‾╲                  ╱‾╲                  ╱‾╲
     ╱   ╲       =        ╱▓▓▓▓╲     -         ╱▓▓╲
   ──┴──┴──┴──          ──┴──┴──┴──          ──┴──┴──┴──
     a  μ  b               a  μ  b              a  μ  b
   P(a<X<b)          F(b) (all left         F(a) (left
                      of b)                  of a)
```

### 7. Standardisation (p014-p015)

```
        Z = (X - μ)/σ         Z ~ N(0, 1)
```

```
   WORKED: μ=100, σ=50, X=200
        Z = (200-100)/50 = 2.0
```

```
   the two scales, same shape:

      X scale:   100                200
                 │                  │
                 ●──────────────────●
                 │                  │
   ──────────────┴───────...────────┴───────────
                 ●──────────────────●
      Z scale:   0                  2.0

   "the distribution is the same, only the SCALE has changed"
```

### 8. THE TWO TABLES - the biggest trap in the whole paper (p022-p023)

```
  ╔═══════════════════════════════════════════════════════════════╗
  ║  THE SLIDES SHOW **TWO DIFFERENT TABLES** AND THEY LOOK ALIKE  ║
  ║                                                               ║
  ║  TABLE 1 (p022, "Areas under Normal Curve"):                   ║
  ║     gives  P(0 < Z < z)     = area FROM THE CENTRE to z        ║
  ║     φ(z). e.g. z=2.0 -> 0.4772                                 ║
  ║                                                               ║
  ║  TABLE 2 (p022 top, standard statistical tables):              ║
  ║     gives  P(Z < z)         = CUMULATIVE from -∞ to z          ║
  ║     F(z). e.g. z=0.0 -> 0.5000, z=2.0 -> 0.9772                ║
  ║                                                               ║
  ║  THEY DIFFER BY 0.5 FOR z > 0:                                 ║
  ║     F(z) = 0.5 + φ(z)                                          ║
  ║     0.9772 = 0.5 + 0.4772  ✓                                  ║
  ║                                                               ║
  ║  DECIDE WHICH TABLE THE QUESTION GIVES **BEFORE** SUBSTITUTING ║
  ╚═══════════════════════════════════════════════════════════════╝
```

```
   the two areas, drawn:

     φ(z) = P(0<Z<z)                  F(z) = P(Z<z)
        ╱‾╲                              ╱‾╲
       ╱▓▓▓╲                            ╱▓▓▓▓▓╲
     ──┴───┴──                        ──┴─────┴──
       0   z                           -∞     z
       centre to z                     everything to z
```

### 9. Symmetry facts (p024-p025)

```
        P(Z < -2.00) = 1 - P(Z < 2.00) = 1 - 0.9772 = 0.0228
        Φ(-z) = 1 - Φ(z)
        P(Z > z) = 1 - Φ(z)
```

```
   the mirror picture:

        ╱‾╲                     ╱‾╲
       ╱▓▓▓╲                   ╱░░░╲
     ──┴───┴──               ──┴───┴──
      -2.0  0                 0   2.0
      left tail .0228         right tail .0228

   the left tail at -z EQUALS the right tail at +z
```

### 10. WORKED: the 8.6 chain (p028-p033)

```
   X ~ N(8.0, 5.0²)      [note: σ = 5.0]
```

```
   (a) FIND P(X < 8.6):
       Z = (8.6 - 8.0)/5.0 = 0.12
       P(X<8.6) = P(Z<0.12) = F(0.12) = 0.5478

   (b) FIND P(X > 8.6):
       P(X>8.6) = 1 - 0.5478 = 0.4522
```

```
   the two areas:

        ╱‾╲                      ╱‾╲
       ╱▓▓▓╲░░                  ╱░░░╲▓▓▓
     ──┴───┴──┴──              ──┴───┴──┴──
      8.0 8.6                   8.0 8.6
      P(X<8.6)=.5478            P(X>8.6)=.4522
```

```
  ERRATA 8: the figure on p030 labels the curve "σ = 10", but the
  arithmetic on the same page divides by 5.0. Use σ = 5.0.
```

### 11. WORKED: the inverse, 20% lower tail (p034-p037)

```
   Find x so that only 20% of values are BELOW x.
```

```
   STEP 1: find z for a 20% lower tail
        look for F(z) = 0.20
        from the table, z ≈ -0.84   (exactly -0.8416)

   STEP 2: CONVERT BACK TO X    ← the forgotten step
        X = μ + Zσ = 8.0 + (-0.84)(5.0) = 8.0 - 4.2 = 3.80
```

```
  ╔══════════════════════════════════════════════════════════════╗
  ║ THE INVERSE HAS TWO STEPS AND PEOPLE STOP AFTER STEP 1.      ║
  ║ Getting z = -0.84 is HALF the answer.                        ║
  ║ The mark is in X = μ + zσ.                                   ║
  ╚══════════════════════════════════════════════════════════════╝
```

```
   the picture:

        ╱‾╲
       ╱░░╲▓▓▓▓▓
     ──┴───┴──────
     3.80  8.0
      .20   .80
     ▲
   z=-0.84
```

### 12. The landmarks (the hidden item H4)

```
        within 1σ : 68.27%
        within 2σ : 95.45%
        within 3σ : 99.73%
```

```
        ╱‾╲
       ╱▒▒▒╲
      ╱▒▒▒▒▒╲
     ─┴──┴──┴─
     -1  0  +1      68.27%
    ──┴────┴──
    -2    0    +2   95.45%
   ───┴──────┴───
   -3     0      +3 99.73%
```

## PART C: EXPONENTIAL (p038-p043) - lecture 16

### 13. What it models

```
  ┌───────────────────────────────────────────────────────────────┐
  │ the LENGTH OF TIME between two occurrences of an event          │
  │ (the time between arrivals)                                    │
  └───────────────────────────────────────────────────────────────┘

   examples: trucks at a dock, transactions at an ATM, phone calls
```

### 14. The density and its parameters (p040-p041)

```
        f(t) = λ e^{-λt},    t > 0
        μ = 1/λ              σ² = 1/λ²
        F(t) = 1 - e^{-λt}   (the cdf)
        P(T > t) = e^{-λt}   (the tail)
```

```
  ╔═══════════════════════════════════════════════════════════════╗
  ║  ERRATA 4: the slide on p040 says "1/λ is the MEAN NUMBER of   ║
  ║  occurrences per unit time". THAT IS BACKWARDS.                ║
  ║     λ   = the rate (occurrences per unit time)                 ║
  ║     1/λ = the mean TIME between occurrences                    ║
  ║  p041 states it correctly as μ = 1/λ.                          ║
  ╚═══════════════════════════════════════════════════════════════╝
```

```
   THE DECAY PICTURE:

   f(t)
   λ  │█╲
      │█ ▲╲
      │█   ▲╲
      │█     ▲╲___
      │█          ▲───────
    0 └─────────────────────────▶ t
      0
      tallest at 0, decays forever (never reaches 0)
```

```
   the cdf rises toward 1:

   F(t)
   1 │              ┌──────
     │           ╱‾‾
     │        ╱‾
     │     ╱‾
   0 ├───╱
     └─────────────────────▶ t
       rises fast, then flattens
```

### 15. WORKED: arrivals at 15 per hour (p042-p043)

```
   "customers arrive at the rate of 15 per hour.
    P(the arrival time between consecutive customers < 3 minutes)?"
```

```
   λ = 15 per HOUR
   3 minutes = 0.05 hours         <- CONVERT THE UNIT
   P(T < 0.05) = 1 - e^{-λt}
               = 1 - e^{-(15)(0.05)}
               = 1 - e^{-0.75}
               = 1 - 0.4724 = 0.5276
```

```
  ╔══════════════════════════════════════════════════════════════╗
  ║  THE UNIT CONVERSION IS THE WHOLE QUESTION.                  ║
  ║  λ is per hour, so t MUST be in hours.                       ║
  ║  3 min = 0.05 hr.                                            ║
  ║  This is the trap the setter builds into almost every        ║
  ║  exponential story (errata families E24S4, A2 D2).           ║
  ╚══════════════════════════════════════════════════════════════╝

   the mean gap = 1/λ = 1/15 hour = 4 minutes
```

### 16. The memoryless property (hidden item H3)

```
        P(T > s + t | T > s) = P(T > t)
```

```
  ┌───────────────────────────────────────────────────────────────┐
  │  "surviving s MORE, given you already survived to now,         │
  │   is the same as surviving s from scratch"                     │
  │                                                                │
  │  the exponential NEVER AGES. A used part is as good as new.    │
  │  (unlike, say, a lightbulb that wears out)                     │
  └───────────────────────────────────────────────────────────────┘
```

```
   PROOF SKETCH:
     P(T>s+t | T>s) = P(T>s+t and T>s) / P(T>s)
                    = P(T>s+t) / P(T>s)
                    = e^{-λ(s+t)} / e^{-λs}
                    = e^{-λt}  =  P(T>t)   ✓

     the e^{-λs} cancels  <- the whole trick
```

```
   the canonical number: e^{-1} = 0.3679
```

## THE THREE CONTINUOUS DISTRIBUTIONS, ONE TABLE

```
   ┌───────────┬─────────────┬──────────────┬─────────────────┐
   │           │ UNIFORM     │ NORMAL       │ EXPONENTIAL     │
   ├───────────┼─────────────┼──────────────┼─────────────────┤
   │ pdf       │ 1/(b-a)     │ 1/(σ√2π)e^.. │ λe^{-λt}        │
   │ mean      │ (a+b)/2     │ μ            │ 1/λ             │
   │ variance  │ (b-a)²/12   │ σ²           │ 1/λ²            │
   │ cdf       │ (x-a)/(b-a) │ table        │ 1-e^{-λt}       │
   │ tail      │ ratio       │ 1-Φ(z)       │ e^{-λt}         │
   │ parameter │ a,b         │ μ,σ²         │ λ (a RATE)      │
   │ models    │ random pt   │ measurement  │ waiting time    │
   └───────────┴─────────────┴──────────────┴─────────────────┘
```

```
   the three shapes side by side:

   UNIFORM          NORMAL           EXPONENTIAL
   ┌───────┐         ╱‾╲             █╲
   │       │        ╱   ╲            █ ▲╲
   │       │       ╱     ╲           █   ▲╲___
   └───────┘      ─╯       ╰─        █        ▲─────
   flat           bell              decay
   "equally       "measurement      "waiting
    likely"        error"            time"
```

---
Next: sampling and the Central Limit Theorem.
