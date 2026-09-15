# MAS2001 MTE formula sheet

Closed book paper, 30 marks. Everything here is inside the MTE scope unless a line says
otherwise. `deck` means `notes-lecture-series-01-09`, the 147 page Dr. Vivek Singh series.
Page refs are the pipeline page numbers, so `deck p104` is `md/notes-lecture-series-01-09/p104.md`.

Every closed form on this sheet is numerically verified in `reports/06-VERIFICATION.md`.

---

## A. Probability fundamentals (deck p023 to p050)

Notation: S is the sample space, A and B are events.

```
Axioms                       P(S) = 1,  P(A) >= 0,  countable additivity on disjoint events
Complement                   P(A') = 1 - P(A)
Addition rule                P(A U B) = P(A) + P(B) - P(A n B)
Disjoint case                A n B = empty  =>  P(A U B) = P(A) + P(B)
Conditional probability      P(A | B) = P(A n B) / P(B),    P(B) > 0
Multiplication rule          P(A n B) = P(A | B) P(B) = P(B | A) P(A)
Independence                 P(A n B) = P(A) P(B)   <=>   P(A | B) = P(A)
Mutually exclusive           no two of the events share an outcome
```

Relations used constantly with Venn diagrams (deck p031 to p040):

```
A n B'   is  "A but not B"
(A U B)' = A' n B'
(A n B)' = A' U B'
```

Counting, needed for every combinatorics question (deck p046 to p049):

```
n!            = n(n-1)...1,   0! = 1
C(n, r)       = n! / (r! (n-r)!)          "choose", order does not matter
P(n, r)       = n! / (n-r)!               "permute", order matters
C(n, r)       = C(n, n-r)
```

Worked in the corpus: laptop allocation from 6 faculty (deck p046), basketball lineup
(deck p048).

---

## B. Random variables and their distributions (deck p051 to p147)

A random variable is a function whose domain is the sample space and whose range is the
real line (deck p051).

Discrete random variable, probability mass function p(x) = P(X = x):

```
p(x) >= 0  for every x,        sum over all x of p(x) = 1
P(X in A) = sum over x in A of p(x)
```

Continuous random variable, probability density function f(x):

```
f(x) >= 0,                     integral of f over the whole line = 1
P(a <= X <= b) = integral from a to b of f(x) dx
P(X = x) = 0 for every single point x, so the endpoints a and b do not matter
```

Cumulative distribution function, both cases:

```
F(x) = P(X <= x),      F is non decreasing,  0 <= F(x) <= 1,  F(-inf) = 0, F(inf) = 1
P(a < X <= b) = F(b) - F(a)
Discrete:   p(x) = F(x) - F(x-)                pmf is the jump in the cdf
Continuous: F(x) = integral from -inf to x of f(t) dt,   f(x) = dF(x)/dx
```

Both are on the MTE syllabus as lectures 5 and 6, and the deck spends p063 to p087 on
the discrete case and p112 to p147 on the continuous case.

---

## C. Expectation (deck p088 to p094, p140 to p147)

```
Discrete            E(X) = sum over x of x p(x)
Continuous          E(X) = integral over the line of x f(x) dx
Function of X       E[h(X)] = sum h(x) p(x)     or     integral h(x) f(x) dx
Linear              E(aX + b) = a E(X) + b
Sum                 E(X + Y) = E(X) + E(Y)                always
Product             E(XY) = E(X) E(Y)                     when X and Y are independent
Constant            E(c) = c
```

Expectation is linear with no independence needed. That distinction is exactly the
kind of true or false the paper can carry.

---

## D. Variance and standard deviation (deck p095 to p111, p144 to p147)

```
Definition          Var(X) = E[(X - mu)^2],   mu = E(X)
Computing formula   Var(X) = E(X^2) - [E(X)]^2            shortcut, deck p101
Standard deviation  sigma = sqrt(Var(X))
Linear transform    Var(aX + b) = a^2 Var(X),   sd(aX + b) = |a| sd(X)     deck p104
Sum, independent    Var(X + Y) = Var(X) + Var(Y)          needs independence
Constant            Var(c) = 0
```

The shift by b never changes spread, and the slope a scales spread by its absolute value.
Both facts show up as one mark sub questions.

---

## E. Chebyshev's inequality (MTE lectures 10 and 11; deck S&P L10-11 arrived 15 Sep)

(The 15 September batch closed the old gap. The deck carries the theorem, the k-sigma
restatement, the complement form and two worked questions; sheet and bank remain the drill.)

```
P(|X - mu| >= k sigma) <= 1 / k^2                 k > 0
P(|X - mu| >= eps)     <= sigma^2 / eps^2         equivalent form
P(|X - mu| <  k sigma) >= 1 - 1 / k^2             complement form
```

