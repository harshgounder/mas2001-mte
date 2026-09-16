# Type space and sibling audit

Built 15 September 2026. Systematically enumerates every question TYPE each MTE topic can
carry, marks what the corpus actually asks, lists the direct SIBLINGS (same skeleton, one
degree of freedom different), and audits our own lists for missed items. Every number below
was recomputed on the machine this session.

Method: for each topic, the type space is built as
    INPUT STATE x TARGET (ASK) x CONDITION SET
All three dimensions vary independently; a type node exists when a method applies.

Legend: [X] asked in corpus | [S] sibling, one mutation away, NOT asked | [F] far, out of
reach | [C] covered by our docs already.

## 1. The full method-inventory (types per topic)

### T2 foundations
Targets: P(event), P(complement), P(union), P(intersection), P(conditional), P(at least one),
P(neither), independence check, count outcomes.
```
  [X] equally likely single draw (A1 MCQ: red ball 0.4, ace 4/13)
  [X] complement via P(A') (A1 MCQ 8, pens "no defective")
  [X] conditional P(A|B) forward (A1 MCQ 6, camera)
  [X] at-least-one via complement (D1-2c 14/15)
  [X] counting C(n,r) inside probability (D1-2, D1-3)
  [X] set operations on coded outcomes (D1-1)
  [X] independence product (event level): D1-15 batteries (.9^2)
  [S] P(neither A nor B): 1 - P(AuB). NOT asked. sibling of "at least one".
      toy verified: P(A)=.6 P(B)=.2 indep -> neither = .32
  [S] independence CHECK from given probabilities ("are A and B independent?"):
      not asked. the corpus only USES independence, never tests it. classic MCQ.
  [S] conditional from a table with counts (2x2): not asked.
  [F] permutations: never used in any question (verified by grep). low risk but the
      deck teaches P(n,r). one MCQ could exist.
```

### T3-4 random variables
Targets: classify discrete/continuous, build pmf from an experiment, function of rv.
```
  [X] classify rv type (A1 MCQ 1, A2 MCQ-ish)
  [X] pmf from enumeration: dice sum, two coins, boards, batteries, dice max
  [X] support identification [C] (documented)
  [X] transformed rv: Y = X+4, M = max, h(X) revenue
  [S] min of two dice (mirror of max): p(min=m) = (13-2m)/36. not asked.
  [S] difference of dice (support -5..5, Var = 35/6 same as sum): not asked.
  [S] "classify: give me the support" as a standalone MCQ: not asked.
```

### T5-6 pmf/pdf/cdf
```
  [X] find k (linear): 15k=1
  [X] find k (quadratic): 10k^2+9k=1
  [X] pmf to cdf build (boards, dice max)
  [X] cdf to pmf (p078 taught, exercise D1-27)
  [X] pdf verify (integral = 1): cable, f=2x, bus
  [X] cdf from pdf (exercise pair D1-27, D1-28)
  [X] pdf from cdf (D1-28)
  [X] interval prob via cdf F(b)-F(a) (A2 B3, D1-25)
  [X] nondecreasing proof (D1-18)
  [S] P(a<=X<=b) for integer rv via F(b) - F(a-1): taught (p135), NOT asked in corpus.
  [S] given F(x) piecewise, find P(X in range): D1-28 exists; a sibling asks TWO
      ranges or the complement; low novelty.
  [S] "is this a valid cdf" check: not asked. sibling of "valid pdf" (A1 short 3).
  [S] pmf/cdf of a transformed discrete rv (Y = 2X+1 pmf): not asked. classic.
```

### T7 expectation
```
  [X] E(X) from table | [X] E(X^2) | [X] E(aX+b) proof | [X] E[h(X)] piecewise
  [X] E from pdf (continuous) | [X] E(Y) of shifted rv
  [S] E(X^2) then Var in one ask: A1 app 1 does exactly this [C, present]
  [S] E of a function with a quadratic h: D1-22 d part (X - .01X^2) exists
  [S] "find E(X) given only the cdf": not asked. method: f = F', then integral.
  [S] E(|X|) or E(min(X, c)) style capped payoffs: not asked. insurance flavor.
      low-med risk. one line method (piecewise sum).
```

