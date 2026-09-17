# F6 NORMAL: every shape, every question, solved from zero

Source: our own material (MTE 2024-25 block C1, MTE 2025-26 block Q7, the ETE papers E24S3,
E25S3, E24S4, E25SUM, R25S4, and the ppt4 deck). Nothing invented. Every number
machine-checked.

CRITICAL DISCOVERY WHILE BUILDING THIS FILE: our course papers use the PHI table (area from
the mean), NOT the cumulative table. This is the single most important fact in this topic and
it is explained in the next block. Getting it wrong makes every normal answer wrong.

```
  SHAPES IN THIS FILE
  F6.1  standard normal MCQ    mean/variance of N(0,1)        2 questions
  F6.2  tail                   P(X>a), P(X<a)                 1 question (MTE!, 4 parts)
  F6.3  interval + binomial    the composite                   (same MTE question)
  F6.4  sample mean (CLT)      Xbar with SE denominator         1 question (MTE!)
  F6.5  two-unknown inverse    31% under 45, 8% over 64         1 question
```

═══════════════════════════════════════════════════════════════════════════════
THE TWO TABLES (read this twice; everything else depends on it)
═══════════════════════════════════════════════════════════════════════════════

There are two ways to print a normal table and they give DIFFERENT numbers for the same z.

```
   +--------------------------+--------------------------------------+
   | CUMULATIVE table  F(z)   | AREA-FROM-MEAN table  phi(z)          |
   | "everything to the LEFT" | "from the centre to z"                |
   +--------------------------+--------------------------------------+
   |                          |                                       |
   |      ###|                |           ###|                        |
   |   ###########            |  #  ###########                       |
   | ---z--------             | ----------0---------z-----            |
   |                          |           ^ this shaded part          |
   | F(0) = 0.5000            | phi(0) = 0.0000                       |
   | F(1.5) = 0.9332          | phi(1.5) = 0.4332                     |
   | F(-1.5) = 0.0668         | phi(-1.5) = 0.4332 (symmetric!)       |
   +--------------------------+--------------------------------------+
              |                              |
              |  relationship:               |
              |  F(z)   = 0.5 + phi(z)  for z > 0
              |  F(z)   = 0.5 - phi(|z|) for z < 0
              +------------------------------+
```

WHICH ONE ARE OUR PAPERS USING? Read the useful data:
```
   M25-Q7 gives: phi(1.8) = 0.4641, phi(0.6) = 0.2257
   the CUMULATIVE F(1.8) is 0.9641, not 0.4641.
   0.4641 is the AREA FROM THE MEAN.  so the papers use the PHI table.

   M24-C1 gives: phi(0.58) = 0.219, phi(0.27) = 0.1064 - also phi values.

   => WHEN A QUESTION PRINTS "useful data" AS phi(x) = small number, IT IS THE AREA-FROM-MEAN
      TABLE. USE THE CONVERSIONS ABOVE.
```

THE CONVERSION CHEAT-SHEET (all four cases, memorize the pattern):

```
   +--------------------------------+-----------------------------+
   | you want                       | from phi(x)                 |
   +--------------------------------+-----------------------------+
   | P(X < a), z = a positive       | 0.5 + phi(z)                |
   | P(X < a), z = a negative       | 0.5 - phi(|z|)              |
   | P(X > a), z = a positive       | 0.5 - phi(z)    (upper tail)|
   | P(X > a), z = a negative       | 0.5 + phi(|z|)              |
   | P(a<X<b), both z same sign     | |phi(z_big) - phi(z_small)| |
   | P(a<X<b), z's opposite signs   | phi(|z1|) + phi(z2)         |
   +--------------------------------+-----------------------------+
```

PICTURE of the last row (opposite signs, the most common case):

```
       ####|      |####
   ----z1----0----z2----
      |<--phi1-->|<--phi2-->|
      total = phi1 + phi2
```