Facts worth memorising, because the paper likes to probe them:

1. It needs only a finite mean and finite variance. No distribution is assumed. That is
   what makes it different from a normal table computation.
2. For k <= 1 the bound is vacuous, it only says the probability is at most 1.
3. The bound is an upper bound on tail probability, so a question that hands you a known
   distribution and asks for the actual probability wants both numbers, and the actual
   probability is always at most the bound.
4. k is measured in standard deviations, not in raw units. Convert first: k = eps / sigma.
5. The k values with exact useful bounds: k=2 gives 3/4, k=3 gives 8/9, k=4 gives 15/16.

Assignment 1 question 5 in the corpus uses variant 1 on the sum of two dice, and the
course handout also lists a binomial tail variant. Both are worked in
`reports/04-QUESTION-BANK.md`.

---

## F. Discrete distributions

### Binomial (lecture 12, ppt3 p001 to p018)

Setup: n independent trials, two outcomes per trial, P(success) = p constant, q = 1 - p.
X counts successes, X ~ B(n, p).

```
pmf         P(X = x) = C(n, x) p^x q^(n-x),        x = 0, 1, ..., n
mean        E(X) = n p
variance    Var(X) = n p q
sd          sqrt(n p q)
mode        the value of x where the ratio P(X = x+1)/P(X = x) crosses 1
```

Recognition checklist from ppt3 p011: each trial has two mutually disjoint outcomes,
n is finite, trials are independent, p is constant across trials.

Worked in the corpus: 5 coin tosses (ppt3 p003 to p007), 10 percent defective pens in a
box of 12 with the complement trick for "at least 2" (ppt3 p013 to p016), irregular die
with p = 5/8 over 10 throws (ppt3 p017 to p018), 600 sixes from 600 throws (Assignment 1).

### Poisson (lecture 13, ppt3 p019 to p028)

Models counts of rare events in a fixed interval. Parameter lambda = mean count.

```
pmf         P(X = x) = e^(-lambda) lambda^x / x!,     x = 0, 1, 2, ...
mean        E(X) = lambda
variance    Var(X) = lambda                          mean equals variance, a signature
```

Poisson as the limit of binomial (ppt3 p022): n indefinitely large, p indefinitely small,
n p approaches lambda. Approximation used for large n and small p:

```
C(n, x) p^x q^(n-x)  ~=  e^(-lambda) lambda^x / x!  with lambda = n p
```

Sum of independent Poissons is Poisson with lambda summed. Worked in the corpus: lambda
from P(X=1) = 0.2 P(X=2) (ppt3 p025), telephone calls at 2 per minute (ppt3 p026), life
insurance 5000 men aged 42 (ppt3 p027).

---

## G. Continuous distributions

### Uniform on (a, b) (lecture 14, ppt4 p001 to p006)

```
pdf         f(x) = 1 / (b - a),        a <= x <= b
mean        (a + b) / 2
variance    (b - a)^2 / 12
cdf         F(x) = 0 below a,  (x - a)/(b - a) between,  1 above b
```

Constant density means probability is proportional to interval length.

### Normal (lecture 15, ppt4 p007 to p037)

```
pdf         f(x) = 1/(sigma sqrt(2 pi)) * exp( -(x - mu)^2 / (2 sigma^2) )
notation    X ~ N(mu, sigma^2)
standardise Z = (X - mu) / sigma,       Z ~ N(0, 1)
probabilities  P(a < X < b) = F(b) - F(a) = Phi((b-mu)/sigma) - Phi((a-mu)/sigma)
inverse        X = mu + Z sigma,   used to find X given a probability
```

Symmetry facts the table relies on (ppt4 p027):

```
Phi(-z) = 1 - Phi(z)
P(Z > z) = 1 - Phi(z)
```

Density is bell shaped and symmetric about mu, mean = median = mode = mu, the two tails
approach zero but never touch. Changing mu shifts the curve, changing sigma widens it
(ppt4 p010 to p011). Useful landmarks: 68.3 percent within 1 sigma, 95.4 within 2 sigma,
99.7 within 3 sigma.

Worked in the corpus: Z = 2.0 for X = 200 with mu = 100 and sigma = 50 (ppt4 p017),
P(X < 8.6) with mu = 8, sigma = 5 giving Z = 0.12 and F = 0.5478 (ppt4 p029 to p031),
upper tail P(X > 8.6) = 0.4522 (ppt4 p032 to p033), and the inverse problem of finding
the 20 percent lower tail value (ppt4 p034 to p037).

### Exponential (lecture 16, ppt4 p038 to p043)

Models waiting time between arrivals, with arrival rate lambda.

