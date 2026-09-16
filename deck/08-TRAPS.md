# 08 TRAPS: every trap and every source errata

## THE TRAPS AS A GAUNTLET

```
   a question walks through and each trap tries to catch it:

   START ──▶ ┌──────────────────┐
             │ 1 exclusive vs   │  "are these independent?"
             │   independent    │  -> exclusive is NOT independent
             └────────┬─────────┘
                      ▼
             ┌──────────────────┐
             │ 2 E(XY) needs    │  E(X+Y) does NOT, E(XY) DOES
             │   independence   │
             └────────┬─────────┘
                      ▼
             ┌──────────────────┐
             │ 3 Var(X-Y) adds  │  the minus stays PLUS
             └────────┬─────────┘
                      ▼
             ┌──────────────────┐
             │ 4 the a-1 rule   │  integer rv: F(b)-F(a-1)
             └────────┬─────────┘
                      ▼
             ┌──────────────────┐
             │ 5 variance slot  │  N(μ,σ²) -> sqrt it
             └────────┬─────────┘
                      ▼
             ┌──────────────────┐
             │ 6 φ vs F table   │  decide BEFORE substituting
             └────────┬─────────┘
                      ▼
             ┌──────────────────┐
             │ 7 rate vs mean   │  λ is a rate, 1/λ is a time
             └────────┬─────────┘
                      ▼
             ┌──────────────────┐
             │ 8 unit mismatch  │  convert first
             └────────┬─────────┘
                      ▼
             ┌──────────────────┐
             │ 9 inverse's last │  convert z back to X
             │   step           │
             └────────┬─────────┘
                      ▼
             ┌──────────────────┐
             │ 10 N x P, not P  │  expected COUNT
             └────────┬─────────┘
                      ▼
                    ANSWER
```

## THE ERRATA, BY WHERE THEY LIVE

```
   ┌──────────────────────┬───────────────────────────────┐
   │ SOURCE               │ ERRATA                        │
   ├──────────────────────┼───────────────────────────────┤
   │ ppt3 (binomial/Poiss)│ E1 insurance 0.1745->0.1755   │
   │                      │ E2 die count 0.549->0.5499    │
   ├──────────────────────┼───────────────────────────────┤
   │ ppt4 (continuous)    │ E4 rate/mean wording p040     │
   │                      │ E8 figure σ=10 -> use 5       │
   ├──────────────────────┼───────────────────────────────┤
   │ notes deck           │ E13 bus integral bound 3 vs 2 │
   ├──────────────────────┼───────────────────────────────┤
   │ clt deck             │ E6 impurity Z2 -0.4 -> -0.94  │
   ├──────────────────────┼───────────────────────────────┤
   │ assignments          │ E3 0.0915->0.0916             │
   │                      │ E5 second edition broken      │
   │                      │ E9 0.5679->0.6225             │
   │                      │ E10 mean 37.5->37.2           │
   │                      │ E11 0.808->0.80               │
   │                      │ E12 sd 0.975->0.97            │
   │                      │ E14 0.8754->0.8753            │
   │                      │ E16 tube 2/3 -> 8/27          │
   │                      │ E17 row sums to 0.9           │
   ├──────────────────────┼───────────────────────────────┤
   │ Chebyshev deck       │ E15 Q3 slide mis-stated       │
   ├──────────────────────┼───────────────────────────────┤
   │ MTE schemes          │ E19 CDF option B -> D         │
   │                      │ E20 infinite bounds -> 0..4   │
   │                      │ E21 E(t²)≠0 -> E(t²)≠θ²       │
   ├──────────────────────┼───────────────────────────────┤
   │ OUR OWN mock         │ E18 "T4 smallest var" FALSE   │
   └──────────────────────┴───────────────────────────────┘
```

## THE 10-TRAP NIGHT LIST, AS A CHECKLIST