### T8-9 independence of rvs (the [H] block)
```
  [X] Var(sum of dice) used inside Chebyshev (A1 short 5)
  [S] E(XY) vs E(X)E(Y) as an MCQ or short: NOT asked but the sheet teaches the rule.
      MCQ: "if X, Y independent, E(XY) = ?" trivial; better: given E(X),E(Y), find E(XY).
  [X] Var(X - 2Y) for independent Poisson variables: MTE 2024-25 QB1, answer 14.
  [S] Var(aX + bY) linear combination: taught in estimator block (p5 p021),
      asked implicitly. standalone ask not present.
  [S] independence check via joint vs product pmf: not asked.
```

### T10-11 Chebyshev
```
  [X] between-form lower bound (A1 app 4: 75 percent)
  [X] tail form with sum of dice (A1 short 5: 35/54)
  [X] counts interval (A1 short 6: 19/24)
  [X] applicability MCQ x2 (A1 MCQ 5, 10)
  [X] reverse: given a tail bound, solve the interval width: MTE 2025-26 Q5, c=10.
  [S] two-sided vs one-sided variant: one-sided bound sigma^2/(sigma^2 + c^2) NOT asked;
      sheet footnote recommended.
  [S] compare bound to actual (A1 short 5 asks "compare": present, [C])
```

### T12-16 the distribution shelf (per distribution: same 9-slot matrix)
For binomial the corpus covers: point [X], tail [X], complement [X], params from ratio [X],
N x P [X], E/Var [X], MCQ formulas [X], nesting [X].
```
  [S] two-sided interval P(a<=X<=b) for binomial: pens P(2<=X<=4) = 0.3367 (verified).
      NOT asked. sibling of tail + point. very likely exam shape.
  [S] binomial min-n design ("how many trials"): n=22 for the .9 guarantee [H, new node]
  [S] conditional discrete P(X=2|X>=1) = 0.3207 (verified): not asked. [H, new node]
  [S] mode of binomial: floor((n+1)p) = 1 for B(12,.1); mode not asked anywhere.
  [S] geometric: pmf asked implicitly (A1 short 4 asks E), E=2 = 1/p [X], Var=(1-p)/p^2
      = 2 for p=.5 NOT asked. sibling.
  [S] geometric tail P(N<=k) = 1-(1-p)^k: not asked (0.875 for p=.5, k=3). sibling.
  [S] hypergeometric full pmf: A1 long 3 asks mean only; pmf values (0.383, .451, .150,
      .016, .0004 verified) NOT asked as full distribution. sibling.
  For Poisson: point [X], ratio [X], tail [X], N x P nested [X], approx [X], overflow [X].
  [S] Poisson time-window change: "scale lambda to the window" (2/min -> 10 per 5 min):
      partially used inside nesting. standalone NOT asked.
  [S] Poisson between values P(1<=X<=3): not asked. sibling of tail.
  For uniform: density [X], ratio [X], abs intervals [X], inverse K [X], clipping [X],
      two-uniforms [X], rounding [X].
  [S] "mean and variance from a and b" as a standalone: MCQ asks variance formula only.
  [S] uniform median: (a+b)/2 trivially = mean. not asked, trivial.
  For normal: forward [X], inverse [X], interval [X], tails [X], two-unknown [X],
      landmarks MCQ [X], N x P [X], two tables [H].
  [S] mu recovery given percentile + sigma: mu = 100 - 1.2816(10) = 87.18 (verified).
      one-unknown sibling of the two-unknown C2. LIKELY exam shape (easier version).
  [S] sigma recovery given percentile + mu: mirror. not asked.
  [S] P(X > mu + 2sigma) style landmark arithmetic: sibling of A2 A11. not asked.
  For exponential: pdf/cdf [X], memoryless [X/2 uses], conditional [X], units [X],
      survival [X], mean [X].
  [X] P(a < T < b) interval: MTE 2024-25 QB2 asks 7 to 12 minutes at rate 1/4.
      Answer $e^{-7/4}-e^{-3}=0.123987$.
  [S] E(T) or Var(T) standalone from lambda: E=2 for lambda=.5 asked implicitly in B5.
  [S] min of two exponentials: rate doubles, P(min>1) = e^-1 = 0.3679 (verified).
      NOT asked. classic adjacency, low-med risk.
```

### T17-18 sampling + CLT
```
  [X] SE compute [lightbulbs], SE scaling ["quadruple halves"], CLT apply [impurity, LED,
      ATM], exact-normal fallback [machines n=9]
  [S] CLT for the SUM (not the mean): sd = sqrt(n)*sigma; impurity sum sd = 10.607
      (verified). NOT asked. direct sibling. the sum-vs-mean distinction is a classic.
  [S] CLT concept MCQ ("what does CLT say"): not present in assignments; likely.
  [S] SE design ("how large n for margin m"): n=35 (verified) [H, new node].
  [S] finite population correction: not asked, not taught. far.
```

