# F1 BINOMIAL: every shape, every question, solved from zero

Source of every question here: our own material (the ppt3 deck pages, and the ETE papers
E24S3, E25S3, E25SUM). Nothing invented. Every number was computed and checked on the machine.

```
  SHAPES IN THIS FILE
  F1.1  point        P(X = exactly k)              3 questions
  F1.2  tail         P(X >= k) / at least          2 questions
  F1.3  moments      E(X), Var(X)                  2 questions
  F1.4  recovery     find p, or the whole pmf      2 questions
  F1.5  formula MCQ  name the pmf                  1 question
```

═══════════════════════════════════════════════════════════════════════════════
BEFORE ANY QUESTION: what "binomial" even means
═══════════════════════════════════════════════════════════════════════════════

A binomial situation has exactly FOUR ingredients. If all four are present, it is binomial.

```
   1. a FIXED number of tries            n       (12 pens, 6 bombs, 10 throws)
   2. each try has TWO outcomes          success or failure  (defective or fine)
   3. the success chance NEVER changes   p       (always 10 percent, every pen)
   4. the tries do NOT affect each other          (pen 3 being bad tells you nothing
                                                   about pen 4)
```

THE PICTURE:

```
   one try:            success (p)  or  failure (q = 1 - p)
                        |
                        |  repeat this n times, independently
                        v
   n tries:  [try][try][try][try][try][try] ... (n boxes)
             each box independently gets a tick (success) or a cross (failure)

   X = the TOTAL number of ticks among all the boxes.
   P(X = k) asks: how often do exactly k ticks appear?
```

THE FORMULA, and where each piece comes from:

```
                     P(X = k)  =  C(n,k)  x   p^k   x   q^(n-k)
                                  ~~~~~~     ~~~~~     ~~~~~~~~
                                  |          |         |
       how many arrangements      |          |         every arrangement has
       of k ticks and n-k         |          |         this exact chance:
       crosses exist              |          |         k ticks = p x p x ...(k times)
                                  |          |         n-k crosses = q x ...(n-k times)
                                  |
              because the ORDER of the ticks does not matter;
              C(n,k) counts the distinct patterns
```

C(n,k) READ OUT LOUD (this is the part most people skip, do not skip it):

```
   C(n,k) = n! / ( k! x (n-k)! )

   the "!" means factorial:  4! = 4 x 3 x 2 x 1 = 24
                             and by definition 0! = 1 and 1! = 1

   in words: "how many ways can I choose k positions out of n positions,
              when the order of my choosing does not matter"

   example C(12,2):
       12! / (2! x 10!)
     = (12 x 11 x 10 x 9 x ... x 1) / ( (2 x 1) x (10 x 9 x ... x 1) )
     the 10 x 9 x ... x 1 cancels top and bottom, leaving
     = (12 x 11) / (2 x 1)
     = 132 / 2
     = 66
```

