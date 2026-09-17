# F8 ESTIMATION: every shape, every question, solved from zero

Source: our own material (MTE 2025-26 block Q3, the ETE papers E24S3, E24S4, E25S3, E25SUM,
R25S3, R25S4, and the ppt5 / lms-theory decks). Nothing invented. All numbers machine-checked.

```
  SHAPES IN THIS FILE
  F8.1  definition MCQs     unbiased / sufficient / MLE / consistent   5 questions (1 MTE!)
  F8.2  verify unbiasedness the 16-sample enumeration                  1 question
  F8.3  consistency         bias and variance -> 0                     1 question
  F8.4  confidence interval sample + formula                           3 questions
  F8.5  sufficiency         the definition                             1 question (MTE!)
```

═══════════════════════════════════════════════════════════════════════════════
BEFORE ANY QUESTION: the vocabulary, in plain words
═══════════════════════════════════════════════════════════════════════════════

An ESTIMATOR is a recipe for guessing a population fact from a sample. The population fact is
called the PARAMETER (usually written theta).

```
   +--------------+------------------------------------------------------+
   | PARAMETER    | the true but unknown number about the population      |
   |              | (the real average, the real variance)                 |
   | ESTIMATOR    | a RECIPE using sample data, e.g. "the sample mean"    |
   | (written     |                                                       |
   |  theta-hat)  |                                                       |
   | ESTIMATE     | the NUMBER you get when you apply the recipe          |
   +--------------+------------------------------------------------------+
```

THE FOUR CHARACTERISTICS (the whole topic lives here):

```
   +----------------+-----------------------------------------------------+
   | UNBIASED       | on average it hits the target: E(theta-hat) = theta  |
   | EFFICIENT      | among unbiased ones, it has the SMALLEST variance    |
   | CONSISTENT     | as n grows it converges to theta (bias->0, var->0)   |
   | SUFFICIENT     | it uses ALL the information about theta in the sample|
   +----------------+-----------------------------------------------------+
```

THE PROTOCOL (check in THIS ORDER; it is the exam's expected sequence):

```
   STEP 1  is it UNBIASED?          if no -> it is eliminated from efficiency
   STEP 2  among the unbiased, is it EFFICIENT (smallest variance)?
   STEP 3  is it CONSISTENT?
   STEP 4  is it SUFFICIENT?
```

THE PICTURE (target shooting):

```
   unbiased, low variance:     unbiased, high variance:    BIASED:
        .                          .  .   .                .  . .
      . x .                     .        .                  .  . .
        .                          .  .                     . x .
     tight cluster                spread out              shifted off-centre
     on the bullseye              on the bullseye           (wrong aim)
```

THE FAMOUS EXAMPLE SET (T1 to T4, used across the course):

```
   sample X1, X2, X3 taken from a population with mean mu and variance sigma^2

   +----+------------------+------------+-------------------+
   |    | formula          | E(T)       | Var(T)            |
   +----+------------------+------------+-------------------+
   | T1 | X1               | mu         | sigma^2           |
   | T2 | (X1+X2)/2        | mu         | sigma^2/2         |
   | T3 | (X1+X2+X3)/3     | mu         | sigma^2/3         |
   | T4 | (X1+X2+X3)/2     | 3mu/2      | (3/4)sigma^2      |
   +----+------------------+------------+-------------------+
     T1, T2, T3 are unbiased.  T4 is BIASED (its E is 3mu/2, not mu).
     among the unbiased, T3 has the smallest variance -> T3 is the efficient one.
     the T4 trap: it LOOKS like it has a small variance (0.75 < 1) but it is biased, and
     efficiency is only defined among unbiased estimators.
```

═══════════════════════════════════════════════════════════════════════════════
F8.1  DEFINITION MCQs  (five of them, all pure recall)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 1 (our paper, ETE 2024-25 S3 A3 - fill in the blank)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   If the expected value of an estimator is equal to its parametric function,
   it is said to be ..........
```

ANSWER: unbiased.

DECODE: "expected value of an estimator" = E(theta-hat). "equal to its parametric function" =
equal to theta. That is the definition of unbiased, word for word.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 2 (our paper, ETE 2025-26 S3 A2 - MCQ form)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   For a statistic theta-hat to be an unbiased estimator of theta, which condition
   must be met?
   a) E(theta-hat) != theta     c) E(theta-hat) = theta
   b) E(theta-hat) < theta      d) E(theta-hat) > theta
```

ANSWER: (c) E(theta-hat) = theta.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 3 (our paper, ETE 2024-25 S4 A1 - the full sentence)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   An estimator is said to be unbiased if:
   a) Its variance is zero
   b) Its expected value equals the true parameter
   c) It has the smallest possible variance
   d) It is equal to the median
