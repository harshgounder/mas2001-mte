# F2 POISSON: every shape, every question, solved from zero

Source of every question: our own material (the MTE 2024-25 paper, the MTE 2025-26 paper, the
ETE papers E24S3, E25SUM, R25S3, R25S4, and the ppt3 deck). Nothing invented. Every number
computed and checked on the machine (9/9 checks pass).

```
  SHAPES IN THIS FILE
  F2.1  point         P(X=k)                     2 questions (deck + paper)
  F2.2  tail          P(X>=k) / at least         1 question
  F2.3  recovery      recover lambda from a ratio 2 questions (MTE!)
  F2.4  rate/window   rescale lambda              1 question
  F2.5  nesting       Poisson then binomial       1 question (deck)
  F2.6  moments algebra  Var of a function        2 questions (MTE!)
  F2.7  formula MCQ   name the pmf                1 question (MTE!)
```

═══════════════════════════════════════════════════════════════════════════════
BEFORE ANY QUESTION: what "Poisson" means
═══════════════════════════════════════════════════════════════════════════════

A Poisson situation counts HOW MANY RARE EVENTS happen in a fixed span (time, space, pages).

```
   +-----------------------------------------------------------------+
   |  YOU GET:                                                        |
   |     lambda  = the AVERAGE count in the span you care about       |
   |                                                                |
   |  YOU WANT:                                                       |
   |     the probability of exactly k events                          |
   |                                                                |
   |  THE FORMULA:                                                    |
   |                                                                |
   |                    e^(-lambda)  x  lambda^k                      |
   |      P(X = k)  =  --------------------------                     |
   |                            k!                                    |
   +-----------------------------------------------------------------+
```

WHAT EVERY SYMBOL MEANS, in plain words:

```
   e          the special number 2.71828... It lives on your calculator (the e^x button).
              e^(-lambda) is a small number; for lambda=1 it is 0.3679.
   lambda     "the average". ALSO the variance (see the signature below).
   k          the count you are asking about. k! = k x (k-1) x ... x 1, and 0! = 1, 1! = 1.
   X          the number of events. A name.
```

THE SIGNATURE (memorize this; it is the fastest way to spot a Poisson):

```
   +---------------------------------------+
   |  MEAN  =  VARIANCE  =  lambda          |
   +---------------------------------------+

   every other distribution we study has mean and variance DIFFERENT from each other.
   Poisson is the only one where they are the SAME NUMBER. If a question says
   "mean equals variance", the answer is Poisson.
```

THE PICTURE of the pmf (lambda = 1.5, the car-hire example later in this file):

```
   P(X=k)
   0.33 |           ##
   0.30 |           ##
   0.27 |     ##    ##
   0.22 |     ##    ##
   0.20 |     ##    ##    ##
   0.15 |     ##    ##    ##
   0.10 |     ##    ##    ##    ##
   0.05 |     ##    ##    ##    ##    ##
   0.00 +---- k=0---k=1---k=2---k=3---k=4---k=5---
              .22   .33   .25   .13   .047  .014

   the peak sits near lambda, and the tail stretches right. "rare events" means the left
   side is fat: k=0 is always a big chunk.
```

THE WINDOW RULE (the single most common Poisson error, learn it now):

```
   lambda MUST match the span you are asking about.

   +----------------------------------------------------------+
   |  rate = 3 per minute.  ask is about 5 minutes.            |
   |  then lambda = 3 x 5 = 15, NOT 3.                         |
   |                                                           |
   |  rate = 0.5 per box.   ask is about 100 boxes.            |
   |  then lambda per box = 0.5 (if asking about one box)      |
   +----------------------------------------------------------+
```

