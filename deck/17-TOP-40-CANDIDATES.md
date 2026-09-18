# 17 TOP 40: the MTE candidates most likely to come (built Fri 18 Sep 2026)

Both question banks recognized, cross-read, and ranked into one drill set.
Questions only. No answers anywhere in this file on purpose.

## The two banks, recognized

```
  repo bank  (github.com/harshgounder/mas2001-mte)       168 [H]  machine-verified numbers
  your bank  (~/Music/SNP-MTE-MASTER-ALL-QUESTIONS.md)   159 [Y]  reproduced as-is
  union                                                  284 unique problems
  in both banks (same problem, both solution routes)      43 [HY]
```

- Overlap by topic, the double-confirmed families: density/cdf mechanics 6, estimation 6,
  foundations 5, Chebyshev 5, Poisson 5, sampling/CLT 4, assignment extras 4.
- The setter's habit, measured (reports/20-SKELETON-LEDGER.md): structure stays fixed, the
  constants move. Telephone parameter: 5 -> 6 -> 4 -> 3 across four appearances. Uniform
  Chebyshev interval: (-1,3) -> (-1,1). Trains at the station: every 30 -> every 15 min.
  "Bread-making machine" -> "a machine". Expect NEW numbers on the same bones.
- Cross-year repeats (the dead certs): Chebyshev (9+ graded uses), exponential phone (both
  MTE years), Poisson (both), normal (both: the 2024 composite and the 2025 sample-mean), density mechanics (both: the 2024 triangular CDF and the 2025 kx^3 find-k).
- Your bank's own 2 predicted papers (18 items) independently pick the same core: Chebyshev
  bounds, normal z-tables, SE/CLT, estimation unbiasedness, Poisson process questions.
  Green flag for the ranking below.
- Package notes: the intro counts 44 merged pairs, the file itself holds 43; "predicted paper
  1 B2" sits misfiled in section 01; the [Y] side solutions were reproduced, not re-verified.

Tiers: `***` family seen on both MTE years or 4+ sources (paper almost surely uses these);
`**` one real year or 3+ sources; `*` bank-only or the next mutation of a seen family.

Refs like `bank 03·003` point into `SNP-MTE-QUESTIONS-ONLY-ALL.md` (section · item).

## A. Section A: MCQ candidates (2 marks each), 14 questions

**A1 `***` Chebyshev forms.** If X is a random variable with mean mu and variance sigma^2 and K is any positive number, then which of the following is/are NOT the Chebyshev's inequality?
(a) P{|X - mu| >= k sigma} <= 1/k^2
(b) P{|X - mu| < k sigma} >= 1 - 1/k^2
(c) P{|X - mu| >= k} <= k^2/sigma^2
(d) P{|X - mu| < k sigma} >= sigma^2/k^2
evidence: real 2024-25 A3 · assignment-1 MCQ5 + MCQ10 (applicability form) · hidden item H2.

**A2 `***` Random variable definition.** A random variable is:
(a) a constant value (b) a probability (c) a function from the sample space to the real numbers (d) an event.
Also its sibling: a discrete random variable takes a COUNTABLE number of values.
evidence: asked three times (ETE 2025-26 S4 A1, ETE summer Q1, ETE re-sess S4 A1) · bank 01·001.

**A3 `***` Density definition.** If f(x) is the probability density function of a continuous random variable, then the integral from -inf to +inf of f(x) dx = ___
1) 0 2) 1 3) -1 4) infinity.
(Twin form: which statement is TRUE: f(x) can never exceed 1 / P(X=x)=f(x) / the integral equals 1 / P(a<X<b)=f(b)-f(a).)
evidence: real 2025-26 Q1 (first question on the paper) · bank 09·012 · bank predicted paper 1 A1.

**A4 `***` Expectation and variance laws.** If E(X) = 4 and Var(X) = 2, then E(3X - 5) and Var(3X - 5) are
(a) 7 and 18 (b) 7 and 6 (c) 17 and 18 (d) 12 and 2.
Twin (real 2024-25 form): X is Poisson with mean 0.5, Y = 2X. Which are correct? (i) E(Y)=1 (ii) Var(Y)=4 (iii) Var(Y)=2 (iv) E(Y)=2.
evidence: real 2024-25 A1 · bank 02·003 · bank predicted paper 2 A1 · A2 MCQ block.

**A5 `**` Poisson substitution drill.** In a Poisson distribution, if mean = e, then p(x) is given by
1) e^(x-e)/x! 2) e^(e-x)/x! 3) x!/e^(x-e) 4) x!/e^(e-x).
evidence: real 2025-26 Q2 · bank 05·008.

