# lms-theory-of-estimation

## THEORY OF ESTIMATION

Parameter • Statistic • Point & Interval Estimation
Characteristics of Good Estimator • Applications & Numerical Problems

MAS2001: STATISTICS AND PROBABILTY

MUJ | Dr. Vivek Singh
page:1

---

## Learning Outcomes

* Define parameter, statistic, estimator and estimate.
* Distinguish between point estimation and interval estimation.
* Understand unbiasedness, consistency and efficiency.
* Use sufficient conditions to establish consistency.
* Compare estimators using bias and variance.
* Apply estimation concepts to practical numerical situations.

MAS2001 MU | Dr. Vivek Singh
page:2

---

## Basic Statistical Terminology

| | |
| :--- | :--- |
| **Population Parameter** | **Statistic** |
| A numerical characteristic describing a population. | A numerical quantity computed from sample data. |
| Examples: $\mu$, $\sigma^2$, $p$. | Examples: $\bar{X}$, $S^2$, $\hat{p}$. |
| | |
| **Estimator** | **Estimate** |
| A function of sample observations used to estimate a parameter. | The numerical value obtained from an estimator. |
| Example: $\bar{X}$ as an estimator of $\mu$. | Example: $\bar{x} = 52$. |
| | |
| **Sample Space** | **Parameter Space** |
| The set of all possible outcomes of a random experiment. | The set of all possible values of a parameter. |
| Example: $S = \{HH, HT, TH, TT\}$. | Example: $\Theta = (-\infty, \infty)$ for $\mu$. |

MAS2001 MUJ | Dr. Vivek Singh

page:3

---

## (untitled)
• **Statistical inference** is the process by which we acquire information about populations from samples.
• There are two procedures for making inferences:
    - Estimation.
    - Hypotheses testing.

**Concepts of Estimation**
• The objective of estimation is to determine the value of a population parameter on the basis of a sample statistic.
• There are two types of estimators
    - Point Estimator
    - Interval estimator

page:4

---

## Estimation

- Estimation is the statistical procedure in which a random sample is selected from a population and a sample statistic is used to approximate an unknown population parameter.

Population $\rightarrow$ Random Sample $\rightarrow$ Statistic $\rightarrow$ Estimate of Parameter

**Point Estimation**
- A single value is used to estimate the unknown parameter.
- A point estimator draws inference about a population by estimating the value of an unknown parameter using a single value or a point.

**Interval Estimation**
- A range of values is used to estimate the unknown parameter.
- An interval estimator draws inferences about a population by estimating the value of an unknown parameter using an interval.
- The interval estimator is affected by the sample size.

MAS2001| MUJ | Dr. Vivek Singh
page:5

---

## Point Estimation

A point estimate is a single numerical value used to estimate an unknown population parameter.

$$ \mu \approx \bar{X} \quad \sigma^2 \approx S^2 \quad p \approx \hat{p} $$

| Mean | Variance | Proportion |
| :--- | :--- | :--- |
| Estimate $\mu$ using $\bar{X}$. | Estimate $\sigma^2$ using $S^2$. | Estimate $p$ using $\hat{p}$. |

Advantage: simple and easy to report. Limitation: it does not directly communicate sampling uncertainty.

page:6

---

## Interval Estimation

Interval estimation provides a range of values within which a population parameter is expected to lie with a specified level of confidence.

* Accounts for uncertainty in estimation.
* Results in a confidence interval.
* More informative than a point estimate when precision matters.

Confidence Interval = Point Estimate $\pm$ Margin of Error

page:7

---

## Point Estimate vs Interval Estimate

**POINT ESTIMATE**
* One value
* Example:
* Estimated average response time = 210 ms
* ✓ Simple
* X Uncertainty not shown

**INTERVAL ESTIMATE**
* A range of plausible values
* Example:
* 95% CI = (204 ms, 216 ms)
* ✓ Shows uncertainty
* ✓ More informative

MUJ | Dr. Vivek Singh
MAS2001|

page:8

---

## Characteristics of a Good Estimator

- **Unbiasedness**
  Correct on average

- **Consistency**
  Approaches the true value as n increases

