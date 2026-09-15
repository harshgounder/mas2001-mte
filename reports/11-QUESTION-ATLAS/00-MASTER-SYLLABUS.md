# Master syllabus map and hidden layers, MTE MAS2001

Built 15 September 2026, second pass (deep). Supersedes the first tree draft. Everything
here comes from the full read of all 348 converted pages and all 112 counted items, and
every number quoted was recomputed on the machine.

Legend:
```
  [+]  taught on slides AND used by questions, named in the syllabus
  [~]  used by questions, sits INSIDE the topic, NOT named in the MTE syllabus list
  [H]  used by questions but no batch-1 slide taught it; Chebyshev left this class on
       15 Sep 2026 (S&P L10-11 deck). Batch-2 decks L1-7 and L8-9 are unconverted, so
       these marks stay provisional until the U12 to U19 dedup pass
  [!]  already graded in assignment 1 or 2
  refs deck = notes-lecture-series-01-09 | p3 = ppt3 | p4 = ppt4 | clt = standard-error-clt
       p5 = ppt5 | lt = lms-theory-of-estimation
  item IDs (D1-x, A1-x, A2-x) come from 00-COUNT-REGISTER.md
```

## 1. The sixteen syllabus lines against slides

| # | syllabus line (verbatim) | lectures | slides | where |
|---|---|---|---|---|
| 1 | Introduction of the Course | 1 | full, not examined | deck p001 to p011 |
| 2 | Basic terminology and concepts of probability Theory | 2 | FULL | deck p012 to p050 |
| 3 | Random variables, Discrete, Continuous | 3-4 | FULL | deck p051 to p062, p112 to p147 |
| 4 | Probability mass and density functions, Cumulative distribution functions | 5-6 | FULL | deck p063 to p087, p112 to p139 |
| 5 | Expectation of random variables | 7 | FULL | deck p088 to p094, p140 to p147 |
| 6 | Expectation of random variables, Independent random variables | 8-9 | HALF | deck p095 to p111: expectation+variance yes, independent-rv rules [H] |
| 7 | Chebyschev's inequality | 10-11 | YES (new batch) | S&P L10-11 deck (9p), CORRECTED 15 Sep; sheet E + bank 6 + mock B1 remain the drill |
| 8 | Binomial distribution | 12 | FULL | p3 p001 to p018 |
| 9 | Poisson distribution | 13 | FULL | p3 p019 to p028 |
| 10 | Uniform distribution (Continuous) | 14 | FULL | p4 p001 to p006 |
| 11 | Normal distribution | 15 | FULL | p4 p007 to p037 (+ [H] landmarks, two-table discipline) |
| 12 | Exponential distribution | 16 | FULL | p4 p038 to p043 (+ [H] memoryless) |
| 13 | Sampling: Population and sample; Standard error | 17 | FULL | clt p001 to p005 |
| 14 | Central Limit Theorem | 18 | FULL | clt p006 to p018 |
| 15 | Theory of Estimation: parameter and statistic, point and interval estimation | 19 | FULL | p5 p001 to p007, lt p001 to p015 |
| 16 | Characteristics of a good estimator | 20-21 | FULL | p5 p008 to p021, lt p016 to p030 (+ sufficiency only in lt) |

## 2. The complete tree, lecture by lecture

### Lecture 2: probability foundations (deck p012 to p050)

