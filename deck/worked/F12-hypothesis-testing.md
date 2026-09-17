# F12 HYPOTHESIS TESTING: solved from zero

Source: our own material (the ETE papers E24S3, E24S4, E25SUM, R25S3, R25S4). Nothing invented.
All numbers machine-checked.

```
  *** SCOPE NOTE, READ THIS FIRST ***
  hypothesis testing is marked OUT of the MTE syllabus in our ledger (scope=OUT, same as
  MLE/MoM/Bayesian). BUT it appears in FIVE ETE papers, including two 10-mark questions,
  and the recall rule from report 32 says: nothing that CAN come should be uncounted.
  So this file exists as a completeness pass: if a hypothesis-testing MCQ shows up on the
  MTE, you are covered. Priority order: F1-F9 first, then this.
```

```
  SHAPES IN THIS FILE
  F12.1  the definition MCQs (Type I/II, level, critical region, t/F use)   8 questions
  F12.2  one-sample t-test            the full protocol + CI              2 questions
  F12.3  two-sample F-test (variances)                                    2 questions
  F12.4  chi-square test (association)                                    1 question
  F12.5  one-way ANOVA                                                    1 question
```

═══════════════════════════════════════════════════════════════════════════════
BEFORE ANY QUESTION: the whole protocol on one page
═══════════════════════════════════════════════════════════════════════════════

THE VOCABULARY:

```
   +--------------------+-----------------------------------------------------------+
   | H0 (null)          | the "no change / no difference" assumption to be tested    |
   | H1 (alternative)   | what you conclude if H0 is rejected                        |
   | alpha              | the significance level = P(Type I error), usually 0.05     |
   | Type I error       | rejecting H0 WHEN IT IS TRUE     (false alarm)             |
   | Type II error      | accepting H0 WHEN IT IS FALSE    (missed detection)        |
   | critical value     | the table value; |statistic| beyond it -> reject            |
   | critical region    | = the REJECTION region                                     |
   | p-value            | probability of data at least this extreme if H0 true       |
   +--------------------+-----------------------------------------------------------+
```

THE FIVE-STAGE FLOWCHART (draw this before every test):

```
     START
       |
       v
   +----------------------------+
   | 1. STATE the hypotheses     |   H0: mu = 100    H1: mu != 100
   +-------------+--------------+
                 |
                 v
   +----------------------------+
   | 2. PICK the test            |   t (small n, sigma unknown) | z (known/large)
   |    and the alpha            |   F (compare variances) | chi2 (association)
   +-------------+--------------+   ANOVA (compare 3+ means)
                 |
                 v
   +----------------------------+
   | 3. COMPUTE the statistic    |   t = (xbar - mu0)/SE ;   F = s1^2/s2^2
   |    (with SE = s/sqrt(n))    |
   +-------------+--------------+
                 |
                 v
   +----------------------------+
   | 4. COMPARE with the         |   |t| > t_crit ?  F > F_crit ?  chi2 > chi2_crit ?
   |    table value              |
   +-------------+--------------+
                 |
                 v
   +----------------------------+
   | 5. CONCLUDE IN WORDS        |   reject H0 / fail to reject H0, THEN one sentence
   |                             |   about the claim
   +----------------------------+
       (fail to reject is NOT "accept H0"; say "no evidence to reject")
```

THE ERROR TABLE (draw this; the MCQs live here):

```
   +-------------------+-----------------------+-----------------------+
   |                   | H0 is TRUE            | H0 is FALSE           |
   +-------------------+-----------------------+-----------------------+
   | reject H0         | TYPE I (alpha)  <-    | correct               |
   | fail to reject H0 | correct               | TYPE II (beta)  <-    |
   +-------------------+-----------------------+-----------------------+
   remember by the DIRECTION of the error: Type I = I saw something that is not there.
   Type II = I missed something that is there.
   (the level of significance alpha = P(Type I error), NOT Type II)
```

═══════════════════════════════════════════════════════════════════════════════
F12.1  THE DEFINITION MCQs  (eight of them; all pure recall)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 1 (our paper, ETE 2025-26 S4 A2) - Type I error
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A Type I error occurs when:
   a) A true null hypothesis is rejected
   b) A false null hypothesis is accepted
   c) The sample is too small
   d) The test statistic is incorrect
