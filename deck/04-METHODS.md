# 04 METHODS: solving path per question type

Every method here is the one the course teaches, plus the fastest valid alternative. Each
entry: when to use it, the steps, and the alternate with its tradeoff.

## 1. Probability of an event

```
  when   any "find the probability that ..." that is not a named distribution
  steps  1 name the sample space and count its size (ordered if the count needs it)
         2 write the event as a set of outcomes, or as a complement
         3 if complement is easier, use P(A) = 1 - P(A')
         4 for "at least one" always go through the complement
  alternate  direct counting vs complement. Complement wins whenever the event says
             "at least", "none", "all of them". Direct counting wins for small explicit sets.
```

## 2. Conditional and independence

```
  when   "given that", "if ... what is the probability", or a two-stage draw
  steps  1 identify the condition B
         2 write P(A|B) = P(A n B)/P(B)
         3 get the intersection from the multiplication rule if the story gives conditionals
  alternate  a tree diagram. Slower to draw but it stops the P(A|B) vs P(B|A) swap.
  independence test  P(A n B) = P(A)P(B), or P(A|B) = P(A). Either form, one line.
```

## 3. Build a distribution (pmf or pdf) from a story

```
  when   "find the probability distribution of X", or "X has pdf f(x)=..."
  steps  1 write the SUPPORT of X first
         2 for discrete, tabulate x and p(x), then verify sum = 1
         3 for continuous, write f(x) with its range, then verify integral = 1
  alternate  if the story is a named distribution, skip the build and name it (binomial,
             Poisson, etc), then quote pmf and moments.
```

## 4. Find the constant k

```
  when   "find k such that f(x) is a density" or "determine k"
  steps  1 write the normalisation, integral (or sum) over the SUPPORT = 1
         2 integrate the polynomial, collect k
         3 solve for k
  traps  the support is finite here, not (-inf, inf). A scheme that prints infinite bounds and
         then evaluates on a finite support is printing a slip (see errata 20).
         the sum version: watch for a k^2 term, the equation can be quadratic with one valid
         positive root (the batch-1 assignment gives k = 1/10 from 10k^2 + 9k = 1)
```

## 5. cdf from pmf or pdf, and back

```
  when   "find the cdf", "find F(x)", "given F(x) find f(x)", "find P(X<6) from the cdf"
  steps  pmf -> cdf  accumulate: F(x) = sum of p up to x. Piecewise on the INTEGER values.
         pdf -> cdf  integrate f from the lower support edge to x
         cdf -> pdf  differentiate F on each interval
         cdf -> pmf  the jump F(x) - F(x-)
  traps  a cdf accumulates ALL earlier mass. For a piecewise cdf on 1<=x<=2 you must add
         the mass from 0 to 1 (errata 19: the 2024 MTE CDF is option D, not the scheme's B)
         the minimum c with F(c) > 1/2 is a cdf query, read it off the accumulation
```

## 6. Expectation

```
  when   "find E(X)", "find the expected value", "find E[h(X)]"
  steps  1 write the sum (discrete) or integral (continuous), over the support
         2 plug, integrate or sum
         3 for E(X^2) repeat with x^2
  alternate  symmetry: a density symmetric about c has E(X) = c with no integration.
  traps  E[g(X)] != g(E(X)). Compute the integral of g, do not plug E into g.
         for a count of items: expected count = N x P, do not report P alone.
```

## 7. Variance

```
  when   "find the variance", "find the sd", "find E(X) and Var(X)"
  steps  1 E(X)
         2 E(X^2) from its own sum/integral
         3 Var = E(X^2) - [E(X)]^2
         4 sd = sqrt Var when asked for spread in original units
  alternate  for a named distribution quote np, npq, l, (b-a)^2/12, 1/l^2 directly.
  traps  keep EXACT values until the final line (errata 12: rounding Var then rooting it
         gives 0.975, the exact sd is 0.9734 -> 0.97)
         the variance is never negative, if you get a negative check your arithmetic
```

## 8. Chebyshev

```
  when   "using Chebyshev's inequality", "find the lower bound", "without assuming a
         distribution", "is this distribution-free"
  steps  1 get mu and sigma (compute if not given, sigma = sqrt Var)
         2 convert the event to |X-mu| >= eps or < eps
         3 k = eps / sigma           (raw units to sigma units)
         4 tail form 1/k^2, or complement form 1 - 1/k^2, whichever the wording wants
  alternate  if the exact distribution is known, compute the exact value TOO and report
             "bound 35/54, exact 1/3, the bound holds and is wider"
  traps  k must be in sigma units. The complement form is for "at least"/"within".
         The bound can exceed 1 (k<=1), then it is vacuous.
         errata 15: the L10-11 deck's Q3 slide mis-states its own row, use Q1 and Q2 only.
```

## 9. Binomial

```
  when   n trials, two outcomes, independent, p constant, count the successes
  steps  1 state X ~ B(n, p), write q = 1-p
         2 the ask: point, tail (complement), or interval
         3 substitute the pmf, use C(n,x)
  alternate  for "at least 1" use 1 - q^n (faster than summing)
  traps  "at least 2" = 1 - P(0) - P(1), the classic two-term complement
         read "p is the success probability", if the story gives failures, invert it first
```

