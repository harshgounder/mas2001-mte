# F5 CHEBYSHEV: every shape, every question, solved from zero

Source: our own material (MTE 2024-25 blocks A3 and B3, MTE 2025-26 block Q5, the ETE papers
E24S3, E25S3, E24S4, E25S4, and the L10-11 Chebyshev deck). Nothing invented. Every number
machine-checked (15/15 checks pass).

WHY THIS FILE IS THE MOST IMPORTANT ONE: Chebyshev appears in EVERY sitting we hold (9 of 9),
and the ETE re-sit and both MTE papers all carry it. It is the highest-frequency topic in the
course.

```
  SHAPES IN THIS FILE
  F5.1  within-k        "what fraction lies within k sigma"      1 question
  F5.2  find-c          "find c such that P(...) <= p"           1 question (MTE!)
  F5.3  inverse         "given the bound, find mean and variance" 2 questions
  F5.4  statement-MCQ   "which is/are NOT Chebyshev"             1 question (MTE!)
  F5.5  interpretation  "what is it useful for"                   1 question
  F5.6  composite       bound vs actual                          1 question (MTE!)
```

═══════════════════════════════════════════════════════════════════════════════
BEFORE ANY QUESTION: what Chebyshev is FOR (get this right and the rest follows)
═══════════════════════════════════════════════════════════════════════════════

Chebyshev bounds how much of a distribution can lie FAR from the mean, using ONLY the mean and
variance. You do not need to know the shape of the distribution.

```
   +---------------------------------------------------------------------+
   |  THE THREE FORMS (memorize all three; the questions use all three)   |
   |                                                                      |
   |   (1) tail form, in sigma units:                                     |
   |         P( |X - mu| >= k sigma )  <=  1 / k^2                        |
   |                                                                      |
   |   (2) within form, in sigma units:                                   |
   |         P( |X - mu| <  k sigma )  >=  1 - 1 / k^2                    |
   |                                                                      |
   |   (3) tail form, in RAW units (when the gap is a plain number c):    |
   |         P( |X - mu| >= c )  <=  sigma^2 / c^2                        |
   |                                                                      |
   |  mu = mean, sigma = standard deviation, sigma^2 = variance.          |
   +---------------------------------------------------------------------+
```

THE VALUE TABLE (memorize; MCQs and fill-in-the-blanks use these):

```
   +------+------------------+------------------+
   |  k   | within 1 - 1/k^2 | outside 1/k^2    |
   +------+------------------+------------------+
   |  2   | 3/4  = 0.75      | 1/4  = 0.25      |
   |  3   | 8/9  = 0.8889    | 1/9  = 0.1111    |
   |  4   | 15/16= 0.9375    | 1/16 = 0.0625    |
   |  5   | 24/25= 0.96      | 1/25 = 0.04      |
   +------+------------------+------------------+
```

THE PICTURE (why it is only a BOUND, not exact):

```
                         1/k^2  (max outside)
   |<--- 1 - 1/k^2 (min inside) --->|<--- 1/k^2 --->|
   |                                |               |
   ---------mu-k sigma-----mu-----mu+k sigma---------

   Chebyshev gives a FLOOR on the inside and a CEILING on the outside.
   It never claims the exact values, because it must be true for EVERY distribution.
   A specific distribution (like uniform) can do much better, which is why
   "bound vs actual" questions get very different numbers.
```

