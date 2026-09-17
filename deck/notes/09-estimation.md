# 09 THEORY OF ESTIMATION (ppt5, 26 pages, lectures 19-21)

## 1. The vocabulary (p003-p004)

```
   ┌──────────────────┬────────────────────────────────────────────┐
   │ PARAMETER        │ a numerical characteristic of a POPULATION  │
   │                  │ μ, σ², p                                   │
   ├──────────────────┼────────────────────────────────────────────┤
   │ STATISTIC        │ a number computed FROM SAMPLE DATA          │
   │                  │ X̄, S², p̂                                   │
   ├──────────────────┼────────────────────────────────────────────┤
   │ ESTIMATOR        │ a FUNCTION of the sample used to estimate   │
   │                  │ a parameter. It is a RANDOM VARIABLE.       │
   │                  │ e.g. X̄ as an estimator of μ                 │
   ├──────────────────┼────────────────────────────────────────────┤
   │ ESTIMATE         │ the NUMBER you get once data is plugged in  │
   │                  │ e.g. x̄ = 52                                 │
   ├──────────────────┼────────────────────────────────────────────┤
   │ PARAMETER SPACE  │ all possible values of the parameter         │
   │                  │ Θ = (-∞, ∞) for μ                           │
   └──────────────────┴────────────────────────────────────────────┘
```

```
  ╔═══════════════════════════════════════════════════════════════╗
  ║  ESTIMATOR vs ESTIMATE - one mark, easy to lose                ║
  ║    X̄       = the RULE (an estimator, a random variable)        ║
  ║    x̄ = 205 = the NUMBER (the estimate, once data is in)        ║
  ╚═══════════════════════════════════════════════════════════════╝
```

## 2. The estimation pipeline (p004)

```
   ┌────────────┐    random    ┌──────────┐   compute   ┌───────────┐
   │ POPULATION │ ──────────▶  │  SAMPLE  │ ──────────▶ │ STATISTIC │
   │  (μ, σ)    │   sample     │ (X1..Xn) │             │   (X̄)     │
   └────────────┘              └──────────┘             └─────┬─────┘
                                                              │
                                                              ▼
                                                    ┌──────────────────┐
                                                    │ ESTIMATE of the  │
                                                    │ PARAMETER        │
                                                    └──────────────────┘
```

## 3. Point vs interval estimation (p005-p007)

```
   POINT ESTIMATION                      INTERVAL ESTIMATION
   ─────────────────                     ───────────────────
   a SINGLE value                        a RANGE of values
   μ ≈ X̄    σ² ≈ S²    p ≈ p̂             with a stated confidence level

   ✓ simple, easy to report              ✓ accounts for uncertainty
   ✗ does not show uncertainty           ✓ more informative
```

```
   the picture from p007:

   POINT                                 INTERVAL
     │                                     ┌───────────┐
     ▼                                     │           │
   ──●──────────────                    ──(───●───────)──
    210 ms                                204ms  216ms
   "one number"                          "a plausible range"
```

```
        CI = Point Estimate ± Margin of Error
```

## 4. The four characteristics of a good estimator (p008)

```
             A GOOD ESTIMATOR
                    │
     ┌──────────────┼──────────────┬──────────────┐
     ▼              ▼              ▼              ▼
 UNBIASED      CONSISTENT      EFFICIENT      SUFFICIENT
 correct on    approaches      smallest       uses all the
 average       truth as        variance       information
               n grows         among the      in the sample
                               UNBIASED
```

```
   "good = little systematic error + stability + precision"
```

## 5. Unbiasedness (p009)

```
  ┌───────────────────────────────────────────────────────────────┐
  │  θ̂ is UNBIASED for θ  if   E(θ̂) = θ                           │
  │  Bias(θ̂) = E(θ̂) - θ                                           │
  └───────────────────────────────────────────────────────────────┘
```

```
   the picture: many samples, plot the estimates

   UNBIASED                    BIASED (over-estimating)
     │                           │
     │ █ █ █                     │        █ █ █
     │ █ █ █ █                   │        █ █ █ █
   ──┴────┬────┴──              ──┴────────────┬──┴──
          ▲                                   ▲
          θ                                   θ
   estimates centre on θ       estimates centre ABOVE θ
```

