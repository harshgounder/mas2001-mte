# lms-standard-error-clt

## Sampling Concepts & Limit Theorems
Population, Sample, Standard Error, and Central Limit Theorem with Practical Examples

---

## Population vs. Sample
The foundation of statistical inference

| Population (N) | Sample (n) |
| :--- | :--- |
| • Definition: The entire group of individuals, objects, or measurements that you want to draw conclusions about. | • Definition: A specific, smaller subset of the population collected to observe and analyze. |
| • Characteristics: Parameters (e.g., Population Mean $\mu$, Population Standard Deviation $\sigma$). | • Characteristics: Statistics (e.g., Sample Mean $\bar{x}$, Sample Standard Deviation $s$). |
| • Reality: Often too large, costly, or impossible to measure completely. | • Reality: Must be representative and randomly selected to avoid bias. |
| • Example: All 500,000 lightbulbs produced by a factory in a month. | • Example: 100 randomly chosen lightbulbs selected for quality testing. |

---

## (untitled)

Figure: A diagram illustrating simple random samples drawn from a population.
On the left, under the label "population", there is a group of ten circles arranged in two rows of five.
The top row contains circles labeled a, b, c, d, e.
The bottom row contains circles labeled f, g, h, i, j.
Circles a, b, g, and h are filled black with white text. The remaining circles are white with black text.
Three arrows point from the population to the right, under the text "simple random samples (without replacement)".
The arrows point to three distinct samples, each containing four circles:
1. The top sample contains circles a, c, j, b.
2. The middle sample contains circles i, e, a, f.
3. The bottom sample contains circles g, c, f, d.
In each sample, the circles retain their original colors (black or white) from the population.

---

## Understanding Standard Error (SE)
Measuring estimate precision

**What is Standard Error?**
Standard Error measures the variability or dispersion of a sample statistic (usually the sample mean) across multiple hypothetical samples. It quantifies how much your sample estimate is expected to deviate from the true population parameter.

**The Formula for Standard Error of the Mean (SEM):**
$$SE = \sigma / \sqrt{n}$$
Where: $\sigma$ = Population Standard Deviation | n = Sample Size

**Key Takeaway:** As sample size (n) increases, the Standard Error decreases. Larger samples lead to more precise estimates.

---

## Standard Error: Practical Example
Calculating precision step-by-step

**Scenario: Lightbulb Lifespan**
* A factory produces lightbulbs with a known population standard deviation ($\sigma$) of 100 hours.
* A quality control inspector randomly pulls a sample of 25 lightbulbs ($n = 25$) to test.
* Problem: Find the Standard Error of the Mean (SEM) for this sample size, and see what happens if we increase $n$ to 100.

**Calculation Steps:**
**Case 1 ($n = 25$):** $SE = 100 / \sqrt{25} = 100 / 5 = 20 \text{ hours}$
**Case 2 ($n = 100$):** $SE = 100 / \sqrt{100} = 100 / 10 = 10 \text{ hours}$

Interpretation: Quadrupling the sample size from 25 to 100 cut our standard uncertainty exactly in half (from 20 hours down to 10 hours).

---

## Central Limit Theorem

Statistics and Probability - MAS2001

---

## The Central Limit Theorem (CLT)
The bridge to modern data analysis

**Core Definition**
The Central Limit Theorem states that if you take sufficiently large samples from a population, the distribution of the sample means will follow a normal distribution (bell curve)-regardless of the population's underlying shape (even if it is heavily skewed, uniform, or bimodal).

**Three Critical Rules of CLT:**
1. Center Rule: The mean of the sample means will equal the population mean ($\mu_{\bar{x}} = \mu$).
2. Spread Rule: The standard deviation of the sample means will equal the Standard Error ($\sigma_{\bar{x}} = \sigma / \sqrt{n}$).
3. Shape Rule: As sample size n increases, the shape becomes normal. If $n \geq 30$, normality is assumed safely.

---

## Note:

1. For a population with any distribution, if $n > 30$, then the sample means will have a distribution that can be approximated by a normal distribution with mean $\mu$ and standard devisation $$ \frac{\sigma}{\sqrt{n}} $$ where n is the sample size.

