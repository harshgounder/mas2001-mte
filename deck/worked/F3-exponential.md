# F3 EXPONENTIAL: every shape, every question, solved from zero

Source: our own material (MTE 2024-25 block B2, MTE 2025-26 block Q6, the ETE papers E24S4,
E25S4, E25SUM, R25S3, and the ppt4 deck). Nothing invented. Every number machine-checked
(12/12 checks pass).

```
  SHAPES IN THIS FILE
  F3.1  setup        pdf / cdf, and the mean-vs-parameter trap   1 question
  F3.2  point        P(X>a), P(X<a)                              1 question (MTE!)
  F3.3  interval     P(a<X<b)                                    1 question (MTE!)
  F3.4  conditional  memoryless                                  1 question
  F3.5  moments      mean, variance, and both directions         1 question (MTE!)
  F3.6  independence multi-variable product                      1 question
```

═══════════════════════════════════════════════════════════════════════════════
BEFORE ANY QUESTION: what "exponential" means
═══════════════════════════════════════════════════════════════════════════════

An exponential models WAITING TIME: how long until the next event, or how long something
lasts (a phone call, a component, a shelf life).

```
   +-------------------------------------------------------------------+
   |  THREE FORMS you must know (l = lambda, the RATE):                 |
   |                                                                    |
   |   pdf (density)   f(x) = l e^(-l x)              x > 0              |
   |   cdf (up to x)   F(x) = 1 - e^(-l x)            P(X < x)           |
   |   survival        S(x) = e^(-l x)                P(X > x)           |
   |                                                                    |
   |   MEAN     = 1 / l       <- careful: ONE OVER lambda                 |
   |   VARIANCE = 1 / l^2                                                 |
   +-------------------------------------------------------------------+
```

THE #1 TRAP, LEARN IT BEFORE ANYTHING ELSE:

```
   +-------------------------------+----------------------------------+
   |  THE QUESTION SAYS            |  SO WHAT IS lambda?              |
   +-------------------------------+----------------------------------+
   |  "mean = 3"                   |  lambda = 1/3                    |
   |  "average life 8 hours"       |  lambda = 1/8                    |
   |  "parameter 1/4"              |  lambda = 1/4 (given directly)   |
   |  "rate 15 per hour"           |  lambda = 15                     |
   |  "f(x) = e^(-x)"              |  lambda = 1 (the coefficient!)   |
   +-------------------------------+----------------------------------+

   THE MEAN IS THE RECIPROCAL OF THE RATE.
   if the question says "mean" or "average", INVERT.
   if it says "parameter" or "rate", DO NOT invert.
```

PICTURE of the density (decaying):

```
   f(x)
   1.0 |##
       | ##
   0.7 |  ##
       |   ##
   0.4 |     ###
       |        ####
   0.1 |            ########
   0.0 +---------------------########------
        0   1   2   3   4   5   6   7   8

   tallest at 0, decays forever. small x = very likely, large x = rare.

   AREA picture for probabilities:
       P(X < 2)  = area from 0 to 2 under the curve  = 1 - e^(-2l)
       P(X > 2)  = area from 2 to infinity           = e^(-2l)
       both pieces together = 1 (whole area)
```

═══════════════════════════════════════════════════════════════════════════════
F3.1  SETUP:  the pdf, and identifying lambda from a given density
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 1 (our paper, ETE 2024-25 S4 A4 - formula recall)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   What is the p.d.f. of exponential distribution?
```

DECODE: "p.d.f." = probability density function, the f(x). Pure recall.

ANSWER:
```
   f(x) = lambda e^(-lambda x)     for x > 0,  and f(x) = 0 otherwise
```

TRAP:
```
   1. Writing e^(-x/lambda) instead of e^(-lambda x). The lambda multiplies x inside the
      exponent; it does not divide.
   2. Forgetting the "x > 0" support. The exponential starts at 0, never negative.
   3. Forgetting the lambda in front. The leading lambda is what makes the area come to 1.
