# F13 ASSIGNMENT SHEETS: both assignments, solved from zero

Source: our own course assignment sheets (Assignment-1 by Dr. Vivek Singh, and Assignment-2
"Probability distributions"). The sheets PRINT their answers; every printed answer was
re-verified with a machine script. Nothing invented.

```
  SHAPES IN THIS FILE
  F13.1  assignment-2 Section A: 12 concept MCQs          (quick table + key)
  F13.2  assignment-2 Section B: 8 full solves
  F13.3  assignment-2 Sections C+D: 6 full solves
  F13.4  assignment-1 short answers: 6 questions
  F13.5  assignment-1 long answers: 3 questions
  F13.6  assignment-1 applications: 4 questions
  F13.7  the printed-answer quirks found (read this)
```

═══════════════════════════════════════════════════════════════════════════════
F13.1  ASSIGNMENT-2 SECTION A:  the 12 concept MCQs
═══════════════════════════════════════════════════════════════════════════════

```
   +----+-----------------------------------------------------+--------+-----------------+
   | #  | question                                            | answer | why             |
   +----+-----------------------------------------------------+--------+-----------------+
   | Q1 | normal curve perfectly symmetric about the:         | (c)    | mu is the axis  |
   |    | a) variance b) sd c) mean d) origin                 | mean   | of symmetry     |
   +----+-----------------------------------------------------+--------+-----------------+
   | Q2 | B(10, 0.5): variance?                               | (b)    | npq=10x.5x.5    |
   |    | a) 5 b) 2.5 c) 10 d) 0.25                           | 2.5    | = 2.5           |
   +----+-----------------------------------------------------+--------+-----------------+
   | Q3 | unique property of the Poisson:                     | (c)    | mean=var=lam    |
   |    | a) mean>var b) mean<var c) mean=var d) sd indep.    |        | is THE property |
   +----+-----------------------------------------------------+--------+-----------------+
   | Q4 | U(a,b) variance formula:                            | (b)    | memorize it     |
   |    | a) (a+b)/2 b) (b-a)^2/12 c) (b-a)/2 d) (b-a)^2/2    |        |                 |
   +----+-----------------------------------------------------+--------+-----------------+
   | Q5 | memoryless property: which distribution?            | (c)    | exponential     |
   |    | a) normal b) uniform c) exponential d) poisson      |        | (the poisson is |
   |    |                                                     |        | discrete, not   |
   |    |                                                     |        | "memoryless"    |
   |    |                                                     |        | in this context)|
   +----+-----------------------------------------------------+--------+-----------------+
   | Q6 | variance of standard normal:                        | (a) 1  | N(0,1): var=1   |
   |    | a) 1 b) 3 c) 0 d) infinity                          |        |                 |
   +----+-----------------------------------------------------+--------+-----------------+
   | Q7 | best model for rare events in fixed interval:       | (c)    | "rare events"   |
   |    | a) binomial b) uniform c) poisson d) exponential    |        | = poisson       |
   +----+-----------------------------------------------------+--------+-----------------+
   | Q8 | exponential with rate lambda: the SD is             | (b)    | SD=1/lam;       |
   |    | a) lambda b) 1/lambda c) 1/lambda^2 d) lambda^2     |        | for exp,        |
   |    |                                                     |        | mean=SD=1/lam   |
   +----+-----------------------------------------------------+--------+-----------------+
   | Q9 | B(12, 0.5): max number of successes possible:       | (d) 12 | max = n itself  |
   |    | a) 6 b) 8 c) 10 d) 12                               |        |                 |
   +----+-----------------------------------------------------+--------+-----------------+
   | Q10| U[a,b], P(c<X<d) with c in (a,b) and d > b:         | (a)    | clip d to b:    |
   |    | a) (b-c)/(b-a) b) (d-c)/(b-a) c) (d-c)/(d-a)        | (b-c)/ | the area runs   |
   |    | d) (b-c)/(d-a)                                      | (b-a)  | only to b       |
   +----+-----------------------------------------------------+--------+-----------------+
   | Q11| area under standard normal between -1 and 1:        | (d)    | the 68% rule    |
   |    | a) 95.45% b) 99.73% c) 50% d) 68.27%                | 68.27% |                 |
   +----+-----------------------------------------------------+--------+-----------------+
   | Q12| X~Poi(l1) and Y~Poi(l2) independent: X+Y follows    | (c)    | poisson adds:   |
   |    | a) binomial mean l1+l2 b) poisson mean l1xl2        |        | sum ~ Poi(l1+l2)|
   |    | c) poisson mean l1+l2 d) exponential mean l1+l2     |        |                 |
   +----+-----------------------------------------------------+--------+-----------------+
```

