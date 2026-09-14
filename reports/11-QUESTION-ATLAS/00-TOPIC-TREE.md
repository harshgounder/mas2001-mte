# MTE topic tree, full detail

Built 14 September 2026 from the full read of every slide (348 pages) and every question
(112 items). Scope: MTE lectures 1 to 21 only.

Legend:

```
  [+]  taught on slides AND used by questions, syllabus-named
  [~]  used by questions, sits inside the topic, NOT named in the MTE syllabus list
  [!!] used by questions but taught NOWHERE on any slide (hidden, dangerous)
  [-]  syllabus-named, no question uses it
```

## 1. Introduction of the course [-]

- course structure, credits, assessment weights (30 MTE, 30 CWS, 40 ETE)
- references list
- no questions exist here

## 2. Basic terminology and concepts of probability

- statistics: definition, scope, limitations
  - [+] numerical vs non-numerical statements
  - [+] misrepresentation / biased sampling example
- random experiment, outcome, sample space, event
  - [+] finite spaces: coin, die, two coins, two dice
  - [~] structured outcome coding of an experiment (tournament 1324)
  - [~] ordered vs unordered outcome spaces (dice pairs, 36 outcomes)
- set theory relations
  - [+] complement, union, intersection, null event, mutually exclusive, Venn diagrams
- counting
  - [+] permutations P(n,r), combinations C(n,r), repeated-item permutations
  - [~] combinations as the counting engine inside probability questions
- probability axioms
  - [+] P(S)=1, P(A)>=0, countable additivity; favourable/total
  - [+] addition rule with and without overlap; complement rule
  - [~] "at least" via complement, with a disjointness check first
- conditional probability
  - [+] definition and renormalization
  - [~] conditional probability inside a continuous model
- independence of events
  - [+] P(A n B) = P(A)P(B); mutual independence of n events
  - [~] independence as a modeling assumption
- Bayes' theorem [-]
  - appears only as an MCQ distractor, never taught, never needed

## 3. Random variables (discrete and continuous)

- definition: function from sample space to reals
  - [~] indicator-style counting rv (heads, defectives)
  - [~] transformed rv: Y = X + 4, h(X) revenue, M = max of two dice
- Bernoulli rv [+]
- discrete: finite or countably infinite
  - [~] countably infinite case (geometric N)
- continuous: intervals, P(X = c) = 0
  - [~] zero probability is not impossibility
- support identification [~]

## 4. pmf/pdf and cdf

- discrete
  - [+] p(x)>=0, sum=1
  - [~] finding k by normalization (15K=1; 10k^2+9k=1)
  - [+] cdf step function, nondecreasing
  - [~] cdf construction per interval
  - [~] pmf from cdf: f(n) = F(n) - F(n-1)
  - [~] interval probability via cdf: F(b) - F(a-1)
  - [~] nondecreasing proof
- continuous
  - [+] f>=0, integral = 1; area interpretation; P(X=c)=0
  - [~] normalizing a non-pdf: f(x)/k
  - [+] cdf integral form; P(X>a)=1-F(a); P(a<=X<=b)=F(b)-F(a); F'(x)=f(x)
  - [~] mixed piecewise pdf; triangular pdf; |x| pdf
  - [~] improper integrals and tail behaviour (Pareto, exponential)

## 5. Expectation

- [+] E(X) = sum x p(x); location parameter
- [+] E[h(X)] definition
- [+] properties E[c]=c, E[cX]=cE(X), E[aX+b] (proved)
- [+] continuous integral forms
- [~] E(X^2) as standard second moment
- [~] E(2X+1)^2 via the laws
- [~] expected revenue via piecewise h(X)
- [~] E(X) with convergence conditions (Pareto k>1)

## 6. Expectation and independent random variables

- variance machinery
  - [+] Var(X)=E[(X-mu)^2], shortcut E(X^2)-[E(X)]^2
  - [+] Var(c)=0, Var(cX)=c^2Var(X), V(aX+b)=a^2V(X)
  - [~] Var from the pdf via two integrals
- INDEPENDENT RANDOM VARIABLES [!!]
  - [!!] E(XY) = E(X)E(Y) under independence, taught nowhere
  - [!!] Var(X+Y) = Var(X) + Var(Y) under independence, taught nowhere
  - [!!] Var(X-Y) case
  - [!!] already graded in assignment 1 Q5 (dice sum, Var = 35/6)
  - [!!] implicitly required by every CLT question
- linearity E(X+Y)=E(X)+E(Y) without independence [+], the contrast is the trap

## 7. Chebyshev's inequality (no slides anywhere)

