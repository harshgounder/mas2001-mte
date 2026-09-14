# Errata found in the source material

Errors located in the supplied slides and answer keys, each with the computed value that
disagrees with it. Recorded so the wrong number does not get memorised.

## 1. Insurance example prints 0.1745 where the value is 0.1755

`md/ppt3-discrete-prob-dist/p027.md`, Poisson with lambda = 5, probability of exactly 4 claims.

```
  printed  P(X = 4) = 0.1745
  computed e^-5 x 5^4 / 4! = 0.0067379 x 26.0417 = 0.175467  ->  rounds to 0.1755
```

Difference is 0.001, so both values would earn the method marks, but 0.1755 is the correct
number to write.

## 2. Irregular die example prints 0.549 where the value is 0.5499

`md/ppt3-discrete-prob-dist/p018.md`, expected number of sets with no even number in 10,000.

```
  printed  0.549
  computed (3/8)^10 x 10000 = 0.00005499 x 10000 = 0.5499  ->  rounds to 0.550
```

## 3. Assignment 1 answer key truncates instead of rounding

`md/mas2001-assignment-1`, short Q2, P(X > 12).

```
  printed  0.0915
  computed 5e^-4 = 0.091578, which rounds to 0.0916
```

The key truncates at the fourth decimal. Use 0.0916 if the answer is asked to four decimals.

## 4. Exponential slide inverts the meaning of lambda

`md/ppt4-continuous-prob-dist/p040.md` states that "1/lambda is the mean number of
occurrences per unit time". That is backwards.

```
  correct   lambda is the mean number of arrivals per unit time
            1/lambda is the mean TIME between arrivals
  the same deck page p041 states it correctly, mu = 1/lambda
```

Read p041 and ignore the p040 wording. The example on p043 uses it correctly.

## 5. Assignment 1, long Q2, the normalisation equation

The question paper itself is self consistent once you notice that P(X = 0) is zero, which
makes the normalisation 9k + 10k^2 = 1 with exact root k = 1/10. Both a 12k and a 14k version
of that equation appear in circulated working and neither is satisfied by k = 1/10.

```
  10(0.1)^2 + 9(0.1)  = 1.00   correct
  10(0.1)^2 + 12(0.1) = 1.30
  10(0.1)^2 + 14(0.1) = 1.50
```

## 6. Impurity example, the Z value printed as -0.4

`md/lms-standard-error-clt/p014.md`. Mean 4.0 g, standard deviation 1.5 g, n = 50, finding
P(3.5 < X bar < 3.8).

```
  SE = 1.5/sqrt(50) = 0.212132
  Z1 = (3.5 - 4)/0.212132 = -2.357  ->  slide prints -2.36, correct
  Z2 = (3.8 - 4)/0.212132 = -0.943  ->  slide prints -0.4, WRONG
```

The final answer on the slide, 0.1644, is nevertheless correct, because the two table areas it
subtracts are 0.4909 for z = 2.36 and 0.3264 for z = 0.94. The area 0.3264 belongs to z = 0.94,
not to z = 0.4 (that area is 0.1554). So the printed Z line is a typo and the working behind it
used the right value.

```
  correct answer, table method   0.4909 - 0.3264 = 0.1645
  exact, no table rounding       0.16368
  what -0.4 would actually give  0.33544, roughly double
```

If you reproduce this question, write Z2 = -0.94. Both the slide's 0.1644 and the exact 0.1637
are acceptable final values, but only with the correct Z.

## 7. Not an error, but easy to misread

`md/notes-lecture-series-01-09/p011.md` and the equivalent page in ppt4 write the normal
notation as X ~ N(mu, sigma^2), while the surrounding prose says "mean and variance". The
second parameter is the variance, not the standard deviation. The assignment paper uses
variance as well (mean 70, variance 25, so sigma = 5).
