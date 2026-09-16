# U01 atlas: 2024-25 and 2025-26 MTE papers

Sixteen top-level question blocks, counted by the locked rule that a multi-part block counts
once. Solution schemes are evidence, not extra questions. All sixteen are new exact items
against the batch-1 count; the type verdict says whether each confirms an existing or formerly
hypothetical method node.

## M25-Q01, density normalization MCQ

- **source:** `md/paper-mte-2025-26/p001.md`, question 1.
- **question:** complete $\int_{-\infty}^{\infty}f(x)dx$ for a continuous density.
- **what it is / type / subtype:** definition check; PDF; normalization.
- **knowledge / approach / steps:** total density mass is one; select 1.
- **alternate:** reject other choices by the probability-mass axiom.
- **intent:** test the defining property before calculation.
- **bloom / dok / math_group / solo / gaise:** Remember; 1; A; uni; A.
- **difficulty / task demand:** 1/5; memorization.
- **traps:** confusing density height with total mass.
- **exam_use / verdict:** in scope; NEW exact item, confirms the existing valid-PDF node.
- **verified:** option 2 matches the paper and scheme.

## M25-Q02, Poisson PMF with mean e

- **source:** `md/paper-mte-2025-26/p001.md`, question 2.
- **question:** identify the Poisson PMF when the mean is e.
- **what it is / type / subtype:** formula substitution; Poisson; point probability.
- **knowledge / approach / steps:** use $P(X=x)=e^{-\lambda}\lambda^x/x!$ and set $\lambda=e$.
- **alternate:** rewrite $e^{-e}e^x$ as $e^{x-e}$.
- **intent:** test symbol handling when the parameter and exponential base share the same letter.
- **bloom / dok / math_group / solo / gaise:** Apply; 1; A; uni; A.
- **difficulty / task demand:** 1/5; routine procedure.
- **traps:** reversing $x-e$, or moving $x!$ to the numerator.
- **exam_use / verdict:** in scope; NEW exact item, confirms the Poisson-PMF node.
- **verified:** option 1 follows algebraically and matches the scheme.

## M25-Q03, sufficient statistic definition

- **source:** `md/paper-mte-2025-26/p002.md`, question 3.
- **question:** identify what makes a statistic sufficient for a parameter.
- **what it is / type / subtype:** concept MCQ; estimation; sufficiency.
- **knowledge / approach / steps:** sufficiency retains all sample information about the parameter.
- **alternate:** eliminate variance, unbiasedness and sample-mean distractors.
- **intent:** separate sufficiency from other estimator properties.
- **bloom / dok / math_group / solo / gaise:** Understand; 1; A; uni; B.
- **difficulty / task demand:** 1/5; comprehension.
- **traps:** treating sufficient as synonymous with unbiased or efficient.
- **exam_use / verdict:** in scope; NEW exact item, confirms a previously lightly evidenced node.
- **verified:** option 2 matches the scheme and standard definition.

## M25-Q04, polynomial PDF normalization and moments

- **source:** `md/paper-mte-2025-26/p002.md`, question 4.
- **question:** for $f(x)=kx^3(4-x)^2$ on $(0,4)$, find k, mean and variance.
- **what it is / type / subtype:** multi-step calculation; continuous distribution; normalization and moments.
- **knowledge / approach / steps:** integrate $f$ to one; integrate $xf$ and $x^2f$; use $Var=E(X^2)-E(X)^2$.
- **alternate:** expand the polynomial first or use beta-integral structure.
- **intent:** connect the three standard PDF operations in one block.
- **bloom / dok / math_group / solo / gaise:** Apply; 2; B; relational; B.
- **difficulty / task demand:** 3/5; procedure with connections.
- **traps:** using infinite bounds despite finite support; dropping k; rounding before variance.
- **exam_use / verdict:** in scope; NEW exact item, confirms the normalize-to-moments chain.
- **verified:** $k=15/1024$, $E(X)=16/7$, $E(X^2)=40/7$, $Var(X)=24/49$; scheme bounds error is errata 20.

## M25-Q05, reverse Chebyshev width

