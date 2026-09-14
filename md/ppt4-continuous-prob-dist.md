# ppt4-continuous-prob-dist

## Continuous Probability Distribution

Statistics and Probability -MAS2001

---

## Probability Distributions

Figure: A flowchart diagram titled "Probability Distributions". A central box at the top labeled "Probability Distributions" branches down to two main categories: "Discrete Probability Distributions" on the left and "Continuous Probability Distributions" on the right. Below "Discrete Probability Distributions", there are two additional boxes: "Binomial" and "Poisson". Below "Continuous Probability Distributions", there are three additional boxes: "Uniform", "Normal", and "Exponential".

---

## The Uniform Distribution
• The uniform distribution is a probability distribution that has equal probabilities for all possible outcomes of the random variable

Figure: A plot of the uniform probability density function, f(x), versus x. The graph shows a rectangular shape with height extending from the horizontal axis to a constant level between x_min and x_max on the x-axis. The x-axis is labeled x with tick marks at x_min and x_max. An arrow points to the shaded rectangular area with a callout box stating "Total area under the uniform probability density function is 1.0".

Statistics for Business and Economics, 6e ©
2007 Pearson Education, Inc.

---

## The Uniform Distribution (continued)

The Continuous Uniform Distribution:

$$f(x) = \begin{cases} \frac{1}{b-a} & \text{if } a \le x \le b \\ 0 & \text{otherwise} \end{cases}$$

where
$f(x) =$ value of the density function at any $x$ value
$a =$ minimum value of $x$
$b =$ maximum value of $x$

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## Properties of the Uniform Distribution

* The mean of a uniform distribution is
$$\mu = \frac{a + b}{2}$$

* The variance is
$$\sigma^2 = \frac{(b - a)^2}{12}$$

Statistics for Business and Economics, 6e ©
2007 Pearson Education, Inc.

---

## Uniform Distribution Example

Example: Uniform probability distribution over the range $2 \le x \le 6$:

$$f(x) = \frac{1}{6 - 2} = .25 \quad \text{for } 2 \le x \le 6$$

Figure: A plot of the probability density function $f(x)$ for a uniform distribution. The y-axis is labeled $f(x)$ with a tick at $.25$. The x-axis is labeled $x$ with ticks at $2$ and $6$. The distribution is represented by a blue rectangle from $x = 2$ to $x = 6$ with a constant height of $0.25$.

$$\mu = \frac{a + b}{2} = \frac{2 + 6}{2} = 4$$

$$\sigma^2 = \frac{(b - a)^2}{12} = \frac{(6 - 2)^2}{12} = 1.333$$

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## The Normal Distribution

Figure: A hierarchical flowchart. At the top is a box labeled "Probability Distributions". A line connects it to a box below labeled "Continuous Probability Distributions". A line from this box branches into three boxes arranged vertically on the right: "Uniform", "Normal" (which has a light blue background), and "Exponential".

Statistics for Business and Economics, 6e © 2007 Pearson Education,
Inc.

---

## The Normal Distribution (continued)

* Bell Shaped
* Symmetrical
* Mean, Median and Mode are Equal

Location is determined by the mean, $\mu$

Spread is determined by the standard deviation, $\sigma$

The random variable has an infinite theoretical range:
$+\infty$ to $-\infty$

Figure: A bell-shaped curve graphed on a coordinate system. The vertical axis is labeled $f(x)$ and the horizontal axis is labeled $x$. The peak of the curve is positioned at the mean $\mu$ on the horizontal axis. A bracket indicating the distance from the mean to the inflection point is labeled $\sigma$. To the right of the graph, the text reads "Mean = Median = Mode".

---

## The Normal Distribution (continued)
- The normal distribution closely approximates the probability distributions of a wide range of random variables
- Distributions of sample means approach a normal distribution given a “large” sample size (Will say more on this later!!)
- Computations of probabilities are direct and elegant
- The normal probability distribution has led to good business decisions for a number of applications

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## Many Normal Distributions

Figure: A plot showing three normal distribution curves on a purple shaded background. One curve is tall and narrow, a second curve is medium in height and width, and a third curve is shorter and wider. No axis labels or numeric ticks are visible.