**A6 `**` Unbiased estimator definition.** A statistic T is said to be an unbiased estimator of the parameter theta if
(a) E(T) = theta (b) Var(T) = 0 (c) E(T) = 0 (d) T = theta for every sample.
evidence: bank predicted paper 1 A3 · ETE 2025-26 S3 A2 (MCQ form) · M25 Q8(ii) context.

**A7 `**` Sufficiency definition.** A statistic is sufficient for a parameter if
1) it minimizes the sample variance 2) it contains all the information needed about the parameter 3) it is always unbiased 4) it is equal to the sample mean.
evidence: real 2025-26 Q3 · bank 11·013.

**A8 `**` Standard error formula.** The standard error of the sample mean, for a sample of size n from a population with standard deviation sigma, is
(a) sigma (b) sigma/n (c) sigma/root n (d) sigma^2/n.
evidence: bank predicted paper 2 A3 · CLT deck SE drill · ETE MCQ forms.

**A9 `**` Memoryless property.** The memoryless property belongs to
(a) uniform (b) normal (c) exponential (d) binomial.
evidence: A2 MCQ5 (real assignment) · bank 08·009 · hidden item H3.

**A10 `**` Normal landmarks.** For a normal distribution, the percentage of values within 1, 2 and 3 standard deviations of the mean are respectively
(a) 65, 90, 99 (b) 68, 95, 99.7 (c) 70, 95, 99.9 (d) 68, 90, 99.7.
evidence: A2 MCQ11 (real assignment) · bank 12·049 · hidden item H4.

**A11 `*` Exponential moments.** For an exponential random variable with mean 8, the standard deviation is
(a) 8 (b) 64 (c) 1/8 (d) 2 root 2.
evidence: bank predicted paper 2 A2 · bank 08·011.

**A12 `**` Discrete RV spot-check.** Which of the following is a discrete random variable?
A) height of students B) time taken to complete an exam C) number of defective bulbs in a box D) temperature of a city.
evidence: assignment-1 MCQ (real assignment) · both banks merged.

**A13 `**` CDF definition.** The cumulative distribution function (CDF) of a random variable is
A) P(X=x) B) P(X<=x) C) P(X>=x) D) P(X>x).
evidence: assignment-1 MCQ (real assignment) · both banks merged.

**A14 `**` Standard normal moments.** For a standard normal variate, the mean and the variance are respectively
(a) 0 and 0 (b) 0 and 1 (c) 1 and 0 (d) 1 and 1.
evidence: ETE 2025-26 S3 A5 (mean alone) · bank 07·016 + 07·017 · hidden item H4.

## B. Section B: 4-mark candidates, 16 questions

**B1 `***` Chebyshev, find the constant.** A random variable X has mean 10 and variance 4. Using Chebyshev's inequality, find the value of the constant c such that P(|X - 10| >= c) <= 0.04.
Twins: lower-bound form with mean 20, variance 16 (find a bound for P(10 < X < 30)); mean 100, sd 5 (bound for P(80 < X < 120)); inverse form P(-2 < X < 8) >= 21/25, find E(X) and Var(X).
evidence: real 2025-26 Q5 (deck Q2(iv) verbatim) · bank 03·003 + predicted papers 1 B1, 2 B1 · bank 03·004.

**B2 `***` Chebyshev bound vs exact.** X = the sum of two dice. Prove P(|X - 7| >= 3) <= 35/54, then compare with the actual probability.
Twin: a symmetric die thrown 600 times, lower bound for P(80 to 120 sixes).
evidence: assignment-1 short5 (real assignment) · bank 12·021 + 12·022 · real 2024-25 B3 family.

**B3 `***` Telephone exponential.** The length of a telephone conversation is exponentially distributed with a mean of 3 minutes. Find the probability that a call (i) ends in more than 1 minute (ii) takes less than 3 minutes.
Twin (2024-25 form): parameter 1/4, find P(more than 6 min), P(between 7 and 12 min), P(not more than 5 min), mean and variance.
evidence: real 2025-26 Q6 + real 2024-25 B2 (both years) · bank 08·005 + 08·006.

**B4 `***` Poisson variance of a combination.** X and Y are independent Poisson variates with P(X=1) = P(X=2) and P(Y=2) = P(Y=3). Find the variance of X - 2Y.
evidence: real 2024-25 B1 (verbatim from the standard book) · bank 05·007.

**B5 `***` Normal sample mean.** The average life of a machine is 7 years with a standard deviation of 1 year. Lives are normal. Find the probability that the average life of 9 sampled machines falls between 6.4 and 7.2 years. Given phi(1.8) = 0.4641, phi(0.6) = 0.2257.
evidence: real 2025-26 Q7 (a lecture-slide example first) · bank 07·012.