2. If $n \leq 30$ and the original population has a normal distribution, then the sample means have a normal distribution with mean $\mu$ and standard deviation $$ \frac{\sigma}{\sqrt{n}} $$,where n is the sample size

3. if $n \leq 30$ and the original population does not have a normal distribution, then we cannot apply the CLT.

---

## (untitled)

Figure: (a) A plot showing Probability Density versus IQ Score. The x-axis is labeled "IQ Score" with ticks at 60, 80, 100, 120, and 140. The y-axis is labeled "Probability Density" with ticks at 0.000, 0.010, and 0.020. A smooth, bell-shaped curve is centered at an IQ score of 100, peaking at a density slightly above 0.020, and tapering down toward 0 near scores of 60 and 140.

Figure: (b) A histogram showing Frequency versus IQ Score. The x-axis is labeled "IQ Score" with ticks at 60, 80, 100, 120, and 140. The y-axis is labeled "Frequency" with ticks at 0, 5, 10, and 15. The bars represent frequencies across score intervals, with several bars reaching between 10 and 15.

Figure: (c) A histogram showing Frequency versus IQ Score. The x-axis is labeled "IQ Score" with ticks at 60, 80, 100, 120, and 140. The y-axis is labeled "Frequency" with ticks at 0, 400, 800, and 1200. The bars form a symmetric, bell-like distribution peaking at an IQ score of 100 with a frequency slightly above 1200.

(a)
(b)
(c)

---

## CENTRAL LIMIT THEOREM

MANIPAL UNIVERSITY JAIPUR

Normal
Uniform
Skewed
Random

Population
n = 10
n = 30

Figure: A grid of 12 plots arranged in 3 rows and 4 columns illustrating the Central Limit Theorem.
Columns (top labels): Normal, Uniform, Skewed, Random.
Rows (left labels): Population, n = 10, n = 30.
- Population row: Displays four distinct starting distributions: a symmetric bell curve (Normal), a flat rectangle (Uniform), a right-skewed curve (Skewed), and an irregular multi-modal shape (Random).
- n = 10 row: Displays the sampling distribution of means for each population with a sample size of 10. The shapes are more bell-like and centered than the original populations.
- n = 30 row: Displays the sampling distribution of means for each population with a sample size of 30. All four plots show nearly identical, narrow, symmetric bell-shaped curves.
Sampling Distribution of Means

---

## Central Limit Theorem: Practical Example
Applying normality to skewed distributions

**Scenario: Bank ATM Wait Times**

* The wait times at a bank ATM follow a heavily right-skewed distribution (most people finish fast, a few take a very long time).
* Population parameters: Mean wait time ($\mu$) = 4 minutes, Standard Deviation ($\sigma$) = 2 minutes.
* Problem: If we track a random sample of 36 customers ($n = 36$), what is the probability that their average wait time is greater than 4.5 minutes?

---

## Central Limit Theorem: Practical Example

**Solution Using CLT Steps:**

1. Apply Normality: Since $n = 36$ (which is $\ge 30$), the sampling distribution of means is Normal, even though individual wait times are skewed.

2. Calculate Standard Error: $SE = 2 / \sqrt{36} = 2 / 6 = 0.333$ minutes.

3. Find Z-Score: $Z = (\bar{x} - \mu) / SE = (4.5 - 4) / 0.333 = 0.5 / 0.333 = 1.50$.

4. Determine Probability: Looking up $Z = 1.50$ on a standard normal table gives an upper-tail probability of approximately 6.68%. Therefore, there is only a 6.68% chance a sample of 36 customers averages over 4.5 minutes.

---

## Example:
The amount of impurity in a batch of a chemical product is a random variable with mean value $4.0\text{ g}$ and standard deviation $1.5\text{ g}$. If 50 batches are independently prepared, what is the approximated probability that the average amount of impurity in these 50 batches is between $3.5\text{ g}$ and $3.8\text{ g}$?

---

## Example:

1. The amount of impurity in a batch of a chemical product is a random variable with mean value 4.0 g and standard deviation 1.5 g. If 50 batches are independently prepared, what is the approximated probability that the average amount of impurity in these 50 batches is between 3.5 g and 3.8 g?

**Solution:**

Given $\mu = 4, \sigma = 1.5, n = 50$

Using CLT, the average will follow the normal distribution with mean $(\mu) = 4$ and SD $= \frac{\sigma}{\sqrt{n}} = \frac{1.5}{\sqrt{50}}$

Then,

$$P(3.5 < \bar{X} < 3.8) = P\left(\frac{3.5 - 4}{\frac{1.5}{\sqrt{50}}} < \frac{\bar{X} - 4}{\frac{1.5}{\sqrt{50}}} < \frac{3.8 - 4}{\frac{1.5}{\sqrt{50}}}\right) = P(-2.36 < Z < -0.4)$$

$$\Rightarrow P(3.5 < \bar{X} < 3.8) = P(0 < Z < 2.36) - P(0 < Z < 0.4) = 0.4909 - 0.3264 = 0.1644$$

---

## Example:

2. A factory produces LED bulbs. The lifespan of these bulbs is heavily skewed. The mean life span is 50,000 hours with a standard deviation of 8,000 hours. A quality control inspector tests a random sample of 64 bulbs. What is the probability that the average lifespan of this batch is less than 48,000 hours?

---

## Example:

2. A factory produces LED bulbs. The lifespan of these bulbs is heavily skewed. The mean life span is 50,000 hours with a standard deviation of 8,000 hours. A quality control inspector tests a random sample of 64 bulbs. What is the probability that the average lifespan of this batch is less than 48,000 hours?

**Solution:**
Given $\mu = 50000, \quad \sigma = 8000, \quad n = 64$
Using CLT, the average will follow the normal distribution with mean $(\mu)= 50000$ and
SD $= \frac{\sigma}{\sqrt{n}} = \frac{8000}{\sqrt{64}}$
Then,

$$P(\bar{X} < 48000) = P \left( \frac{\bar{X} - 50000}{\frac{8000}{\sqrt{64}}} < \frac{48000 - 50000}{\frac{8000}{\sqrt{64}}} \right) = P(Z < -2)$$

$$P(\bar{X} < 48000) = P(-\infty < Z < 0) - P(0 < Z < 2) = 0.5 - 0.4772 = 0.0228$$

---

## Example:

3. The average life of a machine is 7 years with a standard deviation of 1 year. If the lives of these machines follow the normal distribution, find the probability that the average life of 9 random samples of such machines falls between 6.4 years to 7.2 years.

---

## Example:

3. The average life of a machine is 7 years with a standard deviation of 1 year. If the lives of these machines follow the normal distribution, find the probability that the average life of 9 random samples of such machines falls between 6.4 years to 7.2 years.

**Solution:** Given a population of machines and life time of machines follows a normal distribution with average life ($\mu$) = 7 and SD ($\sigma$) = 1.
Sample size ($n$) = 9
Using CLT we say that average life of the samples also follows the normal distribution with mean ($\mu$) = 7 and SD = $\frac{\sigma}{\sqrt{n}} = \frac{1}{3}$.
Then,
$$P(6.4 < \bar{X} < 7.2) = P\left( \frac{6.4-7}{\frac{1}{3}} < \frac{\bar{X}-7}{\frac{1}{3}} < \frac{7.2-7}{\frac{1}{3}} \right) = P(-1.8 < Z < 0.6)$$
$$P(6.4 < \bar{X} < 7.2) = P(-1.8 < Z < 0) + P(0 < Z < 0.6)$$
$$P(6.4 < \bar{X} < 7.2) = 0.4641 + 0.2257 = 0.6898$$

---

## References:

1. Devore, J. L. (2016). *Probability and statistics for engineering and the sciences* (9$^{\text{th}}$ ed.). Cengage Learning.
2. Gupta, S. C. & Kapoor, V. K. (2002). *Fundamentals of Mathematical Statistics* (10$^{\text{th}}$ ed.). Sultan Chand & Sons.