```

ANSWER: (a).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 2 (our paper, ETE 2025 summer Q5) - Type II error
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A Type II error occurs when
   (A) A true null hypothesis is rejected
   (B) A false null hypothesis is accepted
   (C) A false null hypothesis is rejected
   (D) A true null hypothesis is accepted
```

ANSWER: (B).

TRAP: (A) is Type I. The two errors are mirror images: Type I rejects a TRUE H0; Type II
keeps a FALSE H0. Drill the table above until it is automatic.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 3 (our paper, ETE 2025-26 S3 A4) - the investigator form
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   An investigator commits a type II error when he / she
   a) rejects a null hypothesis when it is true
   b) accepts a null hypothesis when it is true
   c) rejects a null hypothesis when it is false
   d) accepts a null hypothesis when it is false
```

ANSWER: (d).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 4 (our paper, ETE re-session S4 A4) - True / False form
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   "Rejecting null hypothesis when it is true comes under type I error".
   Whether this statement is True or False?
```

ANSWER: True. (this is exactly the definition of Type I)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 5 (our paper, ETE 2025-26 S4 A8) - level of significance
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Level of significance is:
   a. Probability of Type II error
   b. Probability of Type I error
   c. Mean
   d. Variance
```

ANSWER: (b). The level alpha IS the probability of a Type I error by construction.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 6 (our paper, ETE 2025-26 S4 A7) - when to use t
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   t-test is used when we have:
   a. Large sample
   b. Small sample
   c. Infinite sample
   d. No sample
```

ANSWER: (b) small sample. (t is the small-sample test with unknown sigma; z is for large
samples or known sigma.)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 7 (our paper, ETE 2025-26 S4 A9) - critical region
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Critical region is:
   a. Acceptance region      b. Rejection region
   c. Sample space           d. Parameter space
```

ANSWER: (b) the REJECTION region.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 7b (our paper, ETE 2024-25 S3 A4 - the one-sided / two-tailed MCQ)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Testing H0: mu = 1000 against H1: mu > 1000 leads to
   a) One sided right-tailed test   b) One sided left-tailed test
   c) Two tailed test               d) None of these
```

EVERY STEP:

```
  STEP 1  read the DIRECTION in H1: "mu > 1000" points RIGHT.
  STEP 2  a directional alternative = ONE-SIDED; the tail follows H1's arrow.
  STEP 3  answer: option (a), one-sided right-tailed.
```

THE PICTURE:
```
   H1: mu > 1000        H1: mu < 1000        H1: mu != 1000
   ----+   [tail]--->   <---[tail]  +----    <--[t]  +  [t]-->
       (a) right            (b) left              (c) two-tailed
```

TRAP: H1 with ">" or "<" is one-sided (the tail on that side); H1 with "!=" is two-tailed.
The tail side follows the ARROW of H1, and the rejection region is where H1 claims the
parameter sits.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 8 (asked twice: ETE 2025-26 S4 A10 form, ETE 2025 summer Q7) - the F-test
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   F-test is used to compare:
   a. Mean   b. Variance   c. Proportion   d. Median
```

ANSWER: (b) variance.

WHY: F = (variance 1)/(variance 2). The F-test compares VARIANCES; the t-test compares
means. This pairing is the most examined one-liner in the section.

═══════════════════════════════════════════════════════════════════════════════
F12.2  ONE-SAMPLE t-TEST:  the full protocol
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 9 (our paper, ETE 2024-25 S3 B5) - the blood sugar test
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A random blood sample for test of fasting sugar for 10 boys gave the following data
   in mg/dl:  70, 120, 110, 101, 88, 83, 95, 107, 100, 98
   Does this support the assumption of population mean of 100 mg/dl? Test at the 5% level
   of significance. Also find the 95% reasonable range in which most of the mean fasting
   sugar tests of the 10 boys lie. (Tabulated value 2.262)
```

STEP 0: DECODE

```
   "support the assumption of mean = 100"  -> H0: mu = 100, H1: mu != 100 (two-tailed)
   "test at 5%"                            -> alpha = 0.05, use t (n = 10 small, sigma unknown)
   "95% reasonable range for the mean"     -> the CONFIDENCE INTERVAL (same question as F8!)
   "tabulated 2.262"                       -> t with n-1 = 9 degrees of freedom
```

EVERY STEP:

```
  STEP 1  sample mean:
          sum = 70+120+110+101+88+83+95+107+100+98 = 972
          xbar = 972/10 = 97.2

  STEP 2  deviations and squares:
          70:  70-97.2 = -27.2  -> 739.84
          120: 120-97.2 =  22.8 -> 519.84
          110: 110-97.2 =  12.8 -> 163.84
          101: 101-97.2 =   3.8 ->  14.44
          88:  88-97.2 =  -9.2  ->  84.64
          83:  83-97.2 = -14.2  -> 201.64
          95:  95-97.2 =  -2.2  ->   4.84
          107: 107-97.2 =   9.8 ->  96.04
          100: 100-97.2 =   2.8 ->   7.84
          98:  98-97.2 =   0.8 ->   0.64
          sum of squares = 1833.6

  STEP 3  sample sd:
          s = sqrt(1833.6 / 9) = sqrt(203.7333) = 14.2735

  STEP 4  standard error:
          SE = s / sqrt(n) = 14.2735 / sqrt(10) = 14.2735 / 3.1623 = 4.5137

  STEP 5  the test statistic:
          t = (xbar - mu0) / SE = (97.2 - 100) / 4.5137
            = -2.8 / 4.5137
            = -0.6203

  STEP 6  compare: |t| = 0.6203 vs t_crit = 2.262
          0.6203 < 2.262  ->  FAIL TO REJECT H0

  STEP 7  the confidence interval (the "reasonable range"):
          xbar +/- t x SE = 97.2 +/- 2.262 x 4.5137
          = 97.2 +/- 10.21
          = (86.99, 107.41)
```

ANSWER: t = -0.62 which is inside the critical values, so there is no evidence against the
assumption; the sample SUPPORTS a population mean of 100 mg/dl. The 95% range for the mean
is (86.99, 107.41).

NOTE how the two asks connect: the decision rule "|xbar - 100| small enough" and the CI
"does the interval contain 100?" are the SAME test. 100 is inside (86.99, 107.41), which
is why we fail to reject. State this link in the answer; it earns marks.

TRAP:
```
   1. Degrees of freedom: n-1 = 9, not 10.
   2. Dividing the sum of squares by n (10) instead of n-1 (9).
   3. Forgetting that "fail to reject" is the answer when |t| < t_crit. The conclusion is
      NOT "population mean = 100"; it is "no evidence against it".
   4. The CI uses the SAME t value (2.262), not 1.96.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 10 (our paper, ETE 2025 summer Q16 / E25SUM-16) - the telephone company
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A local telephone company claims that the average length of a phone call is 8 minutes.
   In a random sample of 18 phone calls, the sample mean was 7.8 minutes, and the standard
   deviation was 0.5 minutes. Is there enough evidence to support this claim at alpha = 0.05?
   Use t-test. [Critical t for 17 df is 2.110]
```

EVERY STEP:

```
  STEP 1  H0: mu = 8   H1: mu != 8   (two-tailed, alpha = 0.05)
  STEP 2  SE = 0.5 / sqrt(18) = 0.5 / 4.2426 = 0.1179
  STEP 3  t = (7.8 - 8) / 0.1179 = -0.2 / 0.1179 = -1.6971
  STEP 4  |t| = 1.697 vs t_crit = 2.110 -> 1.697 < 2.110 -> FAIL TO REJECT
```

ANSWER: no, there is not enough evidence against the claim; the data supports the company's
claim of an 8-minute average.

TRAP:
```
   1. Reading "is there enough evidence to SUPPORT the claim" and flipping the conclusion.
      Failing to reject H0 (mu = 8) IS supporting the claim here, because the claim IS H0.
      (If the claim had been the alternative, the wording of the conclusion flips.)
   2. df = 17 comes from n-1 = 18-1. Using 18 is wrong.
```

═══════════════════════════════════════════════════════════════════════════════
F12.3  TWO-SAMPLE F-TEST  (comparing variances)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 11 (our paper, ETE 2025 summer Q18) - hotel room rates
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A travel agency's brochure indicates that the standard deviations of hotel room rates
   for two cities are the same. A random sample of 13 hotel room rates in one city has a
   standard deviation of Rs 27.50 and a random sample of 16 in the other has a standard
   deviation of Rs 29.75. Can you reject the agency's claim at alpha = 0.01? Use F test.
   [Critical F = 4.72]