═══════════════════════════════════════════════════════════════════════════════
F1.1  POINT:  P(X = exactly k)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 1 (our deck ppt3 p013, also asked verbatim in ETE 2025-26 S3 B2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   10% of pens manufactured by a company are defective. A box contains 12 pens.
   Find the probability that the box contains:
   (i) Exactly 2 defective pens   (ii) At least 2 defective pens   (iii) No defective pen
```

STEP 0: DECODE THE WORDS BEFORE TOUCHING NUMBERS

```
   "10% of pens are defective"     -> the success chance p = 10/100 = 0.10
                                       (here "success" means "defective" even though
                                        a defective pen is a bad thing. the word
                                        "success" in maths just means "the thing
                                        we are counting".)
   "a box contains 12 pens"        -> n = 12, a fixed number of tries
   "defective"                     -> the outcome we count
   "exactly 2"                     -> k = 2, no more and no less
```

WHY BINOMIAL: check the 4 ingredients.

```
   1. fixed tries?      YES, 12 pens
   2. two outcomes?     YES, defective or not
   3. p constant?       YES, every pen has the same 10 percent
   4. independent?      YES, one pen's defect tells nothing about the next
   => binomial with n = 12, p = 0.10, q = 0.90
```

═══════════════ PART (i): exactly 2 defective pens ═══════════════

IN PLAIN: exactly two of the twelve are bad. Not one, not three.

THE FLOWCHART:

```
              START: want P(X = 2)
                        |
                        v
        +-------------------------------+
        | use the binomial formula      |
        | P(X=k) = C(n,k) p^k q^(n-k)   |
        +-------------------------------+
                        |
                        v
        +-------------------------------+
        | n=12, k=2, p=0.10, q=0.90     |
        +-------------------------------+
                        |
        +---------------+---------------+
        |                               |
        v                               v
   count the ways                  chance of ONE way
   C(12,2) = 66                    (0.1)^2 x (0.9)^10
        |                               |
        +---------------+---------------+
                        |
                        v
              multiply: 66 x 0.01 x 0.3487
                        |
                        v
                   ANSWER 0.2301
```

THE LONG VERSION, EVERY STEP:

```
  STEP 1  Write the formula with the numbers placed in it:
          P(X = 2) = C(12,2) x (0.10)^2 x (0.90)^(12-2)
                   = C(12,2) x (0.10)^2 x (0.90)^10

  STEP 2  Work out C(12,2), the number of ways to choose which 2 of the 12 pens are bad:
          C(12,2) = (12 x 11) / (2 x 1) = 132 / 2 = 66
          (why divide by 2? because "pen 3 then pen 7" and "pen 7 then pen 3" are the
           same pair. dividing removes the double-counting.)

  STEP 3  Work out the chance of ONE specific arrangement, say pens 1 and 2 bad and the
          other ten fine:
          (0.10) x (0.10) x (0.90 x 0.90 x 0.90 x 0.90 x 0.90 x 0.90 x 0.90 x 0.90 x 0.90 x 0.90)
          = (0.10)^2 x (0.90)^10
          = 0.01 x 0.3487
          = 0.003487
          (where did 0.3487 come from? that is 0.90 multiplied by itself 10 times.
           on a calculator: 0.9^10. write it as a decimal, 0.3487.)

  STEP 4  Multiply the count by the chance of one:
          66 x 0.003487 = 0.2301
```

ANSWER: P(X = 2) = 0.2301, about 23 percent. Roughly one box in four has exactly two
defective pens.

═══════════════ PART (ii): at least 2 defective pens ═══════════════

IN PLAIN: two or more bad. Could be 2, could be 3, ... could be all 12.

THE WORD "AT LEAST" IS A TRAP-SIGNAL:

```
   "at least 2"     means 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, or 12

   you COULD add eleven terms:
     P(2) + P(3) + P(4) + ... + P(12)        <- eleven calculations, eleven chances to slip

   or you can be clever and add only TWO terms, then subtract from 1:

     +--------------------------------------------------------------+
     |  THE COMPLEMENT RULE                                          |
     |                                                               |
     |  everything that can happen adds to 1                         |
     |  so:   P(at least 2) = 1 - P(everything that is NOT at least 2)|
     |                      = 1 - P(0 or 1)                          |
     |                      = 1 - P(0) - P(1)                        |
     +--------------------------------------------------------------+
```

THE PICTURE:

```
   all the boxes (probabilities must total 1):

   [P0 ][P1 ][P2 ][P3 ][P4 ][P5 ][P6 ][P7 ][P8 ][P9 ][P10][P11][P12]
    \______/     \___________________________________________________/
     the part      the part we WANT ("at least 2")
     NOT wanted
     ("0 or 1")

   instead of adding all eleven wanted boxes,
   take the whole (1) and remove the two unwanted boxes.
```

EVERY STEP:

```
  STEP 1  Compute P(X = 0):
          P(0) = C(12,0) x (0.10)^0 x (0.90)^12
          C(12,0) = 1        (there is exactly one way to choose nothing)
          (0.10)^0 = 1       (anything to the power zero is 1)
          (0.90)^12 = 0.2824
          so P(0) = 1 x 1 x 0.2824 = 0.2824

  STEP 2  Compute P(X = 1):
          P(1) = C(12,1) x (0.10)^1 x (0.90)^11
          C(12,1) = 12       (any one of the 12 pens could be the bad one)
          (0.10)^1 = 0.10
          (0.90)^11 = 0.3138
          so P(1) = 12 x 0.10 x 0.3138 = 0.3766

  STEP 3  Add the two unwanted ones:
          P(0) + P(1) = 0.2824 + 0.3766 = 0.6590

  STEP 4  Subtract from 1:
          P(at least 2) = 1 - 0.6590 = 0.3410
```

ANSWER: P(X >= 2) = 0.3410, about 34 percent.

SELF CHECK (always do this when you have a moment):

```
   P(0) + P(1) + P(at least 2) = 0.2824 + 0.3766 + 0.3410 = 1.0000
   and everything must total 1. the check passes.
```

═══════════════ PART (iii): no defective pen ═══════════════

IN PLAIN: zero bad pens. All twelve fine.

THE PICTURE:

```
   every pen must be FINE:
   fine x fine x fine x fine x fine x fine x fine x fine x fine x fine x fine x fine
    0.9    0.9   0.9    0.9    0.9    0.9    0.9    0.9    0.9    0.9    0.9    0.9
   = 0.9 multiplied by itself 12 times
```

EVERY STEP:

```
  STEP 1  Formula with numbers: P(X=0) = C(12,0) x (0.10)^0 x (0.90)^12
  STEP 2  C(12,0) = 1
  STEP 3  (0.10)^0 = 1        <- a very common slip is to write 0 here. it is 1, not 0.
  STEP 4  (0.90)^12 = 0.2824
  STEP 5  multiply: 1 x 1 x 0.2824 = 0.2824
```

ANSWER: P(X = 0) = 0.2824, about 28 percent.

TRAP for the whole question:
```
   1. For "at least 2", summing 11 terms instead of using the complement (slow + error-prone).
   2. Writing (0.10)^0 = 0 instead of 1.
   3. Forgetting that "at least 2" INCLUDES 2. "at least" means >=. "more than 2" would be
      strictly > 2 and would start at 3.
   4. In (ii), accidentally subtracting only P(0): 1 - 0.2824 = 0.7176 would be
      "at least 1", a different question.
```

MUTATIONS of this question, and what changes:
```
   IF "more than 2"        THEN P = 1 - P(0) - P(1) - P(2) = 1 - 0.2824 - 0.3766 - 0.2301
                                = 0.1109. (one more term than "at least 2")
   IF "at most 2"          THEN P = P(0) + P(1) + P(2) = 0.8891. (no complement needed,
                                just add the three small terms)
   IF "at least 1"         THEN P = 1 - P(0) = 0.7176. (the whole "none" complement)
   IF p becomes 20%        THEN p=0.20, q=0.80, and every number changes; method identical.
   IF the box has 15 pens  THEN C(15,k) and q^(15-k); method identical.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 2 (our paper, ETE 2024-25 S3 B3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   The probability that a bomb dropped from a plane will strike the target is 1/5.
   If six bombs are dropped, find the probability that at least two will strike the
   target and exactly two will strike the target.
```

STEP 0: DECODE

```
   "probability ... will strike the target is 1/5"   -> p = 1/5 = 0.20
   "six bombs are dropped"                           -> n = 6, fixed tries
   "strike / not strike"                             -> two outcomes
   "at least two"                                    -> k >= 2
   "exactly two"                                     -> k = 2
```

WHY BINOMIAL: 4 ingredients
```
   fixed tries (6) yes | two outcomes yes | p constant (every bomb 1/5) yes | independent yes
```

THE PICTURE (6 bombs, each 1-in-5 to hit):

```
   bomb:     1     2     3     4     5     6
            hit?  hit?  hit?  hit?  hit?  hit?
            1/5   1/5   1/5   1/5   1/5   1/5    each independently

   X = how many of the six hit.

   "exactly two"  -> X = 2
   "at least two" -> X = 2, 3, 4, 5, or 6
```

═══════════════ PART A: exactly two ═══════════════

```
  STEP 1  Formula: P(X=2) = C(6,2) x (0.2)^2 x (0.8)^4
  STEP 2  C(6,2) = (6 x 5)/(2 x 1) = 30/2 = 15
  STEP 3  (0.2)^2 = 0.04
  STEP 4  (0.8)^4 = 0.8 x 0.8 x 0.8 x 0.8 = 0.4096
  STEP 5  multiply: 15 x 0.04 x 0.4096
          first 15 x 0.04 = 0.6
          then 0.6 x 0.4096 = 0.24576
          rounding to 4 decimals: 0.2458
```

ANSWER: P(exactly 2) = 0.2458, about 25 percent.

═══════════════ PART B: at least two ═══════════════

```
  THE COMPLEMENT AGAIN:
  "at least 2" = 1 - P(0) - P(1)

  STEP 1  P(0) = C(6,0) x (0.2)^0 x (0.8)^6
               = 1 x 1 x 0.262144 = 0.262144  -> display 0.2621
  STEP 2  P(1) = C(6,1) x (0.2)^1 x (0.8)^5
               = 6 x 0.2 x 0.32768
               = 1.2 x 0.32768 = 0.393216  -> display 0.3932
  STEP 3  keep the unrounded values for the subtraction:
          P(0) + P(1) = 0.262144 + 0.393216 = 0.655360
  STEP 4  subtract from 1: 1 - 0.655360 = 0.344640
          rounding only now gives 0.3446.
          If the displayed 0.2621 and 0.3932 are subtracted instead, the display becomes
          0.3447. That is a rounding artefact, not the final four-decimal answer.
```

ANSWER: P(at least 2) = 0.3446 (about 34 percent).

THE FULL DISTRIBUTION, so you can see the shape of it (a useful habit):

```
   k      P(X=k)     bar (each dot is roughly 1 percent)
   0      0.2621     ##########################
   1      0.3932     ########################################
   2      0.2458     #########################
   3      0.0819     ########
   4      0.0154     ##
   5      0.0015     .
   6      0.0001     .
                    total = 1.0000 (good)

   notice: the most likely single count is 1, not 2. "at least 2" is not "the likely case",
   it is a tail. always picture where you are on this bar chart before believing a number.
```

TRAP:
```
   1. For "at least two", writing "1 - P(0)" only. That answers "at least one".
   2. Using 6 x 5 = 30 for C(6,2) without dividing by 2.
   3. Mixing p and q: writing (0.8)^2 x (0.2)^4 instead of (0.2)^2 x (0.8)^4. The failed
      bombs get q, and there are 4 of them; the hits get p, and there are 2.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 3 (our paper, ETE 2025 summer Q13) - the COUNT variant
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Out of 800 families with 4 children each, how many families would be expected to have
   (i) 2 boys and 2 girls  (ii) at least one boy  (iii) at most 2 girls.
   Use Binomial distribution. Assume equal probabilities for boys and girls.
```

STEP 0: DECODE. THIS QUESTION HIDES ITS REAL ASK IN THE WORD "HOW MANY".

```
   "800 families with 4 children each"   -> there are 800 independent groups, each group = 4 tries
   "equal probabilities for boys and girls" -> p = 1/2 = 0.50
   "how many families would be expected"  -> THIS IS THE KEY. it does not ask for a probability.
                                             it asks for a COUNT = 800 x probability.
```

THE TWO-LAYER PICTURE (this is the "question hidden in the wording" pattern):

```
   LAYER 1: for ONE family of 4 children, what is the probability of the event?
            -> binomial with n=4, p=0.5

   LAYER 2: that probability applies to each of the 800 families independently,
            so expected count = 800 x (probability from layer 1)

   +--------------------+          +---------------------------+
   | ONE family:        |          | 800 families:             |
   | B(4, 0.5)          |  ----->  | expected = 800 x P(event) |
   | find P(event)      |          | report the COUNT          |
   +--------------------+          +---------------------------+
```

VERB DECODER for this whole family of wordings:

```
   "find the probability"          -> report a number between 0 and 1
   "how many ... would be expected" -> report a COUNT: multiply the probability by the
                                       number of groups (here 800)
   "the number of ... expected"     -> COUNT
   "find the chance"                -> probability
```

═══════════════ PART (i): 2 boys and 2 girls ═══════════════

```
  "2 boys and 2 girls" in 4 children -> exactly 2 boys (then the other 2 are girls)
  so we want P(exactly 2 boys) with n=4, p=0.5

  STEP 1  C(4,2) = (4 x 3)/(2 x 1) = 12/2 = 6
  STEP 2  (0.5)^2 x (0.5)^2 = 0.25 x 0.25 = 0.0625
  STEP 3  P = 6 x 0.0625 = 0.375
  STEP 4  expected count = 800 x 0.375 = 300
```

ANSWER: 300 families.

═══════════════ PART (ii): at least one boy ═══════════════

```
  "at least one boy" -> complement: 1 - P(no boys) = 1 - P(all 4 girls)
  STEP 1  P(all 4 girls) = C(4,0) x (0.5)^0 x (0.5)^4 = 1 x 1 x 0.0625 = 0.0625
  STEP 2  P(at least one boy) = 1 - 0.0625 = 0.9375
  STEP 3  expected count = 800 x 0.9375 = 750
```

ANSWER: 750 families.

═══════════════ PART (iii): at most 2 girls ═══════════════

```
  "at most 2 girls" -> 0 girls, 1 girl, or 2 girls.
  counting girls: P(girl) = 0.5, n = 4
  so we need P(X<=2) where X = number of girls

  STEP 1  P(0 girls) = all boys = (0.5)^4 = 0.0625
  STEP 2  P(1 girl)  = C(4,1) x (0.5)^1 x (0.5)^3 = 4 x 0.0625 = 0.25
  STEP 3  P(2 girls) = C(4,2) x 0.0625 = 6 x 0.0625 = 0.375
  STEP 4  add: 0.0625 + 0.25 + 0.375 = 0.6875
  STEP 5  expected count = 800 x 0.6875 = 550
```

ANSWER: 550 families.

SELF CHECK:
```
   0.0625 + 0.25 + 0.375 = 0.6875, and the complement (3 or 4 girls) is 0.25 + 0.0625 = 0.3125.
   0.6875 + 0.3125 = 1.0000. good.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 3b (our paper, ETE re-session S4 B2) - the literate variant (p = 0.2, n = 10)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   In a certain town, 20% of the population are literate. Assume that 200 investigators
   each take samples of 10 individuals to see whether they are literate. How many
   investigators would you expect to report that 3 people or less are literate in their
   samples?
```

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

═══════════════════════════════════════════════════════════════════════════════
F1.2  TAIL:  P(X >= k) - covered above in Q1(ii) and Q2, plus one more form
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 4 (our paper, ETE 2025 summer Q17) - the "at least" with a Poisson wrapper
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A manufacturer, who produces medicine bottles, finds that 0.1% of the bottles are
   defective. The bottles are packed in boxes containing 500 bottles. A drug manufacturer
   buys 100 boxes from the producer of bottles. Using Poisson distribution, find how many
   boxes will contain: (i) no defective, and (ii) at least two defectives.
```

STEP 0: DECODE - this one has THREE hidden layers. Take them one at a time.

```
   LAYER 1: "0.1% of bottles are defective"   -> p = 0.1/100 = 0.001 (VERY small)
            "boxes containing 500 bottles"     -> n = 500 per box
            n is large and p is tiny, so the POISSON approximation applies (see below)
            lambda = n x p = 500 x 0.001 = 0.5 defects per box

   LAYER 2: "find how many boxes will contain ..."  -> a COUNT again!
            100 boxes are bought -> the answer is 100 x P(event per box)

   LAYER 3: "(ii) at least two defectives"  -> a tail, use the complement
```

WHY SWITCH TO POISSON (the rule, and why it is allowed here):

```
   +---------------------------------------------------------------+
   | WHEN n IS BIG AND p IS SMALL, BINOMIAL LOOKS LIKE POISSON      |
   | (a common rule of thumb: n >= 100 and p <= 0.01 is safe)       |
   | with  lambda = n x p                                            |
   +---------------------------------------------------------------+

   n=500, p=0.001 -> lambda = 500 x 0.001 = 0.5

   WHY it is easier: binomial would need C(500,2), which is a monstrous number.
   Poisson needs only e^(-0.5) and 0.5^k.
```

═══════════════ PART (i): no defective in a box ═══════════════

```
  STEP 1  Poisson with lambda = 0.5, want k = 0:
          P(X=0) = e^(-lambda) x lambda^0 / 0!
                 = e^(-0.5) x 1 / 1
                 = e^(-0.5)
  STEP 2  e^(-0.5) = 1 / e^0.5 = 1 / 1.6487 = 0.6065
  STEP 3  expected boxes = 100 x 0.6065 = 60.65, about 61 boxes
```

ANSWER: about 61 boxes will have no defective.

═══════════════ PART (ii): at least two defectives ═══════════════

```
  STEP 1  complement: P(X>=2) = 1 - P(0) - P(1)
  STEP 2  P(0) = 0.6065 (from part i)
  STEP 3  P(1) = e^(-0.5) x 0.5^1 / 1!
               = 0.6065 x 0.5
               = 0.3033
  STEP 4  add: 0.6065 + 0.3033 = 0.9098
  STEP 5  subtract: 1 - 0.9098 = 0.0902
  STEP 6  expected boxes = 100 x 0.0902 = 9.02, about 9 boxes
```

ANSWER: about 9 boxes will have at least two defectives.

TRAP:
```
   1. Using lambda = 0.001 (forgetting to multiply by the box size 500). lambda is the
      average per THE UNIT YOU ARE ASKING ABOUT, here per box.
   2. Reporting 0.6065 instead of 61 boxes. the "how many boxes" wording means multiply by 100.
   3. For "at least two", forgetting P(1). "at least 2" excludes BOTH 0 and 1.
```

═══════════════════════════════════════════════════════════════════════════════
F1.3  MOMENTS:  E(X) = np,  Var(X) = npq
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 5 (our paper, ETE 2025-26 S3 A3) - MCQ form
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   The salary of workers in a factory follows a binomial (180, 1/3) distribution.
   What will be the mean and variance of the distribution curve?
   a) 40, 60   b) 40, 50   c) 60, 50   d) 60, 40
