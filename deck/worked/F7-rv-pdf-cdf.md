# F7 RV / PDF / CDF: every shape, every question, solved from zero

Source: our own material (MTE 2024-25 block A2, MTE 2025-26 blocks Q1 and Q4, the ETE papers
E24S3, E24S4, E25SUM, R25S3, R25S4, and the notes/ppt decks). Nothing invented. Every number
machine-checked (9/9 checks pass, including the integrals done in exact fractions).

THIS IS THE LARGEST FAMILY (14 rows in-scope). Most distribution questions START here.

```
  SHAPES IN THIS FILE
  F7.1  total-mass MCQ     the integral equals what         1 question (MTE!)
  F7.2  find-k             normalise a density               1 question (MTE!)
  F7.3  find-two-constants two equations from two conditions 1 question
  F7.4  cdf from pdf       piecewise integration             1 question (MTE!)
  F7.5  pdf from cdf       differentiate                    1 question
  F7.6  pmf table + cdf    the discrete composite            1 question
```

═══════════════════════════════════════════════════════════════════════════════
BEFORE ANY QUESTION: the four things a density must satisfy
═══════════════════════════════════════════════════════════════════════════════

```
   +---------------------------------------------------------------------+
   |  for f(x) to be a PROBABILITY DENSITY:                               |
   |                                                                     |
   |   1. f(x) >= 0     everywhere (no negative probabilities)            |
   |   2. integral of f over ALL x  =  1     (total mass is one)          |
   |   3. P(a < X < b) = integral of f from a to b                        |
   |   4. the CDF  F(x) = integral of f from -inf to x                    |
   |      and  f(x) = F'(x)   (they are a matched pair)                   |
   +---------------------------------------------------------------------+
```

THE PICTURE (density = height, probability = area):

```
   f(x)
     |      ****
     |    ********
     |  ************
     |****************
     +---a----b--------x
       |<-- area -->|
       P(a<X<b) is the shaded AREA, not the height f(b).
```

THE THREE INTEGRALS YOU ACTUALLY NEED (nothing harder appears in this course):

```
   integral of x^n dx  =  x^(n+1) / (n+1)          (+ C, which cancels in definite integrals)

   definite version:
        integral from a to b of x^n dx  =  [ b^(n+1) - a^(n+1) ] / (n+1)
```

═══════════════════════════════════════════════════════════════════════════════
F7.1  TOTAL-MASS MCQ
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 1 (MTE 2025-26 paper, block Q1 - the real thing, the first question on the paper)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   If f(x) is the probability density function of a continuous random variable, then
   integral from -inf to +inf of f(x) dx = .......
   1) 0    2) 1    3) -1    4) infinity
```

DECODE: this is the total-mass axiom. The whole area under any valid density is exactly 1.

ANSWER: option 2, equal to 1.

WHY (one line): the total probability of ALL possible outcomes must be 1. The density's total
area IS that total probability.

PICTURE:
```
     |      ****
     |    ********
     |  ************
     |****************
   --+------------------+--
    -inf               +inf
     |<--- this whole area = 1 --->|
```

TRAP: choosing (4) infinity. The RANGE is infinite, but the AREA is 1. These are different
things. Also (1) 0 is the answer for P(X = exactly one point), not for the whole line.

═══════════════════════════════════════════════════════════════════════════════
F7.2  FIND-K:  normalise a density (the core skill of this whole family)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 2 (MTE 2025-26 paper, block Q4 - the real thing, a full-marks question)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A random variable X is distributed between the values 0 and 4 so that its probability
   density function is f(x) = kx^3(4 - x)^2 where k is a constant.
   Find the value of k. Using this value of k, find its mean and variance.
```

STEP 0: DECODE - THREE asks in one question, in order.

```
   "between 0 and 4"     -> the support is 0 <= x <= 4, and f = 0 outside.
   "f = kx^3(4-x)^2"     -> k is the unknown to find first.
   ASK 1: find k         -> use total mass = 1
   ASK 2: find the mean  -> E(X) = integral of x f(x) dx
   ASK 3: find variance  -> Var = E(X^2) - [E(X)]^2, needs a second integral
```

THE MASTER FLOWCHART:

