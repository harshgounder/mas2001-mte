# F11-expectation-laws GUIDE: the explanation content behind the questions

This is the non-question content from the family file: the family intro, the
toolboxes, the section intros, decision trees, and the summary card. It is the
TEACHING layer. Read it first (it gives the method), then drill the q*.md files.

Source: deck/worked/F11-expectation-laws.md (same content; this file just isolates it).


──────────────────────────────────────────────────────────────────────────────
[FAMILY INTRO / PREAMBLE (before the first question)]
──────────────────────────────────────────────────────────────────────────────

# F11 EXPECTATION AND VARIANCE LAWS: every shape, solved from zero

Source: our own material (MTE 2025-26 Q8, MTE 2024-25 A1/B1, the ETE papers E24S4, E25SUM,
R25S3, R25S4). Nothing invented. All numbers machine-checked (17/17).

```
  SHAPES IN THIS FILE
  F11.1  the laws of expectation and variance  (the toolbox)      0 questions, the rules
  F11.2  E[XY] for independent variables        MCQ               1 question
  F11.3  variance is always ...                 MCQ               1 question
  F11.4  scaling a Poisson: Y = 2X              MCQ + full solve  1 question (MTE!)
  F11.5  the typist / letters question          the full solve    1 question (MTE!)
  F11.6  soldiers over 6 feet                   the full solve    1 question
```

WHY THIS FILE: F1, F2, F6 and F10 each compute a mean or variance as part of their own
questions. This file collects the LAWS that all of those computations silently use, plus the
four questions that are purely about these laws.

═══════════════════════════════════════════════════════════════════════════════
F11.1  THE LAWS  (the toolbox; every question below uses these)
═══════════════════════════════════════════════════════════════════════════════

THE EXPECTATION LAWS:

```
   +---------------------------------------------------------------+
   | E(c)        = c            a constant's expectation is itself  |
   | E(cX)       = c E(X)       constants pull out of E             |
   | E(X + Y)    = E(X) + E(Y)  ALWAYS (no independence needed)     |
   | E(X - Y)    = E(X) - E(Y)  ALWAYS                              |
   | E(XY)       = E(X) E(Y)    if X and Y are independent          |
   +---------------------------------------------------------------+
```

THE VARIANCE LAWS:

```
   +---------------------------------------------------------------+
   | Var(c)      = 0            a constant does not vary            |
   | Var(cX)     = c^2 Var(X)   the constant is SQUARED (not pulled) |
   | Var(X + c)  = Var(X)       adding a constant shifts, no spread  |
   | Var(X + Y)  = Var(X) + Var(Y)   when INDEPENDENT               |
   | Var(X - Y)  = Var(X) + Var(Y)   when INDEPENDENT (PLUS! see)   |
   | Var(aX + bY) = a^2 Var(X) + b^2 Var(Y)   when independent      |
   +---------------------------------------------------------------+
```

THE TWO MOST-EXAMINED CONTRASTS (draw these; they decide half the MCQs):

```
   +--------------------------------+--------------------------------+
   | THE CONSTANT                   | EXPECTATION      VARIANCE      |
   +--------------------------------+--------------------------------+
   | cX     (scale by c)            | c E(X)           c^2 Var(X)    |
   | X + c  (shift by c)            | E(X) + c         Var(X)        |
   +--------------------------------+--------------------------------+
   | remember: E pulls the constant OUT; Var SQUARES it (for scaling)|
   +--------------------------------+--------------------------------+
```

THE SUBTRACTION SURPRISE:

```
   Var(X - Y) = Var(X) + Var(Y)     <- PLUS, even though it is a minus!

   why: variance measures SPREAD. subtracting two random quantities lets each one wander,
   and their wanderings ADD. the picture:

        X wanders this much:   <---->
        Y wanders this much:   <---->
        X - Y wanders:         <-------->  the variations combine, they do not cancel.
```

THE OTHER FORMULAS (used everywhere in F1-F10, collected here):