```

STEP 0: DECODE "binomial (180, 1/3)"

```
   the notation B(n, p) or "binomial (n, p)" always gives the two parameters in the order:
        first = n (number of trials)      -> n = 180
        second = p (success probability)  -> p = 1/3
```

EVERY STEP:

```
  STEP 1  mean = n x p = 180 x (1/3)
          180 / 3 = 60                  (dividing 180 into three equal parts)
          so mean = 60

  STEP 2  q = 1 - p = 1 - 1/3 = 2/3

  STEP 3  variance = n x p x q = 180 x (1/3) x (2/3)
          do it in two pieces:
            180 x (1/3) = 60
            60 x (2/3) = 120/3 = 40
          so variance = 40

  STEP 4  match to the options: mean 60, variance 40 -> option (d)
```

ANSWER: option (d), 60 and 40.

TRAP:
```
   1. Confusing mean and variance: option (c) is 60, 50 which is the "swapped-ish" decoy.
      The mean is np (bigger here), the variance is npq (smaller, because q<1).
   2. Reading "binomial (180, 1/3)" as p=180. The FIRST number is always n.
   3. Computing q wrong: q = 1 - 1/3 = 2/3, not 1/3.
```

MUTATIONS:
```
   IF B(50, 0.4)   THEN mean = 20, var = 20 x 0.6 = 12.
   IF B(12, 0.1)   THEN mean = 1.2, var = 1.2 x 0.9 = 1.08.
   IF the question gives mean and variance and asks for n,p THEN: np = m and npq = v
        -> divide: q = v/m -> p = 1 - v/m -> n = m/p.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 6 (our paper, ETE 2025 summer Q3) - formula MCQ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Mean of Binomial distribution is:
   (A) np    (B) npq    (C) nq    (D) None of these
