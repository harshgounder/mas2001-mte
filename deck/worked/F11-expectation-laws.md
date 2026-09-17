# F11 EXPECTATION AND VARIANCE LAWS: every shape, solved from zero

Source: our own material (MTE 2025-26 Q8, MTE 2024-25 A1/B1, the ETE papers E24S4, E25SUM,
R25S3, R25S4). Nothing invented. All numbers machine-checked (17/17).

```
  SHAPES IN THIS FILE
  F11.1  the laws of expectation and variance  (the toolbox)      0 questions, the rules
  F11.2  E[XY] for independent variables        MCQ               1 question
  F11.3  variance is always ...                 MCQ               1 question
  F11.4  scaling a Poisson: Y = 2X              MCQ + full solve  1 question (MTE!)
  F11.5  the typist / letters question          the full solve    1 question (MTE!)
  F11.6  soldiers over 6 feet                   the full solve    1 question
```

WHY THIS FILE: F1, F2, F6 and F10 each compute a mean or variance as part of their own
questions. This file collects the LAWS that all of those computations silently use, plus the
four questions that are purely about these laws.

═══════════════════════════════════════════════════════════════════════════════
F11.1  THE LAWS  (the toolbox; every question below uses these)
═══════════════════════════════════════════════════════════════════════════════

THE EXPECTATION LAWS:

```
   +---------------------------------------------------------------+
   | E(c)        = c            a constant's expectation is itself  |
   | E(cX)       = c E(X)       constants pull out of E             |
   | E(X + Y)    = E(X) + E(Y)  ALWAYS (no independence needed)     |
   | E(X - Y)    = E(X) - E(Y)  ALWAYS                              |
   | E(XY)       = E(X) E(Y)    ONLY when X and Y are INDEPENDENT    |
   +---------------------------------------------------------------+
```

THE VARIANCE LAWS:

```
   +---------------------------------------------------------------+
   | Var(c)      = 0            a constant does not vary            |
   | Var(cX)     = c^2 Var(X)   the constant is SQUARED (not pulled) |
   | Var(X + c)  = Var(X)       adding a constant shifts, no spread  |
   | Var(X + Y)  = Var(X) + Var(Y)   when INDEPENDENT               |
   | Var(X - Y)  = Var(X) + Var(Y)   when INDEPENDENT (PLUS! see)   |
   | Var(aX + bY) = a^2 Var(X) + b^2 Var(Y)   when independent      |
   +---------------------------------------------------------------+
```

THE TWO MOST-EXAMINED CONTRASTS (draw these; they decide half the MCQs):

```
   +--------------------------------+--------------------------------+
   | THE CONSTANT                   | EXPECTATION      VARIANCE      |
   +--------------------------------+--------------------------------+
   | cX     (scale by c)            | c E(X)           c^2 Var(X)    |
   | X + c  (shift by c)            | E(X) + c         Var(X)        |
   +--------------------------------+--------------------------------+
   | remember: E pulls the constant OUT; Var SQUARES it (for scaling)|
   +--------------------------------+--------------------------------+
```

THE SUBTRACTION SURPRISE:

```
   Var(X - Y) = Var(X) + Var(Y)     <- PLUS, even though it is a minus!

   why: variance measures SPREAD. subtracting two random quantities lets each one wander,
   and their wanderings ADD. the picture:

        X wanders this much:   <---->
        Y wanders this much:   <---->
        X - Y wanders:         <-------->  the variations combine, they do not cancel.
```

THE OTHER FORMULAS (used everywhere in F1-F10, collected here):

```
   Var(X) = E(X^2) - [E(X)]^2        the computational formula
   E(aX + b) = a E(X) + b            linearity
   E[aX^2 + bX + c] = a E(X^2) + b E(X) + c
```

