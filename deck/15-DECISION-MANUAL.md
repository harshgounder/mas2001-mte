# 15 DECISION MANUAL: faced with X, do Y

Built 17 Sep 2026. A study lookup organised as a working 36-category taxonomy:
16 categories observed in the two supplied MTE papers and 20 recall-gap categories drawn
from the wider course material. The source set contains nine exam papers in total, two MTE
and seven ETE. The taxonomy is a study aid, not an exhaustive model of a future paper.

```
   TRIGGER    the phrase or structure that tells you which shape it is
   DO         the exact first move
   STEPS      the full solve path
   IF/THEN    the sub-shape branches, to the point of "if this, then that"
   VALUES     the constants that recur
   TRAP       the mistake the setter is fishing for
   MUTS       the mutations seen, and what each changes
```

Read it top to bottom once, then use it as a lookup while drilling. This is the file that
turns pattern knowledge into marks.

═══════════════════════════════════════════════════════════════════════════════
HOW TO USE IT IN THE EXAM (the 60-second triage)
═══════════════════════════════════════════════════════════════════════════════

```
   STEP 1  read the question, find the DISTRIBUTION or the domain word
   STEP 2  find the ASK verb (find P / find k / find mean / test / compare)
   STEP 3  jump to that shape below, follow DO
   STEP 4  check the IF/THEN branches before you write the final line
```

```
   domain word heard        ->  family
   coin / defective / n trials / "no. of"    ->  Binomial
   per minute / per hour / arrivals / rare   ->  Poisson
   telephone / waiting time / lifetime / rate ->  Exponential
   interval (a,b) / equally likely / at random ->  Uniform
   bell / mean and sd given / percentage      ->  Normal
   mean mu and variance given, no distribution ->  Chebyshev
   f(x) / cdf / pmf / density                 ->  RV/pdf-cdf
   estimator / unbiased / sufficient / CI     ->  Estimation
   "average of n / sample of n"               ->  CLT
   "define / is said to be"                   ->  Definition
```

═══════════════════════════════════════════════════════════════════════════════
PART 1: THE EIGHT MTE FAMILIES (highest value)
═══════════════════════════════════════════════════════════════════════════════

-------------------------------------------------------------------------------
F1. BINOMIAL
-------------------------------------------------------------------------------

```
 TRIGGER  fixed number of trials n, two outcomes, constant p, independent trials.
          phrases: "defective", "coins", "no. of successes", "n = 50", "out of n".
```

SUB-SHAPES:

```
 F1.1  point  P(X = k)
   DO     C(n,k) p^k q^(n-k).  that is it.
   IF the question gives p as a fraction (1/10) THEN keep it exact until the final decimal
   IF it gives "20 percent" THEN p = 0.20, q = 0.80
   IF k = 0 THEN p^0 = 1, so just q^n   (the "none defective" case)
   VALUES pens B(12,0.1): P(0)=0.2824  P(2)=0.2301

 F1.2  tail  P(X >= k) or "at least" / "at most"
   DO     translate the wording first, then use either a short direct sum or a complement
   IF "at least 1"    THEN P(X>=1) = 1 - P(X=0) = 1 - q^n
   IF "at least 2"    THEN 1 - P(X=0) - P(X=1)   (two terms)
   IF "at most k"     THEN P(X<=k), sum P(0)..P(k) OR 1 - P(>=k+1)
   VALUES B(15,0.08): P(>=1) = 1 - 0.92^15 = 0.7137

 F1.3  moments  E(X) = np, Var(X) = npq, sd = sqrt(npq)
   DO     read n and p, plug. q = 1-p.
   IF they give mean and variance and ask for the pmf THEN solve np = m, npq = v ->
          p = 1 - v/m, n = m/p.  (this recovers the distribution from moments)
   VALUES B(180,1/3): E = 60.  B(50,0.4): E = 20, Var = 12.

 F1.4  parameter recovery
   DO     set up the stated probability relation, solve for p
   IF "P(X=5) = 2 P(X=4)"  THEN P(X=5)/P(X=4) = ((n-4)/5)(p/q) = 2
          -> p/q = 10/(n-4). For n=10, p/q=5/3 and p=5/8.
   TRAP   forgetting the combination ratio C(n,5)/C(n,4) = (n-4)/5

 F1.5  formula MCQ  "the pmf of binomial is ..."
   DO     match the form C(n,x) p^x q^(n-x).  eliminate anything missing C(n,x) or with the
          wrong exponents.
```