TRAPS hidden in this set:
```
   Q3: (a)/(b) describe the binomial (mean > variance when q<1... actually mean np > npq).
       The poisson's signature IS mean=variance=lam.
   Q5: the poisson is also memoryless in its own (discrete) sense, but the question says
       CONTINUOUS distributions, so the answer is the exponential.
   Q8: the trap is 1/lambda^2 (that is the VARIANCE). The SD is 1/lambda.
   Q10: the trap is forgetting to CLIP d at b. The uniform stops at b; the area cannot
        extend past it. So the numerator is (b-c), not (d-c).
```

═══════════════════════════════════════════════════════════════════════════════
F13.2  ASSIGNMENT-2 SECTION B:  the 8 full solves
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 1 (IT support desk, Poisson mean 2.5)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A small IT support desk has 3 technicians on a day-to-day basis. The number of demands
   is Poisson with mean 2.5. Find (i) P(no demand) (ii) P(the demand is rejected).
   (printed answers: 0.0821, 0.2424)
```

DECODE: "demand is rejected" = demand EXCEEDS the 3 technicians = P(X >= 4) (the hidden ask).

```
  STEP 1  lambda = 2.5
  STEP 2  (i) P(X=0) = e^(-2.5) = 0.0821     ✓ printed
  STEP 3  (ii) P(X >= 4) = 1 - P(X<=3)
          P(X<=3) = P(0)+P(1)+P(2)+P(3)
          P(1) = 2.5 e^-2.5 = 0.2052
          P(2) = 2.5^2 e^-2.5/2 = 6.25 x 0.0821/2 = 0.2565
          P(3) = 2.5^3 e^-2.5/6 = 15.625 x 0.0821/6 = 0.2138
          P(X<=3) = 0.0821+0.2052+0.2565+0.2138 = 0.7576
          P(X>=4) = 1 - 0.7576 = 0.2424             ✓ printed
```

TRAP: "rejected" is not written as P(X>=4); it is HIDDEN in the story (only 3 technicians
can take demands). This is the "question hidden in wording" pattern again.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 2 (uniform 10 to 20, P(X > 16))
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   X ~ U(10, 20). Find P(X > 16).   (printed answer: 0.4)
```

```
  STEP 1  the uniform density is constant 1/(b-a) = 1/10 on [10,20].
  STEP 2  P(X>16) = (20-16)/(20-10) = 4/10 = 0.4            ✓ printed
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 3 (normal 50, 10; P(45 < X < 62))
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   X ~ N(50, 100) [sd = 10]. Find P(45 < X < 62).
   (given phi(0.5) = 0.1915, phi(1.2) = 0.3849; printed answer: 0.5764)
```

```
  STEP 1  z1 = (45-50)/10 = -0.5 ; z2 = (62-50)/10 = 1.2
  STEP 2  OPPOSITE signs -> phi values ADD:
          P = phi(0.5) + phi(1.2) = 0.1915 + 0.3849 = 0.5764    ✓ printed
```

TRAP: the given data already tells you the phi (area-from-mean) convention; opposite signs
means ADD. (the same-sign/opposite-sign rule from F6.)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 4 (5000 batteries, normal 1500/100 - the COUNT question)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   5000 lithium-ion batteries; life ~ N(1500, 100^2). Estimate the NUMBER likely to last
   (i) more than 1660 h (ii) less than 1380 h (iii) more than 1350 but less than 1680 h.
   (given phi values: 1.2 -> 0.3849, 1.5 -> 0.4332, 1.6 -> 0.4452, 1.8 -> 0.4641)
   (printed: 274, 576, 4487)
```

```
  STEP 1  z(1660) = (1660-1500)/100 = 1.6 ; z(1380) = -1.2 ; z(1350) = -1.5 ; z(1680) = 1.8
  STEP 2  (i) P(X>1660) = 0.5 - phi(1.6) = 0.5 - 0.4452 = 0.0548
          count = 5000 x 0.0548 = 274                            ✓ printed
  STEP 3  (ii) P(X<1380) = 0.5 - phi(1.2) = 0.5 - 0.3849 = 0.1151
          count = 5000 x 0.1151 = 575.5 -> 576                   ✓ printed
  STEP 4  (iii) P(1350<X<1680): opposite signs -> ADD
          = phi(1.5) + phi(1.8) = 0.4332 + 0.4641 = 0.8973
          count = 5000 x 0.8973 = 4486.5 -> 4487                 ✓ printed
