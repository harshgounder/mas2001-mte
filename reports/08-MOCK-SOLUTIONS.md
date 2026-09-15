# Mock MTE paper, worked solutions

Every number on this page was computed and checked on the machine, then cross checked
against the slide page in this repo that teaches it. Source refs are the pipeline page
numbers.

---

## Section A, one mark each

**A1.** Option 2, the time taken to complete an examination. Time is measured, so it takes
values on a continuum, while the other three are counts.
Source: `md/notes-lecture-series-01-09/p063.md` and `p112.md`.

**A2.** Option 2, P(X <= x). Source: `md/notes-lecture-series-01-09/p074.md`.

**A3.** Option 2, A occurs whenever B occurs. P(A|B) = 1 means every outcome in B is also in A,
so B is a subset of A. Source: `md/notes-lecture-series-01-09/p050.md`.

**A4.** Option 2. The addition rule subtracts the overlap, which was counted twice.
Source: `md/notes-lecture-series-01-09/p031.md` to `p040.md`.

**A5.** Option 2, any distribution with finite mean and finite variance. That is exactly what
makes it useful and exactly why there were no slides for it in the old batch (the 15 Sep
batch added S&P L10-11 with full proofs), because it is
distribution-free. Source: `reports/03-FORMULA-SHEET.md` section E.

**A6.** Option 3, 1/6. Six ordered pairs give a sum of 7 out of 36, so 6/36 = 1/6.
Source: `md/mas2001-assignment-1/p001.md` question 5 uses the same 36 outcome space.

**A7.** Option 1, E = 4 and Var = 2.4. E = np = 10(0.4) = 4, Var = npq = 10(0.4)(0.6) = 2.4.
Source: `md/ppt3-discrete-prob-dist/p012.md`.

**A8.** Option 1, 0.0498. P(X=0) = e^-3 = 0.049787.
Source: `md/ppt3-discrete-prob-dist/p023.md` for the pmf, computed here.

**A9.** Option 2, 0.50. Constant density means probability equals length ratio,
(5 - 2)/(8 - 2) = 3/6 = 0.5. Source: `md/ppt4-continuous-prob-dist/p003.md`.

**A10.** Option 2, halved. The standard error is sigma / sqrt(n), and sqrt(100)/sqrt(25) = 2.
Verified numerically: with sigma = 10, SE(25) = 2.0000 and SE(100) = 1.0000.
Source: `md/lms-standard-error-clt/p004.md`.

---

## Section B

### B1. Chebyshev, 5 marks

Target interval 60 to 80 with mean 70 and standard deviation 5.

1. Distance from mean is 10, so k = 10/5 = 2.

```
P(|X - 70| < 2 sigma) >= 1 - 1/2^2 = 1 - 1/4 = 3/4 = 0.75
```

Minimum proportion is 75 percent. (3 marks: 1 for k, 1 for the complement form, 1 for 0.75.)

2. Interval below 55 or above 85 has distance 15, so k = 15/5 = 3, and this is the tail form,
   not the complement.

```
P(|X - 70| >= 15) <= 1/3^2 = 1/9 = 0.1111
```

(2 marks: 1 for k = 3, 1 for 1/9. Writing 8/9 here is the common error, that is the
complement and answers a different question.)

### B2. Binomial, 5 marks

1. X ~ B(15, 0.08), with q = 0.92. (1 mark)

2. P(X = 1) = C(15,1)(0.08)(0.92)^14 = 15 x 0.08 x 0.311. Computed exactly: 0.373431.
   So 0.3734. (2 marks: 1 for the pmf with correct combination, 1 for the value.)

3. P(X >= 1) = 1 - P(X = 0) = 1 - (0.92)^15 = 1 - 0.286297 = 0.713703, so 0.7137.
   The rule is the complement rule. (1 mark)

4. E(X) = np = 1.2. Var(X) = npq = 15(0.08)(0.92) = 1.104. (1 mark)

Cross check run during preparation: the pmf over x = 0 to 15 sums to 1.000000000000 exactly.

### B3. Normal, 5 marks

Mean 50, variance 100, so sigma = 10.

1. Z = (65 - 50)/10 = 1.5. P(X < 65) = Phi(1.5) = 0.9332. (2 marks)

2. Z = (35 - 50)/10 = -1.5. P(X > 35) = 1 - Phi(-1.5) = Phi(1.5) = 0.9332. The equality is
   symmetry about the mean, and it is worth a line in the answer. (1 mark)

3. P(X < x) = 0.90 needs the table inverse, z = 1.2816, then X = mu + z sigma.
   X = 50 + 1.2816(10) = 62.8155, so x is approximately 62.82. (2 marks: 1 for z, 1 for
   converting back to X units, which is the step that is usually forgotten.)

### B4. Estimation, 5 marks

1. Expectations, using E(Xi) = mu:

```
E(T1) = mu                                   unbiased
E(T2) = (mu + mu)/2 = mu                     unbiased
E(T3) = (mu + mu + mu)/3 = mu                unbiased
E(T4) = (mu + mu + mu)/2 = 3mu/2             BIASED, and the bias is 3mu/2 - mu = mu/2
```

(3 marks, one per correct identification, and the T4 line must name the bias.)

2. Variances, using independence and Var(Xi) = sigma^2:

```
Var(T1) = sigma^2                = 1.0000 sigma^2
Var(T2) = sigma^2/2              = 0.5000 sigma^2
Var(T3) = sigma^2/3              = 0.3333 sigma^2
```

All three unbiased estimators have the same expectation, so the efficient one is the one with
the smallest variance, which is T3. (1 mark)

Note the trap in T4: it is biased, so it does not win the efficiency comparison, and its
variance (3/4 sigma^2) is in fact larger than T2's and T3's, not smaller. Efficiency is only
defined among unbiased estimators, so T4 is excluded on bias before variance is even compared.

3. T3 is the sample mean, whose variance is sigma^2/n, which goes to 0 as n grows, while its
   expectation stays at mu. Both sufficient conditions for consistency hold. T1 is a single
   observation, so its variance stays at sigma^2 for every n and it never concentrates on mu.
   (1 mark)

Source for the layout: `md/ppt5-estimation-summary/p015.md` to `p021.md`, and
`md/lms-theory-of-estimation/p017.md` to `p022.md` for the same question worked with
different constants.

---

## Self check on the mock

```
  Section A    10 marks   one mark each
  B1            3 + 2
  B2            1 + 2 + 1 + 1
  B3            2 + 1 + 2
  B4            3 + 1 + 1
  total        30 marks
```

If B1 part 2 came out as 8/9, if B3 part 3 stopped at z without converting back to X, or if
B4 selected T4, those are the three errors this paper is designed to expose. Fix those three
and the paper pattern is covered.
