# THEORY CHEATSHEET: everything in the MTE, explained

Built 17 Sep 2026. This is the whole theory of the mid-term in one file: every topic, every
formula with its meaning, every definition, every trap. No questions, no drills, just the
theory and how to read it. Every number that appears here was verified in the notes/worked
files before being written down.

Scope: lectures 1 to 21 (per ~/PS/syllabus.txt). Hypothesis testing and estimation methods
beyond the "good estimator" block are OUT of MTE scope; the one estimation block that IS in
scope (the four properties) is fully covered in section 12.

```
  THE TWELVE BLOCKS (this file's table of contents)
  ┌──────────────────────────────────────────────────────────────────────┐
  │  1  Probability foundations       the words, the rules, conditional  │
  │  2  Random variables              the function definition            │
  │  3  PMF, PDF, CDF                 the three letter functions         │
  │  4  Expectation and variance      E(X), Var(X), the laws             │
  │  5  Chebyshev's inequality        bounds without a distribution      │
  │  6  Binomial distribution         n trials, p constant               │
  │  7  Poisson distribution          rare events, mean = variance       │
  │  8  Uniform distribution          flat density, wait stories         │
  │  9  Normal distribution           the bell, the table, the traps     │
  │ 10  Exponential distribution      waiting times, memoryless          │
  │ 11  Sampling, SE, CLT             xbar and its spread                │
  │ 12  Theory of estimation          the four properties of estimators  │
  └──────────────────────────────────────────────────────────────────────┘
```

═══════════════════════════════════════════════════════════════════════════════
1. PROBABILITY FOUNDATIONS
═══════════════════════════════════════════════════════════════════════════════

1.1 THE FOUR VOCABULARY WORDS

```
  ┌──────────────────┬────────────────────────────────────────────────────┐
  │ experiment       │ any process with an uncertain outcome               │
  │                  │ (tossing a coin, rolling a die)                     │
  ├──────────────────┼────────────────────────────────────────────────────┤
  │ outcome          │ ONE possible result (H, or a 4 on the die)          │
  ├──────────────────┼────────────────────────────────────────────────────┤
  │ sample space (S) │ the set of ALL possible outcomes                    │
  ├──────────────────┼────────────────────────────────────────────────────┤
  │ event            │ a subset of S, a collection of outcomes             │
  └──────────────────┴────────────────────────────────────────────────────┘

  The four sample spaces the course uses constantly:
     one coin        S = {H, T}                     2 outcomes
     one die         S = {1,2,3,4,5,6}             6 outcomes
     two coins       S = {HH, HT, TH, TT}          4 outcomes   (order matters!)
     two dice        S = 36 ordered pairs         36 outcomes
```

1.2 SET ALGEBRA ON EVENTS

```
  A u B  (A OR B)          everything in either event
  A n B  (A AND B)         only the overlap
  A'     (not A)           everything in S but outside A
  disjoint / mutually exclusive:  A n B = empty (share nothing)

  THE PICTURE (the whole addition rule in one drawing):
       +---- A ----+--+---- B ----+
       |           |XX|            |     when adding P(A)+P(B),
       |           |XX|            |     the XX overlap is counted
       +-----------+--+------------+     TWICE, so subtract it once
                   ^
              the overlap A n B
```

1.3 THE AXIOMS (everything else is derived)

```
  (1)  P(S) = 1                    the whole space, probability one
  (2)  P(A) >= 0                   nothing negative
  (3)  disjoint A1, A2, ...:  P(A1 u A2 u ...) = P(A1) + P(A2) + ...
```

1.4 THE WORKING RULES

```
  ┌─────────────────────────────────────────────┬────────────────────────────┐
  │ complement      P(A') = 1 - P(A)            │ "not" flips to one minus   │
  │ addition        P(AuB) = P(A)+P(B)-P(AnB)   │ "or" counts overlap once   │
  │ mutually excl.  P(AuB) = P(A)+P(B)          │ overlap is zero            │
  │ multiplication  P(AnB) = P(A) x P(B|A)      │ "and" needs the given form │
  │ independent     P(AnB) = P(A) x P(B)        │ the given form disappears  │
  └─────────────────────────────────────────────┴────────────────────────────┘
```

1.5 MUTUALLY EXCLUSIVE vs INDEPENDENT (the classic swap)

```
  ┌────────────────────┬─────────────────────────┬─────────────────────────┐
  │                    │ MUTUALLY EXCLUSIVE      │ INDEPENDENT             │
  ├────────────────────┼─────────────────────────┼─────────────────────────┤
  │ meaning            │ cannot BOTH happen      │ one does not change the │
  │                    │                         │ other's probability     │
  │ the test           │ P(A n B) = 0            │ P(A n B) = P(A) x P(B)  │
  │ example            │ even vs odd on a die    │ coin and die together   │
  └────────────────────┴─────────────────────────┴─────────────────────────┘

  THE FACT THAT ENDS MCQ ARGUMENTS:
     two events with nonzero probability CANNOT be both.
     if P(AnB)=0 then P(A)P(B) > 0, so the independence test fails.
```

1.6 CONDITIONAL PROBABILITY ("given that")