```

STEP 0: DECODE

```
   "claim: standard deviations are the same" -> H0: sigma1 = sigma2
   the F test works on VARIANCES -> square the sds first!
```

EVERY STEP:

```
  STEP 1  variances: s1^2 = 27.50^2 = 756.25
                     s2^2 = 29.75^2 = 885.0625

  STEP 2  F = larger variance / smaller variance
            = 885.0625 / 756.25
            = 1.1703
          (note the ORDER: bigger on top. this is the standard convention)

  STEP 3  compare: F = 1.1703 vs F_crit = 4.72
          1.1703 < 4.72 -> FAIL TO REJECT
```

ANSWER: no, you cannot reject the agency's claim; the sample variances are not different
enough. The claim that the two standard deviations are equal stands.

TRAP:
```
   1. Forgetting to SQUARE the standard deviations before forming the ratio. F is a ratio of
      VARIANCES. 27.50/29.75 = 0.924 would be meaningless as an F.
   2. Putting the smaller variance on top. The convention (and the critical value) assumes
      the LARGER variance is the numerator, so that F >= 1.
   3. Conclusion wording: "cannot reject the claim" (H0 was the claim).
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 12 (our paper, ETE re-session S3 C1) - two samples, same variance?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Two random samples were drawn from two normal populations:
   A: 66, 67, 75, 76, 82, 84, 88, 90, 92              (n = 9)
   B: 64, 66, 74, 78, 82, 85, 87, 92, 93, 95, 97      (n = 11)
   Test whether the two populations have the same variance at the 10% level.
   (Tabulated value: 3.07)
```

EVERY STEP:

```
  STEP 1  sample means:
          A: sum = 66+67+75+76+82+84+88+90+92 = 720, mean = 720/9 = 80
          B: sum = 64+66+74+78+82+85+87+92+93+95+97 = 913, mean = 913/11 = 83

  STEP 2  variance of A:
          deviations: -14, -13, -5, -4, 2, 4, 8, 10, 12
          squares: 196+169+25+16+4+16+64+100+144 = 734
          varA = 734 / 8 = 91.75

  STEP 3  variance of B:
          deviations: -19, -17, -9, -5, -1, 2, 4, 9, 10, 12, 14
          squares: 361+289+81+25+1+4+16+81+100+144+196 = 1298
          varB = 1298 / 10 = 129.8

  STEP 4  F = 129.8 / 91.75 = 1.4147

  STEP 5  compare: F = 1.4147 vs 3.07
          1.4147 < 3.07 -> FAIL TO REJECT
```

ANSWER: there is no evidence to say the variances differ; the two populations can be taken
to have the same variance.

TRAP:
```
   1. Degrees of freedom for the two variances are n-1 each (8 and 10), and the F table needs
      BOTH. Here the question gives one critical value (3.07), which is why the ratio must
      be formed with the LARGER variance on top.
   2. Arithmetic in the deviations. Write them in a column, square one by one.
   3. Using 10% as a two-sided alpha and doubling anything. The F test as set up here
      compares the computed F directly with the tabulated 3.07.
```

═══════════════════════════════════════════════════════════════════════════════
F12.4  CHI-SQUARE TEST OF ASSOCIATION  (two categorical variables)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 13 (our paper, ETE 2024-25 S4 D1 - a 10-mark question)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   In a packaging plant, a quality analyst wants to determine whether the type of
   packaging machine used is associated with the defect rate. The machines are X, Y, Z;
   the quality categories are No Defect, Minor Defect, Major Defect. The observed table:
   +----------------+-----------+-----------+-----------+
   | Quality        | Machine X | Machine Y | Machine Z |
   +----------------+-----------+-----------+-----------+
   | No Defect      |    50     |    40     |    30     |
   | Minor Defect   |    20     |    25     |    35     |
   | Major Defect   |    30     |    35     |    35     |
   +----------------+-----------+-----------+-----------+
   Test at 5% whether the machine type is associated with the quality.
   (Tabulated value: 9.488)
```

STEP 0: DECODE

```
   "is machine type ASSOCIATED with quality" -> chi-square test of independence
   H0: the two are INDEPENDENT (no association)
   H1: there is an association
   the test compares OBSERVED counts with EXPECTED counts (what independence would predict).
```

THE EXPECTED-COUNT RECIPE:

