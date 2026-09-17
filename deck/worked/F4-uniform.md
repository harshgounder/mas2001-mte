# F4 UNIFORM: every shape, every question, solved from zero

Source: our own material (MTE 2024-25 blocks B3 and B4, the ETE papers E25S4, and the ppt4
deck). Nothing invented. Every number machine-checked (6/6 checks pass).

```
  SHAPES IN THIS FILE
  F4.1  pdf + moments MCQ      name the mean                    1 question
  F4.2  length-ratio point     P(a<X<b)                         1 question (MTE!)
  F4.3  wait-time application  the trains question               1 question (MTE!)
  F4.4  composite with Chebyshev  bound vs actual                1 question (MTE!)
```

═══════════════════════════════════════════════════════════════════════════════
BEFORE ANY QUESTION: what "uniform" means
═══════════════════════════════════════════════════════════════════════════════

Uniform means EVERY VALUE IN THE RANGE IS EQUALLY LIKELY. The picture is a flat rectangle.

```
   +-------------------------------------------------------------------+
   |  X between a and b, written U(a, b):                                |
   |                                                                     |
   |     pdf     f(x) = 1 / (b - a)        for a <= x <= b               |
   |     MEAN    (a + b) / 2                                             |
   |     VARIANCE (b - a)^2 / 12                                         |
   |                                                                     |
   |  THE KEY IDEA: probability = LENGTH RATIO                           |
   |                                                                     |
   |            length of the part you want                              |
   |   P  =  ---------------------------------                           |
   |            length of the whole range                                |
   +-------------------------------------------------------------------+
```

THE PICTURE:

```
   f(x)
   1/(b-a) |######################|     flat top
           |######################|
           |######################|
           +-----[a==========b]---+
                 the rectangle. area = height x width = 1/(b-a) x (b-a) = 1 ✓

   asking P(c < X < d):
   1/(b-a) |      +########+      |
           |      +########+      |
           +------[c########d]----+-----+
                  the shaded piece. its width is (d-c).
                  probability = (d - c) / (b - a)
```

THE CLIPPING RULE (draw the rectangle every time to avoid this):

```
   +--------------------------------------------------------------+
   |  the part you want must be CLIPPED to the range.              |
   |                                                               |
   |  U(2,6), ask P(1 < X < 5):                                    |
   |     the part starts at 1, but the range starts at 2, so        |
   |     use 2, not 1: length = 5 - 2 = 3                          |
   |                                                               |
   |  U(2,6), ask P(X > 7):                                        |
   |     7 is outside the range, so this is impossible: P = 0      |
   +--------------------------------------------------------------+
```

═══════════════════════════════════════════════════════════════════════════════
F4.1  MOMENTS MCQ:  name the mean
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 1 (our paper, ETE 2025-26 S4 A6)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   The mean value of Uniform distribution f(x) = 1/(b-a) is:
   a. (a+b)/2    b. (a-b)/2    c. (b-a)/2    d. Undefined
```

DECODE: the mean of a range is its MIDPOINT, the value exactly halfway between a and b.

ANSWER: (a) (a+b)/2.

WHY IT IS THE MIDPOINT (a picture proof, in case the MCQ asks you to argue it):

```
   a -------------|------------- b
                 mid
   the midpoint is a + (b-a)/2
                 = (2a + b - a) / 2
                 = (a + b) / 2        ✓ same thing
```

TRAP:
```
   1. Option (c) (b-a)/2 is the HALF-WIDTH, not the mean. It is a decoy aimed at people who
      remember a formula has a "/2" but not which one.
   2. Option (b) (a-b)/2 is negative for a<b, impossible for a mean inside [a,b].
```

═══════════════════════════════════════════════════════════════════════════════
F4.2  LENGTH-RATIO POINT
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 2 (course material / the ppt4 form)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A random variable X is uniformly distributed over the interval (2, 6). Find
   (a) P(2 < X < 5)   (b) P(X > 4)   (c) P(3 < X < 7)
```