```
2.1 what statistics is [+]
    definition: collection, presentation, analysis, interpretation (p014)
    numerical-statement criterion: "Ram has 100 Rs" is not statistics, an average is (p012)
    importance list (p015, p016) | limitations + biased-survey example (p017)
    no graded items; read for framing only
2.2 random experiment and sample space [+]
    outcomes known, which one unknown (p023)
    spaces: coin {H,T}, die {1..6}, two coins {HH,HT,TH,TT}, two dice 6x6=36 (p024)
    [~] ordered pairs matter: two dice give 36, not 21
    [~] structured coding of outcomes: tournament notation 1324 = 16 outcomes (D1-1)
2.3 events and set relations [+]
    complement, union, intersection, null event, pairwise disjoint (p032 to p037)
    Venn diagrams (p038 to p040)
    counter-example style: even vs prime on a die share 2, so not disjoint (p025)
2.4 axioms and rules [+]
    P(S)=1, P(A)>=0, countable additivity (p044)
    equally likely: favourable/total (p044)
    addition rule, both forms (p045) | complement rule (p045) | multiplication rule (p045)
    conditional definition P(A|B)=P(AnB)/P(B), renormalization (p050)
    [~] complement discipline: "at least one", "none", "rejected" all become 1 - lower tail
        (A1 MCQ, p3 pens part ii, D1-2 part c, D1-15, A2 B1, A2 C3) [H as a method]
2.5 counting [+]
    P(n,r), C(n,r), repeated-item permutations (p043)
    [~] C(n,r) as the engine: C(6,2)=15 (D1-2), C(4,2) (D1-2b), lineup C's (D1-3)
    [~] disjoint-union counting: 1 - P(A) - P(B) with A,B disjoint (D1-2d)
2.6 conditional probability [+]
    chain from definition (p050): camera example .30/.40=.75 and .30/.60=.50
    [~] conditional on a continuous model via integrals: 5/12 (D1-25)
    [~] conditional on a normal: death interval given survival to 60: 0.4863 (A1 long 1)
    [~] conditional with exponential: P(X<1|X<2) (A2 B5, errata 9)
2.7 independence of events [+]
    P(AnB)=P(A)P(B) <=> P(A|B)=P(A) (p027, p028)
    mutual independence of n events (p028)
    [~] independence as a modeling assumption inside stories (batteries D1-15, dice)
    [H] rv-level independence rules, see lecture 8-9 below
```

### Lectures 3-4: random variables (deck p051 to p062, p112 to p147)

```
3.1 definition: function from S to the reals (p051)
    Bernoulli 0/1 (p052) | counting rv (p053: heads) | dice sum (p054 to p055) | two coins (p056)
    geometric N = flips to first head (p057 to p059) [~] countably infinite support
    car lifetime as continuous (p060) | discrete vs continuous taxonomy (p061, p063, p076)
3.2 [~] functions of an rv
    Y = X + 4 hospitalization (D1-29) | h(X) revenue 25X - 8.5 (D1-22) | M = max of two dice (D1-17)
    [~] support identification before any pmf work
3.3 continuous definition [+] P(X=c)=0, intervals (p112 to p116, p120 to p123)
    [~] "probability zero is not impossibility" (p122)
```

### Lectures 5-6: pmf, pdf, cdf (deck p063 to p087, p112 to p139)

```
4.1 pmf [+]
    conditions p(x)>=0, sum=1 (p064)
    [~] find k by normalization: 15k=1 (D1-14); 10k^2+9k=1 with k=1/10 (D1-12, A1 long 2)
        also the quadratic root selection trap
    [~] pmf built from counting: boards (D1-16), dice maximum (D1-17), batteries (D1-15)
    graphs: line and histogram (p067 to p069), steps (p083 to p084)
4.2 cdf discrete [+]
    definition F(x)=P(X<=x) (p074) | nondecreasing (p078) | proof question (D1-18)
    [~] construction per interval: boards (D1-16c), dice max (D1-17b)
    [~] pmf from cdf: f(n)=F(n)-F(n-1) (p078)
    [~] interval via cdf for integer rv: F(b)-F(a-1) (p135)
    [~] minimum c with P(X<=c)>1/2: c=4 because F(3)=0.5 is not > (D1-12, A1 long 2 iv)
4.3 pdf continuous [+]
    f>=0, integral=1, area = probability (p117, p118)
    [~] normalize a non-pdf: f(x)/k (p119)
    cdf: F(x)=int to x, P(X>a)=1-F(a), P(a<=X<=b)=F(b)-F(a) (p130 to p135)
    [~] F'(x)=f(x), density from cdf: F=(x-1)^4/16 (D1-28) and exercise pair (D1-27)
    [~] piecewise pdf integration: bus triangle (D1-26, errata 13), 1/3-2/3 mix (D1-27i), |x| (D1-27ii)
    [~] two-piece integration practice: f(x)=2x (D1-24), Pareto improper integrals (D1-30)
```