═══════════════════════════════════════════════════════════════════════════════
BEFORE ANY QUESTION: what "normal" means
═══════════════════════════════════════════════════════════════════════════════

```
   +--------------------------------------------------------------------+
   |  X ~ N(mu, sigma^2)                                                  |
   |                                                                     |
   |  THE SECOND NUMBER IS THE VARIANCE, NOT THE SD.                      |
   |  N(2.6, 34.5) means mean 2.6, variance 34.5, so sd = sqrt(34.5) =     |
   |  5.8737. THIS IS A CLASSIC EXAM TRAP.                               |
   |                                                                     |
   |  STANDARDISE:  z = (X - mu) / sigma                                  |
   |  FOR A SAMPLE MEAN:  z = (Xbar - mu) / (sigma / sqrt(n))             |
   +--------------------------------------------------------------------+
```

THE BELL PICTURE:

```
                   ###
                ########
              ############
            ################
          ####################
        ########################
      ############################
    -----------------------------------
            mu        mu+sigma
    |<--68%-->|  (within 1 sd)
    |<----95%---->|  (within 2 sd)
    |<------99.7%------>|  (within 3 sd)
```

═══════════════════════════════════════════════════════════════════════════════
F6.1  STANDARD NORMAL MCQ
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 1 (our paper, ETE 2025-26 S3 A5)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   For a standard normal variate, the value of mean is?
   a) infinity    b) 1    c) 0    d) Not defined
```

DECODE: "standard normal variate" = N(0, 1). By definition its mean is 0.

ANSWER: (c) 0.

RELATED (our paper, ETE 2024-25 S4 A5):
```
   "Mean and variance of standard normal variate are……..."
   ANSWER: mean 0, variance 1.
```

THE REFERENCE CARD:
```
   +-------------------------+--------+----------+
   | distribution            | mean   | variance |
   +-------------------------+--------+----------+
   | N(0,1) standard normal  | 0      | 1        |
   | N(mu, sigma^2) general  | mu     | sigma^2  |
   +-------------------------+--------+----------+
```

TRAP: choosing (b) 1 (that is the variance) or (a) infinity (the range is infinite, the mean
is not).

═══════════════════════════════════════════════════════════════════════════════
F6.2 + F6.3  TAIL and INTERVAL + the binomial composite
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 2 (MTE 2024-25 paper, block C1 - the real thing, the hardest block on the paper)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   The amount of rain (X mm) per day during rainy season is assumed to follow N(2.6, 34.5).
   Find the probability that, in a randomly selected day, the amount of rainfall is
   (i) 6 mm or more  (ii) less than 1 mm  (iii) 1.5 mm to 4.6 mm
   (iv) What is the probability that in a randomly selected week at most 2 days the
   rainfall will be between 1.5 mm to 4.6 mm?
   (Useful Data: phi(0.58) = 0.219, phi(0.27) = 0.1064, phi(0.19) = 0.075, phi(0.34) = 0.133)
```

STEP 0: DECODE - four parts, and part (iv) is a COMPOSITE that reuses part (iii).

```
   "N(2.6, 34.5)"    -> mean mu = 2.6, VARIANCE = 34.5, so sigma = sqrt(34.5) = 5.8737
   "(i) 6 or more"   -> P(X >= 6), an upper tail
   "(ii) less than 1"-> P(X < 1), a lower tail
   "(iii) 1.5 to 4.6"-> P(1.5 < X < 4.6), an interval
   "(iv) at most 2 days in a week" -> BINOMIAL with n=7, p = the answer to (iii)!
```

THE STRUCTURE OF THE WHOLE QUESTION (draw this first):

```
   +----------------------------+
   | N(2.6, 34.5)               |
   | sigma = sqrt(34.5)=5.8737  |
   +-------------+--------------+
                 |
      +----------+----------+-----------+
      |          |          |           |
      v          v          v           v
   (i) tail  (ii) tail  (iii) interval  |
   P(X>=6)   P(X<1)     P(1.5<X<4.6)   |
                              |         |
                              v         |
                    +-------------------+
                    | (iv) binomial:    |
                    | n=7, p = (iii)    |
                    | P(at most 2 days) |
                    +-------------------+
```