## 10. Poisson

```
  when   rare events, arrivals, in a fixed window, or "use the approximation" with n big p small
  steps  1 get l. If given a rate, scale it to the window. If given np in an approximation,
           l = np.
         2 the ask: point e^-l l^x/x!, tail (complement), or the zero case e^-l
         3 state Var = l if asked, it equals the mean
  alternate  for the ratio question P(X=1)=c P(X=2), the e^-l cancels, leaving l = 2/c
  traps  rate vs window scaling (2 per minute, then 5 minutes -> l = the window's rate)
         the nesting: Poisson per minute THEN binomial over the minutes (0.00145 question)
         mean equals variance is the signature, use it to spot Poisson
```

## 11. Uniform

```
  when   "equally likely in an interval", "random point"
  steps  1 identify a and b
         2 probability = length ratio, P(a<=X<=b) = (interval)/(b-a)
         3 moments: mean (a+b)/2, variance (b-a)^2/12
  traps  clip to the support, a value outside [a,b] has probability 0 or 1, not the ratio
         absolute-value events become intervals first: |X-5|<1 is 4<X<6
```

## 12. Normal

```
  when   normal, approximately normal, large-sample mean, or the CLT destination
  steps  1 identify mu and sigma (sigma from variance, sqrt it)
         2 DECIDE which table the question gives (phi area-from-0, or F cumulative)
         3 standardise Z = (X-mu)/sigma
         4 read the table, apply symmetry Phi(-z) = 1 - Phi(z)
         5 for the inverse: get z for the probability, then X = mu + z sigma
  alternate  landmarks: within 1s 68.27, 2s 95.45, 3s 99.73, for a fast sanity check
  traps  the second parameter is VARIANCE, sqrt it
         the inverse's forgotten last step: convert z back to the X scale
         two-unknown questions: two given probabilities give two equations, solve simultaneously
         (errata 10: use mu = 37.2, sigma = 28.2, cutoff = 30.4)
```

## 13. Exponential

```
  when   waiting time, time between arrivals, lifetime, "no memory"
  steps  1 get l (a RATE). If given a mean, l = 1/mean.
         2 match the units of l and t
         3 point/interval: F = 1 - e^-lt.  tail: e^-lt.
         4 memoryless if the condition is on surviving
  alternate  mean-first form f = (1/mu) e^{-t/mu} when the question gives mu directly
  traps  rate vs mean reciprocal (errata 4: the slide p040 states it backwards, read p041)
         conditional in the exponential: P(X<1 | X<2) = (1-e^-0.5)/(1-e^-1) = 0.6225
         (errata 9: the assignment prints 0.5679, that is wrong)
```

## 14. Sampling and standard error

```
  when   "standard error", "sampling distribution", "the mean of a sample of n"
  steps  1 SE = sigma / sqrt(n) (or S/sqrt(n) if the sample sd is given)
         2 the "average of n" template divides by SE, not sigma
  alternate  the sqrt-n rule for sample-size questions: quadruple n halves SE
  traps  a single observation uses sigma; an average of n uses sigma/sqrt(n). Mixing these
         is the commonest CLT slip.
```

## 15. CLT

```
  when   "the sample mean is approximately normal", n listed, population shape unknown
  steps  1 check n >= 30, or the population is normal
         2 Xbar ~ N(mu, sigma^2/n), so Z = (Xbar - mu)/(sigma/sqrt(n))
         3 read the table as a normal
  alternate  for a SUM not a mean, the sum is N(n mu, n sigma^2), sigma scales by sqrt(n) not n
  traps  n<30 with a non-normal population: the CLT does not apply, say so and stop
         a normal population is exact at any n, this is the fallback for small-n questions
         (errata 6: impurity Z2 = -0.94, the slide prints -0.4)
```

## 16. Estimator comparison (the 6 to 8 mark question)

```
  when   "which estimator is unbiased", "most efficient", "find the constant"
  steps  1 write E of each estimator, expand using linearity
         2 unbiased: E(T) = theta. Solve for the constant if one exists.
         3 for each UNBIASED estimator, compute Var(T) using Var(Xi)=sigma^2 and independence
         4 the smallest variance wins
  alternate  relative efficiency Var(T2)/Var(T1) when asked to compare a pair
  traps  a biased estimator is DISQUALIFIED before the variance comparison, even if its
         variance is smaller (errata 18, mock B4: T4 is biased and third of four, the note
         calling it "smallest" is wrong)
         consistency is a large-n property, a fixed-n small variance does not make a
         consistent estimator
```

## 17. The protocol when a question chains parts

```
  when   "find k ... hence find the mean ... hence find P(X>...)"
  steps  1 treat each part as independent given the previous answer
         2 carry the EXACT value forward, round only at the final line
         3 if a part is impossible, say so, do not silently continue (the asgn-variant has
           a row and a key that cannot both be right, errata 5.1)
```