### Lecture 7: expectation (deck p088 to p094, p140 to p147)

```
5.1 E(X)=sum x p(x) (p088) | die example (p089) | E[h(X)] definition (p090)
    [~] E(X^2), E(2X+1)^2 via laws (D1-21) | revenue tables h3, h4 (D1-23) | freezer chain (D1-22)
5.2 properties: E(c)=c, E(cX)=cE(X) (p092), E(aX+b) proof (D1-20, p093)
5.3 continuous: integral forms (p140 to p143), linear case (p144)
    [~] E with convergence condition: Pareto k>1 else infinite (D1-30)
    [~] shifted rv: E(Y)=8 days for Y=X+4 (D1-29)
    [~] [H] expected count over N repeats: E = N x P (p3 p018 sets, A2 B4 bulbs/batteries)
        never stated as a rule on any slide; used in 4+ places
```

### Lectures 8-9: expectation + INDEPENDENT RANDOM VARIABLES (deck p095 to p111)

```
6.1 variance machinery [+]
    Var(X)=E[(X-mu)^2] (p097) | shortcut E(X^2)-[E(X)]^2 (p101 to p103)
    Var(c)=0, Var(cX)=c^2 Var(X) (p103) | V(aX+b)=a^2 V(X), sd=|a|sd (p104, p105)
    [~] sd interpretation paragraphs (p096, p099, p106)
    [~] Var via two integrals from pdf: continuous block (p144, p145)
    [~] Var of a sum of dice: 2 x 35/12 = 35/6 (A1 short 5) [H edge below]
6.2 INDEPENDENT RANDOM VARIABLES: THE MAIN HIDDEN BLOCK [H][!]
    E(XY) = E(X)E(Y) under independence          no slide anywhere
    Var(X+Y) = Var(X) + Var(Y) under independence no slide anywhere
    Var(X-Y) = Var(X) + Var(Y)                    no slide anywhere
    already graded: A1 short Q5 (dice sum bound needs Var(sum)=35/6)
    implicitly needed by: Var(Xbar)=sigma^2/n (clt), estimator variances (p5 p018, p021),
    Poisson additivity (A2 A12), linear combination estimators (p5 p021 T2=29 sigma^2,
    where the -4X2 coefficient squares to +16: the X-Y rule in disguise)
    source of truth: formula sheet sections C and D (lines 90, 106)
6.3 linearity contrast [+] E(X+Y)=E(X)+E(Y) always, no independence needed (sheet line 94)
```

### Lectures 10-11: CHEBYSHEV, deck arrived 15 Sep (was: no slides) [~]

```
7.1 statement P(|X-mu| >= k sigma) <= 1/k^2 | complement form >= 1 - 1/k^2
7.2 distribution-free: only finite mean and variance needed (A1 MCQ 10)
7.3 k extraction from interval half-width (60 to 80 with mu 70, sd 5: k=2)
7.4 tail vs complement form: the 1/9 vs 8/9 trap (mock B1 teaches it)
7.5 apply to a sum: find Var first, then bound (dice: 35/54 vs actual 1/3, A1 short 5)
7.6 lower bound for counts interval (600 throws: k=2.19, 19/24, A1 short 6)
7.7 proportion framing in reverse (marks: at least 75 percent, A1 app 4)
7.8 applicability statement (A1 MCQ 5, MCQ 10)
graded 5 times, deck arrived 15 Sep (S&P L10-11). sources: deck, sheet E, bank section 6, mock B1.
```

### Lecture 12: binomial (p3 p001 to p018)

```
8.1 setup conditions: 2 outcomes, n finite, trials independent, p constant (p008, p011)
8.2 pmf C(n,x) p^x q^(n-x), X~B(n,p) (p009, p010)
8.3 mean np, var npq (p012)
8.4 complement tails: P(X>=2)=1-[P(0)+P(1)] (p015) | direct compute discipline (p014)
8.5 parameter recovery from ratio: P(X=5)=2P(X=4) -> 3p=5q -> p=5/8 (item 2-03, the irregular die)
8.6 [H] expected count over repeats: 10000 x (3/8)^10 = 0.5499 (p3 die part 2, errata 2)
8.7 [~] framing identification: physical die -> success = even number
8.8 limit to Poisson conditions (p022) | used by A2 D3 (Poisson approximation)
8.9 MCQs from A2: var npq (Q2), max successes n (Q9)
```

