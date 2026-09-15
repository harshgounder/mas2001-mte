# Mutation analysis: what changes make a new question type

Built 15 September 2026. Answers the question: if we change a question's values, does its
type change too, and do new (sub)(sub)topics arise when setters re-skin questions. Also
lists the extra checks for coverage completeness.

## 0. The frontier frame (three names for one idea)

| frame | source | core claim |
|---|---|---|
| problem isomorphs | cognitive psychology (Simon/Newell tradition, problem space theory) | problems share deep structure (initial state, goal, operators, constraints) while differing in surface structure (objects, story, words). Solvers fail when surface differs because analogical transfer fails; experts see the deep structure directly |
| radical / incidental | Gierl and Lai, automatic item generation (AIG) | every item = ITEM MODEL (template). RADICALS are the features that affect difficulty (the solve path). INCIDENTALS are surface features assumed NOT to affect difficulty (numbers in ranges, names, units) |
| variation theory | Marton | learning = discerning the critical aspects of an object. You make an aspect visible by varying it while holding the rest invariant; contrast, generalisation, fusion |

The user's decomposition maps onto these exactly:
```
  INTENT (what the setter wants)  =  RADICALS  =  deep structure
  values, names, story            =  INCIDENTALS  =  surface structure
```

## 1. The three levels of "question"

```
  L-INSTANCE   one concrete problem: "10% pens, box of 12, find P(X=2)"
  L-MODEL      the template with slots: "<p> defective, batch <n>, find P(X=<k>)"
               fixed: formula C(n,k)p^k q^(n-k), the steps
               slots (incidentals): p, n, k, story nouns, units
  L-TYPE       the template CLASS sharing a solve path: "binomial point probability"
  L-FAMILY     groups of types under one method family: "binomial block"
```

Key rule this document establishes:
```
  INCIDENTAL mutation -> same TYPE. new practice instance, NOT a new (sub)topic.
  RADICAL mutation    -> new TYPE node. it slots into the tree as a new
                         sub / sub-sub / sub-sub-sub topic under the same topic.
```

## 2. The mutation taxonomy (M0 to M4)

```
  M0  RE-SKIN       swap numbers, names, units, story context.
                    Same radicals, same steps. TYPE UNCHANGED.
                    The exam does this constantly. Practice must include it, but it
                    never adds a tree node.
      examples: pens -> sensors -> bulbs (A1 and A2 are full of these)
                4 red 6 blue -> 5 red 5 blue (same ratio problem)
                mean 70 var 25 -> mean 50 var 16 (same Chebyshev)

  M1  INVERT        swap which quantity is GIVEN vs ASKED.
                    Formula rearranged, solve order flips. NEW TYPE NODE.
      examples: x -> P (forward)  vs  P -> x (inverse, deck p034-037)
                normalize first  vs  given k find probabilities
                distribution -> moments  vs  moments -> distribution parameters
                    (moment matching! method of moments is the systematic version)

  M2  RE-CONDITION  change a structural condition: independence on/off,
                    with/without replacement, sigma known/unknown, n small/large,
                    support discrete/continuous, equal/unequal probabilities.
                    NEW TYPE NODE when the needed formula changes.
      examples: binomial (with replacement) vs hypergeometric mean (without)
                n=25 CLT applies vs n=9 needs a normal population (clt p017-018)
                p constant vs p varies (would be new; not in corpus)
                independent events vs dependent (conditional machinery)

  M3  RE-TARGET     same setup, different target functional: P(X=k) -> P(X<=k)
                    -> P(X>k) -> E(X) -> Var(X) -> E[h(X)] -> conditional ->
                    expected count over N runs. Each target change adds a step
                    (complement turn, second moment, ratio) = NEW TYPE NODE
                    when the method differs, same node when it is the same sum
                    with a different upper limit.
      examples: P(X=2) vs P(X>=2) (pens i vs ii: complement turn)
                E(X) vs E(2X+1)^2 (p094: second moment + algebra)
                P(X=2) vs P(X=2 | X>=1) (conditional, NEW, see 3.d)

  M4  COMPOSE       nest two models, or chain the output of one into the other.
                    NEW TYPE NODE, always. The corpus already has one instance.
      examples: Poisson per-minute then binomial over minutes (p3 p026)
                estimator comparison then consistency then efficiency (p5 p019-021)
                expected value then decision (magazine order 3 vs 4, p109-111)
```

## 3. NEW TYPE NODES the radical analysis generates (not listed before)

These arise from M1/M2/M3/M4 mutations of corpus models. Every number below was computed
on the machine this session.

