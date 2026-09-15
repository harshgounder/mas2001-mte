# MAS2001 MTE: full syllabus tree, maximum depth

Built 15 September 2026. This is the deepest version: every topic expanded to subtopic,
sub-subtopic and atomic facts (definition or formula, source pages, worked numbers, traps,
question cross refs). Supersedes the compressed tree in 00-MASTER-SYLLABUS.md section 2.
Scope: MTE lectures 1 to 21 only. Out of MTE material is excluded entirely.

Legend:
```
  [+]  taught on slides AND used by questions, named in the syllabus
  [~]  used by questions, sits inside the topic, NOT named in the syllabus list
  [H]  used by questions but no batch-1 slide teaches it (Chebyshev left this class on
       15 Sep 2026 when S&P L10-11 arrived; batch-2 L1-7 and L8-9 are unconverted, so
       these marks are provisional until the U12 to U19 dedup pass)
  [!]  already graded in assignment 1 or 2 (batch 2 added: past papers and past assignments)
  deck = notes-lecture-series-01-09 (147 pp) | p3 = ppt3 | p4 = ppt4 | clt = CLT deck
  p5 = ppt5 | lt = lms-theory | D1-x = deck item ID from the count register
```

================================================================================
L1  INTRODUCTION OF THE COURSE  (deck p001 to p011)  not examined
================================================================================

1.1 course mechanics
    1.1.1 course code MAS2001, 3 credits, LTPC 2 1 0 3 [p004]
    1.1.2 assessment plan [p008]: MTE 30 closed book | CWS quizzes+assignments 30 |
          ETE 40 closed book | total 100
    1.1.3 course outcomes [p006, p007]: CO1 probability concepts, CO2 distributions,
          CO3 estimation, CO4 hypothesis testing
    1.1.4 faculty, delivery mode [p001]: Dr. Vivek Singh, powerpoint deck, dated 23 Jul 2026
