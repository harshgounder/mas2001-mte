# MTE MAS2001: the full topic universe

Built 16 September 2026. Consolidates and supersedes (for reading order only, nothing is
deleted) the topic layer spread across `00-MASTER-SYLLABUS.md`,
`00-SYLLABUS-FULL-EXPANDED.md`, `00-TOPIC-FLOW.md`, `00-MUTATION-ANALYSIS.md` and
`00-TYPE-SPACE-AUDIT.md`. New here: the evidence that landed after 15 Sep (the seven ETE /
summer / re-sess papers, the four S&P decks, the 2025-26 assignment bundle) is folded into
the tree as confirmed nodes instead of sitting in separate reports.

Scope: MTE lectures 1 to 21 only. Out-of-MTE material is excluded and listed at the end.

## 0. How to read this, and where every line comes from

Status flags on every node:

```
  [+]  taught on slides AND used by questions, named in the MTE syllabus list
  [~]  used by questions, sits inside the topic, NOT named in the syllabus list
  [H]  used by questions but NO slide teaches it (learn from the formula sheet)
  [!]  already graded (assignment, past paper, ETE, or deck)
  [C]  confirmed by a question that arrived after 15 Sep (new here)
  [-]  boundary: uses lecture 22+ machinery but is named in the MTE list, kept and flagged
```

Sources, one per layer:

```
  syllabus          ~/PS/syllabus.txt (16 lines, verbatim below)
  slides            converted pages in md/ (batch 1 + U01 + U02/U03 papers)
  atlas             reports/11-QUESTION-ATLAS/00-*.md (15 Sep)
  ETE intake        reports/17-ETE-INTAKE.md (97 blocks, 7 papers)
  deck ledger       reports/evidence/deck-block-ledger-20260916.csv (30 blocks)
  bundle ledger     reports/evidence/assignment-bundle-ledger-20260916.csv (119 items, PR 14)
  count register    reports/11-QUESTION-ATLAS/00-COUNT-REGISTER.md (128 / 123 through U01)
```

Warning carried forward: the batch-2 decks L1-7 and L8-9 were unconverted when the [H] marks
were set, so a few [H] marks may retire at the U12-U19 dedup pass. The four S&P decks ARE now
read (30 blocks) and their content is folded in below.

================================================================================
1. THE SIXTEEN SYLLABUS LINES (verbatim) AGAINST SLIDES
================================================================================

```
  #   syllabus line (verbatim)                                  lect   slides   where
  1   Introduction of the Course                                  1    full     deck p001-011
  2   Basic terminology and concepts of probability Theory         2    FULL     deck p012-050
  3   Random variables, Discrete, Continuous                      3-4   FULL     deck p051-062, p112-147
  4   Probability mass and density functions, CDFs                5-6   FULL     deck p063-087, p112-139
  5   Expectation of random variables                              7    FULL     deck p088-094, p140-147
  6   Expectation of random variables, Independent rvs            8-9   HALF     deck p095-111 (indep rules [H])
  7   Chebyschev's inequality                                    10-11  YES      S&P L10-11 deck (9p), arrived 15 Sep
  8   Binomial distribution                                       12    FULL     p3 p001-018
  9   Poisson distribution                                        13    FULL     p3 p019-028
  10  Uniform distribution (Continuous)                           14    FULL     p4 p001-006
  11  Normal distribution                                         15    FULL     p4 p007-037
  12  Exponential distribution                                    16    FULL     p4 p038-043
  13  Sampling: Population and sample; Standard error              17    FULL     clt p001-005
  14  Central Limit Theorem                                       18    FULL     clt p006-018
  15  Theory of Estimation: parameter and statistic, point and
      interval estimation                                        19    FULL     p5 p001-007, lt p001-015
  16  Characteristics of a good estimator                       20-21  FULL     p5 p008-021, lt p016-030
```

================================================================================
2. THE TREE, TOPIC -> SUBTOPIC -> SUB-SUBTOPIC (all 16 topics)
================================================================================

--------------------------------------------------------------------------------
T1  INTRODUCTION OF THE COURSE  (deck p001-011)  not examined
--------------------------------------------------------------------------------
```
1.1 course mechanics
    1.1.1 code MAS2001, 3 credits, LTPC 2-1-0-3 [p004]
    1.1.2 assessment: MTE 30 closed book | CWS 30 | ETE 40 closed book | total 100 [p008]
    1.1.3 course outcomes CO1 probability, CO2 distributions, CO3 estimation, CO4 testing [p006-007]
    1.1.4 faculty Dr Vivek Singh, deck dated 23 Jul 2026 [p001]
1.2 syllabus and books
    1.2.1 syllabus list [p009] + lecture plan with MTE/CWS/ETE tags [handout p004-005]
    1.2.2 references [p010]: Goon/Gupta/Dasgupta, Kendall/Stuart, Casella/Berger, Hogg/Tanis, Feller
    1.2.3 textbook [p011]: Devore 8e (the deck's rv material derives from it)
1.3 graded items: NONE. Framing only.
```