```
  ╔═══════════════════════════════════════════════════════════════╗
  ║ "CORRECT ON AVERAGE, NOT PER SAMPLE"                           ║
  ║ An unbiased estimator can be badly wrong on any ONE sample.    ║
  ║ Unbiasedness is a statement about the LONG RUN.                 ║
  ╚═══════════════════════════════════════════════════════════════╝
```

## 6. Consistency (p010-p012)

```
        θ̂_n converges in probability to θ as n → ∞
        θ̂_n  ──P──▶  θ

   i.e. for any ε > 0:   P(|θ̂_n - θ| < ε) → 1 as n → ∞
```

```
  ╔═══════════════════════════════════════════════════════════════╗
  ║  SUFFICIENT CONDITIONS FOR CONSISTENCY (a sequence T_n):       ║
  ║    1.  E(T_n) → θ      as n → ∞                                ║
  ║    2.  Var(T_n) → 0    as n → ∞                                ║
  ║  Both hold  =>  T_n is consistent.                             ║
  ╚═══════════════════════════════════════════════════════════════╝
```

```
   WHY X̄ IS CONSISTENT (p012) - the standard answer:

   ┌──────────────────┬──────────────────┬────────────────────┐
   │ CONDITION 1      │ CONDITION 2      │ CONCLUSION         │
   ├──────────────────┼──────────────────┼────────────────────┤
   │ E(X̄) = μ         │ Var(X̄) = σ²/n    │ both hold          │
   │ so E(X̄) → μ      │ so σ²/n → 0      │ => X̄ is consistent │
   └──────────────────┴──────────────────┴────────────────────┘

   "more observations -> smaller variance -> more stable estimate"
```

```
   the picture:

   n = 5        n = 50         n = 500
    ╱‾╲          ╱╲              │
   ╱   ╲        ╱  ╲             │
  ─╯     ╰─   ──╯   ╰──        ──┴──
   wide         medium          spike AT θ
   (estimates scattered)    (estimates converge to θ)
```

## 7. Efficiency (p013-p014)

```
   θ̂1 and θ̂2 both UNBIASED for θ:
       if Var(θ̂1) < Var(θ̂2)  then θ̂1 is MORE EFFICIENT
```

```
        Among all UNBIASED estimators, the most efficient has the SMALLEST variance.
        Efficiency ∝ 1/Variance
```

```
   the slide's visual:

   Estimator A              Estimator B
   unbiased, Var = 4        unbiased, Var = 9
      ╱╲                      ╱‾╲
     ╱  ╲                    ╱   ╲
   ──┴──┴──                ──┴───┴──
   concentrated            spread out
   higher precision        lower precision
   -> MORE EFFICIENT       -> less efficient
```

```
  ╔═══════════════════════════════════════════════════════════════╗
  ║  THE ORDER OF OPERATIONS IN ANY COMPARISON:                    ║
  ║    STEP 1  find which are UNBIASED (compute E of each)         ║
  ║    STEP 2  a biased one is ELIMINATED, even if its variance     ║
  ║            is smaller ("efficiency" only compares the unbiased)║
  ║    STEP 3  compare variances of the SURVIVORS, smallest wins   ║
  ╚═══════════════════════════════════════════════════════════════╝
```

## 8. WORKED COMPARISON SET 1 (p015-p018) - the flagship question

```
   Sample of size 5 from N(μ, σ²).  (X1..X5)

   t1 = (X1+X2+X3+X4+X5)/5            <- the sample mean
   t2 = (X1+X2)/2 + X3
   t3 = (2X1 + X2 + λX3)/3            <- λ chosen for unbiasedness
```

```
   STEP 1: FIND λ
       E(t3) = [2E(X1) + E(X2) + λE(X3)]/3
             = (2μ + μ + λμ)/3 = [(3+λ)/3] μ
       for unbiasedness: (3+λ)/3 = 1  ->  λ = 0
       so t3 = (2X1 + X2)/3
```