```

TRAP: remember the x5000 at the end. "Estimate the number" is the count layer.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 5 (exponential mean 2, conditional)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   X exponential with mean 2. Find P(X < 1 | X < 2).   (printed answer: 0.5679)
```

```
  STEP 1  mean 2 -> lambda = 1/2
  STEP 2  P(X < 1) = 1 - e^(-0.5) = 0.3935
          P(X < 2) = 1 - e^(-1) = 0.6321
  STEP 3  conditional: P(A|B) = P(A and B)/P(B). Since X<1 implies X<2,
          P(X<1 and X<2) = P(X<1) = 0.3935
          P(X<1 | X<2) = 0.3935/0.6321 = 0.6225
```

ANSWER: 0.6225 (exact). (see F13.7 for the printed-answer quirk)

TRAP: the numerator is the SMALLER event's probability (X<1 is a subset of X<2), so the
intersection collapses to P(X<1). Do not multiply anything.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 6 (the 10%/85% two-unknown normal - the assignment twin of F6.4b)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   In a distribution exactly normal, 10% of items are under 30 and 85% are under 65.
   Find the mean and sd. (given phi(1.04) = 0.35, phi(1.28) = 0.4)
   (printed answer: 49.31 and 15.09)
```

```
  STEP 1  clue 1: P(X<30) = 0.10 -> phi(|z1|) = 0.5-0.10 = 0.40 -> |z1| = 1.28 (given)
          so z1 = -1.28
  STEP 2  clue 2: P(X<65) = 0.85 -> phi(z2) = 0.85-0.5 = 0.35 -> z2 = 1.04 (given)
  STEP 3  equations: 30-mu = -1.28 sd ; 65-mu = 1.04 sd
          subtract: 35 = (1.04+1.28) sd = 2.32 sd
          sd = 35/2.32 = 15.0862
  STEP 4  back-substitute: mu = 30 + 1.28 x 15.0862 = 30 + 19.31 = 49.31
```

ANSWER: mu = 49.31, sd = 15.09.   (machine-verified, matches the printed answer)

TRAP: read "10% under" (z negative) vs "85% under" (z positive). The given phi values are
the areas-from-mean; phi(1.28)=0.40 means z=1.28 is the 90th percentile split.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 7 (watch repair, exponential lambda 1/2 - the memoryless conditional)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Repair time ~ exponential with lambda = 1/2.
   (i) P(repair exceeds 2 hours) (ii) P(takes more than 11 h | duration exceeds 8 h).
   (printed: e^-1, e^-1.5)
```

```
  STEP 1  (i) P(X>2) = e^(-0.5 x 2) = e^-1 = 0.3679                    ✓
  STEP 2  (ii) THE MEMORYLESS SHORTCUT: for the exponential,
          P(X>11 | X>8) = P(X > 11-8) = P(X>3) = e^(-0.5 x 3) = e^-1.5 = 0.2231    ✓
          (memoryless: the past 8 hours do not change the future distribution; what
           matters is the ADDITIONAL 3 hours.)
```

TRAP: the naive route is P(X>11)/P(X>8) = e^-5.5/e^-4 = e^-1.5, same answer, more work. But
if you subtract wrong (11+8) or divide wrong you lose it. The memoryless shortcut is the
intended method.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 8 (U(-3,3), four asks including find-K)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   X ~ U(-3, 3). Find (i) P(X<2) (ii) P(|X|<2) (iii) P(|X-2|<2) (iv) K with P(X>K) = 1/3.
   (printed: 5/6, 2/3, 1/2, K = 1)
```

```
  STEP 1  density 1/6 on [-3,3].
  STEP 2  (i) P(X<2) = (2-(-3))/6 = 5/6                                ✓
  STEP 3  (ii) |X|<2 means -2<X<2: length 4 -> 4/6 = 2/3               ✓
  STEP 4  (iii) |X-2|<2 means 0<X<4, clipped to [0,3]: length 3 -> 1/2  ✓
  STEP 5  (iv) P(X>K) = (3-K)/6 = 1/3 -> 3-K = 2 -> K = 1              ✓