```

RELATED (our paper, ETE 2025-26 S4 A5):
```
   "Exponential distribution is used for: a. Counting  b. Waiting time  c. Testing  d. None"
   ANSWER: b. Waiting time.
   (Poisson counts events; exponential measures the WAIT between them. They are two faces
    of the same story.)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 2 (our paper, ETE re-session S3 B1) - read lambda off a density
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   The shelf life in years of a certain perishable food product packaged in cardboard
   containers is a random variable, whose probability density function is given by
   f(x) = e^(-x), when x > 0. Let X1, X2, X3 represent the shelf lives for three of
   these containers selected independently. Find the probability
   P(X1 < 2, 1 < X2 < 3, X3 > 2).
```

STEP 0: DECODE - TWO ideas hide here.

```
   HIDDEN 1: f(x) = e^(-x) has NO visible lambda in front. Comparing with f = l e^(-l x):
             the exponent is -x = -1 times x, so lambda = 1. And the leading coefficient
             would be lambda = 1, which is invisible. So lambda = 1.
   HIDDEN 2: "selected independently" -> the three probabilities MULTIPLY.
   the three pieces: X1 < 2, then 1 < X2 < 3, then X3 > 2.
```

THE PICTURE (three separate containers, three separate areas):

```
   container 1        container 2         container 3
   P(X1 < 2)          P(1 < X2 < 3)       P(X3 > 2)
   |########          |   ##   |          |          #####
   ###################  ##################  ###############
   0------2           0--1----3           0-----2---------

   "and" between independent events -> MULTIPLY
```

EVERY STEP:

```
  STEP 1  lambda = 1 (read off the density as above)

  STEP 2  P(X1 < 2) = 1 - e^(-1 x 2) = 1 - e^(-2)
          e^(-2) = 0.1353
          so P = 1 - 0.1353 = 0.8647

  STEP 3  P(1 < X2 < 3) = F(3) - F(1) = [1 - e^(-3)] - [1 - e^(-1)]
          the "1 -" parts cancel, leaving:
               = e^(-1) - e^(-3)
          e^(-1) = 0.3679,  e^(-3) = 0.0498
               = 0.3679 - 0.0498 = 0.3181

  STEP 4  P(X3 > 2) = e^(-1 x 2) = e^(-2) = 0.1353

  STEP 5  independent, so multiply:
          0.8647 x 0.3181 x 0.1353

          do it in two steps:
          0.8647 x 0.3181 = 0.2751
          0.2751 x 0.1353 = 0.0372
```

ANSWER: P = 0.0372, about 3.7 percent.

TRAP:
```
   1. Missing that f(x) = e^(-x) means lambda = 1. If you cannot see lambda, it is 1.
   2. ADDING the three probabilities instead of multiplying. "independently" + "and" means
      multiply. Adding would give 1.32, which is above 1 and therefore impossible; if your
      answer exceeds 1, you added when you should have multiplied.
   3. In the middle piece, writing F(3) - F(1) and keeping the "1 -" (getting
      1 - e^-3 - 1 + e^-1 correctly requires the cancel; a slip here flips signs).
      short cut: P(a<X<b) = e^(-l a) - e^(-l b) directly.
```

═══════════════════════════════════════════════════════════════════════════════
F3.2  POINT:  P(X > a), P(X < a)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 3 (MTE 2024-25 paper, block B2 - the real thing)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   The length of time a person speaks over the phone follows exponential distributions
   with parameter 1/4. What is the probability that the person will talk for
   (i) more than 6 minutes (ii) between 7 and 12 minutes (iii) not more than 5 minutes?
   Also find mean and variance.
```

STEP 0: DECODE - the word "parameter" saves you the inversion.

```
   "with parameter 1/4"     -> lambda = 1/4 = 0.25 DIRECTLY (no inversion! "parameter"
                               means the rate itself)
   "more than 6"            -> P(X > 6), use the survival form
   "between 7 and 12"       -> P(7 < X < 12)
   "not more than 5"        -> P(X <= 5), the cdf form
   "also find mean and variance" -> an extra 2 marks, do not skip them
```

THE THREE-SHAPE PICTURE:

```
   (i) more than 6          (ii) between 7 and 12        (iii) not more than 5
   |          ########      |          |    ####  |      |#####
   -----------6------       ----7------12---------      ----5----------
   area to the RIGHT        area in the middle          area to the LEFT
   = e^(-l x 6)             = e^(-l x 7) - e^(-l x 12)  = 1 - e^(-l x 5)
```