MUTATIONS SEEN:
```
   M0 reskin      pens -> bulbs -> patients   (numbers change, shape identical)
   M0 value       p 1/10 -> 0.20 -> 1/3,  n 12 -> 180 -> 50 -> 15
   M3 retarget    P(=k) -> P(>=k) -> E/Var   (same setup, new ask)
   M4 compose     binomial inside a Poisson window (see F2.5)
```

-------------------------------------------------------------------------------
F2. POISSON
-------------------------------------------------------------------------------

```
 TRIGGER  count of rare events in an interval. phrases: "per minute", "per hour",
          "arrivals", "calls", "typos per page", "defects per unit", "0.005%".
```

SUB-SHAPES:

```
 F2.1  point  P(X = k) = e^-l l^k / k!
   DO     find lambda for THE interval asked, then plug.
   IF the rate is per minute but the ask is per 5 minutes THEN multiply lambda by 5 first
   IF k = 0 THEN e^-l   (the "none" case)
   VALUES lambda=3: P(0) = e^-3 = 0.0498

 F2.2  tail  P(X >= k) or P(X > k)
   DO     complement from 0. P(X>=4) = 1 - P(0) - P(1) - P(2) - P(3)
   IF capacity is c and rejection starts only after capacity is filled THEN use P(X>=c+1);
          state the threshold from the wording before calculating
   VALUES lambda=2: P(X>=4) = 0.1429 ; the capacity story gives 0.2424 at lambda=2.5

 F2.3  parameter recovery
   DO     set the given probability relation, solve for lambda
   IF "P(X=1) = 0.2 P(X=2)"  THEN e^-l l = 0.2(e^-l l^2/2) -> 1 = 0.1l -> l = 10
   IF "P(X=2) = 9 P(X=4) + 90 P(X=6)" THEN divide by e^-l l^2/2:
          1 = 3l^2/4 + l^4/4, so l^4 + 3l^2 - 4 = 0 and the valid rate is l = 1
   TRAP   forgetting to divide out e^-l, which is common to both sides

 F2.4  rate/window scaling
   DO     lambda_new = rate x window length. This is the single most common Poisson error.
   VALUES 2/min -> 5 min = 10 ; 15/hr -> per 1 hr = 15 ; 5/day -> 2.5/day = 2.5

 F2.5  nesting (composite)
   DO     define the event in one interval, find its Poisson probability p, then count how
          many independent intervals satisfy that event with a binomial model
   IF calls arrive at 2/min and the ask is "exactly two calls in each of five minutes"
          THEN p=P(Poisson(2)=2)=2e^-2 and M~B(5,p); P(M=5)=p^5
   VALUES (2e^-2)^5 = 32e^-10 = 0.00145
   TRAP   mixing the two stages' parameters
```

MUTATIONS SEEN:
```
   M0 reskin      calls -> typos -> accidents -> insurance claims
   M0 value       lambda 1, 2, 3, 10, 2.5
   M2 window      per minute <-> per 5 minutes <-> per hour  (lambda rescale)
   M4 compose     Poisson then binomial
```

-------------------------------------------------------------------------------
F3. EXPONENTIAL
-------------------------------------------------------------------------------

```
 TRIGGER  waiting time or lifetime between events. phrases: "telephone conversation",
          "time to repair", "shelf life", "interarrival", "parameter 1/4".
```

