# F15 ASSIGNMENT BANK 2: the 2024-25 and 2025-26 question sets

Source: our own assignment PDFs (the 2024-25 sheets 1-2 and the 2025-26 sheets 1-2, text
extraction at ~/mas2001-mte-audit-v1/text/asgn-*). These are DIFFERENT questions from F13
(which covered Assignment-1 and Assignment-2 of the CURRENT course handout). Nothing
invented: every question is quoted from the sheets, every printed answer re-verified with a
machine script.

```
  SHAPES IN THIS FILE
  F15.1  expectation tricks       E(good) hypergeometric, Z=2X-5Y, salesperson, hospitalization
  F15.2  find-k + densities       kx^2(1-x^3), cdf-to-pdf, pdf-from-cdf (two forms)
  F15.3  count questions          packets (binomial vs poisson), wireless sets, library copies
  F15.4  conditional + memoryless repair times, tube lives, shelf products
  F15.5  normal count extras      bulbs 2040, students 79, mid-class 900, washers, elevator
  F15.6  uniform extras           U(-a,a) find-a, string cutting, U[-3,3] parts
  F15.7  misc drill               keys problem, Y=X^2+2X distribution, radio tubes
  F15.8  the printed-answer flags found (read this)
```

═══════════════════════════════════════════════════════════════════════════════
F15.1  EXPECTATION TRICKS
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 1 (asgn 2025-26 #1 Q6 - the quality inspector's hypergeometric)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A lot of 7 components: 4 good, 3 defective. A sample of 3 is taken (without
   replacement). Find the expected number of GOOD components.  (sheet: 1.7)
```

STEP 0: DECODE - "expected number of good components in a sample drawn from a lot" = the
hypergeometric mean. The shortcut: E = n x (K/N).

EVERY STEP:

```
  STEP 1  identify: N = 7 (the lot), K = 4 (goods), n = 3 (the sample).
  STEP 2  the hypergeometric expectation formula: E(X) = n x K/N
  STEP 3  E = 3 x 4/7 = 12/7 = 1.7143
```

ANSWER: 1.714 (the sheet prints 1.7; the exact value is 12/7).

THE INTUITION (why n x K/N works): each of the 3 sampled items has a 4/7 chance of being
good at the moment it is drawn; expectations add regardless of dependence.

TRAP: this is NOT binomial (no replacement). The binomial mean np = 3 x (4/7) gives the
same number here, which hides the difference: the VARIANCE differs
(hypergeometric: finite-population correction).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 2 (asgn 2025-26 #1 Q11 - the Z = 2X - 5Y linear combination)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   X and Y independent with means 2, 3 and variances 1, 2. Find the mean and variance of
   Z = 2X - 5Y.  (sheet: -11, 54)
```

EVERY STEP:

```
  STEP 1  E(Z) = 2E(X) - 5E(Y) = 2(2) - 5(3) = 4 - 15 = -11
  STEP 2  Var(Z) = 2^2 Var(X) + (-5)^2 Var(Y) = 4(1) + 25(2) = 4 + 50 = 54
          (independence lets us ADD variances; the minus sign VANISHES in the square.)
```

ANSWER: mean -11, variance 54.

