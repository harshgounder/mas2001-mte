# 08 SAMPLING AND THE CENTRAL LIMIT THEOREM (lms-standard-error-clt, 19 pages, lectures 17-18)

## 1. Population vs sample (p001-p002)

```
   ┌────────────────────────────┬──────────────────────────────┐
   │ POPULATION (N)             │ SAMPLE (n)                    │
   ├────────────────────────────┼──────────────────────────────┤
   │ the ENTIRE group you want  │ a smaller subset, collected   │
   │ to draw conclusions about  │ to observe and analyse        │
   ├────────────────────────────┼──────────────────────────────┤
   │ described by PARAMETERS    │ described by STATISTICS       │
   │   μ, σ                     │   X̄, s                       │
   ├────────────────────────────┼──────────────────────────────┤
   │ often too large / costly   │ must be representative and    │
   │ / impossible to measure    │ randomly selected             │
   ├────────────────────────────┼──────────────────────────────┤
   │ e.g. all 500,000 bulbs     │ e.g. 100 randomly chosen      │
   └────────────────────────────┴──────────────────────────────┘
```

```
  ╔══════════════════════════════════════════════════════════════╗
  ║ PARAMETER vs STATISTIC - the words the exam checks            ║
  ║   PARAMETER = a number about the POPULATION (μ, σ, p)         ║
  ║   STATISTIC = a number computed FROM THE SAMPLE (X̄, s, p̂)     ║
  ║   The parameter is UNKNOWN (that is why we sample).           ║
  ║   The statistic is KNOWN (we compute it).                     ║
  ╚══════════════════════════════════════════════════════════════╝
```

## 2. Simple random sampling, the picture (p003)

```
   population (10 items)          simple random samples (without replacement)
   ┌───────────────┐
   │ ■ ■ □ □ □     │ ─────┐
   │ □ ■ ■ □ □     │      │      ┌───┬───┬───┬───┐
   └───────────────┘      ├─────▶│ a │ c │ j │ b │
     a b c d e            │      └───┴───┴───┴───┘
     f g h i j            │      ┌───┬───┬───┬───┐
                          ├─────▶│ i │ e │ a │ f │
                          │      └───┴───┴───┴───┘
                          │      ┌───┬───┬───┬───┐
                          └─────▶│ g │ c │ f │ d │
                                 └───┴───┴───┴───┘
   ■ = the sampled items are spread randomly, NOT clustered
     "without replacement" = once picked, an item is not put back
```

## 3. Standard error (p004)

```
  ┌───────────────────────────────────────────────────────────────┐
  │ STANDARD ERROR measures the variability of a STATISTIC         │
  │ (usually the sample mean) across multiple hypothetical         │
  │ samples. It quantifies how much the estimate deviates from     │
  │ the true parameter.                                            │
  └───────────────────────────────────────────────────────────────┘

        SE = σ / √n
```

```
   ┌──────────────────────────────────────────────────────────┐
   │  KEY: as n increases, SE DECREASES.                        │
   │  Larger samples -> more precise estimates.                 │
   └──────────────────────────────────────────────────────────┘
```

```
   the shrinking spread:

   n small          n medium          n large
     ╱‾╲               ╱╲               │
    ╱   ╲             ╱  ╲              │
   ─╯     ╰─        ──╯    ╰──         ─┴─
   wide SE           narrower          very narrow SE
   (imprecise)                        (precise)
```

## 4. WORKED: lightbulbs (p005)

```
   σ = 100 hours.
```

```
   Case 1: n = 25    SE = 100/√25  = 100/5  = 20 hours
   Case 2: n = 100   SE = 100/√100 = 100/10 = 10 hours
```

```
  ╔══════════════════════════════════════════════════════════════╗
  ║  THE SQRT RULE, memorise it:                                 ║
  ║  QUADRUPLING n HALVES the SE                                 ║
  ║     25 -> 100 is x4, so SE goes 20 -> 10 (halved)            ║
  ║  this is the answer to every "how large a sample" question   ║
  ╚══════════════════════════════════════════════════════════════╝
```

