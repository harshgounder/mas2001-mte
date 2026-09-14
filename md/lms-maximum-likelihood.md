# lms-maximum-likelihood

## Maximum Likelihood Estimation(MLE)
Statistics and Probability - MAS2001

---

## Maximum Likelihood Estimation (MLE)

Content:

* Background & Motivations
* Meaning of Likelihood
* Examples to Understand MLE
* MLE of Binomial Distribution
* MLE of Poisson Distribution:

---

## Maximum Likelihood Estimation (MLE)

Suppose we have a **random sample** $X_1, X_2, ..., X_n$ whose assumed **probability distribution** depends on some unknown **parameter** $\theta$.

**Examples of Unknown Parameters in Different Distributions**
*   **For Binomial Distribution:**
    Unknown parameters $\rightarrow (n, p)$
*   **For Poisson Distribution:**
    Unknown parameter $\rightarrow \lambda$
*   **For Normal Distribution:**
    Unknown parameters $\rightarrow \mu, \sigma^2$

---

## Maximum Likelihood Estimation (MLE)

Suppose we have a random sample $X_1, X_2, ..., X_n$ whose assumed probability distribution depends on some unknown parameter $\theta$.

Our primary goal here will be to find a point estimator $u$, such that
$u(x_1, x_2, ..., x_n)$
is a "good" point estimate of $\theta$,
where $x_1, x_2, ..., x_n$ are the observed values of the random sample.

i.e., Our goal is to find a good estimate of $\theta$ using the data
$x_1, x_2, ..., x_n$
that we obtained from our specific random sample.

page:16

---

## Maximum Likelihood Estimation (MLE)

*   **Maximum Likelihood Estimation (MLE)** is a technique used for estimating the parameters of a given distribution using some observed data.
*   For example, if a population is known to follow a normal distribution, but the mean and variance are unknown, MLE can be used to estimate them using a limited sample of the population.
*   This is done by finding particular values of the mean and variance so that the observed data is the most likely result to have occurred.

---

## Maximum Likelihood Estimation (MLE)

**Example:** Suppose the weights of randomly selected Indian female college students are normally distributed with unknown mean $\mu$ and standard deviation $\sigma$.
A random sample of 10 Indian female college students yielded the following weights (in pounds):
115, 122, 130, 127, 149, 160, 152, 138, 149, 180
Using this data, we identify the likelihood function and the maximum likelihood estimator (MLE) of $\mu$.

*   It seems reasonable that a good estimate of the unknown parameter $\theta$ would be the value of $\theta$ that maximizes the probability, that is, the likelihood of getting the data we observed.
*   This is the reason why it is called the likelihood function.

---

## Maximum Likelihood Estimation (MLE)

**Definition:** Let $x_1, x_2, \ldots, x_n$ be observations from $n$ independent and identically distributed random variables drawn from a probability distribution that depends on some parameter $\theta$.

The goal of Maximum Likelihood Estimation (MLE) is to maximize the likelihood function:

$$L = f(x_1, x_2, \ldots, x_n \mid \theta) = \prod_{i=1}^{n} f(x_i \mid \theta)$$

For maximization, we have:

$$\frac{dL}{d\theta} = 0 \text{ and } \frac{d^2L}{d\theta^2} < 0$$

---

## Maximum Likelihood Estimation (MLE)

Since logarithm is a non-decreasing function, so for maximizing $L$, it is equivalently correct to maximize $\log L$, i.e.,

$$ \frac{1}{L} \frac{dL}{d\theta} = 0 \Rightarrow \frac{d \log L}{d\theta} = 0 $$

In other words, the log-likelihood function is easier to work with:

$$ \log L = \sum_{i=1}^{n} \log f(x_i|\theta) $$

Distribution can be Discrete or Continuous

Figure: A thought bubble on the right containing the formula $L = \prod_{i=1}^{n} f(x_i|\theta)$.

page:7

---

## Maximum Likelihood Estimation (MLE)

**For Discrete Case**

