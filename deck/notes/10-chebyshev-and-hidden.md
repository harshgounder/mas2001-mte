# 10 CHEBYSHEV AND THE HIDDEN LAYER (lectures 10-11 + H1-H8)

## PART A: CHEBYSHEV'S INEQUALITY

### 1. The two forms, and why they exist

```
   The theorem slide states BOTH:

   ①  P(|X - μ| ≥ k)       ≤  σ²/k²        (the definition, k in the EVENT)
   ②  P(|X - μ| ≥ k·σ)     ≤  1/k²         (the k-sigma restatement)
```

```
   and the complement form:

   ③  P(|X - μ| < k·σ)     ≥  1 - 1/k²     (for "at least"/"within")
```

```
  ┌───────────────────────────────────────────────────────────────┐
  │  CHEBYSHEV NEEDS ONLY μ AND σ. NO DISTRIBUTION IS ASSUMED.     │
  │  It is always an UPPER BOUND on a TAIL.                        │
  └───────────────────────────────────────────────────────────────┘
```

### 2. The geometry, drawn

```
   the event |X - μ| ≥ kσ is the union of TWO tails:

        ╱‾╲
       ╱   ╲
      ╱     ╲
   ▓▓╯       ╰▓▓
   ──┬───┬───┬──
     μ-kσ μ  μ+kσ
     └────┴────┘
      each tail is part of the event
      Chebyshev says: total tail ≤ 1/k²

   and the complement |X - μ| < kσ is the CENTRE:
        ╱‾╲
       ╱▓▓▓╲
      ╱▓▓▓▓▓╲
   ──┤▓▓▓▓▓▓▓├──
     μ-kσ    μ+kσ
     Chebyshev says: centre ≥ 1 - 1/k²
```

### 3. The thresholds table (memorise these)

```
   ┌────┬────────────┬─────────────────────┐
   │ k  │ 1/k² tail  │ 1 - 1/k² centre     │
   ├────┼────────────┼─────────────────────┤
   │ 1  │ 1.0000     │ 0.0000   (vacuous)  │
   │ 2  │ 0.2500     │ 0.7500   = 3/4      │
   │ 3  │ 0.1111     │ 0.8889   = 8/9      │
   │ 4  │ 0.0625     │ 0.9375   = 15/16    │
   │ 5  │ 0.0400     │ 0.9600   = 24/25    │
   │ 10 │ 0.0100     │ 0.9900   = 99/100   │
   └────┴────────────┴─────────────────────┘
```

```
   the shape of the bound:

   1/k²
    1.0 │█
        │█
    0.5 │█
        │ █
    0.25│ ██
        │   ██
    0.11│     ██
        │       ████
    0.01│           ████████████
        └──┬───┬───┬───┬───────────▶ k
           1   2   3   4   ...     10
    collapses fast, then flattens
```

### 4. The five facts the paper probes (formula sheet section E)

```
   1. only a finite mean and variance are needed, NO distribution assumed
   2. k ≤ 1 gives a vacuous bound (says only "≤ 1")
   3. the bound is an UPPER bound on the tail, so a known-distribution
      question wants BOTH the bound and the exact value
   4. k is measured in STANDARD DEVIATIONS, so convert k = ε/σ first
   5. the exact useful values: k=2 -> 3/4, k=3 -> 8/9, k=4 -> 15/16
```

### 5. WORKED: the corpus questions

```
   ── Q1 (safe) ──────────────────────────────────────────────
   X has E(X) = 3 and E(X²) = 13. Find a lower bound for P(-2<X<8).

       Var = E(X²) - [E(X)]² = 13 - 9 = 4,  σ = 2

       -2<X<8 is |X-3|<5, so k = 5/2 = 2.5
       P(|X-3| ≥ 5) ≤ 4/25
       complement  P(-2<X<8) = P(|X-3|<5) ≥ 21/25
```