## 5. The Central Limit Theorem (p007-p010)

```
  ┌───────────────────────────────────────────────────────────────┐
  │ "If you take sufficiently large samples from a population,     │
  │  the distribution of the SAMPLE MEANS will follow a normal     │
  │  distribution, REGARDLESS of the population's underlying       │
  │  shape (even if heavily skewed, uniform, or bimodal)."        │
  └───────────────────────────────────────────────────────────────┘
```

```
   THREE RULES:
      1. CENTRE   mean of the sample means = μ       (μ_X̄ = μ)
      2. SPREAD   sd of the sample means = σ/√n      (σ_X̄ = σ/√n)
      3. SHAPE    as n increases the shape becomes normal;
                  n ≥ 30 is the course rule of thumb
```

## 6. THE THREE CASES - the applicability conditions (p008)

```
  ╔═══════════════════════════════════════════════════════════════╗
  ║  1. NON-NORMAL population, large n                              ║
  ║        -> sample means may be approximately Normal(μ, σ/√n)     ║
  ║        n ≥ 30 is the course heuristic, not a theorem cutoff     ║
  ║                                                                ║
  ║  2. n ≤ 30 AND the population IS normal                        ║
  ║        -> sample means are EXACTLY Normal(μ, σ/√n)             ║
  ║                                                                ║
  ║  3. Small n AND the population is NOT normal                    ║
  ║        -> do not assume a normal approximation without evidence ║
  ╚═══════════════════════════════════════════════════════════════╝
```

```
   the decision tree:

              read the question
                    │
             is the pop normal?
              ┌─────┴─────┐
             YES          NO
              │            │
         USE IT AT       is n large enough for
         ANY n           this population shape?
          (exact)          ┌───┴───┐
                          YES      NO
              │            │        │
              └──────┬─────┘        │
                     ▼              ▼
              CLT approx       justify another
              may be used      method or do not approximate
```

## 7. The visual proof (p010a-p010b)

```
   the 3x4 grid the slide shows:

              NORMAL    UNIFORM    SKEWED    RANDOM
   ┌────────┬─────────┬──────────┬─────────┬─────────┐
   │POPULN  │   ╱‾╲   │ ┌─────┐  │  █╲     │  ▄ █ ▄  │
   │        │  ╱   ╲  │ │     │  │  █ ▲╲   │  █ █ █  │
   ├────────┼─────────┼──────────┼─────────┼─────────┤
   │ n = 10 │   ╱╲    │  ╱‾‾╲    │  ╱‾╲    │  ╱‾‾╲   │
   │        │  ╱  ╲   │ ╱    ╲   │ ╱   ╲   │ ╱    ╲  │
   ├────────┼─────────┼──────────┼─────────┼─────────┤
   │ n = 30 │   │╷│   │   │╷│    │   │╷│   │   │╷│   │
   │        │   │││   │   │││    │   │││   │   │││   │
   └────────┴─────────┴──────────┴─────────┴─────────┘
             ^ all four columns look NARROW BELLS at n=30
               that is the CLT: shape washed out, spread shrunk
```

## 8. WORKED: ATM wait times (p011-p012)

```
   heavily right-skewed wait, μ = 4 min, σ = 2 min, n = 36.
   P(average wait > 4.5 min)?
```

```
   STEP 1  n=36 ≥ 30, so the sample mean is normal (even though waits are skewed)
   STEP 2  SE = 2/√36 = 2/6 = 0.333
   STEP 3  Z = (X̄ - μ)/SE = (4.5 - 4)/0.333 = 0.5/0.333 = 1.50
   STEP 4  upper tail at z=1.50  ->  6.68%
```

```
   the picture:

        ╱‾╲
       ╱   ╲▓▓▓
     ──┴───┴──┴──
       4.0 4.5
            ▲
        z = 1.50
        tail = 6.68%
```

