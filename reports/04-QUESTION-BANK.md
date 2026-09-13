# Question bank with verified answers

Every problem the corpus itself poses, with the answer re-derived on the machine rather than
copied from the slide. Where the slide's printed answer differs from the computed one, the
difference is recorded in `reports/09-ERRATA.md` and flagged here with the word SLIDE.

Page refs are the pipeline page numbers, so `ppt3 p014` means `md/ppt3-discrete-prob-dist/p014.md`.

---

## 1. Binomial

### 1.1 Pens, defective rate 10 percent, box of 12 (ppt3 p013 to p016)

Find the probability that the box contains (i) exactly 2 defective pens, (ii) at least 2,
(iii) no defective pen.

```
  X ~ B(12, 0.1), q = 0.9

  (i)   P(X = 2) = C(12,2)(0.1)^2(0.9)^10 = 66 x 0.01 x 0.348678 = 0.230128   slide 0.2301  OK
  (ii)  P(X >= 2) = 1 - P(X=0) - P(X=1)
                  = 1 - 0.282430 - 0.376573 = 0.340998                      slide 0.341   OK
  (iii) P(X = 0) = (0.9)^12 = 0.282430                                        slide 0.2824  OK
  check: sum over x = 0 to 12 equals 1.000000000000
```

### 1.2 Irregular die, P(X=5) = 2 P(X=4) in 10 throws (ppt3 p017 to p018)

Find the expected number of sets with no even number out of 10,000 sets of 10 throws.

```
  C(10,5) p^5 q^5 = 2 C(10,4) p^4 q^6   ->   252 p = 420 q   ->   p = 5/8, q = 3/8
  P(X = 0) = (3/8)^10 = 0.00005499
  expected sets = 10000 x 0.00005499 = 0.5499                                slide 0.549  SLIDE
```

The slide truncates to 0.549, the value is 0.5499 and rounds to 0.550. Not worth marks, but
do not write 0.549 as though it were exact.

---

## 2. Poisson

### 2.1 Lambda from a probability ratio (ppt3 p025)

P(X=1) = 0.2 P(X=2). Find P(X=0).

```
  e^-l l / 1! = 0.2 e^-l l^2 / 2!   ->   1 = 0.1 l   ->   l = 10
  P(X = 0) = e^-10 = 0.0000454                                               slide 0.0000454  OK
```

### 2.2 Telephone calls, rate 2 per minute (ppt3 p026)

Probability that exactly two calls arrive in each of the first five minutes.

```
  P(N = 2) = e^-2 2^2 / 2! = 2e^-2 = 0.270671
  M = number of minutes out of 5 with exactly 2 calls, M ~ B(5, 0.270671)
  P(M = 5) = (2e^-2)^5 = 32 e^-10 = 0.00145280                               slide 0.00145  OK
```

The two step structure is the point here: a Poisson count, then a binomial over the five
minutes. Expect this shape.

### 2.3 Life insurance, 5000 men, death rate 0.001 (ppt3 p027)

Probability of exactly 4 claims in a year.

```
  l = np = 5000 x 0.001 = 5
  P(X = 4) = e^-5 5^4 / 4! = 0.175467                                        slide 0.1745  SLIDE
```

The slide prints 0.1745, the computed value is 0.175467 which rounds to 0.1755. In a written
answer, 0.1755 shown with working is safer than the slide's number.

---

## 3. Uniform

### 3.1 Uniform on 2 to 6 (ppt4 p003 to p006)

```
  f(x) = 1/(6-2) = 0.25 for 2 <= x <= 6
  mu = (2+6)/2 = 4
  sigma^2 = (6-2)^2/12 = 1.333333
  derived addition: P(3 < X < 5) = length ratio = 2/4 = 0.50
```

---

## 4. Normal

### 4.1 Lower tail, mean 8, sigma 5 (ppt4 p030 to p031)

Find P(X < 8.6).

```
  Z = (8.6 - 8)/5 = 0.12
  P(X < 8.6) = P(Z < 0.12) = F(0.12) = 0.547758                              slide 0.5478  OK
```

### 4.2 Upper tail, same parameters (ppt4 p032 to p033)

Find P(X > 8.6).

