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
of that equation appear in circulated working and neither is satisfied by k = 1/10. The 12k
form is no longer a mystery: it is what the second edition of this paper prints (see 5.1).

```
  10(0.1)^2 + 9(0.1)  = 1.00   correct
  10(0.1)^2 + 12(0.1) = 1.30
  10(0.1)^2 + 14(0.1) = 1.50
```

### 5.1 Addendum, VERIFIED 15 Sep: the second edition of this paper is broken

`~/PS/MAS2001-Assignment 1 .pdf` (in `sources.yaml` as `asgn-faculty-variant`, queued for
U05) is a second edition of this same paper, not a re-typed copy. Read three ways on the
machine, all agreeing: `pdftotext -layout`, `pdftotext -bbox` coordinates, and a vision pass
over the rendered page.

```
  x:     0   1    2    3    4    5     6      7
  p(x):  k   2k   2k   3k   3k   k^2   2k^2   7k^2 + k      <- P(X=0) is k, not 0
  sum    12k + 10k^2 = 1   ->   k = 0.078233   (10k^2 + 12k - 1 = 0)

  its own key column prints  k = 1/10
  check:  12(0.1) + 10(0.1)^2 = 1.30, not 1.00   -> the printed key does NOT satisfy its
                                                   own table
  its own key column prints  P(X > 6) = 81/100 and P(X >= 6) = 91/100
  from the row, 11k + k^2 = 0.8667 and 9k^2 + k = 0.1333   -> neither matches
```

Contrast, and this is the point: the batch-1 edition (`md/mas2001-assignment-1/p004.md`,
Dr. Vivek Singh) carries the row 0, k, 2k, 2k, 3k, k^2, 2k^2, 7k^2 + k, sums to
10k^2 + 9k = 1, has the exact root k = 1/10, and its key (81/100, 19/100, c = 4) checks out.
That edition is internally consistent; the second edition is not. If the variant ever grades
anything, the row and the key cannot both be right, and k = 0.0782 is what the row says.

Action at U05: transcribe the whole variant, compare it question by question against the
batch-1 edition, and record this disagreement rather than silently merging the two.

### 5.2 The Chebyshev deck, CORRECTED 15 Sep: it DOES have a usable text layer

An earlier revision of this entry said `pdftotext` returns 0 characters for all 9 pages
("pypdf-produced, pure vector"). That is FALSE and is retracted here. Measured on 15 Sep
by `reports/evidence/verify-audit-round7-20260915.py`:

```
  pdftotext -layout, all 9 pages   3453 non-space characters (4089 raw characters)
  page 8 alone                    extracts in full, the -1,-1,3,5 statement, the
                                  worked row, E(X^2) = 43/3, sigma^2 = 16/3, the
                                  mis-specified template, k = 1, the bound 16/3
  pdffonts                        Times New Roman, Aptos, Cambria Math, all embedded
                                  real fonts, so NOT a pypdf-produced vector file
  watermark                       MSV1RXZXSVM3TK2VFV6K, this year's MSV reseller tag,
                                  not mujstella. Only the title page is watermark-only.
```

What is true: the text layer is sparse in layout terms and the watermark string sits on
almost every page, so a plain grep is noisy. That is a readability nuisance, not an absent
layer. The vision pass over this deck was therefore never required to reach the numbers,
though it was run anyway (300 dpi, committed at errata 15) and it agrees with the text
layer. Lesson recorded: a "no text layer" claim is a measurement, run `pdftotext | wc -c`
before writing it.


## 6. Impurity example, the Z value printed as -0.4

`md/lms-standard-error-clt/p014.md`. Mean 4.0 g, standard deviation 1.5 g, n = 50, finding
P(3.5 < X bar < 3.8).

```
  SE = 1.5/sqrt(50) = 0.212132
  Z1 = (3.5 - 4)/0.212132 = -2.357  ->  slide prints -2.36, correct
  Z2 = (3.8 - 4)/0.212132 = -0.943  ->  slide prints -0.4, WRONG
```

The slide uses the right table entries but prints the wrong subtraction result. The areas are
0.4909 for z = 2.36 and 0.3264 for z = 0.94. The area 0.3264 belongs to z = 0.94, not z =
0.4, whose centre area is 0.1554.

```
  correct answer, table method   0.4909 - 0.3264 = 0.1645
  exact, no table rounding       0.16368
  what -0.4 would actually give  0.33544, roughly double
```

If you reproduce this question, write Z2 = -0.94 and state the precision used. The rounded
table method gives 0.1645; unrounded z values give about 0.1637. The slide's 0.1644 is not
the result of either stated method.

## 7. Not an error, but easy to misread

