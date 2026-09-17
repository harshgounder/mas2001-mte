# F6-normal GUIDE: the explanation content behind the questions

This is the non-question content from the family file: the family intro, the
toolboxes, the section intros, decision trees, and the summary card. It is the
TEACHING layer. Read it first (it gives the method), then drill the q*.md files.

Source: deck/worked/F6-normal.md (same content; this file just isolates it).


──────────────────────────────────────────────────────────────────────────────
[FAMILY INTRO / PREAMBLE (before the first question)]
──────────────────────────────────────────────────────────────────────────────

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

!!! PROMINENT SOURCE-DATA WARNING !!!
```
   The inverse-normal question later prints phi(0.19) = 0.50. That printed pair is
   IMPOSSIBLE for the area-from-mean entry at z = 0.19: phi(0.19) is about 0.075.
   In this table phi(0) = 0 and the area approaches 0.50 only as z grows without bound.
   Treat the paper entry as a typo. The probability statement gives phi(|z|) = 0.19,
   which leads to |z| about 0.496. The detailed correction appears in F6.5.
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


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q1 and Q2)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F6.2 + F6.3  TAIL and INTERVAL + the binomial composite
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q2 and Q3)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F6.4  SAMPLE MEAN:  Xbar, with the SE denominator
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q3 and Q4)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F6.5  TWO-UNKNOWN INVERSE:  given two percentages, find mean and sd
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[CLOSING SECTION (after Q5; usually the summary card)]
──────────────────────────────────────────────────────────────────────────────

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