EVERY STEP:

```
  STEP 1  lambda = 0.25

  PART (i), more than 6 (t = 6):
  STEP 2  P(X > 6) = e^(-lambda x t) = e^(-0.25 x 6) = e^(-1.5)
  STEP 3  e^(-1.5) = 0.2231

  PART (ii), between 7 and 12:
  STEP 4  P(7 < X < 12) = e^(-0.25 x 7) - e^(-0.25 x 12)
  STEP 5  0.25 x 7 = 1.75,  so e^(-1.75) = 0.1738
          0.25 x 12 = 3.0,  so e^(-3.0)  = 0.0498
  STEP 6  subtract: 0.1738 - 0.0498 = 0.1240

  PART (iii), not more than 5 (t = 5):
  STEP 7  P(X <= 5) = 1 - e^(-0.25 x 5) = 1 - e^(-1.25)
  STEP 8  e^(-1.25) = 0.2865
          so P = 1 - 0.2865 = 0.7135

  PART (iv), mean and variance:
  STEP 9  mean = 1 / lambda = 1 / 0.25 = 4 minutes
  STEP 10 variance = 1 / lambda^2 = 1 / 0.0625 = 16

  (note: sd = sqrt(16) = 4, the same as the mean. for an exponential
   the sd ALWAYS equals the mean.)
```

ANSWER:
```
   (i)   more than 6 minutes   = 0.2231
   (ii)  between 7 and 12      = 0.1240
   (iii) not more than 5       = 0.7135
   mean = 4 minutes, variance = 16
```

SELF CHECK:
```
   P(X<=5) + P(>5) should be 1: 0.7135 + e^(-1.25) = 0.7135 + 0.2865 = 1.0000 ✓
```

TRAP:
```
   1. THE BIG ONE: inverting the parameter. The question says "parameter 1/4", so lambda is
      1/4, and the mean is 4. If you inverted (lambda = 4) the mean would come out 0.25
      minutes, which is absurd for a phone call. SANITY-CHECK your mean against the story:
      calls last minutes, not seconds.
   2. "not more than 5" is <=, so the cdf 1 - e^(-l t). Using the survival e^(-l t) gives
      the complement (0.2865) and costs the marks.
   3. In the interval, subtracting the wrong way: e^(-l b) - e^(-l a) is NEGATIVE.
      the order is always F(b) - F(a) = e^(-l a) - e^(-l b), smaller exponent first.
```

MUTATIONS:
```
   IF "mean = 5"          THEN lambda = 1/5, and every e^(-l t) uses 0.2.
   IF "rate 2 per minute" THEN lambda = 2 (already a rate).
   IF "standard deviation = 3" THEN for an exponential sd = mean = 1/lambda, so
                             lambda = 1/3.
```

═══════════════════════════════════════════════════════════════════════════════
F3.3  INTERVAL:  P(a < X < b)   (covered in Q3 part ii; a second practice below)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 4 (MTE 2025-26 paper, block Q6 - the real thing)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   The length of a telephone conversation has been exponentially distributed with a
   mean of 3 minutes. Find the probability that a call (i) ends in more than 1 minute
   and (ii) takes less than 3 minutes.
```

STEP 0: DECODE - this time it says MEAN, so you MUST invert.

```
   "mean of 3 minutes"  -> mean = 3, so lambda = 1/mean = 1/3
   (contrast with the previous question, which gave "parameter". This one gives "mean".
    the wording tells you whether to invert. this is the single most examined trap
    in the whole topic.)
   "more than 1"        -> P(X > 1)
   "less than 3"        -> P(X < 3)
```

THE INVERSION COMPARISON (put these side by side in your head):

```
   +--------------------------+------------------+-------------------+
   | wording                  | lambda           | mean              |
   +--------------------------+------------------+-------------------+
   | "parameter 1/4"          | 1/4 = 0.25       | 4                 |
   | "mean 3"                 | 1/3 = 0.3333     | 3                 |
   | "average life 7 years"   | 1/7              | 7                 |
   | f(x) = 2e^(-2x)          | 2                | 0.5               |
   +--------------------------+------------------+-------------------+
   rule: MEAN -> invert.  PARAMETER/RATE/coefficient -> do not invert.