═══════════════════════════════════════════════════════════════════════════════
F5.1  WITHIN-K:  "what fraction lies within k sigma"
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 1 (our paper, ETE 2024-25 S3 A2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   If K = 3 in Chebyshev's inequality, what percentage of values lie within 3 standard
   deviations of the mean?
```

STEP 0: DECODE - the word "within" picks the form.

```
   "within 3 standard deviations"  ->  the WITHIN form, form (2)
   K = 3                            ->  k = 3
   "what percentage"                ->  the answer is a percentage, not a decimal
```

THE PICTURE:

```
   |<=========== what we want ===========>|
   |                                     |
   ---------mu-3sigma----mu----mu+3sigma---------

   "within 3 sd" is the shaded middle. Chebyshev says it is AT LEAST 1 - 1/9.
```

EVERY STEP:

```
  STEP 1  Write the within form: P(within k sigma) >= 1 - 1/k^2
  STEP 2  Put in k = 3: 1 - 1/3^2 = 1 - 1/9
  STEP 3  1/9 = 0.1111
          so 1 - 0.1111 = 0.8889
  STEP 4  convert to a percentage: 88.89 percent
```

ANSWER: at least 88.89 percent.

TRAP:
```
   1. THE CLASSIC: computing 1/k^2 = 1/9 = 11.11 percent and reporting that. The question
      says WITHIN, so it is 1 - 1/k^2. The 11.11 percent answer is "outside 3 sigma".
      ALWAYS re-read whether it is within or outside before writing.
   2. Reporting 0.8889 when asked for a percentage (or vice versa). Read the ask.
```

MUTATIONS:
```
   IF "within 2 sigma"   THEN 1 - 1/4 = 3/4 = 75 percent.
   IF "outside 3 sigma"  THEN 1/9 = 11.11 percent.
   IF "at least k sigma away" THEN the tail, 1/k^2.
```

═══════════════════════════════════════════════════════════════════════════════
F5.2  FIND-C:  "find c such that P(|X-mu| >= c) <= p"
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 2 (MTE 2025-26 paper, block Q5 - the real thing)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A random variable X has mean = 10 and variance = 4. Using Chebyshev's inequality,
   find the value of the constant c such that P(|X - 10| >= c) <= 0.04.
```

STEP 0: DECODE - the gap is in RAW units (c), not in sigma units, so use form (3).

```
   mean = 10, variance = 4  ->  sigma^2 = 4, sigma = 2
   |X - 10| >= c            ->  the gap is c, a plain number (NOT c times sigma)
   "<= 0.04"                ->  the target ceiling
   => use form (3):  P(|X - mu| >= c) <= sigma^2 / c^2
```

THE DECISION TREE that picks the form (this is the whole skill):

```
   look at the right side of the |...|:
   |
   +-- is it "k sigma" (k times the sd)?   -> FORM 1 (1/k^2)
   |     e.g. P(|X-mu| >= 2 sigma)
   |
   +-- is it a bare number c?               -> FORM 3 (sigma^2 / c^2)
         e.g. P(|X-mu| >= c)   <- THIS QUESTION
```

EVERY STEP:

```
  STEP 1  sigma^2 = 4
  STEP 2  Chebyshev form 3: P(|X - 10| >= c) <= 4 / c^2
  STEP 3  We want the ceiling to be 0.04:
          4 / c^2 = 0.04
  STEP 4  multiply both sides by c^2:
          4 = 0.04 c^2
  STEP 5  divide both sides by 0.04:
          c^2 = 4 / 0.04 = 100
  STEP 6  take the square root:
          c = sqrt(100) = 10
```

ANSWER: c = 10.

THE SANITY CHECK (always do this on a find-c question):

```
   c = 10 means "the gap is 10 units". The sd is 2, so c = 10 = 5 sigma.
   the tail bound for 5 sigma is 1/5^2 = 0.04 ✓ matches the target.

   so the c-question is secretly a k-question: c = k sigma = 5 x 2 = 10.
   either route gives the same answer. use whichever is clearer to you.
```

TRAP:
```
   1. Using form 1 (with k sigma) when the question gives a bare c. Mixing forms is the
      number one error here.
   2. Using sigma = 4 instead of sigma^2 = 4. The question says "variance = 4", and
      variance IS sigma^2, so it goes straight into the numerator. Do not square it again.
   3. Forgetting the square root at the end: answering c = 100.
   4. Sign errors: c^2 = 100 has roots +10 and -10, but a distance cannot be negative, so
      take +10.
```

═══════════════════════════════════════════════════════════════════════════════
F5.3  INVERSE:  "given the bound, find mean and variance"
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 3 (our paper, ETE 2024-25 S3 B1 - the 21/25 case)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   If the Chebyshev's inequality for the random variable X is given by
   P(-2 < X < 8) >= 21/25,  find E(X) and Var(X).
```

STEP 0: DECODE - the interval holds two hidden pieces of information.

```
   P(-2 < X < 8) is an interval. Chebyshev always talks about a SYMMETRIC interval
   around the mean. So:
        - the CENTRE of (-2, 8) is the mean
        - the HALF-WIDTH of (-2, 8) is k times sigma
   ">= 21/25" is the WITHIN form, so 1 - 1/k^2 = 21/25.
```

THE PICTURE (this is the whole trick, drawn):

```
   -2                 ?                 8
    |-----------------|-----------------|
                 the centre
    |<----- 5 ------>| k sigma
    |<----------- 5 ---------->|

   centre = (-2 + 8)/2 = 3   ->  E(X) = 3
   half-width = 8 - 3 = 5    ->  k sigma = 5
```

EVERY STEP:

```
  STEP 1  Find the centre (the mean):
          E(X) = (-2 + 8) / 2 = 6 / 2 = 3

  STEP 2  Find the half-width:
          half-width = 8 - 3 = 5       (equivalently 3 - (-2) = 5)
          so k sigma = 5

  STEP 3  Use the within bound to find k:
          1 - 1/k^2 = 21/25
  STEP 4  rearrange:
          1/k^2 = 1 - 21/25 = 4/25
  STEP 5  flip:
          k^2 = 25/4
          k = sqrt(25/4) = 5/2 = 2.5

  STEP 6  From step 2, k sigma = 5, so:
          sigma = 5 / k = 5 / 2.5 = 2

  STEP 7  Variance = sigma^2 = 2^2 = 4
```

ANSWER: E(X) = 3, Var(X) = 4.

A FASTER ROUTE (worth knowing, same answer):

```
   Chebyshev in raw units says P(|X-mu| < c) >= 1 - sigma^2/c^2
   here c = half-width = 5, and the bound is 21/25:
        1 - sigma^2/25 = 21/25
        sigma^2/25 = 4/25
        sigma^2 = 4
   so the variance is 4 immediately, in one step.
```

TRAP:
```
   1. Not seeing that the midpoint IS the mean. Without that step the question is
      unsolvable, and students freeze here. Draw the number line.
   2. Mismatching the form: using 1/k^2 = 21/25 would give k^2 = 25/21, k = 1.09, which is
      not a sensible k for this context (and gives sigma = 5/1.09 = 4.58, then Var = 21.
      wrong). The 21/25 is a WITHIN number because the interval form P(a<X<b) is "within".
   3. Stopping at sigma instead of squaring. The ask is Var(X) or "variance", so square it.
      (if the ask were "standard deviation", do NOT square.)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 4 (our paper, ETE 2024-25 S4 B3 - the same shape with different numbers)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   If the Chebyshev's inequality for the random variable X is given by
   P(4 < X < 16) >= 24/25,  find E(X) and Var(X).
```

EVERY STEP:

```
  STEP 1  centre = (4 + 16)/2 = 20/2 = 10  ->  E(X) = 10
  STEP 2  half-width = 16 - 10 = 6         ->  k sigma = 6
  STEP 3  within bound: 1 - 1/k^2 = 24/25
  STEP 4  1/k^2 = 1/25  ->  k^2 = 25  ->  k = 5
  STEP 5  sigma = 6 / 5 = 1.2
  STEP 6  Variance = 1.2^2 = 1.44
```

ANSWER: E(X) = 10, Var(X) = 1.44.

TRAP: same as Q3. The numbers changed, the shape did not. If you can do Q3, you can do this.
THIS IS THE MUTATION PATTERN IN ACTION: the paper took the 21/25 skeleton and swapped in
24/25 with a different interval. Learn the SHAPE, and every version is free.

═══════════════════════════════════════════════════════════════════════════════
F5.4  STATEMENT MCQ:  "which is/are NOT Chebyshev"
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 5 (MTE 2024-25 paper, block A3 - the real thing)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   If X is a random variable with mean mu and variance sigma^2 and K is any positive
   number, then which of the following is/are NOT the Chebyshev's inequality?
   a) P{|X - mu| >= k sigma} <= 1/k^2
   b) P{|X - mu| <  k sigma} >= 1 - (1/k^2)
   c) P{|X - mu| >= k} <= k^2/sigma^2
   d) P{|X - mu| <  k sigma} >= sigma^2/k^2
```

STEP 0: DECODE - "NOT" is the whole question. Read all four, check each against the three
known forms.

THE METHOD (a checklist per option):

```
   for each option ask:
     Q1: is the left side |X - mu| (correct structure)?
     Q2: is the direction right (>= pairs with <=, and < pairs with >=)?
     Q3: is the right side the right FORMULA for that direction?
         tail (>=)  -> 1/k^2          (or sigma^2/c^2 in raw units)
         within (<) -> 1 - 1/k^2
```

CHECK EACH:

```
   OPTION (a)  P(|X-mu| >= k sigma) <= 1/k^2
     structure: |X-mu| ok.  direction: >= with <= ok.
     formula: 1/k^2 ok.
     -> IS a correct Chebyshev form (the standard tail form). not an answer.

   OPTION (b)  P(|X-mu| < k sigma) >= 1 - 1/k^2
     structure ok.  direction: < with >= ok.
     formula: 1 - 1/k^2 ok.
     -> IS correct (the standard within form). not an answer.

   OPTION (c)  P(|X-mu| >= k) <= k^2/sigma^2
     structure ok.  direction ok.
     formula: k^2/sigma^2.  WRONG.
       the raw-unit tail form is sigma^2/k^2, NOT k^2/sigma^2. it is INVERTED.
       (check the logic: a bigger gap k should make the probability SMALLER. k^2/sigma^2
        GROWS with k, which is backwards. sigma^2/k^2 shrinks with k, which is right.)
     -> NOT Chebyshev.  <-- one of the answers

   OPTION (d)  P(|X-mu| < k sigma) >= sigma^2/k^2
     structure ok.  direction ok.
     formula: sigma^2/k^2. WRONG for the WITHIN direction.
       the within form is 1 - 1/k^2. the tail form is 1/k^2. sigma^2/k^2 is neither
       (it is the raw-unit tail denominator, misused).
       also check: sigma^2/k^2 can exceed 1 when k is small (e.g. k=0.5 gives 4 sigma^2),
        and a probability bound above 1 is meaningless. that alone rules it out.
     -> NOT Chebyshev.  <-- one of the answers
```

ANSWER: options (c) and (d) are NOT Chebyshev's inequality.

TRAP:
```
   1. The word "NOT". Many students check the correct forms, find (a) and (b) correct, and
      then report (a)(b) as the answer. RE-READ the ask. It wants the FALSE ones.
   2. Not having the forms memorized exactly, then guessing. You need: >= pairs with 1/k^2,
      < pairs with 1 - 1/k^2. Memorize the PAIRINGS.
   3. Missing the inverted fraction in (c). k^2/sigma^2 vs sigma^2/k^2 is a one-glance check
      once you know the correct one.
```

═══════════════════════════════════════════════════════════════════════════════
F5.5  INTERPRETATION MCQ:  "what is it useful for"
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 6 (our paper, ETE 2025-26 S4 A3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Chebyshev's inequality is useful for:
   a. Exact probability    b. Bounding probability
   c. Mean calculation     d. Variance zero
```

DECODE: recalling the PURPOSE. Chebyshev never gives an exact answer; it gives limits.

ANSWER: (b) Bounding probability.

WHY (the one line worth remembering):
```
   Chebyshev works for ANY distribution, using only the mean and variance. That generality
   is bought at a price: it can only BOUND, never pin down, the probability. If you need an
   exact answer you must know the distribution (normal table, binomial formula, etc).
```

TRAP: choosing (a) "exact probability". That is exactly what Chebyshev cannot give, and it is
the standard decoy.

═══════════════════════════════════════════════════════════════════════════════
F5.6  COMPOSITE:  bound vs actual
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 7 (MTE 2024-25 paper, block B3 - the real thing; also see F4.4)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Let X be uniformly distributed U(-1, 1). Compute the upper bound on probability
   P[ |X - E(X)| >= 2 sqrt(Var(X)) ] using Chebyshev's inequality.
   Also, obtain the actual probability.
```

STEP 0: DECODE - TWO asks. The word "Also" marks the second one and it is worth half.

```
   ASK 1: the BOUND (Chebyshev, always workable)
   ASK 2: the ACTUAL (needs the specific distribution, here uniform)
```

EVERY STEP:

```
  STEP 1  Ingredients of U(-1,1):
          E(X) = (a+b)/2 = (-1+1)/2 = 0
          Var(X) = (b-a)^2/12 = (2)^2/12 = 1/3
          so sqrt(Var(X)) = sqrt(1/3) = 0.5774

  STEP 2  Rewrite what the probability asks:
          P( |X - 0| >= 2 x 0.5774 )
          = P( |X| >= 1.1547 )

  STEP 3  THE BOUND: this is the k-sigma form with k = 2
          P(|X - mu| >= k sigma) <= 1/k^2 = 1/4 = 0.25

  STEP 4  THE ACTUAL: read the support of X.
          X lives in [-1, 1], so |X| <= 1 always.
          we need |X| >= 1.1547, which is BEYOND what X can reach.
          therefore no value of X qualifies:
          actual probability = 0
```

ANSWER:
```
   bound  = 0.25
   actual = 0
   and 0 <= 0.25, so the bound holds (it is loose here, which is expected).
```

THE COMPARISON PICTURE:

```
   bound:  0.25 |###################|
   actual: 0.00 |
   the bound says "at most 25 percent", the truth is "none". safe but crude.
```

TRAP:
```
   1. Skipping the actual. "Also" is half the marks.
   2. Trying to integrate for the actual. LOOK at the support: the threshold 1.1547 exceeds
      the maximum 1, so the answer is 0 by inspection. Reading first saves the whole
      calculation.
   3. Comparing 2 against Var = 1/3 directly instead of 2 x sqrt(Var) = 1.1547.
```

═══════════════════════════════════════════════════════════════════════════════
F5 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   THREE FORMS:
     tail  (>= k sigma):  <= 1/k^2
     within(<  k sigma):  >= 1 - 1/k^2
     raw   (>= c):        <= sigma^2 / c^2

   TABLE: k=2 -> 3/4 ; k=3 -> 8/9 ; k=4 -> 15/16 ; k=5 -> 24/25

   THE SKILL: look at the right of the |X-mu|.
     "k sigma" -> form 1 ; a bare number c -> form 3 ; "within" -> form 2.
     c = k sigma connects forms 1 and 3.

   INVERSE (given the interval):
     centre = mean ; half-width = k sigma ; match to 1 - 1/k^2 (if within).

   MCQ CHECKLIST: structure |X-mu| ok? direction pairing ok? formula the right one?
     >= with <= ;  < with >= ; tail=1/k^2 ; within=1-1/k^2.
     and remember to read "NOT" if the question says NOT.

   BOUND vs ACTUAL:
     answer BOTH. the bound from Chebyshev, the actual from the distribution (or by reading
     the support, which is often all that is needed).

   WHY IT MATTERS: Chebyshev is in EVERY sitting we hold. this is the single highest-value
   topic in the course.

   TOP TRAPS:
     within vs outside (the 8/9 vs 1/9 fork)             <- the most common single error
     using form 1 when a bare c is given (or vice versa)
     not seeing the interval midpoint is the mean
     answering only the bound on a bound-vs-actual question
     missing the "NOT" in a statement MCQ
```