- **source:** `md/paper-mte-2025-26/p002.md`, question 5.
- **question:** mean 10, variance 4; find c with $P(|X-10|\geq c)\leq0.04$.
- **what it is / type / subtype:** inequality inversion; Chebyshev; solve for interval width.
- **knowledge / approach / steps:** $\sigma=2$; set $1/k^2=0.04$; $k=5$; $c=k\sigma=10$.
- **alternate:** solve $\sigma^2/c^2=0.04$ directly.
- **intent:** test reverse use, not a forward bound.
- **bloom / dok / math_group / solo / gaise:** Apply; 2; B; relational; B.
- **difficulty / task demand:** 2/5; procedure with connections.
- **traps:** using variance as sigma, taking negative k, or returning k instead of c.
- **exam_use / verdict:** in scope; NEW exact item, CONFIRMS the formerly hypothetical reverse-Chebyshev node.
- **verified:** c=10, matching the scheme and L10-11 Q2.

## M25-Q06, exponential survival and CDF

- **source:** `md/paper-mte-2025-26/p002.md`, question 6.
- **question:** mean 3 minutes; find $P(T>1)$ and $P(T<3)$.
- **what it is / type / subtype:** applied distribution; exponential; survival and CDF.
- **knowledge / approach / steps:** $\lambda=1/3$; use $e^{-\lambda t}$ and $1-e^{-\lambda t}$.
- **alternate:** integrate the density over the requested ranges.
- **intent:** catch the rate-versus-mean inversion.
- **bloom / dok / math_group / solo / gaise:** Apply; 2; B; multi; B.
- **difficulty / task demand:** 2/5; routine procedure.
- **traps:** setting $\lambda=3$, or using the survival form for both parts.
- **exam_use / verdict:** in scope; NEW exact item, confirms existing survival/CDF nodes.
- **verified:** $e^{-1/3}=0.716531$ and $1-e^{-1}=0.632121$.

## M25-Q07, exact-normal sample mean for n=9

- **source:** `md/paper-mte-2025-26/p002.md`, question 7.
- **question:** normal lifetimes with mean 7 and SD 1; find $P(6.4<\bar X<7.2)$ for n=9.
- **what it is / type / subtype:** sampling distribution; normal; sample mean with small n.
- **knowledge / approach / steps:** normal parent makes $\bar X$ normal; $SE=1/3$; z bounds are -1.8 and 0.6.
- **alternate:** standardize $3(\bar X-7)$ directly.
- **intent:** test that exact normality does not require n at least 30.
- **bloom / dok / math_group / solo / gaise:** Apply; 2; B; relational; B.
- **difficulty / task demand:** 3/5; procedure with connections.
- **traps:** dividing by n instead of root n, or rejecting n=9.
- **exam_use / verdict:** in scope; NEW exact item, CONFIRMS the exact-normal small-n sibling.
- **verified:** $0.4641+0.2257=0.6898$ from the supplied table values.

## M25-Q08, Poisson quality design plus estimator transformation

- **source:** `md/paper-mte-2025-26/p002.md`, question 8.
- **question:** derive per-word mistake chances under two acceptance targets, then show $t^2$ is biased for $\theta^2$.
- **what it is / type / subtype:** composite block; Poisson design and estimator bias.
- **knowledge / approach / steps:** use zero-count probability for 200 and 4000 words; solve exponential inequalities; expand $Var(t)$.
- **alternate:** use logs directly rather than common-log approximations.
- **intent:** combine parameter recovery with a short proof.
- **bloom / dok / math_group / solo / gaise:** Analyze; 3; C; relational; B.
- **difficulty / task demand:** 4/5; multi-step reasoning.
- **traps:** confusing letters with words; replacing 0.99 by 0.01; concluding $E(t^2)\ne0$ instead of $E(t^2)\ne\theta^2$.
- **exam_use / verdict:** in scope; NEW exact composite item, CONFIRMS Poisson parameter recovery and transformed-estimator bias.
- **verified:** scheme gives about $5.06\times10^{-5}$ for part i; exact part ii is $-\ln(0.9)/4000=2.6340\times10^{-5}$; proof correction is errata 21.

## M24-QA1, scaled Poisson mean and variance

