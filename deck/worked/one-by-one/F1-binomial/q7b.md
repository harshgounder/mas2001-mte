# F1 Q7b | Binomial distribution

```
  family      F1 binomial
  source      MTE 2024-25 paper, block C1 part b - THE REAL THING, 4 marks
  drill ref   00-QUESTIONS-ONLY.md -> F1-binomial Q7b
  also in     F1-binomial.md (same content)
```

═══════════════════════════════════════════════════════════════════════════════
PART 1: THE QUESTION
═══════════════════════════════════════════════════════════════════════════════

```
A random variable X follows a binomial distribution with mean 5/3 and P(X=1) = P(X=2).
   Find the variance, P(X >= 1), and P(X <= 1).
```

═══════════════════════════════════════════════════════════════════════════════
PART 2: THE FULL ANSWER, FROM ZERO (every step, nothing assumed)
═══════════════════════════════════════════════════════════════════════════════

STEP 0: DECODE - TWO clues, TWO unknowns (n and p), then three linked asks.

```
   clue 1: "mean = 5/3"      -> np = 5/3
   clue 2: "P(X=1) = P(X=2)" -> an equation in n and p
   asks:   variance = npq, P(at least 1), P(at most 1)
```

EVERY STEP:

```
  STEP 1  write the two equations:
          (1)  np = 5/3
          (2)  P(1) = P(2):
               C(n,1) p q^(n-1) = C(n,2) p^2 q^(n-2)

  STEP 2  simplify (2). Divide both sides by the common factors:
               n p q^(n-1) = [n(n-1)/2] p^2 q^(n-2)
          cancel n p q^(n-2) from both sides:
               q = [(n-1)/2] p
          so   2q = (n-1) p
          with q = 1 - p:  2(1-p) = (n-1)p  ->  2 - 2p = np - p  ->  2 = np + p = p(n+1)
          so   p(n+1) = 2

  STEP 3  combine with (1): np = 5/3 and p(n+1) = 2
          divide:  np / [p(n+1)] = (5/3)/2  ->  n/(n+1) = 5/6  ->  6n = 5n + 5  ->  n = 5
          then p = (5/3)/5 = 1/3

  STEP 4  so the distribution is B(5, 1/3), q = 2/3

  STEP 5  the VARIANCE:
          npq = 5 x (1/3) x (2/3) = 10/9

  STEP 6  P(X >= 1) - use the complement (all-fail is the only case below 1):
          P(X >= 1) = 1 - P(X=0) = 1 - q^5 = 1 - (2/3)^5
                    = 1 - 32/243 = 211/243

  STEP 7  P(X <= 1) - direct sum of two terms:
          P(X <= 1) = P(0) + P(1) = (2/3)^5 + 5 x (1/3) x (2/3)^4
                    = 32/243 + 5 x (1/3) x (16/81)
                    = 32/243 + 80/243 = 112/243
```

ANSWER: variance = 10/9; P(X >= 1) = 211/243; P(X <= 1) = 112/243.
(all four values match the official university solution scheme for this paper)

THE PICTURE (the two-clue structure):

```
   +---------------------+     +--------------------------+
   | clue 1: np = 5/3    |     | clue 2: P(1) = P(2)      |
   +---------------------+     +--------------------------+
              \                     /
               \                   /
                v                 v
           n = 5,  p = 1/3  (B(5,1/3))
                    |
        +-----------+-----------+
        |           |           |
        v           v           v
     var=10/9   P(X>=1)     P(X<=1)
                =211/243    =112/243
```

TRAP:
```
   1. Trying to expand C(n,1) and C(n,2) fully without cancelling. The cancellation of
      n p q^(n-2) is what turns the messy equation into 2q = (n-1)p.
   2. Forgetting q = 1 - p in step 2. Both n and p must fall out together.
   3. In P(X>=1), computing P(1) + P(2) + ... instead of the complement 1 - P(0). The
      complement is one term.
   4. In 211/243 vs 112/243: double-check WHICH tail. "At least 1" is the big probability
      (0.868), "at most 1" is the small one (0.461). Sanity-check the sizes.
```