```

DECODE: pure recall. the mean (average number of successes) is n x p.

ANSWER: (A) np.

TRAP: choosing (B) npq, which is the VARIANCE. memorize the pair as a couplet:
```
   mean = np        (no q)     "the average is just tries x success-chance"
   variance = npq   (with q)   "the spread also depends on how balanced the coin is"
```

═══════════════════════════════════════════════════════════════════════════════
F1.4  RECOVERY: find p, or the whole pmf from a stated condition
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 7 (our paper, ETE 2024-25 S3 B4)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   If the sum of the mean and variance of a binomial distribution of 5 trials is 9/5,
   find the probability mass function of the binomial distribution.
```

STEP 0: DECODE "find the probability mass function"

```
   "probability mass function" (pmf) = the complete list of P(X=0), P(X=1), ..., P(X=n).
   "find the pmf" = find p (the success chance), then write out every value in a table.
   "5 trials" = n = 5.  so the pmf has 6 rows: X = 0,1,2,3,4,5.
```

IN PLAIN: we know n = 5. We are told (mean + variance) = 9/5. Every (mean, variance) pair
corresponds to exactly one p. Find that p, then build the table.

THE PICTURE:

```
   mean      = n p   = 5p
   variance  = n p q = 5p(1-p)
   given:  mean + variance = 9/5

        5p + 5p(1-p) = 9/5
```

