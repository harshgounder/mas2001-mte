# ppt3-discrete-prob-dist

## Discrete Probability Distribution

Statistics and Probability -MAS2001

---

## Binomial Distribution

Discrete Probability Distribution

---

## (untitled)

Take the example of 5-coin tosses. What's the probability that you flip exactly 3 heads in 5-coin tosses?

Figure: A cartoon illustration of a boy with brown hair wearing a green shirt, flipping a coin into the air and looking up at it with both hands raised.

page:3

---

## Solution:
One way to get exactly 3 heads: HHHTT

What’s the probability of this exact arrangement?
$$P(\text{heads}) \times P(\text{heads}) \times P(\text{heads}) \times P(\text{tails}) \times P(\text{tails}) = (1/2)^3 \times (1/2)^2$$

Another way to get exactly 3 heads: THHHT
Probability of this exact outcome $= (1/2)^1 \times (1/2)^3 \times (1/2)^1 = (1/2)^3 \times (1/2)^2$

page:4

---

## (untitled)

In fact, $(1/2)^3 \times (1/2)^2$ is the probability of each unique outcome that has exactly 3 heads and 2 tails.

So, the overall probability of 3 heads and 2 tails is:
$$(1/2)^3 \times (1/2)^2 + (1/2)^3 \times (1/2)^2 + (1/2)^3 \times (1/2)^2 + \dots \text{ for as many unique arrangements as there are - but how many are there??}$$

page:5

---

## (untitled)

Figure: A diagram illustrating binomial outcomes for 3 heads in 5 coin flips, showing a binomial coefficient, a list of 10 outcomes with their equal probabilities, and a factorial formula.

$\binom{5}{3}$ ways to arrange 3 heads in 5 trials

$^5C_3 = 5!/3!2! = 10$

| Outcome | Probability |
| :--- | :--- |
| THHHT | $(1/2)^3 \times (1/2)^2$ |
| HHHTT | $(1/2)^3 \times (1/2)^2$ |
| TTHHH | $(1/2)^3 \times (1/2)^2$ |
| HTTHH | $(1/2)^3 \times (1/2)^2$ |
| HHTTH | $(1/2)^3 \times (1/2)^2$ |
| HTHHT | $(1/2)^3 \times (1/2)^2$ |
| THTHH | $(1/2)^3 \times (1/2)^2$ |
| HTHTH | $(1/2)^3 \times (1/2)^2$ |
| HHTHT | $(1/2)^3 \times (1/2)^2$ |
| THHTH | $(1/2)^3 \times (1/2)^2$ |

10 arrangements $\times (1/2)^3 \times (1/2)^2$

The probability of each unique outcome (note: they are all equal)

**Factorial review:** $n! = n(n-1)(n-2)...$

page:6

---

∴ P(3 heads and 2 tails)

$$
= \binom{5}{3} \times P(\text{heads})^3 \times P(\text{tails})^2
$$

$$
= 10 \times \left(\frac{1}{2}\right)^5 = 31.25\%
$$

---

## Binomial distribution

• Let a random experiment be performed repeatedly
• The occurrence of an event in a trial be called a success and its non-occurrence a failure.
• Consider a set of $n$ independent trials ($n$ being finite).
• The probability '$p$' of success in any trial is constant for each trial.
• Then $q = 1 - p$, is the probability of failure in any trial.

---

## Binomial distribution

*Definition:*

A random variable X is said to follow binomial distribution if it assumes only non-negative values and its 'Probability mass function is given by

$$
P(X = x) = \begin{cases} \binom{n}{x} p^x q^{n-x} & \text{for } x = 0, 1, 2, \dots n \\ 0, & \text{otherwise} \end{cases}
$$

---

## (untitled)

* The two independent constants $n$ and $p$ in the distribution are known as the parameters of the distribution.
* '$n$' is also, sometimes known as the degree of the binomial distribution.
* We shall use the notation $X \sim B(n, p)$ to denote that the random variable $X$ follow the binomial distribution with parameters $n$ and $p$.

---

## Physical conditions for Binomial Distribution

We get the binomial distribution under the following experimental conditions.

1) Each trial results in two mutually disjoint outcomes termed as success and failure.
2) The number of trials ‘$n$’ is finite.
3) The trials are independent of each other.
4) The probability of success ‘$p$’ is constant for-each trial.

---

## Mean and variance of binomial distribution

Mean = $E(X) = np$

Var(X) = $npq$

---