STEP 1: THE MASTER CONVERSION (sigma)

```
   sigma = sqrt(34.5)
   sqrt(34.5): 5.8^2 = 33.64 ; 5.9^2 = 34.81, so sigma is between 5.8 and 5.9
   more precisely: 5.8737 (since 5.8737^2 = 34.499...)
```

═══════════════ PART (i): 6 mm or more ═══════════════

IN PLAIN: how likely is a day with 6 mm or more rain, when the average is 2.6?

EVERY STEP:

```
  STEP 1  standardise: z = (X - mu)/sigma = (6 - 2.6)/5.8737 = 3.4/5.8737
  STEP 2  3.4 / 5.8737 = 0.5789
  STEP 3  the paper's table gives phi(0.58) = 0.219
  STEP 4  "6 or more" is an UPPER TAIL, so use the upper-tail conversion:
          P(X >= 6) = 0.5 - phi(0.58)
                    = 0.5 - 0.219
                    = 0.281
```

PICTURE:

```
      ####|       #####
   -------0-------0.58----->
          |        |
          |<-0.219->|<-0.281->|
       (0.5 total to the left, 0.5 to the right of 0)
   the tail beyond 0.58 is 0.5 - 0.219 = 0.281
```

ANSWER (i): 0.281.

═══════════════ PART (ii): less than 1 mm ═══════════════

EVERY STEP:

```
  STEP 1  z = (1 - 2.6)/5.8737 = -1.6/5.8737 = -0.2724
  STEP 2  the table gives phi(0.27) = 0.1064 (they rounded 0.2724 to 0.27)
  STEP 3  z is NEGATIVE, so use the negative conversion:
          P(X < 1) = 0.5 - phi(0.27)
                   = 0.5 - 0.1064
                   = 0.3936
```

PICTURE:

```
        #####|
   --(-0.27)--0--------->
     |<-0.1064->|
     |<----0.3936---->|
   the area to the LEFT of -0.27 is 0.5 - 0.1064 = 0.3936
```

ANSWER (ii): 0.3936.

═══════════════ PART (iii): between 1.5 and 4.6 ═══════════════

EVERY STEP:

```
  STEP 1  z for 1.5: (1.5 - 2.6)/5.8737 = -1.1/5.8737 = -0.1873
  STEP 2  z for 4.6: (4.6 - 2.6)/5.8737 = 2.0/5.8737 = 0.3405
  STEP 3  the z's have OPPOSITE SIGNS (-0.19 and 0.34), so use the sum form:
          P(1.5 < X < 4.6) = phi(0.19) + phi(0.34)
                           = 0.075 + 0.133
                           = 0.208
          (using the paper's rounded table values; the exact value is 0.2075)
```

PICTURE:

```
        ###|      |####
   ----(-0.19)--0--(0.34)----
        |<0.075>|<--0.133-->|
        total = 0.075 + 0.133 = 0.208
```

ANSWER (iii): 0.208 (about 21 percent of days).

═══════════════ PART (iv): at most 2 days in a week ═══════════════

IN PLAIN: each day independently has a 0.208 chance of being "in the 1.5-4.6 band". Over 7
days, what is the chance that AT MOST 2 of them are in that band?

STEP 0: RECOGNISE THE COMPOSITE:

```
   +--------------------------------------------------------------+
   |  this is a BINOMIAL:                                          |
   |     n = 7        (a week has 7 days)                          |
   |     p = 0.208    (the probability from part iii)              |
   |     "at most 2"  -> P(X = 0) + P(X = 1) + P(X = 2)            |
   +--------------------------------------------------------------+
```

EVERY STEP:

```
  STEP 1  p = 0.208, q = 1 - p = 0.792

  STEP 2  P(0) = (0.792)^7
              = 0.792^7
              compute: 0.792^2 = 0.6273; ^4 = 0.3935; ^7 = 0.3935 x 0.6273 x 0.792
              = 0.3935 x 0.4968 = 0.1955
              (calculator: 0.792^7 = 0.1955)

  STEP 3  P(1) = C(7,1) x 0.208 x 0.792^6
              = 7 x 0.208 x 0.2468
              = 1.456 x 0.2468 = 0.3593

  STEP 4  P(2) = C(7,2) x 0.208^2 x 0.792^5
              = 21 x 0.04326 x 0.3117
              = 21 x 0.01348 = 0.2831

  STEP 5  add the three:
          0.1955 + 0.3593 + 0.2831 = 0.8379
```

ANSWER (iv): 0.8379, about 0.838 (84 percent chance that at most 2 of the 7 days fall in the band).

THE COMPOSITE PICTURE (this is the shape the exam loves):

```
   +--------------------------+
   | ONE day: normal(2.6,34.5)|
   | P(1.5 < X < 4.6) = 0.208 |
   +-------------+------------+
                 |
                 | that p becomes the binomial's p
                 v
   +--------------------------+
   | 7 days, each 0.208        |
   | P(at most 2 qualify)      |
   | = B(7, 0.208), 0+1+2      |
   +--------------------------+
```

TRAP (all parts):
```
   1. USING THE CUMULATIVE TABLE. The paper prints phi(0.58) = 0.219, which is the
      area-from-mean. If you treat it as cumulative you get P(X>=6) = 1 - 0.219 = 0.781,
      wildly wrong. READ THE USEFUL DATA AND CHECK WHICH TABLE IT IS.
   2. Treating 34.5 as the sd. It is the VARIANCE. sd = 5.8737.
   3. For part (iii), adding phi values when z's have the SAME sign (you would subtract).
      Here they are opposite signs, so ADD. Draw the picture.
   4. For part (iv), using p = 0.281 or another part's answer. It must be part (iii)'s
      answer, the 1.5-4.6 band.
   5. Forgetting to switch models: part (iv) is not normal, it is binomial.
```

═══════════════════════════════════════════════════════════════════════════════
F6.4  SAMPLE MEAN:  Xbar, with the SE denominator
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 3 (MTE 2025-26 paper, block Q7 - the real thing, and it is a LECTURE SLIDE example)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   The average life of a machine is 7 years with a standard deviation of 1 year. If the
   lives of these machines follow the normal distribution, find the probability that the
   average life of 9 random samples of such machines falls between 6.4 years to 7.2 years.
   (useful data phi(1.8) = 0.4641, phi(0.6) = 0.2257)
```

STEP 0: DECODE - the word that changes everything: "THE AVERAGE LIFE OF 9 SAMPLES".

```
   "average life of a machine is 7"  -> mu = 7
   "standard deviation of 1"         -> sigma = 1
   "the AVERAGE of 9 samples"        -> THIS IS Xbar, NOT X.
                                        the standardisation denominator becomes sigma/sqrt(n)
   "falls between 6.4 and 7.2"       -> an interval on Xbar
```

THE DECISION THAT DECIDES THE WHOLE MARK:

```
   +---------------------------------------------------------------------+
   |  does the question ask about ONE item, or the AVERAGE OF n ITEMS?    |
   |                                                                     |
   |   one item:      z = (X - mu) / sigma                                |
   |   average of n:  z = (Xbar - mu) / (sigma / sqrt(n))                 |
   |                                        ^^^^^^^^ this is the STANDARD |
   |                                        ERROR                     |
   |                                                                     |
   |  "average of 9", "mean of a sample of 9", "9 random samples" -> USE  |
   |  THE STANDARD ERROR. This is the single most common normal error.    |
   +---------------------------------------------------------------------+
