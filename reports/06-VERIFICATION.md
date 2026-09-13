# Verification record

Two layers of verification run over the deliverables in this repo. Both are recorded
with their raw output so the claims can be re-checked rather than trusted.

## Layer 1: conversion integrity

| gate | method | result |
|---|---|---|
| source identity | sha256 of every PDF against `sources.yaml` | 11 of 11 match, 0 mismatches |
| page counts | `pdfinfo` per source against the declared count | 11 of 11 match, total 348 |
| dry run | `python3 scripts/convert.py --dry-run` | 348 pending, 0 skipped |
| pilot conversion | `--label lms-method-of-moments` (11 pages) | 11 done, 0 failed, 0 banned, 0 truncated, 132.6s |
| resume behaviour | rerun the same label | 0.0s wall, 11 done, manifest grew by 0 lines |
| per-page provenance | `work/manifest.jsonl` | one record per page: status, attempts, latency, chars, png sha256, model, ts |
| raw page retention | `work/pages/<label>/pNNN.png` | every converted page keeps the exact image it came from |

## Layer 2: formula and answer-key verification, 79 checks, 79 pass

Checker: a single Python file using only the standard library, run on the machine rather
than asserted from memory. Full raw output is in
`reports/evidence/verify-formula-sheet-20260913.txt`.

What it proves, grouped:

| group | checks | what is proven |
|---|---|---|
| binomial | 4 | pmf sums to 1, mean np, variance npq, and the Poisson limit gap is the expected O(1/n) |
| Poisson | 4 | pmf sums to 1, mean equals variance, additivity of independent Poissons to 2.8e-17 |
| uniform | 3 | integrates to 1, mean (a+b)/2, variance (b-a)^2/12 |
| normal | 10 | integrates to 1, symmetry, standardisation, slide values F(0.12)=0.5478 and P(X>8.6)=0.4522, the 68.27 / 95.45 / 99.73 landmarks, and the inverse X = mu + Z sigma = 3.792 |
| exponential | 5 | integrates to 1, mean 1/lambda, variance 1/lambda^2, tail identity, memorylessness |
| Chebyshev | 6 | bound forms hold, k=2 gives 3/4, k=3 gives 8/9, k=4 gives 15/16, vacuous at k=1, and the bound always above the true probability |
| expectation and variance algebra | 6 | E(X+Y) linear without independence, E(XY) needs independence, Var(aX+b)=a^2 Var(X), Var(X+Y) needs independence |
| CLT | 4 | simulated standardised means from a skewed population land at mean 0.0017, variance 1.0251, skewness 0.388 against theory 2/sqrt(36)=0.333 |
| estimation | 5 | Xbar unbiased, S^2 with n-1 unbiased, S^2 with n biased low (0.216 vs 0.25), MSE = Var + Bias^2, efficiency ranking |
| corpus integrity | 4 | 11 sources parsed, 348 pages declared, all sha256 match, all page counts match |

### Assignment 1, checked against its own official answer key

The assignment PDF carries the answer key in the right hand column. Every keyed value was
recomputed independently:

| question | official key | recomputed | verdict |
|---|---|---|---|
| short Q1, distribution of boys in 3 children | 1/8, 3/8, 3/8, 1/8 and F = 1/8, 4/8, 7/8, 1 | matches | consistent |
| short Q2, P(X > 12) | 0.0915 | 0.0915782 = 5e^-4, which rounds to 0.0916 | key truncates, value is right |
| short Q3, valid pdf and b | yes, b = 1/2 | matches | consistent |
| short Q4, expected tosses to first head | 2 | 1/p = 2 | consistent |
| short Q5, two dice Chebyshev | bound 35/54, actual 1/3 | 0.648148 and 0.333333 | consistent |
| short Q6, 80 to 120 sixes in 600 throws | 19/24 | 0.791667 | consistent |
| long Q1, death density | 0.1544 and 0.4863 | 0.154360 and 0.486265 | consistent |
| long Q2, pmf with k | k = 1/10, then 81/100, 19/100, 4/5, c = 4, 5/7 | all reproduced exactly | consistent, and the normalisation is 10k^2 + 9k - 1 = 0 with exact root 1/10 |
| Q3, 5 defectives in 25, sample 4 | without replacement 0.80, with 0.8 | hypergeometric mean is exactly nK/N = 0.8 | consistent |
| Q4, four bad oranges in 20 | 12/19, 32/95, 3/95 | 0.631579, 0.336842, 0.031579 | consistent |
| application Q1, sensors | valid, E = 1.2, Var = 0.86 | matches | consistent |
| application Q2, calls | F = 0.15, 0.50, 0.80, 1.00, P(X<=2)=0.80, P(X>1)=0.50 | matches | consistent |
| application Q3, battery | 3.45, 0.95, 0.98 | matches | consistent |
| application Q4, marks | at least 75 percent | k = 2, bound 1 - 1/4 = 0.75 | consistent |

## Honest note on my own first pass

The first run of the checker reported 60 of 64 passing. All 4 failures were defects in my
thresholds, not in the material:

1. `binomial approximates Poisson` used a 1e-7 tolerance on a limit whose error is O(1/n),
   measured gap 2.71e-05 at n = 10000. Corrected to 1e-4.
2. `P(X>12) = 0.0915` compared the computed 0.091578 against the key's printed 0.0915 with a
   5e-05 tolerance. The real issue is that the key truncates instead of rounding. The check now
   asserts the exact value.
3. `tail identity` compared two numbers, one of which came from a Simpson integration over
   [12, 4000] with too coarse a step near a rapidly decaying tail. Replaced with an analytic
   comparison.
4. `CLT skewness collapses` used a threshold of 0.2 when theory says the standardised mean of
   an exponential sample of 36 has skewness 2/sqrt(36) = 0.333. The measured 0.388 is correct
   behaviour, so the check now compares against theory instead of against a guess.

After those four corrections the checker is 79 of 79. The corrections are recorded here
because a verification gate that was quietly loosened is worth less than one whose
adjustments are visible.