## 9. WORKED: impurity (p013-p014) - the ERRATA one

```
   μ = 4.0 g, σ = 1.5 g, n = 50.
   P(3.5 < X̄ < 3.8)?
```

```
   SE = 1.5/√50 = 0.212132

   Z1 = (3.5 - 4)/0.212132 = -2.357  ->  -2.36
   Z2 = (3.8 - 4)/0.212132 = -0.943  ->  -0.94

   P = P(0<Z<2.36) - P(0<Z<0.94)
     = 0.4909 - 0.3264 = 0.1645
```

```
  ╔═══════════════════════════════════════════════════════════════╗
  ║  ERRATA 6: the slide PRINTS Z2 = -0.4, which is WRONG.         ║
  ║  The correct value is -0.94.                                   ║
  ║  The final answer 0.1644 is nevertheless correct, because the  ║
  ║  working behind it used the right table areas (0.4909 and       ║
  ║  0.3264; the latter belongs to z=0.94, not z=0.4).             ║
  ║  WRITE Z2 = -0.94 in your answer.                              ║
  ╚═══════════════════════════════════════════════════════════════╝
```

## 10. WORKED: LED bulbs (p015-p016)

```
   "heavily skewed", μ = 50000, σ = 8000, n = 64.
   P(X̄ < 48000)?
```

```
   SE = 8000/√64 = 8000/8 = 1000
   Z  = (48000 - 50000)/1000 = -2.00
   P  = 0.0228
```

```
   note the SAME -2.00 -> 0.0228 as the normal example.
   It is the same table read, just reached through SE instead of σ.
```

## 11. WORKED: machine life, small n (p017-p018)

```
   "the lives follow the NORMAL distribution", μ = 7, σ = 1, n = 9.
   P(6.4 < X̄ < 7.2)?
```

```
   SE = 1/√9 = 1/3
   Z1 = (6.4 - 7)/(1/3) = -1.80
   Z2 = (7.2 - 7)/(1/3) = 0.60

   P = 0.4641 + 0.2257 = 0.6898
```

```
  ╔═══════════════════════════════════════════════════════════════╗
  ║  n = 9 IS BELOW 30, BUT THE QUESTION SAYS THE POPULATION IS    ║
  ║  NORMAL. That is case 2: the sample mean is EXACTLY normal.    ║
  ║  So we can still use the table. The word "normal" in the       ║
  ║  question gives an exact result, so no n≥30 heuristic is needed.║
  ╚═══════════════════════════════════════════════════════════════╝

   the two tails added:

        ╱‾╲
     ▓▓▓│   │▓▓
   ──┴──┴───┴──┴──
    6.4  7.0  7.2
    .4641     .2257
        total 0.6898
```

## THE SAMPLING/CLT KIT

```
   ┌────────────────────┬───────────────────────────────────┐
   │ SE of a mean       │ σ/√n  (or s/√n)                    │
   │ SE of a proportion │ √(p(1-p)/n)                        │
   │ Z for a mean       │ (X̄ - μ)/(σ/√n)                     │
   │ Z for a single obs │ (X - μ)/σ         <- NOT the same! │
   │ n >= 30            │ course heuristic for CLT approx    │
   │ n < 30, normal pop │ exact normal                       │
   │ n < 30, non-normal │ normal approx needs justification  │
   └────────────────────┴───────────────────────────────────┘
```

```
  ╔═══════════════════════════════════════════════════════════════╗
  ║ THE SINGLE COMMONEST MISTAKE IN THIS TOPIC:                    ║
  ║ using σ in the denominator for a question about the AVERAGE    ║
  ║ of n items. An average ALWAYS divides by σ/√n.                 ║
  ║   one bulb's life       -> divide by σ                         ║
  ║   the MEAN of 25 bulbs  -> divide by σ/√25 = σ/5               ║
  ╚═══════════════════════════════════════════════════════════════╝
```

---
Next: theory of estimation.