By varying the parameters $\mu$ and $\sigma$, we obtain different normal distributions

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## (untitled)

Figure: A bell-shaped normal distribution curve. The vertical axis is labeled $f(x)$ and the horizontal axis is labeled $x$. The center of the curve is marked $\mu$ on the $x$-axis. A horizontal double-headed arrow under the peak is labeled $\sigma$.

Changing $\mu$ shifts the distribution left or right.
Changing $\sigma$ increases or decreases the spread.

Given the mean $\mu$ and variance $\sigma$ we define the normal distribution using the notation

$$X \sim N(\mu, \sigma^2)$$

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## The Normal Probability Density Function

• The formula for the normal probability density function is

$$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-(x-\mu)^2 / 2\sigma^2}$$

Where
e = the mathematical constant approximated by 2.71828
$\pi$ = the mathematical constant approximated by 3.14159
$\mu$ = the population mean
$\sigma$ = the population standard deviation
x = any value of the continuous variable, $-\infty < x < \infty$

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## Cumulative Normal Distribution

* For a normal random variable $X$ with mean $\mu$ and variance $\sigma^2$, i.e., $X \sim N(\mu, \sigma^2)$, the cumulative distribution function is

$$F(x_0) = P(X \le x_0)$$

Figure: A normal distribution curve with the vertical axis labeled $f(x)$ and the horizontal axis labeled $X$. The horizontal axis has ticks at $0$ and $x_0$. The area under the curve to the left of $x_0$ is shaded red. An arrow points to the shaded area with the label $P(X \le x_0)$.

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## Finding Normal Probabilities

The probability for a range of values is measured by the area under the curve

$$P(a < X < b) = F(b) - F(a)$$

Figure: A normal distribution curve on a horizontal axis labeled x. The mean is marked as μ. A point a is marked to the left of μ and a point b is marked to the right of μ. The area under the curve between a and μ is shaded red, and the area between μ and b is shaded blue.

Statistics for Business and Economics, 6e ©
2007 Pearson Education, Inc.

---

## Finding Normal Probabilities (continued)

- $F(b) = P(X < b)$
- $F(a) = P(X < a)$
- $P(a < X < b) = F(b) - F(a)$

Figure: A normal distribution curve. The horizontal axis is labeled $x$ with marks at $a$, $\mu$, and $b$. The area under the curve to the left of $b$ is shaded pink.

Figure: A normal distribution curve. The horizontal axis is labeled $x$ with marks at $a$, $\mu$, and $b$. The area under the curve to the left of $a$ is shaded cyan.

Figure: A normal distribution curve. The horizontal axis is labeled $x$ with marks at $a$, $\mu$, and $b$. The area under the curve between $a$ and $b$ is shaded. The region from $a$ to $\mu$ is red, and the region from $\mu$ to $b$ is blue.

Statistics for Business and Economics, 6e ©
2007 Pearson Education, Inc.

---

## (untitled)
$Z \sim N(0,1)$

Figure: A standard normal distribution curve, labeled $f(Z)$ on the vertical axis and $Z$ on the horizontal axis. The curve is bell-shaped and symmetric, centered at 0 on the horizontal axis. A vertical line is drawn at 0, with a horizontal arrow from the peak to the right labeled "1", indicating the standard deviation.

$$Z = \frac{X - \mu}{\sigma}$$

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## (untitled)
MANIPAL UNIVERSITY JAIPUR
NAAC A+ GRADE WITH 3.28 SCORE
$Z = \frac{X - \mu}{\sigma} = \frac{200 - 100}{50} = 2.0$
Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## Comparing X and Z units

Figure: A green bell-shaped normal distribution curve with a vertical line at the mean. Below the horizontal axis, the top row shows numeric ticks 100 and 200, labeled as X ($\mu = 100, \sigma = 50$). The bottom row (in red) shows numeric ticks 0 and 2.0, labeled as Z ($\mu = 0, \sigma = 1$).

Note that the distribution is the same, only the scale has changed. We can express the problem in original units (X) or in standardized units (Z)

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## Finding Normal Probabilities

