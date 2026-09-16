# 02 TERMS: every term, exact meaning, the trap in each

Read with the theory. Each entry is: the term, what it exactly means, and the trap or the
reason the term matters. Terms are grouped by topic.

## Probability

```
  sample space S        the set of all possible outcomes. TRAP: for two dice write 36 ORDERED
                        outcomes, not 21 unordered. The counting must match the space.
  event                 a subset of S. TRAP: "at least one" is the complement of "none".
  mutually exclusive    no two share an outcome (disjoint). TRAP: NOT the same as independent.
                        A die roll even vs prime SHARE the outcome 2, so they are not exclusive.
  independent           P(A n B) = P(A)P(B). TRAP: exclusive events with P>0 are NOT
                        independent (if one happens the other cannot, so knowing A changes B).
  conditional P(A|B)    the chance of A given B already happened. TRAP: the denominator is
                        P(B), not P(A). P(A|B) != P(B|A).
  Bayes                 swapping the condition: P(A|B) = P(B|A)P(A)/P(B). Used in the rare
                        disease and county-forms questions.
  complement discipline "at least one", "none", "rejected", "more than" are all complements.
                        This single move solves more probability marks than any formula.
```

## Counting

```
  permutation P(n,r)    ordered selections, "arrangements", "lineups", "how many ways to
                        order". Order matters.
  combination C(n,r)    unordered selections, "choose", "committees", "sets of". Order does
                        NOT matter. TRAP: "how many ways to form a committee of 3" is C, not P.
  factorial, 0!=1       the seed for every count.
  repeated items        if items repeat, divide by the repeats' factorials.
  complement counting   count the easy case and subtract from the total.
```

## Random variables

```
  random variable       a FUNCTION from the sample space to the real line. TRAP: it is not the
                        outcome, it is the number you attach to the outcome.
  discrete rv           countable support (a list). Uses sums.
  continuous rv         an interval of support. Uses integrals. P(X = one point) = 0.
  support               the set where the rv lives. TRAP: ALWAYS check the support before
                        integrating or summing; a density is zero outside it.
  function of an rv     Y = g(X). TRAP: changing g changes the DISTRIBUTION of Y, so recompute
                        the support of Y before anything else.
  Bernoulli             one trial, X = 1 or 0, P(1)=p. Mean p, variance pq. The atom of binomial.
  geometric             counts trials until the first success. E = 1/p. Memoryless like the
                        exponential, in the discrete world. (no teaching slide, see 11)
  hypergeometric        draws WITHOUT replacement from a finite lot. Mean nK/N, the same as the
                        binomial mean at the same p. (no teaching slide, see 11)
```

## pmf, pdf, cdf

```
  pmf p(x)              discrete, P(X=x). Must be >=0 and sum to 1.
  pdf f(x)              continuous, a DENSITY, not a probability. f(x) can exceed 1 (example:
                        uniform on width 0.5 has f=2). Only its INTEGRAL is a probability.
  cdf F(x)              P(X<=x) for both. Non decreasing, 0 to 1, right continuous.
  pmf from cdf          p(x) = F(x) - F(x-), the jump. For integer rv, F(b)-F(a-1).
  pdf from cdf          f = F'. Integrate to go up, differentiate to come down.
  "valid pdf" check     integrate over its support and it must equal 1. Finding k is exactly
                        this check rearranged.
```

## Expectation

```
  expectation E(X)      the weighted average, the long run mean. Symmetry trick: for symmetric
                        densities E = the centre, no integral needed.
  E[h(X)]               the mean of a TRANSFORMED rv. TRAP: E[g(X)] != g(E(X)) in general.
  linearity             E(aX+b)=aE(X)+b, E(X+Y)=E(X)+E(Y) with NO independence needed.
  product rule          E(XY)=E(X)E(Y) needs INDEPENDENCE. TRAP: this is the classic true/false.
  expected count        out of N items, expected = N x P(success). No teaching slide, see 11.
```

## Variance