**B6 `**` Normal z-table direct.** Marks in a test are normally distributed N(40, 10). Find the probability that a student scored (i) more than 55 (ii) between 25 and 55. Given phi(1.5) = 0.4332.
evidence: bank predicted paper 1 B3 · deck normal-chain examples · bank 07·017 (area between z = -1 and 1).

**B7 `**` Density find-k plus moments.** A random variable X is distributed between 0 and 4 with pdf f(x) = k x^3 (4 - x)^2. Find k. Using that k, find the mean and the variance.
evidence: real 2025-26 Q4 · bank 09·013 · ABES sample paper cross-check.

**B8 `***` Uniform train wait.** Trains arrive at a station at 15-minute intervals starting at 4 AM. A passenger arrives at a time uniformly distributed between 9:00 AM and 9:30 AM. Find the probability he waits (a) less than 6 minutes (b) more than 10 minutes.
evidence: real 2024-25 B4 · bank 06·003 · the classic subway parent problem.

**B9 `**` PMF find-k with a quadratic twist.** A random variable X has the distribution: P(0)=0, P(1)=k, P(2)=2k, P(3)=2k, P(4)=3k, P(5)=k^2, P(6)=2k^2, P(7)=7k^2 + k. (i) Find k. (ii) Find P(1.5 < X < 3.5). (iii) Find the distribution function.
evidence: ETE summer Q12 + its own B1 repeat (asked twice) · bank 01·003.

**B10 `***` Binomial, mean fixed.** X follows a binomial distribution with mean 5/3 and P(X=1) = P(X=2). Find the variance, P(X >= 1) and P(X <= 1).
evidence: real 2024-25 C1 part (b) · bank 04·009.

**B11 `***` Pens and defectives.** 10% of pens manufactured are defective. A box contains 12 pens. Find the probability that the box contains (i) exactly 2 defective pens (ii) at least 2 defective pens (iii) no defective pen.
evidence: assignment-1 + ETE 2025-26 S3 B2 (asked verbatim) · bank 04·001 · both banks merged.

**B12 `**` Estimator comparison, short form.** X1, X2, X3 is a sample from a population with mean mu and variance sigma^2. Two estimators: T1 = (X1 + 2X2 + X3)/4 and T2 = (2X1 + X2 + 3X3)/6. (a) Are T1 and T2 unbiased? (b) Which is the better estimator, and on what ground?
evidence: bank predicted paper 2 B4 · LMS theory deck · assignment set.

**B13 `**` Poisson approximation, typist.** A typist types on average 20 letters per day of about 200 words each. Find the chance of her making a mistake (i) if less than 1% of the letters submitted are rejected (ii) if on 90% of days all letters are accepted (e = 2.72).
evidence: real 2025-26 Q8 part (i), 5 marks · siblings: car hire mean 1.5 (bank 05·005), the 5,000-men insurance (bank 05·006).

**B14 `**` Memoryless conditional.** Repair time for a watch is exponential with lambda = 1/2. (i) P(repair exceeds 2 hours) (ii) P(it takes more than 11 hours given it has already exceeded 8 hours).
Twin: hardware time-to-failure exponential mean 1000 h, P(survive >= 1500 | survived 500).
evidence: A2 section C1 + A2 MCQ5 (real assignment, asked twice) · bank 05·003 + 08·002 · hidden item H3.

**B15 `**` Normal, two unknowns.** In a distribution exactly normal, 10% of items are under 30 and 85% are under 65. Find the mean and the standard deviation. Given phi(1.04) = 0.35, phi(1.28) = 0.4.
Twin: 46% pass, 9% distinction, pass mark 40, distinction 75; find mu, sigma, then the re-examination cutoff (best 25% of failures).
evidence: A2 C2 family + assignment bank 2024-25 · bank 07·005 + 07·003.

**B16 `**` N x P count.** The life of a bulb is N(3000, 400^2). 10,000 bulbs are bought. How many last between 2500 and 3500 hours?
Twin: 5,000 batteries N(1500, 100), number expected between 1400 and 1600.
evidence: A2 section D1 + bank predicted paper 2 B3 · bank 12·017 · hidden item H5.

## C. Section C: the long block (8 marks, came as one composite in 2024-25 and as a 5+3 pair in 2025-26), 10 questions