$$P(a < X < b) = P\left(\frac{a-\mu}{\sigma} < Z < \frac{b-\mu}{\sigma}\right)$$
$$= F\left(\frac{b-\mu}{\sigma}\right) - F\left(\frac{a-\mu}{\sigma}\right)$$

Figure: A bell-shaped normal distribution curve. The y-axis is labeled \( f(x) \). The x-axis has two scales. The top scale is labeled \( x \) with points marked at \( a \), \( \mu \), and \( b \). The bottom scale is labeled \( Z \) with corresponding points at \( \frac{a-\mu}{\sigma} \), \( 0 \), and \( \frac{b-\mu}{\sigma} \). The area under the curve between \( a \) and \( b \) (corresponding to \( Z \)-scores between \( \frac{a-\mu}{\sigma} \) and \( \frac{b-\mu}{\sigma} \)) is shaded orange. An arrow points from the formula box to the shaded region.

Statistics for Business and Economics, 6e ©
2007 Pearson Education, Inc.

---

## Probability as Area Under the Curve

The **total area under the curve is 1.0**, and the curve is symmetric, so half is above the mean, half is below

Figure: A green bell-shaped curve (normal distribution) on a coordinate system. The vertical axis is labeled $f(X)$ and the horizontal axis is labeled $X$. The curve is symmetric and centered at $\mu$ on the $X$-axis. Two boxes with arrows point to the areas under the curve: the left box contains $P(-\infty < X < \mu) = 0.5$ pointing to the left half, and the right box contains $P(\mu < X < \infty) = 0.5$ pointing to the right half. A box at the bottom states $P(-\infty < X < \infty) = 1.0$.

Statistics for Business and Economics, 6e ©
2007 Pearson Education, Inc.

---

## Appendix Table 1

- The Standardized Normal table in the textbook (Appendix Table 1) shows values of the cumulative normal distribution function

- For a given Z-value a, the table shows $F(a)$ (the area under the curve from negative infinity to a)

Figure: A standard normal distribution bell curve with the horizontal axis labeled "Z". The center of the curve is marked "0". A point "a" is marked to the right of 0 on the Z-axis. The entire area under the curve to the left of "a" (from negative infinity to a) is shaded in red. A text box points to the shaded area with the equation $F(a) = P(Z < a)$.

Statistics for Business and Economics, 6e ©
2007 Pearson Education, Inc.

---

## STANDARD STATISTICAL TABLES

1. Areas under the Normal Distribution

The table gives the cumulative probability up to the standardised normal value $z$.

i.e.
$$
P[\,Z < z\,] = \int_{-\infty}^{z} \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{1}{2}t^2\right) dt
$$

Figure: A standard normal distribution curve. The area under the curve to the left of a point $z$ on the horizontal axis is shaded. The shaded area is labeled P[ Z < z ].

