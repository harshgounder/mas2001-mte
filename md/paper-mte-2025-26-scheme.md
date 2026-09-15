# paper-mte-2025-26-scheme

## Solution Scheme

MAS 2001 (Statistics and Probability)

**Q1.** $$\int_{-\infty}^{\infty} f(x)\,dx = 1$$ (2)

**Q2.** $$\frac{e^{x-e}}{x!}$$ (2)

**Q3.** It contains all the information needed about the parameter (2)

**Section-B**

**Q.4** $$\int_{-\infty}^{\infty} f(x)\,dx = 1$$

$$k\int_{-\infty}^{\infty} x^3(4-x)^2\,dx = 1 \;\Rightarrow\; K = \frac{15}{1024}$$ (1)

$$\text{mean} = \mu_1' = \int_{-\infty}^{\infty} x f(x)\,dx = \frac{15}{1024}\int_0^4 x^4(4-x)^2\,dx$$

$$= \frac{16}{7}$$ (1)

$$\mu_2' = \int_{-\infty}^{\infty} x^2 f(x)\,dx = \frac{15}{1024}\int_0^4 x^5(4-x)^2\,dx = \frac{40}{7}$$ (1)

$$\text{variance} = \mu_2' - (\mu_1')^2 = \frac{40}{7} - \left(\frac{16}{7}\right)^2 = \frac{24}{49}$$ (1)

**Q5.** Given $\mu = 10$, $\sigma^2 = 4$, $\Rightarrow \sigma = 2$

Chebyshev's Inequality

$$P(|x - \mu| \geq k\sigma) \leq \frac{1}{k^2}$$ (1)

and $P(|x - 10| \geq c) \leq 0.04$ (given) comparing with Chebyshev's inequality

$$c = k\sigma, \quad \text{and} \quad \frac{1}{k^2} = 0.04 \;\Rightarrow\; k^2 = 25$$ (1)

$$K = \sqrt{25} = 5 \quad \text{(K must be positive)}$$ (1)

$$c = k\sigma = 5 \times 2 = 10 \quad \underline{\text{Ans}}$$ (1)

page:1

---

## (untitled)

**Q6** Let $X$ : length of a telephone conversation. (1)

Given $X$ follow exponential distribution, then mean of exponential distribution is $= \frac{1}{\lambda} = 3$

$\Rightarrow \lambda = \frac{1}{3}$

Then

$$f(x) = \begin{cases} \lambda e^{-\lambda x}, & x \geq 0 \\ 0, & \text{otherwise} \end{cases} = \begin{cases} \frac{1}{3} e^{-\frac{1}{3}x}, & x \geq 0 \\ 0, & \text{otherwise} \end{cases} \quad (1)$$

(i)

$$P(X > 1) = \int_1^{\infty} f(x)\,dx = \int_1^{\infty} \frac{1}{3} e^{-\frac{1}{3}x}\,dx = e^{-\frac{1}{3}} \quad (1)$$

(ii)

$$P(X < 3) = \int_0^{3} f(x)\,dx = \int_0^{3} \frac{1}{3} e^{-\frac{1}{3}x}\,dx = 1 - \frac{1}{e} \quad (1)$$

**Q7** Let $X_i$ denote the average life of a machine,

$E(X_i) = \mu = 7$ years , S.D. $= \sigma = 1$ year.

Let $\bar{X}$ denote the sample mean of such machines falls between 6.4 and 7.2 years. (1)

By central limit theorem, $\bar{X}$ follows standard normal distribution with mean 7 years and standard deviation $= \frac{\sigma}{\sqrt{n}} = \frac{1}{\sqrt{9}} = \frac{1}{3}$ when $n = 9$ sample size. (1)

$$P(6.4 < \bar{X} < 7.2) = P\left( \frac{6.4 - 7}{1/3} < \frac{\bar{X} - 7}{1/3} < \frac{7.2 - 7}{1/3} \right)$$

$$= P(-1.8 < Z < 0.6) \quad (1)$$

$$= P(-1.8 < Z < 0) + P(0 < Z < 0.6)$$

$$= 0.4641 + 0.2257 = 0.6898 \quad (1)$$

---

## Section-C

**Q.8**

**(1)** Assuming that the number of mistakes per page $X$ follows Poisson distribution with parameter $\lambda$. Probability of making no mistake in a page is $= P(0) = e^{-\lambda}$ (1)

If less than 1% of the letters are rejected, then more than 99% of the letters are accepted, i.e. the probability of making no mistake in a page is at least $= 0.99$

Hence
$$e^{-\lambda} \geq 0.99 \qquad (1)$$

But $\lambda = np = 200p$, where $p$ is the probability of making mistake in typing a word.

$$\therefore \quad e^{-200p} \geq 0.99 \;\Rightarrow\; -200p(\log 2.72) \geq \log(0.99)$$

$$\Rightarrow \quad -p(200 \times 0.4346) \geq -0.0044$$

$$\Rightarrow \quad p \leq \frac{0.0044}{86.92} = 0.0000506 \qquad (1)$$

**(2)** The day's work of 20 letters of 200 words each is accepted, when there is no mistake in any of the $n = 20 \times 200 = 4000$ words. Assuming Poisson distribution probability of no mistake in the day's work $= e^{-\lambda}$ where $\lambda = np = 4000p$. We want to find $p$ such that

$$\therefore \quad e^{-4000p} = 0.90 \;\Rightarrow\; -4000p(\log 2.72) = \log(0.90)$$

$$\Rightarrow \quad -p(4000 \times 0.4346) = -0.0458$$

$$\Rightarrow \quad p = \frac{0.0458}{1738.4} = 0.0000263 \qquad (1)$$

page:3

---

## Q8 (11)

Top right corner: 6 (4)

We have $V(t) = E(t-\theta)^2$ (red pen: arrow to circled 1)

$$= E(t^2) - 2\theta E(t) + \theta^2$$

$$= E(t^2) - \theta^2$$ (red pen: arrow to circled 1)

Since $\mathrm{var}(t) \neq 0$ we have $E(t^2) - \theta^2 \neq 0$

i.e. $E(t^2) \neq \theta^2$ (red pen: circled mark, illegible)

Thus $t^2$ is a biased estimator of $\theta^2$. (red pen: arrow to circled 1)