```
                 P(A n B)
     P(A|B)  =  -----------        the chance of A, knowing B happened
                   P(B)

  WHY it shrinks the world: "given B" replaces S with B alone. The picture:

     original S                        after "given B"
     +---------+----+                  +----+
     |    A    |    |                  |A in|
     |      +--+--+ |                  | +--+   the denominator becomes P(B),
     |      |AnB| | |                  | |  |   the numerator stays P(AnB)
     +------+--+--+ |                  +-+--+
     |         B   |                     B
     +-------------+

  THE DEFINITION OF INDEPENDENCE, in conditional language:
     A, B independent  <=>  P(A|B) = P(A)     (B gives no information about A)
```

1.7 COUNTING (how you size up S)

```
  multiplication principle:   choices multiply   6 faces x 6 faces = 36 pairs
  factorial:                  n! = n x (n-1) x ... x 1     3! = 6
  combinations:               C(n,r) = n! / (r!(n-r)!)     how many groups of r
                                                           from n, order ignored
  THE STANDARD COUNTS:
     two dice pairs          36
     two coins outcomes       4
     hands from 52 cards      C(52,5) = 2,598,960
```

═══════════════════════════════════════════════════════════════════════════════
2. RANDOM VARIABLES
═══════════════════════════════════════════════════════════════════════════════

2.1 THE DEFINITION (verbatim, and every word decoded)

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │  A random variable is a FUNCTION whose DOMAIN is the sample space S  │
  │  and whose RANGE is the set of real numbers.                         │
  └──────────────────────────────────────────────────────────────────────┘

     DOMAIN  = what you feed in        -> outcomes
     RANGE   = what comes out          -> numbers
     FUNCTION= each outcome gets EXACTLY ONE number

  THE PICTURE:
       sample space S                 the real line
      +--------------+               +----------------+
      |   H     T    |   --- X --->  |   1      0     |
      +--------------+               +----------------+
        (outcomes)                     (numbers)

  THE FOUR MCQ KILLERS (seen in three papers):
     a constant value                  WRONG (a constant takes one value)
     a probability                     WRONG (the rv is what probabilities attach to)
     an event                          WRONG (an event is a subset, left side of the
                                        arrow; the rv crosses to numbers)
     real numbers -> sample space      WRONG (DIRECTION reversed)
```

2.2 DISCRETE vs CONTINUOUS

```
  ┌────────────────────────────────┬───────────────────────────────────────┐
  │ DISCRETE                       │ CONTINUOUS                            │
  │ values are finite or countable │ values fill an interval               │
  │ (you can list them)            │ (between any two, more values)        │
  ├────────────────────────────────┼───────────────────────────────────────┤
  │ number of heads, number of     │ time, height, temperature, rainfall,  │
  │ defects, dice sums, counts     │ lifetimes, measurements               │
  └────────────────────────────────┴───────────────────────────────────────┘

  THE LIST TEST: can you write the values 1st, 2nd, 3rd...? discrete. no? continuous.

  CONTINUOUS EXACT VALUES HAVE PROBABILITY ZERO:
     P(X = x) = 0 for any single point (an area of zero width)
     so P(a < X < b) = P(a <= X <= b)    the endpoints never matter
     (for DISCRETE variables they do matter: P(X<=2) counts the 2, P(X<2) does not)
```

2.3 SUPPORT (where the variable is allowed to live)

```
  the support is the set of values with positive probability.
  READ IT OFF THE STORY OR THE DENSITY FIRST: it sets every sum and every integral limit.
     "sum of two dice"        support {2,...,12}
     lifetime questions       support x > 0
     "between 0 and 4"        support (0,4)
     U(-1,1)                  support [-1,1]
```

═══════════════════════════════════════════════════════════════════════════════
3. PMF, PDF, CDF (the three functions and how they connect)
═══════════════════════════════════════════════════════════════════════════════

3.1 THE PMF (discrete)

```
  definition:   p(x) = P(X = x)          "the probability of exactly x"
  the two rules:
     (1) p(x) >= 0 for every x
     (2) SUM of p(x) over all values = 1        <- the self-check on every question
  forms:  a TABLE  |  a FORMULA  |  a stick graph
```

3.2 THE PDF (continuous)

```
  definition: the density f(x). probability comes from AREA under f.
     P(a < X < b) = integral from a to b of f(x) dx
  the two rules:
     (1) f(x) >= 0
     (2) integral from -inf to +inf of f(x) dx = 1     <- same self-check
  IMPORTANT: f(x) is NOT a probability. It can exceed 1 for narrow intervals.
  only the AREA is a probability.

  THE AREA PICTURE:
       f(x)
        |     ###
        |   #######
        | ##########
        +--a###b-------> x
           \____/
           this area IS P(a<X<b)
```

3.3 THE CDF (both kinds)

```
  definition:   F(x) = P(X <= x)        the RUNNING TOTAL up to x
  the four facts (each is a possible MCQ):
     (1) 0 <= F(x) <= 1                 it is a probability
     (2) F is NON-DECREASING            it can only stay flat or grow
     (3) F(x) -> 0 as x -> -inf
     (4) F(x) -> 1 as x -> +inf

  DISCRETE cdf:     F(x) = SUM of p(y) for all y <= x     (a staircase)
  CONTINUOUS cdf:   F(x) = INTEGRAL from -inf to x of f   (a smooth climb)

  THE STEP PICTURE (discrete):
       F(x)
       1 |              ____
         |        _____|
     0.5 |  _____|
         |_|
       0 +--+--+--+--+------> x
          0  1  2  3
       jumps happen AT the values; flat between them.
