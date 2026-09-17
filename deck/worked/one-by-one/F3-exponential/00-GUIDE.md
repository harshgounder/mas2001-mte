# F3-exponential GUIDE: the explanation content behind the questions

This is the non-question content from the family file: the family intro, the
toolboxes, the section intros, decision trees, and the summary card. It is the
TEACHING layer. Read it first (it gives the method), then drill the q*.md files.

Source: deck/worked/F3-exponential.md (same content; this file just isolates it).


──────────────────────────────────────────────────────────────────────────────
[FAMILY INTRO / PREAMBLE (before the first question)]
──────────────────────────────────────────────────────────────────────────────

# F3 EXPONENTIAL: every shape, every question, solved from zero

Source: our own material (MTE 2024-25 block B2, MTE 2025-26 block Q6, the ETE papers E24S4,
E25S4, E25SUM, R25S3, and the ppt4 deck). Nothing invented. Every number machine-checked
(12/12 checks pass).

```
  SHAPES IN THIS FILE
  F3.1  setup        pdf / cdf, and the mean-vs-parameter trap   1 question
  F3.2  point        P(X>a), P(X<a)                              1 question (MTE!)
  F3.3  interval     P(a<X<b)                                    1 question (MTE!)
  F3.4  conditional  memoryless                                  1 question
  F3.5  moments      mean, variance, and both directions         1 question (MTE!)
  F3.6  independence multi-variable product                      1 question
```

═══════════════════════════════════════════════════════════════════════════════
BEFORE ANY QUESTION: what "exponential" means
═══════════════════════════════════════════════════════════════════════════════

An exponential models WAITING TIME: how long until the next event, or how long something
lasts (a phone call, a component, a shelf life).

```
   +-------------------------------------------------------------------+
   |  THREE FORMS you must know (l = lambda, the RATE):                 |
   |                                                                    |
   |   pdf (density)   f(x) = l e^(-l x)              x > 0              |
   |   cdf (up to x)   F(x) = 1 - e^(-l x)            P(X < x)           |
   |   survival        S(x) = e^(-l x)                P(X > x)           |
   |                                                                    |
   |   MEAN     = 1 / l       <- careful: ONE OVER lambda                 |
   |   VARIANCE = 1 / l^2                                                 |
   +-------------------------------------------------------------------+
```

THE #1 TRAP, LEARN IT BEFORE ANYTHING ELSE:

```
   +-------------------------------+----------------------------------+
   |  THE QUESTION SAYS            |  SO WHAT IS lambda?              |
   +-------------------------------+----------------------------------+
   |  "mean = 3"                   |  lambda = 1/3                    |
   |  "average life 8 hours"       |  lambda = 1/8                    |
   |  "parameter 1/4"              |  lambda = 1/4 (given directly)   |
   |  "rate 15 per hour"           |  lambda = 15                     |
   |  "f(x) = e^(-x)"              |  lambda = 1 (the coefficient!)   |
   +-------------------------------+----------------------------------+

   THE MEAN IS THE RECIPROCAL OF THE RATE.
   if the question says "mean" or "average", INVERT.
   if it says "parameter" or "rate", DO NOT invert.
```

PICTURE of the density (decaying):

```
   f(x)
   1.0 |##
       | ##
   0.7 |  ##
       |   ##
   0.4 |     ###
       |        ####
   0.1 |            ########
   0.0 +---------------------########------
        0   1   2   3   4   5   6   7   8

   tallest at 0, decays forever. small x = very likely, large x = rare.

   AREA picture for probabilities:
       P(X < 2)  = area from 0 to 2 under the curve  = 1 - e^(-2l)
       P(X > 2)  = area from 2 to infinity           = e^(-2l)
       both pieces together = 1 (whole area)
```

═══════════════════════════════════════════════════════════════════════════════
F3.1  SETUP:  the pdf, and identifying lambda from a given density
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q2 and Q3)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F3.2  POINT:  P(X > a), P(X < a)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q3 and Q4)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F3.3  INTERVAL:  P(a < X < b)   (covered in Q3 part ii; a second practice below)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q4 and Q5)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F3.4  CONDITIONAL / MEMORYLESS  (the hidden-layer item)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q5 and Q6)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F3.5  MOMENTS:  mean 1/lambda, variance 1/lambda^2  (both directions)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[CLOSING SECTION (after Q6; usually the summary card)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F3 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   FORMS:
     f(x) = l e^(-l x)
     F(x) = 1 - e^(-l x)      P(X < x)
     S(x) = e^(-l x)          P(X > x)
     P(a<X<b) = e^(-l a) - e^(-l b)

   MEAN = 1/l ,  VARIANCE = 1/l^2 ,  SD = 1/l = MEAN        <- sd equals mean

   WORD MAP (the inversion rule is the whole game):
     "mean = m" / "average = m"   -> lambda = 1/m        INVERT
     "parameter = l" / "rate = l" -> lambda = l          DO NOT invert
     f(x) = a e^(-a x)            -> lambda = a          read the coefficient

   MEMORYLESS:  P(X > s+t | X > s) = P(X > t)    (the past is irrelevant)

   FREE CHECKS:
     P(X < mean) = 1 - e^-1 = 0.632 ALWAYS
     sd = mean ALWAYS
     if an answer exceeds 1, you added where you should have multiplied

   TOP TRAPS:
     not inverting when the wording says "mean"
     inverting when the wording says "parameter"
     P(a<X<b) subtraction order
     ignoring the "given" in a conditional
```
