# 03 LINGUISTICS: the question wording decoder

## THE DECODER FLOWCHART

```
   READ THE QUESTION
        │
        ├─── is there a story word? ───────────────────────────┐
        │    (calls, arrivals, lifetime, trials, equally likely)│
        │                                                       │
        │                          ┌────────────────────────────┘
        │                          ▼
        │              "calls/rare per unit"  -> POISSON
        │              "n trials, success"    -> BINOMIAL
        │              "waiting/lifetime"     -> EXPONENTIAL
        │              "equally likely"       -> UNIFORM
        │              "normally distributed" -> NORMAL
        │              "the average of n"     -> CLT + SE
        │
        └─── if NO story word -> event probability
                 │
                 ├── "given that"        -> conditional P(A|B)
                 ├── "at least one"      -> complement
                 ├── "how many ways"     -> counting C(n,r)
                 └── "are they independent" -> the product test
                          │
                          ▼
                 NOW read the BOUNDARY word
                 at least / more than / exactly / at most
                          │
                          ▼
                 NOW read the UNIT (min? hr? days?)
                          │
                          ▼
                 NOW read what is ASKED for
                 probability / expectation / variance / a parameter
```

## THE BOUNDARY-WORD MACHINE

```
   number line with the boundary:

   ... k-1     k      k+1 ...
       │       │       │
       │       │       │
   P(X≤k-1)  P(X=k) P(X≥k+1)
   ┌──────────────────────────────────────────┐
   │ "at least k"  = includes k = 1 - P(X≤k-1) │
   │ "more than k" = excludes k = 1 - P(X≤k)   │
   │ "at most k"   = includes k = F(k)         │
   │ "less than k" = excludes k = F(k-1)       │
   └──────────────────────────────────────────┘

   for a CONTINUOUS rv these boundaries do NOT matter (P(X=k)=0)
   for a DISCRETE rv they are worth marks
```

## THE UNIT TRAP, DRAWN

```
   15 per HOUR,  find P(gap < 3 MINUTES)

        rate in HOURS              time in MINUTES
        ┌───────────┐              ┌───────────┐
        │ λ = 15/hr │              │ t = 3 min │
        └───────────┘              └───────────┘
              │                          │
              └──────────┬───────────────┘
                         ▼
              CONVERT ONE TO MATCH THE OTHER
                         │
                   t = 3/60 = 0.05 hr
                         │
                         ▼
              1 - e^{-(15)(0.05)} = 0.5276

   NEVER substitute a rate and a time in different units.
```

The setters reuse a small vocabulary. Almost every wording maps to a fixed ask and a fixed
method. This file is the map from phrase to ask. Read it before a drill pass.

## 1. The trigger words, mapped to the ask

```
  wording in the question                     the ask                  the move
  "exactly k"                                P(X = k)                 direct pmf / pdf point value
  "at least k" / "not less than k"           P(X >= k)                complement, 1 - P(X<=k-1)
  "at most k" / "no more than k"             P(X <= k)                cdf directly
  "more than k" / "exceeds k"                P(X > k)                 complement, 1 - P(X<=k)
  "fewer than k"                             P(X < k)                 cdf at k-1 (discrete)
  "none" / "no" / "zero of them"             P(X = 0)                 single pmf term
  "at least one"                             P(X >= 1)                complement, 1 - P(X=0)
  "between a and b"                          P(a<X<b)                 continuous: F(b)-F(a)
                                                                        integer: F(b-1)-F(a)
  "not more than ... apart"                  |X - c| <= d             interval then probability
  "within k of the mean"                     |X-mu| <= k              interval or Chebyshev
  "deviates by at least k"                   |X-mu| >= k              Chebyshev tail form
  "is at least ..."                          lower bound              Chebyshev COMPLEMENT form
  "expected number" / "expected value"       expectation              N x P if a count of items
  "on the average"                           mean                     1/l for exponential
  "find k" / "find the constant"             normalisation            integral or sum = 1
  "is it a valid pdf"                        check                    integral over support = 1
  "how large a sample"                        n from SE                SE = sigma/sqrt(n) rearrange
  "the probability that the mean ..."        sampling distribution    use SE in the denominator
  "the average of n ..."                     Xbar                     SE denominator, NOT sigma
  "is the estimator unbiased"                E(theta-hat) = theta     compute E
  "most efficient"                           min variance             among the unbiased only
  "is it consistent"                         large-sample claim       E->theta and Var->0
```