```
   STEP 2: WHICH ARE UNBIASED
       E(t1) = (μ+μ+μ+μ+μ)/5 = μ              ✓ unbiased
       E(t2) = (μ+μ)/2 + μ = 2μ               ✗ BIASED
       E(t3) = (2μ+μ)/3 = μ                    ✓ unbiased
```

```
   STEP 3: COMPARE THE VARIANCES (of the unbiased ones)
       Var(t1) = σ²/5          = 0.2000 σ²
       Var(t3) = (4σ² + σ²)/9  = 5σ²/9 = 0.5556 σ²
```

```
       ordering:  σ²/5   <   5σ²/9   <   3σ²/2
                 (t1)       (t3)        (t2, biased)

       BEST = t1 = X̄, the sample mean
```

```
   the variance bar chart:

   t1  ████                     0.200 σ²   <- WINNER
   t3  ███████████              0.556 σ²
   t2  ██████████████████████████████  1.500 σ²  (biased, disqualified)
```

## 9. WORKED COMPARISON SET 2 (p019-p021) - with consistency

```
   Sample of size 3.  T1, T2, T3 estimate μ.

   T1 = X1 + X2 - X3
   T2 = 2X1 + 3X3 - 4X2
   T3 = (λX1 + X2 + X3)/3
```

```
   (i) ARE T1 and T2 UNBIASED?
       E(T1) = μ + μ - μ = μ                          ✓
       E(T2) = 2μ + 3μ - 4μ = μ                       ✓
       BOTH unbiased
```

```
   (ii) FIND λ FOR T3
       E(T3) = (λμ+μ+μ)/3 = ((λ+2)/3)μ
       ((λ+2)/3)μ = μ  ->  λ = 1
       so T3 = (X1+X2+X3)/3 = X̄, the sample mean
```

```
   (iii) IS T3 CONSISTENT?
       With λ=1, this fixed-n statistic is the sample mean for n=3.
       That fact alone does not establish consistency. The sequence Xbar_n is
       consistent under the usual iid assumptions because Var(Xbar_n)=σ²/n -> 0.
```

```
   (iv) VARIANCES
       Var(T1) = Var(X1)+Var(X2)+Var(X3) = 3σ²
       Var(T2) = 4Var(X1)+9Var(X3)+16Var(X2) = 29σ²
       Var(T3) = (1/9)(3σ²) = σ²/3

       minimum  ->  T3 is the BEST estimator
```

```
   the variance bar chart:

   T3  █                          0.33 σ²   <- WINNER
   T1  █████████                  3 σ²
   T2  █████████████████████████████████████████████████████████████████████████████████████  29 σ²
```

```
  ╔═══════════════════════════════════════════════════════════════╗
  ║  THE CONSISTENCY TRAP (worth memorising):                      ║
  ║  T1's variance is 3σ² for a FIXED n=3.                         ║
  ║  That is NOT a consistency statement.                          ║
  ║  Consistency is about behaviour AS n GROWS.                    ║
  ║  A fixed-n variance, however small or large, says nothing      ║
  ║  about consistency.                                            ║
  ╚═══════════════════════════════════════════════════════════════╝
```

## 10. Sufficiency (the lms-theory extra)

```
  ┌───────────────────────────────────────────────────────────────┐
  │  an estimator is SUFFICIENT if it uses ALL the information     │
  │  about θ present in the sample                                 │
  │  the test is the NEYMAN-FISHER factorisation                   │
  └───────────────────────────────────────────────────────────────┘

   examples in the corpus: the Poisson sample sum, the exponential
   sample mean, the sufficient statistics MCQ on MTE 2025-26 Q3
```

## 11. WORKED Real-Life 1: response time (p019)

```
   response times of 8 requests: 180,210,195,220,205,190,200,240
```

```
   x̄ = (sum)/8 = 1640/8 = 205 ms

   ESTIMATOR = X̄           (the rule)
   ESTIMATE  = 205 ms       (the number)
```

```
  ╔═══════════════════════════════════════════════════════════════╗
  ║  THE QUESTION ASKS FOR **BOTH** "the estimator and the         ║
  ║  estimate". Two marks. Do not give only the number.            ║
  ╚═══════════════════════════════════════════════════════════════╝
```

