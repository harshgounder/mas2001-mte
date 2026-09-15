# paper-mte-2024-25-scheme

## MAS 2001: Solution Scheme

B.Tech: III (CSE|AIML|ECE|EE)

Section - A

Q.A (1) 6 (a)

Q.A (2) B (2)

Q.A (3) (C) D (1+1)

Section (B)

Q.B (1) Let $X \sim P(\lambda_1)$ and $Y \sim P(\lambda_2)$

Thus, we have,

$$P(X=x) = \frac{e^{-\lambda_1}\lambda_1^{x}}{x!} \;;\; x = 0, 1, 2, \ldots, \; \lambda_1 > 0$$

$$P(Y=y) = \frac{e^{-\lambda_2}\lambda_2^{y}}{y!} \;;\; y = 0, 1, 2, \ldots, \; \lambda_2 > 0 \qquad (1)$$

Using given condition, we get (1)

$$\lambda_1 e^{-\lambda_1} = \frac{\lambda_1^2 e^{-\lambda_1}}{2!} \quad \text{and} \quad \frac{\lambda_2^2 e^{-\lambda_2}}{2!} = \frac{\lambda_2^3 e^{-\lambda_2}}{3!}$$

Solving (1), we get $\lambda_1 = 2$ and $\lambda_2 = 3$ as $\lambda_1, \lambda_2 > 0$

Now $V(X) = \lambda_1 = 2$ ; $V(Y) = \lambda_2 = 3$ (1)

Hence

$$V(X-2Y) = 1^2 V(X) + (-2)^2 V(Y)$$

$$= 2 + 4 \times 3 = 14$$ [illegible] (1)

page:1

---

## (untitled)

[illegible]

2.62 : let time of speaking in the exponentially distributed r.v.(X) with parameter $\lambda = \frac{1}{4}$

(i)
$$P(X>6)=\int_{6}^{\infty}\frac{1}{4}\,e^{-x/4}\,dx=\frac{1}{4}\int_{6}^{\infty}e^{-x/4}\,dx$$

$$=\frac{1}{4}\cdot\frac{e^{-x/4}}{-\frac{1}{4}}\Big|_{6}^{\infty}=0.2231\qquad(1)$$

(ii)
$$P(7<X<12)=\int_{7}^{12}\frac{1}{4}\,e^{-x/4}\,dx=\frac{1}{4}\cdot\frac{e^{-x/4}}{-\frac{1}{4}}\Big|_{7}^{12}$$

$$=-\,e^{-x/4}\Big|_{7}^{12}=-\left(e^{-3}-e^{-7/4}\right)\qquad(1)$$

$$=e^{-7/4}-e^{-3}=0.17377-0.04978=0.12399$$

(iii)
$$P(X\leq 5)=\int_{0}^{5}\frac{1}{4}\,e^{-x/4}\,dx=\frac{1}{4}\cdot\frac{e^{-x/4}}{-\frac{1}{4}}\Big|_{0}^{5}\qquad(1)$$

$$=-\left[\,e^{-5/4}-e^{0}\,\right]=1-e^{-5/4}$$

$$=1-0.2865=0.7135$$

(iv)
$$\text{Mean}=\frac{1}{\lambda}=\frac{1}{1/4}=4\;;\qquad\text{Variance}=\frac{1}{\lambda^{2}}=\frac{1}{(1/4)^{2}}=16$$

Red annotations below the line: $\left(\frac{1}{4}\right)$ under the Mean result and $\left(\frac{1}{4}\right)^{2}$ under the Variance result.

---

## Q8(3)

since $f(x) = \frac{1}{2}$ ; $-1 \le x \le 1$

So, we have

$$\mu = E(X) = 0$$

$$\sigma^2 = V(X) = \frac{1}{3}$$ (1)

Also, from Chebyshev's inequality, we have

$$P[|X - \mu| \ge k\sigma] \le \frac{\sigma^2}{k^2\sigma^2} = \frac{1}{k^2}$$

$\Rightarrow$ $$P[|X - \mu| \ge 2\sigma] \le \frac{\sigma^2}{4\sigma^2} = \frac{1}{4}$$ (1)

Thus the upper bound of the given probability is $\frac{1}{4}$.

Now from the values of $\mu$ and $\sigma^2$, we have

$$P[|X - 0| \ge \frac{2}{\sqrt{3}}] = 1 - P[|X| \le \frac{2}{\sqrt{3}}]$$ (2)