═══════════════════════════════════════════════════════════════════════════════
F2.1  POINT:  P(X = k)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 1 (our paper, ETE re-session S3 B2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A car hire-firm has two cars which it hires out day by day. The number of demands
   for a car is known to be Poisson distribution with mean 1.5. Find the probability of
   a day on which (i) There is no demand for the car, and (ii) The demand is [at least 2].
```

STEP 0: DECODE

```
   "Poisson distribution"      -> use the Poisson formula
   "with mean 1.5"             -> lambda = 1.5 (the mean IS lambda for Poisson)
   "a day"                     -> the span is ONE day, and lambda is already per day. no rescale.
   "no demand"                 -> k = 0
   "at least 2"                -> k >= 2, use the complement
```

WHY POISSON: counts rare events (demands) in a fixed span (a day).

═══════════════ PART (i): no demand ═══════════════

IN PLAIN: what is the chance nobody wants a car today?

THE FLOWCHART:

```
   want P(X = 0), lambda = 1.5
              |
              v
   +-------------------------+
   | P(X=0) = e^-l x l^0 / 0!|
   +-------------------------+
              |
              v
   +-------------------------+
   | l^0 = 1   and   0! = 1  |     both equal 1, so they vanish
   +-------------------------+
              |
              v
   +-------------------------+
   | P(X=0) = e^-1.5          |
   +-------------------------+
              |
              v
         e^-1.5 = 0.2231
```

EVERY STEP:

```
  STEP 1  Write the formula with numbers in place:
          P(X=0) = e^(-1.5) x (1.5)^0 / 0!

  STEP 2  Simplify the powers and factorial:
          (1.5)^0 = 1        (anything to the power 0 is 1)
          0! = 1             (by definition)
          so P(X=0) = e^(-1.5) x 1 / 1 = e^(-1.5)

  STEP 3  Compute e^(-1.5). Two ways to think about it:
          way 1: calculator e^x with -1.5 -> 0.22313
          way 2: e^(-1.5) = 1 / e^1.5 = 1 / 4.4817 = 0.2231
```

ANSWER: P(no demand) = 0.2231, about 22 percent. Roughly one day in five, no one calls.

═══════════════ PART (ii): at least 2 demands ═══════════════

IN PLAIN: two or more people want a car (and the firm only has two cars, which is why this
matters to them).

THE PICTURE:

```
   all days (probabilities sum to 1):

   [P0      ][P1      ][P2][P3][P4]...
    \_______/  \____________________/
     NOT wanted  WANTED ("at least 2")

   use:  P(>=2) = 1 - P(0) - P(1)
```

EVERY STEP:

```
  STEP 1  P(0) = 0.2231 (from part i)

  STEP 2  P(1) = e^(-1.5) x (1.5)^1 / 1!
               = 0.2231 x 1.5 / 1
               = 0.3347
          (1! = 1, so the divide does nothing.)

  STEP 3  add the unwanted: 0.2231 + 0.3347 = 0.5578

  STEP 4  subtract from 1: 1 - 0.5578 = 0.4422
```

ANSWER: P(at least 2) = 0.4422, about 44 percent.

SELF CHECK:
```
   the missing piece (3 or more) must be 1 - 0.2231 - 0.3347 - 0.4422 = 0.0000. 
   more precisely: P(0)+P(1) = 0.5578, P(>=2) = 0.4422, total 1.0000 ✓
```

TRAP:
```
   1. Rescaling lambda unnecessarily. The mean is per DAY and the ask is per DAY, so lambda
      stays 1.5. Rescaling to 3 or 4.5 loses everything.
   2. For "at least 2", subtracting only P(0). That gives "at least 1" = 0.7769, a different
      question and a wrong answer here.
   3. Thinking e^(-1.5) is negative. e to any power is always positive; a negative exponent
      just means a small number (1/e^1.5), not a negative one.
```

MUTATIONS:
```
   IF "exactly 2 demands"      THEN P(2) = e^-1.5 x 1.5^2/2 = 0.2231 x 2.25/2 = 0.2510
   IF "at most 2"              THEN P(0)+P(1)+P(2) = 0.2231+0.3347+0.2510 = 0.8088
   IF mean = 2.5               THEN lambda = 2.5 and every e^-1.5 becomes e^-2.5 = 0.0821
   IF "per 2 days"             THEN lambda = 3.0 (two days' worth)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 2 (our deck, ppt3, the life-insurance example, and the 5000-men form)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A life insurance company insures the lives of 5,000 men of age 42. If the
   probability of a man dying in a year is 0.001, find the probability that at most
   2 men die in a year.
```

STEP 0: DECODE - this is a BINOMIAL statement that must become POISSON.

```
   "5,000 men"            -> n = 5000 (big)
   "probability ... 0.001"-> p = 0.001 (small)
   n big + p small         -> use the POISSON APPROXIMATION, lambda = n x p
   "at most 2 men die"    -> k <= 2, so P(0) + P(1) + P(2)
```

WHY THE SWITCH:

```
   +------------------------------------------------------------------+
   |  binomial would need C(5000,2) = 12,497,500  (painful)            |
   |  Poisson needs only e^-5 and powers of 5      (easy)              |
   |                                                                   |
   |  the two answers are almost identical because p is tiny           |
   +------------------------------------------------------------------+

   lambda = n x p = 5000 x 0.001 = 5
```

THE PICTURE:

```
   5000 men, each with a 1-in-1000 chance of dying.
   average deaths per year = 5000 x 0.001 = 5.

   "at most 2" = 0, 1, or 2 deaths. that is the left tail.
```

EVERY STEP:

```
  STEP 1  lambda = 5

  STEP 2  P(0) = e^(-5) x 5^0 / 0! = e^(-5) = 0.006738
          (e^-5: calculator, or 1/e^5 = 1/148.413 = 0.006738)

  STEP 3  P(1) = e^(-5) x 5^1 / 1! = 0.006738 x 5 = 0.033690

  STEP 4  P(2) = e^(-5) x 5^2 / 2!
               = 0.006738 x 25 / 2
               = 0.006738 x 12.5
               = 0.084225

  STEP 5  add the three: 0.006738 + 0.033690 + 0.084225 = 0.124653
```

ANSWER: P(at most 2 deaths) = 0.1247, about 12.5 percent.

TRAP:
```
   1. NOT switching to Poisson and trying C(5000,2) by hand. This is the question's whole
      purpose: to test whether you know the n-big-p-small rule.
   2. "at most 2" includes 2 (it is <=, not <). Do not stop at P(1).
   3. Forgetting that lambda = n x p = 5 and using 0.001 or 5000.
```

═══════════════════════════════════════════════════════════════════════════════
F2.3  RECOVERY: find lambda from a stated ratio  (BOTH MTE PAPERS ASK THIS)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 3 (MTE 2024-25 paper, block B1 - the real thing)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   If X and Y are independent Poisson variates such that P(X=1) = P(X=2) and
   P(Y=2) = P(Y=3), find the variance of X - 2Y.
```

STEP 0: DECODE - TWO hidden asks and a formula you must know.

```
   HIDDEN ASK 1:  P(X=1) = P(X=2) is a clue to find lambda_X.
   HIDDEN ASK 2:  P(Y=2) = P(Y=3) is a clue to find lambda_Y.
   THE REAL ASK:  find Var(X - 2Y), which needs the INDEPENDENCE VARIANCE RULE.
```

THE STRUCTURE:

```
   +----------------------+     +----------------------+
   | P(X=1) = P(X=2)      |     | P(Y=2) = P(Y=3)      |
   |  -> find lambda_X    |     |  -> find lambda_Y    |
   +----------+-----------+     +----------+-----------+
              |                            |
              +-------------+--------------+
                            |
                            v
                +---------------------------+
                | Var(X - 2Y)               |
                | = Var(X) + 4 Var(Y)       |
                | (independence rule)       |
                +---------------------------+
                            |
                            v
                 Var = lambda_X + 4 lambda_Y
```

THE RULE YOU NEED (write it on your sheet now):

```
   +----------------------------------------------------------------+
   |  IF X and Y are INDEPENDENT:                                    |
   |                                                                 |
   |     Var(X + Y) = Var(X) + Var(Y)      <- plus stays PLUS        |
   |     Var(X - Y) = Var(X) + Var(Y)      <- minus ALSO becomes PLUS|
   |     Var(aX)    = a^2 Var(X)           <- the constant gets squared|
   |                                                                 |
   |  so  Var(X - 2Y) = Var(X) + Var(2Y) = Var(X) + 4 Var(Y)          |
   +----------------------------------------------------------------+
```

EVERY STEP:

```
  PART A: find lambda_X

  STEP 1  Write P(X=1) and P(X=2) with the Poisson formula:
          P(X=1) = e^(-l) x l^1 / 1! = e^(-l) l
          P(X=2) = e^(-l) x l^2 / 2! = e^(-l) l^2 / 2

  STEP 2  Set them equal (the given condition):
          e^(-l) l  =  e^(-l) l^2 / 2

  STEP 3  Both sides have e^(-l), so cancel it:
          l  =  l^2 / 2

  STEP 4  Multiply both sides by 2:
          2 l = l^2

  STEP 5  Divide both sides by l (valid since l > 0):
          2 = l
          so lambda_X = 2

  PART B: find lambda_Y

  STEP 6  Same method with 2 and 3:
          P(Y=2) = e^(-m) m^2 / 2
          P(Y=3) = e^(-m) m^3 / 6          (3! = 6)

  STEP 7  Set equal: e^(-m) m^2 / 2 = e^(-m) m^3 / 6
          cancel e^(-m):  m^2 / 2 = m^3 / 6
          multiply by 6:  3 m^2 = m^3
          divide by m^2:  3 = m
          so lambda_Y = 3

  PART C: the variance

  STEP 8  For a Poisson, Var = lambda. So:
          Var(X) = lambda_X = 2
          Var(Y) = lambda_Y = 3

  STEP 9  Apply the rule:
          Var(X - 2Y) = Var(X) + 2^2 Var(Y)
                      = 2 + 4 x 3
                      = 2 + 12
                      = 14
```

ANSWER: Var(X - 2Y) = 14.

SELF CHECK:
```
   P(X=1) with l=2: e^-2 x 2 = 0.1353 x 2 = 0.2707
   P(X=2) with l=2: e^-2 x 4/2 = 0.1353 x 2 = 0.2707   ✓ equal
   P(Y=2) with m=3: e^-3 x 9/2 = 0.0498 x 4.5 = 0.2241
   P(Y=3) with m=3: e^-3 x 27/6 = 0.0498 x 4.5 = 0.2241 ✓ equal
```

TRAP:
```
   1. THE BIG ONE: writing Var(X - 2Y) = Var(X) - 4Var(Y) = 2 - 12 = -10. A variance can
      NEVER be negative. The rule is that a MINUS between independent variables becomes a
      PLUS inside the variance. If your answer is negative, you broke this rule.
   2. Forgetting to SQUARE the 2 in 2Y. It is 2^2 = 4, not 2.
   3. Not cancelling e^(-l) and trying to solve a messier equation.
   4. Using Var = lambda for one and forgetting it for the other.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 4 (MTE 2025-26 paper, block Q2 - the real thing, and its Examveda twin)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   In a Poisson Distribution, if mean = e, then p(x) is given by
   1) e^(x-e)/x!      2) e^(e-x)/x!      3) x!/e^(x-e)      4) x!/e^(e-x)
   (Correct option: 1)
```

STEP 0: DECODE - this MCQ is a SUBSTITUTION drill, not a new problem.

```
   "mean = e"  ->  lambda = e (the number 2.71828)
   "p(x)"      ->  the poisson formula for P(X=x)
   the ask     ->  substitute lambda = e into the formula and simplify the exponent
```

EVERY STEP:

```
  STEP 1  Start from the standard Poisson formula:
          P(X=x) = e^(-lambda) x lambda^x / x!

  STEP 2  Substitute lambda = e:
          P(X=x) = e^(-e) x e^x / x!

  STEP 3  Combine the two powers of e (both have base e, so the exponents ADD):
          e^(-e) x e^x  =  e^(-e + x)  =  e^(x - e)
          (rule: e^A x e^B = e^(A+B))

  STEP 4  Put it back:
          P(X=x) = e^(x-e) / x!

  STEP 5  Match the options: "e^(x-e)/x!" is option 1.
```

ANSWER: option 1, e^(x-e) / x!.

TRAP:
```
   1. Exponent sign slips. e^(-e) x e^x: the first exponent is -e (negative), the second is
      +x. Adding gives x - e, NOT e - x. Option 2 has the sign reversed; that is the decoy.
   2. Thinking "mean = e" is impossible or weird. It is just a number, about 2.718. The
      substitution works the same as any other lambda.
   3. Dropping the /x! or moving it to the numerator (options 3 and 4 are those decoys).
```

MUTATIONS:
```
   IF "mean = 2"      THEN P(x) = e^(-2) 2^x / x!
   IF "variance = 3"  THEN lambda = 3 and P(x) = e^(-3) 3^x / x!
   IF "mean = lambda" THEN it is the standard form itself
   the KEY POINT: for a Poisson, mean and variance are BOTH lambda, so either one given
   tells you the same thing.
```

═══════════════════════════════════════════════════════════════════════════════
F2.4  RATE / WINDOW RESCALING
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 5 (our deck, ppt3 - the nesting example, part 1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Telephone calls arrive at an exchange according to the Poisson process at the rate
   of 2 per minute. Find the probability that in a 5-minute interval there are exactly
   10 calls.
```

STEP 0: DECODE - the window is DIFFERENT from the rate's unit.

```
   "rate of 2 per minute"     -> rate = 2, per ONE minute
   "in a 5-minute interval"   -> the ask is over FIVE minutes
   therefore lambda = 2 x 5 = 10        <- this is the window rescale
```

THE RESCALING PICTURE:

```
   rate:  2 calls per 1 minute
            |
            |  multiply by the window length
            v
   5 minutes = 5 x 1 minute
            |
            v
   lambda = 2 x 5 = 10 calls per 5 minutes

   +--------------------------------------------------+
   |  ALWAYS ask: "what span is my lambda for,        |
   |  and what span does the question ask about?"     |
   |  if they differ, multiply or divide.             |
   +--------------------------------------------------+
```

EVERY STEP:

```
  STEP 1  lambda = rate x window = 2 x 5 = 10
  STEP 2  k = 10 (exactly 10 calls)
  STEP 3  P(X=10) = e^(-10) x 10^10 / 10!
  STEP 4  compute the pieces:
          e^(-10) = 0.0000454        (1/e^10, very small)
          10^10 = 10,000,000,000     (ten billion)
          10! = 3,628,800            (10x9x8x7x6x5x4x3x2x1)
  STEP 5  combine:
          P = 0.0000454 x 10,000,000,000 / 3,628,800
          first the division: 10,000,000,000 / 3,628,800 = 2755.7
          then: 0.0000454 x 2755.7 = 0.1251
```

ANSWER: P(exactly 10 in 5 minutes) = 0.1251, about 12.5 percent.

TRAP:
```
   1. Using lambda = 2 (the per-minute rate) when the question asks about 5 minutes. This is
      THE most common Poisson mistake on this course.
   2. Arithmetic slips with 10!. Write it as a decimal or reduce before multiplying.
   3. Confusing this with the NESTING question (next). Here it is a single Poisson; there,
      a second stage follows.
```

═══════════════════════════════════════════════════════════════════════════════
F2.5  NESTING: Poisson then Binomial (the composite they love)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 6 (our deck, ppt3 p026 - the two-stage chain)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Telephone calls arrive at an exchange according to the Poisson process at the rate
   of 2 per minute. What is the probability that exactly 2 calls arrive in each minute
   over a 5-minute period?
```

STEP 0: DECODE - this is TWO MODELS IN ONE. Read it twice.

```
   STAGE 1: calls per minute follow Poisson(2).
   STAGE 2: over 5 minutes, we need EXACTLY 2 calls in EACH of the 5 minutes.
            "each minute" -> five independent successes, each meaning "2 calls in that minute"
            -> that is a BINOMIAL with n = 5, p = P(exactly 2 calls in one minute)
```

THE TWO-STAGE PICTURE (draw this in the exam before computing):

```
   +--------------------------------------------------------+
   | STAGE 1: one minute, lambda = 2                        |
   |   find p = P(X = 2) for Poisson(2)                     |
   +---------------------------+----------------------------+
                               |
                               v
   +--------------------------------------------------------+
   | STAGE 2: five minutes, each independently must hit     |
   |   n = 5 trials, success = "that minute had exactly 2"   |
   |   p = (the value from stage 1)                         |
   |   want P(all 5 succeed) = p^5                          |
   +--------------------------------------------------------+
```

EVERY STEP:

```
  STAGE 1:
  STEP 1  p = P(X=2) with lambda=2
             = e^(-2) x 2^2 / 2!
             = 0.1353 x 4 / 2
             = 0.1353 x 2
             = 0.2707

  STAGE 2:
  STEP 2  Each minute must have exactly 2 calls. There are 5 minutes.
          The chance a given minute qualifies is p = 0.2707.
          All 5 must qualify, independently:
          P(all five) = p x p x p x p x p = p^5
          = 0.2707^5

  STEP 3  0.2707^2 = 0.07328
          0.2707^4 = 0.07328^2 = 0.005370
          0.2707^5 = 0.005370 x 0.2707 = 0.001453

  STEP 4  so P = 0.00145, about 0.145 percent
```

ANSWER: 0.00145 (which is 32 e^-10, the textbook's exact form).

WHY IT IS EXACTLY 32 e^-10:
```
   p = 2 e^-2 ; p^5 = (2 e^-2)^5 = 32 e^-10 ; 32 x 0.0000454 = 0.001453 ✓
```

TRAP:
```
   1. Reading it as a single Poisson over 5 minutes (lambda = 10, P(10) = 0.1251). That
      answers a DIFFERENT question ("10 calls total") and gets it wrong. The phrase is
      "in EACH minute", which forces the two stages.
   2. Using C(5,2) or another combination in stage 2. Every minute must succeed, so it is
      p^5, not C(5,2) p^2 ...
   3. Mixing the two stages' lambdas.
```

═══════════════════════════════════════════════════════════════════════════════
F2.6  MOMENTS ALGEBRA:  Var of a function of a Poisson
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 7 (MTE 2024-25 paper, block A1 - the real thing)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A Poisson variate X has mean equal to 0.5. If Y = 2X, then which of the following
   is/are correct?
   i. E(Y) = 1     ii. Var(Y) = 4     iii. Var(Y) = 2     iv. E(Y) = 2
   a. (i) and (ii) only    b. (ii) & (iv) only
   c. (i) & (iii) only     d. (iii) & (iv) only
```

STEP 0: DECODE

```
   "Poisson variate with mean 0.5" -> lambda = 0.5, and therefore ALSO Var(X) = 0.5
   "Y = 2X"                        -> Y is X multiplied by the constant 2
   the ask: which statements about E(Y) and Var(Y) are true?
```

THE TWO RULES (both needed):

```
   +--------------------------------------------------+
   |  for Y = aX (a is a constant):                   |
   |                                                  |
   |     E(Y)   = a x E(X)        <- constants pass  |
   |                                 straight through |
   |     Var(Y) = a^2 x Var(X)    <- constants get   |
   |                                 SQUARED for      |
   |                                 variance         |
   +--------------------------------------------------+
```

THE PICTURE:

```
   X: mean 0.5, variance 0.5      (Poisson: they are equal)
    |
    |  double it: Y = 2X
    v
   Y: mean 2 x 0.5 = 1            (doubled)
      variance 2^2 x 0.5 = 2      (quadrupled, because 2^2 = 4)
```

EVERY STEP:

```
  STEP 1  E(Y) = E(2X) = 2 x E(X) = 2 x 0.5 = 1
          -> statement (i) "E(Y) = 1" is TRUE
          -> statement (iv) "E(Y) = 2" is FALSE

  STEP 2  Var(Y) = Var(2X) = 2^2 x Var(X) = 4 x 0.5 = 2
          -> statement (iii) "Var(Y) = 2" is TRUE
          -> statement (ii) "Var(Y) = 4" is FALSE
          (the decoy 4 is the SQUARED CONSTANT, not the variance. people write 2^2 = 4
           and stop there, forgetting to multiply by Var(X) = 0.5.)

  STEP 3  True statements: (i) and (iii) -> option (c)
```

ANSWER: option (c), (i) and (iii) only.

TRAP:
```
   1. Writing Var(Y) = 4 by squaring the constant and forgetting to multiply by Var(X).
      Var(Y) = a^2 Var(X) = 4 x 0.5 = 2. The 0.5 matters.
   2. Writing Var(Y) = 2 x 0.5 = 1 (passing the constant through un-squared). Also wrong.
   3. Forgetting that for a Poisson, Var(X) = mean = 0.5. This is the distribution's
      signature and it is what makes this question solvable.
```

═══════════════════════════════════════════════════════════════════════════════
F2.7  FORMULA MCQ / IDENTIFICATION
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 8 (our paper, ETE re-session S4 A2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Which distribution has same mean and variance?
   a) Normal    b) Poisson    c) Uniform    d) Exponential
```

DECODE: pure recall of the signature.

ANSWER: (b) Poisson.

THE COMPARISON TABLE (memorize this row; it is a likely MCQ):

```
   +-------------+----------------+-------------------+
   | distribution| mean           | variance          |
   +-------------+----------------+-------------------+
   | Poisson     | lambda         | lambda   <- SAME  |
   | Binomial    | np             | npq               |
   | Normal      | mu             | sigma^2           |
   | Uniform     | (a+b)/2        | (b-a)^2/12        |
   | Exponential | 1/lambda       | 1/lambda^2        |
   +-------------+----------------+-------------------+
```

TRAP: choosing Normal (because it has two parameters) or Exponential. Only Poisson has
mean EQUAL to variance as an identity.

═══════════════════════════════════════════════════════════════════════════════
F2 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   FORMULA:   P(X=k) = e^(-lambda) lambda^k / k!
   MEAN = VARIANCE = lambda        <- the signature
   0! = 1

   WINDOW RULE: lambda must match the span asked about.
                per minute rate + 5-minute ask -> lambda = rate x 5

   SWITCH FROM BINOMIAL WHEN: n big (>=100) and p small (<=0.01), lambda = n x p

   RECOVERY FROM A RATIO: set the two pmfs equal, cancel e^(-l), solve.
        P(X=1)=P(X=2) -> l=2 ;  P(Y=2)=P(Y=3) -> m=3
        general: P(X=k)=P(X=k+1) -> lambda = k+1

   VARIANCE RULES (independent):
        Var(X + Y) = Var(X) + Var(Y)
        Var(X - Y) = Var(X) + Var(Y)     <- minus becomes PLUS
        Var(aX)    = a^2 Var(X)          <- square the constant
        Var(X - 2Y) = Var(X) + 4 Var(Y)

   WORD MAP:
     "no demand" / "none"        -> P(0) = e^(-lambda)
     "at least k"                -> 1 - P(0) - ... - P(k-1)
     "at most k"                 -> P(0) + ... + P(k)
     "how many boxes expected"   -> COUNT = boxes x P(event)
     "in each of n intervals"    -> NESTING: Poisson first, then p^n

   TOP TRAPS:
     lambda not rescaled to the asked window (the #1 error)
     "at least 2" dropping P(1)
     Var(aX) using a instead of a^2
     Var(X - Y) written as Var(X) - Var(Y) (impossible; variances add)
```
