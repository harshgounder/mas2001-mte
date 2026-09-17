# F1 Q3b | Binomial distribution

```
  family      F1 binomial
  source      our paper, ETE re-session S4 B2
  drill ref   00-QUESTIONS-ONLY.md -> F1-binomial Q3b
  also in     F1-binomial.md (same content)
```

═══════════════════════════════════════════════════════════════════════════════
PART 1: THE QUESTION
═══════════════════════════════════════════════════════════════════════════════

```
In a certain town, 20% of the population are literate. Assume that 200 investigators
   each take samples of 10 individuals to see whether they are literate. How many
   investigators would you expect to report that 3 people or less are literate in their
   samples?
```

═══════════════════════════════════════════════════════════════════════════════
PART 2: THE FULL ANSWER, FROM ZERO (every step, nothing assumed)
═══════════════════════════════════════════════════════════════════════════════

STEP 0: DECODE - same two-layer structure as Question 3, but with p = 0.2 (not 0.5).

```
   "20% literate"                  -> p = 0.20 per individual
   "samples of 10"                 -> n = 10 per sample
   "3 people or less are literate" -> P(X <= 3)
   "how many of the 200 ... expect" -> COUNT = 200 x P(X <= 3)
```

EVERY STEP:

```
  STEP 1  build the pieces (p=0.2, q=0.8):
          P(0) = C(10,0)(0.2)^0(0.8)^10 = 1 x 1 x 0.10737 = 0.10737
          P(1) = C(10,1)(0.2)^1(0.8)^9  = 10 x 0.2 x 0.13422 = 0.26844
          P(2) = C(10,2)(0.2)^2(0.8)^8  = 45 x 0.04 x 0.16777 = 0.30199
          P(3) = C(10,3)(0.2)^3(0.8)^7  = 120 x 0.008 x 0.20972 = 0.20133

  STEP 2  add the four terms:
          P(X <= 3) = 0.10737 + 0.26843 + 0.30199 + 0.20133 = 0.87913
          (machine-checked: 0.8791)

  STEP 3  the count:
          expected = 200 x 0.87913 = 175.83
```

ANSWER: about 176 investigators (175.83).

TRAP:
```
   1. Using P(X = 3) alone (0.2013). "3 or less" is CUMULATIVE: 0, 1, 2, AND 3.
   2. Forgetting the count layer (200 x). The question asks "how many investigators".
   3. Rounding p or q mid-table. Keep 4 decimals through the four terms, then add.
```

TRAP for QUESTION 3 (the 800-families version):
```
   1. Reporting 0.375 instead of 300. The question asked "how many families", a COUNT.
      This is the single most common way to lose all the marks on this style of question
      even though the hard part (the probability) was done right.
   2. In (iii), "at most 2 girls" is NOT the same as "at most 2 boys" unless you are careful
      about which one you are counting. Here we counted girls directly, which is correct.
   3. Using p = 0.5 for boys while counting girls and confusing the two. Boys and girls both
      have p = 0.5, so it works either way, but say out loud which one X counts.
```