| z    | 0.00   | 0.01   | 0.02   | 0.03   | 0.04   | 0.05   | 0.06   | 0.07   | 0.08   | 0.09   |
|------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0.0  | 0.5000 | 0.5040 | 0.5080 | 0.5120 | 0.5159 | 0.5199 | 0.5239 | 0.5279 | 0.5319 | 0.5359 |
| 0.1  | 0.5398 | 0.5438 | 0.5478 | 0.5517 | 0.5557 | 0.5596 | 0.5636 | 0.5675 | 0.5714 | 0.5753 |
| 0.2  | 0.5793 | 0.5832 | 0.5871 | 0.5910 | 0.5948 | 0.5987 | 0.6026 | 0.6064 | 0.6103 | 0.6141 |
| 0.3  | 0.6179 | 0.6217 | 0.6255 | 0.6293 | 0.6331 | 0.6368 | 0.6406 | 0.6443 | 0.6480 | 0.6517 |
| 0.4  | 0.6554 | 0.6591 | 0.6628 | 0.6664 | 0.6700 | 0.6736 | 0.6772 | 0.6808 | 0.6844 | 0.6879 |
| 0.5  | 0.6915 | 0.6950 | 0.6985 | 0.7019 | 0.7054 | 0.7088 | 0.7123 | 0.7157 | 0.7190 | 0.7224 |
| 0.6  | 0.7257 | 0.7291 | 0.7324 | 0.7357 | 0.7389 | 0.7422 | 0.7454 | 0.7486 | 0.7517 | 0.7549 |
| 0.7  | 0.7580 | 0.7611 | 0.7642 | 0.7673 | 0.7704 | 0.7734 | 0.7764 | 0.7794 | 0.7823 | 0.7852 |
| 0.8  | 0.7881 | 0.7910 | 0.7939 | 0.7967 | 0.7995 | 0.8023 | 0.8051 | 0.8078 | 0.8106 | 0.8133 |
| 0.9  | 0.8159 | 0.8186 | 0.8212 | 0.8238 | 0.8264 | 0.8289 | 0.8315 | 0.8340 | 0.8365 | 0.8389 |
| 1.0  | 0.8413 | 0.8438 | 0.8461 | 0.8485 | 0.8508 | 0.8531 | 0.8554 | 0.8577 | 0.8599 | 0.8621 |
| 1.1  | 0.8643 | 0.8665 | 0.8686 | 0.8708 | 0.8729 | 0.8749 | 0.8770 | 0.8790 | 0.8810 | 0.8830 |
| 1.2  | 0.8849 | 0.8869 | 0.8888 | 0.8907 | 0.8925 | 0.8944 | 0.8962 | 0.8980 | 0.8997 | 0.9015 |
| 1.3  | 0.9032 | 0.9049 | 0.9066 | 0.9082 | 0.9099 | 0.9115 | 0.9131 | 0.9147 | 0.9162 | 0.9177 |
| 1.4  | 0.9192 | 0.9207 | 0.9222 | 0.9236 | 0.9251 | 0.9265 | 0.9279 | 0.9292 | 0.9306 | 0.9319 |
| 1.5  | 0.9332 | 0.9345 | 0.9357 | 0.9370 | 0.9382 | 0.9394 | 0.9406 | 0.9418 | 0.9429 | 0.9441 |
| 1.6  | 0.9452 | 0.9463 | 0.9474 | 0.9484 | 0.9495 | 0.9505 | 0.9515 | 0.9525 | 0.9535 | 0.9545 |
| 1.7  | 0.9554 | 0.9564 | 0.9573 | 0.9582 | 0.9591 | 0.9599 | 0.9608 | 0.9616 | 0.9625 | 0.9633 |
| 1.8  | 0.9641 | 0.9649 | 0.9656 | 0.9664 | 0.9671 | 0.9678 | 0.9686 | 0.9693 | 0.9699 | 0.9706 |
| 1.9  | 0.9713 | 0.9719 | 0.9726 | 0.9732 | 0.9738 | 0.9744 | 0.9750 | 0.9756 | 0.9761 | 0.9767 |
| 2.0  | 0.9773 | 0.9778 | 0.9783 | 0.9788 | 0.9793 | 0.9798 | 0.9803 | 0.9808 | 0.9812 | 0.9817 |
| 2.1  | 0.9821 | 0.9826 | 0.9830 | 0.9834 | 0.9838 | 0.9842 | 0.9846 | 0.9850 | 0.9854 | 0.9857 |
| 2.2  | 0.9861 | 0.9864 | 0.9868 | 0.9871 | 0.9875 | 0.9878 | 0.9881 | 0.9884 | 0.9887 | 0.9890 |
| 2.3  | 0.9893 | 0.9896 | 0.9898 | 0.9901 | 0.9904 | 0.9906 | 0.9909 | 0.9911 | 0.9913 | 0.9916 |
| 2.4  | 0.9918 | 0.9920 | 0.9922 | 0.9925 | 0.9927 | 0.9929 | 0.9931 | 0.9932 | 0.9934 | 0.9936 |
| 2.5  | 0.9938 | 0.9940 | 0.9941 | 0.9943 | 0.9945 | 0.9946 | 0.9948 | 0.9949 | 0.9951 | 0.9952 |
| 2.6  | 0.9953 | 0.9955 | 0.9956 | 0.9957 | 0.9959 | 0.9960 | 0.9961 | 0.9962 | 0.9963 | 0.9964 |
| 2.7  | 0.9965 | 0.9966 | 0.9967 | 0.9968 | 0.9969 | 0.9970 | 0.9971 | 0.9972 | 0.9973 | 0.9974 |
| 2.8  | 0.9974 | 0.9975 | 0.9976 | 0.9977 | 0.9977 | 0.9978 | 0.9979 | 0.9979 | 0.9980 | 0.9981 |
| 2.9  | 0.9981 | 0.9982 | 0.9982 | 0.9983 | 0.9984 | 0.9984 | 0.9985 | 0.9985 | 0.9986 | 0.9986 |
| z    | 3.00   | 3.10   | 3.20   | 3.30   | 3.40   | 3.50   | 3.60   | 3.70   | 3.80   | 3.90   |
| P    | 0.9986 | 0.9990 | 0.9993 | 0.9995 | 0.9997 | 0.9998 | 0.9998 | 0.9999 | 0.9999 | 1.0000 |