STEP 0: DECODE

```
   a = 2, b = 6   (from "over the interval (2, 6)")
   "P(2 < X < 5)"  -> the part runs from 2 to 5
   "P(X > 4)"      -> the part runs from 4 to 6 (up to the end of the range)
   "P(3 < X < 7)"  -> the part runs from 3 to 7, BUT 7 is outside the range (max is 6)
                      so it must be CLIPPED to 6
```

THE RECTANGLE, DRAWN THREE TIMES:

```
  (a) P(2<X<5)
       |#########     |
      [2#########5   6]      part = 5-2 = 3, whole = 6-2 = 4

  (b) P(X>4)
       |      ########|
      [2     4########6]     part = 6-4 = 2, whole = 4

  (c) P(3<X<7)  <- CLIP the 7 down to 6
       |   ########   |      part = 6-3 = 3, whole = 4
      [2  3########6  ]7
```

EVERY STEP:

```
  PART (a):
  STEP 1  whole range length = b - a = 6 - 2 = 4
  STEP 2  wanted length = 5 - 2 = 3
  STEP 3  P = 3 / 4 = 0.75

  PART (b):
  STEP 4  "X > 4" means from 4 to the end of the range, 6
  STEP 5  wanted length = 6 - 4 = 2
  STEP 6  P = 2 / 4 = 0.5

  PART (c):
  STEP 7  "3 < X < 7": the upper end 7 is beyond the range (which ends at 6)
  STEP 8  CLIP: use 6 instead of 7
  STEP 9  wanted length = 6 - 3 = 3
  STEP 10 P = 3 / 4 = 0.75
```

ANSWER:
```
   (a) 0.75   (b) 0.5   (c) 0.75
```

TRAP:
```
   1. NOT clipping in part (c): (7-3)/4 = 4/4 = 1.0, which would say "certainty", but X
      can never reach 7 so that is wrong. CLIP.
   2. Using the raw numbers for the whole range when a and b are not neat. Always
      compute b - a explicitly.
   3. In part (b), using 4/4 or 2/6. The denominator is always the full range (4).
```

MUTATIONS:
```
   IF U(0,5): P(X<2) = 2/5 = 0.4.
   IF U(-3,3): P(|X|<1) = P(-1<X<1) = 2/6 = 1/3.
        (the |X| < k form must be expanded to an interval FIRST)
   IF U(a,b) with mean 1 and variance 4/3 (our ETE form): solve two equations:
        (a+b)/2 = 1        -> a + b = 2
        (b-a)^2/12 = 4/3   -> (b-a)^2 = 16 -> b - a = 4
        adding: 2b = 6 -> b = 3, so a = -1.  the range is (-1, 3).
```

═══════════════════════════════════════════════════════════════════════════════
F4.3  WAIT-TIME APPLICATION:  the trains question
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 3 (MTE 2024-25 paper, block B4 - the real thing)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Trains arrive at a station at 15 minute intervals starting at 4 AM. If a passenger
   arrives at the station at a time that is uniformly distributed between 9:00 AM and
   9:30 AM, find the probability that he has to wait for the train for
   (a) less than 6 minutes   (b) more than 10 minutes.
```

STEP 0: DECODE - this is the "question hidden in the story" pattern. Three translations
are needed before any maths.

```
   TRANSLATION 1 - what is the WAIT?
       trains come every 15 minutes. whatever time you arrive, you wait until the next
       train. the wait is uniformly spread between 0 and 15 minutes.
       -> W = wait time, uniform on (0, 15).  a = 0, b = 15.

   TRANSLATION 2 - why "9:00 to 9:30" does not matter
       the passenger's arrival is uniform over a 30-minute window, but the TRAINS come
       every 15 minutes, so the wait pattern is the same no matter which 30 minutes.
       -> the 9:00-9:30 detail is FLAVOUR, not data. the real range is (0,15).

   TRANSLATION 3 - the asks
       "less than 6 minutes" -> P(W < 6)
       "more than 10 minutes"-> P(W > 10), meaning 10 to 15