- **Efficiency**
  Smallest variance among comparable unbiased estimators

- **Sufficiency**
  Uses all relevant information in the sample

Good estimator $\rightarrow$ little systematic error + stability + precision

page:9

---

## Unbiased Estimator

An estimator $\hat{\theta}$ is said to be unbiased for a parameter $\theta$ if

$$E(\hat{\theta}) = \theta$$

It neither overestimates nor underestimates the parameter on average.

$$\text{Bias}(\hat{\theta}) = E(\hat{\theta}) - \theta$$

page:10

---

## Consistency

An estimator $\widehat{\theta}_n$ of a population parameter $\theta$ is said to be consistent if it converges in probability to $\theta$ as the sample size $n$ tends to infinity.

Mathematically,
$$\widehat{\theta}_n \xrightarrow{P} \theta \quad \text{as} \quad n \to \infty$$

This implies that for any $\varepsilon > 0$,
$$P(|\widehat{\theta}_n - \theta| < \varepsilon) \to 1 \quad \text{as} \quad n \to \infty$$

page:11

---

## Sufficient Condition :Consistency

Sufficient Condition for Consistency

For a sequence of estimators $T_n$:

① $E(T_n) \rightarrow \theta$ as $n \rightarrow \infty$

② $Var(T_n) \rightarrow 0$ as $n \rightarrow \infty$

Then $T_n$ is a consistent estimator of $\theta$.

For $\bar{X}$ : $E(\bar{X})=\mu$ and $Var(\bar{X})=\sigma^2/n \rightarrow 0$

page:12

---

## Why is the Sample Mean Consistent?

$$\bar{X} = (X_1 + X_2 + \dots + X_n)/n$$

**Condition 1: Mean**
$E(\bar{X}) = \mu$
Therefore, $E(\bar{X}) \rightarrow \mu$.

**Condition 2: Variance**
$Var(\bar{X}) = \sigma^2/n$
As $n \rightarrow \infty$, $\sigma^2/n \rightarrow 0$.

**Conclusion**
Both conditions hold.
Therefore $\bar{X}$ is a consistent estimator of $\mu$.

**More observations $\rightarrow$ smaller variance $\rightarrow$ more stable estimate**

page:13

---

## Efficient Estimator - Definition

Let $\widehat{\theta}_1$ and $\widehat{\theta}_2$ be two unbiased estimators for parameter $\theta$:

$$E(\widehat{\theta}_1) = \theta \quad \text{and} \quad E(\widehat{\theta}_2) = \theta$$

If:

$$\text{Var}(\widehat{\theta}_1) < \text{Var}(\widehat{\theta}_2)$$

then $\widehat{\theta}_1$ is said to be more efficient than $\widehat{\theta}_2$.

**Mathematical statement**

Among all unbiased estimators, the most efficient one has the smallest variance.

page:14

---

## Efficiency: A Simple Visual

Figure: A diagram comparing two estimators. The left box, Estimator A, lists: "Unbiased", "Variance = 4", "More concentrated estimates", and "$\rightarrow$ Higher precision". The right box, Estimator B, lists: "Unbiased", "Variance = 9", "More spread in estimates", and "$\rightarrow$ Lower precision". A rectangular box at the bottom contains the formula "Efficiency $\propto$ 1 / Variance".

MUJ | Dr. Vivek Singh
15
MAS2001|
page:15

---

## Example 1: Comparing Estimators for a Normal Mean

**Question 1**

A random sample $(X_1, X_2, X_3, X_4, X_5)$ of size 5 is drawn from a normal population with unknown mean $\mu$.
Consider the following estimators for $\mu$:
1. $t_1 = \frac{X_1 + X_2 + X_3 + X_4 + X_5}{5}$
2. $t_2 = \frac{X_1 + X_2}{2} + X_3$
3. $t_3 = \frac{2X_1 + X_2 + \lambda X_3}{3}$
where $\lambda$ is chosen such that $t_3$ is unbiased.

**Tasks**

1. Find the value of $\lambda$
2. Check if $t_1$ and $t_2$ are unbiased
3. Determine the best estimator among $t_1, t_2$, and $t_3$