```
   ── Q2 (safe) ──────────────────────────────────────────────
   μ = 10, σ² = 4  (so σ = 2)

       P(|X - 10| ≥ 3):   k = 3/2 = 1.5
           bound = 1/k² = 1/2.25 = 0.4444 = 4/9

       complement P(|X-10| < 3) ≥ 1 - 4/9 = 5/9 = 0.5556

       and the C=10 form:  find c so P(|X-10| ≥ c) ≤ 0.04
           1/k² = 0.04  ->  k² = 25  ->  k = 5
           c = k·σ = 5 x 2 = 10
```

```
  ╔═══════════════════════════════════════════════════════════════╗
  ║  ERRATA 15: the deck's Q3 slide is a MESS.                     ║
  ║    - it STATES the row (-1,-1,3,5) with p = 1/6,1/6,1/6,1/2    ║
  ║    - it WORKS the row  (-1,+1,3,5)   (the second value +1)     ║
  ║    - it writes a reciprocal template P(|x-μ|≥k) < k²/σ²        ║
  ║                                                               ║
  ║  USE Q1 AND Q2 ONLY. Do not quote Q3's row.                    ║
  ║  (For the record, the WORKED row gives E=3, E(X²)=43/3,        ║
  ║   Var=16/3, bound 16/3. The STATED row would give E=8/3,       ║
  ║   Var=65/9. They are different distributions.)                 ║
  ╚═══════════════════════════════════════════════════════════════╝
```

```
   ── WORKED: two dice (A1 short Q5) ─────────────────────────
   Var(one die) = 35/12
   Var(sum of two) = 35/12 + 35/12 = 35/6       <- INDEPENDENCE RULE

       P(|X-7| ≥ 3):   k = 3,  σ² = 35/6
           bound = 1/k² = 1/9 ... no wait, use form ①:
           bound = σ²/k² = (35/6)/9 = 35/54 = 0.6481

       exact: sums ≤4 or ≥10 are 12 of 36 outcomes -> 1/3 = 0.3333

       bound holds (0.648 ≥ 0.333) and is much wider, as expected
```

```
   ── WORKED: 600 throws (A1 short Q6) ───────────────────────
   X ~ B(600, 1/6):  μ = 100,  σ² = npq = 600(1/6)(5/6) = 250/3

       P(80 ≤ X ≤ 120) = P(|X-100| ≤ 20)
           ε = 20, k² = ε²/σ² = 400/(250/3) = 1200/250 = 4.8
           Chebyshev directly bounds the strict complement |X-100| > 20
           by at most 5/24, so the inclusive event is at least 19/24.

       exact binomial = 0.9754
```

```
   ── WORKED: marks (A1 app Q4) ──────────────────────────────
   μ = 70, variance = 25  (σ = 5).  P(60 < X < 80)?
       |X-70| < 10,  k = 10/5 = 2
       P ≥ 1 - 1/4 = 0.75
```

### 6. The k-extraction recipe

```
   ┌──────────────────────────────────────────────────────────────┐
   │  1.  get μ and σ (σ = √Var, compute Var if not given)         │
   │  2.  write the event as |X - μ| ≥ ε  or  < ε                  │
   │  3.  k = ε / σ          <- RAW UNITS TO SIGMA UNITS           │
   │  4.  tail form 1/k², or complement 1 - 1/k²                   │
   └──────────────────────────────────────────────────────────────┘
```

## PART B: THE HIDDEN LAYER (H1-H8)

These carry marks and have NO teaching slide. Full treatment in `../11-BEYOND-SLIDES.md`.