SUB-SHAPES:

```
 F3.1  setup  f(x) = l e^(-lx), F(x) = 1 - e^(-lx), S(x) = e^(-lx)
   DO     decide which form: pdf for density asks, F for "less than", S for "more than"
   IF given "mean = 3" THEN lambda = 1/3   (mean = 1/lambda)
   IF given "parameter 1/4" THEN lambda = 1/4, mean = 4
   TRAP   the parameter IS lambda; the mean is its reciprocal. swapping these is the #1 error.

 F3.2  point  P(X < a) = 1 - e^(-la) ;  P(X > a) = e^(-la)
   DO     pick F or S by the inequality direction, plug.
   VALUES mean 3: P(X>1) = e^(-1/3) = 0.7165 ; P(X<3) = 1 - e^-1 = 0.6321

 F3.3  interval  P(a < X < b) = e^(-la) - e^(-lb)
   DO     S(a) - S(b), equivalently F(b) - F(a)
   VALUES mean 4: P(7<X<12) = e^(-7/4) - e^(-12/4)

 F3.4  conditional  P(X > a+b | X > a) = P(X > b)   (memoryless)
   DO     for exponential, the condition drops out. P(X>s+t|X>s) = e^(-lt)
   IF NOT memoryless (a general continuous rv) THEN use P(A|B) = P(A n B)/P(B) with S ratios
   VALUES P(X<1|X<2) for mean 2 is (1-e^-0.5)/(1-e^-1) = 0.6225; this is
          a nested lower-tail event, not a memoryless upper-tail event
   TRAP   trying to compute the general conditional when memoryless applies

 F3.5  moments  E = 1/lambda, Var = 1/lambda^2
   DO     invert for mean, square-invert for variance
   IF "mean = 2, find sd" THEN sd = mean = 2 (exponential has equal mean and sd, sd = 1/lambda)
```

MUTATIONS SEEN:
```
   M0 reskin      telephone -> repair time -> shelf life -> machine
   M0 value       mean 5 -> 6 -> 4 -> 3 -> 1/4   (the most-mutated value in the corpus)
   M3 retarget    P(X>a) -> interval -> conditional -> mean
   M2 memoryless  condition given <-> not given
```

-------------------------------------------------------------------------------
F4. UNIFORM
-------------------------------------------------------------------------------

```
 TRIGGER  equally likely over an interval. phrases: "uniformly distributed between a and b",
          "at random in [a,b]", "U(-1,1)", "arrives between 9:00 and 9:30".
```

SUB-SHAPES:

```
 F4.1  pdf  f(x) = 1/(b-a) on [a,b], 0 outside
   DO     write the support exactly; every later step must respect it
   IF "a < x < b" is open vs closed THEN for continuous it does not matter

 F4.2  point / interval  P(c < X < d) = (d - c)/(b - a)   (length ratio)
   DO     clip [c,d] to [a,b] first, THEN take the length ratio
   VALUES U(2,6): P(2<X<5) = 3/4 = 0.75 ; U(0,8): P(a<X<5) via ratio
   TRAP   forgetting to clip; using the raw length when the interval pokes outside the support

 F4.3  absolute-value to interval  P(|X - c| < d) = P(c-d < X < c+d)
   DO     expand the modulus to an interval, clip, ratio
   IF the centre is E(X) THEN c = (a+b)/2
   VALUES for X~U(0,8), P(|X-3|>2) -> P(X<1 or X>5) -> (1+3)/8 = 1/2

 F4.4  moments  E = (a+b)/2, Var = (b-a)^2/12
   DO     plug a and b.
   IF given mean and variance, solve for a and b THEN two equations:
          a+b = 2m ; b-a = sqrt(12 v).  solve.
   VALUES U(0,5): E=2.5 ; (a,b) with mean 1 and variance 4/3 -> a=-1, b=3

 F4.5  inverse  find a so that P(X > c) = p
   DO     set up the ratio equal to p, solve for the unknown bound
   VALUES P(X>1) = 1/3 over (-a,a) -> (a-1)/(2a)=1/3 -> a=3

 F4.6  Chebyshev on uniform  (composite, see F5.4)
```

