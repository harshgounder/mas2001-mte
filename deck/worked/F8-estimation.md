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

SUFFICIENCY QUALIFICATION:
```
   Sufficiency is a property of a statistic for a SPECIFIED parameter in a SPECIFIED
   probability model. "Uses all the information" means that, once the statistic is known,
   the conditional distribution of the rest of the sample does not depend on that parameter.
   It does not mean the statistic is automatically unbiased, efficient, or sufficient under
   a different model. The factorisation statements below assume the stated random-sample
   model and fixed sample size.
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
QUESTION 4b (our paper, ETE 2025 summer Q2 - what a CI provides)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A confidence interval provides
   (A) Exact value of parameter        (B) Range of values likely to contain the parameter
   (C) Only sample mean                (D) Only population variance
```

ANSWER: (B). A CI is a RANGE estimator; it never claims an exact value (that misreads the
nature of an interval).

TRAP: (A) is the tempting wrong answer. "Exact value" contradicts the whole point of an
interval estimate (which exists precisely to express uncertainty).

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
statistic, the rest of the sample adds nothing about that parameter under the stated model.
This is the plain-language version of the parameter-free conditional-distribution definition,
not a claim that every statistic is sufficient in every model.

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
   FINITE-POPULATION ASSUMPTION: the four listed values are the four equally likely members
        of the population, and replacement makes the two draws independent. Unequal member
        frequencies or sampling without replacement would require a different calculation.
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

ASSUMPTION NOTE ON THE FINITE POPULATION:
```
   The displayed answer follows the course convention of treating the 50 observations as
   independent for the standard error, so it does not use a finite-population correction.
   This is appropriate when the target is a larger or superpopulation mean, or when the
   sampling fraction is being ignored as the source does. If the wording instead means a
   simple random sample without replacement from this finite population of N = 600 and the
   target is its finite-population mean, use
        FPC = sqrt((N - n)/(N - 1)) = sqrt(550/599) = 0.9582,
        SE = (0.8/sqrt(50)) x FPC = 0.1084,
   giving ME = 1.96 x 0.1084 = 0.2125 and CI = (3.5875, 4.0125).
   The source does not state this design choice, so state the no-FPC convention when using
   its answer (3.5783, 4.0217).
```

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

   MODEL ASSUMPTION: the observations are an iid sample, the support is x >= 0 and theta is
   the exponential RATE in f(x;theta) = theta exp(-theta x). A different parameterisation,
   support, or sampling model can have a different sufficient statistic.
```

THE STANDARD RESULTS (memorize the table; this is what the exam wants):

These entries are model-specific shorthand. The Poisson and binomial rows assume fixed n;
the normal rows name one parameter of interest and assume the usual iid normal sample.

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 12 (our paper, ETE 2025-26 S4 Q B2 - the Poisson twin, 6 marks)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Show that the sample mean is sufficient for the parameter lambda of the Poisson
   distribution.
```

STEP 0: DECODE - "SHOW" means you must PROVE it, not just state it. The tool is the
Neyman-Fisher factorisation.

EVERY STEP:

```
  STEP 1  write the joint pmf of the sample (independent Poisson observations):
          P(x1,...,xn; lambda) = product over i of [ e^(-lambda) lambda^(xi) / xi! ]

  STEP 2  combine the exponentials and the powers:
          = e^(-n lambda) x lambda^(x1+x2+...+xn) / (x1! x2! ... xn!)

  STEP 3  the two factors:
          (A) e^(-n lambda) lambda^(sum xi)      <- contains lambda AND the data only
                                                     through the SUM
          (B) 1 / (x1! ... xn!)                  <- contains only the data, no lambda

  STEP 4  by the factorisation theorem, a statistic is sufficient exactly when the joint
          pmf splits into (a function of the statistic and the parameter) x (a function of
          the data alone). Factor (A) depends on the data only via sum xi = n x (sample
          mean), so the SAMPLE MEAN (equivalently the sum) is sufficient.

  STEP 5  the closing line to write: the sample mean is sufficient for lambda. Q.E.D.
```

THE LIKELIHOOD-RATIO CHECK (a second way to see it, useful for intuition):
```
   take two different samples with the SAME sum, e.g. (1,1,3) and (2,2,1), both sum 5.
   P(1,1,3)/P(2,2,1) for lambda = 0.5, 2, 5, 100 is CONSTANT (machine-checked: 2/3 in
   all cases). If the ratio does not depend on lambda, then no information about lambda
   lives outside the sum. That is sufficiency.
```