```

3.4 GETTING ONE FROM THE OTHER (the conversions)

```
  discrete:     p(x) = F(x) - F(x-1)          differences give the jumps back
  continuous:   f(x) = F'(x)                  differentiate the cdf
                F(x) = integral of f          integrate the pdf
  THE KEY THEOREM (used everywhere):
     P(a < X <= b) = F(b) - F(a)
     subtract two running totals; the interval is what remains.
```

3.5 THE FIND-K DRILL (normalising a density)

```
  when a density has an unknown constant k:
     set the total integral equal to 1 and solve.
        integral of k g(x) dx = 1   ->  k = 1 / (integral of g)
  same idea for discrete tables: sum the k-terms, set equal to 1, solve.
  if the table has k AND k^2 terms, that is a QUADRATIC in k:
     keep the POSITIVE root. a probability constant can never be negative.
```

═══════════════════════════════════════════════════════════════════════════════
4. EXPECTATION AND VARIANCE
═══════════════════════════════════════════════════════════════════════════════

4.1 EXPECTATION (the weighted average)

```
  discrete:     E(X) = SUM of x p(x)
  continuous:   E(X) = INTEGRAL of x f(x) dx
  the meaning: the long-run average of X, the balance point of the distribution.

  FUNCTION OF X (you rarely need the distribution of g(X) itself):
     E[g(X)] = SUM of g(x) p(x)     (or the integral, continuous)
```

4.2 THE LAWS OF EXPECTATION (memorize all four)

```
  ┌──────────────────────────────────────────┬────────────────────────────────┐
  │ E(aX + b) = a E(X) + b                   │ constants come out; b does not │
  │ E(X + Y) = E(X) + E(Y)                   │ always true, no independence   │
  │ E(X - Y) = E(X) - E(Y)                   │ minus stays minus              │
  │ E(XY) = E(X) E(Y)  IF independent        │ independence needed for        │
  │                                          │ the PRODUCT only               │
  └──────────────────────────────────────────┴────────────────────────────────┘
```

4.3 VARIANCE (the spread)

```
  definition:   Var(X) = E[(X - mu)^2]        average squared distance from the mean
  THE COMPUTATIONAL FORM (the one you actually use):
     Var(X) = E(X^2) - [E(X)]^2
  sd(X) = sqrt(Var(X))                        the same units as X

  HOW TO COMPUTE E(X^2): exactly like E(X), but square each value first:
     E(X^2) = SUM of x^2 p(x)      (or the integral with x^2)
```

4.4 THE VARIANCE LAWS (and the plus-sign surprise)

```
  ┌──────────────────────────────────────────────┬─────────────────────────────┐
  │ Var(aX + b) = a^2 Var(X)                     │ the constant b VANISHES;    │
  │                                              │ the multiplier gets SQUARED │
  │ Var(X + Y) = Var(X) + Var(Y)  IF independent │ spreads ADD                 │
  │ Var(X - Y) = Var(X) + Var(Y)  IF independent │ a DIFFERENCE also ADDS      │
  └──────────────────────────────────────────────┴─────────────────────────────┘

  THE TRAP IN BIG LETTERS: Var(X - Y) is Var(X) + Var(Y), never a minus.
  the picture: two independent sources of wobble both add wobble, whether you
  combine them by adding or subtracting the variables.

  WARNING: E(XY) = E(X)E(Y) needs independence. Var(X+Y) = Var(X)+Var(Y) also
  needs independence. E(X+Y) = E(X)+E(Y) does NOT. Do not mix the rows up.
```

4.5 THE SCALING RECIPE (for Y = aX + b)

```
  given E(X) and Var(X), for Y = aX + b:
     E(Y)    = a E(X) + b
     Var(Y)  = a^2 Var(X)
     sd(Y)   = |a| sd(X)
  example (the MTE A1 question): X ~ Poisson mean 0.5, Y = 2X:
     E(Y) = 2(0.5) = 1 ;  Var(Y) = 4 x 0.5 = 2    (NOT 4, and NOT 0.5x4 by luck)
```

═══════════════════════════════════════════════════════════════════════════════
5. CHEBYSHEV'S INEQUALITY (bounds with no distribution named)
═══════════════════════════════════════════════════════════════════════════════

5.1 THE THEORY

```
  For ANY random variable with finite mean mu and finite variance sigma^2:

     (1) tail form, sigma units:    P(|X - mu| >= k sigma) <= 1/k^2
     (2) within form:               P(|X - mu| <  k sigma) >= 1 - 1/k^2
     (3) tail form, raw units:      P(|X - mu| >= c) <= sigma^2 / c^2

  WHAT IT IS FOR: bounding how much probability can sit far from the mean using
  ONLY the mean and variance. No shape, no distribution name needed.
  WHY IT MATTERS: it is the only inequality in the course, and it appears in
  EVERY sitting examined so far.

  THE GEOMETRY:
       f(x)
        |      #####
        |   ###########
        | #################
        +---[=== mu ===]------> x
            |<-- k sigma -->|
            this middle chunk holds AT LEAST 1 - 1/k^2 of the probability