--------------------------------------------------------------------------------
T2  PROBABILITY FOUNDATIONS  (deck p012-050)  lect 2
--------------------------------------------------------------------------------
```
2.1 what statistics is
    2.1.1 definition [p014]: collection, presentation, analysis, interpretation (four verbs, in order)
    2.1.2 origin [p012]: status (Latin), statista (Italian), statistik (German)
    2.1.3 numerical-statement criterion [p012]: all statistics are numerical statements; NOT all
          numerical statements are statistics. counter: "Ram has 100 Rs" is not; positive: an average is
    2.1.4 importance [p015-016, p020-022]: engineer fields + real-life boxes (disease, stock risk,
          quality control, traffic, reliability, signal processing)
    2.1.5 limitations, all four [p017]: qualitative phenomena, individuals not studied, laws not exact,
          liable to misuse; worked misuse: satisfaction survey run only on loyal customers
    2.1.6 graded items: none. framing only.
2.2 random experiment, outcome, sample space, event
    2.2.1 random experiment [p023]: all outcomes known, which one unknown; four examples
    2.2.2 sample space [p024]: coin {H,T}; die {1..6}; two coins {HH,HT,TH,TT}; two dice 6x6 = 36
          [-]  ordered pairs matter: two dice give 36, not 21
    2.2.3 structured outcome coding [D1-1, p041-042]: tournament teams 1-4, outcome code "1324";
          (a) S = 16 outcomes, (b) 1 wins = 4, (c) 2 reaches final = 8, (d) A u B = 12, A n B = phi
          [~]  the skill: build a code that carries all information, enumerate without duplicates
2.3 event algebra (set relations)
    2.3.1 complement A' [p032]
    2.3.2 union A u B [p033]: includes the overlap
    2.3.3 intersection A n B [p034]
    2.3.4 null event phi [p035]
    2.3.5 mutually exclusive / disjoint [p035], pairwise version [p037]
    2.3.6 counter-example style [p025]: even {2,4,6} and prime {2,3,5} share 2, NOT disjoint
    2.3.7 Venn diagrams [p038-040]: four shaded cases
    2.3.8 three-event extension [p036]: A u B u C = at least one
2.4 axioms and probability rules
    2.4.1 Kolmogorov axioms [p044]: P(S)=1; P(A)>=0; countable additivity
    2.4.2 equally likely [p044]: favourable/total; range 0<=P<=1; scale p018-019
    2.4.3 addition rule [p045]: P(AuB)=P(A)+P(B)-P(AnB); disjoint drops the correction
    2.4.4 complement rule [p045]: P(A^c) = 1 - P(A)
    2.4.5 multiplication rule [p045]: P(AnB)=P(A)P(B|A); independence case P(A)P(B)
    2.4.6 complement discipline as a named method [~][H][!]
          "at least one" -> 1 - P(none);  "no X" -> the zero case;  "rejected/overflow" -> 1 - lower tail;
          "more than k" -> 1 - F(k)
          sites: A1 MCQ style, p3 pens(ii), D1-2c (1-1/15), D1-15, A2 B1 (0.2424), A2 C3 (0.8753)
2.5 counting
    2.5.1 permutations P(n,r) [p043]
    2.5.2 combinations C(n,r) [p043]
    2.5.3 repeated-item permutations n!/(n1!n2!...) [p043]
    2.5.4 factorial reminder [p006]
    2.5.5 C(n,r) as the engine inside probability [~]
          C(6,2)=15 laptop denominator (D1-2); C(4,2)=6 both-desktop (D1-2b);
          C(4,2)C(4,2)C(3,1) lineup (D1-3); C(12,2)=66 pens (p3 p014); C(15,5)=3003 lineup denom (D1-3b)
    2.5.6 disjoint-union counting [~]: 1 - P(A) - P(B) (D1-2d: 8/15)
2.6 conditional probability
    2.6.1 definition [p050]: P(A|B)=P(AnB)/P(B), P(B)>0
    2.6.2 meaning [p050]: renormalize the world to the condition
    2.6.3 camera chain [D1-4, p050]: .30/.40=.75 and .30/.60=.50
    2.6.4 conditional inside a continuous model [~] [D1-25]: f=2x on (0,1), P(X<=1/2|1/3<=X<=2/3)=5/12
    2.6.5 conditional on a normal [~] [!] [A1 long 1]: P(60-70 | live to 60) = 0.1544/0.6826 = 0.4863
    2.6.6 conditional on an exponential [~] [!] [A2 B5, errata 9]: (1-e^-0.5)/(1-e^-1) = 0.6225
2.7 event independence
    2.7.1 product definition [p027]
    2.7.2 equivalent form [p028]: P(A|B)=P(A)
    2.7.3 two-draws intuition [p027]: replace = independent, no replacement = dependent
    2.7.4 mutual independence of n events [p028]: every subset, not just the full set
    2.7.5 independence as a modelling assumption [~]: batteries (D1-15), die tosses, binomial trials
    2.7.6 forward pointer: rv-level independence rules live in T6 [H]
```

--------------------------------------------------------------------------------
T3  RANDOM VARIABLES  (deck p051-062 intro, p112-147 continuous)
--------------------------------------------------------------------------------
```
3.1 the definition
    3.1.1 rv = function from S to the reals [p051, p063], notation X(s)
    3.1.2 Bernoulli 0/1 [p052]
    3.1.3 counting rv [p053]: two coins, X = heads
    3.1.4 dice sum [p054-055]: support 2..12, triangular pmf
    3.1.5 two coins full pmf [p056]: 1/4, 2/4, 1/4 + sum-equals-1 check
    3.1.6 geometric rv [p057-059]: N = tosses to first head, (1-p)^(n-1)p; countably infinite
          support; verify via geometric series [C] the same pmf is in the L12-13 deck family
    3.1.7 car lifetime [p060]: continuous teaser
    3.1.8 taxonomy [p061-063, p076]: discrete (finite or listable) vs continuous (fills an interval,
          P(X=c)=0)
3.2 functions of an rv [~]
    3.2.1 Y = X + 4 [D1-29]: hospitalization, E(Y)=8
    3.2.2 h(X)=25X-8.5 [D1-22] price; h(X)=X-.01X^2 capacity
    3.2.3 M = max of two dice [D1-17]: p(m) = (2m-1)/36
    3.2.4 revenue h3, h4 [D1-23]: plateaus; E[h3]=2.4667 vs E[h4]=2.6667
    3.2.5 support identification [~]: write the value set (open/closed, infinite) before any pmf work
    [C]  3.2.6 two dice pmf table + distribution function [E24S4-B5]
    [C]  3.2.7 min of two dice (mirror of max) and difference of dice: NOT asked, same method [S]
3.3 the continuous case, definitions
    3.3.1 why densities [p113-115]: P(exact peak time) = 0
    3.3.2 continuous rv definition [p116, p063]
    3.3.3 pdf conditions [p117]: f>=0; integral = 1; P(a<=X<=b) = area [p118]
    3.3.4 remarks [p119-123]: normalize non-density by k; P=0 does NOT mean impossible [p122];
          zero outside the support [p123]
```

--------------------------------------------------------------------------------
T4  PMF / PDF AND CDF  (deck p063-087, p112-139)  lect 5-6
--------------------------------------------------------------------------------
```
4.1 pmf, discrete
    4.1.1 definition [p064]: p(x) = P(X=x), fully describes the variable
    4.1.2 two conditions [p064]: p(x)>=0 AND sum = 1 (necessary and sufficient)
    4.1.3 find k, arithmetic [~] [D1-14, p070-071]: p(y)=ky, y=1..5, 15k=1, k=1/15;
          P(Y<=3)=.4; P(2<=Y<=4)=.6; is p=y^2/50 valid? no (55/50)
    4.1.4 find k, quadratic [~] [!] [D1-12, p066, A1 long 2]: 9k+10k^2=1, root k=1/10;
          trap: circulated 12k/14k variants do not satisfy it (errata 5)
    4.1.5 pmf built from combinatorics [~]: boards D1-16 (P(1)=6/10 by complement); dice max D1-17;
          batteries D1-15 (p(y)=(y-1)(.1)^(y-2)(.9)^2)
    4.1.6 proportional-form family [~]: p proportional to y style
    4.1.7 graphs [p067-069, p083-084]: line graph, probability histogram, cdf step plot
4.2 cdf, discrete
    4.2.1 definition [p074]: F(x) = P(X<=x)
    4.2.2 properties [p078]: nondecreasing; proof question [D1-18]
    4.2.3 pmf from cdf [p078]: f(n) = F(n) - F(n-1)
    4.2.4 interval via cdf for INTEGER rv [p135]: P(a<=X<=b) = F(b) - F(a-1). the a-1 is the slip
    4.2.5 construction per interval [~]: boards stepped F; dice max steps 0..1
    4.2.6 minimum c with F(c) > 1/2 [~] [!] [D1-12iv, A1 long 2iv]: F(3)=0.5 exactly, strict > fails, c=4
    4.2.7 "at most" reading [p065]
    [C]  4.2.8 pmf table with k, P(X<6), distribution function, min a [E25S4-B1]
4.3 pdf and cdf, continuous
    4.3.1 cdf definition [p130-132]: area to the left
    4.3.2 using F [p133-135]: P(X>a)=1-F(a); P(a<=X<=b)=F(b)-F(a) (NO a-1 here)
    4.3.3 density from cdf [p136-137]: F'(x)=f(x); worked F=(x-1)^4/16 [D1-28];
          exercise pair [D1-27]: (i) 1/3 then 2/3 piecewise, (ii) |x| on (-1,1)
    4.3.4 piecewise pdf integration [~]: bus triangle [D1-26, errata 13] 7 parts; f=2x [D1-24]
          [C]  bus waiting time pdf [deck L89-01] and CDF-to-density interval [deck L89-02, OPEN]
    4.3.5 improper integrals and tails [~] [D1-30]: Pareto E=k th/(k-1) for k>1, V for k>2,
          E(X^n) finite iff n<k
    [C]  4.3.6 pdf ax^2+bx on (0,1) with mean 0.5, find a and b [E24S3-B2] (constraint-solve on a pdf)
    [C]  4.3.7 pdf kx^2(1-x^3) find k, mean, variance [E24S3-D1]
    [C]  4.3.8 pdf f=6x(1-x), find k with P(X<k)=P(X>k), plus CDF [R25S4-C1, also asgn-24-25 #1 Q3]
```