**C1 `***` Normal plus binomial composite.** In a university, 2,000 students took a test, marks N(50, 10). Find the number of students who scored (i) below 35 (ii) above 70 (iii) between 40 and 60. (iv) Find the probability that exactly 3 out of 5 randomly chosen students scored between 40 and 60. Given phi(1.5) = 0.4332, phi(2) = 0.4772, phi(1) = 0.3413.
evidence: bank predicted paper 2 C1 · the 2024-25 real C1 is the same architecture (rain N(2.6, 34.5) + a week/binomial tail) · bank 14·016.

**C2 `***` Estimator tournament.** X1, X2, X3 is a sample of size 3 with mean mu, variance sigma^2. T1 = X1 + X2 - X3, T2 = 2X1 + 3X3 - 4X2, T3 = (lambda X1 + X2 + X3)/3. (1) Check unbiasedness of T1 and T2. (2) Find lambda so T3 is unbiased. (3) Is T3 consistent? (4) Which is the best estimator?
evidence: LMS theory-of-estimation Example 2 · bank 11·008 · the ETE 10-mark form exists · ppt5.

**C3 `***` Show-that pack (the 5+3 halves).** (i) Show the sample mean x-bar is an unbiased estimator of mu and find its variance in terms of sigma^2 and n. (ii) If t is an unbiased estimator of theta, show that t^2 is a biased estimator of theta^2. (iii) If X ~ B(n, p), show that p-hat = X/n is an unbiased estimator of p.
evidence: real 2025-26 Q8 part (ii) for (ii) · bank predicted p1 C2 + p2 C2 for (i) and (iii) · bank 11·006.

**C4 `**` Poisson process, three parts.** Calls arrive at a help desk per Poisson at 4 per minute. Find the probability that in a given minute there are (i) exactly 6 calls (ii) at least 1 call (iii) more than 6 calls.
evidence: bank predicted paper 1 C1 (bank 14·007) · Poisson process family with the typist block and the emails item.

**C5 `***` N x P expected count.** The lifetimes of 5,000 batteries are N(1500, 100). Find the number of batteries expected to last between 1400 and 1600 hours. Given phi(1) = 0.3413.
evidence: bank predicted paper 2 B3 · A2 D1 twin · bank 12·017 · hidden item H5.

**C6 `**` Two-unknown normal plus a percentile.** In an exam 46% of students passed and 9% got a distinction; pass mark 40, distinction mark 75; marks normal. Find mu and sigma. Then: find the minimum qualifying marks for re-examination if the best 25% of the FAILED candidates get another chance. Given phi(0.1) = 0.04, phi(1.34) = 0.41, phi(0.24) = 0.095.
evidence: bank 07·003 · A2 C2 family · ETE S4 2024-25 B4.

**C7 `**` Chebyshev inverse composite.** The mean of a distribution is 70 and variance is 25. Find the minimum proportion of observations that lie between 60 and 80, using Chebyshev's inequality.
Twin: P(4 < X < 16) >= 24/25, find E(X) and Var(X).
evidence: assignment-1 app4 (real assignment) · bank 03·001 · ETE S4 B3 twin.

**C8 `**` Poisson to exponential wait.** Buses arrive at a terminal per Poisson with an average rate of 5 per hour. Find the probability that (i) the waiting time for the next bus is less than 12 minutes (ii) the waiting time exceeds 30 minutes.
evidence: bank predicted paper 2 B2 · real 2025-26 Q6 family · A2 D2 unit-conversion twin.

**C9 `**` Piecewise density composite.** A random variable X has density f(x) = x for 0 < x <= 1, f(x) = 2 - x for 1 <= x <= 2, 0 otherwise. (i) Verify this is a probability density. (ii) Find the distribution function on both intervals. (iii) Find P(0.5 < X < 1.5).
evidence: real 2024-25 A2 (MCQ form, asked as the CDF piece) · bank 09·015 · density twins: power pdf f(x) = (1/9) x e^(-x/3), P(supply inadequate) (bank 09·003).

**C10 `**` Find-lambda estimator set.** X1..X5 from a normal population with mean mu. Three estimators: t1 = (X1+...+X5)/5, t2 = (X1 + X2)/2 + X3, t3 = (2X1 + X2 + lambda X3)/3 with lambda chosen for unbiasedness. (1) Find lambda. (2) Check t1, t2 for unbiasedness. (3) Which is the best estimator?
evidence: LMS theory-of-estimation Example 1 · bank 11·007 · same family as C2.

## Marks coverage

