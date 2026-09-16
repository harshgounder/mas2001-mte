# 06 BINOMIAL AND POISSON (ppt3, 28 pages, lectures 12-13)

## PART A: BINOMIAL

### 1. The derivation from 5 coin tosses (p003-p007)

```
   QUESTION: P(exactly 3 heads in 5 tosses)?
```

```
   one arrangement: HHHTT
      P = (1/2)(1/2)(1/2)(1/2)(1/2) = (1/2)^3 (1/2)^2

   another: THHHT
      P = (1/2)(1/2)(1/2)(1/2)(1/2) = (1/2)^3 (1/2)^2

   EVERY arrangement with 3 H and 2 T has the SAME probability.
```

```
   how many arrangements?    5 positions, choose 3 for H

      C(5,3) = 5!/(3! 2!) = 120/(6x2) = 10
```

```
   the 10 arrangements, all equally likely:

      THHHT   HHHTT   TTHHH   HTTHH   HHTTH
      HTHHT   THTHH   HTHTH   HHTHT   THHTH
```

```
   THEREFORE:
      P(3 heads and 2 tails)
        = C(5,3) x P(H)^3 x P(T)^2
        = 10 x (1/2)^5
        = 10/32 = 0.3125 = 31.25%
```

```
  ┌──────────────────────────────────────────────────────────┐
  │ THE STRUCTURE, IN ONE PICTURE:                            │
  │   [number of arrangements]  x  [probability of one]       │
  │        C(n,x)                     p^x q^(n-x)             │
  └──────────────────────────────────────────────────────────┘
```

### 2. The setup conditions (p008-p011)

```
   a random experiment performed repeatedly
   "success" = the event occurs, "failure" = it does not
```

```
  ╔═══════════════════════════════════════════════════════════╗
  ║ PHYSICAL CONDITIONS FOR A BINOMIAL                       ║
  ║  1. each trial gives TWO mutually disjoint outcomes       ║
  ║  2. n, the number of trials, is FINITE                    ║
  ║  3. the trials are INDEPENDENT                            ║
  ║  4. p, the success probability, is CONSTANT               ║
  ╚═══════════════════════════════════════════════════════════╝
```

```
   q = 1 - p   (failure probability)
```

### 3. The definition (p009-p010)

```
        P(X = x) = C(n,x) p^x q^(n-x),    x = 0,1,2,...,n
        P(X = x) = 0                      otherwise
```

```
   n and p are the PARAMETERS.   n is also called the DEGREE.
   NOTATION:  X ~ B(n, p)
```

### 4. Mean and variance

```
        E(X) = n p
        Var(X) = n p q
        SD = √(n p q)
```

### 5. WORKED: pens (p013-p016) - the flagship example

```
   10% of pens are defective. A box has 12 pens.
   X = number of defective pens in the box.
   n = 12,  p = 0.1,  q = 0.9      X ~ B(12, 0.1)
```

```
   (i) EXACTLY 2:
       P(X=2) = C(12,2) (0.1)²(0.9)^10
              = 66 x 0.01 x 0.3487
              = 0.2301
```

```
   (ii) AT LEAST 2  (use the COMPLEMENT):
       P(X≥2) = 1 - P(X<2) = 1 - [P(X=0) + P(X=1)]

       P(X=0) = C(12,0)(0.1)^0(0.9)^12 = 0.2824
       P(X=1) = C(12,1)(0.1)^1(0.9)^11 = 12 x 0.1 x 0.3138 = 0.3766

       P(X≥2) = 1 - [0.2824 + 0.3766] = 1 - 0.659 = 0.341
```

```
   (iii) NONE:
       P(X=0) = 0.2824
```

```
  ╔══════════════════════════════════════════════════════════════╗
  ║ THE "AT LEAST 2" MOVE IS THE WHOLE POINT OF THIS EXAMPLE.    ║
  ║ Summing P(2)+P(3)+...+P(12) is 11 terms.                     ║
  ║ Complementing is 2 terms. ALWAYS complement for "at least".  ║
  ╚══════════════════════════════════════════════════════════════╝
```

```
   the pmf picture for B(12, 0.1):

   P(x)
   .38 │  █
   .28 │  █  █
   .23 │  █  █
   .17 │  █  █  ▒
   .10 │  █  █  ▒  ▒
   .03 │  █  █  ▒  ▒  ▒  .  .
       └──┬──┬──┬──┬──┬──┬──┬──▶ x
          0  1  2  3  4  5  6 ...
          ▲  ▲
       P0=.28 P1=.38  <- note P1 > P0 here (p=0.1, n=12, mode at x=1)
```