--------------------------------------------------------------------------------
T5  EXPECTATION OF RANDOM VARIABLES  (deck p088-094, p140-147)  lect 7
--------------------------------------------------------------------------------
```
5.1 expectation, discrete
    5.1.1 definition [p088]: E(X) = sum x p(x), the weighted average
    5.1.2 interpretation [p091]: location / center
    5.1.3 die example [p089]: E(X)=3.5
    5.1.4 function of an rv [p090]: E[h(X)] = sum h(x)p(x), finite absolute sum required
    5.1.5 the p094 question [D1-21] [!]: X on {-3,6,9}: E(X)=11/2, E(X^2)=93/2, E(2X+1)^2=209
          [C] same item appears as ETE-S3 2025-26 B3 and ETE Summer Q15 (twice in real papers)
    5.1.6 revenue tables [D1-23]
    5.1.7 freezer chain [D1-22]: six pieces, E=16.38, V=3.9936, E(25X-8.5)=401, V=2496, E(X-.01X^2)=13.66
5.2 properties of the mean
    5.2.1 E(c)=c [p092]
    5.2.2 E(cX)=cE(X) [p092]
    5.2.3 E(aX+b)=aE(X)+b, proof exercise [D1-20, p093]
    5.2.4 linearity ALWAYS true: E(X+Y)=E(X)+E(Y), no independence needed (sheet line 94) [~][H]
    5.2.5 [C] E[2X+3] with E[X]=5 [E25S3-A1]
5.3 expectation, continuous
    5.3.1 definition [p140-141]: integral form
    5.3.2 E[h(X)] [p143]
    5.3.3 linear case [p144]
    5.3.4 convergence conditions [D1-30]
    5.3.5 shifted rv [D1-29]
    5.3.6 expected count over N repeats [H][!][C]: E = N x P
          p3 p018: 10000 x (3/8)^10 = 0.5499 (errata 2); A2 B4: 274/576/4487;
          A2 D1: 7888 bulbs; [C] R25S4-B1 heights over 6 ft expected count;
          [C] E25SUM-Q13 800 families 4 children binomial counts
```

--------------------------------------------------------------------------------
T6  VARIANCE + INDEPENDENT RANDOM VARIABLES  (deck p095-111)  lect 8-9
--------------------------------------------------------------------------------
```
6.1 variance machinery
    6.1.1 definition [p097]: Var(X)=E[(X-mu)^2], sd = sqrt
    6.1.2 remarks [p098-099, p106]: non-negative; spread interpretation
    6.1.3 shortcut [p101-103]: Var = E(X^2) - [E(X)]^2, proved
    6.1.4 Var(c)=0 [p103]
    6.1.5 Var(cX)=c^2 Var(X) [p103]
    6.1.6 V(aX+b)=a^2 V(X), sd = |a| sd(X) [p104-105]
    6.1.7 unit-change story [p104-105]
    6.1.8 Var from a pdf [~] [p144-145]: two integrals or the shortcut
    6.1.9 numeric chains [D1-22, A1 app 3: var 0.9475, sd 0.9734, errata 12]
    [C]  6.1.10 variance non-negative as a concept item [E25SUM-Q8]
6.2 INDEPENDENT RANDOM VARIABLES, the hidden block [H][!]
    6.2.1 E(XY) = E(X)E(Y) under independence. NO slide. Sheet section C
          [C] CONFIRMED as a real ask: R25S3-A1 independence E[XY]=E[X]E[Y]
    6.2.2 Var(X+Y) = Var(X) + Var(Y). NO slide. Sheet section D
    6.2.3 Var(X-Y) = Var(X) + Var(Y) (coefficient squares)
    6.2.4 downstream need: Var(sum of dice)=35/6 (A1 short 5); Var(Xbar)=sigma^2/n (every CLT);
          estimator variances (p5 p018, p021 with -4 squaring to +16); Poisson additivity (A2 A12)
    6.2.5 the T4 trap: small variance does not win if biased (mock B4)
6.3 canonical drill: variance of a sum of dice [~]
    6.3.1 Var(one die) = 91/6 - 3.5^2 = 35/12
    6.3.2 Var(sum) = 35/6 = 5.8333 by the independence rule
    6.3.3 used in A1 short 5 for k and the 35/54 bound
```

--------------------------------------------------------------------------------
T7  CHEBYSHEV'S INEQUALITY  (S&P L10-11 deck, arrived 15 Sep)  lect 10-11
--------------------------------------------------------------------------------
```
7.1 statement and both forms
    7.1.1 tail form: P(|X-mu| >= k sigma) <= 1/k^2
    7.1.2 complement form: P(|X-mu| < k sigma) >= 1 - 1/k^2
    7.1.3 relation: complements; pick the one matching the ask
    7.1.4 canonical values: k=2 -> 3/4 (1/4 tail); k=3 -> 8/9 (1/9); k=4 -> 15/16 (1/16)
7.2 distribution-free property
    7.2.1 any distribution with finite mean and variance (A1 MCQ 10)
    7.2.2 a moment bound, so shape-free
    [C]  7.2.3 purpose statement: what Chebyshev is FOR [E25S4-A3]
7.3 k extraction from an interval
    7.3.1 convert to |X-mu| < c, then k = c/sigma
    7.3.2 worked: 60-80 around 70, sigma 5, k=2, bound 3/4 (A1 app 4)
    7.3.3 [C] k=3 percentage within 3 sigma [E24S3-A2]; [C] mu=10 var=4, P(5<X<15) and
          P(|X-10|>=3) [E25S3-B1]
7.4 tail vs complement fork (the classic trap)
    7.4.1 "outside"/"at least c away" -> tail -> 1/k^2
    7.4.2 "between"/"within c" -> complement -> 1 - 1/k^2
    7.4.3 the 1/9 vs 8/9 trap (mock B1); also errata 15: the deck's Q3 slide states one row and
          works another (read Q1 and Q2 only)
7.5 application to a sum of rvs [~]
    7.5.1 find Var(sum) first (dice 35/6)
    7.5.2 sigma_sum, then k = c/sigma_sum
    7.5.3 dice question [A1 short 5]: bound 35/54 = 0.6481 vs actual 1/3, compare (loose bound)
7.6 lower bound for a counts interval [~]
    7.6.1 600 throws: mu=100, Var=83.333, sigma=9.129
    7.6.2 k = 20/9.129 = 2.191
    7.6.3 bound 19/24 = 0.7917 (A1 short 6)
7.7 proportion phrasing in reverse [~]: "minimum proportion scoring 60-80" = complement form (A1 app 4)
7.8 applicability statements [A1 MCQ 5, MCQ 10]
7.9 inverse from a stated bound: find the constant C [MTE 2025-26 Q5, deck Q2(iv): mu=10, var=4,
    bound 0.04 -> C=10]; [C] E25S3 variant and re-sess
7.10 sources: deck, sheet E, bank 6, mock B1. Graded 9+ uses across assignment 1, both MTE papers,
    ETE S3/S4 both years, 2025-26 assignment Q5.
```