```
  P(X > 8.6) = 1 - P(Z <= 0.12) = 1 - 0.5478 = 0.452242                     slide 0.4522  OK
```

### 4.3 Inverse problem, finding X from a known probability (ppt4 p034 to p037)

Steps the deck gives: find Z for the known probability, then convert with X = mu + Z sigma.

```
  For a lower tail of 20 percent, z = -0.8416, so X = mu - 0.8416 sigma
  With mu = 8 and sigma = 5 this is 8 - 4.208 = 3.792                        slide 3.792   OK
```

The forgotten step in exams is the last one: getting Z from the table and then not converting
back into the X scale.

---

## 5. Exponential

### 5.1 Arrivals at 15 per hour, gap under three minutes (ppt4 p039 to p043)

```
  l = 15 per hour, t = 3 minutes = 0.05 hours
  P(T < 0.05) = 1 - e^-(15 x 0.05) = 1 - e^-0.75 = 0.527633                 slide 0.5276  OK
  mean gap = 1/l = 1/15 hour = 4 minutes
  variance = 1/l^2 = 1/225 hour^2
```

Time units must match the rate units. The paper will most likely mix minutes and hours.

---

## 6. Chebyshev, no slides exist for this topic

Three shapes are enough. All values computed.

```
  tail form        P(|X - mu| >= k sigma) <= 1/k^2
  complement form  P(|X - mu| <  k sigma) >= 1 - 1/k^2
  thresholds       k=2 -> 3/4,  k=3 -> 8/9,  k=4 -> 15/16,  k=1 -> bound of 1, useless
```

### 6.1 Two fair dice, sum, deviation of 3 or more (assignment 1 short Q5)

```
  Var(one die) = 35/12, Var(sum of two) = 35/6, sigma^2 = 35/6
  k = 3:  P(|X-7| >= 3) <= (35/6)/9 = 35/54 = 0.648148
  exact:  outcomes with sum <= 4 or sum >= 10 are 12 of 36, so 1/3 = 0.333333
```

The bound is loose by design. If asked to compare, say the bound holds and is much wider than
the exact value.

### 6.2 Sixes in 600 throws (assignment 1 short Q6)

```
  X ~ B(600, 1/6), mu = 100, sigma^2 = 250/3
  P(80 <= X <= 120) = P(|X - 100| < 20), so k = 20 and sigma^2 = 250/3
  lower bound = 1 - (250/3)/400 = 1 - 5/24 = 19/24 = 0.791667
  exact binomial probability = 0.975429
```

### 6.3 Marks, mean 70, variance 25 (assignment 1 application Q4)

```
  between 60 and 80 means |X-70| < 10, k = 10/5 = 2
  P >= 1 - 1/4 = 0.75
```

---

## 7. Assignment 1, the tagged paper with the official key

Short answers, all confirmed against the key by recomputation:

```
  Q1  coin, three children      pmf 1/8, 3/8, 3/8, 1/8 ; CDF 0, 1/8, 4/8, 7/8, 1
  Q2  mortality style pdf       P(X>12) = 5e^-4 = 0.091578, key prints 0.0915, see errata
  Q3  f(x) = 6x(1-x)            valid pdf, b = 1/2
  Q4  geometric expectation     E = 2
  Q5  dice Chebyshev            35/54 against an exact 1/3
  Q6  600 throws                19/24
  Long 1  mortality integral    0.154360 and the conditional 0.486265
  Long 2  pmf with unknown k    k = 1/10 exactly, P(X<6) = 0.81, P(X>=6) = 0.19, c = 4, 5/7
  Lot of 25 items, 5 defective  hypergeometric mean is exactly 0.8 in both cases
  Four bad oranges              12/19, 32/95, 3/95
  Application 1                 sensor batch, valid pmf, E = 1.2, Var = 0.86
  Application 2                 CDF 0.15, 0.50, 0.80, 1.00
  Application 3                 battery, mean 3.45, Var 0.9475, sd 0.98
```

The two places your own submission departs from the key are analysed in
`reports/02-MTE-REPORT.md` section 6 and are both inside long Q2.

---

<!-- SECTIONS 8 AND 9 ARE APPENDED WHEN THE LIMIT THEOREM AND ESTIMATION DECKS FINISH CONVERTING -->