### 6. WORKED: irregular die (p017-p018) - the parameter recovery

```
   A six-faced die. P(5 evens in 10 throws) = 2 x P(4 evens in 10 throws).
   In 10,000 sets of 10 throws, expected number with NO even number?
```

```
   set the condition:
       C(10,5) p^5 q^5 = 2 x C(10,4) p^4 q^6

       252 p^5 q^5 = 2 x 210 p^4 q^6
       252 p = 420 q                     (divide by p^4 q^5)
       3p = 5q = 5(1-p)
       3p = 5 - 5p
       8p = 5
       p = 5/8,   q = 3/8
```

```
   then:
       P(X=0) = C(10,0)(5/8)^0(3/8)^10 = (3/8)^10 = 0.00005499

       expected number out of 10,000
         = 10000 x 0.00005499 = 0.5499
```

```
  ╔══════════════════════════════════════════════════════════════╗
  ║ TWO SKILLS IN ONE QUESTION:                                  ║
  ║  1. recover p from a ratio P(X=k+1) = c P(X=k)                ║
  ║     (the C's and the powers of q cancel, leaving a linear eq) ║
  ║  2. EXPECTED COUNT = N x P   (not P alone!)                   ║
  ║     0.5499, NOT 0.00005499                                    ║
  ╚══════════════════════════════════════════════════════════════╝

  ERRATA 2: the slide prints 0.549; the exact value is 0.5499.
```

## PART B: POISSON

### 7. What it models (p019-p021)

```
  ┌───────────────────────────────────────────────────────────────┐
  │ Poisson models the number of "RARE EVENTS" occurring randomly  │
  │ in a fixed interval.                                          │
  └───────────────────────────────────────────────────────────────┘
```

```
   the slide's seven instances:
     1. deaths from a disease (heart attack, cancer, snake bite)
     2. suicides reported in a city
     3. defective material in a packing
     4. faulty blades in a packet of 100
     5. air accidents in a unit of time
     6. printing mistakes per page of a book
     7. cars passing a crossing per minute (busy hours)
```

### 8. Poisson as the limit of binomial (p022)

```
   under these three conditions:
      1. n → ∞                indefinitely large
      2. p → 0                indefinitely small
      3. np = λ, finite       p = λ/n,  q = 1 - λ/n
```

```
   B(n,x) p^x q^(n-x)  ──limit──▶  e^{-λ} λ^x / x!     with λ = np
```

```
  ┌──────────────────────────────────────────────────────────┐
  │ "USE THE APPROXIMATION" IN A QUESTION MEANS:              │
  │   Poisson with λ = n p, NOT the exact binomial.          │
  │   e.g. 5000 men, p=0.001  ->  λ = 5                       │
  └──────────────────────────────────────────────────────────┘
```

### 9. The definition (p023-p025)

```
        P(X = x) = e^{-λ} λ^x / x!,    x = 0,1,2,...,  λ > 0
        P(X = x) = 0                   otherwise
```

```
   λ is the PARAMETER.   NOTATION:  X ~ P(λ)
```

```
        E(X) = λ          Var(X) = λ          ← MEAN EQUALS VARIANCE
```

```
  ╔══════════════════════════════════════════════════════════════╗
  ║ MEAN = VARIANCE IS THE POISSON FINGERPRINT                   ║
  ║ If a question gives you a mean and a variance and they are    ║
  ║ EQUAL, it is asking you to recognise Poisson.                 ║
  ║ If they differ, it is NOT Poisson.                            ║
  ╚══════════════════════════════════════════════════════════════╝
```

### 10. WORKED: parameter from a ratio (p025)

```
   P(X=1) = 0.2 P(X=2).   Find P(X=0).
```

```
      e^{-λ} λ^1        e^{-λ} λ^2
      ────────── = 0.2 ──────────
          1!               2!

      λ = 0.2 λ²/2 = 0.1 λ²
      1 = 0.1 λ         (divide by λ, λ>0)
      λ = 10
```

```
   then:
      P(X=0) = e^{-10} 10^0/0! = e^{-10} = 0.0000454
```