MUTATIONS SEEN:
```
   M0 reskin      interval (2,6) -> (0,5) -> (-1,1) -> (-3,3) -> (a,b)
   M3 retarget    point -> interval -> |X| -> moments -> inverse
   M4 compose     uniform + Chebyshev (bound vs actual)
```

-------------------------------------------------------------------------------
F5. CHEBYSHEV  (recurs in the supplied papers)
-------------------------------------------------------------------------------

```
 TRIGGER  "Chebyshev's inequality", OR mean and variance given with NO distribution named.
```

THE THREE FORMS (memorise all three):

```
   1) P(|X - mu| >= k sigma) <= 1/k^2        (tail form, upper bound)
   2) P(|X - mu| <  k sigma) >= 1 - 1/k^2    (within form, lower bound)
   3) with k in raw units: P(|X-mu| >= k) <= sigma^2 / k^2
```

SUB-SHAPES:

```
 F5.1  within-k  "at least what fraction lies within k sigma"
   DO     form 2. 1 - 1/k^2
   VALUES k=2 -> 3/4 ; k=3 -> 8/9 ; k=4 -> 15/16
   TRAP   giving 1/k^2 (the tail) when they asked "within"

 F5.2  find-c  "find c such that P(|X-mu| >= c) <= p"
   DO     form 3. sigma^2/c^2 = p -> c = sigma/sqrt(p)
   VALUES mu=10 var=4, p=0.04 -> c = 2/0.2 = 10
   TRAP   using form 1 (needs k sigma) when the ask is in raw units c

 F5.3  inverse  "P(-2 < X < 8) >= 21/25, find E(X) and Var(X)"
   DO     recognise (-2,8) is centred: mean = midpoint = 3. half-width = 5 = k sigma.
          set 1 - 1/k^2 = 21/25 -> 1/k^2 = 4/25 -> k = 2.5. then sigma = 5/2.5 = 2.
   VALUES mean 3, sigma 2, so Var 4
   TRAP   not seeing the midpoint IS the mean

 F5.4  bound vs actual  (composite with a named distribution)
   DO     compute BOTH: the Chebyshev bound (form 1 or 3) AND the exact probability from
          the distribution's own formula. present the bound first, then the actual.
   VALUES U(-1,1), k=2: bound = 1/4, actual = 0 (no point is 2 sd from the mean)
   TRAP   reporting only one of the two; the question usually asks for both

 F5.5  applicability  "which statements are/are not Chebyshev's inequality"
   DO     check the FORM: must be 1/k^2 (or sigma^2/k^2), must have |X-mu|, must be an
          inequality with the correct direction.
   TRAP   a sign or direction flip in one option
```

MUTATIONS SEEN:
```
   M0 value       k 2 -> 3 -> 4 ; sigma 2 -> 3 ; interval (-1,3) -> (-1,1)
   M1 invert      given k find bound <-> given bound find c/k
   M3 retarget    within <-> tail <-> inverse <-> bound-vs-actual
   M4 compose     Chebyshev on a SUM (find Var first) ; Chebyshev + named distribution
```

-------------------------------------------------------------------------------
F6. NORMAL
-------------------------------------------------------------------------------

```
 TRIGGER  "normally distributed", "mean and standard deviation", "N(mu, sigma^2)",
          percentage-of-items, bell curve, "standard normal variate".
```

THE FIRST MOVE, ALWAYS:

```
   Z = (X - mu) / sigma        (for a single X)
   Z = (Xbar - mu) / (sigma/sqrt(n))   (for a SAMPLE MEAN, see F9)
```

SUB-SHAPES:

```
 F6.1  point / tail  P(X < a), P(X > a)
   DO     standardise, then read the table.
   IF the ask is "greater than" THEN P(X>a) = 1 - Phi(z)
   IF z is negative THEN use symmetry: Phi(-z) = 1 - Phi(z)
   VALUES N(50,100): P(X<65) = Phi(1.5) = 0.9332 ; P(X>35) = Phi(1.5) = 0.9332 (symmetry)

 F6.2  interval  P(a < X < b)
   DO     Phi(z_b) - Phi(z_a)
   EXAMPLE  for X ~ N(0,1): P(-0.4 < X < 0.6) = Phi(0.6) - Phi(-0.4) = 0.7257 - 0.3446 = 0.3811

 F6.3  inverse  "find x such that P(X < x) = 0.90"
   DO     find z from the table (z = 1.2816 for 0.90), then UN-STANDARDISE: x = mu + z sigma
   VALUES mu=50 sigma=10 -> x = 62.82
   TRAP   stopping at z and forgetting to convert back to X units (loses the last mark)

 F6.4  two-unknown  "7% under 35 and 89% under 63, find mean and sd"
   DO     two equations. z1 = (35-mu)/sigma, z2 = (63-mu)/sigma. from the table z1 = -1.4758,
          z2 = 1.2265. subtract to get 28 = (z2-z1) sigma.
   VALUES sigma = 10.36, mu = 50.29
   TRAP   sign of the lower-tail z

 F6.5  expected count  N x P
   DO     compute P from the normal, then multiply by the population N.
   IF "how many of 10000 lamps" THEN N = 10000 x P(window)
   VALUES 2000 bulbs, first 800 hours -> N x Phi(z1)
   TRAP   reporting the probability when they asked for a COUNT

 F6.6  landmarks  68.27 / 95.45 / 99.73 percent within 1 / 2 / 3 sigma
   DO     use these when the question is about "roughly what percentage"
   TRAP   using the landmarks when an exact table value is needed

 F6.7  standard normal properties MCQ  mean, variance, symmetry
   DO     N(0,1): mean 0, variance 1, symmetric, total area 1. right of mean = 50%.
```

MUTATIONS SEEN:
```
   M0 value       mu/sigma: 8/5, 50/10, 20/10, 45/..., N(2.6, 34.5) means mean 2.6 and
                  VARIANCE 34.5, so sigma = sqrt(34.5) = 5.87
   M1 invert      P->x  <->  x->P
   M2 two-unknown one unknown (given percentile) <-> two unknowns
   M3 retarget    point -> tail -> interval -> inverse -> count
```

-------------------------------------------------------------------------------
F7. RV / PDF / CDF
-------------------------------------------------------------------------------

```
 TRIGGER  f(x) given, or "probability density function", or "distribution function", or
          a piecewise definition.
```

SUB-SHAPES:

```
 F7.1  find-param  "f(x) = k g(x) on [a,b], find k"
   DO     integrate g over the support, set k x (integral) = 1, solve for k.
   IF f = 6x(1-x) on (0,1) THEN the integral is already 1, so f is already normalised (k = 1)
   IF f = kx^3(4-x)^2 on (0,4) THEN integrate x^3(4-x)^2 = 1024/15, so k = 15/1024
   IF f = ax^2 + bx on (0,1) with mean 0.5 THEN TWO equations: total mass = 1 AND E(X) = 0.5
   TRAP   integrating outside the stated support

 F7.2  moments from a density  E(X) = int x f(x) dx ; E(X^2) = int x^2 f(x) dx
   DO     two separate integrals, then Var = E(X^2) - (E(X))^2
   IF they ask E and Var THEN do both integrals, do not shortcut
   TRAP   computing E(X^2) as (E(X))^2

 F7.3  cdf from pdf  F(x) = int_{-inf}^{x} f
   DO     integrate f from the lower support bound to x, piecewise
   IF f has a break THEN the cdf is piecewise too; write each piece

 F7.4  pdf from cdf  differentiate
   DO     f(x) = F'(x) on the support
   TRAP   forgetting to define f = 0 outside the support

 F7.5  probability from cdf  P(a < X < b) = F(b) - F(a)   (continuous)
 F7.6  probability from discrete cdf  P(a <= X <= b) = F(b) - F(a-1)  (watch the a-1)
 F7.7  pmf table + cdf + transformed expectation (composite)
   DO     build F by cumulative sum, then answer each part
   VALUES values -3,6,9 with probs 1/6,1/2,1/3: E = 11/2, E(X^2) = 93/2,
          E(2X+1)^2 = E(4X^2+4X+1) = 4(93/2) + 4(11/2) + 1 = 186 + 22 + 1 = 209
   TRAP   expanding (2X+1)^2 wrongly; forgetting E(1) = 1

 F7.8  formula MCQ  "int_{-inf}^{inf} f dx = ?"
   DO     = 1 (total mass axiom).
```