--------------------------------------------------------------------------------
T8  BINOMIAL DISTRIBUTION  (p3 p001-018)  lect 12
--------------------------------------------------------------------------------
```
8.1 derivation story [p002-007]: 5-coin P(exactly 3 heads) = 10 x (1/2)^5 = 31.25%; why 10 = C(5,3)
8.2 setup conditions [p008, p011]: two outcomes; n finite; trials independent; p constant
8.3 the pmf [p009-010]: C(n,x) p^x q^(n-x); X~B(n,p)
8.4 mean and variance [p012]: E=np, Var=npq (A2 A2: 2.5)
    [C]  8.4.1 mean np [E25SUM-Q3]; [C] binomial(180,1/3) mean and variance [E25S3-A3];
         [C] binomial mean n=50 p=0.4 [E24S3-A1]; [C] max successes is n [A2 A9]
8.5 complement tails: the pens question [p013-016] [!]
    8.5.1 X~B(12,0.1); P(X=2)=0.2301; P(X>=2)=0.341; P(X=0)=0.2824
    [C]  same pens item re-asked as E25S3-B2 and in deck L12-13; the 12-pen version is still OPEN
         for a book source (circulating on askfilo/StudyX/Chegg)
8.6 parameter recovery from a ratio [p017-018]: P(X=5)=2P(X=4) -> 3p=5q -> p=5/8;
    then E = 10000 x (3/8)^10 = 0.5499 (errata 2)
8.7 framing identification [~]: physical die -> success = even number
8.8 Poisson limit conditions [p022]: n->inf, p->0, np finite
8.9 MCQ surface: var npq; max successes
    [C]  8.10 moment matching: 5 trials with mean + variance = 9/5, find pmf [E24S3-B4]
    [C]  8.11 two-sided interval P(a<=X<=b): sibling, pens 2..4 = 0.3367, NOT yet asked
    [C]  8.12 bombs 1/5, six dropped, at least two and exactly two [E24S3-B3]
    [C]  8.13 literate 20%, investigators reporting 3 or less [R25S4-B2]
```

--------------------------------------------------------------------------------
T9  POISSON DISTRIBUTION  (p3 p019-028)  lect 13
--------------------------------------------------------------------------------
```
9.1 when to use [p020-021]: count of rare events in a fixed interval; seven-instance list
9.2 pmf and signature [p023-024]: e^-l l^x/x!; mean = var = lambda
    [C]  9.2.1 "which distribution has mean equal to variance" = Poisson [R25S4-A2]
9.3 lambda recovery from a ratio [p025]: P(1)=0.2P(2) -> lambda=10; then P(0)=e^-10
    [C]  same Poisson-ratio family in deck L12-13 (P1 = 0.2 P2, OPEN for a book source)
9.4 rate and window scaling [~] [p026, A2 D2]: 2/min, 15/hr, 4/hr, 5/day, 2.5/day; convert the
    window first; worked 4/hr wait>30min = e^-2 = 0.1353
    [C]  shelf lives / calls with exactly two in each of five minutes [deck L1213-05]
9.5 the zero case [p025, A2 D3]: P(0)=e^-lambda; 200 jobs 1% -> lambda=2 -> e^-2
    [C]  9.5.1 defective bottles 0.1%, 500 per box, 100 boxes [E25SUM-Q17]
9.6 tail sums [A2 C3]: P(X>2) with lambda=5 = 0.8753 (errata 14: key 0.8754)
9.7 capacity overflow [A2 B1]: 3 technicians, mean 2.5, "rejected" = P(X>=4) = 0.2424
9.8 THE NESTING [p026]: 2 calls/min, P(exactly 2 in EACH of 5 minutes) = (2e^-2)^5 = 32e^-10 = 0.00145
9.9 Poisson as binomial approximation [~] [p027, A2 D3]: 5000 x 0.001 -> lambda=5, P(4)=0.1755
    (errata 1: prints 0.1745)
9.10 additivity of independent Poissons [A2 A12, sheet line 182]
```

--------------------------------------------------------------------------------
T10  UNIFORM DISTRIBUTION (CONTINUOUS)  (p4 p001-006)  lect 14
--------------------------------------------------------------------------------
```
10.1 density and moments: f=1/(b-a); mean (a+b)/2; var (b-a)^2/12 (A2 A4 asks the formula)
     [C]  10.1.1 uniform from 2 to 6 [deck L1415-01, McClave slide source]
     [C]  10.1.2 uniform mean (a+b)/2 as a concept MCQ [E25S4-A6]
10.2 length-ratio shortcut [~]: P(X<5) on (2,6) = 0.5; P(X>16) on (10,20) = 0.4 (A2 B2)
10.3 clipping to support [~] [A2 A10]: (b-c)/(b-a)
10.4 absolute values to intervals [~] [A2 B8]: P(|X|<2)=2/3; P(|X-2|<2)=1/2; P(X>K)=1/3 -> K=1
10.5 rounding error [A2 C4]: err on (-0.5,0.5), P(|err|>0.2) = 0.6
10.6 two uniforms combined [D1-26 cross ref]: triangular total on (0,10)
```