```

EVERY STEP:

```
  STEP 1  Compute the standard error:
          SE = sigma / sqrt(n) = 1 / sqrt(9) = 1 / 3 = 0.3333

  STEP 2  z for the lower end 6.4:
          z = (6.4 - 7) / 0.3333
            = (-0.6) / 0.3333
            = -1.8

  STEP 3  z for the upper end 7.2:
          z = (7.2 - 7) / 0.3333
            = 0.2 / 0.3333
            = 0.6

  STEP 4  the z's have OPPOSITE signs (-1.8 and 0.6), so ADD the phi values:
          P(6.4 < Xbar < 7.2) = phi(1.8) + phi(0.6)
                              = 0.4641 + 0.2257
                              = 0.6898
```

ANSWER: 0.6898, about 69 percent.

PICTURE:

```
        ###|      |####
   ----(-1.8)----0----(0.6)----
       |<-0.4641->|<--0.2257-->|
       total = 0.4641 + 0.2257 = 0.6898

   note how WIDE the interval is in z units: -1.8 to 0.6. that is because the SE (0.3333)
   is much smaller than sigma (1), so the same 0.6-0.8 year gap is many standard errors wide.
   sampling averages are much more concentrated than individual items.
```

TRAP:
```
   1. THE BIG ONE: using sigma = 1 instead of SE = 1/3. Then z = -0.6 and 0.2, and you get
      phi(0.6) + phi(0.2) = 0.2257 + 0.0793 = 0.305. WRONG. The question says "average of 9
      samples"; the denominator is SE.
   2. Using n = 9 in the numerator or dividing by 9 instead of sqrt(9). SE = sigma/sqrt(n),
      not sigma/n.
   3. Using the WRONG table convention (see the top of this file).
```

WHY THIS QUESTION MATTERS: it is a LECTURE SLIDE example (lms-standard-error-clt, Example 3)
put on the paper nearly verbatim. The course recycles its own teaching examples.

═══════════════════════════════════════════════════════════════════════════════
F6.5  TWO-UNKNOWN INVERSE:  given two percentages, find mean and sd
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 4 (our paper, ETE 2024-25 S4 B4)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   In a normal distribution, 31% of items are under 45 and 8% are over 64.
   What is the mean and standard deviation of the distribution?
   (Given that phi(1.41) = 0.42, phi(0.19) = 0.50)
```

STEP 0: DECODE - TWO clues, TWO unknowns, so TWO equations.

```
   clue 1: "31% under 45"   -> P(X < 45) = 0.31
   clue 2: "8% over 64"     -> P(X > 64) = 0.08,  equivalently P(X < 64) = 0.92
   unknowns: mu and sigma.
   => build one z-equation from each clue, then solve them together.
```

STEP 1: TURN EACH CLUE INTO A z-VALUE

```
   CLUE 1: P(X < 45) = 0.31. This is LESS than 0.5, so 45 sits BELOW the mean,
           and its z is NEGATIVE.
           using the phi convention: P(X<45) = 0.5 - phi(|z1|) = 0.31
                so phi(|z1|) = 0.5 - 0.31 = 0.19
                the paper prints "phi(0.19) = 0.50", which does NOT match: phi(0.19)
                really equals 0.0753. CONFIRMED TYPO IN THE PAPER.

           Let me re-read the given data: "phi(0.19) = 0.50" looks like a typo in the
           question paper, because phi(0.19) should be about 0.0754.
           USING THE MATHEMATICALLY CORRECT VALUE: phi(|z1|) = 0.19 -> |z1| = 0.4959
           so z1 = -0.4959.

   CLUE 2: P(X > 64) = 0.08. This is an UPPER tail, so 64 sits ABOVE the mean, z positive.
           P(X>64) = 0.5 - phi(z2) = 0.08
                so phi(z2) = 0.5 - 0.08 = 0.42
                the paper gives phi(1.41) = 0.42  ->  z2 = 1.41   ✓ this one matches.
```