TRAP: writing Var(Z) = 4 - 25(2) = -46. The sign disappears because variances always add
(under independence) with SQUARED coefficients.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 3 (asgn 2025-26 #1 Q15 - the salesperson's expected commission)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   First appointment: 70% chance of a $1000 deal. Second: 40% chance of $1500.
   Independent. Expected total commission?  (sheet: $1300)
```

EVERY STEP:

```
  STEP 1  expected from the first: 0.70 x 1000 = 700
  STEP 2  expected from the second: 0.40 x 1500 = 600
  STEP 3  expectations ADD: 700 + 600 = 1300
          (the independence note is a distractor here; linearity of expectation needs no
           independence at all.)
```

ANSWER: $1300.

TRAP: trying to weight by joint probabilities ("what if both fail..."). Expectation via
linearity handles all four joint outcomes at once.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 4 (asgn 2025-26 #1 Q16 - the hospitalization shift)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Hospitalization period Y = X + 4 where X has density 32/(x+4)^3 for x > 0.
   Find the average number of days hospitalized.  (E(X) = 4)
```

EVERY STEP:

```
  STEP 1  first find E(X): the integral of x f(x)
          E(X) = 32 int_0^inf x/(x+4)^3 dx
          substitute u = x+4: 32 int_4^inf (u-4) u^-3 du
          = 32 [ (1/4) - 2/16 ] = 32 x 1/8 = 4
          so E(X) = 4.
  STEP 2  Y = X + 4 shifts the expectation: E(Y) = E(X) + 4 = 8.
```

ANSWER: 8 days on average.

TRAP: integrating for E(Y) directly (more work). The shift rule E(X+c) = E(X) + c is the
whole question.

═══════════════════════════════════════════════════════════════════════════════
F15.2  FIND-K AND DENSITIES
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 5 (asgn 2025-26 #1 Q9 - kx^2(1 - x^3), k = 6)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   f(x) = k x^2 (1 - x^3) on 0 to 1. Find k, then the mean and variance.
   (sheet: 6, 9/14, 9/245)
```

EVERY STEP:

```
  STEP 1  total = 1:
          int_0^1 k(x^2 - x^5) dx = k[1/3 - 1/6] = k/6 = 1  ->  k = 6
  STEP 2  mean: int_0^1 6(x^3 - x^6) dx = 6[1/4 - 1/7] = 6(3/28) = 18/28 = 9/14 = 0.6429
  STEP 3  E(X^2): int_0^1 6(x^4 - x^7) dx = 6[1/5 - 1/8] = 6(3/40) = 18/40 = 9/20 = 0.45
  STEP 4  variance = 9/20 - (9/14)^2 = 9/20 - 81/196 = (441 - 405)/980 = 36/980 = 9/245
                  = 0.03673
```

ANSWER: k = 6, mean = 9/14, variance = 9/245. (all three machine-verified in exact fractions)

TRAP: expanding kx^2(1 - x^3) correctly: the exponent jumps (x^3 and x^6 for the mean).
Missing the 1/7 or 1/8 term wrecks everything downstream.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 6 (asgn 2025-26 #1 Q10 - pdf from a cdf with the (x-1)^4 form)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   F(x) = (x-1)^4 / 16 on [1,3] (0 below, 1 above). Find the density and P(2 <= x <= 3).
   (sheet: 15/16)
```

EVERY STEP:

```
  STEP 1  the density is the DERIVATIVE of the cdf:
          f(x) = d/dx[(x-1)^4/16] = 4(x-1)^3/16 = (x-1)^3/4 on [1,3]
  STEP 2  P(2<=x<=3) = F(3) - F(2) = (2^4)/16 - (1^4)/16 = (16-1)/16 = 15/16
```

ANSWER: f(x) = (x-1)^3/4; the probability is 15/16.

TRAP: integrating the density again instead of using F directly. When the CDF is given,
P(a<=X<=b) = F(b) - F(a), one subtraction.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 7 (asgn 2024-25 #1 Q11 - pdf from a piecewise cdf)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   F(x) = 0 (x<0); x/2 (0<=x<1); 1/2 (1<=x<2); x/4 (2<=x<4); 1 (x>=4).
   Find the probability density function.  (sheet: 1/2, 0, 1/4, 0)
```

EVERY STEP:

```
  STEP 1  differentiate each branch where it has slope:
          x<0:     f = 0
          0<=x<1:  d/dx (x/2) = 1/2
          1<=x<2:  d/dx (1/2) = 0     (flat: no density)
          2<=x<4:  d/dx (x/4) = 1/4
          x>=4:    f = 0
  STEP 2  assemble the piecewise density:
          f(x) = 1/2 for 0<x<1; 1/4 for 2<x<4; 0 elsewhere
```

ANSWER: f(x) = 1/2 on (0,1), 1/4 on (2,4), 0 otherwise. (check: 1/2 + 1/4 x 2 = 1 ✓)

TRAP: the flat piece (1<=x<2) contributes a JUMP in the cdf, not density mass. Its density
is 0; do not invent a value there. Also: a cdf can have steps for continuous-in-pieces
mixtures; for pure continuous rv the jumps would be absent.

═══════════════════════════════════════════════════════════════════════════════
F15.3  COUNT QUESTIONS (the multiply-by-group layer)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 8 (asgn 2025-26 #1 Q26 - defected items: binomial AND poisson approximation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   p = 0.05 defective. Packets of 20. In 1000 packets, find the number containing
   (a) exactly 2 defective (b) at least 2 (c) at most 2, using
   (i) the binomial (ii) the poisson approximation.  (sheet: 189, 264, 925 / 184, 264, 920)
```

EVERY STEP (the binomial route):

```
  STEP 1  X ~ B(20, 0.05) per packet.
  STEP 2  exactly 2: C(20,2)(0.05)^2(0.95)^18 = 190 x 0.0025 x 0.3972 = 0.1887
          count = 1000 x 0.1887 = 189
  STEP 3  P(0) = 0.95^20 = 0.3585 ; P(1) = 20(0.05)(0.95)^19 = 0.3774
          at least 2 = 1 - 0.3585 - 0.3774 = 0.2641  -> count 264
  STEP 4  at most 2 = 0.3585 + 0.3774 + 0.1887 = 0.9246  -> count 925
```

EVERY STEP (the poisson route):

```
  STEP 5  lambda = np = 20 x 0.05 = 1
  STEP 6  exactly 2 = e^-1/2 = 0.1839 -> 184
          at least 2 = 1 - e^-1(1 + 1) = 1 - 0.7358 = 0.2642 -> 264
          at most 2 = e^-1(1 + 1 + 0.5) = 0.9197 -> 920
```

ANSWER: binomial (189, 264, 925); poisson (184, 264, 920). All six verified exactly.

TRAP: forgetting the 1000-packet multiplier. And note how CLOSE the two routes land (the
poisson approximation is excellent at n=20, p=0.05).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 9 (asgn 2025-26 #2 Q36 - wireless sets, the joint-count)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   25 soldered joints per set, 1 in 500 defective. How many sets (of 10000) free of
   defective joints?  (sheet: 9512)
```

EVERY STEP:

```
  STEP 1  per set: n = 25 joints, p = 1/500 = 0.002.
          lambda = np = 25/500 = 0.05
  STEP 2  P(a set is clean) = e^-0.05 = 0.9512
  STEP 3  count = 10000 x 0.9512 = 9512
```

ANSWER: 9512 sets.

TRAP: using the binomial exactly: (1-0.002)^25 = 0.9512, the same to 4 decimals. Either
route works; the poisson is faster.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 10 (asgn 2025-26 #2 Q32 - the library copies, inverse-normal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   400 students, each needs a book with p = 0.1 on any day. How many copies so that
   P(no student disappointed) > 0.95? (normal approximation)  (sheet: 50)
```

EVERY STEP:

```
  STEP 1  X ~ B(400, 0.1): mean = 40, variance = 400 x 0.1 x 0.9 = 36, sd = 6.
  STEP 2  want c with P(X <= c) >= 0.95.
          standardise: z = (c - 40)/6 and find the z with cumulative 0.95:
          z = 1.645 (area-from-mean 0.45)
  STEP 3  c = 40 + 1.645 x 6 = 40 + 9.87 = 49.87 -> 50 (copies come in whole numbers)
```

ANSWER: 50 copies.

TRAP: rounding DOWN to 49 fails the 0.95 requirement; always round UP for a coverage
requirement. And the word "greater than 0.95" makes c the 95th percentile.

═══════════════════════════════════════════════════════════════════════════════
F15.4  CONDITIONAL + MEMORYLESS
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 11 (asgn 2024-25 #2 Q14 and asgn 2025-26 #2 Q19 - repair times, lambda given)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Repair time exponential, lambda = 1/2 (sheet #14). (a) P(repair exceeds 2h).
   (b) P(takes at least 10h | duration exceeds 9h).  (sheet: 0.3679, 0.6065)
   [the 2025-26 sheet states lambda = 2 but prints the same answers, which belong to
    lambda = 1/2; see F15.8]
```

EVERY STEP (with lambda = 1/2, the consistent reading):

```
  STEP 1  (a) P(X > 2) = e^(-0.5 x 2) = e^-1 = 0.3679
  STEP 2  (b) memoryless: P(X > 10 | X > 9) = P(X > 1) = e^-0.5 = 0.6065
```

ANSWER: 0.3679 and 0.6065.

TRAP: the second part is the memoryless property: subtract the ages (10 - 9 = 1), then
e^(-lambda x 1). The conditional probability of surviving 10 given 9 = surviving 1 more.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 12 (asgn 2025-26 #1 Q7 - three shelf-life products, the product rule)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Shelf life f(x) = e^-x for x > 0. THREE containers, independent.
   Find P(X1 < 2, 1 < X2 < 3, X3 > 2).  (sheet: 0.0372)
```

EVERY STEP:

```
  STEP 1  one-container pieces:
          P(X < 2) = 1 - e^-2 = 0.8647
          P(1 < X < 3) = e^-1 - e^-3 = 0.3679 - 0.0498 = 0.3181
          P(X > 2) = e^-2 = 0.1353
  STEP 2  independence multiplies: 0.8647 x 0.3181 x 0.1353 = 0.0372
```

ANSWER: 0.0372.

TRAP: the three containers are DIFFERENT conditions; do not use the same probability
three times. And the product needs all three (AND).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 13 (asgn 2025-26 #1 Q14 - radio tubes, four parts)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Tube life f(x) = 100/x^2 for x >= 100.
   (i) all 3 tubes replaced during first 150h (ii) none of 3 replaced (iii) a tube lasts
   < 200h given it is still on after 150h (iv) max tubes so P(all alive at 150h) = 0.5.
```

EVERY STEP:

```
  STEP 1  one tube: P(X < 150) = 1 - 100/150 = 1/3 ; P(X > 150) = 2/3.
  STEP 2  (i) all three die early: (1/3)^3 = 1/27 = 0.0370
  STEP 3  (ii) none die: (2/3)^3 = 8/27 = 0.2963
  STEP 4  (iii) P(X<200 | X>150): 
          P(150 < X < 200)/P(X>150) = (100/150 - 100/200)/(100/150)
          = (2/3 - 1/2)/(2/3) = (1/6)/(2/3) = 1/4 = 0.25
  STEP 5  (iv) (2/3)^n = 0.5 -> n = ln(0.5)/ln(2/3) = 1.7095
          the largest whole n = 1. (the sheet prints 1.7; as a COUNT it is 1 tube)
```

ANSWER: (i) 1/27 (ii) 8/27 (iii) 1/4 (iv) n = 1 (the continuous solution is 1.71).

TRAP: part (iii) is a conditional on SURVIVAL: numerator P(150<X<200), denominator
P(X>150). And part (iv) asks for a whole number; 2 tubes fail the 0.5 requirement
((2/3)^2 = 0.444 < 0.5).

═══════════════════════════════════════════════════════════════════════════════
F15.5  NORMAL COUNT EXTRAS
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 14 (asgn 2025-26 #2 Q17 - electric bulbs 2040/60)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   2000 bulbs, mean 2040h, sd 60h. Estimate the number that burn
   (i) more than 2150h (ii) less than 1950h (iii) 1920-2160h.
   (given phi(1.5) = 0.4332, phi(1.83) = 0.4664, phi(2) = 0.4772)
   (sheet: 67, 184, 1909)
```

EVERY STEP:

```
  STEP 1  (i) z = (2150-2040)/60 = 1.83. P(X>2150) = 0.5 - phi(1.83) = 0.0336
          count = 0.0336 x 2000 = 67.2 -> 67
  STEP 2  (ii) z = (1950-2040)/60 = -1.5. P(X<1950) = 0.5 - phi(1.5) = 0.0668
          count = 0.0668 x 2000 = 133.6 -> 134
  STEP 3  (iii) z1 = -2, z2 = 2: opposite signs ADD:
          P = phi(2) + phi(2) = 0.9544 ; count = 1908.8 -> 1909
```

ANSWER: (i) 67, (ii) 134, (iii) 1909. (see F15.8: the sheet prints 184 for (ii); the
method above with the sheet's own phi values gives 134.)

TRAP: part (ii)'s sign: 1950 is BELOW the mean, so its z is -1.5 and the lower tail uses
0.5 - phi(1.5).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 15 (asgn 2025-26 #2 Q15 and Q28 - the two marks questions)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Q15: 1000 students, marks N(70, 5^2). Expected number with marks (i) < 69 (ii) > 72
        (iii) between 69 and 72.  (sheet: 421, 345, 235)
   Q28: mean 79, sd 5, class of 200: how many did NOT get between 75 and 82? (sheet: 97)
```

EVERY STEP (Q15):

```
  STEP 1  (i) z = (69-70)/5 = -0.2: P = 0.5 - phi(0.2) = 0.4207 ; count = 421
  STEP 2  (ii) z = (72-70)/5 = 0.4: P = 0.5 - phi(0.4) = 0.3446 ; count = 345
  STEP 3  (iii) opposite signs ADD: phi(0.2) + phi(0.4) = 0.0793 + 0.1554 = 0.2347
          count = 235
```

EVERY STEP (Q28):

```
  STEP 4  z1 = (75-79)/5 = -0.8 ; z2 = (82-79)/5 = 0.6
          INSIDE = phi(0.8) + phi(0.6) = 0.2881 + 0.2257 = 0.5138
          OUTSIDE = 1 - 0.5138 = 0.4862 ; count = 200 x 0.4862 = 97.2 -> 97
```

ANSWER: 421, 345, 235 and 97. (verified exactly)

TRAP: Q28's ask is "did NOT receive" = the OUTSIDE. Computing the inside and reporting it
is the trap.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 16 (asgn 2025-26 #2 Q29 + Q31 + Q18 - three quick normals)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Q29: income N(900, 200^2): P(600 < X < 1200).  (sheet: 0.8664)
   Q31: elevator 2000 lb capacity, 10 adults, N(165, 20^2), own weight 150:
        P(10 adults + you fit)?  (sheet: 0.9992)
   Q18: washers mean 0.502, sd 0.005, tolerance 0.496-0.508: % defective.
        (given phi(1.2) = 0.3849; sheet: 23.02%)
```

EVERY STEP (Q29):

```
  STEP 1  z1 = (600-900)/200 = -1.5 ; z2 = 1.5. opposite signs ADD:
          P = 2 x phi(1.5) = 2 x 0.4332 = 0.8664
```

EVERY STEP (Q31):

```
  STEP 2  the load: you (150) + ten adults. The ten adults sum ~ N(10 x 165, 10 x 400)
          = N(1650, 4000) with sd = sqrt(4000) = 63.25.
  STEP 3  total with you: mean = 1650 + 150 = 1800.
          P(total <= 2000) = P(z <= (2000-1800)/63.25) = P(z <= 3.16)
          = 0.5 + phi(3.16) = 0.9992
```

EVERY STEP (Q18):

```
  STEP 4  z = (0.508 - 0.502)/0.005 = 1.2. INSIDE = 2 x 0.3849 = 0.7698
  STEP 5  defective (outside) = 1 - 0.7698 = 0.2302 -> 23.02%
```

ANSWER: 0.8664, 0.9992, 23.02%.

TRAP (Q31): the SUM of ten adults has variance 10 x 400 = 4000 (variances add for
independents). Using sd = 20 for the group is the error.

═══════════════════════════════════════════════════════════════════════════════
F15.6  UNIFORM EXTRAS
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 17 (asgn 2025-26 #2 Q21 - U(-a, a), find a)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   X ~ U(-a, a). (i) find a so P(X > 1) = 1/3. (ii) find a so P(|X| < 1) = P(|X| > 1).
   (sheet: a = 3, a = 2)
```

EVERY STEP:

```
  STEP 1  (i) width matters: P(X>1) = (a-1)/(2a) = 1/3
          3(a-1) = 2a -> 3a - 3 = 2a -> a = 3
  STEP 2  (ii) P(|X|<1) = 2/(2a) = 1/a ; P(|X|>1) = 1 - 1/a.
          set equal: 1/a = 1 - 1/a -> 2/a = 1 -> a = 2
```

ANSWER: (i) 3 (ii) 2.

TRAP: (ii) is the median condition: the interval [-1,1] splits the support into equal
halves only when a = 2.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 18 (asgn 2025-26 #2 Q23 - the string cutting, P = 2/3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A 1m string is cut at a random point. P(the longer piece is at least twice the
   shorter)?  (sheet says 1/3; the exact answer is 2/3 - see F15.8)
```

EVERY STEP:

```
  STEP 1  cut at x ~ U(0,1). pieces x and 1-x.
  STEP 2  condition: longer >= 2 x shorter.
          if x <= 1/2: longer = 1-x: need 1-x >= 2x -> x <= 1/3.
          if x >= 1/2: longer = x:   need x >= 2(1-x) -> x >= 2/3.
  STEP 3  P = P(x <= 1/3) + P(x >= 2/3) = 1/3 + 1/3 = 2/3.
```

ANSWER: 2/3 (the sheet's 1/3 counts only one side).

THE PICTURE:
```
   0 ----1/3----------1/2----------2/3---- 1
   [ GOOD ]           |           [ GOOD ]
      1/3             |             1/3        -> total 2/3
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 19 (asgn 2025-26 #2 Q25 - U(-3,3), the four-part standard)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

(In F13 Q8 already; answers 5/6, 2/3, 1/2, K = 1. The 2024-25 and 2025-26 sheets use the
same question, which confirms it is a fixed part of the course's assignment bank.)

═══════════════════════════════════════════════════════════════════════════════
F15.7  MISC DRILL
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 20 (asgn 2024-25 #1 Q15 - the keys problem)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A man with n keys tries them independently at random. Mean and variance of the number
   of trials (i) IF unsuccessful keys are NOT eliminated (ii) IF they are.
```

EVERY STEP:

```
  STEP 1  (i) WITH replacement (keys not eliminated): each trial has p = 1/n of success.
          The trial count is GEOMETRIC: E = 1/p = n ; Var = (1-p)/p^2 = n(n-1).
          (geometric: mean 1/p, variance (1-p)/p^2 with support 1,2,3,...)
  STEP 2  (ii) WITHOUT replacement: the number of the successful key among the n keys is
          uniform on {1,...,n} (each position equally likely).
          E = (n+1)/2 ; Var = (n^2 - 1)/12
          (the standard discrete-uniform moments.)
```

ANSWER: (i) mean n, variance n(n-1). (ii) mean (n+1)/2, variance (n^2-1)/12.

TRAP: recognizing which process it is. "Keys not eliminated" = independent trials =
geometric. "Eliminated" = no repeats = uniform position.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 21 (asgn 2024-25 #1 Q16 - Y = X^2 + 2X, the transformed rv)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Y = X^2 + 2X, X has distribution x: 1,2,3,4 with P: 0.1,0.2,0.5,0.1.
   Find the distribution, cdf, mean, and variance of Y.
```

STEP 0: NOTE the probabilities sum to 0.9, not 1. The sheet has a typo (likely the last P
should be 0.2). Proceed with 0.1, 0.2, 0.5, 0.2 so the distribution is valid.

EVERY STEP:

```
  STEP 1  transform each x: 
          x=1 -> 3 ; x=2 -> 8 ; x=3 -> 15 ; x=4 -> 24
  STEP 2  the distribution of Y:
          +----+-----+-----+------+------+
          | y  |  3  |  8  |  15  |  24  |
          +----+-----+-----+------+------+
          |P(Y)| 0.1 | 0.2 | 0.5  | 0.2  |
          +----+-----+-----+------+------+
  STEP 3  the cdf (cumulative):
          F(y) = 0.1 (y<8); 0.3 (8<=y<15); 0.8 (15<=y<24); 1 (y>=24)
  STEP 4  mean: E(Y) = 3(0.1)+8(0.2)+15(0.5)+24(0.2) = 0.3+1.6+7.5+4.8 = 14.2
  STEP 5  variance: E(Y^2) = 9(0.1)+64(0.2)+225(0.5)+576(0.2) = 0.9+12.8+112.5+115.2
          = 241.4
          Var = 241.4 - (14.2)^2 = 241.4 - 201.64 = 39.76
```

ANSWER (with the corrected probabilities): distribution {3:.1, 8:.2, 15:.5, 24:.2},
E(Y) = 14.2, Var(Y) = 39.76.

TRAP: transform the VALUES, keep the probabilities attached. Do not re-sort or combine
(here the y's are all distinct).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 22 (asgn 2025-26 #2 Q33 + Q34 - two application normals)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Q33: marks N(65, 5^2). 3 students selected. P(at least one scored above 75)?
        (sheet: 0.0667)
   Q34: rope strength N(45, 18). X > 43 -> profit 1000; X <= 43 -> profit 400.
        Expected profit per coil?  (sheet: 920)
```

EVERY STEP (Q33):

```
  STEP 1  one student: P(X>75) = P(z>2) = 0.5 - phi(2) = 0.0228
  STEP 2  "at least one of 3" = 1 - P(none): 1 - (1-0.0228)^3
          = 1 - 0.9772^3 = 1 - 0.9331 = 0.0669
```

EVERY STEP (Q34):

```
  STEP 3  one coil: P(X>43) with z = (43-45)/sqrt(18) = -2/4.2426 = -0.4714
          = 0.5 + phi(0.4714) = 0.5 + 0.1813 = 0.6813
  STEP 4  expected profit = 1000 x 0.6813 + 400 x (1 - 0.6813)
          = 681.3 + 127.5 = 808.8
```

ANSWER: Q33: 0.0669 (sheet's 0.0667 uses a slightly different rounding of 0.0228).
Q34: 808.8 (the sheet prints 920; see F15.8 for the note).

TRAP (Q33): "at least one" over 3 students = the complement of "none of the three".

═══════════════════════════════════════════════════════════════════════════════
F15.8  THE PRINTED-ANSWER FLAGS  (found by machine-verifying every sheet answer)
═══════════════════════════════════════════════════════════════════════════════

```
   +----------+---------------------------+------------------+-------------------------------+
   | sheet    | question                  | printed          | exact (machine)               |
   +----------+---------------------------+------------------+-------------------------------+
   | 25-26#1  | Q6 E(good) 7 comp         | 1.7              | 12/7 = 1.714 (rounding)       |
   | 25-26#2  | Q34 rope profit           | 920              | 808.8 (their 920 implies      |
   |          |                           |                  | P(X>43) = 0.867; exact is     |
   |          |                           |                  | 0.6813) FLAG                  |
   | 25-26#2  | Q17 bulbs <1950h          | 184              | 134 with the given phi(1.5)   |
   |          |                           |                  | = 0.4332; 184 implies a       |
   |          |                           |                  | different z. FLAG             |
   | 25-26#2  | Q23 string                | 1/3              | 2/3 (both cuts count)         |
   | 25-26#2  | Q19 repair lambda=2,      | 0.3679, 0.6065   | consistent only with          |
   |          | says lambda=2             |                  | lambda = 1/2. FLAG            |
   | 24-25#1  | Q14 radio tubes (ii)      | 2/3              | 8/27 = 0.2963 (the 2/3 is     |
   |          | none replaced             |                  | P(survive 150) alone)         |
   | 25-26#2  | Q10 n=100 76 var 256      | 0.6311           | 0.6284 (rounding)             |
   | 24-25#2  | Q19 repair lambda=1/2     | 0.3679/0.6065    | matches; the other sheet's    |
   |          | (consistent version)      |                  | lambda=2 does not             |
   | 24-25#1  | Q16 Y=X^2+2X              | (sum = 0.9)      | probabilities do not sum to 1;|
   |          |                           |                  | proceed with 0.2 for the last |
   +----------+---------------------------+------------------+-------------------------------+
```

HOW TO USE THIS TABLE: in the exam, show the METHOD with the GIVEN table values. The
method carries the marks. If a printed answer looks off, state your reading and move on.

═══════════════════════════════════════════════════════════════════════════════
F15 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   THE KEY VALUES VERIFIED IN THIS FILE (for fast recall):
     hypergeometric E = nK/N (3x4/7 = 1.714)
     Z = 2X - 5Y: mean -11, var 54
     kx^2(1-x^3): k=6, mean 9/14, var 9/245
     packets: binomial 189/264/925 vs poisson 184/264/920 (of 1000)
     wireless 9512 sets; library 50 copies; tube parts 1/27, 8/27, 1/4, n=1
     bulbs 67/134/1909; students 421/345/235; class 97 outside; strings 2/3
     elevator 0.9992; washers 23.02%; mid-class 0.8664
     U(-a,a): a=3 and a=2; keys: (n, n(n-1)) and ((n+1)/2, (n^2-1)/12)

   THE TOP PATTERNS THIS FILE DRILLS:
     expectation of a transformed/combined rv (no distribution rebuild needed)
     the count layer (x1000, x2000, x10000)
     the memoryless subtract-the-ages trick
     the conditional divide-by-survival move
     the opposite-sign ADD rule for normal intervals
     inverse normal (find c for a coverage requirement)
```