```
   Var(X) = E(X^2) - [E(X)]^2        the computational formula
   E(aX + b) = a E(X) + b            linearity
   E[aX^2 + bX + c] = a E(X^2) + b E(X) + c
```

═══════════════════════════════════════════════════════════════════════════════
F11.2  E[XY] FOR INDEPENDENT VARIABLES  (MCQ)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q1 and Q2)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F11.3  VARIANCE IS ALWAYS ...  (MCQ)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q2 and Q3)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F11.4  SCALING A POISSON:  Y = 2X   (MCQ, and the full solve underneath)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q3 and Q4)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F11.5  THE TYPIST / LETTERS QUESTION  (MTE 2025-26 Q8 - the full solve)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q4 and Q5)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F11.6  SOLDIERS OVER 6 FEET  (normal + expectation, the full solve)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q5 and Q6)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F11.7  MORE PAPER QUESTIONS AND THE OFFICIAL-SCHEME FORMS
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
THE TYPIST IN THE OFFICIAL FORM (the scheme expresses the answer per WORD)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The university's solution scheme for M25-Q8 works with the per-WORD mistake probability p
and the base-10 log form (with e = 2.72, log10(e) = 0.4346). Both are the same answer in
different units. Learn both; the exam accepts either, but its scheme uses this one:

```
   (i)  e^(-200p) >= 0.99
        -200p x log10(e) >= log10(0.99)
        -p x (200 x 0.4346) >= -0.0044
        p <= 0.0044/86.92 = 0.0000506        (the scheme's value)

   (ii) e^(-4000p) = 0.90
        -4000p x log10(e) = log10(0.90)
        -p x (4000 x 0.4346) = -0.0458
        p = 0.0458/1738.4 = 0.0000263        (the scheme's value)
```

THE TRANSLATION TABLE (so you can move between the two forms):
```
   +-------------------------+------------------+--------------------+
   | quantity                | per-word p      | per-letter lambda  |
   +-------------------------+------------------+--------------------+
   | (i)  answer             | 0.0000506       | 0.01005            |
   | (ii) answer             | 0.0000263       | 0.00527            |
   | relation                | lambda = 200 p  | (200 words/letter) |
   +-------------------------+------------------+--------------------+
   exact values (natural logs): p_i = 5.03e-5, p_ii = 2.63e-5.
   the scheme's 5.06e-5 differs only by the 2.72 rounding; state the form you use.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[CLOSING SECTION (after Q6; usually the summary card)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F11 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   EXPECTATION LAWS              VARIANCE LAWS
     E(c) = c                      Var(c) = 0
     E(cX) = c E(X)                Var(cX) = c^2 Var(X)     <- SQUARED
     E(X +- Y) = E(X) +- E(Y)      Var(X +- c) = Var(X)
        always                     Var(X +- Y) = Var(X) + Var(Y)   when independent
     E(XY) = E(X)E(Y)                 (PLUS even for the minus case)
        whenever independent; dependence does not by itself rule out equality

   Var(X) = E(X^2) - [E(X)]^2

   THE MCQs IN ONE BREATH:
     independent product  -> E[XY] = E[X]E[Y]
     variance             -> always non-negative
     scaling a Poisson Y=2X -> E doubles, Var QUADRUPLES

   THE TYPIST (MTE Q8): rate per letter vs rate per day (x20); (i) upper bound 0.01005,
     (ii) equation -> 0.00527.

   THE SOLDIERS: 6 feet = 72 in; sigma = sqrt(10.8) = 3.29; z = 1.15; tail 0.1251;
     expected count = 125.

   TOP TRAPS:
     Var(2X) = 2 Var(X)        WRONG, it is 4 Var(X)
     Var(X - Y) = Var(X) - Var(Y)  WRONG, it is PLUS (for independent)
     variance as sd (10.8 vs sqrt(10.8) = 3.29)
     6 feet not converted to 72 inches
     per-letter vs per-day rates (the factor 20)
```