```
   NIGHT BEFORE THE PAPER:

   □ 1 exclusive vs independent        can state the difference in one line
   □ 2 E(XY) needs independence       vs E(X+Y) always
   □ 3 Var(X-Y) = Var(X)+Var(Y)       the minus stays plus
   □ 4 P(a≤X≤b) = F(b)-F(a-1)         integer rv only
   □ 5 N(μ,σ²) second slot is VAR     sqrt before z
   □ 6 φ(z) area-from-0 vs F(z) cum   decide first
   □ 7 λ rate, 1/λ mean               exponential
   □ 8 convert units FIRST            15/hr with 3 min
   □ 9 X = μ + zσ                     the inverse's last step
   □ 10 expected count = N x P        not P
```

Two sections. First the concept traps (mistakes the QUESTIONS are built to catch). Then the
source errata (numbers printed wrong in the slides and keys, with the correct value).

## Part 1: concept traps

```
  1  EXCLUSIVE vs INDEPENDENT. Mutually exclusive means no shared outcome. Independent means
     P(A n B)=P(A)P(B). Exclusive events with positive probability are NOT independent. This is
     the most common true/false the paper can carry.
  2  E(XY) = E(X)E(Y) needs INDEPENDENCE. E(X+Y)=E(X)+E(Y) does NOT. The paper probes exactly
     this contrast.
  3  Var(X-Y) = Var(X) + Var(Y) when independent. The minus stays plus. Squaring kills the sign.
  4  THE a-1 RULE. For an integer rv, P(a<=X<=b) = F(b) - F(a-1). Writing F(a) is the slip. For
     a continuous rv it does not matter.
  5  THE VARIANCE SLOT. N(mu, sigma^2): the second number is the VARIANCE. Square-root it before
     a z-score. "mean 70, variance 25" -> sigma = 5.
  6  TWO TABLE CONVENTIONS. phi(z) is often the area from 0 to z; F(z) is cumulative from -inf.
     MIXING them is the biggest normal error. Decide which the paper gives before substituting.
  7  RATE vs MEAN. Exponential: lambda is a rate, 1/lambda is the mean TIME. Getting the
     reciprocal backwards changes the answer completely. (Slides get this wrong too, errata 4.)
  8  UNIT MISMATCH. A rate per hour with a time in minutes. Convert to one unit first.
  9  THE INVERSE'S LAST STEP. Get z from the table, then convert X = mu + z sigma. Forgetting
     the conversion leaves the answer in z-space.
 10  EXPECTED COUNT vs PROBABILITY. "Expected number out of N" is N x P, not P. (0.5499 not
     5.5e-5.)
 11  CHEBYSHEV k IN SIGMA UNITS. k = eps/sigma. Raw units in, convert first. And the bound is
     an UPPER bound on the tail, so report the exact value too when the distribution is known.
 12  CONSISTENCY vs SMALL VARIANCE. A fixed-n small variance is not consistency. Consistency is
     about n growing. T1 with Var 3 sigma^2 at fixed n=3 is the trap.
 13  BIASED BEFORE VARIANCE. In "most efficient", a biased estimator is disqualified first,
     even if its variance is smaller. Efficiency is among the UNBIASED only.
 14  EXACT vs ROUNDED. Carry exact values to the final line. Rounding mid-way and then rooting
     or summing gives a slightly wrong number the key itself sometimes prints.
 15  SUPPORT CHECK. A density is zero outside its support. Integrating over (-inf, inf) when the
     support is finite is a setup error (a scheme printed this, errata 20).
 16  VALID PDF CHECK. A pmf must sum to 1 over its support. A row that sums to 0.9 is not a pmf
     (errata 17).
 17  "USE THE APPROXIMATION". When the paper says use the Poisson approximation to the
     binomial, set l = np, not the exact binomial.
 18  LARGE SAMPLE LANGUAGE. "The mean of a sample of n" divides by the STANDARD ERROR, not by
     sigma. A single observation uses sigma.
 19  CLT CONDITIONS. n>=30 is the course heuristic, not a universal theorem cutoff. For a
     small non-normal population, do not assume the normal approximation without checking
     shape and tail behaviour.
 20  NORMAL POPULATION FALLBACK. A normal population is exactly normal at any n, so a small-n
     question is fine if the population is stated normal. No large-n heuristic is needed.
```

## Part 2: source errata (the slides and keys print these wrong)