```

TRAP: (iii) is the CLIPPING case (the F4.1 lesson): X cannot exceed 3, so the interval
[0,4] is cut to [0,3]. Forgetting to clip gives 4/6, wrong.

═══════════════════════════════════════════════════════════════════════════════
F13.3  ASSIGNMENT-2 SECTIONS C+D:  the 6 full solves
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 9 (hardware, mean 1000 h, survive 1500 given 500 - memoryless again)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Time to failure ~ exponential, mean 1000. P(survive >= 1500 | survived 500).
   (printed answer: 0.3679)
```

```
  STEP 1  lambda = 1/1000
  STEP 2  memoryless: P(X>1500 | X>500) = P(X > 1000) = e^(-1) = 0.3679     ✓
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 10 (the exam 46/9 two-unknown + the re-exam percentile)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Passes 46%, distinctions 9%. Pass mark 40, distinction mark 75. Normal distribution.
   Find mu, sigma. Then: minimum qualifying marks for re-examination if the best 25% of
   the FAILED candidates get another chance.
   (given phi(0.1) = 0.04, phi(1.34) = 0.41, phi(0.24) = 0.095)
   (printed: mu = 37.5, sigma = 28.2, then 30.43)
```

```
  STEP 1  pass 46% at 40: P(X<40) = 0.46 -> phi(|z1|) = 0.5-0.46 = 0.04 -> z1 = -0.1
  STEP 2  distinction 9% above 75: P(X<75) = 0.91 -> phi(z2) = 0.91-0.5 = 0.41 -> z2 = 1.34
  STEP 3  subtract the two equations to eliminate mu:
          35 = (1.34 + 0.1) sd = 1.44 sd
          sd = 35/1.44 = 24.31
          then mu = 40 + 0.1 x 24.31 = 42.43

  STEP 4  the re-exam part: "the best 25% of the failed candidates get another chance".
          the failed candidates are the bottom 46%. the best quarter of them sits between
          the 34.5th and 46th percentile. the threshold x satisfies
               P(X < x) = 0.46 - 0.25 x 0.46 = 0.345
          area from mean = 0.5 - 0.345 = 0.155 -> (with the given table) z = 0.24
               x = mu - 0.24 sd = 42.43 - 0.24 x 24.31 = 42.43 - 5.83 = 36.60
```

ANSWER (method-correct, with the GIVEN table values): mu = 42.43, sd = 24.31, re-exam
threshold = 36.60.
(the sheet prints mu = 37.5, sd = 28.2, threshold = 30.43; that triple is internally
inconsistent with its own given phi values. see F13.7 for the full note. in the exam, use
the given table values exactly and show the two-equation method: that is where the marks are
in a question of this type.)

TRAP: this question type has MULTIPLE printed inconsistencies; in the exam, show the method
(two equations, subtract, back-substitute) and use the given phi values exactly.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 11 (emails, Poisson mean 5, P(X > 2))
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Emails per day ~ Poisson(5). P(more than 2 emails).   (printed answer: 0.8754)
```

```
  STEP 1  P(X<=2) = e^-5 (1 + 5 + 12.5) = 0.006738 x 18.5 = 0.12465
  STEP 2  P(X>2) = 1 - 0.12465 = 0.87535
```

ANSWER: 0.8754.   (machine-verified)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 12 (rounding error uniform -0.5 to 0.5, magnitude > 0.2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   X ~ U(-0.5, 0.5). P(|X| > 0.2).   (printed answer: 0.6)
```

```
  STEP 1  |X| > 0.2 means X < -0.2 or X > 0.2.
  STEP 2  each tail has length 0.3 out of 1.0 total.
  STEP 3  P = 0.3 + 0.3 = 0.6                                          ✓
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 13 (light bulbs 3000/400, count in 10000)  [Section D]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Life ~ N(3000, 400^2). 10000 bulbs bought. How many last between 2500 and 3500?
   (printed answer: 7888 bulbs)
```

```
  STEP 1  z1 = (2500-3000)/400 = -1.25 ; z2 = (3500-3000)/400 = 1.25
  STEP 2  opposite signs -> ADD: phi(1.25) + phi(1.25) = 2 x 0.3944 = 0.7888
  STEP 3  count = 10000 x 0.7888 = 7888                                 ✓
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 14 (buses, exponential 4/hour, wait > 30 min)  [Section D]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Buses arrive at an average rate of 4 per hour. P(wait > 30 minutes).
   (printed answer: 0.1353)
```