- [!!] P(|X-mu| >= k sigma) <= 1/k^2
- [!!] complement form P(|X-mu| < k sigma) >= 1 - 1/k^2
- [!!] distribution-free condition (finite mean and variance)
- [!!] solving k from interval limits
- [!!] tail vs complement form (1/9 vs 8/9 trap)
- [!!] applying to a sum of rvs (find Var first, dice 35/54)
- [!!] comparing bound with actual probability
- [!!] reverse direction from a proportion to an interval
- graded 5 times already (2 MCQ, 2 short, 1 application)

## 8. Binomial

- [+] setup conditions; pmf; X~B(n,p); mean np; var npq
- [~] complement tails P(X>=k)
- [~] exact hand computation of C(n,x) and powers
- [~] ratio condition to recover p (P(X=5)=2P(X=4) -> p=5/8)
- [~] expected count N*P over repeats
- [~] physical die framed as binomial
- [~] binomial to Poisson limiting logic

## 9. Poisson

- [+] rare-event model; pmf; mean = var = lambda; binomial limit
- [~] lambda from probability ratio (lambda=10 case)
- [~] rate conversion and time-window scaling
- [~] "demand rejected" = P(X >= capacity+1)
- [~] "no event" = e^-lambda
- [~] Poisson approximation to binomial (np small)
- [~] compound process: Poisson arrivals + binomial over minutes (32e^-10)
- [~] additivity of independent Poissons (MCQ only)
- [~] tail sums

## 10. Uniform

- [+] density 1/(b-a); mean (a+b)/2; var (b-a)^2/12
- [~] length-ratio shortcut
- [~] partial-outside intervals clipping to the support
- [~] |X| and |X-2| absolute-value intervals
- [~] inverse problems (find K from P(X>K)=1/3)
- [~] rounding error application

## 11. Normal

- [+] shape, symmetry, parameters; standardization; general procedure; negative-z reflection
- [!!] TWO table conventions in the course, both appear (cumulative table ppt4 p022,
  area-from-0 table ppt4 p023-025); questions give phi() as area-from-0. Mixing loses marks
- [~] interval probability with mixed signs; upper tail 1-F(z)
- [~] inverse direction: z from table then X = mu + z sigma
- [!!] two-unknown system from two percentile facts (mu=37.5, sigma=28.2, cutoff 30.43)
- [!!] 68.27 / 95.45 / 99.73 landmarks: asked in MCQ Q11, taught nowhere
- [~] expected count N*P
- [~] "estimate the number likely" phrasing

## 12. Exponential

- [+] f(t)=lambda e^-lambda t; mean 1/lambda; var 1/lambda^2; cdf 1-e^-lambda t
- [+] interarrival modeling; unit conversion
- [!!] memoryless property: used in MCQ and Section C, never defined on any slide
- [~] conditional probability with exponentials P(X<1|X<2)
- [~] mean to lambda conversion both directions
- [~] survival function form
- [~] wait questions with rate conversion

## 13. Sampling concepts and standard error

- [+] population vs sample; parameters vs statistics; simple random sampling
- [+] SE = sigma/sqrt(n)
- [~] SE scaling law

## 14. Central limit theorem

- [+] sample means normal for n>=30; normal population any n; n<30 non-normal fails
- [~] z transform with SE denominator
- [~] skewed-population applications
- [~] two-sided interval with SE (-0.94 errata zone)
- [~] exact table selections
- [~] "average of n between a and b" template vs plain normal
- [~] exact-normal fallback for small n

## 15. Theory of estimation basics

- [+] parameter, statistic, estimator, estimate, spaces; point vs interval; CI structure
- [~] point estimate from raw data (205 ms)
- [~] proportion estimation (0.93)
- [~] CI with z_{alpha/2} (battery (7.81, 8.99)), lecture 25 machinery inside lect 19-21

## 16. Characteristics of a good estimator

- [+] unbiasedness; consistency with two sufficient conditions; efficiency; sufficiency
- [~] Neyman-Fisher factorization in action (Poisson, exponential)
- [~] constant-to-force-unbiasedness (coefficient sum = 1)
- [~] linear combination variance sigma^2 sum ai^2
- [~] best estimator protocol: filter unbiased first, then min variance (T4 trap)
- [~] consistency of a specific estimator via the two conditions

## Cross-cutting skills (used everywhere, no single home)

- [!!] complement discipline for "at least", "no", "more than", "rejected"
- [!!] table conventions and selection discipline
- [!!] unit conversion inside applied stories
- [!!] exact decimal arithmetic with powers (0.9^10, 0.9^12, e^-2.5)
- [!!] probability-ratio parameter recovery (binomial and Poisson)
- [!!] expected count = N * probability
- [!!] piecewise function handling
- [!!] absolute-value inequalities to intervals
- [~] structured enumeration without listing everything

## The hidden list, ranked by bite

1. independence rules of random variables: graded already, never taught
2. Chebyshev entire topic: graded 5 times, zero slides
3. memoryless property
4. 68/95/99.7 landmarks
5. the two table conventions