MUTATIONS SEEN:
```
   M0 value       kx^3(4-x)^2, 6x(1-x), 15k=1, 9k+10k^2=1, ax^2+bx
   M1 invert      pdf->cdf <-> cdf->pdf
   M3 retarget    find-k -> moments -> probability -> cdf
```

-------------------------------------------------------------------------------
F8. ESTIMATION
-------------------------------------------------------------------------------

```
 TRIGGER  "estimator", "unbiased", "efficient", "consistent", "sufficient",
          "confidence interval", "maximum likelihood".
```

THE PROTOCOL (memorise this order):

```
   1. UNBIASED?   E(estimator) = parameter?  If not, ELIMINATE it.
   2. EFFICIENT?  among the remaining unbiased ones, smallest variance.
   3. CONSISTENT? check both conditions.
   4. SUFFICIENT? check the definition / Neyman-Fisher.
```

SUB-SHAPES:

```
 F8.1  unbiasedness  "is T an unbiased estimator of theta?"
   DO     E(T) = theta?  compute E(T) using E(Xi) = theta and linearity.
   IF T = Xbar THEN unbiased.  IF T = (X1+X2)/2 THEN unbiased.
   IF T = (X1+X2+X3)/2 THEN E = 3theta/2, BIASED.
   VALUES the T1..T4 set: T1 sigma^2, T2 sigma^2/2, T3 sigma^2/3, T4 biased
   TRAP   picking T4 on variance, forgetting it is biased -> efficiency excludes it

 F8.2  efficiency comparison
   DO     among UNBIASED estimators only, compare variances. smallest wins.
   IF a biased one has the smallest variance THEN it still LOSES (efficiency needs unbiasedness)
   IF the question mentions MLE THEN also check the Cramer-Rao bound (variance >= 1/(n I))

 F8.3  consistency  "show T is consistent"
   DO     two conditions: (i) E(T) -> theta as n -> inf, (ii) Var(T) -> 0 as n -> inf.
   IF T is the sample mean THEN both hold (Var = sigma^2/n -> 0).
   IF T is a FIXED-size statistic (T3 from 3 obs) THEN variance never -> 0, NOT consistent.
   TRAP   asserting consistency from unbiasedness alone

 F8.4  sufficiency  "is the statistic sufficient?"
   DO     definition: T is sufficient if the conditional distribution of the sample given T
          does not depend on theta. OR use Neyman-Fisher factorisation.
   IF the parameter is a Poisson mean THEN Xbar (or sum) is sufficient.
   IF the parameter is an exponential rate THEN sum (or Xbar) is sufficient.
   VALUES Poisson sample mean sufficient; exponential sufficient statistic.

 F8.5  confidence interval (boundary material, outside the stated MTE lectures 1-21)
   DO     Xbar +/- z(alpha/2) sigma/sqrt(n) when sigma is known and the population is normal,
          or as a justified large-sample approximation.
   IF sigma is unknown and the population is normal THEN use t with n-1 df; for a
          non-normal population, justify any large-sample approximation.
   VALUES 95% CI for mean weight from a sample; z=1.96 for 95%
   TRAP   using z when t is required

 F8.6  definition MCQ  "unbiased means ...", "sufficient means ...", "MLE maximizes ..."
   DO     match to the exact textbook phrasing.
   VALUES unbiased: E(estimator) = parameter. sufficient: contains all information about
          the parameter. MLE: maximizes the likelihood function.
```

