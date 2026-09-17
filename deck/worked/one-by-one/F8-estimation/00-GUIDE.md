# F8-estimation GUIDE: the explanation content behind the questions

This is the non-question content from the family file: the family intro, the
toolboxes, the section intros, decision trees, and the summary card. It is the
TEACHING layer. Read it first (it gives the method), then drill the q*.md files.

Source: deck/worked/F8-estimation.md (same content; this file just isolates it).


──────────────────────────────────────────────────────────────────────────────
[FAMILY INTRO / PREAMBLE (before the first question)]
──────────────────────────────────────────────────────────────────────────────

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


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q5 and Q6)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F8.2  VERIFY UNBIASEDNESS:  the full-enumeration method
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q6 and Q7)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F8.3  CONSISTENCY
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q7 and Q8)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F8.4  CONFIDENCE INTERVALS
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q10 and Q11)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F8.5  SUFFICIENCY
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[CLOSING SECTION (after Q16; usually the summary card)]
──────────────────────────────────────────────────────────────────────────────

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