## Problem Statement

10% of pens manufactured by a company are defective. A box contains 12 pens.
Find the probability that the box contains:
(i) Exactly 2 defective pens (ii) At least 2 defective pens (iii) No defective pen

Given Parameters

| n (trials) | p (defective) | q = 1 - p | Distribution |
| :--- | :--- | :--- | :--- |
| 12 | 10/100 | 1 - 0.1 | X ~ B(12, 0.1) |
| (pens in box) | = 0.1 | = 0.9 | |

$$P(X = x) = \binom{n}{x} \cdot p^x \cdot q^{n-x} \quad \text{where } x = 0, 1, 2, \dots, n$$

page:13

---

## Part (i): Exactly 2 Defective Pens

Find $P(X = 2)$ where $n = 12, p = 0.1, q = 0.9$

**Step 1: Apply PMF Formula**
$$P(X = 2) = \binom{12}{2} \times (0.1)^2 \times (0.9)^{10}$$

**Step 2: Expand the Combination**
$$\binom{12}{2} = \frac{12!}{2! \times 10!} = 66$$

**Step 3: Compute**
$$66 \times (0.01) \times (0.3487) = 0.2301$$

$\checkmark P(X = 2) = 0.2301$

Binomial Distribution | Problems & Solutions

---

## Part (ii): At Least 2 Defective Pens

Find $P(X \ge 2) = 1 - P(X < 2) = 1 - [P(X = 0) + P(X = 1)]$

Strategy: Complement Rule

**P(X = 0)**
$$\binom{12}{0} \times (0.1)^0 \times (0.9)^{12}$$
$= 1 \times 1 \times 0.2824 = 0.2824$

**P(X = 1)**
$$\binom{12}{1} \times (0.1)^1 \times (0.9)^{11}$$
$= 12 \times 0.1 \times 0.3138 = 0.3766$

Final Calculation

$$P(X \ge 2) = 1 - [0.2824 + 0.3766] = 1 - 0.659 = 0.341$$

$$\checkmark P(X \ge 2) = 0.341$$

Binomial Distribution | Problems & Solutions

---

## Part (iii): No Defective Pen
Find P(X = 0) - probability that all 12 pens are non-defective
Apply PMF with x = 0
$$P(X = 0) = \binom{12}{0} \times (0.1)^0 \times (0.9)^{12}$$
Evaluate Each Term
$\binom{12}{0} = 1$
$(0.1)^0 = 1$
$(0.9)^{12} = 0.2824$
Multiply the terms
$$1 \times 1 \times 0.2824 = 0.2824$$
✓ P(X = 0) = 0.2824

---

## Problem 2: Irregular Six-Faced Die

**Problem Statement**

An irregular six-faced die is thrown. The probability of getting 5 even numbers in 10 throws is TWICE the probability of getting 4 even numbers in 10 throws.
In 10,000 sets of 10 throws each, how many times would you expect NO even number?

**Given Condition** $\rightarrow$ $P(X = 5) = 2 \cdot P(X = 4)$

$$\binom{10}{5} \cdot p^5 \cdot q^5 = 2 \times \binom{10}{4} \cdot p^4 \cdot q^6$$

Let $X$ = number of even numbers obtained | $n = 10$

**Finding $p$ (probability of getting an even number on one throw)**

$$252 \cdot p = 210 \cdot 2q \rightarrow 3p = 5q = 5(1-p) \rightarrow p = 5/8, \quad q = 3/8$$

Binomial Distribution | Problems & Solutions

---

## Problem 2: Finding Expected Sets

Parameters: n = 10, p = 5/8, q = 3/8

| n | p | q | Target |
| :---: | :---: | :---: | :---: |
| 10 | 5/8 = 0.625 | 3/8 = 0.375 | X = 0 |

**Step 1: Probability of getting NO even number (X = 0)**

$$P(X = 0) = {}^{10}C_0 \times (5/8)^0 \times (3/8)^{10} = (3/8)^{10} \approx 0.00005$$

**Step 2: Expected number of sets (out of 10,000)**

$$\text{Expected sets} = 10,000 \times P(X = 0) = 10,000 \times 0.00005$$

$\checkmark$ Expected sets with no even number $\approx$ 0.549

Interpretation: In 10,000 repetitions, we expect this rare event less than once on average.

Binomial Distribution | Problems & Solutions

---

## Poisson Distribution
Discrete Probability Distribution

---