```
   expected(i,j) = (row total i) x (column total j) / grand total

   row totals:   120, 80, 100
   column totals: 100, 100, 100
   grand total:   300

   so EVERY expected count in row 1 is 120 x 100/300 = 40,
   row 2 -> 80/3 = 26.667, row 3 -> 100/3 = 33.333
```

THE WORKING TABLE (observed vs expected vs the terms):

```
  +----------------+--------+--------+--------+-----------+-----------+
  | cell           |    O   |    E   |  O - E |  (O-E)^2  | / E       |
  +----------------+--------+--------+--------+-----------+-----------+
  | NoDef-X        |   50   |  40    |  +10   |  100      |  2.500    |
  | NoDef-Y        |   40   |  40    |    0   |    0      |  0.000    |
  | NoDef-Z        |   30   |  40    |  -10   |  100      |  2.500    |
  | Minor-X        |   20   |  26.667|  -6.667|  44.444   |  1.667    |
  | Minor-Y        |   25   |  26.667|  -1.667|    2.778  |  0.104    |
  | Minor-Z        |   35   |  26.667|  +8.333|   69.444  |  2.604    |
  | Major-X        |   30   |  33.333|  -3.333|   11.111  |  0.333    |
  | Major-Y        |   35   |  33.333|  +1.667|    2.778  |  0.083    |
  | Major-Z        |   35   |  33.333|  +1.667|    2.778  |  0.083    |
  +----------------+--------+--------+--------+-----------+-----------+
   chi-square = sum of the last column = 9.875 (machine-verified)
```

THE DECISION:

```
  STEP 1  degrees of freedom = (rows - 1)(cols - 1) = (3-1)(3-1) = 2 x 2 = 4
  STEP 2  compare: chi2 = 9.875 vs 9.488
          9.875 > 9.488 -> REJECT H0
  STEP 3  conclusion: there IS an association between machine type and packaging quality.
```

THE PICTURE:

```
   under H0 (independence), the expected counts sit in a tidy pattern (40 / 40 / 40 ...)
   the observed counts deviate, and chi2 measures the total squared deviation,
   scaled by the expectation:

      small chi2  ->  data looks like independence  ->  keep H0
      large chi2  ->  data departs from independence -> reject H0
```

TRAP:
```
   1. Degrees of freedom: 4, not 9 and not 8. It is (r-1)(c-1).
   2. Computing expected counts as an average of observed cells. They come from
      row total x column total / grand total.
   3. Forgetting to divide each squared deviation by E. The terms are (O-E)^2/E.
   4. Conclusion direction: rejecting H0 here means "THERE IS an association" (the question
      asked "is it associated"), so the answer is yes.
```

═══════════════════════════════════════════════════════════════════════════════
F12.5  ONE-WAY ANOVA  (three or more means)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 14 (our paper, ETE 2024-25 S4 D2 - a 10-mark question)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Three database systems, five trials each (ms):
   MySQL:      210, 220, 215, 225, 230
   PostgreSQL: 240, 245, 250, 255, 260
   MongoDB:    200, 205, 210, 215, 220
   Test at 5% whether the mean execution times differ. (Tabulated value = 3.89)
```

STEP 0: DECODE

```
   comparing MEANS of THREE groups -> one-way ANOVA -> the F statistic
   H0: mu1 = mu2 = mu3 (all the same)
   H1: at least one mean differs
   the idea: split the total variation into BETWEEN-group and WITHIN-group parts;
   if between >> within, the means differ.
```

EVERY STEP:

```
  STEP 1  group means: MySQL = 220, PostgreSQL = 250, MongoDB = 210
          grand mean = (220+250+210)/3 = 226.6667
          (check: overall sum/total N = 3400/15 = 226.6667 ✓)

  STEP 2  SSB (between groups) = sum over groups of n x (group mean - grand mean)^2
          = 5[(220-226.667)^2 + (250-226.667)^2 + (210-226.667)^2]
          = 5[44.444 + 544.444 + 277.778]
          = 5 x 866.667
          = 4333.33

  STEP 3  SSW (within groups) = sum of squared deviations inside each group
          MySQL:      (210-220)^2+(220-220)^2+(215-220)^2+(225-220)^2+(230-220)^2
                    = 100+0+25+25+100 = 250
          PostgreSQL: (240-250)^2+...+(260-250)^2 = 100+25+0+25+100 = 250
          MongoDB:    (200-210)^2+...+(220-210)^2 = 100+25+0+25+100 = 250
          SSW = 750

  STEP 4  (check: SST = SSB + SSW = 4333.33 + 750 = 5083.33 ✓ from the raw values)

  STEP 5  mean squares:
          MSB = SSB/(k-1) = 4333.33/2 = 2166.67
          MSW = SSW/(N-k) = 750/(15-3) = 750/12 = 62.5

  STEP 6  F = MSB/MSW = 2166.67/62.5 = 34.6667