STEP 2: WRITE THE TWO EQUATIONS

```
   z1 = (45 - mu) / sigma = -0.4959      (equation 1)
   z2 = (64 - mu) / sigma =  1.41        (equation 2)
```

STEP 3: SOLVE (subtract to kill mu)

```
   From (1):  45 - mu = -0.4959 sigma
   From (2):  64 - mu =  1.41 sigma

   subtract (1) from (2):
   (64 - mu) - (45 - mu) = 1.41 sigma - (-0.4959 sigma)
   19 = (1.41 + 0.4959) sigma
   19 = 1.9059 sigma
   sigma = 19 / 1.9059 = 9.97

   (using the paper's given z2 = 1.41 and the correct z1 = 0.4959)
```

STEP 4: BACK-SUBSTITUTE FOR mu

```
   from (2):  64 - mu = 1.41 x 9.97 = 14.06
   mu = 64 - 14.06 = 49.94
```

ANSWER: mean mu about 49.94, standard deviation sigma about 9.97.
(rounded: mean 50, sd 10, which is clearly the intended answer.)

THE METHOD PICTURE (two clues -> two lines -> where they meet):

```
   clue 1: 45 is below the mean, 0.19 of the area between it and the centre
   clue 2: 64 is above the mean, 0.42 of the area between it and the centre

        ###|      |####
   -----45----mu----64---->
      |<-0.19->|<-0.42->|
        z=-0.496      z=1.41
        |                |
        +-- two equations, two unknowns --+
                        |
                        v
              subtract -> find sigma
              substitute -> find mu
```

TRAP:
```
   1. Not converting "8% OVER 64" into a usable form. "over" is an upper tail, so phi(z) =
      0.5 - 0.08 = 0.42. A slip here flips a sign and ruins both answers.
   2. Mixing the two table conventions (see the top of this file).
   3. Trying to solve without subtracting. Subtracting the two equations is what eliminates
      mu and leaves sigma alone.
   4. Note on the printed data: phi(0.19) = 0.50 in the question appears to be a typo
      (phi(0.19) is really about 0.075). Flagged here so you are not confused in the exam;
      work with the correct value and state your assumption.
```

═══════════════════════════════════════════════════════════════════════════════
F6 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   N(mu, sigma^2):  THE SECOND NUMBER IS THE VARIANCE. sd = sqrt(that).

   STANDARDISE:
     one item:       z = (X - mu)/sigma
     average of n:   z = (Xbar - mu)/(sigma/sqrt(n))    <- SE denominator

   THE TWO TABLES:
     cumulative F(z): F(0)=0.5, F(1.5)=0.9332
     AREA-FROM-MEAN phi(z): phi(0)=0, phi(1.5)=0.4332   <- OUR PAPERS USE THIS
     bridge: F(z) = 0.5 + phi(z) for z>0, 0.5 - phi(|z|) for z<0

   TAIL CONVERSIONS:
     P(X < a), z>0:  0.5 + phi(z)
     P(X < a), z<0:  0.5 - phi(|z|)
     P(X > a), z>0:  0.5 - phi(z)
     P(X > a), z<0:  0.5 + phi(|z|)

   INTERVAL:
     same-sign z's:  subtract phi values
     opposite-sign:  ADD phi values

   INVERSE: read z off the table, then un-standardise: x = mu + z sigma

   TWO-UNKNOWN: one equation per clue, subtract to kill mu, solve for sigma, back-substitute.

   COMPOSITE: a normal probability can become the p of a binomial (the MTE C1 pattern).

   LANDMARKS: 68.27 / 95.45 / 99.73 percent within 1 / 2 / 3 sd.

   TOP TRAPS:
     treating the variance as the sd
     using sigma instead of SE for an "average of n" question     <- the #1 error
     the wrong table convention (check the printed useful data)
     adding phi values when z's share a sign
     forgetting part (iv) is binomial, not normal
```
