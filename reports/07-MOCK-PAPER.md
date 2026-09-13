# Mock MTE paper, MAS2001 Statistics and Probability

30 marks, closed book, 90 minutes. Same weighting as the real mid term (30 marks out of 100,
from the official course handout). Scope is lectures 1 to 21 only, the same scope the real
paper uses.

Sit it before reading `reports/08-MOCK-SOLUTIONS.md`. Answers to every numeric value in the
solutions file were computed and checked, not taken from memory.

---

## Section A, multiple choice, 10 marks

One mark each. One correct option per question.

**A1.** Which of the following is a continuous random variable?

1. the number of defective bulbs in a box of 20
2. the time taken to complete an examination
3. the number of sixes in 10 throws of a die
4. the number of calls arriving at an exchange in a minute

**A2.** For a random variable X, the cumulative distribution function is defined as:

1. P(X = x)
2. P(X <= x)
3. P(X >= x)
4. P(X > x)

**A3.** If P(A | B) = 1, then:

1. A is impossible whenever B occurs
2. A occurs whenever B occurs
3. A and B are mutually exclusive
4. A and B are independent

**A4.** For any two events A and B, P(A U B) equals:

1. P(A) + P(B)
2. P(A) + P(B) - P(A n B)
3. P(A) P(B)
4. P(A n B) / P(B)

**A5.** Chebyshev's inequality is applicable to:

1. only normal distributions
2. any distribution with finite mean and finite variance
3. only discrete distributions
4. only continuous distributions

**A6.** Two fair dice are thrown. The probability that the sum of the numbers shown is 7 is:

1. 1/12
2. 1/9
3. 1/6
4. 5/36

**A7.** If X ~ B(10, 0.4), then E(X) and Var(X) are:

1. E = 4, Var = 2.4
2. E = 2.4, Var = 4
3. E = 4, Var = 4
4. E = 0.4, Var = 2.4

**A8.** If X ~ Poisson(3), then P(X = 0) is approximately:

1. 0.0498
2. 0.1494
3. 0.2240
4. 0.3333

**A9.** If X is uniform on the interval (2, 8), then P(X < 5) is:

1. 0.25
2. 0.50
3. 0.60
4. 0.75

**A10.** A sample mean is computed from a sample of size n. If n is increased from 25 to 100,
the standard error of the mean:

1. stays the same
2. is halved
3. is quartered
4. is doubled

---

## Section B, 20 marks

Four questions, 5 marks each, all compulsory. Show working. A correct final number with no
working earns at most half the marks for that part.

**B1. Chebyshev, 5 marks.**
The marks obtained by engineering students in a test have mean 70 and variance 25.

1. Use Chebyshev's inequality to find the minimum proportion of students scoring between
   60 and 80 marks. (3 marks)
2. State the bound for the probability that a student scores below 55 or above 85 marks.
   (2 marks)

**B2. Binomial, 5 marks.**
Eight percent of the components produced by a machine are defective. A random sample of 15
components is drawn. Let X be the number of defective components.

1. State the distribution of X with its parameters. (1 mark)
2. Find P(X = 1). (2 marks)
3. Find P(X >= 1) and state which rule you used. (1 mark)
4. Find the mean and variance of X. (1 mark)

**B3. Normal, 5 marks.**
The lifetime of a component, X, is normally distributed with mean 50 and variance 100.

1. Find P(X < 65). (2 marks)
2. Find P(X > 35). (1 mark)
3. Find the value x such that P(X < x) = 0.90. (2 marks)

**B4. Estimation, 5 marks.**
Let X1, X2, X3 be a random sample of size 3 from a population with mean mu and variance
sigma^2. Consider four estimators:

```
T1 = X1
T2 = (X1 + X2) / 2
T3 = (X1 + X2 + X3) / 3
T4 = (X1 + X2 + X3) / 2
```

1. Which of the four are unbiased for mu? Show the expectation for each. (3 marks)
2. Among the unbiased ones, which is most efficient? Justify with variances. (1 mark)
3. Explain in one or two lines why T3 is consistent for mu while T1 is not. (1 mark)

---

## Marking guide for self assessment

```
  24 to 30     ready, keep the formula sheet warm and sit the paper
  18 to 23     one weak block, spend the remaining time on that block only
  below 18     the weak block is likely lectures 1 to 11 or the CLT, revise those first
```

Where each answer comes from is printed next to the solution in
`reports/08-MOCK-SOLUTIONS.md`, including which slide page in this repo covers it.