### 3.a DESIGN / MIN-SIZE INVERSION  (M1 under binomial, CLT, CI)
```
  Ask pattern: "how many/few trials to guarantee/achieve X"
  instances:
    binomial: smallest n with P(X>=1) >= 0.9, p = 0.1
              -> n = 22  (1 - 0.9^22 = 0.9015; n = 21 gives 0.8906)
    CI:       smallest n with margin <= 0.5, z = 1.96, sigma = 1.5
              -> n >= 34.57, so n = 35
    Chebyshev: smallest k for a stated lower bound (existing 19/24 already)
  why new: the unknown sits in the SIZE of the experiment, not in a probability.
  where it slots: binomial block AND CLT block AND Chebyshev block (3 sites, one type)
```

### 3.b PARAMETER RECOVERY, THE GENERAL FAMILY  (M1 across ALL distributions)
```
  Ask pattern: a probability statement about the variable, recover a parameter.
  The corpus has it only piecemeal; it is one cross-chapter type:
    binomial:  P(X=5)=2P(X=4) -> p = 5/8           (p3 p017, already charted)
    Poisson:   P(X=1)=0.2P(X=2) -> lambda = 10     (p3 p025, already charted)
    Poisson:   P(X=0) = 0.1 -> lambda = ln 10 = 2.3026   (NEW adjacency)
    exponential: P(T>2) = 0.5 -> lambda = ln2/2 = 0.3466 (NEW adjacency)
    normal:    P(X<100) = 0.90 with sigma = 10 -> mu = 87.18  (M1 of the forward table read)
    uniform:   P(X>4) = 1/3 on (1, b) -> b = 5.5   (endpoint recovery)
    moment matching: given E and Var, solve the two parameters (binomial np, npq ->
                     n and p; normal mu, sigma^2 directly; uniform a, b from mean, var)
  why new: one method (solve the probability equation for the parameter), five chapters.
  the exam form: ANY of the five is fair game; drill the pattern once, all five open.
```

### 3.c DERIVED-VARIABLE ALGEBRA  (M2/M4 around rvs)
```
  Ask pattern: a function of one or more rvs; find its distribution or a probability.
  corpus instances: sum of two dice (p054), M = max (D1-17), Y = X+4 (D1-29),
  h(X) = X - .01X^2 (D1-22), T2 = 2X1 + 3X3 - 4X2 (p5 p021)
  unlisted but adjacent (same methods, verifiable):
    min of two dice (mirror of max; pmf derivation identical in structure)
    difference of dice (support -5..5; Var same as sum = 35/6 by the plus rule)
    sum of two independent Poissons (A2 A12, one line, already half-covered)
    sum of independent binomials with the SAME p is binomial again:
        B(5,0.3) + B(7,0.3) = B(12,0.3); verified by convolution to 1e-12
  why new: the "algebra of rvs" type node (sum, difference, min, max, scale, shift,
  combine) deserves one tree entry; the corpus teaches the pieces in five places.
```

### 3.d CONDITIONAL ON AN INEQUALITY, DISCRETE  (M3)
```
  Ask pattern: P(X = k | X >= j) or similar for a discrete distribution.
  corpus: conditionals exist for continuous (D1-25), normal (A1 long 1), exponential
  (A2 B5); NOT for binomial/Poisson.
  instance: pens, X ~ B(12, 0.1): P(X=2 | X>=1) = 0.2301 / 0.7176 = 0.3207  (computed)
  why new: same ratio machinery, discrete support; the setter can ask it tomorrow.
```

### 3.e DECISION / OPTIMIZATION STORY QUESTIONS  (M4, target = a choice)
```
  Ask pattern: "which option is better" with expectation behind it.
  corpus: magazine order 3 vs 4 (D1-23), technicians capacity (A2 B1 overflow),
  estimator choice (p5, lms-theory). Unlisted as a type but already 3 instances.
  the general form: compute E (or a probability) for each option, compare, answer
  in words. The "interpret the result" tail of every A1 application question is
  this type in disguise.
```

### 3.f APPROXIMATION-CHOICE QUESTIONS  (M2 around the Poisson limit)
```
  corpus: Poisson approximation to binomial (A2 D3, p3 p027 style).
  adjacent, standard, not in corpus: binomial -> normal for large n
  (B(100,0.4), P(X<=45) with continuity correction z = (45.5-40)/4.899 = 1.123).
  Ask pattern: "which distribution models this" and "is the approximation valid".
  why new: approximation validity is a named decision, not a computation.
```

### 3.g MSE / BIAS-VARIANCE COMPARISON  (M3/M4 in estimation)
```
  corpus: T4 trap (biased but smallest variance loses on "efficiency").
  the missing radical: compare on MSE = Var + Bias^2 instead.
  instance: T4 = (X1+X2+X3)/2 with sigma=1, mu=10: MSE = 3/4 + 100/4 = 25.75
  vs T3 unbiased Var = 1/3. On efficiency T3 wins; on MSE a biased estimator can win
  when the bias is small vs variance, or lose catastrophically here.
  the sheet already carries MSE = Var + Bias^2 in the checks; the QUESTION form
  ("which has smaller MSE") is the new node.
```