```
   ┌────────────────────────────────────────────────────────────────┐
   │ H1  INDEPENDENCE RULES OF RVs                                  │
   │       E(XY) = E(X)E(Y)                  [needs independence]   │
   │       Var(X+Y) = Var(X) + Var(Y)        [needs independence]   │
   │       Var(X-Y) = Var(X) + Var(Y)        [the minus STAYS PLUS] │
   │       E(X+Y) = E(X) + E(Y)              [ALWAYS, no condition] │
   │                                                                │
   │     gates: dice-sum variance, Var(X̄), estimator variances,     │
   │            Poisson additivity, every CLT SE                    │
   └────────────────────────────────────────────────────────────────┘

   ┌────────────────────────────────────────────────────────────────┐
   │ H2  CHEBYSHEV (the whole topic) - taught only in the L10-11    │
   │     deck, which arrived 15 Sep. Graded 9+ times.               │
   └────────────────────────────────────────────────────────────────┘

   ┌────────────────────────────────────────────────────────────────┐
   │ H3  MEMORYLESS  P(T>s+t | T>s) = P(T>t)                        │
   │     exponential never ages. P(T>t)=e^(-lambda t).              │
   │     graded: A2 MCQ Q5, A2 section C Q1.                        │
   └────────────────────────────────────────────────────────────────┘

   ┌────────────────────────────────────────────────────────────────┐
   │ H4  NORMAL LANDMARKS  68.27 / 95.45 / 99.73 within 1,2,3 sigma  │
   │     graded: A2 MCQ Q11.                                        │
   └────────────────────────────────────────────────────────────────┘

   ┌────────────────────────────────────────────────────────────────┐
   │ H5  EXPECTED COUNT = N x P                                      │
   │     "out of N items, how many do we expect"                     │
   │     graded: A1 app, A2 B4 (5000 batteries), A2 D1 (10000 bulbs),│
   │             the 0.5499 die question, ETE family.                │
   │     TRAP: report N x P, not P.                                  │
   └────────────────────────────────────────────────────────────────┘

   ┌────────────────────────────────────────────────────────────────┐
   │ H6  GEOMETRIC  E(X) = 1/p   (counts trials to first success)    │
   │     graded: A1 short Q4 (E = 2).                                │
   └────────────────────────────────────────────────────────────────┘

   ┌────────────────────────────────────────────────────────────────┐
   │ H7  HYPERGEOMETRIC MEAN = nK/N   (draws WITHOUT replacement)    │
   │     graded: A1 long Q3 (4 x 5/25 = 0.80 exactly, both cases)    │
   │     note it EQUALS the binomial mean np at the same p.          │
   └────────────────────────────────────────────────────────────────┘

   ┌────────────────────────────────────────────────────────────────┐
   │ H8  THE TWO NORMAL TABLE CONVENTIONS  φ(z) vs F(z)              │
   │     φ(z) = area from 0 to z;  F(z) = cumulative from -∞         │
   │     differ by 0.5 for z > 0.  DECIDE FIRST.                     │
   └────────────────────────────────────────────────────────────────┘
```

### The hidden-layer study order and cost

```
   priority   item   why                                  time
   ─────────────────────────────────────────────────────────────
   1          H2     highest mark count (9+), gates nothing but  30m
                     is itself a whole topic
   2          H1     gates 4 downstream topics                   25m
   3          H8     every normal/CLT numeric                    15m
   4          H3     2 graded uses, one line to state            10m
   5          H5     graded repeatedly, one idea                 10m
   6          H6     1 graded use                                 5m
   7          H7     1 graded use                                 5m
   8          H4     1 graded use, pure recall                    5m
   ─────────────────────────────────────────────────────────────
              TOTAL ≈ 1h45
```

```
  ╔═══════════════════════════════════════════════════════════════╗
  ║  WHY THIS BLOCK IS THE BEST-SPENT TIME BEFORE THE PAPER:       ║
  ║  it is the part of the syllabus that the slides UNDER-TAUGHT   ║
  ║  but the papers KEEP ASKING. Cheapest marks available.         ║
  ╚═══════════════════════════════════════════════════════════════╝
```

---
End of the notes. Back to `00-NOTES-INDEX.md` for the map, or `../00-INDEX.md` for the reference deck.
