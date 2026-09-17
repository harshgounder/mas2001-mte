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
   |  take many independent samples of size n, and look at the AVERAGE    |
   |  of each sample. as n gets large, those averages follow a NORMAL     |
   |  distribution, NO MATTER WHAT THE ORIGINAL POPULATION LOOKS LIKE.    |
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
   |  n > 30, ANY population shape   -> Xbar is normal (CLT)   |
   |  ANY n, population IS normal    -> Xbar is normal         |
   |  n <= 30 and population NOT normal -> CLT does NOT apply  |
   +----------------------------------------------------------+
```

═══════════════════════════════════════════════════════════════════════════════
F9.1  STANDARD ERROR VALUE
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 1 (our paper, ETE 2024-25 S3 A5)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   If the variance of a population is 400 and the sample size is 100, then by the
   central limit theorem Xbar follows the normal distribution with standard
   deviation ..........
```

STEP 0: DECODE - "variance of a population is 400" means sigma^2 = 400, NOT sigma = 400.

```
   sigma^2 = 400   ->  sigma = sqrt(400) = 20      <- THE KEY STEP
   n = 100
   asked: the sd of Xbar, which IS the standard error
```

EVERY STEP:

```
  STEP 1  sigma = sqrt(variance) = sqrt(400) = 20
  STEP 2  SE = sigma / sqrt(n) = 20 / sqrt(100) = 20 / 10
  STEP 3  SE = 2
```

ANSWER: the standard deviation of Xbar is 2.

THE COMPARISON PICTURE:

```
   individual observation:  sd = sigma = 20
   average of 100 of them:  sd = SE = 2      <- ten times tighter

   averaging REDUCES the spread. the reduction factor is sqrt(n) = sqrt(100) = 10.
```

TRAP:
```
   1. Reporting 20 (the population sd) instead of 2 (the SE). Read the ask: "Xbar follows
      ... with standard deviation", so it is the SE.
   2. Using sigma = 400 directly (forgetting to square-root the variance first). Then SE
      = 400/10 = 40, wrong.
   3. Dividing by n instead of sqrt(n): 20/100 = 0.2, wrong.
```