- **source:** `md/paper-mte-2024-25/p001.md`, QA1.
- **question:** $X$ is Poisson with mean 0.5 and $Y=2X$; identify correct mean/variance statements.
- **what it is / type / subtype:** transformation MCQ; expectation and variance; scaling.
- **knowledge / approach / steps:** $E(2X)=2E(X)$; $Var(2X)=4Var(X)$; Poisson variance equals mean.
- **alternate:** write Y values explicitly, though the moment rules are faster.
- **intent:** distinguish linear scaling of expectation from quadratic scaling of variance.
- **bloom / dok / math_group / solo / gaise:** Apply; 2; A; relational; B.
- **difficulty / task demand:** 2/5; routine procedure.
- **traps:** multiplying variance by 2 instead of 4.
- **exam_use / verdict:** in scope; NEW exact item, confirms the linear-transformation node.
- **verified:** $E(Y)=1$, $Var(Y)=2$; statements i and iii, option C.

## M24-QA2, triangular PDF to CDF

- **source:** `md/paper-mte-2024-25/p001.md`, QA2.
- **question:** find the CDF expression on $1\leq x\leq2$ for a triangular density.
- **what it is / type / subtype:** integration MCQ; PDF to CDF; piecewise accumulation.
- **knowledge / approach / steps:** include mass from 0 to 1, then integrate $2-t$ from 1 to x.
- **alternate:** integrate from x to 2 and subtract from one.
- **intent:** test that a later CDF branch includes earlier support mass.
- **bloom / dok / math_group / solo / gaise:** Apply; 2; B; relational; B.
- **difficulty / task demand:** 3/5; procedure with connections.
- **traps:** integrating only the current density branch.
- **exam_use / verdict:** in scope; NEW exact item, confirms PDF-to-CDF; official key is wrong.
- **verified:** $F(x)=2x-x^2/2-1$, option D; endpoint checks give 1/2 and 1. Errata 19.

## M24-QA3, identify false Chebyshev forms

- **source:** `md/paper-mte-2024-25/p001.md`, QA3.
- **question:** identify which displayed statements are not Chebyshev's inequality.
- **what it is / type / subtype:** statement audit; Chebyshev; tail and complement forms.
- **knowledge / approach / steps:** compare each option with $P(|X-\mu|\geq k\sigma)\leq1/k^2$ and its complement.
- **alternate:** convert all options to the absolute-width form $\sigma^2/c^2$.
- **intent:** test form recognition and inequality direction.
- **bloom / dok / math_group / solo / gaise:** Analyze; 2; C; relational; B.
- **difficulty / task demand:** 3/5; procedure with connections.
- **traps:** accepting $k^2/\sigma^2$ or treating tail and center bounds as identical.
- **exam_use / verdict:** in scope; NEW exact item, CONFIRMS the statement-spotting sibling.
- **verified:** a and b are valid; c and d are not valid general forms as printed.

## M24-QB1, variance of independent Poisson combination

- **source:** `md/paper-mte-2024-25/p001.md`, QB1.
- **question:** infer two Poisson parameters from adjacent point-probability equalities, then find $Var(X-2Y)$.
- **what it is / type / subtype:** parameter recovery; Poisson and variance; linear combination.
- **knowledge / approach / steps:** $P(X=1)=P(X=2)$ gives $\lambda_X=2$; $P(Y=2)=P(Y=3)$ gives $\lambda_Y=3$; independence gives $2+4(3)$.
- **alternate:** use the adjacent-probability ratio $P(k+1)/P(k)=\lambda/(k+1)$.
- **intent:** join parameter inference to the variance scaling rule.
- **bloom / dok / math_group / solo / gaise:** Analyze; 3; B; relational; B.
- **difficulty / task demand:** 3/5; procedure with connections.
- **traps:** subtracting variances, or failing to square -2.
- **exam_use / verdict:** in scope; NEW exact item, CONFIRMS $Var(X-2Y)$ and Poisson-ratio siblings.
- **verified:** $Var(X-2Y)=2+12=14$, matching the scheme.

## M24-QB2, exponential multi-part probabilities

- **source:** `md/paper-mte-2024-25/p001.md`, QB2.
- **question:** rate 1/4; find survival, interval, CDF, mean and variance.
- **what it is / type / subtype:** applied distribution; exponential; multi-target calculation.
- **knowledge / approach / steps:** use survival differences; $E=1/\lambda$; $Var=1/\lambda^2$.
- **alternate:** integrate the density for each probability.
- **intent:** test the full exponential tool set in one four-mark block.
- **bloom / dok / math_group / solo / gaise:** Apply; 2; B; multi; B.
- **difficulty / task demand:** 3/5; routine procedures.
- **traps:** using mean 1/4, subtracting CDFs backwards, or reporting SD as variance.
- **exam_use / verdict:** in scope; NEW exact item, CONFIRMS the formerly hypothetical exponential-interval node.
- **verified:** 0.223130, 0.123987, 0.713495, mean 4, variance 16.