MUJ | Dr. Vlyek Singh
page:15

---

## Solution: Step 1 - Find $\lambda$

For $t_3$ to be unbiased, we require $E(t_3)=\mu$.

$$E(t_3) = \frac{2E(X_1) + E(X_2) + \lambda E(X_3)}{3}$$

$$= \frac{2\mu + \mu + \lambda\mu}{3} = \left[ \frac{3+\lambda}{3} \right] \mu$$

$$\frac{3+\lambda}{3} = 1 \implies \lambda = 0$$

Hence, $t_3 = \frac{2X_1 + X_2}{3}$.

MAS2001 | MUJ | Dr. Vivek Singh | 17

page:17

---

## Solution: Step 2 : Check Unbiasedness

**$t_1$**
$E(t_1) = (\mu+\mu+\mu+\mu+\mu)/5 = \mu$
✓ $t_1$ is unbiased.

**$t_2$**
$E(t_2) = (\mu+\mu)/2 + \mu = 2\mu$
✗ $t_2$ is biased.

**$t_3$**
With $\lambda=0$:
$E(t_3) = (2\mu+\mu)/3 = \mu$
✓ $t_3$ is unbiased.

Unbiased estimators: $t_1$ and $t_3$

page:18

---

## Solution: Step 3 - Compare Variances

Let $\text{Var}(X_i)=\sigma^2$ and assume the observations are independent.

$$ \text{Var}(t_1) = \frac{\sigma^2}{5} $$

$$ \text{Var}(t_2) = \sigma^2/2 + \sigma^2 = \frac{3\sigma^2}{2} $$

$$ \text{Var}(t_3) = (4\sigma^2+\sigma^2)/9 = \frac{5\sigma^2}{9} $$

**Comparison**

$$ \sigma^2/5 < 5\sigma^2/9 < 3\sigma^2/2 $$

Therefore $t_1$ has the smallest variance among the unbiased estimators.

**Best estimator** $= t_1 = \bar{X}$

page:19

---

## Properties of a Good Point Estimator

**Example2:** Let $X_1$, $X_2$ and $X_3$ be a random sample of size 3 from a population with mean $\mu$ and variance $\sigma^2$. $T_1$, $T_2$ and $T_3$ are estimators used to estimate the mean $\mu$, where:
$T_1 = X_1 + X_2 - X_3$
$T_2 = 2X_1 + 3X_3 - 4X_2$
$T_3 = \frac{(\lambda X_1 + X_2 + X_3)}{3}$
Answer the following:
1. Are $T_1$ and $T_2$ unbiased estimators?
2. Find the value of $\lambda$ such that $T_3$ is an unbiased estimator for $\mu$.
3. With the value of $\lambda$ obtained, is $T_3$ a consistent estimator?
4. Which one is the best estimator?

page:20

---

## Properties of a Good Point Estimator

**(ii) Finding value of $\lambda$ for $T_3$ to be unbiased**

Let $T_3 = \lambda (X_1 + X_2 + X_3) / 3$

For unbiasedness, $E(T_3) = \mu$

$E(T_3) = (\lambda / 3) [E(X_1) + E(X_2) + E(X_3)]$

$= (\lambda / 3) (\mu + \mu + \mu) = \lambda \mu$

For unbiasedness: $\lambda \mu = \mu \Rightarrow \lambda = 1$

**(iii) Consistency of $T_3$**

With $\lambda = 1$, $T_3 = (X_1 + X_2 + X_3) / 3 = \bar{X}$ (sample mean).

Since the sample mean is a consistent estimator of the population mean, $T_3$ is a consistent estimator.

page:21

---

## Properties of a Good Point Estimator

(iv) Variance of the estimators:

$\text{Var}(T_1) = \text{Var}(X_1) + \text{Var}(X_2) + \text{Var}(X_3) = 3\sigma^2$

$\text{Var}(T_2) = 4\text{Var}(X_1) + 9\text{Var}(X_3) + 16\text{Var}(X_2) = 29\sigma^2$

$\text{Var}(T_3) = (1/9) [\text{Var}(X_1) + \text{Var}(X_2) + \text{Var}(X_3)]$

