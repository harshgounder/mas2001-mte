# ppt5-estimation-summary

## THEORY OF ESTIMATION

Parameter • Statistic • Point & Interval Estimation
Characteristics of Good Estimator • Applications & Numerical Problems

MAS2001: STATISTICS AND PROBABILTY
Prepared by : Dr. Shamshad Ur Rasool

---

## Learning Outcomes
- Define parameter, statistic, estimator and estimate.
- Distinguish between point estimation and interval estimation.
- Understand unbiasedness, consistency and efficiency.
- Use sufficient conditions to establish consistency.
- Compare estimators using bias and variance.
- Apply estimation concepts to practical numerical situations.

page:2

---

## Basic Statistical Terminology

**Population Parameter**
A numerical characteristic describing a population. Examples: $\mu, \sigma^2, p$.

**Statistic**
A numerical quantity computed from sample data. Examples: $\bar{X}, S^2, \hat{p}$.

**Estimator**
A function of sample observations used to estimate a parameter. Example: $\bar{X}$ as an estimator of $\mu$.

**Estimate**
The numerical value obtained from an estimator. Example: $\bar{x} = 52$.

**Sample Space**
The set of all possible outcomes of a random experiment. Example: $S = \{HH, HT, TH, TT\}$.

**Parameter Space**
The set of all possible values of a parameter. Example: $\Theta = (-\infty, \infty)$ for $\mu$.

page:3

---

## Estimation

Estimation is the statistical procedure in which a random sample is selected from a population and a sample statistic is used to approximate an unknown population parameter.

Figure: A flowchart with arrows showing the progression: Population $\rightarrow$ Random Sample $\rightarrow$ Statistic $\rightarrow$ Estimate of Parameter.

**Point Estimation**
A single value is used to estimate the unknown parameter.

**Interval Estimation**
A range of values is used to estimate the unknown parameter.

page:4

---

## Point Estimation

A point estimate is a single numerical value used to estimate an unknown population parameter.

$$\mu \approx X \quad \sigma^2 \approx S^2 \quad p \approx \hat{p}$$

**Mean**
Estimate $\mu$ using $\bar{X}$.

**Variance**
Estimate $\sigma^2$ using $S^2$.

**Proportion**
Estimate $p$ using $\hat{p}$.

Advantage: simple and easy to report. Limitation: it does not directly communicate sampling uncertainty.

page:5

---

## Interval Estimation

Interval estimation provides a range of values within which a population parameter is expected to lie with a specified level of confidence.

• Accounts for uncertainty in estimation.
• Results in a confidence interval.
• More informative than a point estimate when precision matters.

$$\text{Confidence Interval} = \text{Point Estimate} \pm \text{Margin of Error}$$

page:6

---

## Point Estimate vs Interval Estimate

**POINT ESTIMATE**
- One value
- Example:
- Estimated average response time = 210 ms
- $\checkmark$ Simple
- $\times$ Uncertainty not shown

**INTERVAL ESTIMATE**
- A range of plausible values
- Example:
- 95% CI = (204 ms, 216 ms)
- $\checkmark$ Shows uncertainty
- $\checkmark$ More informative

page:7

---

## Characteristics of a Good Estimator

*   **Unbiasedness**
    *   Correct on average
*   **Consistency**
    *   Approaches the true value as $n$ increases
*   **Efficiency**
    *   Smallest variance among comparable unbiased estimators
*   **Sufficiency**
    *   Uses all relevant information in the sample

Good estimator $\rightarrow$ little systematic error + stability + precision

page:8

---

## Unbiased Estimator
An estimator $\hat{\theta}$ is said to be unbiased for a parameter $\theta$ if
$E(\hat{\theta}) = \theta$

An estimator $\hat{\theta}$ is said to be unbiased for a parameter $\theta$ if
$$E(\hat{\theta}) = \theta$$

It neither overestimates nor underestimates the parameter on average.

$$\text{Bias}(\hat{\theta}) = E(\hat{\theta}) - \theta$$

page:9

---

## Consistency

An estimator $\widehat{\theta}_n$ of a population parameter $\theta$ is said to be consistent if it converges in probability to $\theta$ as the sample size $n$ tends to infinity.

Mathematically,
$$\widehat{\theta}_n \xrightarrow{P} \theta \text{ as } n \rightarrow \infty$$

This implies that for any $\epsilon > 0$,
$$P(|\widehat{\theta}_n - \theta| < \epsilon) \rightarrow 1 \text{ as } n \rightarrow \infty$$

page:10

---

## Sufficient Condition :Consistency

Sufficient Condition for Consistency

For a sequence of estimators $T_n$:

① $E(T_n) \to \theta$ as $n \to \infty$
② $\text{Var}(T_n) \to 0$ as $n \to \infty$

Then $T_n$ is a consistent estimator of $\theta$.

For $\bar{X}$ : $E(\bar{X}) = \mu$ and $\text{Var}(\bar{X}) = \sigma^2/n \to 0$

page:11

---

## Why is the Sample Mean Consistent?

$$ \bar{X} = (X_1 + X_2 + \cdots + X_n)/n $$

| Condition 1: Mean | Condition 2: Variance | Conclusion |
| :--- | :--- | :--- |
| $E(\bar{X}) = \mu$ | $\text{Var}(\bar{X}) = \sigma^2/n$ | Both conditions hold. |
| Therefore, | As $n \to \infty$, | Therefore $\bar{X}$ is a consistent |
| $E(\bar{X}) \to \mu$. | $\sigma^2/n \to 0$. | estimator of $\mu$. |

More observations $\rightarrow$ smaller variance $\rightarrow$ more stable estimate

page:12

---

## Efficient Estimator - Definition

Let $\hat{\theta}_1$ and $\hat{\theta}_2$ be two unbiased estimators for parameter $\theta$:

$$ E(\hat{\theta}_1) = \theta \quad \text{and} \quad E(\hat{\theta}_2) = \theta $$

If:

$$ \text{Var}(\hat{\theta}_1) < \text{Var}(\hat{\theta}_2) $$

then $\hat{\theta}_1$ is said to be more efficient than $\hat{\theta}_2$.

**Mathematical statement**

Among all unbiased estimators, the most efficient one has the smallest variance.

page:13

---

## Efficiency: A Simple Visual

**Estimator A**
* Unbiased
* Variance = 4
* More concentrated estimates
* $\rightarrow$ Higher precision

**Estimator B**
* Unbiased
* Variance = 9
* More spread in estimates
* $\rightarrow$ Lower precision

Efficiency $\propto$ 1 / Variance

page:14

---

## Example 1: Comparing Estimators for a Normal Mean

### Question 1
A random sample $(X_1, X_2, X_3, X_4, X_5)$ of size 5 is drawn from a normal population with unknown mean $\mu$.
Consider the following estimators for $\mu$:
1. $t_1 = \frac{X_1 + X_2 + X_3 + X_4 + X_5}{5}$
2. $t_2 = \frac{X_1 + X_2}{2} + X_3$
3. $t_3 = \frac{2X_1 + X_2 + \lambda X_3}{3}$ where $\lambda$ is chosen such that $t_3$ is unbiased.

### Tasks
1. Find the value of $\lambda$
2. Check if $t_1$ and $t_2$ are unbiased
3. Determine the best estimator among $t_1, t_2,$ and $t_3$

page:15

---

## Solution: Step 1 - Find $\lambda$
For $t_3$ to be unbiased, we require $E(t_3)=\mu$.

$$E(t_3) = [2E(X_1)+E(X_2)+\lambda E(X_3)]/3$$

$$= (2\mu + \mu + \lambda\mu)/3 = [(3+\lambda)/3]\mu$$

$$(3+\lambda)/3 = 1 \implies \lambda = 0$$

Hence, $t_3 = (2X_1 + X_2)/3$.

page:16

---

## Solution: Step 2: Check Unbiasedness

*   **$t_1$**
    $E(t_1) = (\mu+\mu+\mu+\mu+\mu)/5 = \mu$
    $\checkmark$ $t_1$ is unbiased.

*   **$t_2$**
    $E(t_2) = (\mu+\mu)/2 + \mu = 2\mu$
    $\times$ $t_2$ is biased.

*   **$t_3$**
    With $\lambda=0$:
    $E(t_3) = (2\mu+\mu)/3 = \mu$
    $\checkmark$ $t_3$ is unbiased.

Unbiased estimators: $t_1$ and $t_3$

page:17

---

## Solution: Step 3 - Compare Variances
Let $\text{Var}(X_i) = \sigma^2$ and assume the observations are independent.

$\text{Var}(t_1) = \sigma^2/5$

$\text{Var}(t_2) = \sigma^2/2 + \sigma^2 = 3\sigma^2/2$

$\text{Var}(t_3) = (4\sigma^2 + \sigma^2)/9 = 5\sigma^2/9$

Comparison
$\sigma^2/5 < 5\sigma^2/9 < 3\sigma^2/2$

Therefore $t_1$ has the smallest variance among the unbiased estimators.

Best estimator $= t_1 = \bar{X}$

page:18

---

## Properties of a Good Point Estimator