```

5.2 THE THRESHOLD TABLE (memorize)

```
  ┌─────┬──────────────────┬──────────────────┐
  │  k  │ within: 1 - 1/k^2│ outside: 1/k^2   │
  ├─────┼──────────────────┼──────────────────┤
  │  2  │ 3/4  = 0.75      │ 1/4  = 0.25      │
  │  3  │ 8/9  = 0.8889    │ 1/9  = 0.1111    │
  │  4  │ 15/16= 0.9375    │ 1/16 = 0.0625    │
  │  5  │ 24/25= 0.96      │ 1/25 = 0.04      │
  └─────┴──────────────────┴──────────────────┘
```

5.3 THE K-EXTRACTION RECIPE (any form of question)

```
  STEP 1  find mu and sigma^2 from the question (or from E(X), E(X^2))
  STEP 2  look at the right side of the bar:  "k sigma" -> form (1)/(2)
                                              a bare number c -> form (3)
  STEP 3  match the direction:  "at least k sigma away"  -> the 1/k^2 side
                                "within k sigma"          -> the 1 - 1/k^2 side
  STEP 4  solve for the unknown (k, c, mu, sigma whatever the ask is)
  STEP 5  sanity-check: a probability bound must land in [0,1]

  THE INVERSE FORM (given the bound, find the interval): work backwards.
     P(-2 < X < 8) >= 21/25 means: centre = (-2+8)/2 = 3 = mu ; half-width = 5
     1 - 1/k^2 = 21/25  ->  1/k^2 = 4/25  ->  k = 2.5  ->  sigma = 5/2.5 = 2
```

5.4 THE STATEMENT MCQs

```
  the exam asks "which of the following is NOT Chebyshev?".
  read each option against the three forms:
     >= pairs with 1/k^2        (tail)
     <  pairs with 1 - 1/k^2    (within)
     raw-c tail uses sigma^2/c^2, NOT c^2/sigma^2 (the inverted fraction is the decoy)
  also: the bound is a BOUND, not the exact probability. "exact probability" is
  the classic wrong description. Chebyshev only bounds.
```

═══════════════════════════════════════════════════════════════════════════════
6. BINOMIAL DISTRIBUTION
═══════════════════════════════════════════════════════════════════════════════

6.1 THE SETUP (all four conditions must hold)

```
  (1) n INDEPENDENT trials
  (2) each trial has exactly TWO outcomes (success / failure)
  (3) p is the SAME on every trial
  (4) X counts the SUCCESSES
  then   X ~ Binomial(n, p),   q = 1 - p
  the single trial is the Bernoulli; binomial = n Bernoullis stacked.
```

6.2 THE FORMULA

```
  pmf:    P(X = x) = C(n,x) p^x q^(n-x)        x = 0, 1, ..., n
  the three factors decoded:
     C(n,x)   how many orders the x successes can occur in
     p^x      the x successes, one factor each
     q^(n-x)  the remaining failures
```

6.3 MOMENTS

```
  mean:      E(X) = np
  variance:  Var(X) = npq          sd = sqrt(npq)
  the shape: rises to a peak near np, symmetric when p = 0.5.
```

6.4 THE ASK-SHAPES (each maps to one line of method)

```
  ┌──────────────────────────────┬───────────────────────────────────────────┐
  │ "exactly k"                  │ one term: C(n,k) p^k q^(n-k)              │
  │ "at least k"                 │ 1 - P(X <= k-1)   (complement, faster)    │
  │ "at most k"                  │ P(0)+...+P(k)     (direct sum)            │
  │ "how many groups expected"   │ the probability x the number of groups    │
  │ "find n or p from clues"     │ equations: np = mean, npq = variance, or  │
  │                              │ a ratio condition like P(1)=P(2)          │
  └──────────────────────────────┴───────────────────────────────────────────┘

  THE RATIO CLUE PATTERN (both MTE papers use it in some form):
     P(X=1) = P(X=2) expands and cancels, leaving  q = (n-1)p/2  or similar.
     always divide out the common factors BEFORE expanding factorials.
```

6.5 THE COUNT LAYER (the hidden ask)

```
  when the question says "how many families would you expect", there are TWO layers:
     layer 1: the probability for ONE group  (use the binomial)
     layer 2: multiply by the number of groups
  "find the probability" stops at layer 1. "how many" and "the number expected"
  go to layer 2. One missing multiplication loses the whole question.
```

6.6 BINOMIAL vs POISSON (when to switch)

```
  np small (rule of thumb np < 5 to 10) and n large?  Poisson approximation:
     Binomial(n,p)  ~  Poisson(lambda = np)
  the Poisson then does the arithmetic with e^-lambda instead of huge powers.