═══════════════════════════════════════════════════════════════════════════════
F9.2  SE BEHAVIOUR
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 2 (our paper, ETE re-session S3 A3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   With all other factors held constant, if the sample size (n) is increased, the
   standard error will:
   a. Increase.   b. Remain the same.   c. Decrease.   d. First increase, then decrease.
```

DECODE: SE = sigma/sqrt(n). n sits in the DENOMINATOR, so bigger n means smaller SE.

ANSWER: (c) Decrease.

THE PICTURE:

```
   SE
    |*
    | *
    |  *
    |    *
    |        * *
    |             * * * *
    +-----------------------> n
   the curve falls. more data -> tighter estimate -> smaller error.
```

TRAP: choosing (a) "increase" by mixing up n's position. Remember: n is in the DENOMINATOR
(under the square root), so bigger n gives a smaller SE. A physical check: more measurements
should make your average MORE reliable, not less.

═══════════════════════════════════════════════════════════════════════════════
F9.3 + F9.4  THE TWO APPLICABILITY MCQs
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 3 (our paper, ETE 2025 summer Q9)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Central limit theorem applies to
   (A) Small samples only
   (B) Any distribution with large sample size
   (C) Only normal distributions
   (D) Only discrete variables
```

ANSWER: (B) any distribution, provided the sample size is large.

WHY: the CLT's whole point is that the ORIGINAL distribution can be anything. The requirement
is on n (large), not on the shape.

TRAP: (C) "only normal distributions" is the most tempting wrong answer. It inverts the
theorem: the CLT is precisely what lets you USE the normal distribution when the population is
NOT normal.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 4 (our paper, ETE 2025 summer Q10)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   As sample size increases, sampling distribution approaches
   (A) Binomial   (B) Poisson   (C) Normal   (D) Uniform
```

ANSWER: (C) Normal.

WHY: that is the CLT statement again, from the other direction. The larger n is, the closer
the distribution of the sample mean comes to normal.

═══════════════════════════════════════════════════════════════════════════════
F9.5  CLT PROBABILITY:  the full worked solve
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 5 (the deck's own example, lms-standard-error-clt p011-p012 - also on the MTE paper)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   The wait times at a bank ATM follow a heavily right-skewed distribution.
   Population parameters: mean wait time mu = 4 minutes, standard deviation sigma = 2
   minutes. If we track a random sample of 36 customers (n = 36), what is the probability
   that their average wait time is greater than 4.5 minutes?
```

STEP 0: DECODE - four things to note before computing.

```
   "heavily right-skewed"  -> the population is NOT normal. this matters for whether we can
                              use the normal table at all.
   "n = 36"                -> 36 >= 30, so the CLT DOES apply despite the skew.
   "average wait time"     -> we are looking at Xbar, so use SE = sigma/sqrt(n).
   "greater than 4.5"      -> an upper tail.
```

THE MASTER FLOWCHART (use this for every CLT probability question):

```
              START
                |
                v
   +-----------------------------+
   | 1. is n >= 30, or is the     |   if NO -> cannot use the normal table
   |    population normal?        |            (the CLT does not apply)
   +--------------+--------------+   if YES -> continue
                  |
                  v
   +-----------------------------+
   | 2. compute SE = sigma/sqrt(n)|
   +--------------+--------------+
                  |
                  v
   +-----------------------------+
   | 3. z = (xbar - mu) / SE      |   NOT / sigma! the denominator is SE
   +--------------+--------------+
                  |
                  v
   +-----------------------------+
   | 4. read the table for the    |
   |    direction asked           |
   +-----------------------------+
```

EVERY STEP:

```
  STEP 1  applicability: n = 36 >= 30, so Xbar is approximately normal even though the
          population is skewed. the CLT is what licenses the next steps.

  STEP 2  the standard error:
          SE = sigma / sqrt(n) = 2 / sqrt(36) = 2 / 6 = 0.3333

  STEP 3  standardise with the SE:
          z = (xbar - mu) / SE = (4.5 - 4) / 0.3333
            = 0.5 / 0.3333
            = 1.50

  STEP 4  "greater than" is an upper tail, so use the cumulative form:
          P(Xbar > 4.5) = 1 - F(1.5) = 1 - 0.9332 = 0.0668
          (or with the phi table: 0.5 - phi(1.5) = 0.5 - 0.4332 = 0.0668, same answer)
```

ANSWER: 0.0668, about 6.7 percent.

THE PICTURE:

```
   distribution of Xbar:  ###
                          #####
                         #######
                        #########
                     -------|------->
                          mu=4  4.5
                          |<-0.3333->|
                          the tail beyond 4.5 is 6.68%
```

TRAP:
```
   1. USING sigma INSTEAD OF SE. This is the single most common CLT error. Without the sqrt(n)
      the answer is quite different.
   2. Refusing to apply the normal table because the population is "heavily skewed". That is
      exactly what the CLT is for; n=36 licenses it.
   3. Using the lower tail (0.9332) instead of the upper (0.0668) for "greater than".
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 6 (the deck's example 2, p013-p014 - the impurity example)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   The amount of impurity in a batch of a chemical product is a random variable with
   mean 4.0 g and standard deviation 1.5 g. If 50 batches are independently prepared,
   what is the approximate probability that the average amount of impurity in these
   50 batches is between 3.5 g and 3.8 g?
```

STEP 0: DECODE

```
   mu = 4.0, sigma = 1.5, n = 50  (>= 30, so CLT applies)
   "average amount"  -> Xbar, use SE
   "between 3.5 and 3.8"  -> an interval
```

EVERY STEP:

```
  STEP 1  SE = sigma / sqrt(n) = 1.5 / sqrt(50) = 1.5 / 7.0711 = 0.2121

  STEP 2  z for the lower end 3.5:
          z = (3.5 - 4.0) / 0.2121 = -0.5 / 0.2121 = -2.357

  STEP 3  z for the upper end 3.8:
          z = (3.8 - 4.0) / 0.2121 = -0.2 / 0.2121 = -0.943

  STEP 4  BOTH z's are negative (same sign), so we SUBTRACT the cumulative values:
          P = F(-0.943) - F(-2.357)
            = 0.1728 - 0.0092
            = 0.1636
          (with the phi table: |phi(0.94) - phi(2.36)| = |0.3264 - 0.4909| = 0.1645, matching
           the deck's stated 0.1644 when using the printed table values)
```

ANSWER: approximately 0.164 (about 16 percent).

PICTURE:

```
   ####|   |###
   ---(-2.36)---(-0.94)---0----
      |<-0.0092->|
      |<--------------->|   <- the interval we want sits entirely LEFT of the mean
          the answer is the thin slice between those two points
```

TRAP:
```
   1. Adding the phi values when both z's have the SAME sign. The rule (from F6): same sign
      -> subtract; opposite signs -> add. Draw the picture.
   2. Using sigma = 1.5 in the denominator instead of SE = 0.2121.
   3. Arithmetic: both z's are negative, so both table look-ups are below 0.5.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 7 (the deck's example 3, p015 - the LED bulbs, and the MTE machine-life twin)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A factory produces LED bulbs. The lifespan of these bulbs is heavily skewed. The mean
   life span is 50,000 hours with a standard deviation of 8,000 hours. A quality control
   inspector tests a random sample of 64 bulbs. What is the probability that the average
   lifespan of this batch is less than 48,000 hours?
```

EVERY STEP:

```
  STEP 1  n = 64 >= 30, so the CLT applies despite the skew.
  STEP 2  SE = 8000 / sqrt(64) = 8000 / 8 = 1000
  STEP 3  z = (48000 - 50000) / 1000 = -20000/1000 = -2.0
  STEP 4  "less than" is a lower tail: P = F(-2.0) = 0.0228
```

ANSWER: 0.0228, about 2.3 percent.

THE MTE TWIN (MTE 2025-26 Q7, solved in full in F6.4):
```
   the MTE asked the same shape with machine lives: mu = 7, sigma = 1, n = 9, between
   6.4 and 7.2. Note n = 9 there, which is BELOW 30 - but the question states the lives
   follow a normal distribution, so the CLT is not even needed. That is the F6 case
   (population normal -> any n works).
```

═══════════════════════════════════════════════════════════════════════════════
F9 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   CLT: the sample mean of a large sample is approximately normal, whatever the population.
        mean of Xbar = mu ;  sd of Xbar = sigma/sqrt(n) = SE

   APPLICABILITY:
     n > 30, any shape        -> OK
     any n, normal population -> OK
     n <= 30, non-normal      -> NOT OK

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
     refusing to apply the normal table to a skewed population when n >= 30
     same-sign vs opposite-sign z handling in the interval

   CONNECTION: this family feeds F6 (the normal solves) and F8 (the CI uses the same SE).
```