$= (1/9)(3\sigma^2)$

$= \sigma^2 / 3$

Since $\text{Var}(T_3)$ is minimum, $T_3$ is the best estimator.

MUJ | Dr. Vlvek Singh

page:22

---

## Sufficient Estimator - Definition

**Key Concept**
A statistic $T$ is **sufficient** for parameter $\theta$ if the conditional distribution of the sample given $T$ does not depend on $\theta$.

$$f(x_1, \dots, x_n \mid T = t; \theta) \text{ is free of } \theta$$

**Factorization Theorem (Neyman-Fisher)**
The joint distribution can be factorized as:

$$\text{Joint PDF/PMF} = (\text{Function of } T \text{ and } \theta) \times (\text{Function independent of } \theta)$$

$$\underbrace{f(x_1, \dots, x_n; \theta)}_{\text{Joint distribution}} = \underbrace{g(T(x_1, \dots, x_n), \theta)}_{\text{Depends on sample through } T \text{ only}} \cdot \underbrace{h(x_1, \dots, x_n)}_{\text{Independent of } \theta}$$

page:23

---

## Example: Sufficiency in Poisson Distribution

**Problem**
Show that $\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i$ is sufficient for $\lambda$ when $X_i \sim \text{Poisson}(\lambda)$.

**Solution**
Joint PMF:
$$f(x_1, \dots, x_n; \lambda) = \prod_{i=1}^{n} \frac{e^{-\lambda} \lambda^{x_i}}{x_i!} = e^{-n\lambda} \lambda^{\sum x_i} \prod_{i=1}^{n} \frac{1}{x_i!}$$

Let $T = \sum_{i=1}^{n} X_i = n\bar{X}$:
$$f(x_1, \dots, x_n; \lambda) = \underbrace{e^{-n\lambda} \lambda^T}_{g(T, \lambda)} \cdot \frac{1}{\underbrace{\prod_{i=1}^{n} x_i!}_{h(\mathbf{x})}}$$

By Factorization Theorem, $T$ (and hence $\bar{X}$) is sufficient for $\lambda$.