--------------------------------------------------------------------------------
T11  NORMAL DISTRIBUTION  (p4 p007-037)  lect 15
--------------------------------------------------------------------------------
```
11.1 density and shape: f(x); X~N(mu, sigma^2) (second slot is VARIANCE, errata 7);
     symmetric; mean=median=mode; many normals [p008-012]
     [C]  11.1.1 N(0,1) properties as a concept item [E25S4-A4]; [C] mean and variance of
          standard normal [E25S3-A5, E24S4-A5]
11.2 standardization [p019, p028]: Z = (X-mu)/sigma
11.3 THE TWO TABLE CONVENTIONS [H]: cumulative F(z) [p022, appendix, F(0.12)=0.5478] vs
     area-from-zero phi(z) [p023-025, assignments give phi(1.04)=0.35]; conversion
     phi = F - 0.5; identify BEFORE substituting
11.4 left tail: P(Z<-2) = 0.0228 [p026-027]
11.5 upper tail: P(X>8.6) = 0.4522 [p032-033]
     [C]  N(8,5) probability above 8.6 [deck L1415-05]
11.6 interval: mu 50 sigma 10, P(45<X<62) = 0.5764 [A2 B3]
     [C]  normal N(8,5) below 8.6 [deck L1415-04]
11.7 inverse: z then X = mu + z sigma; 20% lower tail -> 3.80 [p034-037]
     [C]  N(8,5) lower-20% cutoff [deck L1415-06]
11.8 landmarks 68.27/95.45/99.73 [H] [A2 A11]
11.9 two-unknown system from two percentiles [H] [A2 C2, errata 10]: sigma 28.23 -> 28.2,
     mu 37.18 -> 37.2 (key prints 37.5); re-exam cutoff 30.4
     [C]  11.9.1 one-unknown sibling (mu from one percentile, sigma given): HIGH priority, not asked
     [C]  11.9.2 normal, 2000 students over 60 [E24S3-D1b]; [C] 10000 lamps normal life, first
          800 hours and 800-1200 [E25S4-C1]; [C] normal 31% under 45, 8% over 64 find mean+sd
          [E24S4-B4, also asgn-24-25 #2 Q17]
11.10 expected count N x P [~]: batteries 274/576/4487; bulbs 7888
11.11 errata 8: p030 figure prints sigma=10 under mu=8; real sigma 5.0
     [C]  11.12 [E25SUM-Q10] sampling distribution approaches normal
```

--------------------------------------------------------------------------------
T12  EXPONENTIAL DISTRIBUTION  (p4 p038-043)  lect 16
--------------------------------------------------------------------------------
```
12.1 density family: f = lambda e^-lambda t; F = 1 - e^-lambda t; survival e^-lambda t;
     mean 1/lambda; var 1/lambda^2 [p041]; errata 4: p040 inverts the lambda wording
     [C]  12.1.1 exponential pdf identification [E24S4-A4]; [C] exponential use / waiting time
          [E25S4-A5]
12.2 modelling [p039]: time between arrivals
12.3 memoryless property [H][!]: P(T>s+t | T>s) = P(T>t) [A2 MCQ Q5, A2 C1: e^-1 = 0.3679]
12.4 conditionals with cdf ratios [A2 B5, errata 9]: P(X<1|X<2) = 0.6225
12.5 mean to lambda both directions [~]: mean 2 -> lambda 0.5; lambda 0.5 -> mean 2
12.6 unit conversion in the story [A2 D2]: 30 min vs a rate in hours
12.7 repair time [A2 B7]: P(T>2)=e^-1; P(T>11|T>8)=e^-1.5 by memoryless
12.8 slide example [p042-043]: 15/hr, gap under 3 min = 0.05 hr, P = 1 - e^-0.75
     [C]  12.8.1 exponential 15/hr under three minutes [deck L1415-07, McClave slide source]
     [C]  12.8.2 independent exponential shelf lives, joint probability [R25S3-B1];
          [C] repair time exponential lambda=1/3 [E24S4-C1b]
```

--------------------------------------------------------------------------------
T13  SAMPLING AND STANDARD ERROR  (clt p001-005)  lect 17
--------------------------------------------------------------------------------
```
13.1 population and sample [p002]: parameters mu, sigma vs statistics xbar, s; why sampling
13.2 simple random sampling [p003]: without replacement, every subset equally likely
13.3 standard error [p004]: SE = sigma/sqrt(n), the sd of the sample mean
     [C]  13.3.1 CLT standard error, var 400 n=100 [E24S3-A5]; [C] sample size up -> SE down
          [R25S3-A3]
13.4 scaling law [p005]: quadruple n -> halve SE (lightbulbs 100: 25->20, 100->10)
13.5 sampling distribution of the mean as a topic: population 2,4,6,8 sample mean unbiased
     [C] [E25S3-B5]
```

--------------------------------------------------------------------------------
T14  CENTRAL LIMIT THEOREM  (clt p006-018)  lect 18
--------------------------------------------------------------------------------
```
14.1 statement [p007-008]: normal population any n; n>=30 is the course heuristic, not a
     universal cutoff; for non-normal populations check skew, tails, and assumptions
     [C]  14.1.1 CLT applicability concept item [E25SUM-Q9]
14.2 distribution of the mean: mean mu, sd sigma/sqrt(n)
14.3 z transform with SE denominator [~]: z = (xbar-mu)/(sigma/sqrt(n)); "average of n" template
     vs plain normal (only the denominator differs: the classic mix-up)
14.4 worked: ATM [p011-012]; impurity [p013-014, errata 6: z=-0.94 typo -0.4,
     rounded table 0.1645, unrounded about 0.1637];
     LED [p015-016]; machines n=9 exact-normal fallback [p017-018]
14.5 exact table selections in the deck: 0.4909, 0.3264, 0.4641, 0.2257, 0.4772
```

--------------------------------------------------------------------------------
T15  THEORY OF ESTIMATION, INTRODUCTION  (p5 p001-007, lt p001-015)  lect 19
--------------------------------------------------------------------------------
```
15.1 vocabulary [p003, p005]: population parameter; statistic (xbar, S^2, p-hat); estimator (the
     RULE, a random variable) vs estimate (the NUMBER); sample space vs parameter space
     [C]  15.1.1 random variable definition as an MCQ [E25S4-A1, E25SUM-Q1]; [C] discrete rv
          definition [R25S4-A1]; [C] condition for unbiasedness [E25S3-A2]; [C] unbiased estimator
          definition [E24S3-A3, E24S4-A1]; [C] consistency definition [R25S4-A3]
15.2 point vs interval [p004]: interval estimate = point +/- margin
15.3 point estimation worked [p022]: 1640/8 = 205 ms
15.4 proportion estimation [p023]: p-hat = 465/500 = 0.93
15.5 CI shape [p024] [-]: 8.4 +/- 1.96(1.5/sqrt25) = (7.81, 8.99); uses lecture 25 machinery,
     kept because "point and interval estimation" is named in the MTE list
     [C]  15.5.1 what a confidence interval provides [E25SUM-Q2, BOUNDARY]; [C] 95% CI, 81 families
          [E25S3-C1a, BOUNDARY]; [C] 95% CI t-table leaf weights [E25S4-B5]; [C] 95% CI accidents
          per crossing [R25S4-B4]
15.6 lt p031-039: full CI block, OUT of MTE, not counted
```