EVERY STEP OF THE ALGEBRA (slowly, because this is where people give up):

```
  STEP 1  Write the given equation:
          5p + 5p(1-p) = 9/5

  STEP 2  Factor out 5p on the left:
          5p [ 1 + (1-p) ] = 9/5
          5p [ 2 - p ]     = 9/5

  STEP 3  Multiply out the left side:
          10p - 5p^2 = 9/5

  STEP 4  Multiply the whole equation by 5 to clear the fraction:
          50p - 25p^2 = 9

  STEP 5  Rearrange into a standard quadratic (bring everything to one side):
          25p^2 - 50p + 9 = 0
          (I moved everything to the right so the p^2 term is positive; either way works.)

  STEP 6  Use the quadratic formula. For a p^2 + b p + c = 0:
              p = [ -b +/- sqrt(b^2 - 4ac) ] / (2a)
          here a = 25, b = -50, c = 9
              p = [ 50 +/- sqrt(2500 - 4 x 25 x 9) ] / (2 x 25)
              p = [ 50 +/- sqrt(2500 - 900) ] / 50
              p = [ 50 +/- sqrt(1600) ] / 50
              p = [ 50 +/- 40 ] / 50

  STEP 7  Two solutions:
              p = (50 + 40)/50 = 90/50 = 1.8      <- IMPOSSIBLE (a probability cannot exceed 1)
              p = (50 - 40)/50 = 10/50 = 0.2      <- valid
          so p = 0.2 (which is 1/5)

  STEP 8  q = 1 - 0.2 = 0.8
```