Use the computed value. Each entry is verified in the repo (reports/09-ERRATA.md).

```
  E1   insurance Poisson: slide 0.1745, correct 0.1755   (ppt3 p027)
  E2   irregular die count: slide 0.549, correct 0.5499   (ppt3 p018)
  E3   assignment Q2 P(X>12): key 0.0915, correct 0.0916  (truncation)
  E4   exponential rate/mean meaning inverted on p040, read p041 instead
  E5   assignment 1 long Q2 normalisation: the 12k version is a broken SECOND EDITION.
       batch-1 edition: 10k^2 + 9k = 1, k = 1/10 exact, key checks out.
       second edition: 12k + 10k^2 = 1, k = 0.0782, but its own key prints 1/10 which does
       NOT satisfy its own table. Do not drill the second edition.
  E6   impurity Z: slide prints Z2 = -0.4, correct -0.94. Answer 0.1644 is still right
       (because the working used 0.94). (clt p014)
  E7   N(mu, sigma^2): the prose says variance, the notation says squared. Second slot IS
       variance.
  E8   ppt4 p030 figure labels sigma = 10 under mu = 8, but the arithmetic uses sigma = 5.
       Use 5. (errata 8)
  E9   assignment 2 B Q5: key prints 0.5679, correct 0.6225  (exponential conditional)
  E10  assignment 2 C Q2: key prints mean 37.5, correct 37.2 (the key's own cutoff agrees
       with 37.2). Use mu 37.2, sigma 28.2, cutoff 30.4.
  E11  assignment 1 long Q3: key prints 0.808, both cases are exactly 0.80 (hypergeometric
       mean equals binomial mean here)
  E12  assignment 1 app Q3: key rounds twice, sd 0.975 -> 0.98. Exact is 0.9734 -> 0.97.
  E13  deck bus example p127/p129: the printed first integral bound (3) contradicts the stated
       event (Y<2). Final answer 2/5 is correct for "Y<2 or Y>6". Use P(Y<2)+P(Y>6)=0.08+0.32=0.40
  E14  assignment 2 C Q3: key 0.8754, exact 0.8753.
  E15  Chebyshev L10-11 Q3 slide: states one row, works another. It also writes a reciprocal
       template. USE Q1 (E=3, E(X^2)=13, bound 21/25) AND Q2 (mu=10, var=4) ONLY. Do not quote
       Q3's row. (Full retraction detail in the repo errata, incl. two claims that were
       themselves retracted after checking.)
  E16  tube question (2024 A1 Q12 and 2025-26 Q14): key part (ii) prints 2/3, correct is the
       probability that ALL THREE survive = (2/3)^3 = 8/27. The key carried the single-tube
       number into the three-tube part. Parts (i) 1/27, (iii) 0.25, (iv) 1.7 are correct.
  E17  2024-25 assignment 1 Q16: the probability row sums to 0.9, not 1. It is not a valid pmf.
       State the renormalisation you choose (divide by 0.9) or ask for the correction.
  E18  mock paper B4 (our own): the Note says T4 has the smallest variance. False, T4 is third
       of four (order T3, T2, T4, T1). T4 is biased, keep that part, drop the superlative.
  E19  2024 MTE QA2 CDF: scheme marks B, correct is option D (the CDF must accumulate the mass
       from 0 to 1). Option B gives F(1)=1.5, impossible.
  E20  2025 MTE scheme Q4: displays infinite integration bounds, but the support is 0<x<4 and
       the arithmetic uses 0 and 4. The constants are right, the printed bounds are the slip.
  E21  2025 MTE scheme Q8(ii): prints E(t^2) != 0, correct is E(t^2) != theta^2.
```

## The 10-item trap list to read the night before

```
  1  exclusive vs independent
  2  E(XY) needs independence, E(X+Y) does not
  3  Var(X-Y) adds
  4  the a-1 in F(b)-F(a-1)
  5  variance slot in N(mu, sigma^2), sqrt it
  6  phi vs F table convention
  7  rate vs mean in the exponential
  8  unit mismatch
  9  the inverse's last conversion step
  10 expected count = N x P, not P
```