page:22

---

## AREAS UNDER NORMAL CURVE

Normal probability curve is given by

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp \left\{ -\frac{1}{2} \left( \frac{x - \mu}{\sigma} \right)^2 \right\}, -\infty < x < \infty$$

and standard normal probability curve is given by

$$\phi(z) = \frac{1}{\sqrt{2\pi}} \exp \left( -\frac{1}{2}z^2 \right), -\infty < z < \infty$$

where $Z = \frac{X - E(X)}{\sigma_X} \sim N(0, 1)$

Figure: Normal probability curve titled "Areas under Normal Curve". The x-axis shows $X = \mu$ ($Z = 0$) at the center and $X = x$ ($Z = z$) to the right. The region under the bell-shaped curve between $Z = 0$ and $Z = z$ is shaded.

The following table gives the shaded area in the diagram viz., $P(0 < Z < z)$ for different values of $z$.

---

## TABLE OF AREAS

MANIPAL UNIVERSITY JAIPUR
NAAC A+ GRADE WITH 3.28 SCORE

| ↓Z→ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| .0 | .0000 | .0040 | .0080 | .0120 | .0160 | .0199 | .0239 | .0279 | .0319 | .0359 |
| .1 | .0398 | .0438 | .0478 | .0517 | .0557 | .0596 | .0636 | .0675 | .0714 | .0759 |
| .2 | .0793 | .0832 | .0871 | .0910 | .0948 | .0987 | .1026 | .1064 | .1103 | .1141 |
| .3 | .1179 | .1217 | .1255 | .1293 | .1331 | .1368 | .1406 | .1443 | .1480 | .1517 |
| .4 | .1554 | .1591 | .1628 | .1664 | .1700 | .1736 | .1772 | .1808 | .1844 | .1879 |
| .5 | .1915 | .1950 | .1985 | .2019 | .2054 | .2088 | .2123 | .2157 | .2190 | .2224 |
| .6 | .2257 | .2291 | .2324 | .2357 | .2389 | .2422 | .2454 | .2486 | .2517 | .2549 |
| .7 | .2580 | .2611 | .2642 | .2673 | .2703 | .2734 | .2764 | .2794 | .2823 | .2852 |
| .8 | .2881 | .2910 | .2939 | .2967 | .2995 | .3023 | .3051 | .3078 | .3106 | .3133 |
| .9 | .3159 | .3186 | .3212 | .3238 | .3264 | .3289 | .3315 | .3340 | .3365 | .3389 |
| 1.0 | .3413 | .3438 | .3461 | .3485 | .3508 | .3531 | .3554 | .3577 | .3599 | .3621 |
| 1.1 | .3643 | .3665 | .3686 | .3708 | .3729 | .3749 | .3770 | .3790 | .3810 | .3830 |
| 1.2 | .3849 | .3869 | .3888 | .3907 | .3925 | .3944 | .3962 | .3980 | .3997 | .4015 |
| 1.3 | .4032 | .4049 | .4066 | .4082 | .4099 | .4115 | .4131 | .4147 | .4162 | .4177 |
| 1.4 | .4192 | .4207 | .4222 | .4236 | .4251 | .4265 | .4279 | .4292 | .4306 | .4319 |
| 1.5 | .4332 | .4345 | .4357 | .4370 | .4382 | .4394 | .4406 | .4418 | .4429 | .4441 |

---

## TABLE OF AREAS