The simplest case is when both the distribution and the parameter space (the possible values of the parameters) are discrete, meaning that there are a finite number of possibilities for each.

In this case, the MLE can be determined by explicitly trying all possibilities.

**Example:** An unfair coin is flipped 100 times, and 61 heads are observed. The coin either has probability $\frac{1}{3}$, $\frac{1}{2}$, or $\frac{2}{3}$ of flipping a head each time it is flipped. Which of the three is the MLE?

---

## Maximum Likelihood Estimation (MLE)

**Solution:** Here the distribution is the **Binomial distribution** with $n = 100$.

**p.m.f of Binomial Distribution**
$$P(X=x) = \binom{n}{x} p^x (1-p)^{n-x}$$
where
$$0 \le p \le 1, x = 0,1,2, \dots, n$$

$$P(H = 61 \mid p = \frac{1}{3}) = \binom{100}{61} \left(\frac{1}{3}\right)^{61} \left(\frac{2}{3}\right)^{39} \approx 9.6 \times 10^{-9}$$
$$P(H = 61 \mid p = \frac{1}{2}) = \binom{100}{61} \left(\frac{1}{2}\right)^{61} \left(\frac{1}{2}\right)^{39} = 0.007$$
$$P(H = 61 \mid p = \frac{2}{3}) = \binom{100}{61} \left(\frac{2}{3}\right)^{61} \left(\frac{1}{3}\right)^{39} = 0.040$$

Since
$$P(H = 61 \mid p = \frac{2}{3})$$
is **maximum**, the **Maximum Likelihood Estimate (MLE)** is
$$\hat{p} = \frac{2}{3}$$

---

## Maximum Likelihood Estimation (MLE)

**Example:** An unfair coin is flipped 100 times, and 61 heads are observed. What is the MLE when nothing is previously known about the coin?
**Solution:** Since the distribution follows a Binomial distribution with parameter $p$. Here $n = 100$.
The likelihood function is
$$P(H = 61 \mid p) = \binom{100}{61} p^{61} (1 - p)^{39}$$

**For Maximization**
$$\frac{d}{dp} P(H = 61 \mid p) = 0$$
$$\Rightarrow \binom{100}{61} [61 p^{60} (1 - p)^{39} - 39 p^{61} (1 - p)^{38}] = 0$$
$$\Rightarrow p^{60} (1 - p)^{38} (61 - 100p) = 0 \Rightarrow p = 0, \frac{61}{100}, 1$$

**Likelihood Values**
$$P(H = 61 \mid p = 0) = 0$$
$$P\left(H = 61 \mid p = \frac{61}{100}\right) = \binom{100}{61} \left(\frac{61}{100}\right)^{61} \left(\frac{39}{100}\right)^{39}$$
$$P(H = 61 \mid p = 1) = 0$$

Since $P\left(H = 61 \mid p = \frac{61}{100}\right)$
is **maximum**, therefore the **Maximum Likelihood Estimator (MLE)** is $\hat{p} = \frac{61}{100}$

---

## Maximum Likelihood Estimation (MLE)

Example: For a random sample $x_1, x_2, ..., x_n$. Assume that $x_i$'s are independent Binomial random variables with unknown parameter $p$, find the maximum likelihood estimator of $p$.

Solution: For binomial distribution, we have

$$ p(x_i) = \binom{n}{x_i} p^{x_i} (1-p)^{n-x_i} ; \quad x_i = 0,1,2,...,n; p \in [0,1] $$

Figure: A red checkmark next to the binomial probability formula.

The likelihood function $L$ is defined as

$$ L = \prod_{i=1}^n p(x_i|\theta) = \prod_{i=1}^n \binom{n}{x_i} p^{x_i} (1-p)^{n-x_i} $$

Figure: A thought bubble containing the text "Our target is to find the MLE of p".

---

## Maximum Likelihood Estimation (MLE)

The likelihood function L is defined as

$$L = \prod_{i=1}^{n} p(x_i|\theta)$$