### 3.h FORMULA SHEET GAP CHECK (this analysis found these)
```
  geometric distribution has pmf taught (p057-059) and E = 1/p graded (A1 short 4)
  but the sheet does NOT list E = 1/p or Var = (1-p)/p^2. ADD to sheet:
      geometric  pmf (1-p)^(x-1) p, E = 1/p, Var = (1-p)/p^2
  hypergeometric mean nK/N used and graded (A1 long 3) but not on the sheet. ADD:
      hypergeometric  E = n K/N  (var = np(1-p)(N-n)/(N-1), adjacency)
  these are real coverage gaps in the revision material, both already graded once.
```

## 4. The rule table: does a change make a new type

```
  change                              new type?   why
  ------------------------------------------------------------------------------
  numbers only                        NO          incidental
  names / story / units               NO          incidental
  rounding of given data              NO          incidental
  which value is asked of the SAME formula   NO   same substitution
  forward <-> inverse (x <-> P)       YES         solve order flips (M1)
  point -> tail or interval           YES         complement or F(b)-F(a) step (M3)
  unconditional -> conditional        YES         ratio step (M3)
  single -> expected count over N     YES         N x P step (M3)
  independence assumed -> not         YES         rule set changes (M2)
  replacement -> no replacement       YES         distribution changes (M2)
  n small -> n large (same test)      MAYBE       only if the applied distribution
                                                  changes (M2: CLT applies or not)
  one model -> two nested models      YES         composition (M4)
  target E <-> Var <-> E[h(X)]        YES         moment order changes (M3)
  efficiency <-> MSE comparison       YES         criterion changes (M3)
```

## 5. The study protocol this implies (solve, mutate, re-solve)

```
  for every corpus question:
    1. solve it as printed
    2. write its MODEL: name the fixed skeleton (formula + steps) and circle the slots
    3. apply M1 once (invert the ask), solve the inverted version
    4. apply M2 once (flip one condition), solve
    5. apply M3 once (change the target), solve
  a skeleton is owned only when you can solve all four states of it.
  the exam, by design, sets NEW instances of OLD models (M0) and often one M1/M2/M3
  twist. instance practice without mutation practice is half the job.
```

## 6. Extra completeness checks (the "what else should we check" list)

```
  1  every cross-deck duplicate skeleton: pens vs sensors vs bulbs vs jobs (done,
     all are M0 re-skins of 2 skeletons: point probability and complement tail)
  2  formula sheet gaps: geometric E/Var, hypergeometric mean (found above, patch)
  3  the boundary block: CI machinery appears inside a lect-19-21 example. If the
     paper slips lecture 25 content in, sheet section J is the insurance
  4  the textbook: slides derive from Devore 8e; if any Devore exercise set is in
     play, that is an unbounded source. No copy on disk. FLAG
  5  CWS quizzes (30 marks, in-class): none on disk. The two assignments are the
     only setter-authored instruments we hold. Ask for quiz papers if any survive
  6  past MTE papers: none on disk; Google Drive sweep blocked (OAuth dead). FLAG
  7  the [H] blocks: all eight stay first priority (no slides at all)
  8  one-side Chebyshev variant: P(X - mu >= c) <= sigma^2 / (sigma^2 + c^2), the
     one-sided form. The corpus uses the two-sided form only. The one-sided form is
     a real adjacency; keep in sheet as a footnote
  9  mode questions (binomial mode formula, sheet mentions "where the ratio crosses
     1"): no graded instance; low risk; one line in the sheet
 10  continuity corrections: not in corpus; risk only if they ask binomial->normal;
     one line in the sheet
```

## 7. Verified numbers used in this file

```
  binomial min-n       n=22 (0.9015), n=21 fails (0.8906)
  Poisson from P(0)    lambda = 2.3026
  exponential quantile lambda = 0.3466 (P(T>2) = 0.5)
  normal from percentile mu = 87.18 (P(X<100)=0.90, sigma 10, z=1.2816)
  uniform endpoint     b = 5.5 ((b-4)/(b-1) = 1/3)
  pens conditional     P(X=2|X>=1) = 0.3207
  binomial additivity  B(5,.3)+B(7,.3)=B(12,.3), convolution matches direct to 1e-12
  MSE example          MSE(T4) = 25.75 vs Var(T3) = 0.3333 (sigma=1, mu=10)
  binomial->normal     z = 1.123 with continuity correction (B(100,.4), P<=45)
  hypergeometric var   0.56 vs binomial var 0.64 (the (N-n)/(N-1) factor)
  negative binomial    P(first success on flip 3, p=.5) = 0.125; two-heads-by-3 = 0.25
  one-sided Chebyshev  bound sigma^2/(sigma^2+c^2); two-sided stays 1/k^2
```
