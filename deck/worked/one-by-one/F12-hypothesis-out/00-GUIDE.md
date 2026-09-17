# F12-hypothesis-testing GUIDE: the explanation content behind the questions

This is the non-question content from the family file: the family intro, the
toolboxes, the section intros, decision trees, and the summary card. It is the
TEACHING layer. Read it first (it gives the method), then drill the q*.md files.

Source: deck/worked/F12-hypothesis-testing.md (same content; this file just isolates it).


──────────────────────────────────────────────────────────────────────────────
[FAMILY INTRO / PREAMBLE (before the first question)]
──────────────────────────────────────────────────────────────────────────────

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
   | Type II error      | failing to reject H0 WHEN IT IS FALSE (missed detection) |
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


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q8 and Q9)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F12.2  ONE-SAMPLE t-TEST:  the full protocol
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q10 and Q11)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F12.3  TWO-SAMPLE F-TEST  (comparing variances)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q12 and Q13)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F12.4  CHI-SQUARE TEST OF ASSOCIATION  (two categorical variables)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q13 and Q14)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F12.5  ONE-WAY ANOVA  (three or more means)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q14 and Q15)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F12.6  MORE PAPER QUESTIONS (the remaining real ones from our corpus)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[CLOSING SECTION (after Q19; usually the summary card)]
──────────────────────────────────────────────────────────────────────────────

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
