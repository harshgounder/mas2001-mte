# 01 CHEATSHEET: everything, one pass

Closed book paper. This page is the whole exam in formulas. Read it daily, last thing at night.

## A. Probability

```
  P(S)=1   P(A)>=0   disjoint additivity on S
  P(A') = 1 - P(A)
  P(A U B) = P(A) + P(B) - P(A n B)
  disjoint: P(A U B) = P(A) + P(B)
  P(A|B) = P(A n B)/P(B),  P(B)>0
  P(A n B) = P(A|B)P(B) = P(B|A)P(A)
  independent: P(A n B) = P(A)P(B)
  (A U B)' = A' n B'      (A n B)' = A' U B'
  n!  0!=1   C(n,r)=n!/(r!(n-r)!)   P(n,r)=n!/(n-r)!   C(n,r)=C(n,n-r)
```

## B. Random variables, pmf, pdf, cdf

```
  discrete      p(x)>=0, sum p(x)=1,  P(X in A)=sum
  continuous    f(x)>=0, int f dx =1, P(a<=X<=b)=int_a^b f dx,  P(X=x)=0
  cdf           F(x)=P(X<=x), non decreasing, F(-inf)=0, F(inf)=1
  P(a<X<=b) = F(b) - F(a)
  discrete      p(x) = F(x) - F(x-)        (the jump)
  continuous    F(x)=int_{-inf}^x f,  f(x)=F'(x)
  integer rv    P(a<=X<=b) = F(b) - F(a-1)   <- the a-1, the commonest slip
```

## C. Expectation

```
  discrete   E(X)=sum x p(x)     continuous  E(X)=int x f dx
  E[h(X)]    sum h(x)p(x)  or  int h(x) f dx
  E(aX+b)=aE(X)+b    E(c)=c    E(X+Y)=E(X)+E(Y)   ALWAYS
  E(XY)=E(X)E(Y)                                  only if INDEPENDENT
  expected count: out of N items, expected = N . P
```

## D. Variance

```
  Var(X) = E[(X-mu)^2] = E(X^2) - [E(X)]^2
  sd = sqrt Var
  Var(aX+b) = a^2 Var(X)      sd(aX+b) = |a| sd(X)      Var(c)=0
  Var(X+Y) = Var(X)+Var(Y)        independent only
  Var(X-Y) = Var(X)+Var(Y)        independent only, the MINUS still ADDS
  Var(Xbar) = sigma^2 / n
```

## E. Chebyshev

```
  P(|X-mu| >= k sigma) <= 1/k^2                 k>0
  P(|X-mu| >= eps)     <= sigma^2/eps^2
  P(|X-mu| <  k sigma) >= 1 - 1/k^2             complement form
  k=2 -> 3/4    k=3 -> 8/9    k=4 -> 15/16    k=1 -> 1, useless
  k is in standard deviations: k = eps/sigma
  no distribution assumed, only finite mu and variance
  always an UPPER bound on the tail, so actual <= bound, say so when asked
```

## F. The five distributions

```
  BINOMIAL   X~B(n,p)   q=1-p
      P(X=x)=C(n,x)p^x q^(n-x)      E=np    Var=npq
      needs: 2 outcomes, finite n, independent trials, p constant

  POISSON    X~Poi(l)
      P(X=x)=e^-l l^x / x!          E=l     Var=l      (mean = variance)
      l = np for the rare-event approximation, n large p small

  UNIFORM    X~U(a,b)
      f=1/(b-a)     E=(a+b)/2     Var=(b-a)^2/12     F=(x-a)/(b-a)
      probability = length ratio

  NORMAL     X~N(mu, sigma^2)      (second slot is VARIANCE)
      Z=(X-mu)/sigma                X = mu + Z sigma
      P(a<X<b) = Phi((b-mu)/s) - Phi((a-mu)/s)
      Phi(-z)=1-Phi(z)     P(Z>z)=1-Phi(z)
      landmarks: 68.27 within 1s, 95.45 within 2s, 99.73 within 3s

  EXPONENTIAL T~Exp(l)   (l is a RATE)
      f=l e^{-l t}    F=1-e^{-l t}    P(T>t)=e^{-l t}
      E=1/l    Var=1/l^2
      memoryless: P(T>s+t | T>s) = P(T>t)
      if the question gives the MEAN mu instead, l = 1/mu and f=(1/mu)e^{-t/mu}
```

## G. Sampling, SE, CLT

```
  SE of the mean      sigma_Xbar = sigma / sqrt(n)
  SE estimate         S / sqrt(n)
  SE of a proportion  sqrt( p(1-p)/n )
  CLT  n>=30 any population:  Xbar ~ N(mu, sigma^2/n) approx
       Z = (Xbar - mu)/(sigma/sqrt(n))
  exact, not approx, when the population itself is normal (any n)
  n<30 and population not normal: CLT does NOT apply
  sum of n draws ~ N(n mu, n sigma^2)
  quadruple n -> halve the SE   (sqrt rule)
```

## H. Estimation

```
  estimator = a rule (a random variable), estimate = the number
  unbiased     E(theta-hat) = theta
  consistent   converges in probability; sufficient pair E->theta, Var->0
  efficient    smallest variance AMONG UNBIASED
  relative efficiency of T1 vs T2 = Var(T2)/Var(T1)
  sufficient   uses all information in the sample (Neyman-Fisher)
  MSE = Var + Bias^2
  Xbar: unbiased, Var = sigma^2/n, consistent
  S^2 = sum(Xi-Xbar)^2/(n-1): unbiased for sigma^2   (the n-1 matters)
  p-hat = X/n: unbiased, Var = p(1-p)/n
```

## I. The four sentence patterns that carry most marks

```
  1  "state which estimator is unbiased"       check E of each, sum the coefficients
  2  "find the constant that makes it unbiased" solve sum of coefficients = divisor
  3  "which is most efficient"                 variances, smallest among the unbiased
  4  "show Xbar is consistent"                 E=mu for all n, Var=sigma^2/n -> 0
```

## J. Boundaries

```
  in scope   lectures 1 to 21, the four MTE papers plus their schemes, the in-scope parts of
             the 2024-25 and 2025-26 assignments, all four S&P decks, the Chebyshev deck
  boundary   the confidence interval shape (named in lecture 19, mechanics in lecture 25)
  out        MLE, method of moments, hypothesis testing, t/F/chi-square, ANOVA,
             confidence interval mechanics, lms-theory p031-p040
```