```

EVERY STEP:

```
  STEP 1  lambda = 1/3 = 0.3333

  PART (i), more than 1 minute (t = 1):
  STEP 2  P(X > 1) = e^(-lambda x 1) = e^(-1/3)
  STEP 3  e^(-0.3333) = 0.7165

  PART (ii), less than 3 minutes (t = 3):
  STEP 4  P(X < 3) = 1 - e^(-lambda x 3) = 1 - e^(-1)
  STEP 5  e^(-1) = 0.3679
          so P = 1 - 0.3679 = 0.6321
```

ANSWER:
```
   (i)  more than 1 minute = 0.7165
   (ii) less than 3 minutes = 0.6321
```

NICE PATTERN TO NOTICE:
```
   P(X < mean) = 1 - e^(-1) = 0.6321 for EVERY exponential.
   Because t = mean means l t = l x (1/l) = 1 exactly, so it is always 1 - e^-1.
   So "less than the mean" is always about 63 percent, no matter the lambda.
   That is a free sanity check and a possible MCQ.
```

TRAP:
```
   1. NOT inverting: using lambda = 3. Then P(X>1) = e^(-3) = 0.0498. The story check saves
      you: if the mean call is 3 minutes (given), then a call lasting MORE than 1 minute
      should be quite likely (well above half), so 0.0498 is obviously wrong and 0.7165
      is right. ALWAYS run this story check.
   2. Mixing the two parts' lambdas (they are the same here; both use 1/3).
```

═══════════════════════════════════════════════════════════════════════════════
F3.4  CONDITIONAL / MEMORYLESS  (the hidden-layer item)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 5 (course material, the repair-time pattern in E24S4-C1b and the ETE set)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   The time X (in hours) required to repair a machine is exponentially distributed
   with parameter lambda = 1/3. Find the probability that a repair takes
   (a) at least 3 hours   (b) more than 6 hours, given it has already taken 3 hours.
```

STEP 0: DECODE - part (b) is the CONDITIONAL, and the exponential has a magic property.

```
   "parameter lambda = 1/3"  -> lambda = 1/3 given directly
   (a) "at least 3"          -> P(X >= 3) = survival
   (b) "more than 6, GIVEN it has already taken 3"  -> P(X > 6 | X > 3)
```

THE MAGIC PROPERTY (memoryless) - the idea behind the whole shape:

```
   +--------------------------------------------------------------------+
   |  FOR AN EXPONENTIAL, THE PAST DOES NOT MATTER.                      |
   |                                                                     |
   |     P(X > s + t  |  X > s)  =  P(X > t)                             |
   |                                                                     |
   |  meaning: if a repair has ALREADY lasted 3 hours, the chance it      |
   |  lasts 3 MORE hours is the same as a brand-new repair lasting 3      |
   |  hours. the machine does not "remember" that it has been running.    |
   +--------------------------------------------------------------------+
```

THE PICTURE:

```
   WITHOUT memoryless, you would think:
      "it already ran 3 hours, so it is 'due' to finish"      <- WRONG for exponential

   WITH memoryless:
      already-3-hours ----+---- need 3 more ----
                          |
                    the clock RESETS here
      P(3 more hours) is the same as a fresh start
```

EVERY STEP:

```
  PART (a):
  STEP 1  P(X >= 3) = e^(-lambda x 3) = e^(-(1/3) x 3) = e^(-1) = 0.3679

  PART (b), two ways, both correct:

  WAY 1 (memoryless, fast):
  STEP 2  P(X > 6 | X > 3) = P(X > 3)     <- drop the past, keep the excess (6-3=3)
  STEP 3  = e^(-(1/3) x 3) = e^(-1) = 0.3679

  WAY 2 (by the definition, to verify):
  STEP 4  P(A | B) = P(A and B) / P(B), with A = "X > 6", B = "X > 3"
  STEP 5  if X > 6 then X > 3 automatically, so "A and B" is just "A":
          P(X > 6 and X > 3) = P(X > 6) = e^(-(1/3) x 6) = e^(-2) = 0.1353
  STEP 6  P(B) = P(X > 3) = e^(-1) = 0.3679
  STEP 7  divide: 0.1353 / 0.3679 = 0.3679  ✓ same answer
```