$$= 1 - P\left[-\frac{2}{\sqrt{3}} \le X \le \frac{2}{\sqrt{3}}\right] = 1 - P[-1.1547 \le X \le 1.1547]$$

$$= 1 - P[-1 \le X \le 1] = 1 - 1 = 0$$

page:5

---

## (untitled)

Page

Q. B4 :- Let X be the random variable representing the number of minutes past 9 that the passenger arrives at station. So, $f(x) = \frac{1}{30}$ (1)

(a) He has to wait for less than 6 minutes if he arrives between 9:09 and 9:15 or 9:24 and 9:30. So required probability

$$P(9 < X < 15) + P(24 < X < 30) \quad (1.5)$$

$$= \int_{9}^{15} \frac{1}{30}\, dx + \int_{24}^{30} \frac{1}{30}\, dx = \frac{1}{5} + \frac{1}{5} = \frac{2}{5}$$

(b) Required probability $= P(0 < X < 5) + P(15 < X < 20)$

$$= \frac{1}{6} + \frac{1}{6} = \frac{1}{3} \quad (1.5)$$

Section: C

Q.C (a) Given $X \sim N(3.6, 34.5)$, $\sigma = 5.87$

(i) We need $P(X > 6)$

$$Z = \frac{X - \mu}{\sigma} = \frac{6 - 3.6}{5.87} = 0.58 \quad (1)$$

$P(X > 6) = P(Z > 0.58) = 1 - P(Z < 0.58) = 0.281$

(ii) $P(X < 1)$

$$Z = \frac{X - \mu}{\sigma} = \frac{1 - 3.6}{5.87} = -0.27 \quad (1)$$

$P(X < 1) = P(Z < -0.27) = 0.3936$

---

## (untitled)

(iii) $P(1.5 < X < 4.6)$

$$z_1 = \frac{x_1 - \mu}{\sigma} = -0.19 \quad ; \quad z_3 = \frac{x_3 - \mu}{\sigma} = 0.34$$

$$P(1.5 < X < 4.6) = P(-0.19 < Z < 0.34) = P(Z < 0.34) - P(Z < -0.19)$$

$$= 0.6331 - 0.4247 = 0.2084 \quad (1)$$

(iv) Let $Y$ be the randomly selected days in which the rainfalls range from $1.5$ mm to $4.6$ mm. The probability of a day having such amount of rainfall is $p = 0.2084$. There $q = 1 - p = 0.7916$. we have

$$P(Y = y) = \binom{7}{y}(0.2084)^y(0.7916)^{7-y} \quad ; \quad y = 0, 1, 2, \ldots, 7$$

$\therefore \; P(Y \leq 2) = P(y=0) + P(y=1) + P(y=2) \quad (1)$

$$= \binom{7}{0}(0.7916)^7 + \binom{7}{1}(0.2084)(0.7916)^6$$

$$+ \binom{7}{2}(0.2084)^2(0.7916)^5 \approx 0.83722$$

Q.C(b) Let $n$ and $p$ be the parameters. Thus we have,

$$P(X = x) = \binom{n}{x}p^x q^{n-x} \quad \text{where } x = 0, 1, \ldots, n \text{ and } p + q = 1$$

By question, we have $(1)$

$$\text{mean} = np = \frac{5}{3} \quad ; \quad P(X=2) = P(X=1)$$

$$\binom{n}{2}p^2 q^{n-2} = \binom{n}{1}p^1 q^{n-1} \Rightarrow p = \frac{1}{3}, \; q = \frac{2}{3}$$

page:5

---

## (untitled)

we have $n = 5$

Now, the Variance of the distribution $= npq = 5 \times \frac{1}{3} \times$ [illegible] $= \frac{10}{9}$

$P(X = \text{at least } 1) = P(X \geq 1) = 1 - P(X \leq 0) = 1 - P(X = 0)$

$$= 1 - \binom{5}{0}\left(\frac{1}{3}\right)^{0}\left(\frac{2}{3}\right)^{5} = \frac{211}{243} \qquad (1.5)$$

$P(X = \text{at most } 1) = P(X = 0) + P(X = 1)$

$$= \left(\frac{2}{3}\right)^{5} + \binom{5}{1}\left(\frac{1}{3}\right)^{1}\left(\frac{2}{3}\right)^{4} = \frac{112}{243} \qquad (1.5)$$

Figure: a horizontal decorative divider drawn across the page below the worked solution, made of double-headed arrows alternating with asterisk marks (arrow, star, arrow, star, arrow, star, arrow).

For more material and PYQs, checkout [website] and MUJstella app on Playstore

page:6
