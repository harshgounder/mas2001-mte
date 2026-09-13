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

## Mean and variance of binomial distribution

Mean = $E(X) = np$

Var(X) = $npq$