`md/notes-lecture-series-01-09/p011.md` and the equivalent page in ppt4 write the normal
notation as X ~ N(mu, sigma^2), while the surrounding prose says "mean and variance". The
second parameter is the variance, not the standard deviation. The assignment paper uses
variance as well (mean 70, variance 25, so sigma = 5).

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

## 15. Chebyshev deck (arrived 15 Sep), Q3: statement and working disagree

`~/PS/S&P L10-11 Chebyshev's inequality.pdf` p008, read from the text layer and confirmed
by vision at 300 dpi (CORRECTED 15 Sep: an earlier revision of this entry said the file has
"no text layer at all"; it does, see 5.2). Every number below was computed, not eyeballed:
the script and its raw output are `reports/evidence/verify-errata15-20260915.py` and `.txt`,
and each claim is re-checked in `reports/evidence/verify-audit-round7-20260915.py`.

What the deck actually contains, which the earlier version of this entry got wrong in one
place: the theorem slide states BOTH standard forms correctly,

```
  P(|x - mu| >= k)      <= sigma^2 / k^2          (the definition, k in the event)
  P(|x - mu| >= k*sigma) <= 1 / k^2                (the k-sigma restatement)
```

so it is not true that the deck "mis-specifies the inequality" in general. The defect is
narrower and is on the worked slide only: page 8's displayed template line prints the
reciprocal form `P(|x - mu| >= k) < k^2 / sigma^2` against the event's own k, which is the
template inversion, and the working below it then correctly uses sigma^2/k^2 = 16/3. An
earlier note calling the deck's k-sigma form "not the standard form" was itself wrong and is
retracted.

What the slide does:

```
  states  X takes  -1, -1, 3, 5   with p = 1/6, 1/6, 1/6, 1/2
  works   E(X) = -1/6 + 1/6 + 3/6 + 5/2 = 3
          E(X^2) = 43/3
          sigma^2 = 43/3 - 9 = 16/3
          bound = 16/3
```

Two real defects, both computed:

```
  (a)  the stated row and the worked row are different distributions.
       stated  (-1, -1, 3, 5)  ->  E(X) = 8/3,  Var = 65/9 = 7.2222
       worked  (-1,  1, 3, 5)  ->  E(X) = 3,    Var = 16/3 = 5.3333
       The printed E(X) = 3 and sigma^2 = 16/3 belong to the WORKED row. The plus sign in
       the E(X) line gives it away: the slide silently treats the second value as +1.
  (b)  page 8's displayed inequality template is written
       P(|x - mu| >= k) < k^2 / sigma^2.
       The event's k and the right-hand k are not the same quantity, and a strict <
       replaces <=. The theorem slide states the correct forms, so this is a
       transcription slip on the worked slide, not a wrong theorem.
  (c)  k is then obtained by "comparing Chebyshev's inequality and required probability"
       and set to 1, which is not a k-extraction.
```

What I claimed on the first pass and RETRACTED after running it (15 Sep):

```
  "sigma^2 = 16/3 is an arithmetic error, sum x^2 p(x) = 59/3 so Var = 32/3"
       FALSE. sum x^2 p(x) = 1/6 + 1/6 + 9/6 + 25/2 = 43/3 exactly, and 43/3 - 9 = 16/3.
       Both printed values are correct for the row the working uses.
  "the printed bound 16/3 is wrong"
       FALSE. The event is |X - 3| >= 1, so k*sigma = 1 and the bound is 1/k^2 = sigma^2.
       With sigma^2 = 16/3 the correct bound IS 16/3. It is correct and also useless:
       5.3333 for a probability whose exact value is 1 - P(X=3) = 5/6 = 0.8333.
```

Safe on the same deck: Q1 (E(X)=3, E(X^2)=13, lower bound 21/25) and Q2 (mu=10,
sigma^2=4: 4/9, 5/9, 21/25, C=10). Q2(iv) is the official MTE 2025-26 Q5 verbatim, 4 marks
in the scheme. Teach Q1 and Q2; treat Q3 as mis-transcribed and do not quote its row.

## 16. Tube question, printed key part (ii) reads 2/3 where the value is 8/27

Found 15 Sep by the round-7 audit, not previously recorded. The question appears twice, in
both 2024-25 Assignment 1 Q12 and the 2025-26 combined set Q14, with the same p.d.f. and the
same printed key. The question text layer is in `~/mas2001-mte-audit-v1/text/asgn-2024-25-1.txt`
line 101 and `asgn-2025-26-1-5.txt` line 152.

```
  f(x) = 100 / x^2 for x >= 100, 0 elsewhere
  P(X < 150)            = 1 - 100/150 = 1/3       (a tube dies inside 150 hours)
  P(X > 150)            = 2/3                      (a tube survives them)

  printed key:  Ans. 1/27, 2/3, 0.25, 1.7
  (i)   all three replaced   (1/3)^3 = 1/27         key 1/27   correct
  (ii)  none replaced        (2/3)^3 = 8/27 = 0.296296   key 2/3  WRONG
  (iii) P(X<200 | X>150)     = 0.25                  key 0.25   correct
  (iv)  (2/3)^n = 0.5 -> n = 1.7095 -> 1.7          key 1.7    correct
```