```

═══════════════════════════════════════════════════════════════════════════════
7. POISSON DISTRIBUTION
═══════════════════════════════════════════════════════════════════════════════

7.1 WHAT IT MODELS

```
  the NUMBER of events in a fixed interval (time, space, area, volume) when
  events happen independently at a constant average rate.
  examples from our material: phone calls per minute, defects per page,
  accidents per day, customers per hour.
```

7.2 THE FORMULA

```
                e^(-lambda) lambda^x
     P(X = x) = -------------------          x = 0, 1, 2, ...
                       x!

  lambda = the average count in the interval (the rate x the window length)
```

7.3 THE SIGNATURE (the MCQ bait)

```
  ┌───────────────────────────────────────────────────────────────┐
  │           MEAN = LAMBDA  and  VARIANCE = LAMBDA               │
  │           mean = variance is the Poisson identity             │
  └───────────────────────────────────────────────────────────────┘
  among the named families, it is the one whose mean and variance
  formulas are identical. (an observed numerical equality alone is not
  proof; use the stated model or formula.)
```

7.4 RATE AND WINDOW SCALING

```
  lambda must match the window in the question.
     "2 calls per minute, in a 5-minute interval"  ->  lambda = 10
     "15 per hour, in 20 minutes"                  ->  lambda = 15 x (1/3) = 5
  THE SCALING PICTURE:
       rate:  2 per minute
       ----------+----------+----------+----------+----------+
                 1 min      2 min      3 min      4 min      5 min
       lambda:    2          4          6          8         10
```

7.5 THE RECOVERY PATTERN (find lambda from a stated relation)

```
  given a relation between probabilities, write both sides with the formula,
  then DIVIDE OUT the common factors:
     P(X=1) = 0.2 P(X=2):   e^-l l   = 0.2 e^-l l^2/2
       cancel e^-l and one l:      1 = 0.1 l      ->  l = 10
     P(X=2) = 9 P(X=4) + 90 P(X=6):  divide by e^-l l^2/2 through:
       1 = 3l^2/4 + l^4/4   ->  l^4 + 3l^2 - 4 = 0  ->  l^2 = 1  ->  l = 1
  NEVER expand e^-l or try to take logs before cancelling.
```

7.6 COMBINING AND NESTING

```
  X ~ Poi(l1), Y ~ Poi(l2), independent  ->  X + Y ~ Poi(l1 + l2)
  the composite (both MTE papers use a version):
     stage 1: a Poisson gives a COUNT (say, calls in 5 minutes = 10 by expectation)
     stage 2: that count becomes the n (or the story becomes binomial)
  read the second stage carefully; the word "of" or "then" marks the switch.
```

═══════════════════════════════════════════════════════════════════════════════
8. UNIFORM DISTRIBUTION (continuous)
═══════════════════════════════════════════════════════════════════════════════

8.1 THE DENSITY (a flat rectangle)

```
  X ~ U(a, b):   f(x) = 1/(b - a)   for a <= x <= b,  0 outside

       f(x)
        1/(b-a) |====================|
                |                    |
                +----a---------b-----+---> x
  the rectangle has area 1:  width (b-a) x height 1/(b-a) = 1.
```

8.2 PROBABILITIES ARE LENGTH RATIOS

```
  P(c < X < d) = (d - c) / (b - a)     the sub-length over the whole length
  CLIPPING (the exam favorite): if the interval sticks out, clip it to [a,b] first.
     P(X > c) with c inside    = (b - c)/(b - a)
     P(c < X < d) with d > b   = (b - c)/(b - a)
```

8.3 MOMENTS AND CDF

```
  mean:      E(X) = (a + b)/2                     the midpoint
  variance:  Var(X) = (b - a)^2 / 12              the width squared over twelve
  cdf:       F(x) = (x - a)/(b - a)   on [a,b],  0 below, 1 above
```

8.4 THE WAIT-TIME STORY (the classic application)

```
  "trains every 15 minutes, arrival uniform, how long does he wait?"
     translate: the WAIT is uniform on [0, interval] (or [0,30] for the 30-min gap)
     then it is a plain uniform question on that interval.
  "less than 6 minutes wait"    -> a sub-length of the wait interval
  "more than 10 minutes"        -> the complement sub-length
```

═══════════════════════════════════════════════════════════════════════════════
9. NORMAL DISTRIBUTION
═══════════════════════════════════════════════════════════════════════════════

9.1 THE SHAPE AND NOTATION

```
  X ~ N(mu, sigma^2)      THE SECOND NUMBER IS THE VARIANCE, NOT THE SD.
     mean = mu          sd = sigma = sqrt(sigma^2)
  the bell: symmetric about mu, total area 1, tails approach zero.

       f(x)
        |        ****
        |     ***    ***
        |   **          **
        +--+----mu-----+---> x
        sd markers: mu-sigma, mu, mu+sigma at the inflection points
```

9.2 STANDARDISATION

```
  z = (X - mu) / sigma          turns any normal into the standard normal N(0,1)
  the standard normal:  mean 0, variance 1.
  FOR A SAMPLE MEAN (the "average of n" questions):
     z = (xbar - mu) / (sigma / sqrt(n))      SE in the denominator, not sigma