MUTATIONS SEEN:
```
   M0 reskin      different constants in the T1..T4 set
   M4 compose     unbiased + efficient + consistent in ONE question (the usual MTE form)
   M3 retarget    single property -> all four
```

═══════════════════════════════════════════════════════════════════════════════
PART 2: CLT / SAMPLING (recall-gap family, still drill)
═══════════════════════════════════════════════════════════════════════════════

-------------------------------------------------------------------------------
F9. CLT AND STANDARD ERROR
-------------------------------------------------------------------------------

```
 TRIGGER  "average of n", "sample of n", "standard error", "central limit theorem".
```

SUB-SHAPES:

```
 F9.1  standard error
   DO     SE = sigma / sqrt(n)
   IF n quadruples THEN SE halves (sqrt(4) = 2)
   VALUES sigma=10: n=100 -> 1.0 ; n=25 -> 2.0

 F9.2  CLT probability  (sample mean falls in a range)
   DO     z = (xbar - mu) / (sigma/sqrt(n)), then read the normal table.
   DO NOT use z = (x - mu)/sigma. THE DENOMINATOR IS SE, NOT SIGMA.
   TRAP   using sigma instead of SE, the single most common CLT error

 F9.3  applicability  "when does the CLT hold"
   DO     if the population is normal, Xbar is normal for every n. Otherwise, assess sample
          size together with skewness and tail weight. The course's n>=30 cutoff is a
          classroom heuristic, not a theorem and not a guarantee for every distribution.

 F9.4  sampling distribution  distribution of Xbar
   DO     mean = mu, variance = sigma^2/n.
```

-------------------------------------------------------------------------------
F10. DEFINITION (recall-gap family)
-------------------------------------------------------------------------------

```
 TRIGGER  "define", "is said to be", "which of the following is the ... definition".
   DO     match to the exact course wording. These are pure recall.
   VALUES
     random variable: a function mapping the sample space to the real numbers
     discrete rv: takes countable values
     P(X = exact value) = 0 for a CONTINUOUS rv
     N(0,1): mean 0, variance 1
     pdf integrates to 1
     unbiased: E(estimator) = parameter
```

═══════════════════════════════════════════════════════════════════════════════
PART 3: THE MASTER DECISION TREE (which method when)
═══════════════════════════════════════════════════════════════════════════════

```
                          START: read the question
                                    |
              +---------------------+---------------------+
              |                                           |
        distribution named?                         mean+variance only?
              |                                           |
              v                                           v
     +--------+--------+                          CHEBYSHEV (F5)
     |        |        |                          pick within/tail/inverse
     v        v        v
  discrete  continuous  named-normal
     |        |        |
     +--+     +--+     +-- Normal (F6)
     |  |     |  |
  Binom Pois Unif Exp
  (F1) (F2) (F4) (F3)
     |
     +---- if a COUNT feeds a second stage -> NESTING (F2.5)

  none of the above?
     |
     +-- f(x) given              -> RV/pdf-cdf (F7)
     +-- estimator language      -> Estimation (F8)
     +-- "average of n"          -> CLT (F9)
     +-- "define / is said to be" -> Definition (F10)
```

═══════════════════════════════════════════════════════════════════════════════
PART 4: THE ASK-VERB MAP (one line each)
═══════════════════════════════════════════════════════════════════════════════