```
  THE EXAM SHAPE: 30 marks, 90 min, closed book, calculator allowed
  ┌──────────┬────────────┬─────────────────┬──────────────────────────────────────┐
  │ section  │ per paper  │ marks           │ this file's candidates               │
  ├──────────┼────────────┼─────────────────┼──────────────────────────────────────┤
  │ A (MCQ)  │ 3          │ 3 x 2 = 6       │ 14 candidates (A1..A14)              │
  │ B        │ 4          │ 4 x 4 = 16      │ 16 candidates (B1..B16)              │
  │ C        │ 1 block    │ 8 (5+3 split)   │ 10 candidates (C1..C10)              │
  │ total    │ 8          │ 30              │ 40                                   │
  └──────────┴────────────┴─────────────────┴──────────────────────────────────────┘

  TOPIC COVERAGE OF THE 40 (every in-scope block has candidates):
    foundations / definitions ............ A2, A12, A13
    density mechanics / cdf .............. A3, B7, B9, C9
    expectation + variance laws .......... A4, B4, C2
    Chebyshev ............................ A1, B1, B2, C7
    binomial ............................. B10, B11, C1(iv)
    Poisson .............................. A5, B4, B13, C4
    uniform .............................. B8
    normal ............................... B5, B6, B15, B16, C1, C5, C6
    exponential .......................... A11, B3, B14, C8
    sampling / SE ........................ A8, B5, C5
    estimation ........................... A6, A7, B12, C2, C3, C10
    hidden layer (H1..H8) ................ A9, A10, B16, C3
    composites ........................... C1..C10

  MOST LIKELY SINGLE FILLS (one guess per slot, from the tiers):
    A (3 slots):  A1 Chebyshev forms / A3 density def / A4 or A6 (laws or estimation def)
    B (4 slots):  B1 Chebyshev + B3 exponential + B4 Poisson + one of B5/B7/B8/B10
    C (1 block):  C1 normal+binomial composite or C2/C3 estimation (the 5+3 split)
```

Drill order for today: the `***` tier first (16 questions), then the `**` tier (23), then the one `*` (A11), plus any question you fail twice. Attempt before reading any solution. Full papers for timing practice: reports/07-MOCK-PAPER-v2.md and the two real MTE papers.

## Self-audit (18 Sep): is this really the top 40, and what does it buy you

```
  EVIDENCE CLASSES OF THE 40 (every item checked):
    traces to a prior MTE paper item or its verbatim family    17
    graded course material (assignments, ETE, deck examples)   19
    bank-only (the softest entries: A11, B6, C4, C8)            4

  THE LIST RE-MAPPED AGAINST THE TWO REAL PAPERS:
    MTE 2025-26: 8 of 8 slots land in the set
                 (Q1->A3, Q2->A5, Q3->A7, Q4->B7, Q5->B1, Q6->B3, Q7->B5, Q8->B13+C3)
    MTE 2024-25: 6 direct + 2 inside families = 7 of 8
                 (the triangular-CDF MCQ sits inside C9; the uniform bound-vs-exact
                  sits inside the B2/C7 family)

  WHY THE PAPER LIKELY RETURNS TO THIS SET: both years drew 5-6 of the 8 slots from
  the core families (Chebyshev, exponential, Poisson, normal, density mechanics,
  estimation). The other 2-3 slots rotate among uniform, binomial, hidden items and
  composites. The 40 hold the core in depth and every rotation seen so far.

  A DRILL-ONLY RUN, WHAT IT LIKELY SCORES (an estimate with the method shown, not a
  measured probability; a covered slot pays full marks for a drilled student):
    per slot: P(covered) ~ 0.9 core / ~ 0.6 known rotation / ~ 0.3 field
    scenario table, 30 marks:
      the core + a known rotation, no surprises ....... 27-29  (~92%)
      normal rotation, 4 core slots + 4 moves ......... 23-26  (~78-85%)
      heavy rotation, 3+ slots outside everything ..... 19-22  (~63-73%)
    central estimate for a clean drill: 23-25 / 30.

  BENCH: the five that just missed (add these, about 30 minutes total):
    geometric E = 1/p (H6) | hypergeometric mean nK/N (H7) | Poisson additivity (A2 A12)
    | the triangular-CDF MCQ form (M24-A2) | the discrete conditional sibling

  CAVEATS, stated: one setter so far, a two-paper history, tiers are evidence-weighted
  judgment and not a calibrated probability. A paper from a different faculty pool
  shifts the odds; the bench plus 12-DRILL covers most of that shift.
```

Built from: SNP-MTE-MASTER-ALL-QUESTIONS.md + SNP-MTE-QUESTIONS-ONLY-ALL.md (the Music package), your repo deck/worked + one-by-one, reports/20-SKELETON-LEDGER.md, reports/11-QUESTION-ATLAS, deck notes. Numbers follow the source files as printed.