```

9.3 THE TWO TABLES (the biggest trap in the paper)

```
  ┌───────────────────────────┬────────────────────────────────────────────┐
  │ CUMULATIVE table F(z)     │ AREA-FROM-MEAN table phi(z)                │
  │ area from -inf to z       │ area between 0 and z                       │
  │ F(0) = 0.5                │ phi(0) = 0                                 │
  │ F(1.5) = 0.9332           │ phi(1.5) = 0.4332                          │
  ├───────────────────────────┴────────────────────────────────────────────┤
  │ bridge:  F(z) = 0.5 + phi(z) for z > 0;  F(z) = 0.5 - phi(|z|) for z<0 │
  │ OUR PAPERS use the phi form: they print things like phi(1.8) = 0.4641  │
  └─────────────────────────────────────────────────────────────────────────┘

  THE FOUR CONVERSIONS (all interval questions are these four lines):
     P(X < a),  z > 0:   0.5 + phi(z)
     P(X < a),  z < 0:   0.5 - phi(|z|)
     P(X > a),  z > 0:   0.5 - phi(z)
     P(X > a),  z < 0:   0.5 + phi(|z|)

  INTERVALS: same signs -> SUBTRACT the phi values; opposite signs -> ADD them.
     P(-1 < Z < 2)  = phi(1) + phi(2)      (opposite: add)
     P(1 < Z < 2)   = phi(2) - phi(1)      (same: subtract)
```

9.4 THE LANMARK RULE (the 68-95-99.7)

```
  within 1 sd of the mean:  about 68.27 percent
  within 2 sd:              about 95.45 percent
  within 3 sd:              about 99.73 percent
  (this is the NORMAL's own rule; Chebyshev applies to ANY distribution and gives
   the 1 - 1/k^2 numbers instead. Do not mix the two sets up in MCQs.)
```

9.5 INVERSE NORMAL (given a probability, find the value)

```
  P(X < x) = p  ->  find z with the right tail area, then  x = mu + z sigma
  "only 20 percent of values lie below this x" with N(8, 5^2):
     phi(|z|) = 0.5 - 0.2 = 0.3  ->  z = -0.84  ->  x = 8 + (-0.84)(5) = 3.8
```

9.6 THE TWO-UNKNOWN PATTERN (two clues, two equations)

```
  "31 percent under 45 and 8 percent over 64, find mu and sigma":
     clue 1 -> an equation:  (45 - mu)/sigma = z1   (z1 from the lower tail)
     clue 2 -> an equation:  (64 - mu)/sigma = z2   (z2 from the upper tail)
     SUBTRACT one from the other: mu vanishes, solve sigma first, then put it back.
  the whole method is: two clues -> two lines -> subtract -> back-substitute.
```

9.7 THE COMPOSITE (normal probability feeding a binomial)

```
  the MTE C1 pattern: part (iii) gives a probability p from the normal.
  part (iv) asks "in 7 days, at most 2 days":  BINOMIAL with n = 7 and p = that answer.
     recognize: "days", "items", "trials" after a probability was just computed
       -> the p carries forward into a binomial.
```

═══════════════════════════════════════════════════════════════════════════════
10. EXPONENTIAL DISTRIBUTION
═══════════════════════════════════════════════════════════════════════════════

10.1 WHAT IT MODELS

```
  the WAITING TIME until the next event, when events follow a Poisson process.
  examples: length of a phone call, repair time, shelf life, time between arrivals.
```

10.2 THE DENSITY AND CDF

```
  X ~ Exp(rate = lambda > 0):
     pdf:      f(x) = lambda e^(-lambda x)        x >= 0
     cdf:      F(x) = P(X <= x) = 1 - e^(-lambda x)
     survival: P(X > x) = e^(-lambda x)

  "parameter" in the question = the rate lambda. no inversion.
  "mean" in the question (mean = 1/lambda): INVERT to get lambda.
```

10.3 MOMENTS

```
  mean:      E(X) = 1 / lambda
  variance:  Var(X) = 1 / lambda^2
  sd:        sqrt(variance) = 1/lambda = the mean
  UNIQUE FACT: for the exponential, sd = mean, always. No other family does this.
```

10.4 MEMORYLESS (the signature)

```
  P(X > s + t | X > s) = P(X > t)

  saying: the object is not "due" for failure. if it has survived s, that fact
  gives NO information about the remaining time. The conditional drops away.

  THE PICTURE: the survival curve resets at every point.
     P(X>10 | X>9) = P(X>1) = e^(-lambda)
  the exponential is the ONLY continuous distribution with this property.
```

10.5 THE TAIL-COMPUTATION RECIPE

```
  P(X > a)  = e^(-lambda a)
  P(X < a)  = 1 - e^(-lambda a)
  P(a < X < b) = e^(-lambda a) - e^(-lambda b)     (subtract two survivals)
  numbers to know: e^-1 = 0.3679, e^-0.5 = 0.6065, e^-2 = 0.1353, e^-4 = 0.0183
```

═══════════════════════════════════════════════════════════════════════════════
11. SAMPLING, STANDARD ERROR, CENTRAL LIMIT THEOREM
═══════════════════════════════════════════════════════════════════════════════

11.1 POPULATION vs SAMPLE

```
  population: every member. its facts are PARAMETERS (mu, sigma^2, p).
  sample: the subset we observe. its facts are STATISTICS (xbar, s^2, p-hat).
  we use statistics to guess parameters. that gap is what "inference" means.