2/3 is the per-tube survival probability, not the probability that none of three fails. The
key's author carried the single-tube figure into the three-tube part. Answer (ii) is 8/27.

## 17. 2024-25 Assignment 1, Q16: the probability row sums to 0.9, not 1

Found 15 Sep by the round-7 audit. `~/PS/2024-2025-Assignment 1.pdf`, Q16, text layer at
`~/mas2001-mte-audit-v1/text/asgn-2024-25-1.txt` line 124.

```
  x:     1     2     3     4
  P(x):  0.1   0.2   0.5   0.1        sum = 0.9
```

Y = X^2 + 2X is then asked for its distribution, CDF, mean and variance. A pmf must sum to
1, so the row as printed cannot be used as written. The parts that follow cannot be graded
against a printed key (this file carries no answer key for Q16), so the question is only
sound if the reader renormalises, which changes every later number. A sweep of all 36 batch-2
text layers found this as the ONLY valid-pmf row in the corpus that fails to sum to 1, so it
is an isolated defect, not a layout artefact.

If asked something like this in the paper, state the renormalisation you chose (dividing the
row by 0.9 gives 1/9, 2/9, 5/9, 1/9) and carry it through, or ask for the corrected row.

## 18. Mock paper B4: the Note claims T4 has the smallest variance, it is third of four

Found 15 Sep by the round-7 audit, in our own material. `reports/08-MOCK-SOLUTIONS.md`,
section B4.

```
  Var(T1) = sigma^2     = 1.0000 sigma^2
  Var(T2) = sigma^2/2   = 0.5000 sigma^2
  Var(T3) = sigma^2/3   = 0.3333 sigma^2
  Var(T4) = 3 sigma^2/4 = 0.7500 sigma^2      (T4 = (X1+X2+X3)/2)

  order, smallest first:  T3, T2, T4, T1
```

The body line on the same page states T3 correctly. The Note below it reads "Note the trap in
T4: it has the smallest variance of all four, but it is biased", which is false twice over:
T4 is third of four, and the sentence immediately above it just listed T3 as the smallest.
The intended trap is real and worth keeping, T4 is biased and therefore excluded from the
efficiency comparison, but the superlative must be dropped or changed to "larger variance
than T3 while still biased". A false "smallest variance" line inside our own mock solutions
is the most dangerous kind of errata: the student has no reason to doubt it.

## 19. 2024-25 MTE QA2: the scheme marks B, but the CDF is option D

`md/paper-mte-2024-25/p001.md` gives

```
  f(x) = x       for 0 < x <= 1
         2 - x   for 1 <= x <= 2
```

For `1 <= x <= 2`, the CDF must include all mass accumulated before 1:

```
  F(x) = integral_0^1 t dt + integral_1^x (2-t) dt
       = 1/2 + 2x - x^2/2 - 3/2
       = 2x - x^2/2 - 1
```

That is option D. It also passes both endpoint checks, `F(1) = 1/2` and `F(2) = 1`.
The solution scheme on `md/paper-mte-2024-25-scheme/p001.md` marks QA2 as B. Option B
equals 3/2 at x = 1 and 2 at x = 2, so it cannot be a CDF. Use D.

## 20. 2025-26 MTE scheme Q4: the displayed integration bounds contradict the support

`md/paper-mte-2025-26-scheme/p001.md` prints the normalization and expectation integrals
from negative infinity to infinity, but the question defines the density only on `0 < x < 4`.
The scheme then evaluates the polynomial using 0 and 4, which is why its constants are right.

The valid written setup is:

```
  k integral_0^4 x^3(4-x)^2 dx = 1
  E(X) = k integral_0^4 x^4(4-x)^2 dx
  E(X^2) = k integral_0^4 x^5(4-x)^2 dx
```

The printed values `k = 15/1024`, `E(X) = 16/7`, `E(X^2) = 40/7`, and
`Var(X) = 24/49` are consistent with those finite bounds. The defect is in the displayed
bounds, not the final arithmetic.

## 21. 2025-26 MTE scheme Q8(ii): the last expectation inequality drops theta squared

`md/paper-mte-2025-26-scheme/p004.md` correctly reaches

```
  Var(t) = E(t^2) - theta^2 != 0
```

but the next source line prints `E(t^2) != 0`. That does not follow. Adding `theta^2` to
both sides gives the required result:

```
  E(t^2) != theta^2
```

That corrected relation proves `t^2` is a biased estimator of `theta^2`. The repository
transcription preserves the source's wrong line; use the correction above when studying.