--------------------------------------------------------------------------------
T16  CHARACTERISTICS OF A GOOD ESTIMATOR  (p5 p008-021, lt p016-030)  lect 20-21
--------------------------------------------------------------------------------
```
16.1 unbiasedness [p009]: E(theta-hat) = theta; bias = E - theta
     [C]  16.1.1 T1, T2 unbiased, efficiency comparison [E25S4-B3]
16.2 force unbiasedness with a constant [p016, p020]: coefficient sum = divisor (lambda=0, lambda=1)
16.3 consistency [p010-011]: convergence in probability; two sufficient conditions E(Tn)->theta
     AND Var(Tn)->0; why xbar is consistent [p012]
     [C]  16.3.1 consistency of Tn, bias and variance to 0 [R25S3-A2]
16.4 efficiency [p013-014]: smallest variance among unbiased
16.5 comparison set 1 [p015-018]: t1 Var sigma^2/5; t2 BIASED (E=2mu) eliminated; t3 after lambda=0
     Var 5sigma^2/9; best t1
16.6 comparison set 2 [p019-021]: T1 Var 3 sigma^2; T2 Var 29 sigma^2; T3 after lambda=1 Var
     sigma^2/3; best T3. THE PROTOCOL: filter unbiased FIRST, then min variance
16.7 sufficiency [lt p024-025]: Neyman-Fisher factorization; Poisson worked (T=sum sufficient);
     exponential worked (xbar sufficient)
     [C]  16.7.1 sufficiency MCQ [MTE 2025-26 Q3]; [C] sample mean sufficient for Poisson lambda
          [E25S4-B2]; [C] sufficient estimators, exponential population [E24S4-B2]
```

================================================================================
3. THE HIDDEN LAYER (no teaching slide; learn from the formula sheet)
================================================================================

```
[H1] independence rules of rvs: E(XY)=E(X)E(Y), Var(X+Y)=Var(X)+Var(Y), Var(X-Y)=+
     feeds: Chebyshev sums, CLT variances, estimator variances, Poisson additivity
     graded: A1 short 5; CONFIRMED as a direct ask by R25S3-A1
[H2] Chebyshev entire topic: 9+ graded uses. Sources: S&P L10-11 deck, sheet E, bank 6, mock B1
     (this one LEFT the hidden class on 15 Sep when the deck arrived; still top priority)
[H3] memoryless property: 2 graded uses (A2 MCQ Q5, A2 C1). Sheet only
[H4] landmarks 68.27 / 95.45 / 99.73: 1 graded use (A2 A11). Sheet only
[H5] expected count N x P: graded (A2 B4, A2 D1, R25S4-B1, E25SUM-Q13) + slide usage. No slide rule
[H6] geometric E(N) = 1/p: graded (A1 short 4). pmf taught, E not
[H7] hypergeometric mean nK/N: graded (A1 long 3, exactly 0.8 both cases). No slide
[H8] two-table discipline (phi vs F): every normal/CLT numeric. Slides show both tables, never warn
```

================================================================================
4. THE DISTRIBUTION SHELF: THE 9-SLOT TARGET MATRIX
================================================================================

Every distribution in the syllabus is asked through the same nine target slots. This is the
single most useful shape for drilling.

```
  slot           what it asks                            binomial  Poisson  uniform  normal  exp
  1 point        P(X=k)                                     [X]      [X]      [X]      [X]    [X]
  2 tail         P(X>k) / P(X>=k) / complement             [X]      [X]      [X]      [X]    [X]
  3 interval     P(a<=X<=b) or P(a<X<b)                    [S]      [S]      [X]      [X]    [X]
  4 moments      E, Var (and E(X^2))                       [X]      [X]      [X]      [X]    [X]
  5 params       recover a parameter from a probability    [X]      [X]      [S]      [X]    [S]
  6 inverse      recover a quantile / cutoff               [S]      [S]      [X]      [X]    [S]
  7 count        N x P expected count over repeats         [X]      [X]      [ ]      [X]    [ ]
  8 conditional  P(A|B) inside the model                   [S]      [ ]      [ ]      [X]    [X]
  9 compose      nest two models / chain an output         [S]      [X]      [S]      [X]    [X]
  [X] asked, [S] sibling one mutation away, [ ] no evidence either way
```

================================================================================
5. CROSS-CUTTING MICRO SKILLS (12 drills, these carry the marks)
================================================================================

```
S1   complement turn: at least / none / more than / rejected -> 1 minus lower tail
S2   table discipline: identify convention (phi vs F), pick the row, mind the sign
S3   exact powers: 0.9^10, 0.9^12, e^-2.5 by hand
S4   ratio recovery: equate two pmf expressions, cancel, solve
S5   N x P expected counts
S6   piecewise integration with correct limits, no double counting at breakpoints
S7   |expr| < c <=> interval; and interval length over support length
S8   pmf sanity: sums to 1, admissible k
S9   cdf sanity: nondecreasing, limits 0 and 1, jumps at atoms
S10  rounding discipline: exact until the final line (errata 3, 12)
S11  read the ask: at most / at least / between / inclusive / neither / exactly
S12  draw the curve, mark the area, before computing
```

================================================================================
6. THE MUTATION SYSTEM (M0-M4) AND THE MUTATIONS SEEN IN OUR OWN CORPUS
================================================================================

Three names for one idea: problem isomorphs (Simon/Newell) = item models with RADICALS vs
INCIDENTALS (Gierl and Lai, AIG) = variation theory (Marton). The mapping:
```
  INTENT (what the setter wants)  =  RADICALS  =  deep structure  = the SOLVE PATH
  values, names, story, units     =  INCIDENTALS = surface structure
```
Three levels of "question":
```
  L-INSTANCE  "10% pens, box of 12, find P(X=2)"
  L-MODEL     "<p> defective, batch <n>, find P(X=<k>)"  fixed formula+steps, slots = p, n, k, story
  L-TYPE      template class sharing a solve path: "binomial point probability"
  L-FAMILY    types grouped under one method: "binomial block"
```
The rule:
```
  INCIDENTAL mutation -> SAME TYPE. a new practice instance, NOT a new tree node.
  RADICAL mutation    -> NEW TYPE NODE. it slots into the tree as a sub / sub-sub topic.
```

## 6.1 The five mutation operators
```
  M0  RE-SKIN       numbers, names, units, story swapped. TYPE UNCHANGED.
                    pens -> sensors -> bulbs; 4 red 6 blue -> 5 red 5 blue;
                    mean 70 var 25 -> mean 50 var 16
  M1  INVERT        which quantity is GIVEN vs ASKED swaps. solve order flips. NEW NODE.
                    x -> P  vs  P -> x (inverse); normalize-first vs given-k;
                    distribution -> moments  vs  moments -> parameters (moment matching)
  M2  RE-CONDITION  a structural condition changes: independence on/off, replacement,
                    sigma known/unknown, n small/large, discrete/continuous, equal/unequal p.
                    NEW NODE when the needed formula changes.
                    with replacement vs hypergeometric; n=25 CLT vs n=9 normal population
  M3  RE-TARGET     same setup, different target functional: P(X=k) -> P(X<=k) -> P(X>k) ->
                    E(X) -> Var(X) -> E[h(X)] -> conditional -> expected-count-over-N.
                    NEW NODE when the method differs.
  M4  COMPOSE       nest two models or chain one output into another. ALWAYS a NEW NODE.
                    Poisson per-minute then binomial over minutes; estimator compare then
                    consistency then efficiency; expected value then a decision
```

