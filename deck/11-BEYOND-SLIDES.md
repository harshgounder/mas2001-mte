# 11 BEYOND SLIDES: what is asked but never taught

Eight items carry marks in every graded set we hold but have NO teaching slide in the converted
batch. They are the day-one priority: cheapest marks on the paper, and prerequisites for the
later topics. This file is the full treatment of each.

## H1. Independence rules of random variables

```
  why hidden   the notes deck teaches expectation to p094 and variance from p095, but the
               product rule and the variance-of-a-sum rule sit on edges the conversion did not
               capture as a named slide. Yet they gate four downstream topics.
  what it is   E(XY) = E(X) E(Y) when X, Y independent
               Var(X + Y) = Var(X) + Var(Y) when independent
               Var(X - Y) = Var(X) + Var(Y) when independent   (the minus stays plus)
               contrast: E(X + Y) = E(X) + E(Y) needs NO independence
  why it matters  every dice-sum variance, every Var(Xbar), every estimator variance, every
               Poisson additivity uses it. Without it, half the estimation block cannot be done.
  drill        Var(one die) = 35/12 -> Var(sum of two) = 35/6 -> the 35/54 Chebyshev bound
               Var(Xbar) = sigma^2/n is this rule applied n times
  real ask     R25S3-A1 asks E[XY] = E[X]E[Y] directly (confirmed this is a graded question)
```

## H2. Chebyshev's inequality (whole topic)

```
  why hidden   batch 1 had no Chebyshev slide at all. The L10-11 deck arrived 15 Sep and closed
               the gap, but it is the ONE deck that is genuinely new; everything else re-teaches.
  what it is   P(|X-mu| >= k sigma) <= 1/k^2, complement form >= 1 - 1/k^2
               k in sigma units. k=2 -> 3/4, k=3 -> 8/9, k=4 -> 15/16.
               No distribution assumed. Always an upper bound on the tail.
  why it matters  graded 9+ times: A1 MCQ5, MCQ10, short5, short6, app4; MTE 2024 QA3, QB3;
               MTE 2025 Q5; ETE S3 and S4 both years; 2025-26 bundle Q5.
  drill        dice 35/54 vs exact 1/3; 600 throws 19/24; marks 75 percent; inverse c from a
               stated bound (solve 1/k^2 = the given bound)
  trap         Q3 of the L10-11 deck mis-states its own row (errata 15), use Q1 and Q2 only
```

## H3. The memoryless property

```
  why hidden   no slide states P(T>s+t | T>s) = P(T>t).
  what it is   the exponential does not age: surviving s more, given you already survived,
               equals surviving s from scratch.
  why it matters  A2 MCQ Q5 and A2 section C Q1 both use it. It is one line to state and a
               full mark in a short answer.
  drill        P(T > 5 | T > 3) = P(T > 2). e^-1 = 0.3679 as the canonical number.
```

## H4. The 68 / 95 / 99.7 landmarks

```
  why hidden   no slide prints the empirical rule.
  what it is   68.27 percent within 1 sigma, 95.45 within 2, 99.73 within 3.
  why it matters  A2 MCQ Q11 uses it. Also the fast sanity check for any normal answer.
  drill        "what fraction lies within 2 sigma" -> 95.45.
```

## H5. Expected count, N x P

```
  why hidden   slides compute probabilities and expectations separately, never the "out of N
               items, how many" phrasing as a named method.
  what it is   expected number of items = N x P(success). It is expectation applied to a count.
  why it matters  A1 app, A2 B4 (5000 batteries), A2 D1 (10000 bulbs), the irregular die count
               (0.5499), and the new E25SUM-Q13 (800 families) and R25S4-B1 (heights > 6ft).
  drill        out of 10000 sets, expected = 10000 x (3/8)^10 = 0.5499
  trap         report N x P, not P. 0.5499, not 5.5e-5.
```

## H6. Geometric distribution

```
  why hidden   the notes deck uses a geometric count (p057-059) but never names E = 1/p as a
               result.
  what it is   X = trials until the first success. E(X) = 1/p, Var(X) = q/p^2.
  why it matters  A1 short Q4 asks the geometric expectation, E = 2. Graded once in batch 1,
               so it is live.
  drill        E = 1/p. For p = 1/2, E = 2. The "number of failures before" convention gives
               1/p - 1, read the wording.
```

## H7. Hypergeometric mean

```
  why hidden   no slide. It appears only in a question.
  what it is   drawing WITHOUT replacement from a finite lot: mean = n x K/N, the same value as
               the binomial mean at the same p.
  why it matters  A1 long Q3: lot of 25, 5 defective, sample of 4, mean = 4 x 5/25 = 0.80
               exactly, both with and without replacement.
  drill        nK/N, and note it equals np here. (errata 11: the key prints 0.808, wrong.)
```

## H8. The two normal table conventions

```
  why hidden   the deck uses a table but does not name phi(z) vs F(z) as two different
               conventions.
  what it is   phi(z) is often tabulated as the area from 0 to z; F(z) is the cumulative from
               -inf to z. They differ by 0.5 for z > 0.
  why it matters  every normal and CLT numeric goes through a table. Mixing the conventions is
               the single biggest source of normal marks lost.
  drill        P(Z < 0.12): from phi table, 0.5 + 0.0478 = 0.5478. From F table, read 0.5478
               directly. Same answer, different route. Always decide which table the question
               gives BEFORE substituting.
```

## The one-block summary (all eight, one line each)

```
  H1  E(XY)=E(X)E(Y), Var(X+Y)=Var(X)+Var(Y), Var(X-Y) adds    independence rules
  H2  Chebyshev, k in sigma, 1/k^2 tail, complement 1-1/k^2    the whole topic
  H3  memoryless P(T>s+t|T>s)=P(T>t), e^-1 = 0.3679            exponential
  H4  68.27 / 95.45 / 99.73                                     normal landmarks
  H5  expected count = N x P                                    the count question
  H6  geometric E = 1/p                                         discrete lifeline
  H7  hypergeometric mean = nK/N                                without replacement
  H8  phi(z) area-from-0 vs F(z) cumulative                     the table decision
```

Study order for these: H2 and H1 first (they gate the most), then H8 and H3, then H5, then
H6, H7, H4. Total about 1h40, and it is the best-spent time before the paper.
