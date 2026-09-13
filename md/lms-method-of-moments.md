# lms-method-of-moments

## Method of Moments(MOM)

Statistics and Probability - MAS2001

---

## Introduction

**Parameter Estimation**
Parameter estimation is the process of using sample data to estimate the values of unknown population parameters.

**Two Common Methods of Parameter Estimation**
1. Method of Moments (MOM)
2. Maximum Likelihood Estimation (MLE)

page:1

---

## THE METHOD OF MOMENTS WORKS BY EQUATING POPULATION MOMENTS WITH SAMPLE MOMENTS.

Population $r$-th moment about origin
$$\mu'_r = E(X^r)$$

Sample $r$-th moment
$$m'_r = \frac{1}{n} \sum_{i=1}^n X_i^r$$

Idea: Replace theoretical moments with sample moments and solve for unknown parameters.

---

## STEPS IN METHOD OF MOMENTS

Step 1: Write the Population Moments
Compute the first k theoretical (population) moments about the origin:
$$\mu_r' = E(X^r)$$

Step 2: Compute the Sample Moments
Compute the corresponding sample moments from the observed data:
$$m_r' = \frac{1}{n} \sum_{i=1}^{n} X_i^r$$

---

## STEPS IN METHOD OF MOMENTS

**Step 3: Equate Population and Sample Moments**

$$\mu'_r = m'_r, \quad r = 1, 2, \dots, k$$

**Step 4: Solve for Parameters**

Solve the resulting $k$ equations to obtain estimates of the unknown parameters.

**Step 5: State the MoM Estimators**

$$\hat{\theta}_1 = f_1(m'_1, m'_2, \dots), \quad \hat{\theta}_2 = f_2(m'_1, m'_2, \dots)$$

---

## EXAMPLE 1 - POISSON DISTRIBUTION

**Question**
Estimate the parameter $\lambda$ of a Poisson distribution using the Method of Moments.

**Solution**

$$P(X = x) = \frac{e^{-\lambda}\lambda^x}{x!}, \quad x = 0, 1, 2, \dots$$

$E(X) = \lambda \quad (\text{The parameter of the Poisson distribution})$

**Method of Moments says:**

$$\mu'_r = m'_r$$

---

## EXAMPLE 1 - POISSON DISTRIBUTION

**Step-by-Step Derivation**
Put $r = 1$

$\mu'_1 = \lambda$ (First population moment about origin)

$m'_1 = \frac{1}{n} \sum_{i=1}^{n} x_i = \bar{X}$

$\mu'_1 = m'_1$

**Solve for $\lambda$**

$$\lambda = \frac{1}{n} \sum_{i=1}^{n} x_i$$

$$\lambda = \bar{X}$$

$$\hat{\lambda}_{MoM} = \bar{X}$$

$$\hat{\lambda}_{MoM} = \bar{X}$$

---

## EXAMPLE 2 - EXPONENTIAL DISTRIBUTION

Question
Estimate the parameter $\lambda$ of the Exponential distribution using the Method of Moments.

Solution
$$f(x) = \lambda e^{-\lambda x}, \quad 0 \leq x < \infty$$

$$E(X) = \frac{1}{\lambda}$$

Method of Moments says:
$$\mu'_r = m'_r$$

---

## EXAMPLE 2 - EXPONENTIAL DISTRIBUTION (STEP-BY-STEP SOLUTION)

Step-by-Step Derivation
Put r = 1
μ′₁ = 1/λ
(First population moment about origin)
$$ m'_1 = \frac{1}{n} \sum_{i=1}^{n} x_i = \bar{X} $$
μ′₁ = m′₁

Solve for λ
$$ \frac{1}{\lambda} = \bar{X} $$
$$ \lambda = \frac{1}{\bar{X}} $$
$$ \boxed{ \hat{\lambda}_{\text{MoM}} = \frac{1}{\bar{X}} } $$

---

## Practice Question: Method of Moments Estimation

Consider the Pareto random variable X with probability density function

$$f(x) = \frac{3\theta^3}{x^4}, \quad x \geq \theta, \quad \theta > 0.$$

**Using the Method of Moments (MoM), estimate the unknown parameter $\theta$. Does the resulting moment estimator always make sense?**

**Think Before Solving: Identify the first population moment and equate it with the first sample moment.**

---

## References

1. Devore, J. L. (2016). *Probability and statistics for engineering and the sciences* (9th ed.). Cengage Learning.
2. Gupta, S. C. & Kapoor, V. K. (2002). *Fundamentals of Mathematical Statistics* ($10^{\text{th}}$ ed.). Sultan Chand & Sons.
3. Devore, J. L., *Probability & Statistics for Engineering and the Sciences*, 8th Edition, Cengage Learning, 2012.
4. K. Sundarapandian, *Probability, Statistics and Queuing Theory*, PHI Learning.
