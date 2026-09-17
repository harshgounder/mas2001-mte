# F2-poisson GUIDE: the explanation content behind the questions

This is the non-question content from the family file: the family intro, the
toolboxes, the section intros, decision trees, and the summary card. It is the
TEACHING layer. Read it first (it gives the method), then drill the q*.md files.

Source: deck/worked/F2-poisson.md (same content; this file just isolates it).


──────────────────────────────────────────────────────────────────────────────
[FAMILY INTRO / PREAMBLE (before the first question)]
──────────────────────────────────────────────────────────────────────────────

# F2 POISSON: every shape, every question, solved from zero

Source of every question: our own material (the MTE 2024-25 paper, the MTE 2025-26 paper, the
ETE papers E24S3, E25SUM, R25S3, R25S4, and the ppt3 deck). Nothing invented. Every number
computed and checked on the machine (9/9 checks pass).

```
  SHAPES IN THIS FILE
  F2.1  point         P(X=k)                     2 questions (deck + paper)
  F2.2  tail          P(X>=k) / at least         1 question
  F2.3  recovery      recover lambda from a ratio 2 questions (MTE!)
  F2.4  rate/window   rescale lambda              1 question
  F2.5  nesting       Poisson then binomial       1 question (deck)
  F2.6  moments algebra  Var of a function        2 questions (MTE!)
  F2.7  formula MCQ   name the pmf                1 question (MTE!)
```

═══════════════════════════════════════════════════════════════════════════════
BEFORE ANY QUESTION: what "Poisson" means
═══════════════════════════════════════════════════════════════════════════════

A Poisson situation counts HOW MANY RARE EVENTS happen in a fixed span (time, space, pages).

```
   +-----------------------------------------------------------------+
   |  YOU GET:                                                        |
   |     lambda  = the AVERAGE count in the span you care about       |
   |                                                                |
   |  YOU WANT:                                                       |
   |     the probability of exactly k events                          |
   |                                                                |
   |  THE FORMULA:                                                    |
   |                                                                |
   |                    e^(-lambda)  x  lambda^k                      |
   |      P(X = k)  =  --------------------------                     |
   |                            k!                                    |
   +-----------------------------------------------------------------+
```

WHAT EVERY SYMBOL MEANS, in plain words:

```
   e          the special number 2.71828... It lives on your calculator (the e^x button).
              e^(-lambda) is a small number; for lambda=1 it is 0.3679.
   lambda     "the average". ALSO the variance (see the signature below).
   k          the count you are asking about. k! = k x (k-1) x ... x 1, and 0! = 1, 1! = 1.
   X          the number of events. A name.
```

THE SIGNATURE (memorize this; it is the fastest way to spot a Poisson):

```
   +---------------------------------------+
   |  MEAN  =  VARIANCE  =  lambda          |
   +---------------------------------------+

   for a Poisson law, the mean and variance are the SAME NUMBER for every lambda.
   This is the Poisson signature, but an observed numerical equality by itself is not
   sufficient to prove a Poisson law. Another distribution can have matching mean and
   variance for a particular parameter choice, so use the stated model or the full
   probability formula.
```

THE PICTURE of the pmf (lambda = 1.5, the car-hire example later in this file):

```
   P(X=k)
   0.33 |           ##
   0.30 |           ##
   0.27 |     ##    ##
   0.22 |     ##    ##
   0.20 |     ##    ##    ##
   0.15 |     ##    ##    ##
   0.10 |     ##    ##    ##    ##
   0.05 |     ##    ##    ##    ##    ##
   0.00 +---- k=0---k=1---k=2---k=3---k=4---k=5---
              .22   .33   .25   .13   .047  .014

   the peak sits near lambda, and the tail stretches right. "rare events" means the left
   side is fat: k=0 is always a big chunk.
```

THE WINDOW RULE (the single most common Poisson error, learn it now):

```
   lambda MUST match the span you are asking about.

   +----------------------------------------------------------+
   |  rate = 3 per minute.  ask is about 5 minutes.            |
   |  then lambda = 3 x 5 = 15, NOT 3.                         |
   |                                                           |
   |  rate = 0.5 per box.   ask is about 100 boxes.            |
   |  then lambda per box = 0.5 (if asking about one box)      |
   +----------------------------------------------------------+
```

═══════════════════════════════════════════════════════════════════════════════
F2.1  POINT:  P(X = k)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q2 and Q3)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F2.3  RECOVERY: find lambda from a stated ratio  (BOTH MTE PAPERS ASK THIS)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q4 and Q5)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F2.4  RATE / WINDOW RESCALING
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q5 and Q6)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F2.5  NESTING: Poisson then Binomial (the composite they love)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q6 and Q7)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F2.6  MOMENTS ALGEBRA:  Var of a function of a Poisson
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q7 and Q8)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F2.7  FORMULA MCQ / IDENTIFICATION
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[CLOSING SECTION (after Q8; usually the summary card)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F2 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   FORMULA:   P(X=k) = e^(-lambda) lambda^k / k!
   MEAN = VARIANCE = lambda        <- the signature
   0! = 1

   WINDOW RULE: lambda must match the span asked about.
                per minute rate + 5-minute ask -> lambda = rate x 5

   SWITCH FROM BINOMIAL WHEN: n big (>=100) and p small (<=0.01), lambda = n x p

   RECOVERY FROM A RATIO: set the two pmfs equal, cancel e^(-l), solve.
        P(X=1)=P(X=2) -> l=2 ;  P(Y=2)=P(Y=3) -> m=3
        general: P(X=k)=P(X=k+1) -> lambda = k+1

   VARIANCE RULES (independent):
        Var(X + Y) = Var(X) + Var(Y)
        Var(X - Y) = Var(X) + Var(Y)     <- minus becomes PLUS
        Var(aX)    = a^2 Var(X)          <- square the constant
        Var(X - 2Y) = Var(X) + 4 Var(Y)

   WORD MAP:
     "no demand" / "none"        -> P(0) = e^(-lambda)
     "at least k"                -> 1 - P(0) - ... - P(k-1)
     "at most k"                 -> P(0) + ... + P(k)
     "how many boxes expected"   -> COUNT = boxes x P(event)
     "in each of n intervals"    -> NESTING: Poisson first, then p^n

   TOP TRAPS:
     lambda not rescaled to the asked window (the #1 error)
     "at least 2" dropping P(1)
     Var(aX) using a instead of a^2
     Var(X - Y) written as Var(X) - Var(Y) (impossible; variances add)
```