═══════════════════════════════════════════════════════════════════════════════
F11.2  E[XY] FOR INDEPENDENT VARIABLES  (MCQ)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 1 (our paper, ETE re-session S3 A1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   The expectation of two independent random variables X and Y will be
   a. E[XY] = 1
   b. E[XY] = 0
   c. E[XY] = E[X] + E[Y]
   d. E[XY] = E[X] E[Y]
```

ANSWER: (d) E[XY] = E[X] E[Y].

WHY: independence is exactly the condition that makes the expectation of a product FACTOR.
Without independence this fails (for example, X = Y gives E[XY] = E[X^2], not (E[X])^2).

TRAP:
```
   (c) E[X] + E[Y] is the rule for E(X + Y), which holds ALWAYS. The question asks about the
   PRODUCT XY, and for products you need independence. Additive rule: always. Multiplicative
   rule: only independent. Keep the two straight.
```

═══════════════════════════════════════════════════════════════════════════════
F11.3  VARIANCE IS ALWAYS ...  (MCQ)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 2 (our paper, ETE 2025 summer Q8)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Variance is always
   (A) Negative   (B) Zero   (C) Non-negative   (D) Infinite
```

ANSWER: (C) non-negative.

WHY: variance is a sum (or integral) of SQUARED deviations, (x - mu)^2, each divided by n or
multiplied by a probability. Squares are never negative, weights are never negative, so the
sum can never be negative. It CAN be zero (when the variable is a constant), but that is a
special case, not the general rule.

TRAP: (B) "zero". Zero is a possible VALUE (for a degenerate distribution), but "always" in
the question means "every variance lies in this range", and the range is [0, infinity).

═══════════════════════════════════════════════════════════════════════════════
F11.4  SCALING A POISSON:  Y = 2X   (MCQ, and the full solve underneath)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 3 (MTE 2024-25 paper, block A1 - the real thing)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A Poisson variate X has mean equal to 0.5. If Y = 2X, then which of the following
   is/are correct?
   i. E(Y) = 1        ii. Var(Y) = 4       iii. Var(Y) = 2      iv. E(Y) = 2
   a. (i) and (ii) only      b. (ii) and (iv) only
   c. (i) and (iii) only     d. (iii) and (iv) only
```

STEP 0: DECODE

```
   "Poisson variate X has mean 0.5"  -> E(X) = 0.5. For a Poisson, Var(X) = mean = 0.5 too.
   "Y = 2X"                          -> Y is X scaled by the constant 2.
   the ask: which of the FOUR statements about E(Y) and Var(Y) are true.
```

EVERY STEP:

```
  STEP 1  E(Y) = E(2X) = 2 E(X) = 2 x 0.5 = 1
          -> statement (i) E(Y) = 1 is TRUE.   statement (iv) E(Y) = 2 is FALSE.

  STEP 2  Var(Y) = Var(2X) = 2^2 Var(X) = 4 x 0.5 = 2
          -> statement (iii) Var(Y) = 2 is TRUE.  statement (ii) Var(Y) = 4 is FALSE.
          (the 4 in statement (ii) is the SQUARED constant; the answer is 4 x Var(X) =
           4 x 0.5 = 2, so (ii) confuses the squared constant with the final variance.)

  STEP 3  true statements: (i) and (iii).
```

ANSWER: option (c): (i) and (iii) only.

THE PICTURE (what scaling does to a Poisson):

```
   X ~ Poisson(0.5):
        P(X=0) = 0.6065    |
        P(X=1) = 0.3033    |###
        P(X=2) = 0.0758    |#
        ...                 +---- 0 1 2 3 ...
                                    mean 0.5, var 0.5

   Y = 2X can only take even values 0, 2, 4, 6, ...
        P(Y=0) = 0.6065    |
        P(Y=2) = 0.3033    |###
        P(Y=4) = 0.0758    |#
        ...                 +---- 0 2 4 6 ...
                                    mean 1, var 2

   the distribution is STRETCHED horizontally by 2 (so the mean doubles and the
   variance multiplies by 4 = 2^2).
```

TRAP:
```
   1. Thinking Y = 2X is still a Poisson. It is NOT (it only takes even values), but its
      mean and variance still follow the scaling rules.
   2. Using Var(2X) = 2 Var(X). The constant is SQUARED for variance: 2^2 = 4. This is the
      exact trap statements (ii) and (iii) are built around.
   3. Mixing up (ii) and (iii): (iii) says Var(Y) = 2, which is the correct
      4 x 0.5 = 2. (ii) says 4, which would be correct only if Var(X) were 1.
```

═══════════════════════════════════════════════════════════════════════════════
F11.5  THE TYPIST / LETTERS QUESTION  (MTE 2025-26 Q8 - the full solve)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 4 (MTE 2025-26 paper, block Q8 - the real thing, a full 5-mark question)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A manager accepts the work submitted by his typist only when there is no mistake in
   the work. The typist has to type on an average 20 letters per day, each of about 200
   words. Find the chance of her making a mistake:
   (i) if less than 1% of the letters submitted by her are rejected,
   (ii) if on 90% of days all the letters submitted by her are accepted.  (e = 2.72)
```

STEP 0: DECODE - this is the single trickiest wording on the paper. Break it apart.

```
   PHASE 1 - what is being counted?
     "200 words per letter, 20 letters per day"  -> 4000 words per day, and the MISTAKE
     count is per WORDS. Let lambda = the average number of mistakes per 4000 words
     (per day). The mistakes-per-day count is then Poisson(lambda).

   PHASE 2 - what does "acceptance" mean?
     the manager accepts a letter ONLY IF there is no mistake in it.
     so "the letter is accepted" = "no mistakes in that letter".

   PHASE 3 - what are the two conditional statements really saying?
     (i)  "less than 1% of the letters are rejected" -> P(a letter is rejected) < 0.01
          "a letter is rejected" = "at least one mistake in it"
          -> P(at least 1 mistake in a letter) < 0.01
     (ii) "on 90% of days ALL the letters are accepted" ->
          P(all letters in a day are accepted) = 0.90
          "all accepted" = "zero mistakes in the whole day"
          -> P(no mistakes at all in a day) = 0.90
```

THE RATE BOOKKEEPING (this is the heart of the question):

```
   mistakes are counted per WORD. the typist types 200 words per letter and 20 letters
   per day = 4000 words per day.

   let lam = average number of mistakes per 200 words (per letter).
   then per day:  lam_day = 20 x lam   (20 letters, each with its own expectation)
   (equivalently: if the per-word rate is r, lam = 200r and lam_day = 4000r.)
```

PART (i): less than 1% of letters rejected

```
  STEP 1  P(letter rejected) = P(at least 1 mistake in the letter)
          = 1 - P(0 mistakes) = 1 - e^(-lam)

  STEP 2  the condition: 1 - e^(-lam) < 0.01

  STEP 3  solve:  e^(-lam) > 0.99
                  -lam > ln(0.99)
                  lam < -ln(0.99) = 0.01005

  ANSWER (i): the average number of mistakes per letter must be less than about 0.01.
  (so roughly one mistake every 100 letters, at most.)
```

PART (ii): 90% of days fully accepted

```
  STEP 1  "0 mistakes in the whole day" with the day count Poisson(lam_day):
          P(0 mistakes in the day) = e^(-lam_day) = e^(-20 lam)

  STEP 2  the condition: e^(-20 lam) = 0.90

  STEP 3  solve:  -20 lam = ln(0.90)
                  20 lam = -ln(0.90) = 0.10536
                  lam = 0.10536 / 20 = 0.005268

  ANSWER (ii): the average mistakes per letter must be about 0.0053
  (roughly one mistake every 190 letters).
```

THE PICTURE (why (ii) demands fewer mistakes than (i)):

```
   (i)  concerns ONE letter:                 (ii) concerns a WHOLE DAY (20 letters):
        P(1 mistake somewhere in it) < 1%         P(zero mistakes across all 20) = 90%
        -> lam < 0.01005                          -> 20 lam = 0.105 -> lam < 0.0053

   requirement (ii) is STRICTER because "no mistakes all day" has to survive 20 letters
   in a row: any single mistake anywhere kills the day.
```

TRAP:
```
   1. USING THE SAME CONDITION FOR BOTH PARTS. (i) is a per-letter probability; (ii) is a
      per-day probability. The day rate is 20x the letter rate, and forgetting the factor
      20 is the classic mistake.
   2. Mixing the directions: (i) gives an UPPER bound (error rate below 1%), (ii) gives an
      equation (exactly 90%), not an inequality. Read which is a bound and which is an
      equation.
   3. Forgetting "rejected = at least one mistake" and trying to use P(exactly one).
   4. The 200 words detail: it scales the WORD rate to the LETTER rate. If the question had
      given mistakes per word, you would multiply by 200. Keep the units consistent.
   5. ln(0.99) is NEGATIVE (-0.01005); do not drop the sign. lam must come out positive.
```

═══════════════════════════════════════════════════════════════════════════════
F11.6  SOLDIERS OVER 6 FEET  (normal + expectation, the full solve)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 5 (our paper, ETE re-session S4 B1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Assume the mean height of soldiers to be 68.22 inches with a variance of 10.8 inches.
   How many soldiers in a regiment of 1000 would you expect to be over 6 feet tall?
   The useful data is 0.3749.
```

STEP 0: DECODE - two moves: a probability, then an expectation.

```
   "mean 68.22, VARIANCE 10.8"  -> mu = 68.22, sigma = sqrt(10.8) = 3.2863 (SQUARE-ROOT IT)
   "over 6 feet tall"           -> 6 feet = 72 inches. so we want P(height > 72).
   "how many ... would you expect" -> EXPECTED COUNT = 1000 x P(over 72).
```

EVERY STEP:

```
  STEP 1  sigma = sqrt(10.8) = 3.2863

  STEP 2  z = (72 - 68.22) / 3.2863 = 3.78 / 3.2863 = 1.1502

  STEP 3  the question supplies phi(1.15) = 0.3749 (the area-from-mean table).
          the area from the mean to z = 1.15 is 0.3749, so the area ABOVE it is
          0.5 - 0.3749 = 0.1251

  STEP 4  expected count = 1000 x 0.1251 = 125.1
```

ANSWER: about 125 soldiers (the exact figure 125.1 rounds to 125).

THE PICTURE:

```
   heights ~ N(68.22, 10.8):
                          ####
                        ########
                       ##########
                     ##############
                   --------------------->
                  68.22        72
                      |<-1.15->|   the right tail (beyond 6 feet) = 0.1251
                                    of 1000 soldiers -> about 125
```

TRAP:
```
   1. FORGETTING TO CONVERT 6 FEET TO INCHES. 6 feet = 72 inches. Using 6 in the z-formula
      gives a nonsense z.
   2. Using the VARIANCE 10.8 as the standard deviation. It must be square-rooted first
      (sigma = 3.2863).
   3. Reporting the probability (0.1251) when the question asks for a COUNT (125). "How many
      would you expect" -> multiply by the total.
   4. Reading 0.3749 as the tail. It is the area FROM THE MEAN; the tail is 0.5 - 0.3749.
```

═══════════════════════════════════════════════════════════════════════════════
F11.7  MORE PAPER QUESTIONS AND THE OFFICIAL-SCHEME FORMS
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
THE TYPIST IN THE OFFICIAL FORM (the scheme expresses the answer per WORD)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The university's solution scheme for M25-Q8 works with the per-WORD mistake probability p
and the base-10 log form (with e = 2.72, log10(e) = 0.4346). Both are the same answer in
different units. Learn both; the exam accepts either, but its scheme uses this one:

```
   (i)  e^(-200p) >= 0.99
        -200p x log10(e) >= log10(0.99)
        -p x (200 x 0.4346) >= -0.0044
        p <= 0.0044/86.92 = 0.0000506        (the scheme's value)

   (ii) e^(-4000p) = 0.90
        -4000p x log10(e) = log10(0.90)
        -p x (4000 x 0.4346) = -0.0458
        p = 0.0458/1738.4 = 0.0000263        (the scheme's value)
```

THE TRANSLATION TABLE (so you can move between the two forms):
```
   +-------------------------+------------------+--------------------+
   | quantity                | per-word p      | per-letter lambda  |
   +-------------------------+------------------+--------------------+
   | (i)  answer             | 0.0000506       | 0.01005            |
   | (ii) answer             | 0.0000263       | 0.00527            |
   | relation                | lambda = 200 p  | (200 words/letter) |
   +-------------------------+------------------+--------------------+
   exact values (natural logs): p_i = 5.03e-5, p_ii = 2.63e-5.
   the scheme's 5.06e-5 differs only by the 2.72 rounding; state the form you use.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 6 (our paper, ETE 2025-26 S3 B3 - E(X^2) and the at-most part, plus the M24 twin)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

(The full solve of E(X), E(X^2), E(2X+1)^2 is in F10.4. The additional asks that appear in
the paper variants:)

```
   E25SUM-15 variant asks the same three. R25S3-A1 asks E[XY] for independent X,Y (F11.2).
   The M24 paper's binomial variant (mean 5/3): variance 10/9, P(X>=1) = 211/243,
   P(X<=1) = 112/243 - full solve in F1, Question 7b.
```

═══════════════════════════════════════════════════════════════════════════════
F11 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   EXPECTATION LAWS              VARIANCE LAWS
     E(c) = c                      Var(c) = 0
     E(cX) = c E(X)                Var(cX) = c^2 Var(X)     <- SQUARED
     E(X +- Y) = E(X) +- E(Y)      Var(X +- c) = Var(X)
        always                     Var(X +- Y) = Var(X) + Var(Y)   when independent
     E(XY) = E(X)E(Y)                 (PLUS even for the minus case)
        only if independent

   Var(X) = E(X^2) - [E(X)]^2

   THE MCQs IN ONE BREATH:
     independent product  -> E[XY] = E[X]E[Y]
     variance             -> always non-negative
     scaling a Poisson Y=2X -> E doubles, Var QUADRUPLES

   THE TYPIST (MTE Q8): rate per letter vs rate per day (x20); (i) upper bound 0.01005,
     (ii) equation -> 0.00527.

   THE SOLDIERS: 6 feet = 72 in; sigma = sqrt(10.8) = 3.29; z = 1.15; tail 0.1251;
     expected count = 125.

   TOP TRAPS:
     Var(2X) = 2 Var(X)        WRONG, it is 4 Var(X)
     Var(X - Y) = Var(X) - Var(Y)  WRONG, it is PLUS (for independent)
     variance as sd (10.8 vs sqrt(10.8) = 3.29)
     6 feet not converted to 72 inches
     per-letter vs per-day rates (the factor 20)
```