```
pdf         f(t) = lambda e^(-lambda t),      t > 0
mean        E(T) = 1 / lambda                 the pdf parameter is a rate, the mean is its reciprocal
variance    Var(T) = 1 / lambda^2
tail        P(T > t) = e^(-lambda t)
memoryless  P(T > s + t | T > s) = P(T > t)
```

The reciprocal relation between rate lambda and mean 1/lambda is the single most common
place to lose a mark. The course also uses the mean-first form with pdf
f(t) = (1/mu) e^(-t/mu). Check which parameter the question hands you before substituting.

Worked in the corpus: customers arriving at 15 per hour (ppt4 p042 to p043), and the
Assignment 1 question with f(x) = x e^(-x/3)/9 asking P(X > 12), solved through the tail
identity P(X > x) = e^(-x/3)(1 + x/3) giving 5e^(-4) = 0.0916.

---

## H. Sampling, standard error, central limit theorem (lectures 17 to 18, clt deck)

```
Parameter       a number describing a population, mu, sigma, p
Statistic       a number computed from a sample, Xbar, S, p-hat
Standard error  sd of the sampling distribution of a statistic
SE of the mean  sigma_Xbar = sigma / sqrt(n)
SE estimate     S / sqrt(n), used with the sample sd
SE of a share   sqrt( p(1-p) / n )
```

Central limit theorem (clt deck p007 to p008):

```
For a population with mean mu and sd sigma, for n large enough (the deck uses n >= 30),
Xbar is approximately normal:   Xbar ~ N( mu, sigma^2 / n )
so                              Z = (Xbar - mu) / (sigma / sqrt(n))   is approx N(0,1)
For a sum:                      sum of n draws ~ approx N( n mu, n sigma^2 )
```

Two conditions often tested:

1. If the population itself is normal, then Xbar is exactly normal for every n, not
   approximately.
2. Increasing n shrinks the standard error by sqrt(n), so quadrupling n halves the spread
   of Xbar. This is the answer to "how large a sample" style questions.

Worked in the corpus: lightbulb lifespan standard error (clt deck p005), bank ATM wait
times with n = 36 (p011 to p012), impurity in a chemical batch, mu = 4.0, sigma = 1.5,
n = 50 (p013 to p014), skewed LED lifespans, mu = 50000 (p015 to p016), machine life
mu = 7, sigma = 1 (p017 to p018).

---

## I. Theory of estimation (lectures 19 to 21, ppt5, lms-theory p001 to p030)

```
Estimator    a rule, it is a random variable because it depends on the sample
Estimate     the number you get once data is plugged in
```

Point versus interval estimation (ppt5 p005 to p007):

```
Point      one value, for example Xbar for mu, S^2 for sigma^2, p-hat for p
Interval   a range with a stated confidence level, for example Xbar +- margin
```

Characteristics of a good estimator (ppt5 p008 to p014):

```
Unbiased       E(theta-hat) = theta                          correct on average
Consistent     theta-hat converges in probability to theta as n grows
               sufficient condition: E(T_n) -> theta  and  Var(T_n) -> 0
Efficient      among unbiased estimators, the one with the smallest variance
               relative efficiency of T1 against T2 = Var(T2)/Var(T1)
Sufficient     it uses all the information about theta present in the sample
```

Mean squared error decomposition, the honest comparison when bias is allowed:

```
MSE(theta-hat) = Var(theta-hat) + [Bias(theta-hat)]^2
```

Standard unbiased results used in every numerical:

```
Xbar estimates mu          unbiased, Var = sigma^2 / n
S^2 = sum (Xi - Xbar)^2 / (n - 1)   estimates sigma^2, unbiased, the n-1 matters
p-hat = X / n             estimates p, unbiased, Var = p(1-p)/n
```

Consistency argument to reproduce on demand (ppt5 p012, lss deck p013): Xbar has
E(Xbar) = mu for every n, and Var(Xbar) = sigma^2/n, which goes to 0, so both sufficient
conditions hold and Xbar is consistent for mu.

The estimator-comparison question is the standard 6 to 8 mark question of this block.
Layout that scores: state which estimator is unbiased, solve for the constant that makes
the third one unbiased, then compute variances and name the most efficient. Worked fully
at ppt5 p015 to p021 and again at lms-theory p017 to p022.

---

## J. Named out-of-scope formula, for completeness

Confidence interval for a mean with sigma known (lecture 25 and 27, ETE only, but the
concept of interval estimation is named in MTE lecture 19):

```
Xbar +- z(alpha/2) * sigma / sqrt(n)
z values: 90 percent -> 1.645, 95 percent -> 1.960, 99 percent -> 2.576
```

Do not spend MTE revision time on the confidence interval mechanics of lms-theory
p031 to p039, on MLE (lms-maximum-likelihood), or on method of moments
(lms-method-of-moments). They are formally out of scope for the mid term.