**Example2:** Let $X_1$, $X_2$ and $X_3$ be a random sample of size 3 from a population with mean $\mu$ and variance $\sigma^2$. $T_1$, $T_2$ and $T_3$ are estimators used to estimate the mean $\mu$, where:

$T_1 = X_1 + X_2 - X_3$

$T_2 = 2X_1 + 3X_3 - 4X_2$

$T_3 = (\lambda X_1 + X_2 + X_3) / 3$

Answer the following:

1. Are $T_1$ and $T_2$ unbiased estimators?
2. Find the value of $\lambda$ such that $T_3$ is an unbiased estimator for $\mu$.
3. With the value of $\lambda$ obtained, is $T_3$ a consistent estimator?
4. Which one is the best estimator?

---

## Properties of a Good Point Estimator

**(ii) Finding value of $\lambda$ for $T_3$ to be unbiased**

Let $T_3 = \lambda (X_1 + X_2 + X_3) / 3$

For unbiasedness, $E(T_3) = \mu$

$E(T_3) = (\lambda / 3) [E(X_1) + E(X_2) + E(X_3)]$

$= (\lambda / 3)(\mu + \mu + \mu) = \lambda\mu$

For unbiasedness: $\lambda\mu = \mu \Rightarrow \lambda = 1$

**(iii) Consistency of $T_3$**

With $\lambda = 1, T_3 = (X_1 + X_2 + X_3) / 3 = \bar{X}$ (sample mean).

Since the sample mean is a consistent estimator of the population mean, $T_3$ is a consistent estimator.

---

## Properties of a Good Point Estimator

**(iv) Variance of the estimators:**

$$\text{Var}(T_1) = \text{Var}(X_1) + \text{Var}(X_2) + \text{Var}(X_3) = 3\sigma^2$$

$$\text{Var}(T_2) = 4\text{Var}(X_1) + 9\text{Var}(X_3) + 16\text{Var}(X_2) = 29\sigma^2$$

$$\text{Var}(T_3) = (1/9) [\text{Var}(X_1) + \text{Var}(X_2) + \text{Var}(X_3)]$$
$$= (1/9)(3\sigma^2)$$
$$= \sigma^2 / 3$$

Since $\text{Var}(T_3)$ is minimum, $T_3$ is the best estimator.

---

## Real-Life Numerical 1: Average Server Response Time

| Situation | Question | Solution |
| :--- | :--- | :--- |
| A service team records the response times (ms) of 8 randomly selected requests:<br><br>180, 210, 195, 220,<br>205, 190, 200, 240 | Estimate the population mean response time using a point estimator.<br><br>Also state the estimator and the estimate. | $\bar{X} = \frac{\text{sum of observations}}{8}$<br><br>$= \frac{1640}{8}$<br><br>$= 205 \text{ ms}$<br><br>Estimator: $\bar{X}$<br>Estimate: 205 ms |

page:19

---

## Real-Life Numerical 2: Packet Delivery Success

| Situation | Question | Solution |
| :--- | :--- | :--- |
| During a network test, 500 packets are transmitted. Of these, 465 are successfully delivered. | Estimate the probability p of successful packet delivery.<br><br>Identify the estimator used. | $\hat{p} = X/n$<br><br>$= 465/500$<br><br>$= 0.93$<br><br>Estimated success probability = 93%. |

page: 20

---

## Real-Life Numerical 3: Battery-Life Estimation

**Situation**

A sample of 25 devices has an average battery life of 8.4 hours. The population standard deviation is known to be 1.5 hours.

**Question**

Construct a 95% confidence interval for the population mean battery life.

Use $z_{0.975} = 1.96$.

**Solution**

$CI = \bar{X} \pm z(\sigma/\sqrt{n})$

$= 8.4 \pm 1.96(1.5/5)$

$= 8.4 \pm 0.588$

$CI \approx (7.81, 8.99)$ hours.

**Interpretation**: the interval gives a plausible range for the population mean.

page:21

---

## Quick Comparison: Three Real-Life Problems

**1. Response Time**

*   Parameter: $\mu$
*   Statistic: $\bar{X}$
*   Point estimate = 205 ms

**2. Packet Success**

*   Parameter: $p$
*   Statistic: $\hat{p}$
*   Point estimate = 0.93

**3. Battery Life**

*   Parameter: $\mu$
*   Statistic: $\bar{X}$
*   95% CI $\approx$ (7.81, 8.99)

Point estimation $\rightarrow$ one value    Interval estimation $\rightarrow$ range

page:22

---

## References

1. Devore, J. L., Probability & Statistics for Engineering and the Sciences, 8th Edition, Cengage Learning, 2012.