```
   the cancellation picture:

      e^{-λ} λ        =  0.2  x   e^{-λ} λ²
      └─┬──┘                     └─┬──┘
      cancels                    cancels
              λ      =  0.2 λ²/2
              ────────►  λ = 10
```

### 11. WORKED: telephone calls, THE NESTING (p026)

```
   calls arrive at λ = 2 per minute.
   P(exactly two calls in each of the first 5 minutes)?
```

```
   STEP 1: Poisson within ONE minute
       P(N=2) = e^{-2} 2²/2! = 2e^{-2} = 0.270671

   STEP 2: binomial over the FIVE minutes
       M = number of minutes (of 5) with exactly 2 calls
       M ~ B(5, 0.270671)

       P(M=5) = (2e^{-2})^5 = 32 e^{-10} = 0.00145
```

```
   THE STRUCTURE:

      ┌────────────────────────┐
      │ minute 1 .. minute 5   │   ← binomial: how many of the 5?
      └────────────────────────┘
              │
        for EACH minute:
      ┌────────────────────────┐
      │ calls in that minute   │   ← Poisson: exactly 2?
      └────────────────────────┘
              │
         P = 2e^{-2} per minute
              │
      P(all 5 succeed) = (2e^{-2})^5
```

```
  ╔══════════════════════════════════════════════════════════════╗
  ║ THIS IS THE COMPOSITION (SLOT 9) QUESTION SHAPE.             ║
  ║ The inner model gives a probability. That probability then    ║
  ║ becomes the p of an outer binomial.                           ║
  ║ Recognise: "in EACH of the k intervals" -> nest.              ║
  ╚══════════════════════════════════════════════════════════════╝
```

### 12. WORKED: life insurance (p027)

```
   5000 men aged 42, P(death in a year) = 0.001.
   P(exactly 4 claims)?
```

```
   λ = n p = 5000 x 0.001 = 5

   P(X=4) = e^{-5} 5^4 / 4! = e^{-5}(625/24)
          = 0.0067379 x 26.0417 = 0.175467
```

```
  ERRATA 1: the slide prints 0.1745. The correct value rounds to 0.1755.
```

### 13. The tail form (p028)

```
   P(X > 2) = 1 - P(0) - P(1) - P(2)

   general:  P(X > k) = 1 - Σ_{i=0}^{k} P(X=i)
```

## PART C: THE DISCRETE DISTRIBUTIONS SIDE BY SIDE

```
   ┌────────────┬──────────────────┬──────────────────┐
   │            │ BINOMIAL         │ POISSON          │
   ├────────────┼──────────────────┼──────────────────┤
   │ models     │ # successes in   │ # rare events in │
   │            │ n trials         │ a fixed interval │
   │ setup      │ n finite, indep, │ rare, indep in   │
   │            │ p constant       │ time/space       │
   │ pmf        │ C(n,x)p^x q^n-x  │ e^-λ λ^x / x!    │
   │ mean       │ np               │ λ                │
   │ variance   │ npq              │ λ                │
   │ signature  │ npq < np always  │ mean = variance  │
   │ link       │  n→∞,p→0,np=λ ───▶│ (the limit)      │
   └────────────┴──────────────────┴──────────────────┘
```

```
   the pmf shapes:

   B(12,0.1)              B(10,0.5)            Poi(3)
   .38│ █                 .25│      █           .22│
   .28│ █ █               .20│    █ █ █         .22│  █   █
   .10│ █ █ ▒ ▒           .12│  █ █ █ █ █       .22│  █ █ █
   .03│ █ █ ▒ ▒ ▒ .       .04│█ █ █ █ █ █ █ █    .10│█ █ █ █ ▒ ▒
      └─┬─┬─┬─┬─┬──         └─┬─┬─┬─┬─┬─┬───      └─┬─┬─┬─┬─┬─┬─
       0 1 2 3 4 5           0 1 2 3 4 5 6 7         0 1 2 3 4 5 6
       skewed right         symmetric            skewed right, long tail
       (p small)            (p = 0.5)
```

## THE RECOGNITION ROUTINE FOR THESE TWO

```
   "n trials, two outcomes, independent, p constant"     -> BINOMIAL
   "arrivals, calls, defects, rare, per unit time"       -> POISSON
   "use the approximation"                               -> POISSON with λ=np
   "in each of the k intervals"                          -> NEST (Poisson then binomial)
   "mean equals variance given"                          -> POISSON
   "at least one"                                        -> complement, 1 - q^n
```

---
Next: the three continuous named distributions.