```

ANSWER: (b).

TRAP for all three: options (a) and (c) describe EFFICIENCY or an idealized zero-variance
estimator, not unbiasedness. Keep the four definitions separate in your head:
```
   unbiased    = right on average
   efficient   = smallest variance (among unbiased)
   consistent  = converges as n grows
   sufficient  = uses all the information
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 4 (our paper, ETE 2025 summer Q4, and ETE re-session S4 A3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   (a) Maximum likelihood estimator maximizes:
       (A) Mean   (B) Likelihood function   (C) Variance   (D) Bias
   (b) If an estimator "t" approaches the true parameter value "theta" as the sample size
       n increases to infinity, the estimator "t" is called
       a) Efficient   b) Sufficient   c) Consistent   d) Unbiased
```

ANSWERS: (a) (B) Likelihood function.   (b) (c) Consistent.

WHY: the MLE's entire definition is "the value of the parameter that makes the observed data
most likely". And convergence as n grows IS consistency.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 5 (MTE 2025-26 paper, block Q3 - the real thing)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A statistic is sufficient for a parameter if
   1) It minimizes the sample variances
   2) It contains all the information needed about the parameter
   3) It is always unbiased
   4) It is equal to the sample mean
```

ANSWER: option 2.

WHY (and this is worth a line in any written answer): sufficiency means the statistic captures
EVERYTHING in the sample that tells you about the parameter. Once you know the sufficient
statistic, the rest of the sample adds nothing.

TRAP: option 1 is efficiency, option 3 is unbiasedness, option 4 is a specific example (the
sample mean IS sufficient for a normal mean, but that is not the DEFINITION).

═══════════════════════════════════════════════════════════════════════════════
F8.2  VERIFY UNBIASEDNESS:  the full-enumeration method
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 6 (our paper, ETE 2025-26 S3 B5)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A population consists of four values 2, 4, 6 and 8. Draw all samples of size two with
   replacement. Verify that the sample mean is an unbiased estimator of population mean.
```

STEP 0: DECODE

```
   "all samples of size two with replacement" -> every ordered pair (a,b) from {2,4,6,8},
        and there are 4 x 4 = 16 of them.
   "verify the sample mean is unbiased" -> show E(sample mean) = population mean.
   the METHOD: enumerate all 16, average their means, compare to the population mean.
```

STEP 1: THE POPULATION MEAN

```
   mu = (2 + 4 + 6 + 8) / 4 = 20/4 = 5
```

STEP 2: ENUMERATE ALL 16 SAMPLES AND THEIR MEANS

```
       second pick ->
        2     4     6     8
   +---------------------------+
 2 |    2     3     4     5    |
 4 |    3     4     5     6    |
 6 |    4     5     6     7    |
 8 |    5     6     7     8    |
   +---------------------------+
   first pick down the side.
   each cell shows the MEAN of that pair: (a+b)/2.

   for example: pair (2,4) has mean 3; pair (6,8) has mean 7.
```

STEP 3: AVERAGE ALL 16 MEANS

```
   by symmetry the grid is symmetric about 5, so the average must be 5.
   verify by counting:
       mean 2: appears 1 time
       mean 3: appears 2 times
       mean 4: appears 3 times
       mean 5: appears 4 times
       mean 6: appears 3 times
       mean 7: appears 2 times
       mean 8: appears 1 time
       total = 16 ✓

   weighted sum = 2(1) + 3(2) + 4(3) + 5(4) + 6(3) + 7(2) + 8(1)
                = 2 + 6 + 12 + 20 + 18 + 14 + 8
                = 80

   average = 80 / 16 = 5
   (machine-checked: 5.0)
```

STEP 4: THE VERDICT

```
   E(sample mean) = 5
   population mean = 5
   they are EQUAL, so the sample mean is an unbiased estimator of the population mean. ✓