```

THE DECISION:

```
  degrees of freedom: numerator k-1 = 2, denominator N-k = 12
  F = 34.6667 vs 3.89
  34.6667 > 3.89 -> REJECT H0
```

ANSWER: yes, there IS a significant difference in the mean execution times of the three
database systems.

THE PICTURE (what the F compares):

```
   between-group spread: the group means are 220, 250, 210 -> spread 40 ms apart
   within-group spread:  each group varies only 10 ms around its own mean

   between >> within  ->  the differences between groups are REAL, not noise.
```

TRAP:
```
   1. Using N = 15 where k-1 is needed. df pairs: (2, 12).
   2. Dividing SSB by N-k or SSW by k-1. The divisors follow their df.
   3. The conclusion phrase: "at least one mean differs" (not "all three differ" - ANOVA
      does not say by itself WHICH pairs differ).
```

═══════════════════════════════════════════════════════════════════════════════
F12.6  MORE PAPER QUESTIONS (the remaining real ones from our corpus)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 15 (our paper, ETE 2025-26 S3 D1 - contingency table, 10 marks)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Given the following contingency table for hair colour and eye colour:
   +------------+--------+---------+---------+
   | Eye colour | Fair   | Brown   | Black   |
   +------------+--------+---------+---------+
   | Blue       |  15    |   5     |   20    |
   | Grey       |  20    |  10     |   20    |
   | Brown      |  25    |  15     |   20    |
   +------------+--------+---------+---------+
   Is there a good association between hair colour and eye colour at 5% level?
   (Tabulated value: 9.488)
```

EVERY STEP:

```
  STEP 1  totals:
          rows: Blue 40, Grey 50, Brown 60;  columns: Fair 60, Brown 30, Black 60
          grand total = 150

  STEP 2  expected counts = row x col / 150:
          Blue-Fair 16, Blue-Brown 8, Blue-Black 16
          Grey-Fair 20, Grey-Brown 10, Grey-Black 20
          Brown-Fair 24, Brown-Brown 12, Brown-Black 24

  STEP 3  the terms (O-E)^2/E:
          (15-16)^2/16 = 0.0625      (5-8)^2/8 = 1.125        (20-16)^2/16 = 1.0
          (20-20)^2/20 = 0           (10-10)^2/10 = 0         (20-20)^2/20 = 0
          (25-24)^2/24 = 0.0417      (15-12)^2/12 = 0.75      (20-24)^2/24 = 0.6667
          chi2 = 0.0625 + 1.125 + 1.0 + 0.0417 + 0.75 + 0.6667 = 3.6458

  STEP 4  df = (3-1)(3-1) = 4; compare 3.6458 vs 9.488
          3.6458 < 9.488 -> FAIL TO REJECT
```

ANSWER: no evidence of association; hair colour and eye colour are independent in this
data. (machine-verified chi2 = 3.6458)

TRAP: the same as the other chi-square: expected counts from row x col / grand, divide each
squared deviation by E, df = (r-1)(c-1) = 4.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 16 (our paper, ETE re-session S3 B3 - engine parts, t-test + CI)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A company manufactures small engine parts. The engineers aim for a part weight of 25.0 g.
   A sample of 20 parts from a recent run: 24.8, 25.1, 24.9, 25.0, 25.2, 24.7, 25.0, 25.1,
   25.3, 24.9, 25.0, 24.8, 25.1, 24.9, 25.2, 25.0, 25.1, 24.8, 25.0, 25.2.
   Test the hypothesis at 5% and give the 95% confidence limits.
   (t for 19 df at 5% = 2.093)