### Lecture 13: Poisson (p3 p019 to p028)

```
9.1 rare events model (p020, p021 list)
9.2 pmf e^-l l^x / x! (p023) | mean = var = lambda (p024)
9.3 [~] lambda from a probability ratio: P(1)=0.2P(2) -> lambda=10 (p025, errata-free)
9.4 [~] rate and window scaling: 2/min, 15/hr, 4/hr, conversions (p026, A2 D2)
9.5 [~] P(0)=e^-lambda (p025, A2 D3)
9.6 [~] tail sums: P(X>2)=1-P(0)-P(1)-P(2)=0.8753 exact (A2 C3, key prints 0.8754, minor)
9.7 [~] capacity overflow: "demand rejected" = P(X >= 4) = 0.2424 (A2 B1)
9.8 [~] NESTING: Poisson per minute then binomial over 5 minutes: 32e^-10 = 0.00145 (p026)
9.9 [~] Poisson approximation to binomial: 5000x0.001 (p027), 200x0.01 (A2 D3)
9.10 [+] additivity of independent Poissons (A2 A12, sheet line 182)
```

### Lecture 14: uniform (p4 p001 to p006)

```
10.1 pdf 1/(b-a), mean (a+b)/2, var (b-a)^2/12 (p6 area)
10.2 [~] length ratio shortcut: P(X<5)=(5-2)/6=0.5 (item 3-01, p4 p006)
10.3 [~] clipping to support: P(c<X<d) with d>b -> (b-c)/(b-a) (A2 A10)
10.4 [~] absolute values to intervals: P(|X|<2), P(|X-2|<2), P(X>K)=1/3 -> K=1 (A2 B8)
10.5 [~] rounding error [-0.5, 0.5]: P(|err|>0.2)=0.6 (A2 C4)
10.6 [~] two uniforms combined: bus waiting triangle pdf (D1-26) cross-link
```

### Lecture 15: normal (p4 p007 to p037)

```
11.1 density, mu and sigma^2, symmetry, mean=median=mode (p008, p011, p012)
11.2 standardization Z=(X-mu)/sigma (p019, p028)
11.3 TWO TABLE CONVENTIONS, know both [H discipline]
     cumulative F(z) = P(Z<z): p022 table, textbook appendix, "F(0.12)=0.5478"
     area from 0, phi(z): p023 to p025 tables, assignments give phi(1.04)=0.35 style
     conversion: phi(z) = F(z) - 0.5. identify which one the paper gives BEFORE substituting
11.4 left tail and negative z: P(Z<-2)=1-0.9772=0.0228 (p026, p027)
11.5 upper tail: P(X>8.6)=1-0.5478=0.4522 (p032, p033)
11.6 interval F(b)-F(a): 45 to 62 gives 0.5764 (A2 B3)
11.7 inverse: z from table then X=mu+z sigma: 20 percent lower tail -> 3.80 (p034 to p037)
11.8 [H] landmarks 68.27 / 95.45 / 99.73 (A2 A11 asks it; no slide teaches it)
11.9 [H] two-unknown system: 46 percent pass at 40, 9 percent distinction at 75 ->
     sigma=28.23, mu=37.18 -> 37.2; re-exam cutoff 30.4 (A2 C2, errata 10)
11.10 [~] expected count N x P: 5000 batteries -> 274/576/4487 (A2 B4), 10000 bulbs -> 7888 (A2 D1)
11.11 errata 8: p030 figure prints sigma = 10, must be 5.0
```

### Lecture 16: exponential (p4 p038 to p043)