## (untitled)
The Poisson probability distribution provides a good model for the probability distribution of the number of "rare events" that occur randomly .

---

## Following are some instances where Poisson distribution may be successfully employed

1) Number of deaths from a disease. Such as heart attack or cancer or due to snake bite.
2) Number of suicides reported in a particular city.
3) The number of defective material in a packing manufactured by a good concern.
4) Number of faulty blades in a packet of 100.
5) Number of air accidents in some unit of time.
6) Number of printing mistakes at each page of the book.
7) Number of cars passing a crossing per minute during the busy hours of a day.

---

## Poisson distribution is a limiting case of the binomial distribution under the following conditions:
1) n, the number of trials is indefinitely large, i.e., $n \to \infty$.
2) p, the constant probability of success for each trial is indefinitely small, i.e., $p \to 0$.
3) $np = \lambda$, (say), is finite. Thus $p = \frac{\lambda}{n}$, $q = 1 - \frac{\lambda}{n}$, where $\lambda$ is a positive real number.

---

## Definition:
• A random variable X is said to follow a Poisson distribution if it assumes only non-negative values and its probability mass function is given by
$$
P(X = x) = \begin{cases}
\frac{e^{-\lambda}\lambda^x}{x!}; & \text{x = 0, 1, 2, ... ......; } \lambda > 0 \\
0, & \text{otherwise}
\end{cases}
$$
• Here $\lambda$ is known as the parameter of the distribution.
• We shall use the notation X~P ($\lambda$) to denote that X is a Poisson variate with parameter $\lambda$.

---

## (untitled)

• Mean and variance of Poisson distribution

• Mean = $E(X) = \lambda$.

• Var $X = \lambda$

---

## Poisson Distribution Examples

**Example 1:**
A random variable X has a Poisson distribution with parameter $\lambda$ such that
$P(X=1) = (0.2) P(X=2)$. Find $P(X=0)$.

**Solution:**
For the Poisson distribution, the probability function is defined as:

$$P(X=x) = \frac{e^{-\lambda} \lambda^x}{x!}$$, where $\lambda$ is a parameter.

Given that, $P(x=1) = (0.2) P(X=2)$
$$\frac{e^{-\lambda} \lambda^1}{1!} = (0.2) \frac{e^{-\lambda} \lambda^2}{2!}$$
$$\Rightarrow \lambda = \frac{\lambda^2}{10}$$
$$\Rightarrow \lambda = 10$$

Now, substitute $\lambda = 10$, in the
formula, we get:
$$P(X=0) = \frac{e^{-\lambda} \lambda^0}{0!}$$
$$P(X=0) = e^{-10} = 0.0000454$$
Thus, $P(X=0) = 0.0000454$

---

## Example 2:
Telephone calls arrive at an exchange according to the Poisson process at a rate $\lambda= 2/\text{min}$.
Calculate the probability that exactly two calls will be received during each of the first 5 minutes of the hour.

**Solution:**
Assume that "$N$" be the number of calls received during a 1 minute period.
Therefore,
$P(N= 2) = \frac{e^{-2} \cdot 2^2}{2!}$
$P(N=2) = 2e^{-2}$
Now, "$M$" be the number of minutes among 5 minutes considered, during which exactly 2 calls will be received. Thus "$M$" follows a binomial distribution with parameters $n=5$ and $p= 2e^{-2}$.
$P(M=5) = 32 \times e^{-10}$
$P(M =5) = 0.00145$, where "$e$" is a constant, which is approximately equal to $2.718$.

---

## Example 3

**Example 3:** A life insurance company insures the lives of 5,000 men of age 42. If actuarial studies show the probability of any 42-year-old man dying in a given year to be 0.001, the probability that the company will have to pay 4 claims in a given year can be approximated by the Poisson distribution.

Number of men (n): 5,000
Probability of death (p): 0.001
lambda = 5,000 * 0.001 = 5
The Poisson probability mass function for finding the probability of exactly x events is:
$$P(X = x) = \frac{e^{-\lambda} \lambda^x}{x!},$$

Substituting our values:
$$P(X = 4) = \frac{e^{-\lambda} \lambda^4}{4!}$$
$$= 0.1745$$

---

## References

1. S.C. Gupta and V.K. Kapoor, *Fundamentals of Mathematical Statistics*, Sultan Chand & Sons.
S. Palaniammal, *Probability and Random Variables*, PHI Learning.
K. Sundarapandian, *Probability, Statistics and Queuing Theory*, PHI Learning.