## 2. The boundary words, exact

```
  "at least k"  includes k.   P(X>=k) = 1 - P(X<=k-1)
  "more than k" EXCLUDES k.   P(X>k)  = 1 - P(X<=k)
  "at most k"   includes k.   P(X<=k) = F(k)
  "less than k" excludes k.   P(X<k)  = F(k-1)  for an integer rv

  for a CONTINUOUS rv these boundaries do not matter, P(X=k)=0 either way.
  for a DISCRETE rv they are worth marks. Read the word twice.
```

## 3. The story templates (a story is a distribution in disguise)

```
  story words                                   distribution
  "n independent trials", "each trial", "success" binomial
  "number of arrivals", "calls", "defects per unit", "arrivals in an interval" Poisson
  "time between arrivals", "waiting time", "lifetime", "until failure" exponential
  "equally likely", "random point in an interval", "uniformly" uniform
  "heights/weights/marks are normally distributed", "approximately normal" normal
  "no memory", "as good as new", "does not age"                          exponential memoryless
  "without replacement", "from the lot", "sample of k from N items"      hypergeometric
  "how large a sample", "how many observations"                          SE/CLT inverse
  "the whole population of ... ", "draws of n"                           sampling distribution
```

## 4. The instruction verbs (what the marker wants)

```
  "find" / "compute" / "calculate"   a number, show the working, two lines of setup
  "show that" / "prove"              a derivation, every algebra step written
  "state"                            the formula or the theorem, no derivation needed
  "verify" / "check that"            substitute and confirm, one line
  "hence" / "using the above"        reuse the earlier part, do not restart
  "compare" / "comment"              state which is bigger/smaller and why, one sentence
  "state the assumptions"            list the conditions (n, independence, p constant)
  "explain whether"                  a true/false verdict WITH one reason
```

## 5. The words that decide which formula wins

```
  "independent"          opens the product rule E(XY)=E(X)E(Y), Var(X+Y)=Var(X)+Var(Y)
  "not independent"      do not factor E(XY) or drop covariance without more information.
                         A joint distribution or a stated covariance can still make it solvable.
  "population is normal" opens the exact-Xbar fallback at any n
  "large sample" / "n=50, n=40"  opens CLT with an approximate answer
  "small sample, non-normal"     do not assume a normal approximation without justification
  "known sigma"          use sigma/sqrt(n) directly
  "sample standard deviation"    use S/sqrt(n)
  "rate"                 Poisson or exponential, never a mean
  "mean time"            reciprocal of the rate, check unit
  "variance is 25"       sigma = 5, square root it before z
  
  THE UNIT TRAP: exponential and CLT questions mix minutes and hours, or hours and days.
  Convert so the rate and the time share a unit BEFORE computing. ("15 per hour, 3 minutes")
```

## 6. The three question shapes the paper reuses

```
  shape 1  single slot            "find P(X=k)" or "find E(X)". One formula, one answer.
  shape 2  chain                  "find k, then the mean, then the probability". Each part
                                  uses the previous part's number. Do NOT restart.
  shape 3  applicability          "which of these estimators is unbiased, and which is most
                                  efficient". A protocol, not a computation: unbiased first,
                                  then compare variances of the survivors.
```

## 7. Words that appear in our corpus questions and what they meant (real examples)

```
  "the expected number of sets with no even number"    N x P, expected COUNT not a probability
  "find the value of the constant c such that P(...)<=0.04"  Chebyshev, solve 1/k^2 = 0.04
  "using Chebyshev's inequality find the lower bound"  complement form 1 - 1/k^2
  "determine a number b such that P(X<b)=P(X>b)"       median via symmetry, b = midpoint
  "check that f(x) is a pdf, and determine k"          normalise first, THEN answer the second ask
  "find the number of failures before the first success" geometric count, check the convention
  "probability that exactly two arrive in each minute"  nest: Poisson per minute, then binomial
                                                       over the minutes
  "find the minimum value of n"                        solve an inequality in n, not an equality
  "find the mean and variance of X"                    E(X), then E(X^2)-[E(X)]^2, show both
  "is T an unbiased estimator of theta"                compute E(T), compare to theta, verdict
```