```
  variance              E[(X-mu)^2], the spread squared. Never negative.
  shortcut              E(X^2) - [E(X)]^2. Always easier than the definition.
  standard deviation    sqrt Var, in the ORIGINAL units. Use sd when Chebyshev k or a z-score
                        is involved.
  Var(aX+b)             a^2 Var(X). TRAP: the shift b does NOTHING, the scale a squares.
  Var(X-Y)              Var(X)+Var(Y). TRAP: the MINUS stays PLUS because Var is on squares.
  Var(Xbar)             sigma^2/n. The root of every CLT standard error.
```

## Chebyshev

```
  Chebyshev inequality  bounds a tail using only mu and sigma. Any distribution.
  k                     distance in STANDARD DEVIATIONS, k = eps/sigma. TRAP: raw units in,
                        must convert to sigma units first.
  vacuous bound         k<=1 gives a bound of 1 or more, which says nothing.
  distribution-free     no normal table, no assumption. That is why "which is valid without
                        knowing the distribution" always points here.
```

## Distributions

```
  binomial              n independent 2-outcome trials, p constant, X counts successes. E=np.
  Poisson               counts of rare events in a fixed window. The signature is E = Var = l.
  uniform               constant density. Probability is proportional to interval LENGTH.
  normal                bell, symmetric, mean = median = mode = mu. Second parameter is VARIANCE.
  standard normal Z     N(0,1), the table world. Every normal question goes through Z.
  phi vs F              TWO table conventions. phi(z) is usually the area from 0 to z, F(z) is
                        the cumulative from -inf. MIXING THEM is the single biggest normal error.
                        Decide which the question gives BEFORE substituting. (see 11)
  exponential           waiting time, l = rate, mean = 1/l. TRAP: rate vs mean confusion.
  memoryless            surviving s more given you survived to now = surviving s. No ageing.
  Poisson as a limit    binomial with n big and p small, l = np. "Use the approximation" means
                        Poisson with that l.
```

## Sampling, CLT

```
  population vs sample  N with parameters (mu, sigma) vs n with statistics (Xbar, s).
  parameter             a number describing the population (mu, sigma, p).
  statistic             a number computed from the sample (Xbar, S, p-hat).
  sampling distribution the distribution of a statistic over repeated samples.
  standard error        the standard deviation of that sampling distribution. SE = sigma/sqrt(n).
  CLT                   for n>=30 the SAMPLE MEAN is approximately normal, whatever the shape of
                        the population. TRAP: it is about the MEAN, not about single values.
  exact vs approx       a normal population gives an exactly normal Xbar at ANY n. This is the
                        fallback when a question uses a small n.
  sqrt-n rule           quadruple n, halve SE. The answer to "how large a sample".
```

## Estimation

```
  estimator             a RULE, a random variable (Xbar is a rule). 
  estimate              the NUMBER once data is plugged in (Xbar = 205 ms).
  unbiased              E(theta-hat) = theta. Correct ON AVERAGE, not per sample.
  bias                  E(theta-hat) - theta.
  consistent            converges to theta as n grows. A large-sample property.
  consistency test      sufficient pair: E(Tn)->theta and Var(Tn)->0.
  efficient             smallest variance AMONG THE UNBIASED. TRAP: a biased estimator can have
                        a smaller variance and still lose, it is disqualified first.
  relative efficiency   Var(T2)/Var(T1). Bigger than 1 means T1 is more efficient.
  sufficient            the estimator keeps all the information about theta in the sample.
                        Neyman-Fisher factorisation is the test.
  MSE                   Var + Bias^2. The honest score when bias is allowed to compete.
  n-1                   the sample variance divides by n-1, not n, to be unbiased. The reason is
                        that deviations are measured from Xbar, which already used the data.
```

## Words that are not statistics but decide marks

```
  "exactly"        P(X=x), point probability
  "at least k"     P(X>=k) = 1 - P(X<=k-1)
  "at most k"      P(X<=k)
  "more than k"    P(X>k) = 1 - P(X<=k)   NOTE the boundary moves
  "no" / "none"    P(X=0)
  "between a and b" depends on <= vs <, for continuous rv it does not matter
  "expected number" N x P, expected COUNT not probability
  "on average"      mean
  "spread"/"variation" variance or sd, read which unit is wanted
  "consistent with" a distributional claim, an applicability test
  "using the approximation" Poisson with l = np, not the exact binomial
```