## 6.2 Does a change make a new type (the rule table)
```
  change                                     new type?   why
  numbers only                                  NO       incidental
  names / story / units                         NO       incidental
  rounding of given data                        NO       incidental
  which value is asked of the SAME formula      NO       same substitution
  forward <-> inverse (x <-> P)                YES       M1, solve order flips
  point -> tail or interval                    YES       M3, complement or F(b)-F(a)
  unconditional -> conditional                 YES       M3, ratio step
  single -> expected count over N              YES       M3, N x P step
  independence assumed -> not                  YES       M2, rule set changes
  replacement -> no replacement                YES       M2, distribution changes
  n small -> n large (same test)             MAYBE       only if the applied distribution changes
  one model -> two nested models               YES       M4 composition
  target E <-> Var <-> E[h(X)]                 YES       M3, moment order
  efficiency <-> MSE comparison                YES       M3, criterion changes
```

## 6.3 The mutations ACTUALLY USED in our questions (the value-delta log)
```
  skeleton                            source value          our mutated values
  telephone exponential (S05/S15)     mean 5 (G&K ch5 ex10)  6 (asgn-24-25 #2 Q20), 4 (MTE 24-25 B2),
                                                             3 (MTE 25-26 Q6)
  uniform Chebyshev interval (S06)    (-1,3) (G&K ex15b)     (-1,1) (MTE 24-25 B3)
  trains / subway (S07)               30-min subway (G&K)    15-min, 4 AM, 9:00-9:30 (MTE 24-25 B4)
  Chebyshev inverse (S26/S27)         sigma 2, 21/25 (G&K)   sigma 3, 24/25 (ETE S4 24-25 B3)
  machine life (S16)                  "bread-making machine" "a machine" (MTE 25-26 Q7)
  density kx^3(4-x)^2 (S13/M25-Q4)    ABES sample: asks SD   our paper asks VARIANCE
  pens defective, box of 12 (S28)     G&K family (18 units)  12 pens, 3 parts (deck + ETE, OPEN source)
  Poisson Y=2X Var (M24-B1)           G&K (answer 14)        VERBATIM
  t^2 biased (M25-Q8 ii)              G&K estimation ex6     VERBATIM
  binomial ratio p=5/8 (8.6)          deck p017              re-asked in papers by re-skin
```
That is the whole mutation pattern the setters use on this course: take a book skeleton, swap
one or two incidentals, sometimes flip the target (M3), rarely nest (M4).

================================================================================
7. NEW TYPE NODES THE RADICAL ANALYSIS GENERATES (not listed in the syllabus)
================================================================================

These come from M1/M2/M3/M4 mutation of corpus models. Every number was computed on the machine.

```
  7.a  DESIGN / MIN-SIZE INVERSION (M1 under binomial, CLT, Chebyshev)
       "how many/few trials to guarantee or achieve X"
       binomial: smallest n with P(X>=1)>=0.9, p=0.1 -> n=22 (n=21 gives 0.8906)
       CI:       smallest n with margin<=0.5, z=1.96, sigma=1.5 -> n=35
       Chebyshev: smallest k for a stated lower bound (19/24 already in corpus)
       risk: HIGH. three sites, one method.
  7.b  PARAMETER RECOVERY, GENERAL FAMILY (M1 across ALL distributions)
       binomial P(X=5)=2P(X=4) -> p=5/8                     [asked]
       Poisson  P(X=1)=0.2P(X=2) -> lambda=10                [asked]
       Poisson  P(X=0)=0.1 -> lambda=ln10=2.3026              [adjacency]
       exponential P(T>2)=0.5 -> lambda=ln2/2=0.3466          [adjacency]
       normal   P(X<100)=0.90, sigma=10 -> mu=87.18           [adjacency, HIGH]
       uniform  P(X>4)=1/3 on (1,b) -> b=5.5                  [adjacency]
       moment matching: E and Var -> params (binomial n,p; normal; uniform a,b)
       [C] confirmed as real asks in our papers: binomial mean+var (E24S3-B4),
           pdf with a mean constraint (E24S3-B2 ax^2+bx mean 0.5)
       risk: HIGH. one method, five chapters.
  7.c  DERIVED-VARIABLE ALGEBRA (M2/M4 around rvs)
       corpus: sum of dice, M=max, Y=X+4, h(X)=X-.01X^2, T2=2X1+3X3-4X2
       adjacency: min of two dice, difference of dice, sum of Poissons [asked: A2 A12],
       sum of binomials with the same p is binomial again (verified to 1e-12)
  7.d  CONDITIONAL ON AN INEQUALITY, DISCRETE (M3)
       P(X=k | X>=j) for binomial/Poisson: pens P(X=2|X>=1) = 0.2301/0.7176 = 0.3207
       corpus has conditionals only for continuous, normal, exponential.
       [C] confirmed as a real ask: P(X<1|X<2) exponential [A2 B5, E24S4-C1b]
  7.e  DECISION / OPTIMIZATION STORY (M4, target is a choice)
       "which option is better" with expectation behind it: magazine order 3 vs 4,
       technician capacity overflow, estimator choice. 3 corpus instances already.
  7.f  APPROXIMATION-CHOICE (M2 around the Poisson limit)
       corpus: Poisson approximation to binomial [asked]; adjacency: binomial -> normal
       (B(100,0.4), P(X<=45) with continuity correction, z=1.123). "which distribution
       models this" and "is the approximation valid" are the named decisions.
  7.g  MSE / BIAS-VARIANCE COMPARISON (M3/M4 in estimation)
       efficiency vs MSE = Var + Bias^2. instance: T4 biased, MSE=25.75 vs Var(T3)=0.3333.
       sheet carries MSE; the QUESTION form ("which has smaller MSE") is the new node.
  7.h  SHEET GAP CHECK (found by this analysis)
       geometric E=1/p and Var=(1-p)/p^2 are needed but NOT on the sheet [H6]
       hypergeometric mean nK/N needed but NOT on the sheet [H7]
       both already graded once. ADD to the sheet.
```

================================================================================
8. TYPE SPACE: WHAT IS ASKED vs THE SIBLING ONE MUTATION AWAY
================================================================================

`[X]` asked in corpus | `[S]` sibling, one mutation away, NOT asked | `[C]` covered by our docs

## 8.1 foundations, rvs, pmf/cdf
```
  [X] equally likely single draw; complement; conditional forward; at-least-one via complement;
      counting inside probability; set ops on coded outcomes; independence product (event level)
  [S] P(neither A nor B) = 1 - P(AuB); independence CHECK from given probabilities (classic MCQ);
      conditional from a 2x2 count table
  [F] permutations: never used in any question (grep-verified)
  [X] classify rv; pmf from enumeration; support identification; transformed rv
  [S] min of two dice; difference of dice; "give the support" as a standalone MCQ
  [X] find k linear; find k quadratic; pmf->cdf; cdf->pmf; pdf verify; cdf from pdf; pdf from cdf;
      interval via cdf; nondecreasing proof
  [S] integer interval F(b)-F(a-1) (taught, NOT asked); "is this a valid cdf"; pmf/cdf of Y=2X+1
```