```
12.1 pdf lambda e^-lambda t, cdf 1-e^-lambda t, survival e^-lambda t (p040, p041)
12.2 mean 1/lambda, var 1/lambda^2 (p041) | errata 4: p040 inverts the lambda wording
12.3 [H][!] memoryless: P(T>s+t | T>s)=P(T>t) (A2 MCQ Q5 + A2 C1; no slide defines it)
12.4 [~] conditional with cdf ratio: P(X<1|X<2)=0.6225 (A2 B5, errata 9)
12.5 [~] mean to lambda both directions (mean 2 -> lambda 0.5; lambda 1/2 -> mean 2)
12.6 [~] wait-time phrasing with unit conversion: 30 min at 4/hr -> 0.1353 (A2 D2)
12.7 [~] repair time: P(T>2)=e^-1, memoryless P(T>11|T>8)=e^-1.5 (A2 B7)
12.8 [~] arrival rate example on slides: 15/hr, gap under 3 min = 0.05 hr (p042, p043)
```

### Lecture 17: sampling and standard error (clt p001 to p005)

```
13.1 population vs sample, parameter vs statistic, SRS without replacement (p002, p003)
13.2 SE = sigma / sqrt(n) (p004)
13.3 [~] scaling law: quadrupling n halves SE (p005, lightbulbs 20 -> 10)
```

### Lecture 18: CLT (clt p006 to p018)

```
14.1 statement: n>=30 any shape | normal population any n | n<30 non-normal fails (p007, p008)
14.2 sample mean sd = sigma/sqrt(n)
14.3 [~] z with SE denominator: (xbar - mu)/(sigma/sqrt(n)) (p011 to p018)
14.4 [~] applications: ATM (p011-12), impurity 0.1644 (p013-14, errata 6 z=-0.94), LED (p015-16),
     machines n=9 exact normal fallback (p017-18)
14.5 [~] exact table selections: 0.4909, 0.3264, 0.4641, 0.2257, 0.4772
14.6 [~] "average of n" template vs plain normal: only the denominator differs, classic mix-up
```

### Lecture 19: estimation basics (p5 p001 to p007, lt)

```
15.1 parameter, statistic, estimator, estimate, sample space, parameter space (p003, p005)
15.2 point vs interval estimation, CI = estimate +/- margin (p004, p005 to p007)
15.3 [~] point estimate from raw data: 1640/8 = 205 ms (p022)
15.4 [~] proportion: p-hat = 465/500 = 0.93 (p023)
15.5 [~] CI with z(alpha/2): 8.4 +/- 1.96 x 0.3 = (7.81, 8.99) battery (p024) boundary item:
     uses lecture 25 machinery inside a lectures 19-21 problem; kept, flagged in register
15.6 lt p031 to p039 confidence interval block: OUT of MTE, carry no counted items
```

### Lectures 20-21: estimator properties (p5 p008 to p021, lt p016 to p030)

```
16.1 unbiasedness: E(theta-hat)=theta, bias = E - theta (p009)
16.2 [~] force unbiasedness with a constant: coefficient sum = 1 (p016 lambda=0, p020 lambda=1)
16.3 consistency: convergence in probability; two sufficient conditions
     E(Tn)->theta AND Var(Tn)->0 (p010, p011)
16.4 [~] why the sample mean is consistent (p012) | consistency of T3 given (p020 iii)
16.5 efficiency: smallest variance among unbiased (p013, p014)
16.6 [~] compare set 1: t1, t2=(X1+X2)/2+X3 BIASED (E=2mu), t3 after lambda=0; vars
     sigma^2/5 < 5sigma^2/9 -> best t1 (p015 to p018)
16.7 [~] compare set 2: T1, T2=2X1+3X3-4X2, T3 after lambda=1; vars 3, 29, 1/3 -> best T3
     (p019 to p021). THE PROTOCOL: filter unbiased FIRST, then min variance
     (a biased low-variance candidate never wins; the T4 trap in mock B4)
16.8 [~] sufficiency and Neyman-Fisher: product structure, sum is sufficient
     Poisson example + Exponential example (lt, the 2 unique items outside p5)
```

## 3. Hidden layer, complete