MAS2001[
MUIT Dr. Vlyak Singh

page:74

---

## Example: Sufficiency in Exponential Distribution

**Problem Statement**
Let $X_1, X_2, \dots, X_n$ be a random sample from an exponential distribution with rate parameter $\lambda$:

$$X_i \sim \text{Exp}(\lambda), \quad f(x; \lambda) = \lambda e^{-\lambda x}, \quad x > 0, \lambda > 0$$

Show that $\overline{X} = \frac{1}{n} \sum_{i=1}^n X_i$ is a sufficient statistic for $\lambda$.

**Step 1: Write the Joint PDF**
Since $X_1, X_2, \dots, X_n$ are i.i.d.:

$$f(x_1, x_2, \dots, x_n; \lambda) = \prod_{i=1}^n f(x_i; \lambda) = \prod_{i=1}^n \lambda e^{-\lambda x_i}$$

$$\prod_{i=1}^n \lambda e^{-\lambda x_i} = \lambda^n \cdot e^{-\lambda \sum_{i=1}^n x_i} = \lambda^n \cdot e^{-\lambda(n\overline{x})}$$

page:25

---

## Solution Continued: Applying Factorization Theorem

Step 3: Factorize the Joint PDF

We have:
$$f(x_1, x_2, \dots, x_n; \lambda) = \lambda^n \cdot e^{-\lambda n \bar{x}}$$

Let $T = \bar{X}$, then:
$$f(x_1, x_2, \dots, x_n; \lambda) = \underbrace{\lambda^n e^{-\lambda n T}}_{g(T, \lambda)} \cdot \underbrace{1}_{h(x_1, \dots, x_n)}$$

Step 4: Verify the Conditions

$g(T, \lambda) = \lambda^n e^{-\lambda n T}$
* Depends on parameter $\lambda$
* Depends on data only through $T = \bar{X}$

$h(x_1, \dots, x_n) = 1$
* Constant function
* Independent of $\lambda$

MAS2001 | MUJ | Dr. Vyom Singh

page:26

---

## Real-Life Numerical 1: Average Server Response Time

**Situation**

A service team records the response times (ms) of 8 randomly selected requests:

180, 210, 195, 220, 205, 190, 200, 240

**Question**

Estimate the population mean response time using a point estimator.

Also state the estimator and the estimate.

**Solution**

$\bar{X} = (\text{sum of observations})/8 = 1640/8 = 205$ ms

Estimator: $\bar{X}$

Estimate: 205 ms

page:27

---

## Real-Life Numerical 2: Packet Delivery Success

**Situation**
During a network test, 500 packets are transmitted. Of these, 465 are successfully delivered.

**Question**
Estimate the probability $p$ of successful packet delivery.
Identify the estimator used.

**Solution**
$\hat{p} = X/n$
$= 465/500$
$= 0.93$
Estimated success probability = 93%.

page:28

---

## Real-Life Numerical 3: Battery-Life Estimation

Situation

A sample of 25 devices has an average battery life of 8.4 hours. The population standard deviation is known to be 1.5 hours.

Question

Construct a 95% confidence interval for the population mean battery life.

Use $z_{0.975} = 1.96$.

Solution

$\text{CI} = \bar{X} \pm z(\sigma/\sqrt{n})$

$= 8.4 \pm 1.96(1.5/5)$

$= 8.4 \pm 0.588$

$\text{CI} \approx (7.81, 8.99)$ hours.

**Interpretation:** the interval gives a plausible range for the population mean.

MUJ | Dr. Vivek Singh MAS2001 | 21

page:29

---

## Quick Comparison: Three Real-Life Problems

**1. Response Time**
Parameter: $\mu$
Statistic: $\bar{X}$
Point estimate $= 205$ ms

**2. Packet Success**
Parameter: $p$
Statistic: $\hat{p}$
Point estimate $= 0.93$

**3. Battery Life**
Parameter: $\mu$
Statistic: $\bar{X}$
$95\%$ CI $\approx (7.81, 8.99)$

Point estimation $\rightarrow$ one value &nbsp;&nbsp;&nbsp; Interval estimation $\rightarrow$ range

page:30

---

## Interval Estimate of a Population Mean: $\sigma$ Known

- In order to develop an interval estimate of a population mean, the margin of error must be computed using either:
  - the population standard deviation $\sigma$, or
  - the sample standard deviation $s$

- $\sigma$ is rarely known exactly, but often a good estimate can be obtained based on historical data or other information.

- We refer to such cases as the $\sigma$ **known case**.

page:31

---

## Interval Estimate of a Population Mean: $\sigma$ Known

**Estimating the Population Mean when the Population Standard Deviation is Known (i.e. $\sigma$ Known)**

*   How is an interval estimator produced from a sampling distribution?
    *   To estimate $\mu$, a sample of size $n$ is drawn from the population, and its mean $\overline{\text{X}}$ is calculated.
    *   Under certain conditions, $\overline{\text{X}}$ is normally distributed (or approximately normally distributed.), thus

$$Z = \frac{\overline{\text{X}} - \mu}{\sigma / \sqrt{n}}$$

---

## Interval Estimate of a Population Mean: $\sigma$ Known

There is a $1 - \alpha$ probability that the value of a sample mean will provide a margin of error of $z_{\alpha/2} \sigma_{\bar{x}}$ or less.

Figure: A bell-shaped normal distribution curve representing the sampling distribution of $\bar{x}$. The horizontal axis is labeled $\bar{x}$ and the center of the distribution is marked $\mu$. The middle area under the curve is shaded green and labeled "$1 - \alpha$ of all $\bar{x}$ values". The left and right tail areas are shaded blue and each is labeled $\alpha/2$. The distance from the mean $\mu$ to the boundaries of the central area on both sides is indicated by arrows and labeled $z_{\alpha/2} \sigma_{\bar{x}}$. A text box labeled "Sampling distribution of $\bar{x}$" is positioned to the right of the peak, pointing toward the green shaded area.

9/11/2026
MUJ | Dr Vivek Singh

---

## Interval Estimate of a Population Mean: σ Known

Figure: A sampling distribution of x̄ curve. The curve is a green bell-shaped normal distribution centered at μ. The middle green shaded area is labeled "1 - α of all x̄ values". The left and right tails are shaded dark blue, each labeled "α/2". The x-axis is labeled x̄. Two yellow speech bubbles point to the tails: the left bubble states "interval does not include μ", the right bubble states "interval includes μ". Vertical lines mark the boundaries of the intervals. Labels on the horizontal axis show the distance from the center μ as z_{α/2}σ_x̄ on both the left and right sides. Below the axis, three example intervals are indicated with dashed blue lines: the left interval is [x̄ - z_{α/2}σ_x̄, x̄ + z_{α/2}σ_x̄] and does not include μ, the middle and right intervals do include μ.

9/11/2026
MUJ | Dr Vivek Singh

---

## (untitled)

Confidence level

Lower confidence limit

Upper confidence limit

Figure: A normal distribution curve with mean at $\bar{x}$ and confidence interval limits at $\bar{x} - z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$ and $\bar{x} + z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$. The shaded area between the limits is labeled $1 - \alpha$ and corresponds to the confidence level. Arrows indicate the distance from the mean to each limit, and the total width of the interval is labeled $2 z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$.

$$2 z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$$

$$\left[ \bar{x} - z_{\alpha/2} \frac{\sigma}{\sqrt{n}}, \bar{x} + z_{\alpha/2} \frac{\sigma}{\sqrt{n}} \right]$$

9/11/2026

MUJ | Dr Vivek Singh

---

## (untitled)

- We know that $P(\mu - z_{\alpha/2} \frac{\sigma}{\sqrt{n}} \le \bar{x} \le \mu + z_{\alpha/2} \frac{\sigma}{\sqrt{n}}) = 1 - \alpha$
- This leads to the relationship

$$P(\bar{x} - z_{\alpha/2} \frac{\sigma}{\sqrt{n}} \le \mu \le \bar{x} + z_{\alpha/2} \frac{\sigma}{\sqrt{n}}) = 1 - \alpha$$

$1 - \alpha$ of all the values of $\bar{x}$ obtained in repeated sampling from this distribution, construct an interval

$$\left[ \bar{x} - z_{\alpha/2} \frac{\sigma}{\sqrt{n}}, \bar{x} + z_{\alpha/2} \frac{\sigma}{\sqrt{n}} \right]$$

that includes (covers) the expected value of the population.

9/11/2026
MUJ | Dr Vivek Singh

---

## Interval Estimate of a Population Mean: $\sigma$ Known

Interval Estimate of $\mu$

$$\bar{x} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$$

where: 
$\bar{x}$ is the sample mean
$1 - \alpha$ is the confidence coefficient
$z_{\alpha/2}$ is the $z$ value providing an area of $\alpha/2$ in the upper tail of the standard normal probability distribution
$\sigma$ is the population standard deviation
$n$ is the sample size

9/11/2026

MUJ | Dr Vivek Singh

---

## Interval Estimate of a Population Mean: $\sigma$ Known

Values of $z_{\alpha/2}$ for the Most Commonly Used Confidence Levels

| Confidence Level | $\alpha$ | $\alpha/2$ | Table Look-up Area | $z_{\alpha/2}$ |
| :--- | :--- | :--- | :--- | :--- |
| 90% | .10 | .05 | .9500 | 1.645 |
| 95% | .05 | .025 | .9750 | 1.960 |
| 99% | .01 | .005 | .9950 | 2.576 |

---

## Meaning of Confidence

*   Because 90% of all the intervals constructed using $\bar{x} \pm 1.645\sigma_{\bar{x}}$ will contain the population mean, we say we are 90% confident that the interval $\bar{x} \pm 1.645\sigma_{\bar{x}}$ includes the population mean $\mu$.
*   We say that this interval has been established at the 90% confidence level.
*   The value .90 is referred to as the confidence coefficient.

---

## References

1. Devore, J. L., Probability & Statistics for Engineering and the Sciences, 8th Edition, Cengage Learning, 2012.

MUJ | Dr. Vivek Singh
page:40