```

THE PICTURE (why the wait is uniform on 0 to 15):

```
   train     train     train
     |         |         |
     |---15----|---15----|
     ^
     passenger arrives at a random moment in this gap

   if she arrives just after a train, wait ~ 0
   if she arrives just before the next, wait ~ 15
   every value in between is equally likely -> wait ~ U(0, 15)

   the WAIT rectangle:
      |###           |
     [0###6        15]        (a) less than 6: part = 6-0 = 6, whole = 15
      |          ####|
     [0         10##15]       (b) more than 10: part = 15-10 = 5, whole = 15
```

EVERY STEP:

```
  STEP 1  whole range length = 15 - 0 = 15

  PART (a):
  STEP 2  wanted length = 6 - 0 = 6
  STEP 3  P(W < 6) = 6 / 15 = 0.4

  PART (b):
  STEP 4  "more than 10" runs from 10 to the end of the range, 15
  STEP 5  wanted length = 15 - 10 = 5
  STEP 6  P(W > 10) = 5 / 15 = 1/3 = 0.3333
```

ANSWER:
```
   (a) P(wait less than 6 min) = 0.4
   (b) P(wait more than 10 min) = 1/3 (about 33 percent)
```

TRAP:
```
   1. THE BIG ONE: using 9:00 to 9:30 as the range (30 minutes) instead of the wait range
      (0 to 15). The question hands you a 30-minute window, but the WAIT only ever runs
      0 to 15 because a train comes every 15 minutes. If you use 30 as the denominator you
      get 6/30 = 0.2, which is wrong. The tell: "wait for the train", so the variable is
      the WAIT, and the wait's range is set by the INTERVAL between trains.
   2. Forgetting that "more than 10" ends at 15, not at 30.
   3. Not seeing that the uniform is on the wait, not on the arrival time. The arrangement
      of train times converts an arrival-uniform into a wait-uniform.
```

SELF CHECK:
```
   the wait is always between 0 and 15, so P(W<6) + P(6<W<10) + P(W>10) = 1:
   0.4 + (4/15 = 0.2667) + 0.3333 = 1.0000 ✓
```

MUTATION:
```
   IF trains come every 20 minutes  THEN the wait is U(0,20), and every denominator is 20.
   IF the ask is "less than 5"      THEN 5/15 = 1/3.
   IF trains come every 15 min and the window is 45 min THEN still U(0,15): the interval
        between trains is what matters, not the arrival window.
```

═══════════════════════════════════════════════════════════════════════════════
F4.4  COMPOSITE:  Uniform + Chebyshev  (bound vs actual)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 4 (MTE 2024-25 paper, block B3 - the real thing)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Let X be uniformly distributed U(-1, 1). Compute the upper bound on probability
   P[ |X - E(X)| >= 2 sqrt(Var(X)) ] using Chebyshev's inequality.
   Also, obtain the actual probability.
```

STEP 0: DECODE - this is TWO questions in one, and the second one is the interesting part.

```
   ASK 1: the CHEBYSHEV BOUND (always computable)
   ASK 2: the ACTUAL probability (specific to this uniform distribution)
   "Also" is the signal that you must answer BOTH. two marks each, four total.
```

STEP 1: FIND THE INGREDIENTS OF U(-1, 1)

```
   a = -1, b = 1

   E(X)   = (a+b)/2 = (-1+1)/2 = 0
   Var(X) = (b-a)^2 / 12 = (1-(-1))^2 / 12 = 2^2/12 = 4/12 = 1/3
   sd(X)  = sqrt(1/3) = 0.5774
```

STEP 2: READ WHAT THE PROBABILITY IS ASKING

```
   P[ |X - E(X)| >= 2 sqrt(Var(X)) ]
        |           |        |
     centre 0    k=2 copies of sd

   = P[ |X - 0| >= 2 x 0.5774 ]
   = P[ |X| >= 1.1547 ]
```

STEP 3: THE CHEBYSHEV BOUND

```
   Chebyshev tail form: P(|X - mu| >= k sigma) <= 1 / k^2
   here k = 2
   bound = 1 / 2^2 = 1/4 = 0.25
```

STEP 4: THE ACTUAL PROBABILITY (the part people miss)

```
   THE CRITICAL OBSERVATION: X lives only in [-1, 1]. So |X| can be at most 1.
   But we need |X| >= 1.1547, and 1.1547 is LARGER than 1.

   so NO value of X can ever satisfy |X| >= 1.1547.
   the actual probability is 0.

   the picture:
        |X| can reach here:        |===========|   (0 to 1)
        where we need it:                |=======|  (1.1547 and beyond)
                                         ^
                                   nothing lives out here

   actual P = 0
```

THE ANSWER:
```
   Chebyshev bound (the upper limit)  = 0.25
   actual probability                 = 0
   and note 0 <= 0.25: the bound HOLDS (it is an upper limit and the truth is below it),
   but it is very LOOSE here. that looseness is the point of the question.
```

THE COMPARISON PICTURE:

```
   bound:  |################|         0.25
   actual: |                          0.00
   the bound permits up to 25 percent, the truth is none. Chebyshev is safe but crude.
   (this is why the deck calls it distribution-free: it must work for EVERY distribution,
    so it cannot be tight for any particular one.)
```

TRAP:
```
   1. Answering only the bound (0.25) and skipping the actual. The word "Also" is worth
      half the marks.
   2. Computing the actual by trying to integrate. Read the support: |X| maxes at 1, the
      threshold is 1.1547, so it is simply 0. No integration needed.
   3. Using Var = 1/3 but forgetting the sqrt, then comparing k=2 against 1/3 (wrong scale).
      The threshold is 2 x sqrt(Var) = 2 x 0.5774 = 1.1547.
   4. Reporting a negative or "impossible" probability. The actual is 0, which is a perfectly
      valid probability.
```

MUTATIONS:
```
   IF U(-1,1) and k=1  THEN threshold = 1 x 0.5774 = 0.5774 (inside the range).
        actual: P(|X| >= 0.5774) = [part from 0.5774 to 1] + [part from -1 to -0.5774]
              = 2 x (1 - 0.5774)/2 = 0.4226
        bound = 1/1^2 = 1 (meaningless but valid).
   IF U(-2,2) and k=2  THEN Var = 16/12 = 1.333, sd = 1.1547, threshold = 2.31 > 2 = max|X|,
        so actual is again 0. the pattern: when the threshold exceeds the support, the
        actual is 0.
```

═══════════════════════════════════════════════════════════════════════════════
F4 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   U(a,b):  f = 1/(b-a) | MEAN = (a+b)/2 | VAR = (b-a)^2/12 (so sd = (b-a)/sqrt(12))

   THE ONE IDEA: probability = LENGTH RATIO = (wanted length) / (b - a)

   CLIPPING: whatever you want must sit INSIDE [a,b].
        ask below a  -> start at a
        ask above b  -> end at b
        ask fully outside -> probability 0

   |X| FORMS:  P(|X - c| < d) = P(c-d < X < c+d), then clip.

   STORY PATTERN (trains, buses):  the WAIT is uniform on (0, interval-between-arrivals).
        the arrival window in the story is FLAVOUR, not the range.

   COMPOSITE: bound vs actual -> answer BOTH. read the support before integrating;
        sometimes the actual is 0 by inspection.

   TOP TRAPS:
     not clipping
     using the story's window instead of the wait's range
     skipping the "Also" half of a bound-vs-actual question
     mixing up (a+b)/2 (mean) with (b-a)/2 (half-width)
```