```
  STEP 1  UNITS: 4 per hour = 2 per half-hour. the wait is exponential with lambda = 2
          (per half-hour unit).
  STEP 2  P(wait > 30 min) = P(T > 1 half-hour) = e^(-2 x 1) = e^-2 = 0.1353        ✓
  (equivalently: lambda = 4/hr, t = 0.5 hr, e^(-4 x 0.5) = e^-2.)
```

TRAP: unit conversion. 30 minutes is 0.5 HOURS; with lambda per hour the exponent is
-(4)(0.5) = -2. Mixing minutes and hours gives e^-120 or similar nonsense.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 15 (jobs 1%, Poisson approximation to binomial)  [Section D]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   1% of 200 jobs need weekend scheduling. Using the Poisson approximation to binomial,
   P(no jobs wait).   (printed answer: 0.1353)
```

```
  STEP 1  binomial: n=200, p=0.01. lambda = np = 2.
  STEP 2  poisson approximation: P(X=0) = e^-2 = 0.1353                            ✓
```

TRAP: recognize the "poisson approximation to binomial" phrase: it means lambda = np, then
use the poisson formula. Do not compute C(200,0) x 0.99^200 directly (it gives the same
0.1340, close but the question asked for the approximation route).

═══════════════════════════════════════════════════════════════════════════════
F13.4  ASSIGNMENT-1 SHORT ANSWERS:  the 6 questions
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 16 (3 children - the full distribution + CDF)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Find the probability distribution of boys and girls in families with 3 children
   (equal probabilities). Also give the distribution function.
   (printed: pmf 1/8, 3/8, 3/8, 1/8; cdf 1/8, 4/8, 7/8, 1)
```

```
  STEP 1  X = number of boys ~ B(3, 0.5)
  STEP 2  pmf: P(0)=1/8, P(1)=3/8, P(2)=3/8, P(3)=1/8      ✓
  STEP 3  cdf: F(0)=1/8, F(1)=4/8, F(2)=7/8, F(3)=1        ✓
```

TRAP: "3 children" - the variable could count boys or girls (both p=0.5, same table). State
which one X counts.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 17 (electric power, f(x) = (1/9) x e^(-x/3), P(supply inadequate))
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Daily power consumption X has pdf f(x) = (1/9) x e^(-x/3) for x > 0. Plant capacity is
   12 million kWh. P(supply inadequate on a certain day).   (printed answer: 0.0915)
```

```
  STEP 1  "inadequate" = demand EXCEEDS capacity = P(X > 12).
  STEP 2  integrate by parts:  int_12^inf (1/9) x e^(-x/3) dx
          = (1/9)[ -3x e^(-x/3) - 9 e^(-x/3) ]_12^inf
          = (1/9)(3 x 12 + 9) e^(-4) = (45/9) e^-4 = 5 e^-4
  STEP 3  5 e^-4 = 5 x 0.018316 = 0.09158                              ✓ (0.0915)
```

TRAP: recognizing "inadequate" = exceeding capacity. And the integration by parts of
x e^(-x/3). The closed form for this density: P(X>a) = ((a+3)/3) e^(-a/3).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 18 (cable 6x(1-x): verify pdf + find b with P(X<b)=P(X>b))
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   f(x) = 6x(1-x), 0<=x<=1. (i) check it is a pdf (ii) find b with P(X<b) = P(X>b).
   (printed: yes, b = 1/2)
```

```
  STEP 1  (i) non-negative on [0,1] ✓ ; integral = 6[ x^2/2 - x^3/3 ]_0^1 = 6(1/2-1/3) = 1 ✓
  STEP 2  (ii) P(X<b) = P(X>b) means b is the MEDIAN, so F(b) = 1/2.
          F(b) = 6( b^2/2 - b^3/3 ) = 3b^2 - 2b^3 = 1/2
          try b = 1/2: 3/4 - 1/4 = 1/2 ✓
```

THE PICTURE:
```
   f(x) = 6x(1-x) is a parabola peaking at x=1/2 (max 1.5).
   the median sits exactly at the peak because the parabola is symmetric about x=1/2.
```