THE CHECK (never skip this):
```
   mean = 5 x 0.2 = 1
   variance = 5 x 0.2 x 0.8 = 0.8
   mean + variance = 1 + 0.8 = 1.8 = 9/5   ✓ matches the question
```

NOW BUILD THE PMF (6 rows), with the arithmetic shown for two rows:

```
  P(X=x) = C(5,x) x (0.2)^x x (0.8)^(5-x)

  x=0:  C(5,0)=1,  (0.2)^0=1,   (0.8)^5 = 0.32768   -> 1 x 1 x 0.32768     = 0.32768
  x=1:  C(5,1)=5,  (0.2)^1=0.2, (0.8)^4 = 0.4096    -> 5 x 0.2 x 0.4096    = 0.4096
        (5 x 0.2 = 1.0, and 1.0 x 0.4096 = 0.4096)
  x=2:  C(5,2)=10, (0.2)^2=0.04,(0.8)^3 = 0.512     -> 10 x 0.04 x 0.512   = 0.2048
        (10 x 0.04 = 0.4, 0.4 x 0.512 = 0.2048)
  x=3:  C(5,3)=10, (0.2)^3=0.008,(0.8)^2=0.64       -> 10 x 0.008 x 0.64   = 0.0512
  x=4:  C(5,4)=5,  (0.2)^4=0.0016,(0.8)^1=0.8       -> 5 x 0.0016 x 0.8    = 0.0064
  x=5:  C(5,5)=1,  (0.2)^5=0.00032,(0.8)^0=1        -> 1 x 0.00032 x 1     = 0.00032
```

