# F1-binomial GUIDE: the explanation content behind the questions

This is the non-question content from the family file: the family intro, the
toolboxes, the section intros, decision trees, and the summary card. It is the
TEACHING layer. Read it first (it gives the method), then drill the q*.md files.

Source: deck/worked/F1-binomial.md (same content; this file just isolates it).


──────────────────────────────────────────────────────────────────────────────
[FAMILY INTRO / PREAMBLE (before the first question)]
──────────────────────────────────────────────────────────────────────────────

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


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q3b and Q4)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F1.2  TAIL:  P(X >= k) - covered above in Q1(ii) and Q2, plus one more form
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q4 and Q5)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F1.3  MOMENTS:  E(X) = np,  Var(X) = npq
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q6 and Q7)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F1.4  RECOVERY: find p, or the whole pmf from a stated condition
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[CLOSING SECTION (after Q8; usually the summary card)]
──────────────────────────────────────────────────────────────────────────────

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