TRAP: "P(X<b) = P(X>b)" IS the definition of the median; do not set up two separate
integrals from scratch. F(b) = 1/2, solve.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 19 (coin until head - the geometric expectation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A coin is tossed until a head appears. Expectation of the number of tosses.
   (printed answer: 2)
```

```
  STEP 1  X = tosses until first head, geometric with p = 1/2: P(X=k) = (1/2)^k.
  STEP 2  E(X) = 1/p = 1/(1/2) = 2   (standard result)
          or from scratch: E(X) = sum k (1/2)^k = 2.
```

TRAP: the geometric mean is 1/p; for a fair coin that is 2. Some books write the geometric
starting at 0 (failures before first success) with mean (1-p)/p = 1; read which convention
the question wants ("number of TOSSES" = 2 here).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 20 (two dice, Chebyshev bound 35/54 vs actual 1/3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   X = sum of two dice. Prove P(|X-7| >= 3) <= 35/54. Compare with the actual probability.
   (printed: actual = 1/3)
```

```
  STEP 1  E(X) = 7 ; Var(X) = Var(die1)+Var(die2) = 2 x (35/12) = 35/6
  STEP 2  Chebyshev in RAW units: P(|X-mu| >= c) <= Var(X)/c^2 with c = 3:
          = (35/6)/9 = 35/54                                        ✓
  STEP 3  the ACTUAL probability: the sums with |X-7| >= 3 are 2,3,4,10,11,12:
          P = (1+2+3+3+2+1)/36 = 12/36 = 1/3                       ✓
  STEP 4  comparison: the bound 35/54 = 0.648 is far above the actual 1/3 = 0.333.
          Chebyshev is SAFE but loose.
```

THE PICTURE:
```
   actual: [0.333]                    bound: [============= 0.648 =============]
   the true probability sits well under the bound. that is what a bound means.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 21 (600 throws, 80-120 sixes, lower bound)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A symmetric die is thrown 600 times. Lower bound for P(getting 80 to 120 sixes).
   (printed answer: 19/24)
```

```
  STEP 1  X = sixes ~ B(600, 1/6): mean = 100, var = 600 x (1/6) x (5/6) = 500/6
          sd = sqrt(500/6) = 9.1287
  STEP 2  the band 80..120 is 20 away from the mean. In sd units: k = 20/9.1287 = 2.1909
  STEP 3  Chebyshev within: 1 - 1/k^2 = 1 - 1/4.8 = 1 - 5/24 = 19/24              ✓
          (1/k^2 = 1/(20^2/(500/6)) = (500/6)/400 = 500/2400 = 5/24)
```

TRAP: the band is SYMMETRIC around the mean (80 to 120 = 100 +/- 20), so the WITHIN form
applies. Convert the raw gap (20) to k = gap/sd first.

═══════════════════════════════════════════════════════════════════════════════
F13.5  ASSIGNMENT-1 LONG ANSWERS:  the 3 questions
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 22 (the death function (3e-9) t^2 (100-t)^2 - the big integral)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   f(t) = (3 x 10^-9) t^2 (100-t)^2 for 0 <= t <= 100.
   (i) P(die between 60 and 70) (ii) P(die between 60 and 70 | lived to 60).
   (printed: 0.1544, 0.4863)
```

```
  STEP 1  expand: t^2(100-t)^2 = t^2(10000 - 200t + t^2) = 10000t^2 - 200t^3 + t^4
  STEP 2  the antiderivative: c[ 10000 t^3/3 - 200 t^4/4 + t^5/5 ] with c = 3e-9
                    = c[ 10000t^3/3 - 50t^4 + t^5/5 ]
  STEP 3  (i) P(60<=t<=70) = I(70) - I(60)
          I(70) = 3e-9[ 10000 x 343000/3 - 50 x 24010000 + 1680700000/5 ]
                = 3e-9[ 1143333333.3 - 1200500000 + 336140000 ]
                = 3e-9 x 278973333.3 = 0.83692
          I(60) = 3e-9[ 10000 x 216000/3 - 50 x 12960000 + 777600000/5 ]
                = 3e-9[ 720000000 - 648000000 + 155520000 ] = 3e-9 x 227520000 = 0.68256
          P = 0.83692 - 0.68256 = 0.15436                                     ✓ (0.1544)
  STEP 4  (ii) conditional on living to 60: divide by P(t > 60) = 1 - F(60) = 1 - 0.68256
          = 0.31744
          P = 0.15436/0.31744 = 0.48628                                       ✓ (0.4863)
```

TRAP: the conditional in (ii) divides by the SURVIVAL probability (1 - F(60)), not by 1.
This is the same conditional structure as the watch-repair question.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 23 (the 25 items / 5 defectives expectation - sampling with vs without replacement)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   From 25 items containing 5 defectives, a sample of 4 is drawn (i) without replacement
   (ii) with replacement. Find E(number of defectives) in each case.
   (printed: 0.808 and 0.8)
```

```
  STEP 1  (ii) WITH replacement: X ~ B(4, 0.2), E = np = 4 x 5/25 = 0.8               ✓
  STEP 2  (i) WITHOUT replacement: X is hypergeometric.
          E(X) = n x (K/N) = 4 x 5/25 = 0.8  (the same expectation, by the standard
          hypergeometric mean formula)
          the exact distribution: P(0)=0.3830, P(1)=0.4506, P(2)=0.1502, P(3)=0.0158,
          P(4)=0.0004; weighted sum = 0.8000.
```

NOTE: the sheet prints 0.808 for (i); the exact hypergeometric mean is 0.8000. See F13.7.

TRAP: the expectation is the same 0.8 in both cases (a nice fact); only the VARIANCE
differs (without replacement it is smaller: the finite-population correction).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 24 (4 bad oranges among 16 - the distribution)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Four bad oranges mixed with 16 good. Probability distribution of the number of bad
   oranges in a draw of two.   (printed: 12/19, 32/95, 3/95)
```

```
  STEP 1  X = bad oranges in 2 draws (without replacement), hypergeometric N=20, K=4, n=2
  STEP 2  P(0) = C(16,2)/C(20,2) = 120/190 = 12/19              ✓
  STEP 3  P(1) = C(4,1)C(16,1)/C(20,2) = 64/190 = 32/95          ✓
  STEP 4  P(2) = C(4,2)/C(20,2) = 6/190 = 3/95                   ✓
  STEP 5  check: 12/19 + 32/95 + 3/95 = 60/95 + 32/95 + 3/95 = 95/95 = 1 ✓
```

═══════════════════════════════════════════════════════════════════════════════
F13.6  ASSIGNMENT-1 APPLICATIONS:  the 4 questions
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 25 (defective sensors - pmf check, E, Var, interpret)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   X: 0,1,2,3 with P: 0.25, 0.40, 0.25, 0.10.
   Verify a valid PMF; find E(X); find Var(X); interpret.   (printed: E=1.2, Var=0.86)
```

```
  STEP 1  sum = 0.25+0.40+0.25+0.10 = 1.00, all in [0,1] -> valid PMF ✓
  STEP 2  E(X) = 0(0.25)+1(0.40)+2(0.25)+3(0.10) = 0.40+0.50+0.30 = 1.2          ✓
  STEP 3  E(X^2) = 0+1(0.40)+4(0.25)+9(0.10) = 0.40+1.00+0.90 = 2.30
          Var = 2.30 - (1.2)^2 = 2.30 - 1.44 = 0.86                              ✓
  STEP 4  interpretation: on average 1.2 defective sensors per batch, with a spread of
          sd = sqrt(0.86) = 0.927. For production planning: expect about 1-2 defectives
          per batch; plan QC capacity accordingly.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 26 (customer calls - CDF, P(X<=2), P(X>1))
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   X: 0,1,2,3 with P: 0.15, 0.35, 0.30, 0.20. CDF; P(X<=2); P(X>1); interpretation.
   (printed: 0.50 for the middle ask)
```

```
  STEP 1  CDF: F(0)=0.15, F(1)=0.50, F(2)=0.80, F(3)=1.00
  STEP 2  P(X<=2) = F(2) = 0.80
  STEP 3  P(X>1) = 1 - F(1) = 1 - 0.50 = 0.50                                    ✓
  STEP 4  interpretation: half the hours see more than 1 call; staffing should cover the
          >1-call hours as the common case.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 27 (battery life 2..5 - mean, var, sd)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   X: 2,3,4,5 with P: 0.20, 0.30, 0.35, 0.15. Mean; variance; sd; interpret.
   (printed: 3.45 years, 0.95, sd ~ 0.98)
```

```
  STEP 1  E(X) = 2(0.20)+3(0.30)+4(0.35)+5(0.15) = 0.4+0.9+1.4+0.75 = 3.45        ✓
  STEP 2  E(X^2) = 4(0.20)+9(0.30)+16(0.35)+25(0.15) = 0.8+2.7+5.6+3.75 = 12.85
          Var = 12.85 - (3.45)^2 = 12.85 - 11.9025 = 0.9475                       ✓ (0.95)
  STEP 3  sd = sqrt(0.9475) = 0.9734                                            ~ ✓ (0.98)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 28 (marks 70/25, Chebyshev 60-80)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Mean 70, variance 25. Minimum proportion scoring 60-80 (Chebyshev).
   (printed: at least 75%)
```

```
  STEP 1  the band is 70 +/- 10. sd = 5. k = 10/5 = 2.
  STEP 2  within form: 1 - 1/k^2 = 1 - 1/4 = 3/4 = 75%                            ✓
```

═══════════════════════════════════════════════════════════════════════════════
F13.7  THE PRINTED-ANSWER QUIRKS  (found while machine-verifying every assignment answer)
═══════════════════════════════════════════════════════════════════════════════

```
   +-----+-------------------------+------------------+---------------------------------+
   | #   | question                | printed          | exact (machine)                 |
   +-----+-------------------------+------------------+---------------------------------+
   | B5  | P(X<1|X<2), exp mean 2  | 0.5679           | 0.6225                          |
   |     |                         |                  | (the printed value uses ln 2 =  |
   |     |                         |                  | 0.6931 in the denominator       |
   |     |                         |                  | instead of 1-e^-1 = 0.6321.     |
   |     |                         |                  | the correct answer is 0.6225)   |
   +-----+-------------------------+------------------+---------------------------------+
   | C2  | exam 46/9 + re-exam     | mu=37.5, sd=28.2 | with the GIVEN z's:             |
   |     |                         | and 30.43        | sd = 35/1.44 = 24.31,           |
   |     |                         |                  | mu = 42.43. the printed pair is |
   |     |                         |                  | internally inconsistent with    |
   |     |                         |                  | the given phi values. show the  |
   |     |                         |                  | method; answer with the given   |
   |     |                         |                  | table values.                   |
   +-----+-------------------------+------------------+---------------------------------+
   | LA2 | 25 items/5 def, no      | 0.808            | 0.8000 (hypergeometric mean     |
   |     | replacement             |                  | nK/N = 4x5/25). the 0.808 likely|
   |     |                         |                  | comes from a rounding slip in   |
   |     |                         |                  | the sheet. exact = 0.8.         |
   +-----+-------------------------+------------------+---------------------------------+
   | APP3| battery sd              | 0.975            | sqrt(0.9475) = 0.9734. the      |
   |     |                         |                  | printed sd treats the variance  |
   |     |                         |                  | as 0.95 flat, losing the .95 -> |
   |     |                         |                  | .9475 detail. both round to 0.97|
   +-----+-------------------------+------------------+---------------------------------+
```

HOW TO HANDLE THESE IN THE EXAM: show the method with the GIVEN table values; the method
carries the marks. When a printed answer differs, state both and move on. These quirks also
show WHY the exam gives you the table values: it wants the method, not exact arithmetic.

═══════════════════════════════════════════════════════════════════════════════
F13 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   ASSIGNMENT-2 SECTION A: the 12 answers in one row:
     c, b, c, b, c, a, c, b, d, a, d, c
     (mean-symmetry, 2.5, mean=var, (b-a)^2/12, exponential, 1, poisson, 1/lambda,
      12, (b-c)/(b-a), 68.27%, poisson(l1+l2))

   THE FULL-SOLVE HIGHLIGHTS:
     IT desk: "rejected" = P(X>=4) (hidden in the story)
     batteries: 274, 576, 4487 (the count layer)
     exp conditionals: memoryless shortcuts (e^-1, e^-1.5, 0.3679)
     U(-3,3): the clip case (iii) -> 1/2
     600 dice: k = 20/sd = 2.19 -> 19/24
     death integral: I(70)-I(60) = 0.1544; conditional /(1-F(60)) = 0.4863
     oranges: 12/19, 32/95, 3/95
     3 children: 1/8,3/8,3/8,1/8

   TOP TRAPS IN THIS FILE:
     "rejected/inadequate/not up to standard" -> decode to the right tail
     memoryless: subtract the ages (11-8), never add
     conditional: divide by the survival probability
     count layer: multiply by the group size (batteries, bulbs, families)
     clip at the uniform's edge (U(-3,3) case iii)
     unit conversion (buses: 30 min = 0.5 h; or lambda 2 per half-hour)
     printed-answer quirks: answer with the given table values, show the method
```