THE ANSWER TABLE (this IS the pmf):

```
   +-----+----------+
   |  x  |  P(X=x)  |
   +-----+----------+
   |  0  |  0.32768 |
   |  1  |  0.40960 |
   |  2  |  0.20480 |
   |  3  |  0.05120 |
   |  4  |  0.00640 |
   |  5  |  0.00032 |
   +-----+----------+
   sum  |  1.00000 |   <- check: a real pmf always sums to exactly 1
```

THE BAR CHART PICTURE:

```
   0.41 |              ##
   0.37 |   ##          ##
   0.32 |   ##          ##
   0.28 |   ##          ##
   0.25 |   ##          ##
   0.20 |   ##    ##    ##
   0.15 |   ##    ##    ##
   0.10 |   ##    ##    ##
   0.05 |   ##    ##    ##    ##
   0.00 +---x=0--x=1--x=2--x=3--x=4--x=5----
           1/3   .41  .20  .05  .006 .0003

   shape: starts high at 0, peaks at 1, decays. small p pushes the mass to the left.
```

TRAP:
```
   1. In step 6, forgetting the quadratic formula has TWO solutions, then picking 1.8.
      ALWAYS discard any p outside [0,1].
   2. "find the pmf" and reporting only p. The pmf is the TABLE, all six rows.
   3. An arithmetic slip in the quadratic: sqrt(1600) = 40, not 400.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 7b (MTE 2024-25 paper, block C1 part b - THE REAL THING, 4 marks)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   A random variable X follows a binomial distribution with mean 5/3 and P(X=1) = P(X=2).
   Find the variance, P(X >= 1), and P(X <= 1).
```

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 8 (our deck ppt3 p017) - find p from a ratio, then a count
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   An irregular six-faced die is thrown. The probability of getting 5 even numbers in
   10 throws is TWICE the probability of getting 4 even numbers in 10 throws.
   In 10,000 sets of 10 throws each, how many times would you expect NO even number?
```

STEP 0: DECODE - TWO hidden asks in one question.

```
   ASK 1 (hidden): the ratio condition is not the real question. it is a CLUE to find p,
                   the chance of an even number on one throw of this irregular die.
   ASK 2 (the real one): once p is known, find P(no even number in 10 throws), then
                   multiply by 10,000 (a COUNT again).