```
  "find the probability that"     -> translate the event, then choose point, sum, or tail
  "at least"                       -> often a lower-tail complement, e.g. P(X>=k)=1-P(X<=k-1)
  "at most"                        -> P(X<=k), either sum 0..k or use 1-P(X>=k+1)
  "greater than" / "exceeds"      -> upper tail, 1 - F
  "between a and b"               -> F(b) - F(a)
  "find k" / "find the constant"  -> normalise (integrate = 1) then solve
  "find the value of c"           -> inverse: solve the inequality for the bound
  "find the mean and variance"    -> moments (distribution formula, or integrate)
  "how many ... expected"         -> N x P (a COUNT, not a probability)
  "find x such that P(X<x)=p"     -> INVERSE: table z, then x = mu + z sigma
  "is it unbiased / sufficient"   -> Estimation
  "which of the following"        -> concept/statement MCQ; check form and direction
  "show that"                     -> derive, write every line (it is a proof mark)
  "use Chebyshev's inequality"    -> the bound, and possibly the actual too
```

═══════════════════════════════════════════════════════════════════════════════
PART 5: THE MUTATION LAYER (what a change does)
═══════════════════════════════════════════════════════════════════════════════

```
  M0 RE-SKIN   change numbers, names, units      -> SAME method. no thinking.
  M1 INVERT    swap given and asked              -> NEW method. (x->P becomes P->x)
  M2 RE-COND   flip a structural condition       -> NEW method when the formula changes
               (replacement on/off, n<30 vs n>=30, memoryless on/off)
  M3 RE-TARGET same setup, different ask         -> check if the method differs
               (=k -> >=k -> E/Var -> count)     (usually yes: complement, or integrate)
  M4 COMPOSE   nest two models                   -> do stage 1 fully, feed stage 2
```

WHEN A MUTATION KEEPS THE SAME METHOD:
```
  numbers only, names only, units only, rounding, same formula different story
```
WHEN A MUTATION CHANGES THE METHOD:
```
  forward <-> inverse
  point <-> tail/interval
  unconditional <-> conditional
  single <-> expected count
  independence on <-> off
  one model <-> two models (composite)
  E <-> Var <-> E[h(X)]
```

═══════════════════════════════════════════════════════════════════════════════
PART 6: THE 36-CATEGORY STUDY CHECKLIST (tick each off while drilling)
═══════════════════════════════════════════════════════════════════════════════

IN-MTE (16)  [ ] Chebyshev/concept-mcq  [ ] Chebyshev/inverse-c  [ ] Chebyshev/point
             [ ] Chebyshev/moments  [ ] Poisson/concept-mcq  [ ] Poisson/formula-mcq
             [ ] Poisson/moments  [ ] Binomial/tail  [ ] Exponential/tail
             [ ] Normal/interval  [ ] Estimation/sufficiency  [ ] Estimation/tail
             [ ] RV/pdf-cdf/find-param  [ ] RV/pdf-cdf/formula-mcq  [ ] RV/pdf-cdf/point
             [ ] Uniform/tail

RECALL-GAP (20)  [ ] Binomial/point  [ ] Binomial/moments  [ ] Binomial/formula-mcq
                 [ ] Poisson/point  [ ] Poisson/tail  [ ] Poisson/sufficiency
                 [ ] Exponential/point  [ ] Exponential/sufficiency  [ ] Expectation/point
                 [ ] Uniform/point  [ ] Normal/point  [ ] Normal/tail  [ ] Normal/moments
                 [ ] Normal/find-param  [ ] CLT/point  [ ] Estimation/point
                 [ ] Estimation/moments  [ ] Estimation/formula-mcq
                 [ ] Definition/concept-mcq  [ ] Hypothesis-OUT/point

═══════════════════════════════════════════════════════════════════════════════

This is an "if given X, do Y" study map. Read it once, then test it against the drill. The
mutation layer records changes observed in the supplied material. A future question may make
one change, several changes, or use a form not represented here.