| ↓Z→ | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    |
|-----|------|------|------|------|------|------|------|------|------|------|
| 1.6 | .4452 | .4463 | .4474 | .4484 | .4495 | .4505 | .4515 | .4525 | .4535 | .4545 |
| 1.7 | .4554 | .4564 | .4573 | .4582 | .4591 | .4599 | .4608 | .4616 | .4625 | .4633 |
| 1.8 | .4641 | .4649 | .4656 | .4664 | .4671 | .4678 | .4686 | .4693 | .4699 | .4706 |
| 1.9 | .4713 | .4719 | .4726 | .4732 | .4738 | .4744 | .4750 | .4756 | .4761 | .4767 |
| 2.0 | .4772 | .4778 | .4783 | .4788 | .4793 | .4798 | .4803 | .4808 | .4812 | .4817 |
| 2.1 | .4821 | .4826 | .4830 | .4834 | .4838 | .4842 | .4846 | .4850 | .4854 | .4857 |
| 2.2 | .4861 | .4864 | .4868 | .4871 | .4875 | .4878 | .4881 | .4884 | .4887 | .4890 |
| 2.3 | .4893 | .4896 | .4898 | .4901 | .4904 | .4906 | .4909 | .4911 | .4913 | .4916 |
| 2.4 | .4918 | .4920 | .4922 | .4925 | .4927 | .4929 | .4931 | .4932 | .4934 | .4936 |
| 2.5 | .4938 | .4940 | .4941 | .4943 | .4945 | .4946 | .4948 | .4949 | .4951 | .4952 |
| 2.6 | .4953 | .4955 | .4956 | .4957 | .4959 | .4960 | .4961 | .4962 | .4963 | .4964 |
| 2.7 | .4965 | .4966 | .4967 | .4968 | .4969 | .4970 | .4971 | .4972 | .4973 | .4974 |
| 2.8 | .4974 | .4975 | .4976 | .4977 | .4977 | .4978 | .4979 | .4979 | .4980 | .4981 |
| 2.9 | .4981 | .4982 | .4982 | .4983 | .4984 | .4984 | .4985 | .4985 | .4986 | .4986 |
| 3.0 | .4987 | .4987 | .4987 | .4988 | .4988 | .4989 | .4989 | .4989 | .4990 | .4990 |
| 3.1 | .4990 | .4991 | .4991 | .4991 | .4992 | .4992 | .4992 | .4992 | .4993 | .4993 |
| 3.2 | .4993 | .4993 | .4994 | .4994 | .4994 | .4994 | .4994 | .4995 | .4995 | .4995 |
| 3.3 | .4995 | .4995 | .4995 | .4996 | .4996 | .4996 | .4996 | .4996 | .4996 | .4997 |
| 3.4 | .4997 | .4997 | .4997 | .4997 | .4997 | .4997 | .4997 | .4997 | .4997 | .4998 |
| 3.5 | .4998 | .4998 | .4998 | .4998 | .4998 | .4998 | .4998 | .4998 | .4998 | .4998 |
| 3.6 | .4998 | .4998 | .4999 | .4999 | .4999 | .4999 | .4999 | .4999 | .4999 | .4999 |
| 3.7 | .4999 | .4999 | .4999 | .4999 | .4999 | .4999 | .4999 | .4999 | .4999 | .4999 |
| 3.9 | .5000 | .5000 | .5000 | .5000 | .5000 | .5000 | .5000 | .5000 | .5000 | .5000 |

---

## (untitled)
* Appendix Table 1 gives the probability $F(a)$ for any value $a$

Example:
$P(Z < 2.00) = .9772$

Figure: A standard normal distribution curve. The horizontal axis is labeled $Z$ with tick marks at $0$ and $2.00$. The area under the curve to the left of $Z = 2.00$ is shaded red. A callout box containing the value .9772 points to the shaded area.

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## (untitled)

*   For *negative Z-values*, use the fact that the distribution is symmetric to find the needed probability:

Example:
$P(Z < -2.00) = 1 - 0.9772$
$= 0.0228$

