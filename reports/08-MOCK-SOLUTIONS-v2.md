# Mock MTE v2, worked solutions

Mark total: Section A 6, Section B 16, Section C 8, total 30.

## Section A

### Q1

Option 2. By definition, $F_X(x)=P(X\leq x)$. (2)

Source: `md/notes-lecture-series-01-09/p074.md`.

### Q2

Option 2. Chebyshev requires a finite mean and finite variance, not a named distribution. (2)

Source: `reports/03-FORMULA-SHEET.md`, section E, and the 9-page L10-11 deck.

### Q3

Option 3. Since $SE(\bar X)=\sigma/\sqrt n$, halving SE requires multiplying n by 4.
Thus 25 becomes 100. (2)

Source: `md/lms-standard-error-clt/p004.md`.

## Section B

### Q4, Chebyshev

The standard deviation is $\sigma=\sqrt{25}=5$.

1. The interval 60 to 80 is $|X-70|<10=2\sigma$. Therefore

$$P(|X-70|<2\sigma)\geq1-\frac1{2^2}=\frac34.$$

The minimum proportion is 0.75, or 75 percent. (2: one for $k=2$, one for the bound.)

2. Below 55 or above 85 is $|X-70|\geq15=3\sigma$. Therefore

$$P(|X-70|\geq3\sigma)\leq\frac1{3^2}=\frac19.$$

The upper bound is $1/9$, approximately 0.1111. (2: one for $k=3$, one for the tail bound.)

### Q5, binomial

Here $n=15$, $p=0.08$, and $q=0.92$.

1. $X\sim B(15,0.08)$. (1)
2. $P(X=1)=\binom{15}{1}(0.08)(0.92)^{14}=0.373431$, so 0.3734. (1)
3. $P(X\geq1)=1-P(X=0)=1-(0.92)^{15}=0.713703$, so 0.7137. (1)
4. $E(X)=np=1.2$ and $Var(X)=npq=1.104$. (1)

Source: `md/ppt3-discrete-prob-dist/p009.md` and `p012.md`.

### Q6, normal

The standard deviation is $\sigma=\sqrt{100}=10$.

1. $z=(65-50)/10=1.5$, so $P(X<65)=\Phi(1.5)=0.9332$. (1)
2. $z=(35-50)/10=-1.5$. By symmetry, $P(X>35)=\Phi(1.5)=0.9332$. (1)
3. The 0.90 quantile has $z=1.2816$, hence

$$x=\mu+z\sigma=50+1.2816(10)=62.816.$$

Thus $x\approx62.82$. (2: one for z, one for returning to X units.)

Source: `md/ppt4-continuous-prob-dist/p007.md` to `p037.md`.

### Q7, estimation

Using $E(X_i)=\mu$,

$$E(T_1)=\mu,\quad E(T_2)=\mu,\quad E(T_3)=\mu,\quad E(T_4)=\frac32\mu.$$

Therefore $T_1,T_2,T_3$ are unbiased and $Bias(T_4)=\mu/2$. (2)

Independence gives

$$Var(T_1)=\sigma^2,\quad Var(T_2)=\frac{\sigma^2}{2},\quad
Var(T_3)=\frac{\sigma^2}{3},\quad Var(T_4)=\frac{3\sigma^2}{4}.$$

Among the unbiased estimators, $T_3$ has the smallest variance and is most efficient. (1)

For a sample mean based on n observations, the expectation stays $\mu$ while the variance
$\sigma^2/n$ tends to zero. For $T_1$, the variance remains $\sigma^2$, so it does not
concentrate around $\mu$. (1)

Source: `md/ppt5-estimation-summary/p015.md` to `p021.md`.

## Section C

### Q8.1, uniform

The density is $f_X(x)=1/6$ on $(2,8)$ and zero elsewhere. Integrating by region gives

$$F_X(x)=\begin{cases}
0, & x\leq2,\\
\dfrac{x-2}{6}, & 2<x<8,\\
1, & x\geq8.
\end{cases}$$

Hence $P(X<5)=F_X(5)=(5-2)/6=1/2$. (4: one for each CDF region and one for the probability.)

Source: `md/ppt4-continuous-prob-dist/p001.md` to `p006.md`.

### Q8.2, Poisson

For $Y\sim Poisson(3)$,

$$P(Y=0)=e^{-3}=0.049787,$$

$$P(Y\geq1)=1-P(Y=0)=1-e^{-3}=0.950213.$$

Also $E(Y)=3$ and $Var(Y)=3$. (4: one mark per requested result.)

Source: `md/ppt3-discrete-prob-dist/p019.md` to `p023.md`.

## Mark check

```
  Section A    3 x 2       6
  Section B    4 x 4      16
  Section C    1 x 8       8
  total                   30
```
