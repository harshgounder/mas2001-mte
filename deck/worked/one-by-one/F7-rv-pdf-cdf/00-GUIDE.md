# F7-rv-pdf-cdf GUIDE: the explanation content behind the questions

This is the non-question content from the family file: the family intro, the
toolboxes, the section intros, decision trees, and the summary card. It is the
TEACHING layer. Read it first (it gives the method), then drill the q*.md files.

Source: deck/worked/F7-rv-pdf-cdf.md (same content; this file just isolates it).


──────────────────────────────────────────────────────────────────────────────
[FAMILY INTRO / PREAMBLE (before the first question)]
──────────────────────────────────────────────────────────────────────────────

# F7 RV / PDF / CDF: every shape, every question, solved from zero

Source: our own material (MTE 2024-25 block A2, MTE 2025-26 blocks Q1 and Q4, the ETE papers
E24S3, E24S4, E25SUM, R25S3, R25S4, and the notes/ppt decks). Nothing invented. Every number
machine-checked (9/9 checks pass, including the integrals done in exact fractions).

THIS IS THE LARGEST FAMILY (14 rows in-scope). Most distribution questions START here.

```
  SHAPES IN THIS FILE
  F7.1  total-mass MCQ     the integral equals what         1 question (MTE!)
  F7.2  find-k             normalise a density               1 question (MTE!)
  F7.3  find-two-constants two equations from two conditions 1 question
  F7.4  cdf from pdf       piecewise integration             1 question (MTE!)
  F7.5  pdf from cdf       differentiate                    1 question
  F7.6  pmf table + cdf    the discrete composite            1 question
```

═══════════════════════════════════════════════════════════════════════════════
BEFORE ANY QUESTION: the four things a density must satisfy
═══════════════════════════════════════════════════════════════════════════════

```
   +---------------------------------------------------------------------+
   |  for f(x) to be a PROBABILITY DENSITY:                               |
   |                                                                     |
   |   1. f(x) >= 0     everywhere (no negative probabilities)            |
   |   2. integral of f over ALL x  =  1     (total mass is one)          |
   |   3. P(a < X < b) = integral of f from a to b                        |
   |   4. the CDF  F(x) = integral of f from -inf to x                    |
   |      and  f(x) = F'(x)   (they are a matched pair)                   |
   +---------------------------------------------------------------------+
```

THE PICTURE (density = height, probability = area):

```
   f(x)
     |      ****
     |    ********
     |  ************
     |****************
     +---a----b--------x
       |<-- area -->|
       P(a<X<b) is the shaded AREA, not the height f(b).
```

THE THREE INTEGRALS YOU ACTUALLY NEED (nothing harder appears in this course):

```
   integral of x^n dx  =  x^(n+1) / (n+1)          (+ C, which cancels in definite integrals)

   definite version:
        integral from a to b of x^n dx  =  [ b^(n+1) - a^(n+1) ] / (n+1)
```

═══════════════════════════════════════════════════════════════════════════════
F7.1  TOTAL-MASS MCQ
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q1 and Q2)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F7.2  FIND-K:  normalise a density (the core skill of this whole family)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q2 and Q3)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F7.3  FIND TWO CONSTANTS from two conditions
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q3 and Q4)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F7.4  CDF FROM PDF:  the piecewise case
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q4 and Q5)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F7.5  PDF FROM CDF / FINDING THE CDF  (the paired skill)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q5 and Q6)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F7.6  PMF TABLE + CDF (the discrete composite)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[CLOSING SECTION (after Q6; usually the summary card)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F7 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   FOUR RULES for a density: f >= 0 | total integral = 1 | area = probability | F' = f

   THE INTEGRAL YOU NEED:  integral a to b of x^n dx = [b^(n+1) - a^(n+1)]/(n+1)

   FIND-K:      integrate f over the support, set = 1, solve for k
   FIND-2-CONST: two conditions (total mass + a given moment), solve simultaneously
   CDF:         F(x) = area from the start to x.  PIECEWISE if f is piecewise; do not
                forget the accumulated area from earlier pieces.
   PDF from CDF: differentiate.
   MEDIAN:      P(X<k) = P(X>k) means F(k) = 0.5. check for symmetry first.
   DISCRETE:    pmf table (count/36 style), then cumulative for the CDF.
                For integer-valued X with integer endpoints,
                P(a<=X<=b) = F(b) - F(a-1), note the a-1. Between support points F is flat.

   FREE CHECKS (they eliminate MCQ decoys and catch algebra slips):
     continuous support: F(left endpoint) = 0 and F(right endpoint) = 1 (here, no endpoint
     atom is present)
     discrete support: F(x) = 0 below the smallest support value, while F(at the smallest
     support value) includes that point's mass; F(x) = 1 at and above the largest value
     the pmf/cdf must be non-decreasing
     the mean must lie inside the support
     Var = E(X^2) - (E(X))^2, the second term SQUARED

   TOP TRAPS:
     not expanding brackets before integrating
     forgetting earlier pieces of a piecewise CDF
     rounding mid-calculation (use exact fractions, convert at the end)
     treating 11 dice sums as equally likely
```
