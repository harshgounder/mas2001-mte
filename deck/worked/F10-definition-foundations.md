# F10 DEFINITION AND FOUNDATION QUESTIONS: solved from zero

Source: our own material (the ETE papers E25S4, E25SUM, R25S4, E24S3, E25S3). Nothing invented.
All numbers machine-checked (5/5).

WHY THIS FILE EXISTS: these are pure-recall marks. They are the cheapest marks on the paper
and students lose them by not having the definitions word-perfect. Every sentence here has
appeared in a real paper.

```
  SHAPES IN THIS FILE
  F10.1  what a random variable is       3 questions (all near-identical)
  F10.2  the pmf find-k drill            1 question (with a twist: three k-terms)
  F10.3  the joint pmf + marginal        1 question
  F10.4  the expectation chain           (covered in F1-F3; summarized here)
```

═══════════════════════════════════════════════════════════════════════════════
F10.1  WHAT A RANDOM VARIABLE IS
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 1 (asked three times: ETE 2025-26 S4 A1, ETE 2025 summer Q1, ETE re-sess S4 A1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A random variable is:
   a. A constant value
   b. A probability
   c. A function from the sample space to the real numbers
   d. An event
```

ANSWER: (c) a function from the sample space to the real numbers.

WHY (the picture that makes it stick):

```
   sample space S            real number line
   (all outcomes)            (the numbers)
   +-----------+             +------------+
   |  HH       |----->  2    |            |
   |  HT       |----->  1    |            |
   |  TH       |----->  1    |            |
   |  TT       |----->  0    |            |
   +-----------+             +------------+
        outcomes                 values

   a random variable is the MAPPING (the arrows). It takes each outcome and
   assigns it a NUMBER. That is why it is a FUNCTION.
```

THE VARIANTS (all three papers ask this; the wording changes slightly):
```
   "a function from sample space to real numbers"        (E25S4-A1, E25SUM-1)
   "A discrete random variable X is a function that maps: the sample space to the set of
    countable real numbers"                              (R25S4-A1 - the discrete version)
```

TRAP:
```
   1. Choosing (a) "a constant value". A random variable takes DIFFERENT values for different
      outcomes; only its distribution is fixed.
   2. Choosing (b) "a probability". A probability is a number between 0 and 1; a random
      variable can take any value (heights, counts, sums).
   3. Choosing (d) "an event". An event is a SUBSET of the sample space. The random variable
      is the map from outcomes to numbers, not a subset.
```

THE RELATED ONE-LINERS (worth memorizing; they appear as fill-in-the-blanks):

```
   "P(X = an exact value) = 0 for a CONTINUOUS random variable"     (ETE S4)
       (because a single point has zero area under a density)

   "For a standard normal variate, the mean is 0"                   (ETE S3)
   "Mean and variance of a standard normal are 0 and 1"             (ETE S4)

   "The range of a distribution function is [0, 1]"
       (a cdf is a probability, so it lies between 0 and 1)

   "A discrete random variable takes a COUNTABLE number of values"
```

═══════════════════════════════════════════════════════════════════════════════
F10.2  THE PMF FIND-K DRILL  (with the three-k-terms twist)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 2 (our paper, ETE 2025 summer Q12; the same table appears again in Q B1 of the same paper)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A random variable X has the following probability distribution.
   +-----+-----+-----+------+------+------+------+------+----------+
   |  X  |  0  |  1  |  2   |  3   |  4   |  5   |  6   |    7     |
   +-----+-----+-----+------+------+------+------+------+----------+
   | P(X)|  0  |  k  |  2k  |  2k  |  3k  | k^2  | 2k^2 | 7k^2 + k |
   +-----+-----+-----+------+------+------+------+------+----------+
   (i) Find the value of k.   (ii) Find P(1.5 < X < 3.5).
   (the Q B1 variant of the same table asks: (i) evaluate P(X<6), P(X>=6), P(0<X<5);
    (ii) if P(X <= a) > 1/2 find the minimum value of a; (iii) the distribution function)
```

STEP 0: DECODE - every pmf must sum to 1. That is the only tool needed.

```
   the rule: sum of all probabilities = 1
   the twist: the terms include k AND k^2, so summing gives a QUADRATIC in k.
```

EVERY STEP:

```
  STEP 1  write the sum of all the probabilities:
          P(total) = 0 + k + 2k + 2k + 3k + k^2 + 2k^2 + (7k^2 + k)

  STEP 2  collect the k terms:
          the terms in order are:
               0, k, 2k, 2k, 3k, k^2, 2k^2, 7k^2 + k
          the k-terms: k + 2k + 2k + 3k + k(from the last term) = 9k
          the k^2-terms: k^2 + 2k^2 + 7k^2 = 10k^2

  STEP 3  set the sum equal to 1:
          9k + 10k^2 = 1
          10k^2 + 9k - 1 = 0

  STEP 4  solve the quadratic. a=10, b=9, c=-1:
          k = [ -9 +/- sqrt(81 + 40) ] / 20
            = [ -9 +/- sqrt(121) ] / 20
            = [ -9 +/- 11 ] / 20

  STEP 5  two roots:
          k = (-9 + 11)/20 = 2/20 = 1/10 = 0.1     <- valid
          k = (-9 - 11)/20 = -20/20 = -1           <- REJECT (k is a probability weight)

  STEP 6  so k = 1/10
```

ANSWER: k = 1/10 = 0.1.

THE SANITY CHECK (always substitute back):
```
   with k = 0.1:  k^2 = 0.01
   9k + 10k^2 = 0.9 + 0.1 = 1.0 ✓  the probabilities sum to 1.
```

PART (ii) - P(1.5 < X < 3.5):

```
  STEP 1  X is DISCRETE, so only whole values count: 1.5 < X < 3.5 means X = 2 or X = 3.
  STEP 2  P(X=2) + P(X=3) = 2k + 2k = 4k
  STEP 3  = 4 x 0.1 = 0.4
```

ANSWER part (ii): 0.4.

THE Q B1 VARIANT (the same table, five more asks; this is the full drill):

```
   with k = 0.1, the full pmf table is:
   +-----+-------+-------+-------+-------+-------+-------+-------+-------+
   |  X  |   0   |   1   |   2   |   3   |   4   |   5   |   6   |   7   |
   +-----+-------+-------+-------+-------+-------+-------+-------+-------+
   | P(X)|  0    |  0.1  |  0.2  |  0.2  |  0.3  | 0.01  | 0.02  | 0.17  |
   +-----+-------+-------+-------+-------+-------+-------+-------+-------+
   (each cell from the k-expressions: 7k^2 + k = 7(0.01) + 0.1 = 0.17)
   sum check: 0.1+0.2+0.2+0.3+0.01+0.02+0.17 = 1.0 ✓

   (i) P(X < 6) = P(0)+P(1)+P(2)+P(3)+P(4)+P(5)
                = 0 + 0.1 + 0.2 + 0.2 + 0.3 + 0.01
                = 0.81
                (in k-form: 8k + k^2 = 0.8 + 0.01 = 0.81 ✓)

       P(X >= 6) = P(6) + P(7) = 0.02 + 0.17 = 0.19
                (in k-form: 9k^2 + k = 0.09 + 0.1 = 0.19 ✓)
       note 0.81 + 0.19 = 1.00 ✓ (they are complements)

       P(0 < X < 5) = P(1)+P(2)+P(3)+P(4) = 0.1+0.2+0.2+0.3 = 0.8
                (in k-form: 8k = 0.8 ✓)

   (ii) P(X <= a) > 1/2. Build the cumulative distribution and look for the first value
        ABOVE 0.5 (strictly):
            F(1) = 0.1
            F(2) = 0.3
            F(3) = 0.5    <- equal to 1/2, but the condition is STRICTLY greater
            F(4) = 0.8    <- first value above 1/2
        so the minimum a is 4.

   (iii) the distribution function (the cdf), piecewise:
            F(x) = 0         for x < 1
                 = 0.1       for 1 <= x < 2
                 = 0.3       for 2 <= x < 3
                 = 0.5       for 3 <= x < 4
                 = 0.8       for 4 <= x < 5
                 = 0.81      for 5 <= x < 6
                 = 0.83      for 6 <= x < 7
                 = 1.0       for x >= 7
```

TRAP:
```
   1. Forgetting the k-term hidden INSIDE the last expression (7k^2 + k). Its "k" is easy to
      miss, and without it the sum is 8k + 10k^2 and the quadratic has a different (wrong)
      answer (that one solves to k = 0.1099, not 0.1).
   2. Forgetting that a quadratic has TWO roots and not discarding the negative one. A
      probability weight cannot be negative, so -1 is out.
   3. In part (ii)-of-B1: stopping at F(3) = 0.5. The condition is P(X<=a) > 1/2 STRICTLY,
      and 0.5 is not > 0.5, so it must be a = 4.
   4. For discrete X, "1.5 < X < 3.5" means X=2 and X=3 only. Do not try to include any
      fractional values.

═══════════════════════════════════════════════════════════════════════════════
F10.3  THE JOINT PMF AND THE MARGINAL  (a two-variable extension)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 3 (our paper, ETE 2025 summer Q14)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   The joint probability mass function of (X, Y) is given by
   P(x, y) = K(2x + 3y),  x = 0, 1, 2;  y = 1, 2, 3.
   Find (i) the value of K, (ii) the marginal distribution of X for x = 0, 1, 2.
```

STEP 0: DECODE - "joint" means two variables at once. Two new skills: sum over a 2D grid, and
"marginalise" (sum over the other variable).

```
   "joint pmf" = the probability of the PAIR (x, y) together
   "marginal distribution of X" = the probability of X alone, ignoring Y
       = sum the joint probabilities over ALL values of y
```

STEP 1: (i) FIND K - the total over the whole grid must be 1

```
   THE GRID (a 3x3 table of pairs, since x has 3 values and y has 3 values):

        x=0   x=1   x=2
   y=1  (0,1) (1,1) (2,1)
   y=2  (0,2) (1,2) (2,2)
   y=3  (0,3) (1,3) (2,3)

   SUM of (2x + 3y) over all 9 pairs:
        work row by row (fix y, sum over x):

     y=1: (2(0)+3(1)) + (2(1)+3(1)) + (2(2)+3(1))
        = 3 + 5 + 7 = 15
     y=2: (2(0)+3(2)) + (2(1)+3(2)) + (2(2)+3(2))
        = 6 + 8 + 10 = 24
     y=3: (2(0)+3(3)) + (2(1)+3(3)) + (2(2)+3(3))
        = 9 + 11 + 13 = 33

   total = 15 + 24 + 33 = 72
   (machine-checked: 72)

   so  K x 72 = 1  ->  K = 1/72
```

STEP 2: (ii) THE MARGINAL OF X

```
   for each value of x, ADD the joint probabilities over ALL y:

   P(X = 0) = P(0,1) + P(0,2) + P(0,3)
            = (1/72)(3) + (1/72)(6) + (1/72)(9)
            = (1/72)(3 + 6 + 9)
            = 18/72
            = 1/4 = 0.25

   P(X = 1) = P(1,1) + P(1,2) + P(1,3)
            = (1/72)(5) + (1/72)(8) + (1/72)(11)
            = (1/72)(5 + 8 + 11)
            = 24/72
            = 1/3 = 0.3333

   P(X = 2) = P(2,1) + P(2,2) + P(2,3)
            = (1/72)(7) + (1/72)(10) + (1/72)(13)
            = (1/72)(7 + 10 + 13)
            = 30/72
            = 5/12 = 0.4167
```

THE ANSWER TABLE:

```
   +-----+--------+--------+
   |  x  | P(X=x) | decimal|
   +-----+--------+--------+
   |  0  |  1/4   | 0.2500 |
   |  1  |  1/3   | 0.3333 |
   |  2  |  5/12  | 0.4167 |
   +-----+--------+--------+
   sum   = 1/4 + 1/3 + 5/12 = 3/12 + 4/12 + 5/12 = 12/12 = 1 ✓
```

THE PICTURE (marginalising = squashing the grid):

```
   the joint grid:            squash each COLUMN into the margin:
        y=1  y=2  y=3              x=0  x=1  x=2
   x=0   [3]  [6]  [9]   -->      |    |    |
   x=1   [5]  [8]  [11]       sum each row across y
   x=2   [7]  [10] [13]           1/4  1/3  5/12
                                  (all divided by 72)
```

TRAP:
```
   1. Not dividing by the total (forgetting K entirely). The numbers 18, 24, 30 must each be
      divided by 72.
   2. Summing over x instead of y when finding the marginal of X. For the marginal of X, sum
      over the OTHER variable (y), because you are removing y from the picture.
   3. Arithmetic in the grid: write all 9 cells before summing, so nothing is missed.
```

═══════════════════════════════════════════════════════════════════════════════
F10.4  THE EXPECTATION CHAIN (recap; the full treatment is in F1-F3)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 4 (our paper, ETE 2025-26 S3 B3 - one question, three asks, linked)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Let X be a random variable with the following probability distribution:
   +--------+-----+-----+-----+
   | X = x  | -3  |  6  |  9  |
   +--------+-----+-----+-----+
   | P(X=x) | 1/6 | 1/2 | 1/3 |
   +--------+-----+-----+-----+
   Find E(X) and E(X^2) and, using the laws of expectation, evaluate E(2X+1)^2.
```

STEP 0: DECODE - three linked asks. The third uses the first two.

```
   the key property:  E(2X+1)^2 means E[ (2X+1)^2 ], the expectation of the SQUARE of (2X+1).
   expand it first:   (2X+1)^2 = 4X^2 + 4X + 1
   then by linearity: E(4X^2 + 4X + 1) = 4 E(X^2) + 4 E(X) + 1
   so once you have E(X) and E(X^2), the third is one line.
```

EVERY STEP:

```
  STEP 1  E(X) = sum of x times P(x):
          = (-3)(1/6) + (6)(1/2) + (9)(1/3)
          = -1/2 + 3 + 3
          = -1/2 + 6
          = 11/2
          = 5.5

  STEP 2  E(X^2) = sum of x^2 times P(x):
          = (9)(1/6) + (36)(1/2) + (81)(1/3)
          = 9/6 + 36/2 + 81/3
          = 1.5 + 18 + 27
          = 46.5
          = 93/2

  STEP 3  the expansion:
          (2X + 1)^2 = 4X^2 + 4X + 1

  STEP 4  apply linearity of expectation:
          E[(2X+1)^2] = 4 E(X^2) + 4 E(X) + 1
                      = 4(46.5) + 4(5.5) + 1
                      = 186 + 22 + 1
                      = 209
```

ANSWER: E(X) = 11/2 (5.5), E(X^2) = 93/2 (46.5), E[(2X+1)^2] = 209.

THE LINEARITY RULE (write it on your sheet; it earns marks in the working):
```
   E(aX + b)   = a E(X) + b          (linear, the constant passes straight through)
   E(aX^2 + bX + c) = a E(X^2) + b E(X) + c     (linearity works term by term)

   NOTE the difference with VARIANCE: E() passes constants straight through, but
   Var() SQUARES them: Var(aX + b) = a^2 Var(X).
```

TRAP:
```
   1. NOT expanding (2X+1)^2 first. Some students compute E(2X+1) = 12 and then square that,
      getting 144. WRONG: E[(2X+1)^2] is not [E(2X+1)]^2. Compute the SQUARE first, then
      take the expectation.
   2. Forgetting the "+1" contributes E(1) = 1.
   3. Slipping on the negative value: (-3)(1/6) is -0.5.
```

THE COMPARISON (this distinction is examined):
```
   +----------------------------+--------------------------+
   | E[(2X+1)^2]                | [E(2X+1)]^2              |
   +----------------------------+--------------------------+
   | square first, then average | average first, then square|
   | = 209  (the answer here)   | = (12)^2 = 144           |
   +----------------------------+--------------------------+
   the question says E(2X+1)^2 with the 2 attached to the bracket, so it is the FIRST one.
```

═══════════════════════════════════════════════════════════════════════════════
F10 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   RANDOM VARIABLE      = a FUNCTION from the sample space to the real numbers
   DISCRETE rv          = countable values
   P(exact value) = 0   for a CONTINUOUS rv
   STANDARD NORMAL      = mean 0, variance 1
   CDF range            = [0, 1]

   PMF RULE              sum of all probabilities = 1  (this is the only tool for find-k)
     if terms include k^2 -> quadratic in k -> two roots -> DISCARD the negative one

   JOINT PMF            P(x,y) = K(...)
     find K:  sum over the WHOLE grid, set = 1
     marginal of X:  sum the joint over all y

   EXPECTATION
     E(X)   = sum x P(x)
     E(X^2) = sum x^2 P(x)
     E[(2X+1)^2]: EXPAND first (4X^2+4X+1), then 4E(X^2)+4E(X)+1
     E[(2X+1)^2] is NOT [E(2X+1)]^2

   TOP TRAPS:
     rv is a function, not a constant/probability/event
     missing a hidden k-term in a long pmf expression
     keeping the negative root of a quadratic
     marginalising over the wrong variable
     squaring the expectation instead of the variable
```