```
             START: f = k x^3 (4-x)^2 on (0,4)
                          |
                          v
          +---------------------------------------+
          | ASK 1: integrate f over (0,4), set = 1 |
          |        solve for k                     |
          +-------------------+-------------------+
                              |
                              v
          +---------------------------------------+
          | ASK 2: E(X) = integral of x f(x)       |
          +-------------------+-------------------+
                              |
                              v
          +---------------------------------------+
          | ASK 3: E(X^2) = integral of x^2 f(x)   |
          |        Var = E(X^2) - (E(X))^2         |
          +---------------------------------------+
```

STEP 1: EXPAND the density so we can integrate it term by term

```
   (4 - x)^2 = 16 - 8x + x^2           (expand the bracket first: this is where people slip)
   so x^3 (4-x)^2 = x^3 (16 - 8x + x^2)
                  = 16x^3 - 8x^4 + x^5
   therefore  f(x) = k (16x^3 - 8x^4 + x^5)
```

STEP 2: ASK 1 - find k from the total mass

```
   integral from 0 to 4 of f(x) dx = 1

   integral of (16x^3 - 8x^4 + x^5) dx:
      term by term, using x^(n+1)/(n+1):
       16x^3 -> 16 x^4 / 4      = 4x^4
       -8x^4 -> -8 x^5 / 5      = -(8/5) x^5
        x^5  -> x^6 / 6          = (1/6) x^6

   evaluate from 0 to 4:
       4(4^4) = 4 x 256 = 1024
       -(8/5)(4^5) = -(8/5) x 1024 = -1638.4
       (1/6)(4^6) = (1/6) x 4096 = 682.67

   sum: 1024 - 1638.4 + 682.67 = 68.27

   more exactly, in fractions:
       1024 - 8192/5 + 4096/6
     = 1024 - 8192/5 + 2048/3
     common denominator 15:
       = (15360 - 24576 + 10240) / 15
       = 1024/15

   so  integral of x^3(4-x)^2 over (0,4) = 1024/15

   then k x (1024/15) = 1
        k = 15/1024 = 0.0146484
```

STEP 3: ASK 2 - the mean

```
   E(X) = integral from 0 to 4 of x f(x) dx
        = k x integral of x . x^3(4-x)^2 dx
        = k x integral of x^4 (4-x)^2 dx

   x^4(4-x)^2 = x^4(16 - 8x + x^2) = 16x^4 - 8x^5 + x^6

   integral from 0 to 4:
       16 x^5/5 -> 16(1024)/5 = 16384/5 = 3276.8
       -8 x^6/6 -> -(4/3)(4096) = -16384/3 = -5461.33
        x^7/7 -> 16384/7 = 2340.57

   in fractions: 16384/5 - 16384/3 + 16384/7
   common denominator 105:
       = 16384 x (21 - 35 + 15)/105
       = 16384 x (1)/105
       = 16384/105

   E(X) = k x 16384/105 = (15/1024) x (16384/105)
        = 15 x 16 / 105        (since 16384/1024 = 16)
        = 240/105
        = 16/7
        = 2.2857
```

STEP 4: ASK 3 - E(X^2) and then the variance

```
   E(X^2) = k x integral of x^2 . x^3(4-x)^2 dx = k x integral of x^5(4-x)^2 dx

   x^5(4-x)^2 = 16x^5 - 8x^6 + x^7

   integral from 0 to 4:
       16 x^6/6 -> (8/3)(4096) = 32768/3
       -8 x^7/7 -> -(8/7)(16384) = -131072/7
        x^8/8 -> 65536/8 = 8192

   in fractions with denominator 21:
       32768/3 = 229376/21
       -131072/7 = -393216/21
       8192 = 172032/21
       sum = (229376 - 393216 + 172032)/21 = 8192/21

   E(X^2) = k x 8192/21 = (15/1024)(8192/21) = 15 x 8/21 = 120/21 = 40/7 = 5.7143

   Var(X) = E(X^2) - [E(X)]^2
          = 40/7 - (16/7)^2
          = 40/7 - 256/49
          = 280/49 - 256/49
          = 24/49
          = 0.4898
```

ANSWER:
```
   k = 15/1024 (about 0.01465)
   E(X) = 16/7 (about 2.286)
   Var(X) = 24/49 (about 0.4898)
```

SANITY CHECKS (always run these):
```
   1. the mean 2.286 lies inside the support (0,4) ✓
   2. the variance is positive ✓
   3. the density is symmetric-ish around the middle of (0,4), and 2.286 is near 2 ✓
      (the (4-x)^2 factor pulls it slightly right of centre, which is why it is 2.286 not 2.0)
```