```

THE PICTURE (the distribution of the 16 sample means):

```
   4 |          ##
   3 |       ## ## ##
   2 |    ## ## ## ## ##
   1 | ## ## ## ## ## ## ##
     +--2--3--4--5--6--7--8--
       centred exactly on the population mean 5. that IS unbiasedness, drawn.
```

TRAP:
```
   1. Forgetting "with replacement" and listing only 10 unordered pairs. With replacement
      gives 4^2 = 16 ORDERED pairs; (2,4) and (4,2) are different draws.
   2. Averaging the means without weighting by how often each appears.
   3. Concluding "unbiased" without actually comparing to mu. STATE the comparison.
```

═══════════════════════════════════════════════════════════════════════════════
F8.3  CONSISTENCY
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 7 (our paper, ETE re-session S3 A2 - MCQ)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Let Tn be an estimator for the population parameter theta. The mean and variance of Tn
   are given by E(Tn) = theta + 1/n,  Var(Tn) = 4/n^2.
   Is the estimator Tn a consistent estimator for theta?
   a. Yes, because the bias -> 0 and the variance -> 0 as n -> infinity.
   b. No, because the bias does not tend to zero as n -> infinity.
   c. Yes, because ... (other wording)
```

STEP 0: DECODE - consistency has TWO conditions.

```
   +---------------------------------------------------------------------+
   |  an estimator is CONSISTENT when BOTH hold as n -> infinity:         |
   |     (1) the BIAS goes to 0                                           |
   |     (2) the VARIANCE goes to 0                                       |
   +---------------------------------------------------------------------+
```

EVERY STEP:

```
  STEP 1  Find the bias. bias = E(Tn) - theta = (theta + 1/n) - theta = 1/n
  STEP 2  As n -> infinity, bias = 1/n -> 0 ✓ condition 1 holds.
  STEP 3  Variance is 4/n^2. As n -> infinity, 4/n^2 -> 0 ✓ condition 2 holds.
  STEP 4  Both conditions hold, so Tn IS consistent.
```

ANSWER: option (a), yes, because both the bias and the variance tend to zero.

THE PICTURE (what happens as n grows):

```
   n=1:   bias = 1.000   var = 4.000
   n=5:   bias = 0.200   var = 0.160
   n=10:  bias = 0.100   var = 0.040
   n=100: bias = 0.010   var = 0.0004
   n=inf: bias -> 0      var -> 0        both go to the target.

   the estimator's "spread" collapses onto theta.
```

TRAP:
```
   1. Seeing "theta + 1/n" and concluding "not unbiased, therefore not consistent".
      A BIASED estimator can still be consistent if the bias vanishes as n grows. These are
      DIFFERENT properties, and this question is designed to catch exactly that confusion.
   2. Checking only one of the two conditions. You need BOTH.
   3. Reading 1/n as a constant. It depends on n; that is the whole point.
```