## M24-QB3, Chebyshev bound versus actual probability

- **source:** `md/paper-mte-2024-25/p002.md`, QB3.
- **question:** for $U(-1,1)$, compare the Chebyshev bound for $|X-E(X)|\geq2\sqrt{Var(X)}$ with the actual probability.
- **what it is / type / subtype:** comparison; Chebyshev and uniform; bound versus support.
- **knowledge / approach / steps:** mean 0, variance 1/3; Chebyshev gives at most 1/4; threshold $2/\sqrt3>1$ lies outside support, so actual probability is zero.
- **alternate:** inspect support before applying the inequality.
- **intent:** show that distribution-free bounds can be loose.
- **bloom / dok / math_group / solo / gaise:** Analyze; 3; C; relational; B.
- **difficulty / task demand:** 3/5; interpretation.
- **traps:** reporting the upper bound as the actual probability.
- **exam_use / verdict:** in scope; NEW exact item, CONFIRMS bound-versus-actual evidence.
- **verified:** upper bound 1/4, actual 0, matching the source scheme.

## M24-QB4, periodic train waiting time

- **source:** `md/paper-mte-2024-25/p002.md`, QB4.
- **question:** arrivals every 15 minutes; passenger arrival uniform from 9:00 to 9:30; find wait below 6 and above 10 minutes.
- **what it is / type / subtype:** periodic application; uniform; measure-of-time ratio.
- **knowledge / approach / steps:** split the 30-minute window into two 15-minute cycles; measure favorable subinterval lengths.
- **alternate:** define waiting time modulo 15, which is uniform on $(0,15)$.
- **intent:** test modeling before arithmetic.
- **bloom / dok / math_group / solo / gaise:** Apply; 3; B; relational; B.
- **difficulty / task demand:** 3/5; application in context.
- **traps:** treating the full 30 minutes as one train interval.
- **exam_use / verdict:** in scope; NEW exact item, confirms a periodic-uniform application.
- **verified:** $P(W<6)=12/30=2/5$ and $P(W>10)=10/30=1/3$.

## M24-QC1, normal rainfall plus recovered binomial parameters

- **source:** `md/paper-mte-2024-25/p002.md`, QC1.
- **question:** four normal-rainfall probabilities including a weekly binomial layer, then infer a binomial model from its mean and $P(X=1)=P(X=2)$.
- **what it is / type / subtype:** composite block; normal-to-binomial nesting and parameter recovery.
- **knowledge / approach / steps:** standardize daily rainfall; use the interval probability as binomial p for seven independent days; solve $p=2/(n+1)$ with $np=5/3$.
- **alternate:** derive the adjacent binomial ratio before substituting the mean.
- **intent:** test distribution composition and reverse parameter inference.
- **bloom / dok / math_group / solo / gaise:** Analyze; 3; C; relational; B.
- **difficulty / task demand:** 5/5; multi-step reasoning.
- **traps:** reading 34.5 as SD instead of variance; omitting the independent-day assumption; using normal p directly without binomial nesting.
- **exam_use / verdict:** in scope; NEW exact composite item, confirms normal nesting and binomial-ratio nodes.
- **verified:** daily results use z 0.58, -0.27, -0.19 and 0.34; interval p=0.2084; under independent days $P(K\leq2)=0.837219$. Binomial part gives $n=5,p=1/3$, variance $10/9$, $P(X\geq1)=211/243$, $P(X\leq1)=112/243$.

## U01 count and dedup verdict

| paper | top-level blocks | exact duplicates inside batch 1 | new exact items |
|---|---:|---:|---:|
| 2025-26 MTE | 8 | 0 | 8 |
| 2024-25 MTE | 8 | 0 | 8 |
| total | 16 | 0 | 16 |

The schemes repeat the questions while assigning marks, so they add zero items. Similar
methods are type overlap, not exact-item duplication. U01 therefore changes the locked total
from 112 items / 107 unique to 128 items / 123 unique.