1.2 syllabus and books
    1.2.1 the syllabus list [p009] and the lecture plan with MTE/CWS/ETE tags [handout p004, p005]
    1.2.2 reference books [p010]: Goon/Gupta/Dasgupta, Kendall/Stuart, Casella/Berger,
          Hogg/Tanis/Zimmerman, Feller
    1.2.3 textbook [p011]: Devore, Probability and Statistics for Engineering and the
          Sciences, 8th ed (the deck's random-variable material derives from it)
1.3 graded items: NONE. Read for framing only.

================================================================================
L2  BASIC TERMINOLOGY AND CONCEPTS OF PROBABILITY  (deck p012 to p050)  lect 2
================================================================================

2.1 what statistics is
    2.1.1 definition [p014]: the science of collection, presentation, analysis and
          interpretation of numerical data. Four verbs, in order.
    2.1.2 origin [p012]: science of statecraft; status (Latin), statista (Italian),
          statistik (German)
    2.1.3 the numerical-statement criterion [p012]:
          - all statistics are numerical statements BUT not all numerical statements
            are statistics
          - counter: "Ram has 100 Rs in his pocket" is NOT statistics (individual fact)
          - positive: "the average age of 5th class is 10 yrs" IS statistics (aggregate)
    2.1.4 importance [p015, p016, p020, p022]
          - engineer fields list: AI, ML, data science, robotics, networks, signal
            processing, quality control, reliability, manufacturing, finance, healthcare
          - real-life application boxes: disease prediction, stock risk, quality control,
            traffic, reliability, signal processing [p022]
    2.1.5 limitations, all four [p017]
          - not suited to qualitative phenomena
          - does not study individuals
          - statistical laws are not exact (not universally true)
          - liable to misuse
          - misuse worked example: satisfaction survey run only among loyal customers,
            dissatisfied ones excluded, so the result is falsely positive
    2.1.6 graded items: none. Framing only.

2.2 random experiment, outcome, sample space, event
    2.2.1 random experiment [p023]: outcome cannot be predicted with certainty in advance,
          although all possible outcomes are known. Four examples: coin, die, card, student.
    2.2.2 sample space [p024]: the set of all possible outcomes, denoted S
          - coin: S = {H, T}
          - die: S = {1, 2, 3, 4, 5, 6}
          - two coins: S = {HH, HT, TH, TT}, 4 outcomes
          - two dice: S = {(1,1) ... (6,6)}, 6 x 6 = 36 outcomes
          - subtlety: two-dice outcomes are ORDERED pairs, (1,2) and (2,1) both exist
    2.2.3 outcomes of an experiment, structured coding (D1-1, deck p041 to p042)
          - tournament setup: teams 1, 2, 3, 4; first round 1v2 and 3v4; winners final,
            losers consolation
          - outcome notation "1324": 1 beats 2, 3 beats 4, then 1 beats 3 and 2 beats 4
          - part (a): list all of S: 16 outcomes, enumerated
          - part (b): A = "1 wins the tournament": 4 outcomes (1 first in the code)
          - part (c): B = "2 reaches the championship game": 8 outcomes
          - part (d): A u B has 12 outcomes; A n B = empty (1 and 2 cannot both be in the
            final); A' has 12 outcomes
          - the skill: construct an outcome code that carries all information, enumerate
            without listing duplicates, then answer set questions on it
    2.2.4 graded refs: D1-1 (tournament). Also appears in style across A1 short 1.

2.3 event algebra (set relations)
    2.3.1 complement A' [p032]: all outcomes in S not in A
    2.3.2 union A u B [p033]: "A or B", outcomes in A, in B, or in both. Wording matters:
          the union INCLUDES the overlap
    2.3.3 intersection A n B [p034]: "A and B", outcomes in both
    2.3.4 null event phi [p035]: event with no outcomes
    2.3.5 mutually exclusive / disjoint [p035]: A n B = phi. Pairwise version for many
          events [p037]
    2.3.6 counter-example style [p025]: even {2,4,6} and prime {2,3,5} share 2, NOT
          disjoint. Same page has the two clean examples (even/odd, head/tail)
    2.3.7 Venn diagrams [p038 to p040]: rectangle = S, closed curve = event; four shaded
          cases (A n B, A u B, A', disjoint pair)
    2.3.8 extension to 3 events [p036]: A u B u C = at least one; A n B n C = all three
    2.3.9 graded refs: set questions inside every combinatorial item.

2.4 axioms and probability rules
    2.4.1 Kolmogorov axioms [p044]: P(S) = 1; P(A) >= 0 for every A; for disjoint
          A1, A2, ... : P(union) = sum of P(Ai)
    2.4.2 equally likely outcomes [p044]: P(E) = favourable / total, and the range
          0 <= P(E) <= 1. Interpretation scale [p018, p019]: near 1 = very likely,
          near 0 = rare, 0.5 = even odds
    2.4.3 addition rule [p045]: P(A u B) = P(A) + P(B) - P(A n B). Disjoint case drops
          the correction: P(A u B) = P(A) + P(B)
    2.4.4 complement rule [p045]: P(A^c) = 1 - P(A)
    2.4.5 multiplication rule [p045]: P(A n B) = P(A) P(B|A) = P(B) P(A|B); the
          independence case: P(A n B) = P(A) P(B)
    2.4.6 complement discipline as a method [~][H, as a named technique]
          - "at least one" -> 1 - P(none)
          - "no X" -> the single zero case
          - "rejected / overflow" -> 1 - lower tail
          - "more than k" -> 1 - F(k)
          - usage sites: A1 MCQ style, p3 pens part (ii), D1-2(c) (1 - 1/15 = 14/15),
            D1-15, A2 B1 (P(X>=4) = 0.2424), A2 C3 (P(X>2) = 0.8753)
          - no slide teaches it as a named method; it is learned by doing
    2.4.7 graded refs: every probability question leans on these four rules.

2.5 counting
    2.5.1 permutations [p043]: P(n, r) = n!/(n-r)!, order matters
    2.5.2 combinations [p043]: C(n, r) = n!/((n-r)! r!), order does not matter
    2.5.3 repeated items [p043]: n!/(n1! n2! ... nk!) for n1, n2, ... identical items
    2.5.4 factorial reminder [p006]: n! = n(n-1)(n-2)...
    2.5.5 C(n,r) as the engine inside probability questions [~]
          - C(6,2) = 15: the laptop/desktop denominator (D1-2)
          - C(4,2) = 6: both-desktop favourable count (D1-2b)
          - C(4,2) C(4,2) C(3,1) style products: the basketball lineup count (D1-3)
          - C(12,2) = 66: binomial coefficient in the pens question (p3 p014)
          - C(15,5) = 3003: the lineup probability denominator (D1-3b)
    2.5.6 disjoint-union counting [~]: when A and B are disjoint, count the middle case
          as 1 - P(A) - P(B) (D1-2d: 1 - 1/15 - 2/5 = 8/15)
    2.5.7 graded refs: D1-2, D1-3, pens, every combinatorial denominator.

2.6 conditional probability
    2.6.1 definition [p050]: for P(B) > 0, P(A|B) = P(A n B) / P(B)
    2.6.2 meaning [p050]: renormalize the world to the condition; "of all those with B,
          what fraction also have A"
    2.6.3 camera chain (D1-4, p050): P(A) = .60 card, P(B) = .40 battery, P(A n B) = .30
          - P(A|B) = .30/.40 = .75
          - P(B|A) = .30/.60 = .50
          - skill: read which conditional is asked, divide by the right marginal
    2.6.4 conditional inside a continuous model [~] (D1-25): f(x) = 2x on (0,1),
          P(X <= 1/2 | 1/3 <= X <= 2/3) = (int_1/3^1/2 2x) / (int_1/3^2/3 2x) = 5/12
          - skill: probability ratio of two areas, no new machinery
    2.6.5 conditional on a normal [~] (A1 long 1): P(die 60-70 | live to 60) =
          0.1544 / 0.6826 = 0.4863
          - skill: P(A n B) / P(B) with normal machinery; here A implies subset of B
    2.6.6 conditional on an exponential [~] (A2 B5, errata 9): P(X < 1 | X < 2) =
          (1 - e^-0.5)/(1 - e^-1) = 0.6225 (the key's 0.5679 is wrong)
    2.6.7 link to independence [p028]: A, B independent iff P(A|B) = P(A)
    2.6.8 graded refs: D1-4, D1-25, D1-26(f style), A1 long 1, A2 B5.

2.7 event independence
    2.7.1 definition via product [p027]: P(A n B) = P(A) P(B)
    2.7.2 equivalent form [p028]: P(A|B) = P(A); dependent otherwise
    2.7.3 two-draws intuition [p027]: draw a card, REPLACE, draw again: independent.
          Without replacement the second draw is affected (dependent)
    2.7.4 mutual independence of n events [p028]: for EVERY k = 2..n and every subset
          i1..ik: P(intersection) = product of P's. All subsets, not just the full set
    2.7.5 independence as a modeling assumption [~]: batteries selected independently
          (D1-15), die tosses, the trial conditions in binomial
    2.7.6 forward pointer [H]: rv-level independence rules sit only in lecture 8-9, and
          they are NOT on any slide. See section H below
    2.7.7 graded refs: MCQ style, every binomial/Poisson framing.

================================================================================
L3-4  RANDOM VARIABLES  (deck p051 to p062 intro, p112 to p147 continuous)  
================================================================================

3.1 the definition
    3.1.1 random variable [p051, p063]: a function whose domain is the sample space and
          whose range is the real numbers. Notation X(s) = value
    3.1.2 Bernoulli rv [p052]: only values 0 and 1; coin mapping X(H) = 1, X(T) = 0
    3.1.3 counting rv [p053]: two coins, X = number of heads; X(HH) = 2, X(HT) = 1,
          X(TH) = 1, X(TT) = 0
    3.1.4 dice sum [p054, p055]: X = sum of two fair dice; support 2..12;
          P(X=2) = 1/36, P(X=3) = 2/36, P(X=4) = 3/36 (listed), general triangular pmf
    3.1.5 two coins full pmf [p056]: Y = heads count: P(0) = 1/4, P(1) = 2/4,
          P(2) = 1/4, and the sum equals 1 check
    3.1.6 geometric rv [p057 to p059]: toss until first head; N = number of tosses;
          P(N=1) = p, P(N=2) = (1-p)p, P(N=n) = (1-p)^(n-1) p
          - support is countably infinite (values 1, 2, 3, ...)
          - the verify step [p059]: P(union of N=n) = 1 via geometric series with
            common ratio (1-p). This is the discrete-with-infinite-support case
    3.1.7 car lifetime [p060]: values fill an interval, the continuous case teaser
    3.1.8 taxonomy [p061, p062, p063, p076]:
          - discrete: finite, or listable as a sequence with a first, second, ... element
          - continuous: values fill an interval (or disjoint union), and P(X = c) = 0
            for every single c
    3.1.9 graded refs: D1-5, D1-6, D1-7, D1-8, D1-9, D1-10 (the ten opening examples).

3.2 functions of a random variable [~]
    3.2.1 Y = X + 4 [D1-29]: hospitalization days; find E(Y) = 8
    3.2.2 h(X) = 25X - 8.5 [D1-22]: expected price; and h(X) = X - .01 X^2: expected
          actual capacity
    3.2.3 M = max of two dice [D1-17]: pmf of M: p(1) = 1/36, p(2) = 3/36, ..., p(6) = 11/36
          (the pattern 2m - 1 over 36)
    3.2.4 revenue functions h3, h4 [D1-23]: pieces depending on demand vs stock
          - h3(x) = 2x - 3 for x = 1, 2 then plateaus at 3
          - h4(x) = 2x - 4 for x = 1..3 then plateaus at 4
          - E[h3] = 2.4667 vs E[h4] = 2.6667: order 4 copies
    3.2.5 support identification [~]: before any pmf work, write the set of possible
          values (and note open/closed, infinite bounds)
    3.2.6 graded refs: D1-15 to D1-17, D1-22, D1-23, D1-29.

3.3 the continuous case, definitions
    3.3.1 why densities [p113 to p115]: peak demand time; probability of an EXACT value
          like the peak at 12.013278... is zero. The zero-probability logic:
          P(X = x0) = int_x0^x0 f = 0 [p121]
    3.3.2 continuous rv definition [p116, p063]: assumes any value in an interval, and
          P(X = that value) = 0
    3.3.3 continuous density (pdf) conditions [p117]:
          (i) f(x) >= 0
          (ii) int_{-inf}^{+inf} f(x) dx = 1
          (iii) P(a <= X <= b) = int_a^b f(x) dx, the AREA interpretation [p118]
    3.3.4 remarks [p119 to p123]:
          - normalize a non-density: if int = k != 1, then f(x)/k is the pdf
          - idealized description note
          - P = 0 does NOT mean impossible (unlike the discrete case) [p122]
          - if X lives on [a, b], set f(x) = 0 outside [p123]
    3.3.5 graded refs: D1-24 onward.

================================================================================
L5-6  PMF / PDF AND CDF  (deck p063 to p087, p112 to p139)
================================================================================

4.1 pmf, discrete
    4.1.1 definition [p064]: p(x) = P(X = x) = P(all s in S with X(s) = x); it fully
          describes the variable
    4.1.2 the two conditions [p064]: p(x) >= 0 AND sum over all x = 1 (necessary and
          sufficient)
    4.1.3 find k by normalization, arithmetic case [~] (D1-14, deck p070 to p071):
          p(y) = ky for y = 1..5: sum = k(1+2+3+4+5) = 15k = 1, so k = 1/15
          - part b: P(Y <= 3) = 6/15 = .4
          - part c: P(2 <= Y <= 4) = 9/15 = .6
          - part d: is p(y) = y^2/50 valid? sum = 55/50 != 1, NO
    4.1.4 find k by normalization, quadratic case [~] (D1-12, deck p066, A1 long 2):
          p: 0, k, 2k, 2k, 3k, k^2, 2k^2, 7k^2+k over x = 0..7
          - normalisation: 9k + 10k^2 = 1 (since p(0) = 0 adds nothing)
          - exact root k = 1/10; the trap: circulated versions with 12k or 14k do not
            satisfy k = 1/10 (errata 5)
    4.1.5 pmf built from combinatorics [~]:
          - boards [D1-16]: pairs from 5 boards, P(X=0) = 3/10, P(X=2) = 1/10,
            P(X=1) = 6/10 found by COMPLEMENT
          - dice maximum [D1-17]: see 3.2.3
          - batteries [D1-15]: P(2) = .81, P(3) = .162, P(5) = .00324, general
            p(y) = (y-1)(.1)^(y-2)(.9)^2
    4.1.6 proportional-form family [~]: p(y) prop to y style, see 4.1.3
    4.1.7 graphs [p067 to p069, p083, p084]: line graph AND probability histogram; the
          step plot for cdfs
    4.1.8 graded refs: D1-12, D1-14, D1-15, D1-16, D1-17.

4.2 cdf, discrete
    4.2.1 definition [p074]: F(x) = P(X <= x) = sum of p(y) over y <= x
    4.2.2 properties [p078]: nondecreasing; the proof question [D1-18]: for x1 < x2,
          F(x2) = F(x1) + P(x1 < X <= x2) >= F(x1); equality when that middle piece
          has probability zero
    4.2.3 pmf from cdf [p078]: f(n) = F(n) - F(n-1)
    4.2.4 interval via cdf for integer rvs [p135]: P(a <= X <= b) = F(b) - F(a-1).
          The a-1 is the classic slip (continuous case uses F(b) - F(a) instead)
    4.2.5 construction per interval [~]:
          - boards [D1-16c]: F(x) = 0 for x<0, .30 for 0<=x<1, .90 for 1<=x<2, 1 for x>=2
          - dice max [D1-17b]: F steps 0, 1/36, 4/36, 9/36, 16/36, 25/36, 1
    4.2.6 minimum c with F(c) > 1/2 [~] (D1-12 iv, A1 long 2 iv): F(3) = 5/10 exactly,
          the strict > fails equality, so c = 4
    4.2.7 "at most" reading [p065]: P(X <= 2) = .05+.10+.15 = .30 style
    4.2.8 graded refs: D1-12, D1-14, D1-16, D1-17, D1-18.

4.3 pdf and cdf, continuous
    4.3.1 cdf definition [p130 to p132]: F(x) = P(X <= x) = int_{-inf}^x f(y) dy;
          the area to the left of x
    4.3.2 using F [p133 to p135]: P(X > a) = 1 - F(a); P(a <= X <= b) = F(b) - F(a).
          The discrete analog uses F(b) - F(a-1), the continuous one does NOT [p135]
    4.3.3 density from cdf [p136, p137]: F'(x) = f(x) at every point where the derivative
          exists (Fundamental Theorem of Calculus)
          - worked [D1-28]: F(x) = (x-1)^4/16 on [1,3]; f(x) = (x-1)^3/4;
            P(2 <= X <= 3) = 1 - F(2) = 1 - 1/16 = 15/16
          - exercise pair [D1-27]: (i) f = 1/3 on [0,1] then 2/3 on (1,2];
            (ii) f = |x| on (-1,1), even symmetry
    4.3.4 piecewise pdf integration [~]:
          - bus triangle [D1-26, errata 13]: f(y) = y/25 on [0,5), 2/5 - y/25 on [5,10];
            7 parts: sketch, verify integral = 1, P(Y<=3) = .18, P(Y<=8) = .92,
            P(3<=Y<=8) = .74, P(Y<2 or Y>6) = .40 (errata: printed bound 3, should be 2)
          - f = 2x [D1-24]: verify + P(X <= 1/2) = 1/4
    4.3.5 improper integrals and tails [~] (D1-30): Pareto f = k th^k / x^(k+1)
          - E(X) = k th/(k-1) for k > 1; infinite at k = 1
          - V(X) = k th^2 / ((k-2)(k-1)^2) for k > 2; infinite at k = 2
          - E(X^n) finite iff n < k
    4.3.6 graded refs: D1-24, D1-26, D1-27, D1-28, D1-30.

================================================================================
L7  EXPECTATION OF RANDOM VARIABLES  (deck p088 to p094, p140 to p147)
================================================================================

5.1 expectation, discrete
    5.1.1 definition [p088]: E(X) = mu_X = sum over D of x p(x); the weighted average
    5.1.2 interpretation [p091]: location parameter, center of the distribution; "the
          mean" mu
    5.1.3 die example [p089]: E(X) = (1+2+...+6)/6 = 3.5 via the sum
    5.1.4 function of an rv [p090]: E[h(X)] = sum h(x) p(x), provided sum |h(x)| p(x)
          is finite
    5.1.5 the p094 question [D1-21]: X over {-3, 6, 9} with 1/6, 1/2, 1/3:
          E(X) = 11/2, E(X^2) = 93/2, E(2X+1)^2 = 209 (uses the laws, not enumeration)
          - E(2X+1)^2 = E(4X^2 + 4X + 1) = 4(93/2) + 4(11/2) + 1 = 209
    5.1.6 revenue tables [D1-23]: see 3.2.4
    5.1.7 freezer chain [D1-22], all six pieces: E(X) = 16.38, E(X^2) = 272.298,
          V(X) = 3.9936, E(25X - 8.5) = 401, V(25X - 8.5) = 2496,
          E(X - .01 X^2) = 13.66
    5.1.8 graded refs: D1-20, D1-21, D1-22, D1-23.

5.2 properties of the mean
    5.2.1 E(c) = c, proof by sum [p092]
    5.2.2 E(cX) = c E(X), proof by sum [p092]
    5.2.3 E(aX + b) = a E(X) + b, the proof exercise [D1-20, p093]
    5.2.4 the always-true linearity [formula sheet line 94]: E(X + Y) = E(X) + E(Y),
          NO independence needed. The contrast with the product rule is a trap zone

5.3 expectation, continuous
    5.3.1 definition [p140, p141]: replace summation with integration: E(X) = int x f(x) dx
    5.3.2 E[h(X)] [p143]: int h(x) f(x) dx
    5.3.3 linear case [p144] continues: E(aX + b) = aE(X) + b
    5.3.4 convergence conditions [D1-30]: see 4.3.5
    5.3.5 shifted rv [D1-29]: Y = X + 4, E(Y) = 8 days
    5.3.6 expected count over N repeats [H][!]: E = N x P
          - p3 p018: 10000 sets x (3/8)^10 = 10000 x 0.000055 = 0.5499 expected sets
            with no even number (errata 2: slide prints 0.549)
          - A2 B4: 5000 batteries: 274 / 576 / 4487 expected in each range
          - A2 D1: 10000 bulbs x P(2500 < X < 3500) = 7888
          - no slide states the rule; it is used at least four times
    5.3.7 graded refs: D1-29, D1-30, A2 B4, A2 D1, p3 p018.

================================================================================
L8-9  EXPECTATION + INDEPENDENT RANDOM VARIABLES  (deck p095 to p111)
================================================================================

6.1 variance machinery
    6.1.1 definition [p097]: Var(X) = E[(X - mu)^2]; sd = sqrt(Var)
    6.1.2 remarks [p098, p099]: always non-negative; large variance = inconsistent,
          spread out; small = concentrated, stable [p106]
    6.1.3 the shortcut formula [p101 to p103]: Var(X) = E(X^2) - [E(X)]^2, proved:
          expand E[(X - mu)^2] = E(X^2) - 2mu E(X) + mu^2
    6.1.4 Var(c) = 0 [p103]
    6.1.5 Var(cX) = c^2 Var(X) [p103]
    6.1.6 V(aX + b) = a^2 V(X); sd(aX + b) = |a| sd(X), absolute value because a can
          be negative [p104, p105]
    6.1.7 the unit-change story [p104, p105]: multiplication = unit conversion,
          addition = shift only, no spread change
    6.1.8 Var from a pdf, two integrals [~] [p144, p145]: V(X) = int (x-mu)^2 f(x) or
          the shortcut E(X^2) - mu^2 with E(X^2) = int x^2 f(x)
    6.1.9 freezers etc: full numeric chains live in D1-22, A1 app 3 (battery var 0.9475,
          sd 0.9734, errata 12)

6.2 INDEPENDENT RANDOM VARIABLES, the hidden block [H][!]
    6.2.1 E(XY) = E(X) E(Y) when X, Y independent: NO slide teaches it. Source of truth:
          formula sheet section C
    6.2.2 Var(X + Y) = Var(X) + Var(Y) when independent: NO slide. Sheet section D
    6.2.3 Var(X - Y) = Var(X) + Var(Y), same plus rule (the coefficient squares):
          NO slide
    6.2.4 where it is needed downstream:
          - Var(sum of two dice) = 2 x 35/12 = 35/6: the Chebyshev sum question (A1 short 5)
          - Var(Xbar) = sigma^2 / n: every CLT question (clt deck)
          - estimator variances: Var(t2 = (X1+X2)/2 + X3) = sigma^2/2 + sigma^2 (p5 p018)
          - T2 = 2X1 + 3X3 - 4X2: coefficient -4 squares to 16 (p5 p021)
          - sum of independent Poissons is Poisson (A2 A12)
    6.2.5 the T4/trap note: variance being SMALL does not win if the estimator is biased
          (mock B4, see L20-21)
    6.2.6 graded refs: A1 short 5, every CLT numeric, both estimator comparison sets.

6.3 the variance of a sum of dice, the canonical drill [~]
    6.3.1 Var(one die) = E(X^2) - 3.5^2 = 91/6 - 12.25 = 35/12
    6.3.2 Var(two dice sum) = 35/12 + 35/12 = 35/6 = 5.8333 (independence rule)
    6.3.3 used in A1 short 5 to get k and the 35/54 bound

================================================================================
L10-11  CHEBYSHEV'S INEQUALITY  (deck arrived 15 Sep, was the missing block)
================================================================================

7.1 the statement and both forms
    7.1.1 tail form: P(|X - mu| >= k sigma) <= 1 / k^2
    7.1.2 complement form: P(|X - mu| < k sigma) >= 1 - 1 / k^2
    7.1.3 relation: the two forms are complements; pick the one matching the ask
    7.1.4 canonical values: k=2 -> 3/4 (or 1/4 tail), k=3 -> 8/9 (or 1/9),
          k=4 -> 15/16 (or 1/16)
7.2 the distribution-free property
    7.2.1 applicable to ANY distribution with finite mean and variance (A1 MCQ 10)
    7.2.2 why: it is a moment bound, distribution-free
7.3 k extraction from an interval
    7.3.1 convert the interval to |X - mu| < c, then k = c / sigma
    7.3.2 worked: 60 to 80 around mu 70, sigma 5: c = 10, k = 2, bound 3/4 (A1 app 4)
7.4 the tail vs complement fork (the classic trap)
    7.4.1 "outside" / "at least c away" -> tail form -> 1/k^2 (upper bound)
    7.4.2 "between" / "within c" -> complement form -> 1 - 1/k^2 (lower bound)
    7.4.3 the 1/9 vs 8/9 trap: below-55-or-above-85 is the TAIL, answer 1/9 (mock B1)
7.5 application to a sum of rvs [~]
    7.5.1 step 1: find Var(sum) using the independence rule (dice: 35/6)
    7.5.2 step 2: sigma_sum = sqrt(35/6); step 3: k = 3 / sigma_sum
    7.5.3 the dice question [A1 short 5]: P(|X - 7| >= 3) <= 35/54 = 0.6481,
          actual probability 1/3 = 0.3333, compare and note the bound is loose
7.6 lower bound for a counts interval [~]
    7.6.1 600 throws, X = sixes: mu = 100, Var = 600 x (1/6)(5/6) = 83.333,
          sigma = 9.129
    7.6.2 80 to 120 = within 20 of the mean: k = 20 / 9.129 = 2.191, k^2 = 4.8
    7.6.3 bound: 1 - 1/4.8 = 19/24 = 0.7917 (A1 short 6)
7.7 proportion phrasing in reverse [~]
    7.7.1 "minimum proportion scoring between 60 and 80" = the complement form directly
          (A1 app 4: 75 percent)
7.8 applicability statements
    7.8.1 A1 MCQ 5: which inequality gives an upper bound on deviation from the mean:
          Chebyshev
    7.8.2 A1 MCQ 10: applicable to any distribution with finite mean and variance
7.9 sources: deck S&P L10-11 (arrived 15 Sep), formula sheet section E, question bank
    section 6, mock B1. Graded: 5x in assignment 1 + MTE 2024-25 (QA3, QB3) + MTE
    2025-26 (Q5) + 2025-26 assignment Q5 = 9+ uses.

================================================================================
L12  BINOMIAL DISTRIBUTION  (p3 p001 to p018)
================================================================================

8.1 the derivation story [p002 to p007]
    8.1.1 5-coin toss, P(exactly 3 heads): each arrangement has probability
          (1/2)^3 (1/2)^2, ten arrangements, so 10 x (1/2)^5 = 31.25%
    8.1.2 why 10: C(5,3) = 5!/(3! 2!) = 10 arrangements, all listed on p006
    8.1.3 the pattern that becomes the pmf: coefficient x p^x x q^(n-x)
8.2 setup conditions [p008, p011], all four
    8.2.1 each trial has two disjoint outcomes (success / failure)
    8.2.2 n finite
    8.2.3 trials independent
    8.2.4 p constant across trials
8.3 the pmf [p009, p010]
    8.3.1 P(X = x) = C(n, x) p^x q^(n-x), x = 0..n, zero otherwise
    8.3.2 notation X ~ B(n, p); n = "degree"; the two parameters n, p
8.4 mean and variance [p012]
    8.4.1 E(X) = np
    8.4.2 Var(X) = npq
    8.4.3 (used in A2 A2: n=10, p=0.5 -> var 2.5)
8.5 complement tails, the pens question [p013 to p016]
    8.5.1 setup: 10% defective, box of 12, X ~ B(12, 0.1)
    8.5.2 part i: P(X = 2) = C(12,2)(0.1)^2(0.9)^10 = 66 x 0.01 x 0.3487 = 0.2301
          - coefficient expansion C(12,2) = 12!/(2! 10!) = 66
    8.5.3 part ii: P(X >= 2) = 1 - [P(0) + P(1)] = 1 - [0.2824 + 0.3766] = 0.341
          - P(0) = 0.9^12 = 0.2824; P(1) = 12 x 0.1 x 0.9^11 = 12 x 0.1 x 0.3138 = 0.3766
    8.5.4 part iii: P(X = 0) = 0.2824 (no defective: all 12 good)
8.6 parameter recovery from a ratio, the irregular die [p017, p018]
    8.6.1 condition: P(X = 5) = 2 P(X = 4) over n = 10 throws
    8.6.2 C(10,5) p^5 q^5 = 2 C(10,4) p^4 q^6 -> 252 p = 2 x 210 x q -> 3p = 5q
    8.6.3 solve with q = 1 - p: p = 5/8, q = 3/8
    8.6.4 then E = 10000 x P(X = 0) = 10000 x (3/8)^10 = 0.5499 (errata 2: prints 0.549)
8.7 framing identification [~]
    8.7.1 physical die -> "even number" is the success; p = 0.5 if fair, here unknown
8.8 the Poisson limit conditions [p022] (used by A2 D3)
    8.8.1 n -> infinity, p -> 0, np -> lambda finite
    8.8.2 approximation: C(n,x) p^x q^(n-x) ~= e^-lambda lambda^x / x!
8.9 MCQ surface from A2
    8.9.1 variance formula check (A2 A2: 2.5)
    8.9.2 max successes possible (A2 A9: 12, the whole n)
8.10 graded refs: pens (p3 13-16), die (p3 17-18), coin toss (p3 3-7), A2 A2, A2 A9, A2 D3.

================================================================================
L13  POISSON DISTRIBUTION  (p3 p019 to p028)
================================================================================

9.1 when to use it [p020, p021]
    9.1.1 count of rare events in a fixed interval (time, space, volume)
    9.1.2 the seven-instance list [p021]: deaths, suicides, defective material, faulty
          blades, air accidents, printing mistakes, cars at a crossing
9.2 the pmf and its signature [p023, p024]
    9.2.1 P(X = x) = e^-lambda lambda^x / x!, x = 0, 1, 2, ..., lambda > 0
    9.2.2 notation X ~ P(lambda)
    9.2.3 E(X) = lambda; Var(X) = lambda; mean EQUALS variance is the signature
9.3 lambda recovery from a ratio [p025]
    9.3.1 P(X=1) = 0.2 P(X=2): e^-l l = 0.2 e^-l l^2/2 -> 1 = 0.1 l -> lambda = 10
    9.3.2 then P(X = 0) = e^-10 = 0.0000454
9.4 rate and window scaling [~] [p026, A2 D2]
    9.4.1 rates met: 2/min, 15/hr (slide), 4/hr (A2), 5/day (A2 C3), 2.5/day (A2 B1)
    9.4.2 convert the ASKED window to the rate's unit before substituting
    9.4.3 worked: 4/hr, wait > 30 min = 0.5 hr: e^-2 = 0.1353 (A2 D2)
9.5 the zero case [p025, A2 D3]
    9.5.1 P(X = 0) = e^-lambda
    9.5.2 200 jobs, 1% need weekend: lambda = 2, P(0) = e^-2 = 0.1353 (A2 D3)
9.6 tail sums [A2 C3]
    9.6.1 P(X > 2) = 1 - P(0) - P(1) - P(2); with lambda = 5:
          1 - e^-5(1 + 5 + 12.5) = 0.875348 -> 0.8753 (errata 14: key prints 0.8754)
9.7 capacity overflow reading [A2 B1]
    9.7.1 3 technicians, demand Poisson mean 2.5; "demand rejected" = P(X >= 4)
    9.7.2 P(X = 0) = 0.0821; P(X >= 4) = 0.2424
    9.7.3 read "rejected" as the complement of "serveable": n = 3 so overflow starts at 4
9.8 the nesting question [p026], the trickiest corpus item
    9.8.1 calls at 2/min; find P(exactly 2 calls in EACH of the first 5 minutes)
    9.8.2 layer 1: P(2 calls in one minute) = e^-2 2^2/2! = 2e^-2 = p
    9.8.3 layer 2: M = number of minutes (of 5) with exactly 2 calls: M ~ B(5, p)
    9.8.4 P(M = 5) = p^5 = (2e^-2)^5 = 32 e^-10 = 0.00145
    9.8.5 the skill: two distributions stacked, identify both before computing
9.9 Poisson as a binomial approximation [p027, A2 D3]
    9.9.1 5000 men, p = 0.001: lambda = 5, P(4 claims) = e^-5 5^4 / 4! = 0.1755
          (errata 1: prints 0.1745)
    9.9.2 rule of thumb: large n, small p, lambda = np moderate
9.10 additivity of independent Poissons [A2 A12]
    9.10.1 X + Y ~ P(lambda1 + lambda2) when independent (sheet line 182)
9.11 graded refs: p3 25, 26, 27, A2 A3, A2 A7, A2 A12, A2 B1, A2 C3, A2 D2, A2 D3.

================================================================================
L14  UNIFORM DISTRIBUTION (CONTINUOUS)  (p4 p001 to p006)
================================================================================

10.1 the density and moments
    10.1.1 f(x) = 1/(b-a) flat on (a, b), 0 outside
    10.1.2 mean = (a+b)/2; variance = (b-a)^2/12
    10.1.3 A2 A4 asks the variance formula directly
10.2 the length-ratio shortcut [~]
    10.2.1 probability = length of subinterval / total length
    10.2.2 P(X < 5) for (2, 6) = 3/6 = 0.5 (p4 p006)
    10.2.3 P(X > 16) for (10, 20) = 0.4 (A2 B2)
10.3 clipping to the support [~] [A2 A10]
    10.3.1 P(c < X < d) with d > b: the part beyond b has probability zero, so the
          answer is (b - c)/(b - a)
10.4 absolute values to intervals [~] [A2 B8]
    10.4.1 X on (-3, 3): P(X < 2) = 5/6; P(|X| < 2) = P(-2 < X < 2) = 2/3;
          P(|X - 2| < 2) = P(0 < X < 4 clipped to 3) = 1/2
    10.4.2 inverse: P(X > K) = 1/3 -> (3 - K)/6 = 1/3 -> K = 1
10.5 rounding error application [A2 C4]
    10.5.1 error uniform on (-0.5, 0.5); P(|err| > 0.2) = P(err < -0.2 or err > 0.2)
          = 2 x 0.3 / 1 = 0.6
10.6 two uniforms combined [D1-26 cross ref]
    10.6.1 waiting at two stops, each uniform (0, 5); total time is triangular on (0, 10)
10.7 graded refs: p4 3-6, A2 A4, A2 A10, A2 B2, A2 B8, A2 C4, D1-26.

================================================================================
L15  NORMAL DISTRIBUTION  (p4 p007 to p037)
================================================================================

11.1 the density and its shape
    11.1.1 f(x) = 1/(sigma sqrt(2pi)) exp(-(x-mu)^2 / 2 sigma^2) [p012]
    11.1.2 parameters mu and sigma^2; notation X ~ N(mu, sigma^2) (the second slot is
          VARIANCE, easy to misread, errata 7)
    11.1.3 symmetry; mean = median = mode = mu; tails never touch [p008]
    11.1.4 many normals via mu and sigma [p010, p011]
11.2 standardization [p019, p028]
    11.2.1 Z = (X - mu)/sigma; Z ~ N(0, 1)
    11.2.2 procedure: draw, convert X to Z, read the table
11.3 THE TWO TABLE CONVENTIONS, both live in this course [H discipline]
    11.3.1 cumulative table: F(z) = P(Z < z), full area from -inf (p022 table, appendix,
          "F(0.12) = 0.5478")
    11.3.2 area-from-zero table: phi(z) = area between 0 and z (p023 to p025 tables,
          the classic "table of areas" with .0000 .0040 .0080 rows)
    11.3.3 conversion: phi(z) = F(z) - 0.5; F(z) = 0.5 + phi(z)
    11.3.4 identify the convention from the question's given values BEFORE substituting
          (assignments give phi values like phi(1.04) = 0.35)
11.4 left tail and negative z [p026, p027]
    11.4.1 symmetry reflection: P(Z < -a) = P(Z > a) = 1 - P(Z < a)
    11.4.2 worked: P(Z < -2.00) = 1 - 0.9772 = 0.0228
11.5 upper tail [p032, p033]
    11.5.1 P(X > 8.6) = P(Z > 0.12) = 1 - 0.5478 = 0.4522
11.6 interval probabilities [p019]
    11.6.1 P(a < X < b) = F((b-mu)/sigma) - F((a-mu)/sigma)
    11.6.2 worked: mu 50, sigma 10, P(45 < X < 62): z1 = -0.5, z2 = 1.2,
          0.1915 + 0.3849 = 0.5764 (A2 B3)
11.7 inverse direction [p034 to p037]
    11.7.1 steps: find z for the stated probability, then X = mu + z sigma
    11.7.2 worked: 20% lower tail: z = -0.84, X = 8.0 + (-0.84)(5.0) = 3.80
11.8 landmarks [H] [A2 A11]
    11.8.1 68.27% within 1 sigma; 95.45% within 2; 99.73% within 3
    11.8.2 asked in MCQ (pick 68.27% for +-1); no slide teaches the numbers
11.9 two-unknown system from two percentiles [H] [A2 C2, errata 10]
    11.9.1 setup: 46% pass at 40 -> phi = 0.04 at z = 0.10; 9% distinction at 75 ->
          phi = 0.41 at z = 1.34
    11.9.2 subtract: 35 = (1.34 - 0.10) sigma -> sigma = 28.23 -> 28.2
    11.9.3 back-substitute: mu = 40 - 0.10 x 28.23 = 37.18 -> 37.2 (key prints 37.5,
          its own cutoff 30.43 only reproduces with 37.2)
    11.9.4 third part: top 25% of failures re-examined: cutoff = mu - 0.24 sigma =
          37.2 - 6.77 = 30.4
    11.9.5 the skill: two equations, two unknowns, then a conditional tail re-use
11.10 expected count [~]: see 5.3.6 (batteries 274/576/4487, bulbs 7888)
11.11 errata 8: p030 figure prints sigma = 10 under mu = 8; real sigma 5.0
11.12 graded refs: p4 17, 26, 27, 29-37, A2 A1, A2 A6, A2 A11, A2 B3, A2 B4, A2 B6,
     A2 C2, A2 D1.

================================================================================
L16  EXPONENTIAL DISTRIBUTION  (p4 p038 to p043)
================================================================================

12.1 the density family
    12.1.1 f(t) = lambda e^-lambda t for t > 0
    12.1.2 cdf: F(t) = 1 - e^-lambda t
    12.1.3 survival: P(T > t) = e^-lambda t
    12.1.4 mean = 1/lambda; variance = 1/lambda^2 [p041]
    12.1.5 errata 4: p040 says "1/lambda is the mean number of occurrences per unit
          time", which inverts it; lambda is the rate, 1/lambda is the mean TIME
12.2 modeling [p039]: time between arrivals (trucks, ATM transactions, phone calls)
12.3 memoryless property [H][!] [A2 MCQ Q5, A2 C1]
    12.3.1 statement: P(T > s + t | T > s) = P(T > t)
    12.3.2 no slide defines it; the formula sheet carries it
    12.3.3 worked: survived 500 hr, P(survive to 1500) = P(T > 1000) = e^-1 = 0.3679
          (A2 C1)
12.4 conditionals with cdf ratios [A2 B5, errata 9]
    12.4.1 P(X < 1 | X < 2) = (1 - e^-0.5)/(1 - e^-1) = 0.6225
12.5 mean to lambda both directions [~]
    12.5.1 mean 2 -> lambda = 1/2 (A2 B5); lambda = 1/2 -> mean 2 (A2 B7)
    12.5.2 read carefully which one the question gives
12.6 unit conversion inside the story [A2 D2]
    12.6.1 30 minutes against a rate in hours: t = 0.5 hr
    12.6.2 P(wait > 30 min) = e^-4(0.5) = e^-2 = 0.1353
12.7 repair-time pattern [A2 B7]
    12.7.1 P(T > 2) = e^-1 (lambda = 1/2)
    12.7.2 P(T > 11 | T > 8) = P(T > 3) = e^-1.5 (memoryless shortcut)
12.8 slide example [p042, p043]: arrivals 15/hr; gap under 3 min = 0.05 hr;
     P = 1 - e^-0.75 = 0.5276 style worked
12.9 graded refs: p4 39-43, A2 MCQ Q5, A2 A5 style, A2 B5, A2 B7, A2 C1, A2 D2.

================================================================================
L17  SAMPLING CONCEPTS AND STANDARD ERROR  (clt p001 to p005)
================================================================================

13.1 population and sample [p002]
    13.1.1 population: entire group; parameters mu, sigma
    13.1.2 sample: subset; statistics xbar, s
    13.1.3 why sampling: too large, costly, impossible to census
13.2 simple random sampling [p003]
    13.2.1 without replacement; every subset equally likely; diagram with a-j population
13.3 standard error [p004]
    13.3.1 SE = sigma / sqrt(n), the sd of the sample mean over repeated samples
    13.3.2 interpretation: precision of the estimate; larger n, smaller SE
13.4 the scaling law [p005]
    13.4.1 quadruple n -> halve SE (worked: lightbulbs sigma 100, n 25 -> 20; n 100 -> 10)
13.5 graded refs: clt 4-5 style; feeds every CLT numeric.

================================================================================
L18  CENTRAL LIMIT THEOREM  (clt p006 to p018)
================================================================================

14.1 the statement [p007, p008]
    14.1.1 sample means are approximately normal for n >= 30, whatever the population
          shape
    14.1.2 if the population is normal, any n works
    14.1.3 n < 30 with non-normal population: CLT does NOT apply
14.2 the distribution of the mean
    14.2.1 mean of Xbar = mu; sd of Xbar = sigma / sqrt(n); the SE shows up as the sd
14.3 the z transform with SE denominator [~]
    14.3.1 z = (xbar - mu) / (sigma / sqrt(n))
    14.3.2 the "average of n" template vs a plain normal question: ONLY the denominator
          differs; the classic mix-up, read twice
14.4 worked applications
    14.4.1 ATM wait [p011, p012 style]
    14.4.2 impurity [p013, p014, errata 6]: mean 4.0, sd 1.5, n = 50;
          P(3.5 < Xbar < 3.8): SE = 0.2121; z1 = -2.36, z2 = -0.94 (slide prints -0.4,
          typo); answer 0.1644
    14.4.3 LED sample [p015, p016]
    14.4.4 machine lives [p017, p018]: n = 9 but the population is normal, so exact
          normal applies, no CLT needed; the fallback reading
14.5 exact table selections appearing in the deck: 0.4909, 0.3264, 0.4641, 0.2257, 0.4772
14.6 graded refs: clt 5-18, and every "n items averaged" question.

================================================================================
L19  THEORY OF ESTIMATION, INTRODUCTION  (p5 p001 to p007, lt p001 to p015)
================================================================================

15.1 vocabulary [p003, p005]
    15.1.1 population parameter: mu, sigma^2, p
    15.1.2 statistic: xbar, S^2, p-hat
    15.1.3 estimator: the RULE (a random variable); estimate: the NUMBER
    15.1.4 sample space vs parameter space
15.2 point vs interval [p004]
    15.2.1 point: single value
    15.2.2 interval: a range; interval estimate = point estimate +/- margin
15.3 point estimation worked [p022]
    15.3.1 response times 180..240, n = 8: xbar = 1640/8 = 205 ms; name estimator AND
          estimate in the answer
15.4 proportion estimation [p023]
    15.4.1 p-hat = X/n = 465/500 = 0.93
15.5 CI shape [p024, boundary item]
    15.5.1 8.4 +/- 1.96 x (1.5/sqrt(25)) = 8.4 +/- 0.588 = (7.81, 8.99)
    15.5.2 z(0.025) = 1.96 for 95 percent; the CI machinery formally belongs to lecture
          25, kept because "interval estimation" is named in the MTE list
15.6 lt p031 to p039: the full CI block, OUT of MTE, read-only if CWS puts it back

================================================================================
L20-21  CHARACTERISTICS OF A GOOD ESTIMATOR  (p5 p008 to p021, lt p016 to p030)
================================================================================

16.1 unbiasedness [p009]
    16.1.1 definition: E(theta-hat) = theta
    16.1.2 bias = E(theta-hat) - theta
16.2 force unbiasedness with a constant [p016, p020]
    16.2.1 t3 = (2X1 + X2 + lambda X3)/3: E = (3+lambda)mu/3, set = mu -> lambda = 0
    16.2.2 T3 = (lambda X1 + X2 + X3)/3: E = lambda mu -> lambda = 1
    16.2.3 the pattern: make the coefficient sum equal to the divisor
16.3 consistency [p010, p011]
    16.3.1 convergence in probability
    16.3.2 two sufficient conditions: E(Tn) -> theta AND Var(Tn) -> 0
    16.3.3 why Xbar is consistent: E = mu always, Var = sigma^2/n -> 0 [p012]
16.4 efficiency [p013, p014]
    16.4.1 among unbiased estimators, smallest variance wins
    16.4.2 visual: same center, tighter spread
16.5 comparison set 1 [p015 to p018]
    16.5.1 t1 = (X1+..+X5)/5: E = mu, Var = sigma^2/5
    16.5.2 t2 = (X1+X2)/2 + X3: E = 2mu, BIASED, eliminated
    16.5.3 t3 after lambda = 0: E = mu, Var = 5 sigma^2/9
    16.5.4 sigma^2/5 < 5 sigma^2/9 -> best = t1
16.6 comparison set 2 [p019 to p021]
    16.6.1 T1 = X1 + X2 - X3: E = mu; Var = 3 sigma^2
    16.6.2 T2 = 2X1 + 3X3 - 4X2: E = mu; Var = (4 + 9 + 16) sigma^2 = 29 sigma^2
    16.6.3 T3 after lambda = 1: E = mu; Var = sigma^2/3
    16.6.4 best = T3; the protocol: filter unbiased FIRST, then min variance
16.7 sufficiency [lt p024, p025, the 2 unique items]
    16.7.1 idea: conditional distribution of the sample given T is free of theta
    16.7.2 Neyman-Fisher factorization: f = g(T, theta) x h(x)
    16.7.3 Poisson worked: join pmf -> e^-n lambda^T x prod 1/xi!; T = sum sufficient
    16.7.4 exponential worked: lambda^n e^-lambda n xbar; xbar sufficient
16.8 graded refs: p5 15-21, lt 24-25, A1 style, mock B4 (the T4 biased-low-variance trap).

================================================================================
H.  THE HIDDEN LAYER, complete (nothing here has a teaching slide)
================================================================================

[H1] independence rules of rvs: E(XY), Var(X+Y), Var(X-Y). Feeds Chebyshev sums,
     CLT variances, estimator variances, Poisson additivity. Graded already (A1 short 5)
[H2] Chebyshev entire topic: 5 graded uses. Sources: sheet E, bank 6, mock B1
[H3] memoryless property: 2 graded uses (A2 MCQ Q5, A2 C1). Sheet only
[H4] landmarks 68.27 / 95.45 / 99.73: 1 graded use (A2 A11). Sheet only
[H5] expected count N x P: graded (A2 B4, A2 D1) + slide usage (p3 p018). No slide rule
[H6] geometric E(N) = 1/p: graded (A1 short 4: E = 2 for p = 1/2). pmf taught, E not
[H7] hypergeometric mean nK/N: graded (A1 long 3: exactly 0.8 both cases). No slide
[H8] two-table discipline (phi vs F): every normal/CLT numeric question. Slides show
     both tables but never warn about the mix

================================================================================
S.  CROSS-CUTTING MICRO SKILLS (12 drills)
================================================================================

S1  complement turn: at least / none / more than / rejected -> 1 minus lower tail
S2  table discipline: identify convention, pick row, mind the sign
S3  exact powers: 0.9^10, 0.9^12, e^-2.5 without panic
S4  ratio recovery: equate two pmf expressions, cancel, solve
S5  N x P expected counts
S6  piecewise integration with correct limits, no double counting at breakpoints
S7  |expr| < c <=> interval; interval length over support length
S8  pmf sanity: sum = 1, admissible k
S9  cdf sanity: nondecreasing, 0 and 1 limits, jumps at atoms
S10 rounding discipline: exact until the final line (errata 3, 12)
S11 read the ask: at most / at least / between / inclusive / neither / exactly
S12 draw the curve and mark the area before computing

================================================================================
X.  ERRATA MAP (14 entries, full text in reports/09-ERRATA.md)
================================================================================

 1  p3 insurance: 0.1745 printed, 0.1755 correct
 2  p3 die sets: 0.549 printed, 0.5499 correct
 3  A1 key truncates 0.0915 (correct 0.0916)
 4  p4 p040 inverts lambda wording
 5  A1 long 2 normalisation 9k + 10k^2 = 1, root 1/10 (see 5.1: the untracked second
    edition prints a different row, 12k + 10k^2 = 1, and a key that does not satisfy it)
 6  clt impurity Z: -0.4 printed, -0.94 correct
 7  notation note: N(mu, sigma^2) is variance
 8  p4 p030 figure: sigma = 10 printed, 5.0 correct
 9  A2 B5: 0.5679 printed, 0.6225 correct
10  A2 C2: mu 37.5 printed, 37.2 correct; cutoff 30.43 -> 30.4
11  A1 long 3: 0.808 printed, 0.8 exact both cases
12  A1 app 3: sd chain 0.975/0.98; exact 0.9734 -> 0.97
13  bus example: working bound 3 vs event Y<2; final 0.40 correct; double equals sign
14  A2 C3: 0.8754 printed, 0.8753 exact

================================================================================
Z.  INVENTORY (locked)
================================================================================

teaching items 60 (55 unique) | assignments 52 | total 112, 107 unique
deck01 30 | p3 6 | p4 7 | clt 5 | p5 5 | lt 7 (2 unique)
excluded: MLE 16 pp, MoM 11 pp, handout 7 pp, lt CI block 10 pp