TRAP:
```
   1. Answering only "the sample mean is sufficient" without the factorisation. The word
      SHOW earns marks only with the split written out.
   2. Forgetting that "sum" and "sample mean" are interchangeable here (one is n times
      the other).
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 13 (our paper, ETE 2025-26 S4 Q B3 - the weighted estimators, 6 marks)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Let X1, X2, X3, X4, X5 be a random sample of size 5 from a population with mean mu and
   variance sigma^2. Two estimators are suggested:
        T1 = (X1 + X2 + X3 + X4 + X5) / 5
        T2 = (X1 + 2X2 + 3X3 + 4X4 + 5X5) / 15
   Are both estimators unbiased? Which one is more efficient?
```

EVERY STEP:

```
  STEP 1  E(T1): each Xi has mean mu, so
          E(T1) = (mu + mu + mu + mu + mu)/5 = 5mu/5 = mu  -> UNBIASED ✓

  STEP 2  E(T2): the weights are 1,2,3,4,5 over a denominator of 15:
          E(T2) = (1mu + 2mu + 3mu + 4mu + 5mu)/15 = 15mu/15 = mu  -> UNBIASED ✓
          (both are unbiased; the weights summing to the denominator is exactly why)

  STEP 3  Var(T1): independent Xi, equal weights 1/5:
          Var(T1) = (1/25)(5 sigma^2) = sigma^2/5 = 9 sigma^2/45

  STEP 4  Var(T2): weights 1/15, 2/15, ..., 5/15, squared:
          Var(T2) = (1^2+2^2+3^2+4^2+5^2) sigma^2 / 15^2
                  = (55/225) sigma^2
                  = 11 sigma^2/45

  STEP 5  compare: 9/45 vs 11/45.
          Var(T1) < Var(T2), so T1 is MORE EFFICIENT.
```

ANSWER: both unbiased; T1 is more efficient because it has the smaller variance
(sigma^2/5 vs 11 sigma^2/45).

THE PICTURE (why the equal weights win):
```
   T1 gives every observation the same weight: 1/5 each   <- spreads the risk evenly
   T2 leans on X5 (weight 5/15) and barely uses X1 (1/15) <- a few observations carry
                                                              most of the risk

   the squared weights in Var:  T1 -> 5 x (1/25)          = 0.200
                                T2 -> (1+4+9+16+25)/225    = 0.244
   the uneven weights make the variance bigger. That is the general lesson: among linear
   unbiased estimators with independent equal-variance data, equal weights are best.
```

TRAP:
```
   1. Concluding T2 is "more efficient" because it weights bigger Xi more. Weighting the
      DATA values tells you nothing; what matters is the variance formula with SQUARED
      weights.
   2. Concluding T2 is biased. Its weights sum to the same as the denominator (15), so
      E(T2) = mu exactly. The un-normalised-looking form is the decoy.
   3. Forgetting the SQUARES in Var(T2): the term is (2/15)^2 = 4/225, not 2/225.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 11b (the MTE MCQ above, cross-referenced)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For completeness: the MTE 2025-26 paper asks the SUFFICIENCY DEFINITION as MCQ (Q3), solved
at the top of this file (F8.1 Question 5). The three real paper questions on sufficiency
(all in our corpus) are now: the MTE definition MCQ, the exponential "find sufficient
estimators" (2024-25 S4 B2), and the Poisson "show the sample mean is sufficient"
(2025-26 S4 B2).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 14 (MTE 2025-26 paper, block Q8 part (ii) - THE REAL THING, 3 marks)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   If t is an unbiased estimator of the parameter theta, show that t^2 is a biased
   estimator of theta^2.
```

ASSUMPTION NOTE:
```
   The source wording above states only unbiasedness. The conclusion also needs the missing
   non-degeneracy condition 0 < Var(t) < infinity. If Var(t) = 0, the identity below gives
   E(t^2) = theta^2, so t^2 is not biased for theta^2. The proof therefore records the extra
   condition instead of treating it as if it appeared in the source question.
```

STEP 0: DECODE - a PROOF question. The tool: the variance identity.

```
   "t is unbiased for theta"       -> E(t) = theta
   "show t^2 is BIASED for theta^2"-> show E(t^2) is NOT equal to theta^2
   the tool: V(t) = E(t^2) - [E(t)]^2   (the computational variance identity)
             and assume 0 < V(t) < infinity (the source question omits this condition)
```

EVERY STEP:

```
  STEP 1  start from the definition of variance of t:
          V(t) = E[(t - theta)^2]

  STEP 2  expand the square inside the expectation:
          E[(t - theta)^2] = E[t^2 - 2 theta t + theta^2]
                           = E(t^2) - 2 theta E(t) + theta^2     (linearity)

  STEP 3  use the unbiasedness E(t) = theta:
          V(t) = E(t^2) - 2 theta (theta) + theta^2
               = E(t^2) - 2 theta^2 + theta^2
               = E(t^2) - theta^2

  STEP 4  rearrange:
          E(t^2) = V(t) + theta^2

  STEP 5  the punchline: since V(t) is positive under the added non-degeneracy condition,
          E(t^2) = theta^2 + V(t) > theta^2
          so    E(t^2) - theta^2 = V(t) != 0
          the bias of t^2 as an estimator of theta^2 equals V(t), which is NON-ZERO.

  STEP 6  conclude: a biased estimator is one whose expectation is NOT the parameter,
          so t^2 is a BIASED estimator of theta^2. Q.E.D.
```

ANSWER: under the added condition 0 < V(t) < infinity, the proof shows that the bias of t^2
is V(t), which is positive and non-zero. With only the source's unbiasedness assumption, the
general identity is E(t^2) = theta^2 + V(t), so the claim is not guaranteed when V(t) = 0.

THE PICTURE (why squaring breaks unbiasedness):

```
   t lands around theta:     ...t...theta...t...
   t^2 lands around theta^2 + V(t) when V(t) > 0:
        E(t^2) = theta^2 + V(t)      <- always ABOVE theta^2
                 |<--bias=V(t)-->|
   squaring shifts the average upward by exactly the variance. that shift IS the bias.
```

NOTE ON THE OFFICIAL SCHEME: the university's solution prints E(t^2) != 0 at one step; the
mathematically correct line is E(t^2) != theta^2 (or equivalently E(t^2) - theta^2 = V(t)
!= 0). Use the correct form in the exam; the marks are for the identity V(t) = E(t^2) -
[E(t)]^2 applied with E(t) = theta.

TRAP:
```
   1. Writing E(t^2) = [E(t)]^2 (i.e. pulling the square out of the expectation). This is
      exactly the false step the question tests. E(t^2) = [E(t)]^2 + V(t), ALWAYS.
   2. Forgetting to use E(t) = theta (the unbiasedness assumption). It is the input that
      makes the identity collapse to the answer.
   3. Concluding "biased" without stating the bias. The clean finish is: bias = V(t) != 0.
   4. Confusing the two statements: "t is unbiased" (TRUE, given) vs "t^2 is unbiased for
      theta^2" (FALSE, what you are disproving).
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 15 (our LMS deck, theory-of-estimation Example 1 - the find-lambda estimator set)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A sample (X1..X5) from a normal population with mean mu. Three estimators:
        t1 = (X1+X2+X3+X4+X5)/5
        t2 = (X1+X2)/2 + X3
        t3 = (2X1 + X2 + lambda X3)/3   with lambda chosen for unbiasedness.
   Tasks: (1) find lambda (2) check t1, t2 unbiased (3) best estimator?
```

EVERY STEP:

```
  STEP 1  find lambda so E(t3) = mu:
          E(t3) = (2mu + mu + lambda mu)/3 = [(3+lambda)/3] mu
          set = mu:  3+lambda = 3  ->  lambda = 0
          so t3 = (2X1 + X2)/3

  STEP 2  unbiasedness check:
          E(t1) = mu          -> UNBIASED
          E(t2) = (mu+mu)/2 + mu = mu + mu = 2mu  -> BIASED
          E(t3) = (2mu+mu)/3 = mu -> UNBIASED
          so the unbiased pair is t1 and t3.

  STEP 3  variances (independent Xi, Var = sigma^2 each):
          Var(t1) = 5 sigma^2/25 = sigma^2/5      = 0.2000 sigma^2
          Var(t2) = sigma^2/2 + sigma^2 = 3sigma^2/2 = 1.5000 sigma^2  (biased, out anyway)
          Var(t3) = (4 sigma^2 + sigma^2)/9 = 5 sigma^2/9 = 0.5556 sigma^2

  STEP 4  among the UNBIASED: sigma^2/5 < 5sigma^2/9 -> t1 has the smaller variance.
```

ANSWER: lambda = 0; t1 and t3 unbiased (t2 biased); best = t1 = the sample mean.

THE PICTURE:
```
   variance ladder:  t1 [0.20]  <  t3 [0.56]  <  t2 [1.50] (out: biased)
                      ^ best
```