```

11.2 THE SAMPLE MEAN AND STANDARD ERROR

```
  xbar = (X1 + ... + Xn)/n          the estimator of mu
  E(xbar) = mu                      it is unbiased, always
  SE(xbar) = sigma / sqrt(n)        THE STANDARD ERROR, the sd of xbar

  THE PICTURE (why the SE formula):
     one observation has spread sigma.
     averaging n of them divides the wobble by sqrt(n).
        n = 25:  SE = sigma/5
        n = 100: SE = sigma/10        (4x the sample -> HALF the SE)
  "to halve the SE you need FOUR TIMES the sample" is the standard MCQ.
```

11.3 THE CENTRAL LIMIT THEOREM

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │  for a sample of size n from ANY population with mean mu and         │
  │  sd sigma:   xbar is APPROXIMATELY normal with                        │
  │              mean mu  and  sd = sigma / sqrt(n)                      │
  │  and the approximation improves as n grows.                          │
  └──────────────────────────────────────────────────────────────────────┘
  for the course: n >= 30 is the usual working threshold (a heuristic, not a
  universal law); if the POPULATION is normal, any n works.

  THE APPLICABILITY TABLE (the two MCQs test exactly this):
     n >= 30, any shape        -> use the normal, approximately (course heuristic)
     any n, population normal  -> exactly normal
     n < 30, population skewed -> do not assume; inspect or skip
```

11.4 CLT COMPUTATION (the mechanics)

```
  the z formula for an average:     z = (xbar - mu) / (sigma / sqrt(n))
  the same four phi conversions from section 9 apply after standardising.
  WATCH THE DENOMINATOR: an "average of n" question uses the SE; a "single
  observation" question uses plain sigma. This single choice decides the marks.
```

═══════════════════════════════════════════════════════════════════════════════
12. THEORY OF ESTIMATION (the four properties)
═══════════════════════════════════════════════════════════════════════════════

12.1 THE VOCABULARY

```
  parameter (theta):  the true, unknown population fact
  estimator:          the RECIPE (a formula in the sample), e.g. xbar itself
  estimate:           the NUMBER you get once the sample is in, e.g. 52
  the two words are different; the exam swaps them in MCQs.
```

12.2 THE FOUR CHARACTERISTICS (each with its exact test)

```
  ┌───────────────┬──────────────────────────────┬──────────────────────────┐
  │ UNBIASED      │ E(estimator) = theta         │ "correct on average"     │
  ├───────────────┼──────────────────────────────┼──────────────────────────┤
  │ CONSISTENT    │ bias -> 0 and variance -> 0  │ improves as n grows      │
  │               │ as n -> infinity             │                          │
  ├───────────────┼──────────────────────────────┼──────────────────────────┤
  │ EFFICIENT     │ smallest variance AMONG the  │ the tightest of the      │
  │               │ UNBIASED estimators          │ unbiased candidates      │
  ├───────────────┼──────────────────────────────┼──────────────────────────┤
  │ SUFFICIENT    │ the statistic captures all   │ once known, the rest of  │
  │               │ the information about theta  │ the sample adds nothing  │
  └───────────────┴──────────────────────────────┴──────────────────────────┘
```