Figure: Two normal distribution curves. The top curve shows a red shaded area to the left of $Z=2.00$ with a label of .9772 and a yellow shaded area to the right of $Z=2.00$ with a label of .0228. The bottom curve shows a yellow shaded area to the right of $Z=-2.00$ with a label of .9772 and a red shaded area to the left of $Z=-2.00$ with a label of .0228. Both horizontal axes are labeled $Z$ and include ticks at 0, 2.00, and -2.00.

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## General Procedure for Finding Probabilities

To find $P(a < X < b)$ when $X$ is distributed normally:

* Draw the normal curve for the problem in terms of $X$
* Translate X-values to Z-values
* Use the Cumulative Normal Table

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

page:Chap 6-28

---

## Finding Normal Probabilities
* Suppose $X$ is normal with mean $8.0$ and standard deviation $5.0$
* Find $P(X < 8.6)$

Figure: A normal distribution curve with a green outline and a horizontal axis labeled 'X'. The mean is marked at $8.0$. The area under the curve to the left of $8.6$ is shaded, with the portion to the left of $8.0$ in red and the portion between $8.0$ and $8.6$ in teal. The value $8.6$ is marked on the axis to the right of the mean.

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## Finding Normal Probabilities (continued)

$$Z = \frac{X - \mu}{\sigma} = \frac{8.6 - 8.0}{5.0} = 0.12$$

Figure: Two normal distribution curves illustrating the conversion of a normal random variable $X$ to a standard normal variable $Z$. The left curve shows a normal distribution with mean $\mu = 8$ and standard deviation $\sigma = 10$ on an $X$-axis. The $X$-axis has ticks at $8$ and $8.6$. The area to the left of $X = 8.6$ is shaded red, labeled $P(X < 8.6)$. An arrow points from the first curve to the second curve on the right. The second curve shows the standard normal distribution with mean $\mu = 0$ and standard deviation $\sigma = 1$ on a $Z$-axis. The $Z$-axis has ticks at $0$ and $0.12$. The area to the left of $Z = 0.12$ is shaded red, labeled $P(Z < 0.12)$.

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

page:6-30

---

## Solution: Finding P(Z < 0.12)

Standardized Normal Probability Table (Portion)

| z    | F(z) |
|------|------|
| .10  | .5398|
| .11  | .5438|
| .12  | .5478|
| .13  | .5517|

P(X < 8.6) = P(Z < 0.12)
F(0.12) = 0.5478

Figure: A standard normal curve with the horizontal axis labeled "z". The area under the curve to the left of z=0.12 is shaded red. Two vertical lines indicate z=0.00 and z=0.12, with arrows pointing to these points on the axis.

page:6-31

---

## Upper Tail Probabilities

* Suppose $X$ is normal with mean 8.0 and standard deviation 5.0.
* Now Find $P(X > 8.6)$

Figure: A normal distribution curve with a green outline plotted against a horizontal axis labeled $X$. A vertical dotted line marks the center at 8.0. A vertical solid line marks the value 8.6 in green text on the $X$ axis. The area under the curve to the right of 8.6 is shaded red.

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## (continued)

• Now Find $P(X > 8.6)$...

$$P(X > 8.6) = P(Z > 0.12) = 1.0 - P(Z \leq 0.12)$$
$$= 1.0 - 0.5478 = 0.4522$$

Figure: Two normal distribution curves. Left curve: vertical line at Z=0.12, area to the left shaded red, label box "1.000" points to shaded area. Right curve: vertical dashed line at Z=0.12, area to the left shaded light blue labeled "0.5478", area to the right shaded red labeled "1.0 - 0.5478 = 0.4522". Both horizontal axes labeled Z with ticks at 0 and 0.12.

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.
Chap 6-33

page:33

---

## Finding the X value for a Known Probability

• Steps to find the X value for a known probability:
1. Find the Z value for the known probability
2. Convert to X units using the formula:

$$X = \mu + Z\sigma$$

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## Finding the X value for a Known Probability (continued)

Example:
* Suppose X is normal with mean 8.0 and standard deviation 5.0.
* Now find the X value so that only 20% of all values are below this X

