# F6 Q4b | Normal distribution

```
  family      F6 normal
  source      our assignment, 2025-26 assignment sheet #2 Q27
  drill ref   00-QUESTIONS-ONLY.md -> F6-normal Q4b
  also in     F6-normal.md (same content)
```

═══════════════════════════════════════════════════════════════════════════════
PART 1: THE QUESTION
═══════════════════════════════════════════════════════════════════════════════

```
In a distribution exactly normal, 7% of the items are under 35 and 89% are under 63.
   What are the mean and standard deviation of the distribution?
   (the assignment sheet prints the answer: 50.3 and 10.33)
```

═══════════════════════════════════════════════════════════════════════════════
PART 2: THE FULL ANSWER, FROM ZERO (every step, nothing assumed)
═══════════════════════════════════════════════════════════════════════════════

STEP 0: DECODE - same shape as Question 4, different numbers. This variant is CLEANER (no
typo) and is the one to drill first.

```
   clue 1: P(X < 35) = 0.07    -> 35 is BELOW the mean, z1 negative
   clue 2: P(X < 63) = 0.89    -> 63 is ABOVE the mean (0.89 > 0.5), z2 positive
```

STEP 1: TURN EACH CLUE INTO A z-VALUE (area-from-mean convention)

```
   CLUE 1: P(X<35) = 0.5 - phi(|z1|) = 0.07
           phi(|z1|) = 0.5 - 0.07 = 0.43
           the z whose phi is 0.43:  |z1| = 1.4758   ->  z1 = -1.4758
           (table check: phi(1.47)~0.4292, phi(1.48)~0.4306, so 1.4758 fits)

   CLUE 2: P(X<63) = 0.5 + phi(z2) = 0.89
           phi(z2) = 0.89 - 0.5 = 0.39
           the z whose phi is 0.39:  z2 = 1.2265
           (table check: phi(1.22)~0.3888, phi(1.23)~0.3907)
```

STEP 2: THE TWO EQUATIONS

```
   z1 = (35 - mu)/sigma = -1.4758
   z2 = (63 - mu)/sigma =  1.2265
```

STEP 3: SUBTRACT (kills mu)

```
   (63 - mu) - (35 - mu) = (1.2265 + 1.4758) sigma
   28 = 2.7023 sigma
   sigma = 28 / 2.7023 = 10.3615
```

STEP 4: BACK-SUBSTITUTE

```
   from clue 2:  63 - mu = 1.2265 x 10.3615 = 12.7086
   mu = 63 - 12.7086 = 50.2914
```

ANSWER: mean 50.29, sd 10.36 (the assignment's printed 50.3 / 10.33 matches, small rounding).
(machine-verified: z1 = -1.4758, z2 = 1.2265, sigma = 10.3615, mu = 50.2914)

THE SELF-CHECK (always do this on two-unknown questions):
```
   check P(X<35) with the found values: z = (35-50.2914)/10.3615 = -1.4758
        -> 0.5 - phi(1.4758) = 0.5 - 0.43 = 0.07 ✓ (matches clue 1)
   check P(X<63): z = (63-50.2914)/10.3615 = 1.2265 -> 0.5 + 0.39 = 0.89 ✓
```

TRAP: identical to Question 4. The extra trap here: "89% are under 63" is a LOWER
cumulative ask (not an upper tail), so its phi is 0.89 - 0.5 = 0.39 and z is POSITIVE.
Read "under" vs "over" with full attention; that single word decides the sign.