12.3 THE STANDARD COMPARISON EXERCISE (the exam's favorite)

```
  sample X1..Xn, candidate estimators T:
     step 1  E(T) for each candidate.  equals mu? unbiased.
     step 2  Var(T) for the unbiased ones:  Var(aX+b) rules + independence
     step 3  smallest variance wins = most efficient
     step 4  consistency: check bias -> 0 and variance -> 0 as n -> infinity
  THE TRAP: an estimator with a smaller variance but a bias is OUT of the
  efficiency race (efficiency only compares unbiased candidates).
  THE OTHER TRAP: if the candidate weights sum to something other than 1,
  it is already biased before any variance work.
```

12.4 THE SUFFICIENCY LINE

```
  sufficiency is a property of a statistic for a SPECIFIED parameter in a
  SPECIFIED model. "contains all the information about the parameter" is the
  plain version; the technical version: given the statistic, the conditional
  distribution of the rest of the sample does not depend on that parameter.
  standard results: sum (or mean) is sufficient for Poisson lambda; the sum is
  sufficient for exponential theta; sample mean for a normal mean.
```

═══════════════════════════════════════════════════════════════════════════════
THE FORMULA WALL (everything in one place)
═══════════════════════════════════════════════════════════════════════════════

```
  PROBABILITY
     P(A') = 1 - P(A)                 P(AuB) = P(A)+P(B)-P(AnB)
     P(A|B) = P(AnB)/P(B)             independence: P(AnB) = P(A)P(B)

  RANDOM VARIABLES
     discrete p(x) = P(X=x), sum = 1          continuous: area under f = 1
     F(x) = P(X<=x)   P(a<X<=b) = F(b)-F(a)   f = F'  (continuous)

  EXPECTATION AND VARIANCE
     E(X) = sum x p(x) or integral x f dx
     Var(X) = E(X^2) - [E(X)]^2
     E(aX+b) = aE(X)+b        Var(aX+b) = a^2 Var(X)
     E(X+Y) = E(X)+E(Y)       Var(X+Y) = Var(X)+Var(Y) if independent
     Var(X-Y) = Var(X)+Var(Y) if independent      (PLUS, always plus)

  CHEBYSHEV
     P(|X-mu| >= k sigma) <= 1/k^2       P(|X-mu| < k sigma) >= 1 - 1/k^2
     P(|X-mu| >= c) <= sigma^2/c^2       k=2: 3/4   k=3: 8/9   k=4: 15/16

  BINOMIAL(n,p)                     POISSON(lambda)
     P(X=x) = C(n,x)p^x q^(n-x)       P(X=x) = e^-l l^x / x!
     mean np, var npq                 mean = var = lambda
     approx: Bin(n,p) ~ Poi(np) when np small and n large

  UNIFORM(a,b)                      EXPONENTIAL(lambda)
     f = 1/(b-a) on [a,b]             f = l e^(-lx),  F = 1 - e^(-lx)
     mean (a+b)/2, var (b-a)^2/12     mean 1/l, var 1/l^2, sd = mean
     P(c<X<d) = (d-c)/(b-a)           P(X>x) = e^(-lx)
                                      memoryless: P(X>s+t|X>s) = P(X>t)

  NORMAL(mu, sigma^2)               SAMPLING + CLT
     z = (x-mu)/sigma                 SE = sigma/sqrt(n)
     z = (xbar-mu)/(sigma/sqrt(n))    xbar ~ N(mu, sigma^2/n) approx, large n
     F(z) = 0.5 + phi(z), z>0         68/95/99.7 within 1/2/3 sd
     P(-1<Z<2) = phi(1)+phi(2)        inverse: x = mu + z sigma
```

═══════════════════════════════════════════════════════════════════════════════
THE TRAP LIST (every one seen in real papers)
═══════════════════════════════════════════════════════════════════════════════

```
   1. N(mu, sigma^2): the second number is the VARIANCE. sd = sqrt(that).
   2. "Average of n": use SE = sigma/sqrt(n) in the denominator, never sigma.
   3. The phi table: papers print AREA-FROM-MEAN values (phi(1.8)=0.4641).
      do not mix with the cumulative F(z). Bridge: F = 0.5 + phi.
   4. Independent P(A|B) vs P(B|A): the "given" event goes in the denominator.
   5. Mutually exclusive vs independent: different tests, and nonzero-probability
      events cannot be both.
   6. "at most" vs "at least": at-most sums upward and includes the value;
      at-least uses the complement. One word swings the whole question.
   7. Continuous: P(X=x)=0, so endpoints do not matter. Discrete: they do.
   8. Var(X-Y) = Var(X) + Var(Y): the difference still ADDS the spreads.
   9. Var(aX+b): a gets SQUARED, b disappears.
  10. Exponential "parameter" is the rate; "mean" must be inverted: lambda = 1/mean.
  11. Chebyshev within vs tail: within -> 1 - 1/k^2, tail -> 1/k^2.
  12. Poisson: mean = variance always (the identity), but an equality alone does
      not prove a Poisson law; read the model stated.
  13. The count layer: "how many expected" = probability x number of groups.
  14. The composite: a probability from part (iii) becomes p in a binomial at (iv).
  15. Find-k quadratics: discard the negative or impossible root (p cannot exceed 1).
```

═══════════════════════════════════════════════════════════════════════════════
HOW THE TOPICS CONNECT (the map of the whole course)
═══════════════════════════════════════════════════════════════════════════════

```
                            PROBABILITY (rules)
                                   |
                                   v
                         RANDOM VARIABLES (values)
                                   |
              +--------------------+--------------------+
              v                                         v
     DISCRETE (listable)                        CONTINUOUS (intervals)
        |            |                            |             |
        v            v                            v             v
     pmf/CDF     expectation                   pdf/CDF      expectation
        |            |                            |             |
        +-----+------+------------+---------------+------+------+
              v                   v                      v
        BINOMIAL             POISSON                NORMAL      EXPONENTIAL   UNIFORM
        (n,p counts)          (rare counts)          (bell)      (waiting)    (flat)
              \                   |                    |            |          /
               \                  |                    |            |         /
                +-----------------+---------+----------+------------+--------+
                                            |
                                            v
                                    CHEBYSHEV (bounds any of them)
                                            |
                                            v
                                SAMPLING + CLT (averages)
                                            |
                                            v
                                ESTIMATION (guessing parameters)
```

═══════════════════════════════════════════════════════════════════════════════
WHERE THIS FILE SITS
═══════════════════════════════════════════════════════════════════════════════

```
   THIS file          the theory, explained, all of it, in one place
   deck/notes/        the same theory at full length (11 files, slide-level detail)
   deck/15-DECISION   the if-X-do-Y manual: which method for which question
   deck/worked/       the 158 questions solved from zero
   deck/worked/one-by-one/   one file per question: question + full answer
   deck/12-DRILL.md   the 50-item drill
   reports/08-MOCK    the mock papers

   reading order:  this file once -> notes where a section feels thin ->
                   decision manual -> the drill -> mocks.
```