Figure: A normal distribution curve with a green outline. A vertical line marks the mean at the center, and another vertical line is positioned to the left. The area under the curve to the left of this second line is shaded light blue, with a callout label ".2000". Below the horizontal axis, two rows are labeled X and Z. Under the center vertical line, the X value is 8.0 and the Z value is 0. Under the left vertical line, the X value is marked with a question mark (?) and the Z value is marked with a question mark (?) inside a circle.

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

page:35

---

## Find the Z value for 20% in the Lower Tail

1. Find the Z value for the known probability

Standardized Normal Probability Table (Portion)

| z | F(z) |
|---|---|
| .82 | .7939 |
| .83 | .7967 |
| .84 | .7995 |
| .85 | .8023 |

* 20% area in the lower tail is consistent with a Z value of -0.84

Figure: A bell-shaped normal distribution curve. The area under the curve to the left of a vertical boundary line is shaded and labeled ".20". The area to the right of the boundary is labeled ".80". A vertical line indicates the boundary. On the horizontal axis, the labels "X" and "Z" are stacked vertically on the right side. At the boundary on the Z-axis, a circle contains a question mark and the value "-0.84". On the X-axis at the same boundary, the numbers "8.0" and "0" are stacked vertically.

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## Finding the X value

2. Convert to X units using the formula:

$$
\begin{aligned}
X &= \mu + Z\sigma \\
&= 8.0 + (-0.84)5.0 \\
&= 3.80
\end{aligned}
$$

So 20% of the values from a distribution with mean 8.0 and standard deviation 5.0 are less than 3.80

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## The Exponential Distribution

Figure: A flow chart showing the hierarchy of probability distributions. A box at the top labeled "Probability Distributions" is connected by a line to a box below labeled "Continuous Probability Distributions". From this box, three lines branch out to the right to boxes labeled "Normal", "Uniform", and "Exponential". The "Exponential" box is shaded light blue.

Statistics for Business and Economics, 6e © 2007 Pearson Education,
Inc.

---

## The Exponential Distribution
* Used to model the length of time between two occurrences of an event (the time between arrivals)
* Examples:
* Time between trucks arriving at an unloading dock
* Time between transactions at an ATM Machine
* Time between phone calls to the main operator

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## The Exponential Distribution (continued)
* The exponential random variable T (t>0) has a probability density function
$$f(t) = \lambda e^{-\lambda t} \text{ for } t > 0$$
* Where
* 1/$\lambda$ is the mean number of occurrences per unit time
* t is the number of time units until the next occurrence
* e = 2.71828

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## The Exponential Distribution
* T is said to follow an exponential probability distribution defined by a single parameter, its mean $1/\lambda$ (lambda)
$$\mu = \frac{1}{\lambda} \quad \sigma^2 = \frac{1}{\lambda^2}$$
* The cumulative distribution function (the probability that an arrival time is less than some specified time $t$) is
$$F(t) = 1 - e^{-\lambda t}$$
where
$e =$ mathematical constant approximated by $2.71828$
$1/\lambda =$ the population mean number of arrivals per unit
$t =$ any value of the continuous variable where $t > 0$

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## Exponential Distribution Example

Example: Customers arrive at the service counter at the rate of 15 per hour. What is the probability that the arrival time between consecutive customers is less than three minutes?

Statistics for Business and Economics, 6e ©
2007 Pearson Education, Inc.

---

## Exponential Distribution Example

**Example:** Customers arrive at the service counter at the rate of 15 per hour. What is the probability that the arrival time between consecutive customers is less than three minutes?

*   The mean number of arrivals per hour is 15, so $\lambda = 15$
*   Three minutes is .05 hours
*   $P(\text{arrival time} < .05) = 1 - e^{-\lambda X} = 1 - e^{-(15)(.05)} = 0.5276$
*   So there is a 52.76% probability that the arrival time between successive customers is less than three minutes

Statistics for Business and Economics, 6e © 2007 Pearson Education, Inc.

---

## References

S.C. Gupta and V.K. Kapoor, *Fundamentals of Mathematical Statistics*, Sultan Chand & Sons.

S. Palaniammal, *Probability and Random Variables*, PHI Learning.

K. Sundarapandian, *Probability, Statistics and Queuing Theory*, PHI Learning.

J. T. Mc Clave, Statistics for Business and Economics, Pearson Education, Inc.