```

THE STRUCTURE:

```
   +-----------------------------------+
   | CLUE: P(X=5) = 2 x P(X=4), n=10    |
   +-----------------------------------+
                   |
                   v
        solve for p  (the die's even-chance)
                   |
                   v
   +-----------------------------------+
   | find P(X=0) with that p, n=10      |
   +-----------------------------------+
                   |
                   v
        expected = 10,000 x P(X=0)
```

EVERY STEP:

```
  STEP 1  Write the clue with the formula on both sides (n = 10 for both):
          C(10,5) p^5 q^5  =  2 x C(10,4) p^4 q^6

  STEP 2  Work out the combinations:
          C(10,5) = 252
          C(10,4) = 210

  STEP 3  Put them in:
          252 p^5 q^5 = 2 x 210 x p^4 q^6
          252 p^5 q^5 = 420 p^4 q^6

  STEP 4  Divide both sides by p^4 q^5  (the pieces common to both):
          252 p = 420 q

  STEP 5  Divide both sides by 84 to simplify:
          3 p = 5 q

  STEP 6  Replace q with (1 - p):
          3 p = 5 (1 - p)
          3 p = 5 - 5 p
          3 p + 5 p = 5
          8 p = 5
          p = 5/8 = 0.625
          and q = 1 - 5/8 = 3/8 = 0.375

  STEP 7  CHECK: does this satisfy the clue? (quick sanity)
          p=0.625 is greater than 0.5, so 5 evens (a high count) is more likely to
          be twice 4 evens. the direction is plausible. the algebra already proved it.

  STEP 8  Now the real ask: P(no even number in 10 throws) = P(X=0) with p=5/8, q=3/8
          P(X=0) = C(10,0) x (5/8)^0 x (3/8)^10 = 1 x 1 x (3/8)^10

  STEP 9  (3/8)^10: compute carefully.
          3/8 = 0.375
          0.375^2 = 0.140625
          0.375^4 = 0.140625^2 = 0.019775
          0.375^8 = 0.019775^2 = 0.000391
          0.375^10 = 0.375^8 x 0.375^2 = 0.000391 x 0.140625 = 0.0000550

  STEP 10 expected count = 10,000 x 0.0000550 = 0.55, about 1 time (or "roughly half a time";
          as a count you would report 0 or 1, and this tells you it is very rare)
```

ANSWER: P(no even) = (3/8)^10 = 0.000055, and the expected number of such sets out of
10,000 is about 0.55.

TRAP:
```
   1. Not seeing that the ratio condition is a CLUE, and trying to answer the count question
      with p = 0.5 (the fair-die value). The die is irregular, that is the whole point.
   2. Dividing step 4 wrongly, e.g. dividing by p^5 q^6 instead of p^4 q^5, which changes
      the exponents and breaks the algebra.
   3. In step 10, computing 10,000 x 0.000055 = 0.55 but reporting "0.55 times" as if the
      answer must be a whole number. an EXPECTED count can be less than 1.
```

═══════════════════════════════════════════════════════════════════════════════
F1 SUMMARY CARD (the compressed version, for revision)
═══════════════════════════════════════════════════════════════════════════════

```
   4 INGREDIENTS:  fixed n | two outcomes | constant p | independent

   FORMULA:        P(X=k) = C(n,k) p^k q^(n-k)         q = 1-p
   C(n,k):         n!/(k!(n-k)!)  e.g. C(12,2)=66, C(10,5)=252, C(6,2)=15

   MEAN:           np
   VARIANCE:       npq

   WORD MAP:
     "exactly k"        -> P(X=k), the formula straight
     "at least k"       -> 1 - P(0) - ... - P(k-1)      (complement, few terms)
     "more than k"      -> 1 - P(0) - ... - P(k)        (note: starts at k+1)
     "at most k"        -> P(0) + ... + P(k)            (add the few small terms)
     "how many expected"-> COUNT = (number of groups) x P(event)
     "at least one"     -> 1 - q^n
     "none"             -> q^n

   SWITCH TO POISSON WHEN: n big (>=100) and p small (<=0.01), then lambda = np

   TOP TRAPS:
     "at least 2" is not "at least 1" (do not drop P(1))
     (0.10)^0 = 1, not 0
     p never exceeds 1 (discard impossible quadratic roots)
     "how many" means multiply by the group count
```