```
[H] independence rules of rvs (E(XY), Var(X+Y), Var(X-Y))     feeds 4 downstream areas
    Chebyshev entire topic LEFT THIS CLASS 15 Sep: S&P L10-11 deck arrived; still
    priority (asked in A1, MTE 2024-25, MTE 2025-26)
[H] memoryless property                                       2 graded uses
[H] landmarks 68.27/95.45/99.73                               1 graded use
[H] expected count N x P rule                                 graded + slide usage
[H] geometric E(N) = 1/p                                      graded (A1 short 4); pmf taught, E not
[H] hypergeometric mean nK/N                                  graded (A1 long 3); no slide mentions it
[~] structured counting without listing (tournament)          graded
[~] ordered vs unordered sample spaces (36 outcomes)          graded
[~] complement discipline as a named method                   everywhere
[~] probability-ratio parameter recovery (binomial + Poisson) same trick, two chapters
[~] two-normal-tables discipline                              every normal/CLT numeric question
[~] absolute-value to interval conversion                     uniform block
[~] piecewise function handling                               pdfs, cdfs, revenue
[~] unit conversion inside stories                            exponential, Poisson, CLT
```

## 4. Cross cutting micro skills (drill these, they carry marks)

```
1  complement turn: "at least / none / more than / rejected" -> 1 minus lower tail
2  table discipline: identify convention, pick row, interpolate or match, mind the sign
3  exact powers: 0.9^10, 0.9^12, e^-2.5 hand arithmetic without calculator panic
4  ratio recovery: set two pmf expressions equal, cancel, solve
5  N x P counts: "expected number of X in N trials" = N times the probability
6  piecewise integration with correct limits, no double counting at the breakpoint
7  |expr| < c  <=>  interval, and interval length over support length
8  pmf sanity: sum to 1, find k, check both conditions
9  cdf sanity: nondecreasing, right limits 0 and 1, jumps at atoms
10 rounding discipline: keep exact till the end (battery SD lesson, errata 12)
11 read the ask: "at most / at least / between / inclusive / neither / exactly"
12 draw the normal curve and mark the area before computing anything
```

## 5. Errata map (full list, see reports/09-ERRATA.md)

```
1  p3 insurance prints 0.1745, value 0.1755
2  p3 die expected sets prints 0.549, value 0.5499
3  A1 key truncates 0.0915, value 0.0916
4  p4 p040 inverts lambda wording, p041 is right
5  A1 long 2: normalisation is 9k + 10k^2 = 1, root 1/10 exact
6  clt impurity: prints Z=-0.4, must be -0.94 (answer 0.1644/0.1637 fine)
7  notation note: X ~ N(mu, sigma^2), second parameter is VARIANCE
8  p4 p030 figure prints sigma = 10 under mu = 8, must be 5.0 (source text layer confirmed)
9  A2 B5: prints 0.5679, computed (1-e^-0.5)/(1-e^-1) = 0.6225
10 A2 C2: key prints mu = 37.5; its own cutoff 30.43 reproduces with mu = 37.2;
   from the given tables mu = 37.18 -> 37.2, sigma = 28.23 -> 28.2, cutoff 30.4
11 A1 long 3: prints 0.808 without replacement; both cases are exactly 0.8 (nK/N = np = 0.8)
12 A1 app 3: exact var 0.9475, exact sd 0.9734 -> 0.97; key's 0.975 and 0.98 come from
   taking sqrt of the rounded variance
13 deck bus example (p127, p129): statement digits sit under the footer watermark (read as
   6 or 8 by different readers); the working's first integral bound (3) contradicts its own
   event (Y < 2); the final 2/5 = 0.4 is correct for Y < 2 or Y > 6 (0.08 + 0.32), and the
   printed bound 3 would give 0.5. Also a doubled equals sign on that line.
14 A2 C3 minor: exact 0.87535 -> 0.8753; key prints 0.8754 (sum of rounded terms)
```

## 6. Inventory recap

```
teaching items 60 (55 unique) | assignments 52 | total 112 items, 107 unique
per deck: deck01 30, p3 6, p4 7, clt 5, p5 5, lt 7 (5 repeat p5, 2 unique)
excluded out of MTE: MLE 16 pages, MoM 11 pages, handout 7 pages, lt CI block 10 pages
```