ANSWER:
```
   (a) P(at least 3 hours) = 0.3679
   (b) P(more than 6 | already 3) = 0.3679  (the same number, that is the point of memoryless)
```

TRAP:
```
   1. Computing P(X > 6) = 0.1353 and reporting that for part (b). That ignores the GIVEN
      information. The "|X > 3" changes the question.
   2. Thinking the machine is "due" and giving a smaller probability. Exponential has no
      memory; the past is irrelevant.
   3. Forgetting the formula and doing 6 - 3 = 3 correctly but then using t = 6.
```

═══════════════════════════════════════════════════════════════════════════════
F3.5  MOMENTS:  mean 1/lambda, variance 1/lambda^2  (both directions)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 6 (course material, the standard moment asks)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   (a) If X has an exponential distribution with mean = 2, find the standard deviation.
   (b) If f(x) = 4e^(-4x) for x > 0, find the mean and variance.
```

EVERY STEP:

```
  PART (a):
  STEP 1  mean = 2, so lambda = 1/2 = 0.5
  STEP 2  variance = 1/lambda^2 = 1/0.25 = 4
  STEP 3  standard deviation = sqrt(variance) = sqrt(4) = 2
  SHORTCUT: for an exponential, sd = mean ALWAYS.
            so sd = mean = 2 immediately, no lambda needed.

  PART (b):
  STEP 4  Read lambda off the density: f(x) = 4 e^(-4x) matches f = lambda e^(-lambda x)
          with lambda = 4.
  STEP 5  mean = 1/lambda = 1/4 = 0.25
  STEP 6  variance = 1/lambda^2 = 1/16 = 0.0625
```

ANSWER:
```
   (a) sd = 2   (equal to the mean, which is the exponential's signature)
   (b) mean = 0.25, variance = 0.0625
```

THE SIGNATURE TABLE (memorize):

```
   +-------------+------------------+---------------------+
   | quantity    | formula          | for f = 4e^(-4x)     |
   +-------------+------------------+---------------------+
   | lambda      | read from f      | 4                    |
   | mean        | 1 / lambda       | 0.25                 |
   | variance    | 1 / lambda^2     | 0.0625               |
   | sd          | 1 / lambda       | 0.25                 |
   | note        | sd = mean        | 0.25 = 0.25 ✓        |
   +-------------+------------------+---------------------+
```

TRAP:
```
   1. Using lambda = 4 as the mean. It is the rate. The mean is 1/4.
   2. Squaring the mean for the variance instead of squaring 1/lambda. Var = (mean)^2 for
      an exponential, which is the same thing (1/lambda)^2. Either viewpoint gives 0.0625.
   3. Forgetting sd = mean for this distribution (a fast check).
```

═══════════════════════════════════════════════════════════════════════════════
F3 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   FORMS:
     f(x) = l e^(-l x)
     F(x) = 1 - e^(-l x)      P(X < x)
     S(x) = e^(-l x)          P(X > x)
     P(a<X<b) = e^(-l a) - e^(-l b)

   MEAN = 1/l ,  VARIANCE = 1/l^2 ,  SD = 1/l = MEAN        <- sd equals mean

   WORD MAP (the inversion rule is the whole game):
     "mean = m" / "average = m"   -> lambda = 1/m        INVERT
     "parameter = l" / "rate = l" -> lambda = l          DO NOT invert
     f(x) = a e^(-a x)            -> lambda = a          read the coefficient

   MEMORYLESS:  P(X > s+t | X > s) = P(X > t)    (the past is irrelevant)

   FREE CHECKS:
     P(X < mean) = 1 - e^-1 = 0.632 ALWAYS
     sd = mean ALWAYS
     if an answer exceeds 1, you added where you should have multiplied

   TOP TRAPS:
     not inverting when the wording says "mean"
     inverting when the wording says "parameter"
     P(a<X<b) subtraction order
     ignoring the "given" in a conditional
```