═══════════════════════════════════════════════════════════════════════════════
F8.4  CONFIDENCE INTERVALS
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 8 (our paper, ETE 2025-26 S3 C1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A survey showed that a family in a metro-city spends an average of Rs 500 on clothes
   every month. Suppose a sample of 81 families resulted in a sample mean of Rs 540 per
   month and a sample standard deviation of Rs 150, develop a 95 per cent confidence
   interval estimator of the mean amount spent per month by a family.
   (Tabulated value: 1.96)
```

STEP 0: DECODE

```
   "sample of 81"        -> n = 81
   "sample mean 540"     -> xbar = 540
   "sample sd 150"       -> s = 150
   "95 per cent"         -> z = 1.96 (given in the question)
   "confidence interval estimator of the mean" -> the formula xbar +/- z x SE
```

EVERY STEP:

```
  STEP 1  the standard error:
          SE = s / sqrt(n) = 150 / sqrt(81) = 150 / 9 = 16.6667

  STEP 2  the margin of error:
          ME = z x SE = 1.96 x 16.6667
             = 32.6667
          (1.96 x 16.6667: 1.96 x 16 = 31.36; 1.96 x 0.6667 = 1.3067; total 32.6667)

  STEP 3  the interval:
          lower = 540 - 32.6667 = 507.3333
          upper = 540 + 32.6667 = 572.6667
```

ANSWER: the 95 percent confidence interval is (507.33, 572.67).

THE PICTURE (what a CI is):

```
   xbar = 540
     |
     v
   ---[507.33 ============== 572.67]---
             |
      "we are 95% confident the TRUE population mean lies in here"

   the interval is CENTRED on the sample mean, and its half-width is the margin of error.
```

THE MEANING (a likely MCQ / one-mark explanation):
```
   "95 percent confident" means: if we repeated this sampling many times and built an
   interval each time, about 95 percent of those intervals would contain the true mean.
   It does NOT mean "95 percent of families spend in this range".
```

TRAP:
```
   1. Dividing by n instead of sqrt(n). SE = 150/sqrt(81) = 150/9, not 150/81.
   2. Using a t value when the question gives z (or vice versa). Read the given table value.
   3. Forgetting the margin of error entirely and answering "540". That is the point
      estimate, not the interval.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 9 (our paper, ETE 2024-25 S4 C1a) - the t version
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A mechanical engineer measures the tensile strength (in MPa) of 10 steel rods to test
   whether the population mean tensile strength is 550 MPa. The recorded values are:
   540, 560, 545, 555, 570, 530, 535, 558, 565, 548.
   Determine the 95% confidence interval for the mean tensile strength.
   (Tabulated value: 2.262)
```

EVERY STEP:

```
  STEP 1  n = 10 values. Compute the sample mean:
          sum = 540+560+545+555+570+530+535+558+565+548
          540+560 = 1100
          1100+545 = 1645
          1645+555 = 2200
          2200+570 = 2770
          2770+530 = 3300
          3300+535 = 3835
          3835+558 = 4393
          4393+565 = 4958
          4958+548 = 5506
          xbar = 5506 / 10 = 550.6

  STEP 2  the sample standard deviation. First each deviation from the mean:
          (540-550.6) = -10.6   -> squared 112.36
          (560-550.6) =   9.4   -> squared  88.36
          (545-550.6) =  -5.6   -> squared  31.36
          (555-550.6) =   4.4   -> squared  19.36
          (570-550.6) =  19.4   -> squared 376.36
          (530-550.6) = -20.6   -> squared 424.36
          (535-550.6) = -15.6   -> squared 243.36
          (558-550.6) =   7.4   -> squared  54.76
          (565-550.6) =  14.4   -> squared 207.36
          (548-550.6) =  -2.6   -> squared   6.76
          sum of squares = 112.36+88.36+31.36+19.36+376.36+424.36+243.36+54.76+207.36+6.76
                         = 1564.4

          sample variance = 1564.4 / (n-1) = 1564.4 / 9 = 173.8222
          s = sqrt(173.8222) = 13.1842

  STEP 3  the standard error:
          SE = s / sqrt(n) = 13.1842 / sqrt(10) = 13.1842 / 3.1623 = 4.1697

  STEP 4  the margin of error with t = 2.262 (given):
          ME = 2.262 x 4.1697 = 9.4307

  STEP 5  the interval:
          lower = 550.6 - 9.4307 = 541.17
          upper = 550.6 + 9.4307 = 560.03
```

ANSWER: the 95 percent confidence interval is approximately (541.17, 560.03).

IMPORTANT NOTE on why t and not z:
```
   sigma is unknown AND n is small (10 < 30), so the t value is used. The question gives
   t = 2.262, which is the t value for 95 percent with n-1 = 9 degrees of freedom.
   DEGREES OF FREEDOM = n - 1 = 10 - 1 = 9.  Always n-1 for a single-sample t interval.
```

TRAP:
```
   1. Forgetting n-1 in the variance. Using 1564.4/10 = 156.44 gives s = 12.51 and a
      different (wrong) interval. The divisor for a SAMPLE variance is n-1.
   2. Using z = 1.96 instead of the given t = 2.262. With n = 10 and unknown sigma, t is
      correct; the question hands you the t value to make this explicit.
   3. Arithmetic in the sum of squares. Take the deviations carefully; a single slip changes
      s noticeably.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 10 (our paper, ETE re-session S4 B4) - the same shape, third time
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   In a random selection of 50 of 600 road crossings in a town, the mean number of
   automobile accidents per year was found to be 3.8 and the sample standard deviation
   was 0.8. Construct a 95% confidence interval for the mean number of accidents per
   crossing per year. The useful data is 1.96.
```

EVERY STEP:

```
  STEP 1  SE = s / sqrt(n) = 0.8 / sqrt(50) = 0.8 / 7.0711 = 0.1131
  STEP 2  ME = 1.96 x 0.1131 = 0.2217
  STEP 3  CI = 3.8 +/- 0.2217 = (3.5783, 4.0217)
```

ANSWER: (3.5783, 4.0217).

TRAP: the "50 of 600" detail is a distractor. You use n = 50 (the SAMPLE), not 600 (the
population). The 600 is flavour.

THE THREE-CI PATTERN (this is a MUTATION family, learn the shape):
```
   all three questions are: xbar +/- (table value) x (s / sqrt(n))
   only the numbers and the table value (z or t) change.
   this shape has now appeared in THREE different papers.
```

═══════════════════════════════════════════════════════════════════════════════
F8.5  SUFFICIENCY
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 11 (our paper, ETE 2024-25 S4 B2, and the MTE MCQ above)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Let x1, x2, ..., xn be a random sample from an exponentially distributed population.
   Find sufficient estimators for theta.
```

STEP 0: DECODE

```
   "exponentially distributed population" -> f(x) = theta e^(-theta x) or similar
   "find sufficient estimators" -> find the statistic that captures all the information
      about theta
   the METHOD: Neyman-Fisher factorisation, OR recognise the standard result.
```

THE STANDARD RESULTS (memorize the table; this is what the exam wants):

```
   +--------------------------+--------------------------------+
   | population               | sufficient statistic for the    |
   |                          | parameter                       |
   +--------------------------+--------------------------------+
   | Poisson (mean theta)     | the SUM (or the sample mean)    |
   | Exponential (rate theta) | the SUM (or the sample mean)    |
   | Normal (mean mu)         | the sample mean                 |
   | Normal (variance)        | the sum of squared deviations   |
   | Binomial (p)             | the sum of successes            |
   +--------------------------+--------------------------------+
```

STEP 1: THE ANSWER FOR THIS QUESTION

```
   for an exponential population, the sufficient statistic for theta is
        the SAMPLE SUM  (sum of xi)  or equivalently the SAMPLE MEAN (xbar)
   either form is accepted; they carry the same information (one is a fixed multiple of
   the other for fixed n).
```

STEP 2: THE JUSTIFICATION (write this line to earn full marks)

```
   by the Neyman-Fisher factorisation theorem, the joint density of the sample can be
   written as a product of (a) a function of the statistic and theta, and (b) a function of
   the data alone. For the exponential family, the sum achieves this separation, so the sum
   is sufficient.
```

THE INTUITION (why the sum, and not something else):
```
   the exponential's parameter theta controls the average size of the observations.
   the sum measures exactly that. once you know the sum, knowing WHICH particular values
   produced it adds nothing about theta.
```

TRAP:
```
   1. Answering with a generic statistic like "the variance" or "an individual xi".
      A single observation is NOT sufficient (it throws away most of the sample).
   2. Not stating that the sample MEAN is equivalent to the SUM. Either is fine.
   3. Confusing sufficient with unbiased (see the MTE MCQ - option 3 is the decoy).
```

═══════════════════════════════════════════════════════════════════════════════
F8 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   FOUR PROPERTIES (keep them apart!):
     UNBIASED    E(theta-hat) = theta
     EFFICIENT   smallest variance AMONG the unbiased
     CONSISTENT  bias -> 0 AND variance -> 0 as n -> infinity
     SUFFICIENT  uses all the information about theta

   THE CHECK ORDER: unbiased -> efficient -> consistent -> sufficient

   T1..T4 SET: T1 sigma^2, T2 sigma^2/2, T3 sigma^2/3, T4 biased (3mu/2)
     T3 wins on efficiency; T4 is eliminated on bias.

   CONFIDENCE INTERVAL:  xbar +/- (table value) x (s / sqrt(n))
     z when sigma is known or n is large;  t when sigma is unknown and n is small
     degrees of freedom = n - 1
     SE = s/sqrt(n), NOT s/n

   SUFFICIENT STATISTICS: sum / sample mean for Poisson, exponential, normal mean.
     justify with Neyman-Fisher.

   TOP TRAPS:
     biased-but-consistent confusion (the E(Tn)=theta+1/n question)
     T4 chosen on variance (efficiency excludes biased estimators)
     dividing by n for the variance instead of n-1
     using z when t is required (or the reverse)
     sufficiency vs unbiasedness vs efficiency in MCQs
```
