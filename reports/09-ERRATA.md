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

## 8. ppt4 p030 figure prints sigma = 10 under mu = 8

`md/ppt4-continuous-prob-dist/p030.md`. The worked question is mu = 8.0, sigma = 5.0
(stated on p029, p032, p033, p035 and used in the Z = 0.12 arithmetic). The figure on p030
labels the left curve "mu = 8, sigma = 10" while the Z computation on the same slide divides
by 5.0.

```
  source text layer, PPT 4 page 30, verbatim:
      mu = 8
      sigma = 10        <- figure label, contradicts everything else on the page
  Z = (8.6 - 8.0) / 5.0 = 0.12    <- the real sigma is 5.0, used in the arithmetic
```

Confirmed by reading the source PDF text layer directly (not the conversion). If you
sketch this curve, use sigma = 5.0. The mark-relevant numbers are unaffected.

## 9. Assignment 2, B Q5 prints 0.5679 where the value is 0.6225

`md/mas2001-assignment-2/p003.md`, Q5: X exponential with mean 2, so lambda = 1/2.
Find P(X < 1 | X < 2).

```
  computed  P(X<1) = 1 - e^-0.5 = 0.393469
            P(X<2) = 1 - e^-1   = 0.632121
            ratio  = 0.393469 / 0.632121 = 0.622459  -> 0.6225
  printed   0.5679
```

0.5679 is not reproduced by any natural misreading checked: 0.9 x P(X<2) = 0.5689 and
ln 2 x 0.82 = 0.5684 come within 0.001 but neither equals it, and the complement
P(X>1|X<2) = 0.3775 is far off. Write 0.6225.

## 10. Assignment 2, C Q2: the printed mean 37.5 does not reproduce from the given tables

`md/mas2001-assignment-2/p003.md`, Q2: 46 percent pass, 9 percent distinction, pass mark 40,
distinction mark 75, normal marks. Given phi(0.1) = 0.04, phi(1.34) = 0.41, phi(0.24) = 0.095.

```
  from the given tables (solve the two equations):
      sigma = 35 / (1.34 - 0.10) = 28.23   ->  28.2   (key agrees)
      mu    = 40 - 0.10 x 28.23 = 37.18    ->  37.2   (key prints 37.5)
  the key's own third value, the re-exam cutoff, uses which pair?
      with 37.2 and 28.2:  37.2 - 0.24 x 28.2 = 30.432  ->  30.43 = the key's own number
      with 37.5 and 28.2:  37.5 - 0.24 x 28.2 = 30.732  ->  30.73, not printed
```

So the key's cutoff (30.43) is only consistent with mu = 37.2, and the given tables also
give 37.2. The "37.5" appears to be a typo. Reproduce with mu = 37.2, sigma = 28.2,
cutoff = 30.4.

## 11. Assignment 1, long Q3 prints 0.808 where both cases are exactly 0.8

`md/mas2001-assignment-1/p004.md` and `p005.md`: lot of 25 items, 5 defective, sample of 4.
Expected number of defectives (i) without replacement, (ii) with replacement.

```
  (ii) with replacement: binomial mean = n p = 4 x 0.2 = 0.80  (key prints 0.8, correct)
  (i)  without replacement: hypergeometric mean = n x K/N = 4 x 5/25 = 0.80 exactly
       the pmf recomputed: 0.38300, 0.45059, 0.15020, 0.01581, 0.00040
       weighted sum = 0.80000 (exact to five decimals)
  printed 0.808
```

0.808 is not produced by either case, by the naive n p answer, or by any 4-digit rounding of
the pmf sum. Both answers are 0.8; the structural fact to remember is that the hypergeometric
mean equals the binomial mean here.

## 12. Assignment 1, application Q3: exact SD is 0.97, the key's chain rounds twice

`md/mas2001-assignment-1/p006.md`: battery life distribution, mean 3.45, then variance.

```
  Var = E(X^2) - mean^2 = 12.85 - 3.45^2 = 0.9475
  exact SD = sqrt(0.9475) = 0.97340  ->  0.97
  the key's numbers: variance prints 0.95 (rounded to 2dp),
      SD prints 0.975 (= sqrt(0.95) of the ROUNDED variance), then "~ 0.98"
  sqrt(0.95) = 0.97468 does not equal the exact 0.97340
```

If asked for SD, write 0.97 from the exact variance, or state which rounding you used.
Same family as errata 3: keep exact values until the final line.

## 13. Deck bus example: statement digits unreadable, working has a double equals and a
   lower limit that disagrees with its own answer

`md/notes-lecture-series-01-09/p127.md` and `p129.md`, the bus waiting time example
(6 parts). The pages are images with no usable text layer; the part (f) digits on p127 sit
under the footer watermark and read as "6" in some renders and "8" in others. What is
certain, from the working on p129 and from computation:

```
  statement (f): "...total waiting time is either less than 2 min or more than 6 or 8 min?"
  working (f):   P(Y < 2 or Y > 6) = integral_0^3 y/25 dy + integral_6^10 (...) = 2/5 = .4
  the working's first integral bound (3) contradicts its own stated event (Y < 2):
      int_0^2  y/25 dy = 0.08   (matches "Y < 2")
      int_0^3  y/25 dy = 0.18   (what the printed bound says, and the wrong event)
      int_6^10 (2/5 - y/25) dy = 0.32
      0.08 + 0.32 = 0.40 = 2/5   <- the printed final answer
      0.18 + 0.32 = 0.50         <- what the printed lower bound would actually give
```

So the final answer 2/5 is correct for the event "less than 2 or more than 6", and the
printed lower limit 3 in the first integral is the slip. There is also a doubled equals sign
("= =") on the same line. If you reproduce it: P(Y<2 or Y>6) = 0.08 + 0.32 = 0.40.

## 14. Minor: assignment 2, C Q3 last-digit rounding

Exact e^-5 (1 + 5 + 12.5) computed: P(X > 2) = 1 - P(0) - P(1) - P(2) = 0.875348, so 0.8753.
The key prints 0.8754 (the sum of three separately rounded terms). Both grade, 0.8753 is the
exact value.

## 15. Not an error, but easy to misread

`md/notes-lecture-series-01-09/p011.md` and the equivalent page in ppt4 write the normal
notation as X ~ N(mu, sigma^2), while the surrounding prose says "mean and variance". The
second parameter is the variance, not the standard deviation. The assignment paper uses
variance as well (mean 70, variance 25, so sigma = 5).