## 8.2 expectation, independence, Chebyshev
```
  [X] E(X), E(X^2), E(aX+b) proof, E[h(X)], E from pdf, E of shifted rv
  [S] E(X) from the cdf alone; E(|X|) or capped payoffs
  [X] Var(sum of dice) used; Var(X-2Y) independent Poisson [MTE 24-25 QB1];
      E(XY) independence [R25S3-A1, CONFIRMED]
  [S] Var(aX+bY) standalone; independence check via joint vs product pmf
  [X] Chebyshev between-form, tail-form, counts interval, applicability x2, reverse find-c
  [S] one-sided Chebyshev sigma^2/(sigma^2+c^2); compare-bound-to-actual [covered]
```

## 8.3 the distribution shelf, siblings
```
  binomial:   [S] two-sided interval pens 2..4 = 0.3367 (HIGH); min-n design n=22;
                  conditional P(X=2|X>=1)=0.3207; mode floor((n+1)p)=1
  geometric:  [S] Var=(1-p)/p^2 = 2 for p=.5; tail P(N<=k)=1-(1-p)^k (0.875 for p=.5,k=3)
  hypergeom:  [S] full pmf (0.383, .451, .150, .016, .0004)
  Poisson:    [S] standalone window scaling; between-values P(1<=X<=3)
  uniform:    [S] mean/variance from a,b standalone; [X] clipping, abs-intervals, inverse K
  normal:     [S] mu recovery from one percentile (HIGH); sigma recovery; landmark arithmetic
  exponential:[X] interval [MTE 24-25 QB2, P(7<T<12) at 1/4 = 0.123987];
              [S] E(T)/Var(T) standalone; min of two exponentials (rate doubles, e^-1=0.3679)
  CLT:        [S] CLT for the SUM not the mean (sd = sqrt(n) sigma); CLT concept MCQ;
              [S] SE design n=35; [F] finite population correction
  estimation: [X] vocabulary, point estimate, p-hat, CI, unbiasedness, lambda-forcing,
              consistency, efficiency, sufficiency, protocol
              [S] MSE comparison; relative efficiency ratio (5/9)/(1/5)=25/9=2.7778
```

## 8.4 risk-ranked sibling list (drill these)
```
  1  normal one-unknown recovery (easy version of A2 C2)                HIGH
  2  binomial two-sided interval (pens 2..4 = 0.3367)                   HIGH
  3  CLT for a sum (sqrt(n) sigma)                                      MED-HIGH
  4  discrete conditional P(X=k | X>=j)                                 MED-HIGH
  5  min-n design (binomial n=22, CLT n=35)                             HIGH
  6  geometric Var / tail                                               MED
  7  independence check question                                        MED
  8  MSE comparison                                                     MED
  9  Poisson between-values probability                                 MED
 10  valid-cdf check                                                    LOW-MED
```

================================================================================
9. WHAT THE LATE EVIDENCE ADDS (folded in above, listed here so nothing hides)
================================================================================

The 15 Sep atlas was built from batch 1 + U01 only. Since then three evidence sets landed and
their topic-bearing content is now in the tree (marked [C]):

```
  ETE intake, 7 papers, 97 blocks (reports/17-ETE-INTAKE.md)
      IN 56, BOUNDARY 3, PARTIAL 3, OUT 35
      topic-bearing: rv/rv-type definitions x3, Chebyshev x4 forms, binomial x5 shapes,
      Poisson x3, normal x4 (incl 10000 lamps two-window, 31/45 inverse), exponential x2,
      sampling/SE x2, CLT x1, estimation definitions x5, CI x4 (boundary), sufficiency x2
  the four S&P decks, 30 blocks (reports/evidence/deck-block-ledger-20260916.csv)
      L1-7 (13 Devore items), L8-9 (4: bus pdf, CDF-to-density, hospitalization E(Y), Pareto),
      L12-13 (6: 5-coin, pens, irregular die, Poisson ex1-3), L14-15 (7 McClave: uniform 2-6,
      two standard-normal, two N(8,5), inverse 20% cutoff, exponential 15/hr)
  the 2025-26 assignment bundle, 119 items (PR 14 ledger)
      text-extracted, one row per occurrence; categories: 16 concept, 14 analytical,
      13 application, 12 memory, 64 uncategorised; 2024-match column not yet assessed
```

Also confirmed: the SAME skeletons repeat across years and across instruments. The pens
binomial, the Chebyshev inverse pair, the subway uniform, the E(X)/E(X^2)/E((2X+1)^2) table,
and the telephone exponential each appear in two or more of deck, assignment, MTE, ETE. That
repetition is itself the strongest evidence for the M0/M1 mutation model above.

================================================================================
10. ERRATA AND TRAPS TO CARRY
================================================================================

Errata 1-15 (full text in reports/09-ERRATA.md): slide/key arithmetic slips (insurance 0.1755,
die sets 0.5499, sd chain 0.9734, binomial normalisation 1/10, clt Z -0.94, normal figure
sigma 5.0, A2 C2 mu 37.2, A2 C3 0.8753, exponential 0.6225, A2 B5, Chebyshev deck Q3 row).
Errata 19-21 (added in the U01 review): MTE 2024-25 QA2 CDF key marks B, integration gives D;
MTE 2025-26 scheme Q4 prints infinite bounds but works 0 to 4; MTE 2025-26 Q8(ii) drops
theta^2 from the inference.

Trap list for the exam (10 items, from the learn plan):
```
  1 Chebyshev tail vs complement (1/9 not 8/9)
  2 which normal table (phi is area-from-0, not cumulative)
  3 exponential: lambda is rate, 1/lambda is mean time
  4 complement discipline: at least, none, rejected, more than
  5 ratio recovery: cancel, solve, check q = 1-p
  6 rounding: exact until the end
  7 N x P, never forget the multiply
  8 independence: only E(XY) and Var(sum) need it, E(sum) never does
  9 "between" inclusive or not, read twice
 10 CI: z(alpha/2) = 1.96 at 95 percent, margin = 1.96 sigma/sqrt(n)
```

================================================================================
11. OUT OF MTE SCOPE (excluded, listed so the line is visible)
================================================================================

```
  lms-maximum-likelihood 16 pp | lms-method-of-moments 11 pp | mas2001-course-handout 7 pp
  | lms-theory CI block p031-039 10 pp
  topics: MLE, method of moments, Bayesian estimation, CI mechanics beyond the shape,
  hypothesis testing, t/F/chi-square, ANOVA, type I/II error theory
```

================================================================================
12. INVENTORY AND STATUS
================================================================================

```
  locked count register: teaching 60 (55 unique) + assignments 52 + U01 papers 16 = 128 / 123
  since 15 Sep: four decks 30, ETE 97, 2024-25 assignments 125, 2025-26 bundle 119
  provenance ledger (PR 10 branch): 383 gross instances, 37 traced, 9 open, 337 unsearched
  with the bundle merged (PR 14): 502 gross, 37 traced, 9 open, 456 unsearched
  the topic universe above is the union of every node those questions touch; the [C] marks
  are the nodes the late evidence confirmed.
```

---
Universe v1, 16 Sep 2026. Additive doc: nothing in the five superseded atlas files is deleted;
this one merges them and adds the post-15-Sep evidence. Fixes and the deep audit run after
the user's go, per order.