$$= \prod_{i=1}^{n} \binom{n}{x_i} p^{x_i} (1-p)^{n-x_i}$$

$$\Rightarrow \log L = \sum_{i=1}^{n} \left[ \log \binom{n}{x_i} + \log p^{x_i} + \log(1-p)^{n-x_i} \right]$$

$$\Rightarrow \log L = \sum_{i=1}^{n} \left[ \log \binom{n}{x_i} + x_i \log p + (n-x_i) \log(1-p) \right]$$

$$\Rightarrow \log L = \sum_{i=1}^{n} \log \binom{n}{x_i} + \log p \sum_{i=1}^{n} x_i + \log(1-p) \sum_{i=1}^{n} (n-x_i)$$

To maximize L, we have

$$\frac{d}{dp} \log L = 0 \Rightarrow \frac{1}{p} \sum x_i - \frac{1}{1-p} \sum (n-x_i) = 0$$

$$\Rightarrow \frac{1}{p} \sum x_i - \frac{n^2}{1-p} + \frac{1}{1-p} \sum x_i = 0$$

$$\Rightarrow \frac{1}{p(1-p)} \sum x_i = \frac{n^2}{1-p}$$

$$\Rightarrow \frac{1}{p} \sum x_i = n^2$$

$$\Rightarrow p = \frac{\sum x_i}{n^2}$$

$$\frac{d^2}{dp^2} \log L = -\frac{1}{p^2} \sum x_i + \frac{1}{(1-p)^2} \sum (n-x_i) < 0$$

> **Hence, the MLE of $p$ is $\frac{\sum x_i}{n^2}$**

---

## Maximum Likelihood Estimation (MLE)

**Example:** Find the **Maximum Likelihood Estimate (MLE)** of the parameter $\lambda$ of a **Poisson distribution** for a random sample $x_1, x_2, x_3, \dots, x_n$.

**Solution:** For **Poisson distribution**, we have
$$f(x_i) = \frac{e^{-\lambda}\lambda^{x_i}}{x_i!}, x_i = 0, 1, 2, \dots$$

**Likelihood Function**
The likelihood function $L$ is defined as
$$L = \prod_{i=1}^{n} f(x_i \mid \lambda)$$
$$L = \prod_{i=1}^{n} \frac{e^{-\lambda}\lambda^{x_i}}{x_i!}$$

**Log Likelihood**
$$\log L = \sum_{i=1}^{n} \log \left( \frac{e^{-\lambda}\lambda^{x_i}}{x_i!} \right) = \sum_{i=1}^{n} [\log e^{-\lambda} + \log \lambda^{x_i} - \log(x_i!)]$$
$$= \sum_{i=1}^{n} [-\lambda + x_i \log \lambda - \log(x_i!)] = -n\lambda + \left( \sum_{i=1}^{n} x_i \right) \log \lambda - \sum_{i=1}^{n} \log (x_i!)$$

---

## Maximum Likelihood Estimation (MLE)

MLE of Poisson Parameter  

$$\frac{d}{d\lambda} (\log L) = 0$$  
$$\Rightarrow -n + \frac{1}{\lambda} \sum_{i=1}^{n} x_i = 0$$  
$$\Rightarrow \lambda = \frac{\sum_{i=1}^{n} x_i}{n}$$  
$$\therefore \hat{\lambda} = \bar{x}$$  


Second Derivative Test  

$$\frac{d^2}{d\lambda^2} (\log L) = -\frac{1}{\lambda^2} \left( \sum_{i=1}^{n} x_i \right) < 0$$  


Hence, the MLE for $\lambda$ is the sample mean. $\hat{\lambda} = \bar{x}$  


**Example:** Find the MLE of the parameters $\mu$ and $\sigma^2$ of a normal distribution for a random sample $x_1, x_2, \ldots, x_n$.

---

## References

1. Devore, J. L., Probability & Statistics for Engineering and the Sciences, 8th Edition, Cengage Learning, 2012.