## 12. WORKED Real-Life 2: packet success (p020)

```
   500 packets, 465 delivered.  Estimate p.
```

```
   p̂ = X/n = 465/500 = 0.93 = 93%
   estimator used: p̂
```

## 13. WORKED Real-Life 3: battery life (p021) - the CI boundary item

```
   n = 25, x̄ = 8.4 hours, σ = 1.5 known.  95% CI,  z(0.975) = 1.96
```

This z interval assumes a normal population or a separately justified normal
approximation. A sample size of 25 alone does not supply that justification.

```
   CI = x̄ ± z(σ/√n)
      = 8.4 ± 1.96(1.5/5)
      = 8.4 ± 1.96(0.3)
      = 8.4 ± 0.588
      = (7.81, 8.99) hours
```

```
   the picture:

   ────────(───────●───────)────────
         7.81    8.4    8.99
              "plausible range for μ"

   NOTE: the CI MECHANICS belong to lecture 25 (BOUNDARY for this audit), but
   "point and interval estimation" IS named in the MTE syllabus line 15.
   Keep the formula in reserve; do not drill the mechanics.
```

## 14. The comparison quick table (p022)

```
   ┌────┬───────────┬───────────┬──────────────────┐
   │ #  │ PARAMETER │ STATISTIC │ RESULT           │
   ├────┼───────────┼───────────┼──────────────────┤
   │ 1  │ μ         │ X̄         │ 205 ms           │
   │ 2  │ p         │ p̂         │ 0.93             │
   │ 3  │ μ         │ X̄         │ 95% CI (7.81,8.99)│
   └────┴───────────┴───────────┴──────────────────┘

   point -> one value        interval -> a range
```

## 15. The standard unbiased results (the toolkit)

```
   ┌──────────────────────┬───────────────┬──────────────────┐
   │ ESTIMATOR            │ ESTIMATES     │ VARIANCE         │
   ├──────────────────────┼───────────────┼──────────────────┤
   │ X̄                    │ μ             │ σ²/n             │
   │ S² = Σ(Xi-x̄)²/(n-1)  │ σ²            │ (the n-1 matters)│
   │ p̂ = X/n              │ p             │ p(1-p)/n         │
   └──────────────────────┴───────────────┴──────────────────┘
```

```
  ╔═══════════════════════════════════════════════════════════════╗
  ║  WHY n-1 AND NOT n IN S²                                       ║
  ║  The deviations are measured from x̄, which ALREADY used the    ║
  ║  data. Using n would make S² too small on average. Dividing    ║
  ║  by n-1 corrects that. It is the price of estimating the mean   ║
  ║  from the same data.                                           ║
  ╚═══════════════════════════════════════════════════════════════╝
```

## 16. MSE, the honest comparison (formula sheet addition)

```
        MSE(θ̂) = Var(θ̂) + [Bias(θ̂)]²
```

```
   the picture:

   MSE = VARIANCE  +  BIAS²
         └─ spread ─┘  └ off-target ┘

        target
          │
     ─────●─────  <- the truth
       ▓▓ ▓▓
       ▓▓ ▓▓      <- estimates: spread (Variance) AND off centre (Bias)
```

```
  ┌───────────────────────────────────────────────────────────┐
  │ Efficiency ONLY compares unbiased estimators.              │
  │ MSE lets a biased estimator compete, by paying for its     │
  │ bias in the second term. The exam could introduce this.    │
  └───────────────────────────────────────────────────────────┘
```

## THE ESTIMATION DECISION TREE (for any question in this block)

```
              an estimation question
                      │
        ┌─────────────┴─────────────┐
        │                           │
   "find the value"            "compare estimators"
        │                           │
   point: X̄, p̂, S²          compute E of each
   interval: x̄ ± zσ/√n            │
        │                 ┌────────┴────────┐
   state estimator      unbiased         biased
   AND estimate          │                 │
                    compare Var        DISQUALIFIED
                         │             (or use MSE if asked)
                    smallest = winner
                    + name it
```

---
That is the theory of estimation. The estimator-comparison layout (unbiased -> variances -> name the winner) is the 6-to-8 mark question of this block.
