# F9-clt-sampling GUIDE: the explanation content behind the questions

This is the non-question content from the family file: the family intro, the
toolboxes, the section intros, decision trees, and the summary card. It is the
TEACHING layer. Read it first (it gives the method), then drill the q*.md files.

Source: deck/worked/F9-clt-sampling.md (same content; this file just isolates it).


──────────────────────────────────────────────────────────────────────────────
[FAMILY INTRO / PREAMBLE (before the first question)]
──────────────────────────────────────────────────────────────────────────────

# F9 CLT AND SAMPLING: every shape, every question, solved from zero

Source: our own material (the ETE papers E24S3, E25SUM, R25S3, and the lms-standard-error-clt
deck's own worked examples). Nothing invented. Every number machine-checked (10/10 checks).

```
  SHAPES IN THIS FILE
  F9.1  standard error value   fill in the SE               1 question
  F9.2  SE behaviour           what happens when n grows    1 question
  F9.3  CLT applicability      MCQ                           1 question
  F9.4  sampling distribution  approaches what              1 question
  F9.5  CLT probability        the full worked solve         3 deck questions
```

═══════════════════════════════════════════════════════════════════════════════
BEFORE ANY QUESTION: what the CLT says, in plain words
═══════════════════════════════════════════════════════════════════════════════

```
   +---------------------------------------------------------------------+
   |  THE CENTRAL LIMIT THEOREM (CLT):                                    |
   |                                                                     |
   |  take independent observations and look at their AVERAGE. under the  |
   |  usual CLT conditions, as n gets large, those averages approach a    |
   |  NORMAL distribution, even when the population is not normal.       |
   |                                                                     |
   |  and the averages' spread is:    sigma / sqrt(n)                     |
   |                                  ^^^^^^^^^^^^^^^                     |
   |                                  this is the STANDARD ERROR          |
   +---------------------------------------------------------------------+
```

THE TWO-PARAMETER SUMMARY of the sample mean Xbar:

```
   +----------------------------------+----------------------------------+
   | mean of Xbar   = mu              | same as the population mean      |
   | variance of Xbar = sigma^2 / n   | so sd of Xbar = sigma / sqrt(n)  |
   +----------------------------------+----------------------------------+
                                    |
                                    v
                     the STANDARD ERROR, SE = sigma / sqrt(n)
```

THE PICTURE (why the CLT is magic):

```
   the POPULATION can be any shape:
        skewed:  |#####
                 |########
                 |######
                 |####
                 |##
                 +-------------->

   but the distribution of Xbar (the sample average) becomes:
                                   ###
        n small:    ##          n large:   #####
                   ####                     #######
                  ######                   #########
                  ------                  -----------
                  still skewed            NORMAL, and narrower

   as n grows: (1) the shape becomes normal  (2) the spread shrinks like 1/sqrt(n)
```

THE APPLICABILITY RULES (memorize; two MCQs test this):

```
   +----------------------------------------------------------+
   | n >= 30, any shape -> approximate normal by course       |
   |                   heuristic, not a universal cutoff    |
   | any n, normal population -> normal                       |
   | n < 30, non-normal -> inspect shape and tails; CLT       |
   |                         is not automatic                 |
   +----------------------------------------------------------+
```

═══════════════════════════════════════════════════════════════════════════════
F9.1  STANDARD ERROR VALUE
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q1 and Q2)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F9.2  SE BEHAVIOUR
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q2 and Q3)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F9.3 + F9.4  THE TWO APPLICABILITY MCQs
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q4 and Q5)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F9.5  CLT PROBABILITY:  the full worked solve
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[CLOSING SECTION (after Q8; usually the summary card)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F9 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   CLT: under the usual conditions, the sample mean of a large sample is approximately normal,
        even when the population is not normal.
        mean of Xbar = mu ;  sd of Xbar = sigma/sqrt(n) = SE

   APPLICABILITY:
     n >= 30, any shape        -> approximately OK under the course heuristic
     any n, normal population -> OK
     n < 30, non-normal        -> inspect shape and tails; CLT is not automatic

   THE UNIVERSAL SOLVE:
     1. check applicability
     2. SE = sigma/sqrt(n)
     3. z = (xbar - mu)/SE          <- SE, NOT sigma
     4. read the table for the direction

   BEHAVIOUR MCQ:
     n up  -> SE down (it is 1/sqrt(n))
     variance 400 -> sigma 20 (square-root first)

   TABLES:
     "approaches normal" -> CLT; "applies to any distribution with large n" -> CLT
     "Xbar follows normal with sd ..." -> the answer is the SE

   TOP TRAPS:
     using sigma instead of SE                                     <- the #1 error
     forgetting to sqrt the variance
     treating n >= 30 as a universal theorem cutoff for a skewed population
     same-sign vs opposite-sign z handling in the interval

   CONNECTION: this family feeds F6 (the normal solves) and F8 (the CI uses the same SE).
```