### T19-21 estimation
```
  [X] vocabulary [X], point estimate [X], p-hat [X], CI compute [X/boundary],
  [X] unbiasedness check [X], lambda-forcing [X], consistency [X], efficiency compare [X],
  [X] sufficiency [X, direct MTE 2025-26 Q3], protocol [X].
  [S] MSE comparison ("which has smaller MSE"): new node [H]. MSE(T4)=25.75 vs Var(T3)=.33
      verified. sheet has MSE = Var + Bias^2.
  [S] relative efficiency as a ratio: (5/9)/(1/5) = 2.7778 = 25/9 (verified). not asked.
      sibling of "which is best".
  [S] Var of a linear combination standalone: Var(2X1+3X3-4X2) = 29 sigma^2 asked inside
      the comparison [C, present].
```

## 2. Sibling matrix, condensed (the double check)

```
  corpus model                  direct sibling NOT asked                    risk
  ----------------------------------------------------------------------------------
  pens P(X=k), tail, zero       pens P(2<=X<=4) two-sided interval           HIGH
  normal two-unknown C2         normal ONE-unknown (mu from one percentile)  HIGH
  exp survival / conditional    exp interval CONFIRMED by MTE 2024-25 QB2    ASKED
  CLT mean impurity             CLT SUM interval (sd = sqrt(n) sigma)        MED-HIGH
  Var(sum of dice)              Var(X-2Y) CONFIRMED by MTE 2024-25 QB1       ASKED
  E(X), E(X^2) chain            E of capped/|X| payoff                      MED
  geometric E = 1/p             geometric Var or P(N<=k)                     MED
  hypergeometric mean           hypergeometric full pmf                      MED
  Poisson tail                  Poisson P(a<=X<=b) between                   MED
  A1 independence use           independence CHECK question                  MED
  valid-pdf check               valid-cdf check                              LOW-MED
  efficiency "which best"       MSE comparison / relative efficiency ratio   MED
  estimate "classify rv"        min/difference of dice derivation            LOW
  at-least-one complement       P(neither)                                   LOW
  -- new nodes from mutation analysis, not asked anywhere: --
  min-n design (binomial n=22, CLT n=35)                                       HIGH
  discrete conditional P(X=k|X>=j)                                             MED-HIGH
  parameter recovery generalized (lambda from P(0), mu from z)                 HIGH
```

## 3. Audit of OUR OWN lists (did we miss anything in the docs)

```
  our docs (MASTER, FULL-EXPANDED, MUTATION) already contain:
    [C] the 8 hidden blocks, the new nodes 3.a-3.h, errata 1-15, the 4-state drill
  found missing in the audit of our own docs:
    A. deck p135's "integer interval via F(b) - F(a-1)" was charted as taught but its
       sibling status (NOT asked) was not marked. add: taught-not-asked.
    B. the mode formula: sheet mentions the ratio crossing rule; the closed form
       floor((n+1)p) was not written. add one line.
    C. one-sided Chebyshev: not anywhere in our docs except this file's recommendation.
       add footnote to sheet section E.
    D. the geometric and hypergeometric sheet gaps: flagged in mutation file 3.h; still
       to be patched into the actual sheet.
    E. A2 A10's d>b clipping: our docs say (b-c)/(b-a); the audit recheck confirms the
       clipping READING is correct; keep.
    F. our count register item 27 says "two cdfs" for D1-27; exact: two parts, three
       pdfs (1/3-2/3, |x|) plus one cdf build; the "two" counts two sub-parts.
       cosmetic, no count change (multi-part counts once).
```

## 4. Verdict

Every sibling above is ONE mutation from a corpus model and all are legal MTE asks
(lectures 1-21, slides teach the machinery). None needs material outside the syllabus.
Highest-value siblings to drill before the exam:
```
  1  normal one-unknown recovery (easy version of C2)
  2  binomial two-sided interval (pens 2..4 = 0.3367)
  3  CLT for a sum (sqrt(n) sigma)
  4  discrete conditional P(X=k | X>=j)
  5  min-n design (binomial, CLT)
  6  geometric Var / tail
  7  independence check question
  8  MSE comparison
  9  Poisson between-values probability
 10  valid-cdf check
```