```

EVERY STEP:

```
  STEP 1  sum = 500.1, n = 20 -> xbar = 25.005
  STEP 2  sum of squared deviations = 0.4895 -> s^2 = 0.4895/19 = 0.025763
          s = 0.16051
  STEP 3  SE = 0.16051 / sqrt(20) = 0.16051/4.4721 = 0.03589
  STEP 4  t = (25.005 - 25.0) / 0.03589 = 0.005/0.03589 = 0.1393
  STEP 5  |t| = 0.1393 < 2.093 -> FAIL TO REJECT (no evidence of a shift)
  STEP 6  CI = 25.005 +/- 2.093 x 0.03589 = 25.005 +/- 0.0751
            = (24.9299, 25.0801)
```

ANSWER: t = 0.1393, no evidence the mean has shifted from 25.0 g; the 95% CI is
(24.93, 25.08), which contains 25.0 (consistent with the decision).
(machine-verified: xbar = 25.005, s = 0.16051, t = 0.1393, CI = (24.9299, 25.0801))

TRAP: the same t-protocol points as the sugar question: df = 19 (n-1), divide the sum of
squares by n-1 = 19, and use the SAME t for the CI as for the test.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 17 (our paper, ETE 2025-26 S3 D2 - the ANOVA techniques, 10 marks)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Three techniques (medication, exercise, special diet) are randomly assigned to people
   with high blood pressure. The reductions (after four weeks):
   Medication: 10, 12, 9, 15, 13
   Exercise:    6,  8, 3,  0,  2
   Diet:        5,  9, 12, 8,  4
   Test at 5% whether there is a significant difference in the mean reduction.
   (Tabulated value: 19.41)
```

EVERY STEP:

```
  STEP 1  group means: Medication = 59/5 = 11.8 ; Exercise = 19/5 = 3.8 ; Diet = 38/5 = 7.6
          grand mean = (59+19+38)/15 = 116/15 = 7.7333

  STEP 2  SSB = sum of n x (group mean - grand mean)^2
          = 5[(11.8-7.7333)^2 + (3.8-7.7333)^2 + (7.6-7.7333)^2]
          = 5[16.5378 + 15.4711 + 0.0178]
          = 5 x 32.0267 = 160.1333

  STEP 3  SSW (deviations inside each group):
          Medication: (10-11.8)^2+(12-11.8)^2+(9-11.8)^2+(15-11.8)^2+(13-11.8)^2
                    = 3.24+0.04+7.84+10.24+1.44 = 22.8
          Exercise:   (6-3.8)^2+(8-3.8)^2+(3-3.8)^2+(0-3.8)^2+(2-3.8)^2
                    = 4.84+17.64+0.64+14.44+3.24 = 40.8
          Diet:       (5-7.6)^2+(9-7.6)^2+(12-7.6)^2+(8-7.6)^2+(4-7.6)^2
                    = 6.76+1.96+19.36+0.16+12.96 = 41.2
          SSW = 22.8 + 40.8 + 41.2 = 104.8

  STEP 4  mean squares:
          MSB = 160.1333/2 = 80.0667
          MSW = 104.8/12 = 8.7333

  STEP 5  F = 80.0667/8.7333 = 9.1679
```

THE DECISION:

```
   F = 9.1679 vs 19.41
   9.1679 < 19.41 -> FAIL TO REJECT
```

ANSWER: no significant difference in mean reduction among the three techniques at the 5%
level. (machine-verified: SSB=160.1333, SSW=104.8, F=9.1679)

TRAP:
```
   1. The same df structure as the other ANOVA: (k-1, N-k) = (2, 12).
   2. This one FAILS to reject while the database ANOVA rejected. Do not pattern-match
      "ANOVA always rejects"; the decision depends entirely on the numbers.
   3. Arithmetic in SSW: three separate sums, then add.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 18 (our paper, ETE 2024-25 S3 B6 - the inoculation 2x2, 5 marks)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Two batches of 12 animals each test an inoculation. One batch was inoculated.
   Dead/Survived:
   +----------------+------+-----------+
   |                | Dead | Survived  |
   +----------------+------+-----------+
   | Inoculated     |   2  |    10     |
   | Not inoculated |   8  |     4     |
   +----------------+------+-----------+
   Can the inoculation be regarded as effective? (Tabulated value 3.841)
```

EVERY STEP:

```
  STEP 1  totals: rows 12 and 12; columns Dead 10, Survived 14; grand 24

  STEP 2  expected: cell = row x col / 24
          Inoculated-Dead:     12 x 10/24 = 5
          Inoculated-Survived: 12 x 14/24 = 7
          Not-Dead:            12 x 10/24 = 5
          Not-Survived:        12 x 14/24 = 7

  STEP 3  terms:
          (2-5)^2/5 = 1.8000
          (10-7)^2/7 = 1.2857
          (8-5)^2/5 = 1.8000
          (4-7)^2/7 = 1.2857
          chi2 = 6.1714

  STEP 4  df = (2-1)(2-1) = 1 (a 2x2 table)
          compare 6.1714 vs 3.841
          6.1714 > 3.841 -> REJECT H0
```

ANSWER: there is a significant association; the inoculation IS effective (the death rate is
much lower among the inoculated). (machine-verified chi2 = 6.1714; with Yates continuity
correction = 4.2857, still > 3.841, same decision)

TRAP:
```
   1. df for a 2x2 table is 1, not 2.
   2. The Yates correction (2x2-specific) reduces chi2 to 4.2857. The decision is the same,
      but if the question's critical value were between the two, you would need to know
      which convention your course uses. Here it does not matter.
   3. Reading the table axes correctly: the question asks whether INOCULATION matters, so the
      rows are the groups and the columns are dead/survived.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 19 (our paper, ETE re-session S4 B3 - the bulbs t-test, 4 marks)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A sample of 26 bulbs gives a mean life of 990 hours with a standard deviation of
   20 hours. The manufacturer claims a mean life of 1000 hours. Is the sample "not up to
   the standard"? (Useful data: 1.708)
```

STEP 0: DECODE

```
   "is the sample not up to the standard" -> H0: mu = 1000 (the claim), and we ask whether
      the sample gives evidence AGAINST it. n = 26 (small), sigma unknown -> t-test.
   "1.708" -> the t value for 25 df, ONE-tailed at 5% (the question's implied direction)
```

EVERY STEP:

```
  STEP 1  SE = s/sqrt(n) = 20/sqrt(26) = 20/5.0990 = 3.9223
  STEP 2  t = (990 - 1000)/3.9223 = -10/3.9223 = -2.5495
  STEP 3  compare: |t| = 2.5495 vs 1.708
          2.5495 > 1.708 -> REJECT H0
```

ANSWER: yes, the sample is NOT up to the standard; the mean life is below the claimed
1000 hours by a margin that is real at the 5% level. (machine-verified: SE = 3.9223, t = -2.5495)

TRAP:
```
   1. df = n-1 = 25, and the given 1.708 matches 25 df. Do not use 26.
   2. Reading "1.708" as two-tailed: 1.708 IS the one-tailed 5% value for 25 df. The
      question's phrasing ("is the sample not up to standard") is directional.
   3. Reporting the t value without the conclusion sentence. State which way the decision
      goes and what it means for the claim.
```

═══════════════════════════════════════════════════════════════════════════════
F12 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   ERRORS:     Type I  = reject TRUE H0        (alpha, the significance level)
               Type II = keep FALSE H0         (beta)
   LEVEL OF SIGNIFICANCE = P(Type I error)
   CRITICAL REGION = REJECTION region
   t-test compares MEANS (small samples);  F-test compares VARIANCES
   chi-square tests ASSOCIATION between two categorical variables
   ANOVA compares 3+ means via F

   THE PROTOCOL: hypotheses -> pick test -> statistic -> compare with table -> conclude
   FAIL TO REJECT is not "accept"; the wording: "no evidence against ..."

   THE FORMULAS:
     t = (xbar - mu0)/SE,  SE = s/sqrt(n),  df = n-1
     F = larger variance / smaller variance  (F >= 1 by construction)
     expected (chi2) = row total x col total / grand; df = (r-1)(c-1)
     MSB = SSB/(k-1), MSW = SSW/(N-k), F = MSB/MSW
     CI: xbar +/- t_crit x SE  (same t as the test!)

   VERIFIED ANSWERS FROM OUR PAPERS:
     sugar:      t = -0.6203, fail to reject, CI (86.99, 107.41)
     phone:      t = -1.6971, fail to reject (claim supported)
     hotel F:    F = 1.1703, cannot reject (sds equal)
     A vs B:     F = 1.4147, same variance
     chi2:       9.875 > 9.488 -> associated
     ANOVA:      F = 34.6667 > 3.89 -> means differ
```
