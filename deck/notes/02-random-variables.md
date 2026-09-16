# 02 RANDOM VARIABLES (notes p051-p062)

## 1. What a random variable IS (p051)

```
  ┌────────────────────────────────────────────────────────────────┐
  │  A random variable is a FUNCTION whose domain is the sample    │
  │  space and whose range is the set of real numbers.             │
  │                                                                │
  │  It is NOT the outcome. It is the NUMBER you attach to it.    │
  └────────────────────────────────────────────────────────────────┘
```

```
       sample space S                      the real line
      ┌──────────────┐                   ┌──────────────┐
      │  H    T      │  ──── X ────▶     │  1    0      │
      └──────────────┘    (a function)  └──────────────┘
        outcomes                          numbers

      X(H) = 1        X(T) = 0
```

```
                       RANDOM VARIABLE
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
        ┌───────────┐                   ┌────────────┐
        │ DISCRETE  │                   │ CONTINUOUS │
        │ countable │                   │ interval   │
        │ list them │                   │ can't list │
        │ use SUMS  │                   │ use ∫      │
        └───────────┘                   └────────────┘
```

## 2. Example 1: Bernoulli (p052)

```
  toss one fair coin, S = {H, T}
  define X(H) = 1,  X(T) = 0

  ┌──────────────────────────────────────────────────────────┐
  │ DEFINITION: any rv whose only values are 0 and 1 is a     │
  │ BERNOULLI random variable.                                │
  └──────────────────────────────────────────────────────────┘
```

Bernoulli is the atom of the binomial: one trial, success = 1, failure = 0.

## 3. Example 2: two coins (p053)

```
  S = {HH, HT, TH, TT}
  X = number of heads

       outcome     X value
       ───────     ───────
         HH           2
         HT           1
         TH           1
         TT           0

  X(HH)=2,  X(TT)=0,  X(TH)=1,  X(HT)=1
```

Notice HT and TH give the SAME X. Different outcomes, same value. That collapse is how a pmf is born (next file).

## 4. Example 3: dice sum (p054-p055)

```
  X = sum of two fair dice

   x    outcomes producing it         count   P(X=x)
  ───   ──────────────────────────     ─────   ──────
   2    (1,1)                            1      1/36
   3    (1,2)(2,1)                       2      2/36
   4    (1,3)(2,2)(3,1)                  3      3/36
   5    (1,4)(2,3)(3,2)(4,1)             4      4/36
   6    5 outcomes                       5      5/36
   7    6 outcomes                       6      6/36   <- peak
   8    5 outcomes                       5      5/36
   9    4 outcomes                       4      4/36
  10    3 outcomes                       3      3/36
  11    (5,6)(6,5)                       2      2/36
  12    (6,6)                            1      1/36
                                          Σ     36/36 = 1  ✓
```

The pmf as a picture:

```
   P(x)
   6/36 │           █
   5/36 │         █ █ █
   4/36 │       █ █ █ █ █
   3/36 │     █ █ █ █ █ █ █
   2/36 │   █ █ █ █ █ █ █ █ █
   1/36 │ █ █ █ █ █ █ █ █ █ █ █
        └─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─▶ x
          2 3 4 5 6 7 8 9 10 11 12
                    ▲
                 triangular, peaks at 7
```

The identity the slide writes:

```
              12
   1 = P( ∪   (X=n) ) = Σ  P(X=n)
              n=2       n=2
```

## 5. Example 4: two coins as Y = heads (p056)

```
   P(Y=0) = P(TT)      = 1/4
   P(Y=1) = P(HT,TH)   = 2/4
   P(Y=2) = P(HH)      = 1/4
   sum = 1  ✓
```

## 6. Example 5: geometric (p057-p059) - counts flips until first head

```
   N = number of flips needed to get the first head

   P(N=1) = P(H)          = p
   P(N=2) = P(TH)         = (1-p)p
   P(N=3) = P(TTH)        = (1-p)^2 p
   ...
   P(N=n) = (T...TH)      = (1-p)^(n-1) p
```

```
    p
    │█
    │█ █
    │█ █ ▒
    │█ █ ▒ ▒
    │█ █ ▒ ▒ ▒  .  .  .  .        <- each bar smaller by factor (1-p)
    └───────────────▶ n
     1 2 3 4 5 ...
```

The sum verification (infinite geometric series, common ratio (1-p)):

```
   Σ (1-p)^(n-1) p  =  p / (1 - (1-p))  =  p/p  =  1   ✓
```

```
  ┌───────────────────────────────────────────────────────────┐
  │ This is the GEOMETRIC distribution. Mean = 1/p.           │
  │ It has NO teaching slide for its mean, but the exam       │
  │ asks it (assignment 1 short Q4: E = 2).                   │
  └───────────────────────────────────────────────────────────┘
```

## 7. Example 6: car lifetime (p060) - the bridge to continuous

```
   X = lifetime of a car, assumed to take any value in an interval (a,b)
   - not countable, cannot be listed as a sequence
   -> NOT a discrete rv
```

## 8. Discrete vs continuous, the definitions (p061-p063)

```
  ┌────────────────────────────────┬────────────────────────────────┐
  │ DISCRETE                       │ CONTINUOUS                     │
  ├────────────────────────────────┼────────────────────────────────┤
  │ finite OR countably infinite   │ all values in an interval      │
  │ can be arranged as a sequence  │ CANNOT be listed as a sequence │
  │ 1st, 2nd, 3rd, ...             │                                │
  │                                │ P(X = any single c) = 0        │
  └────────────────────────────────┴────────────────────────────────┘
```

The formal continuous definition has TWO parts:

```
   1. possible values = all numbers in one interval (or a union of intervals)
      e.g. [0,10] ∪ [20,30]
   2. NO single value has positive probability:  P(X = c) = 0
```

```
  ╔════════════════════════════════════════════════════════════╗
  ║  WHY P(X=c)=0 FOR CONTINUOUS                               ║
  ║  P(X=c) = ∫ from c to c of f(x) dx = 0                     ║
  ║  the width is zero, an area of zero width is zero          ║
  ║  -> endpoints never matter: P(a<X<b) = P(a≤X≤b)            ║
  ╚════════════════════════════════════════════════════════════╝
```

## 9. The summary table to memorise

```
   ┌──────────────┬─────────────────┬─────────────────────────┐
   │              │ DISCRETE        │ CONTINUOUS              │
   ├──────────────┼─────────────────┼─────────────────────────┤
   │ support      │ list of values  │ interval(s)             │
   │ tool         │ Σ (sum)         │ ∫ (integral)            │
   │ P(X=x)       │ p(x) > 0        │ 0 always                │
   │ E(X)         │ Σ x p(x)        │ ∫ x f(x) dx             │
   │ Var(X)       │ Σ (x-μ)²p(x)    │ ∫ (x-μ)²f(x) dx         │
   │ named        │ binomial,       │ uniform, normal,        │
   │ examples     │ Poisson, geo    │ exponential             │
   └──────────────┴─────────────────┴─────────────────────────┘
```

---
Next file builds the pmf and cdf (the two functions that describe any rv).
