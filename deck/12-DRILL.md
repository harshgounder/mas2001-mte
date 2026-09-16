# 12 DRILL: the practice set with answers

Solve, then check. Each item names its distribution and slot so you can trace the method back
to 04-METHODS.md. Answers are exact where the source gives an exact value.

## Warm-up: probability and counting

```
  D1   Six faculty, choose 3 for laptops. How many ways?
       ans  C(6,3) = 20
  D2   A camera chain: P(works each step) given. P(all three work)?
       ans  product of the three, from the multiplication rule
  D3   "At least one" heads in 3 fair coins.
       ans  1 - (1/2)^3 = 7/8   (complement)
```

## Binomial

```
  D4   B(12, 0.1). P(X=2).             ans 66 x 0.01 x 0.348678 = 0.2301
  D5   B(12, 0.1). P(X>=2).            ans 1 - 0.2824 - 0.3766 = 0.3410
  D6   B(12, 0.1). P(X=0).             ans 0.2824
  D7   Irregular die, P(X=5)=2P(X=4). Find p.   ans 5/8
  D8   Same die, 10 throws, P(no even).         ans (3/8)^10 = 5.499e-5
  D9   Out of 10000 sets of 10, expected with no even number.   ans 0.5499
  D10  B(600, 1/6). E and Var.         ans 100, 250/3
```

## Poisson

```
  D11  P(X=1)=0.2 P(X=2). Find l.      ans l = 10
  D12  Same, P(X=0).                   ans e^-10 = 4.54e-5
  D13  Calls at 2/min. P(exactly 2 in a minute).   ans 2e^-2 = 0.2707
  D14  P(exactly 2 in each of 5 minutes).          ans (2e^-2)^5 = 32e^-10 = 0.00145
  D15  5000 men, death rate 0.001. P(X=4).         ans e^-5 5^4/4! = 0.1755
  D16  P(X>2) with l=5.                ans 0.8753
  D17  "Rejected" P(X>=4) with l appropriate.      ans 0.2424
```

## Uniform

```
  D18  U(2,6). f, mean, variance.      ans 0.25, 4, 1.3333
  D19  U(2,6). P(3<X<5).               ans 2/4 = 0.50
  D20  U(2,6). P(X<1).                 ans 0 (below support)
```

## Normal

```
  D21  N(8,5). P(X<8.6).               ans Z=0.12, 0.5478
  D22  N(8,5). P(X>8.6).               ans 0.4522
  D23  N(8,5). Find x for P(X<x)=0.20. ans Z=-0.8416, x=3.792
  D24  Marks: pass 40 = 46 percent, distinction 75 = 9 percent. Find mu, sigma.
       ans sigma = 28.2, mu = 37.2
  D25  Same, re-exam cutoff at the 24 percent lower tail.   ans 30.4
  D26  N(100,50^2), X=200. Find Z.     ans 2.0
```

## Exponential

```
  D27  15/hour. P(gap < 3 min).        ans 0.05 hr, 1-e^-0.75 = 0.5276
  D28  15/hour. Mean gap.              ans 4 minutes
  D29  Mean 2. P(X<1 | X<2).           ans 0.6225
  D30  f(x)= x e^-x/3 / 9, P(X>12).    ans 5e^-4 = 0.0916
  D31  Memoryless: P(T>8 | T>5).       ans P(T>3) = e^-3l
```

## Chebyshev

```
  D32  Two dice, P(|X-7|>=3) bound.    ans sigma^2=35/6, k=3, 35/54 = 0.6481, exact 1/3
  D33  600 throws, P(80<=X<=120) lower bound.   ans 19/24 = 0.7917
  D34  Mean 70, var 25, P(60<X<80) lower bound.  ans k=2, 0.75
  D35  mu=10, var=4, P(5<X<15) and P(|X-10|>=3).  ans 1-4/25=21/25=0.84, and 4/9=0.4444
  D36  Find c so P(|X-10|>=c) <= 0.04, var 4.    ans k=5, c=10
```

## Sampling, CLT

```
  D37  sigma=100, n=25 then n=100. Find SE.       ans 20 then 10
  D38  mu=4, sigma=2, n=36. P(Xbar>4.5).          ans Z=1.50, 0.0668
  D39  mu=4.0, sigma=1.5, n=50. P(3.5<Xbar<3.8).  ans Z1=-2.36, Z2=-0.94, 0.1644
  D40  mu=50000, sigma=8000, n=64. P(Xbar<48000). ans Z=-2.00, 0.0228
  D41  mu=7, sigma=1, n=9 (normal pop). P(6.4<Xbar<7.2).  ans Z1=-1.80, Z2=0.60, 0.6898
```

## Estimation

```
  D42  Sample of 5 normal; t1=mean, t2=(X1+X2)/2+X3, t3=(2X1+X2+lambda X3)/3.
       Find lambda, the unbiased ones, variances, the best.
       ans lambda=0; t1 and t3 unbiased, t2 not; Var 0.2, 1.5, 0.5556 sigma^2; best t1
  D43  T1=X1+X2-X3, T2=2X1+3X3-4X2, T3=(lambda X1+X2+X3)/3.
       Find lambda, unbiased set, variances, best, and comment on consistency.
       ans lambda=1; all unbiased; Var 3, 29, 1/3 sigma^2; best T3; T3 is the sample mean so
           it is consistent, T1 is not a consistency statement (fixed n=3)
  D44  n=25, Xbar=8.4, sigma=1.5, 95 percent interval.    ans 8.4 +- 0.588 = (7.81, 8.99)
  D45  Response times sum 1640, n=8. Point estimate.      ans 205 ms
  D46  465 of 500 packets succeed. Point estimate of p.   ans 0.93
```

## The four high-risk siblings (from 07-PATTERNS, do these)

```
  D47  Normal one-unknown: 30 percent below 45 and 8 percent above 64, find mu, sigma.
  D48  Binomial two-sided interval: B(12,0.1), P(2<=X<=4) = ?
  D49  CLT for a SUM: n=40 draws, mu=10, sigma=3. P(sum > 440)?
       ans sum ~ N(400, 360), Z = (440-400)/sqrt(360) = 2.108, tail 0.0175
  D50  Discrete conditional: B(10,0.5), P(X=5 | X>=3) = P(5)/(1-P(0)-P(1)-P(2))
```

## The self-check rule

If you can do D4 to D46 without notes, you are at the level where the paper's Section B and C
are mechanical. If D47 to D50 are also fine, you are covered on the mutation surface. Anything
below that, go back to 04-METHODS.md for that slot before trying more questions.