TRAP:
```
   1. NOT expanding (4-x)^2 first. Without expanding you cannot integrate term by term.
   2. Arithmetic in the fractions. Write every integral as an exact fraction (as done above)
      and only convert to decimals at the very end. Rounding mid-way ruins the final answer.
   3. Forgetting to multiply the integrals by k. The integral alone is not E(X); you need
      E(X) = k x (integral).
   4. Var = E(X^2) - [E(X)]^2, NOT E(X^2) - E(X). The second term is SQUARED.
```

═══════════════════════════════════════════════════════════════════════════════
F7.3  FIND TWO CONSTANTS from two conditions
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 3 (our paper, ETE 2024-25 S3 B2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A continuous random variable X is distributed over the interval (0,1) with probability
   density function f(x) = ax^2 + bx, where a, b are constants. If the mean of X is 0.5,
   find the value of a and b.
```

STEP 0: DECODE - two unknowns means you need TWO conditions. Find both.

```
   CONDITION 1 (always available): total mass = 1
   CONDITION 2 (given in the question): mean = 0.5
```

THE TWO-EQUATION PICTURE:

```
   +---------------------------+     +---------------------------+
   | CONDITION 1:              |     | CONDITION 2:              |
   | integral f = 1            |     | mean = 0.5                |
   | -> a/3 + b/2 = 1          |     | -> a/4 + b/3 = 1/2        |
   +-------------+-------------+     +-------------+-------------+
                 |                                 |
                 +---------------+-----------------+
                                 |
                                 v
                    solve two equations, two unknowns
```

EVERY STEP:

```
  STEP 1  CONDITION 1, total mass:
          integral from 0 to 1 of (ax^2 + bx) dx = 1
          = a x^3/3 + b x^2/2, evaluated 0 to 1
          = a/3 + b/2
          so:  a/3 + b/2 = 1          (equation I)

  STEP 2  CONDITION 2, the mean:
          mean = integral from 0 to 1 of x f(x) dx = 0.5
          x f(x) = a x^3 + b x^2
          integral = a x^4/4 + b x^3/3, evaluated 0 to 1
          = a/4 + b/3
          so:  a/4 + b/3 = 1/2        (equation II)

  STEP 3  SOLVE. Clear the fractions in (I) by multiplying by 6:
          2a + 3b = 6                 (I')

          Clear the fractions in (II) by multiplying by 12:
          3a + 4b = 6                 (II')

  STEP 4  Subtract to eliminate a. Multiply (I') by 3 and (II') by 2:
          6a + 9b = 18
          6a + 8b = 12
          subtract: b = 6

  STEP 5  Substitute b = 6 into (I'):
          2a + 18 = 6
          2a = -12
          a = -6
```

ANSWER: a = -6, b = 6.

THE CHECK (and a nice surprise):
```
   with a = -6, b = 6:
        f(x) = -6x^2 + 6x = 6x(1 - x)
   that is EXACTLY the cable density 6x(1-x) that appears in the 2024-25 assignments and
   the re-session paper! The questions are connected: this is the same density expressed in
   the general form ax^2+bx.
   verify the conditions: total mass = 1 ✓ and mean = 0.5 ✓ (machine-checked)
```

TRAP:
```
   1. Negative a looks wrong but is CORRECT. The density 6x(1-x) = 6x - 6x^2 has a negative
      x^2 coefficient. Do not "fix" it to make a positive.
   2. Using the wrong integrand for the mean. The mean is integral of x times f(x), so the
      exponents go UP by one: x^2 -> x^3, x -> x^2. Getting this wrong gives a wrong second
      equation.
   3. Sign slips in the subtraction.
```

MUTATION (the same question with different givens):
```
   IF "the mean is 3/4" instead of 0.5   THEN the two equations change and you re-solve.
   IF "variance = 1/20" is given instead of the mean THEN use
        E(X^2) = Var + mean^2, but you would need the mean too - so this variant would also
        have to give the mean, or a different second condition.
```

═══════════════════════════════════════════════════════════════════════════════
F7.4  CDF FROM PDF:  the piecewise case
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 4 (MTE 2024-25 paper, block A2 - the real thing, an MCQ)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Let the pdf of
        f(x) = x        for 0 < x <= 1
        f(x) = 2 - x    for 1 <= x <= 2
        f(x) = 0        otherwise
   The part of its distribution function in the interval 1 <= x <= 2 is
   a) 2x - x^2/2 - 1/2    b) 2x - x^2/2    c) x - x^2/2 + 1    d) 2x - x^2/2 - 1
```

STEP 0: DECODE

```
   "the part of its distribution function in [1,2]" -> find F(x) ONLY for x between 1 and 2.
   the CDF at x is the area under the pdf from the START up to x.
   for x in [1,2], the area has TWO pieces: the part from 0 to 1, plus the part from 1 to x.
```

THE PICTURE (draw this; it is the whole question):

```
   f(x)
    1|  ***
     | ** **
     |**     **
     |         ***
     +---1-------2----x
      ^^^^^^
      piece 1 (0 to 1)
      the triangle up to x=1

   for a general x between 1 and 2:
     |<-- piece 1 -->|<- piece2 ->|
     the first piece is FINISHED (it does not depend on x)
     the second piece grows with x
```

EVERY STEP:

```
  STEP 1  PIECE 1, the area from 0 to 1 of f(x) = x:
          integral of x dx from 0 to 1 = [x^2/2] from 0 to 1 = 1/2 - 0 = 1/2

  STEP 2  PIECE 2, the area from 1 to x of f(x) = 2 - x:
          integral of (2 - x) dx from 1 to x
          = [2t - t^2/2] from t=1 to t=x        (using t so we do not confuse it with x)
          = (2x - x^2/2) - (2(1) - 1^2/2)
          = (2x - x^2/2) - (2 - 1/2)
          = (2x - x^2/2) - 3/2

  STEP 3  TOTAL CDF for 1 <= x <= 2:
          F(x) = piece 1 + piece 2
               = 1/2 + (2x - x^2/2 - 3/2)
               = 2x - x^2/2 - 1

          match: option (d) is 2x - x^2/2 - 1   ✓
```

ANSWER: option (d), F(x) = 2x - x^2/2 - 1 on [1,2].

SANITY CHECKS (do these, they catch the decoys):
```
   at x = 1: F(1) = 2 - 1/2 - 1 = 1/2        ✓ (piece 1 alone should give 1/2)
   at x = 2: F(2) = 4 - 2 - 1 = 1            ✓ (a CDF must reach 1 at the end of support)
   the decoys fail one of these:
      option (a) 2x - x^2/2 - 1/2: F(2) = 4 - 2 - 0.5 = 1.5 > 1  IMPOSSIBLE
      option (b) 2x - x^2/2:       F(2) = 4 - 2 = 2 > 1          IMPOSSIBLE
      option (c) x - x^2/2 + 1:    F(1) = 1 - 0.5 + 1 = 1.5 > 1  IMPOSSIBLE
   ONLY option (d) passes both checks. You could answer this MCQ without integrating at all,
   just by testing x=1 and x=2!
```

TRAP:
```
   1. Forgetting piece 1 (the area already accumulated from 0 to 1). Then you get
      2x - x^2/2 - 3/2 or similar, which matches no option.
   2. Not using the F(1)=1/2 and F(2)=1 checks. They are free and they eliminate all three
      decoys instantly.
   3. Mixing up the two branches of f. Between 1 and 2 the density is (2-x), not x.
```

NOTE ON THE OFFICIAL SCHEME (conflict, flagged honestly):

```
   the handwritten university scheme for this paper appears to mark this MCQ as "B".
   the CORRECT answer is (d), by direct computation:
        F(x) = 1/2 + [2t - t^2/2] from 1 to x = 2x - x^2/2 - 1   on [1,2]
        check F(1) = 1/2 (must equal the first piece) ✓
        check F(2) = 1   (a cdf must end at 1)        ✓
   option (b) fails both checks (F(1)=1.5, F(2)=2), so it cannot be right.
   resolution: if the exam ever shows this question, write (d) and show the F(1)/F(2)
   checks; they settle it in 20 seconds without integration. the scheme's "B" is
   either a handwriting misread (the image is low quality) or a grader's slip.
```

═══════════════════════════════════════════════════════════════════════════════
F7.5  PDF FROM CDF / FINDING THE CDF  (the paired skill)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 5 (our paper, ETE re-session S4 C1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Diameter of an electric cable say X is assumed to be a continuous random variable with
   probability distribution function f(x) = 6x(1-x), 0 <= x <= 1. Determine a number k,
   such that P(X < k) = P(X > k). Also, find its cumulative distribution function.
```

STEP 0: DECODE - TWO asks.

```
   ASK 1: find k with P(X<k) = P(X>k).  READ THIS: the split point where the area is half
          on each side. that is the MEDIAN.
   ASK 2: find the CDF, F(x).
   NOTE: the question calls f "probability distribution function" but it means DENSITY
         (it is f, not F). Read past that sloppy wording.
```

STEP 1: ASK 2 first (easier), the CDF

```
   F(x) = integral of 6t(1-t) dt from 0 to x
        = integral of (6t - 6t^2) dt
        = 3t^2 - 2t^3   evaluated from 0 to x
        = 3x^2 - 2x^3

   so F(x) = 3x^2 - 2x^3 on [0,1]
```

STEP 2: ASK 1, the median

```
   P(X<k) = P(X>k)  means  F(k) = 0.5  (also written 1 - F(k) = 0.5)

   3k^2 - 2k^3 = 0.5

   multiply by 2:  6k^2 - 4k^3 = 1
   rearrange:      4k^3 - 6k^2 + 1 = 0

   try k = 0.5:
        3(0.25) - 2(0.125) = 0.75 - 0.25 = 0.5  ✓ it works immediately

   so k = 0.5
```

WHY IT WORKS FIRST TRY (the shortcut worth knowing):
```
   f(x) = 6x(1-x) is SYMMETRIC about x = 0.5:
        f(0.5 - t) = 6(0.5-t)(0.5+t) = 6(0.25 - t^2)
        f(0.5 + t) = 6(0.5+t)(0.5-t) = 6(0.25 - t^2)   SAME
   a symmetric density has its median at the centre of symmetry.
   so k = 0.5 and the long algebra is unnecessary. SPOT THE SYMMETRY.
```

THE PICTURE:

```
   f(x)
   1.5|     ###
      |   #######
      | ####     ####
      |##           ##
      +---0----k=0.5--1---x
              |<--0.5-->|
          half the area left, half right
```

ANSWER:
```
   k = 0.5
   F(x) = 3x^2 - 2x^3 on [0,1]
```

SANITY CHECKS:
```
   F(0) = 0 - 0 = 0 ✓
   F(1) = 3 - 2 = 1 ✓
   F(0.5) = 3(0.25) - 2(0.125) = 0.75 - 0.25 = 0.5 ✓
```

TRAP:
```
   1. Not recognising P(X<k) = P(X>k) as the median condition. Draw the picture.
   2. Missing the symmetry and grinding the cubic. The cubic HAS a neat root here; test 0.5.
   3. Forgetting the CDF ask. The word "Also" is worth half.
   4. "probability distribution function" is sloppy wording for DENSITY. If they had meant
      the CDF they would not have given you f(x) as the formula to start from.
```

═══════════════════════════════════════════════════════════════════════════════
F7.6  PMF TABLE + CDF (the discrete composite)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 6 (our paper, ETE 2024-25 S4 B5)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Two dice are rolled. Let X denote the random variable which counts the total number of
   points on the upturned faces, construct a table giving the non-zero values of the
   probability mass function. Also find the distribution function of X.
```

STEP 0: DECODE

```
   ASK 1: the pmf table for X = sum of two dice (only the values with non-zero probability,
          so X = 2 through 12).
   ASK 2: the distribution function = the CDF, F(x) = P(X <= x).
```

STEP 1: THE OUTCOME SPACE (the key fact: 36 equally-likely outcomes)

```
        first die
              1    2    3    4    5    6
        +----------------------------------+
     1  |   2    3    4    5    6    7     |   each cell is a sum
     2  |   3    4    5    6    7    8     |
     3  |   4    5    6    7    8    9     |
     4  |   5    6    7    8    9   10     |
     5  |   6    7    8    9   10   11     |
     6  |   7    8    9   10   11   12     |
        +----------------------------------+
        second die

   total cells = 6 x 6 = 36, all equally likely.
```

STEP 2: COUNT HOW MANY CELLS GIVE EACH SUM

```
   sum 2:  1 cell   (1,1)
   sum 3:  2 cells  (1,2) (2,1)
   sum 4:  3 cells  (1,3) (2,2) (3,1)
   sum 5:  4
   sum 6:  5
   sum 7:  6        <- the peak, 6 cells on the diagonal-ish band
   sum 8:  5
   sum 9:  4
   sum 10: 3
   sum 11: 2
   sum 12: 1
   total: 36 ✓ (1+2+3+4+5+6+5+4+3+2+1 = 36)
```

STEP 3: THE PMF TABLE (each cell count / 36)

```
   +-----+--------+----------+
   |  x  | count  |  P(X=x)  |
   +-----+--------+----------+
   |  2  |   1    |  1/36    |
   |  3  |   2    |  2/36    |
   |  4  |   3    |  3/36    |
   |  5  |   4    |  4/36    |
   |  6  |   5    |  5/36    |
   |  7  |   6    |  6/36    |
   |  8  |   5    |  5/36    |
   |  9  |   4    |  4/36    |
   | 10  |   3    |  3/36    |
   | 11  |   2    |  2/36    |
   | 12  |   1    |  1/36    |
   +-----+--------+----------+
   sum              = 36/36 = 1 ✓
```

STEP 4: THE CDF (cumulative sum)

```
   +-----+----------+-----------------------------+
   |  x  |  P(X=x)  |  F(x) = P(X <= x)           |
   +-----+----------+-----------------------------+
   |  2  |  1/36    |  1/36                       |
   |  3  |  2/36    |  3/36                       |
   |  4  |  3/36    |  6/36                       |
   |  5  |  4/36    | 10/36                       |
   |  6  |  5/36    | 15/36                       |
   |  7  |  6/36    | 21/36  <- over half here     |
   |  8  |  5/36    | 26/36                       |
   |  9  |  4/36    | 30/36                       |
   | 10  |  3/36    | 33/36                       |
   | 11  |  2/36    | 35/36                       |
   | 12  |  1/36    | 36/36 = 1                   |
   +-----+----------+-----------------------------+
```

THE BAR CHART (see the shape):

```
   6/36 |              ##
   5/36 |           ## ## ##
   4/36 |        ## ## ## ## ##
   3/36 |     ## ## ## ## ## ## ##
   2/36 |  ## ## ## ## ## ## ## ## ##
   1/36 |## ## ## ## ## ## ## ## ## ## ##
        +2--3--4--5--6--7--8--9-10-11-12----
              triangular! peaks at 7
```

TRAP:
```
   1. Writing the pmf as 1/11 for each (treating the 11 sums as equally likely). They are
      NOT: the sum 7 is six times as likely as the sum 2. The 36-cell grid is the truth.
   2. Forgetting the CDF is CUMULATIVE. F(x) must be non-decreasing and end at 1.
   3. Off-by-one in a discrete CDF: for integer-valued X, P(a <= X <= b) = F(b) - F(a-1).
      Note the "a-1", which differs from the continuous case.
```

═══════════════════════════════════════════════════════════════════════════════
F7 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   FOUR RULES for a density: f >= 0 | total integral = 1 | area = probability | F' = f

   THE INTEGRAL YOU NEED:  integral a to b of x^n dx = [b^(n+1) - a^(n+1)]/(n+1)

   FIND-K:      integrate f over the support, set = 1, solve for k
   FIND-2-CONST: two conditions (total mass + a given moment), solve simultaneously
   CDF:         F(x) = area from the start to x.  PIECEWISE if f is piecewise; do not
                forget the accumulated area from earlier pieces.
   PDF from CDF: differentiate.
   MEDIAN:      P(X<k) = P(X>k) means F(k) = 0.5. check for symmetry first.
   DISCRETE:    pmf table (count/36 style), then cumulative for the CDF.
                P(a<=X<=b) = F(b) - F(a-1), note the a-1.

   FREE CHECKS (they eliminate MCQ decoys and catch algebra slips):
     F(lowest support value) = 0
     F(highest support value) = 1
     the pmf/cdf must be non-decreasing
     the mean must lie inside the support
     Var = E(X^2) - (E(X))^2, the second term SQUARED

   TOP TRAPS:
     not expanding brackets before integrating
     forgetting earlier pieces of a piecewise CDF
     rounding mid-calculation (use exact fractions, convert at the end)
     treating 11 dice sums as equally likely
```