TRAP: t2 LOOKS like it uses all three observations but its weights are (1/2, 1/2, 1) summing
to 2, not 1, so it is biased. Always check the WEIGHTS SUM to 1 before comparing variances.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 16 (our LMS deck, theory-of-estimation Example 2 - the T1/T2/T3 set)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   X1, X2, X3 a sample of size 3 with mean mu, variance sigma^2.
        T1 = X1 + X2 - X3
        T2 = 2X1 + 3X3 - 4X2
        T3 = (lambda X1 + X2 + X3)/3
   (1) unbiasedness of T1, T2 (2) lambda for T3 unbiased (3) is T3 consistent then
   (4) best estimator?
```

CONSISTENCY QUALIFICATION:
```
   The source gives only one statistic at the fixed sample size n = 3. Consistency is a
   property of a sequence of estimators as n -> infinity, not of one fixed-n statistic.
   Thus T3 at n = 3 can be shown unbiased, but its variance sigma^2/3 does not itself tend
   to zero. To answer the source's consistency part, interpret T3 as the n = 3 member of the
   sample-mean sequence T_n = (X1 + ... + Xn)/n, with iid observations of finite variance.
```

EVERY STEP:

```
  STEP 1  T1: E = mu + mu - mu = mu                -> UNBIASED
          Var(T1) = sigma^2 + sigma^2 + sigma^2 = 3 sigma^2

  STEP 2  T2: E = 2mu + 3mu - 4mu = mu             -> UNBIASED (2+3-4 = 1!)
          Var(T2) = 4sigma^2 + 9sigma^2 + 16sigma^2 = 29 sigma^2

  STEP 3  T3: E = (lambda mu + 2mu)/3 = mu  ->  lambda + 2 = 3  ->  lambda = 1
          then T3 = (X1+X2+X3)/3 = the sample mean.

  STEP 4  at the displayed fixed n = 3, T3 has E(T3) = mu and Var(T3) = sigma^2/3.
          This proves unbiasedness at n = 3, but does NOT prove consistency because there is
          no n -> infinity limit for one fixed statistic.

  STEP 5  under the sample-mean-sequence interpretation in the note,
          T_n = (X1 + ... + Xn)/n has E(T_n) = mu and Var(T_n) = sigma^2/n -> 0.
          Its bias and variance therefore both tend to zero, so the sequence is consistent.

  STEP 6  variances at the displayed n = 3:
          3 sigma^2 (T1) vs 29 sigma^2 (T2) vs sigma^2/3 (T3)
          sigma^2/3 < 3sigma^2 < 29sigma^2  -> T3 is the BEST.
```

ANSWER: T1 and T2 are unbiased; lambda = 1; T3 is the n = 3 sample mean and is best at this
fixed n. Under the intended sample-mean-sequence interpretation, the family T_n is consistent.
The fixed-n display alone does not establish consistency.

TRAP: T2's coefficients (2, -4, 3) look wild but sum to 1, so it IS unbiased; its variance
is the killer (29). And note the negative weight SQUARES into the variance as positive 16.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
F8.7  THE REAL-LIFE NUMERICALS (LMS deck):  point estimates and the z-CI table
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Three quick drills from the deck (they teach the estimator-vs-estimate distinction):

```
   DRILL 1: server response times 180,210,195,220,205,190,200,240 (ms).
     estimator = Xbar ; estimate = 1640/8 = 205 ms.

   DRILL 2: 500 packets, 465 delivered.
     estimator = p-hat = X/n ; estimate = 465/500 = 0.93 (93%).

   DRILL 3: n=25 devices, xbar=8.4 h, sigma=1.5 KNOWN. 95% CI with z=1.96.
     CI = 8.4 +/- 1.96 x (1.5/sqrt(25)) = 8.4 +/- 1.96 x 0.3
        = 8.4 +/- 0.588 = (7.812, 8.988) -> about (7.81, 8.99) hours.
```

THE Z-TABLE TO MEMORIZE (the CI rows):

```
   +-------------+-------+---------+--------+
   | confidence  | alpha | alpha/2 | z      |
   +-------------+-------+---------+--------+
   | 90%         | 0.10  | 0.050   | 1.645  |
   | 95%         | 0.05  | 0.025   | 1.960  |
   | 99%         | 0.01  | 0.005   | 2.576  |
   +-------------+-------+---------+--------+
```

TRAP: sigma KNOWN -> use z (1.96 etc). sigma UNKNOWN with small n -> use t (2.262, 2.093...).
The papers mix both (see the sugar question uses t, this drill uses z).

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
