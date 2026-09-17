# F5-chebyshev GUIDE: the explanation content behind the questions

This is the non-question content from the family file: the family intro, the
toolboxes, the section intros, decision trees, and the summary card. It is the
TEACHING layer. Read it first (it gives the method), then drill the q*.md files.

Source: deck/worked/F5-chebyshev.md (same content; this file just isolates it).


──────────────────────────────────────────────────────────────────────────────
[FAMILY INTRO / PREAMBLE (before the first question)]
──────────────────────────────────────────────────────────────────────────────

# F5 CHEBYSHEV: every shape, every question, solved from zero

Source: our own material (MTE 2024-25 blocks A3 and B3, MTE 2025-26 block Q5, the ETE papers
E24S3, E25S3, E24S4, E25S4, and the L10-11 Chebyshev deck). Nothing invented. Every number
machine-checked (15/15 checks pass).

WHY THIS FILE IS THE MOST IMPORTANT ONE: Chebyshev appears in EVERY sitting we hold (9 of 9),
and the ETE re-sit and both MTE papers all carry it. It is the highest-frequency topic in the
course.

```
  SHAPES IN THIS FILE
  F5.1  within-k        "what fraction lies within k sigma"      1 question
  F5.2  find-c          "find c such that P(...) <= p"           1 question (MTE!)
  F5.3  inverse         "given the bound, find mean and variance" 2 questions
  F5.4  statement-MCQ   "which is/are NOT Chebyshev"             1 question (MTE!)
  F5.5  interpretation  "what is it useful for"                   1 question
  F5.6  composite       bound vs actual                          1 question (MTE!)
```

═══════════════════════════════════════════════════════════════════════════════
BEFORE ANY QUESTION: what Chebyshev is FOR (get this right and the rest follows)
═══════════════════════════════════════════════════════════════════════════════

Chebyshev bounds how much of a distribution can lie FAR from the mean, using ONLY the mean and
variance. You do not need to know the shape of the distribution.

```
   +---------------------------------------------------------------------+
   |  THE THREE FORMS (memorize all three; the questions use all three)   |
   |                                                                      |
   |   (1) tail form, in sigma units:                                     |
   |         P( |X - mu| >= k sigma )  <=  1 / k^2                        |
   |                                                                      |
   |   (2) within form, in sigma units:                                   |
   |         P( |X - mu| <  k sigma )  >=  1 - 1 / k^2                    |
   |                                                                      |
   |   (3) tail form, in RAW units (when the gap is a plain number c):    |
   |         P( |X - mu| >= c )  <=  sigma^2 / c^2                        |
   |                                                                      |
   |  mu = mean, sigma = standard deviation, sigma^2 = variance.          |
   +---------------------------------------------------------------------+
```

THE VALUE TABLE (memorize; MCQs and fill-in-the-blanks use these):

```
   +------+------------------+------------------+
   |  k   | within 1 - 1/k^2 | outside 1/k^2    |
   +------+------------------+------------------+
   |  2   | 3/4  = 0.75      | 1/4  = 0.25      |
   |  3   | 8/9  = 0.8889    | 1/9  = 0.1111    |
   |  4   | 15/16= 0.9375    | 1/16 = 0.0625    |
   |  5   | 24/25= 0.96      | 1/25 = 0.04      |
   +------+------------------+------------------+
```

THE PICTURE (why it is only a BOUND, not exact):

```
                         1/k^2  (max outside)
   |<--- 1 - 1/k^2 (min inside) --->|<--- 1/k^2 --->|
   |                                |               |
   ---------mu-k sigma-----mu-----mu+k sigma---------

   Chebyshev gives a FLOOR on the inside and a CEILING on the outside.
   It never claims the exact values, because it must be true for EVERY distribution.
   A specific distribution (like uniform) can do much better, which is why
   "bound vs actual" questions get very different numbers.
```

═══════════════════════════════════════════════════════════════════════════════
F5.1  WITHIN-K:  "what fraction lies within k sigma"
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q1 and Q2)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F5.2  FIND-C:  "find c such that P(|X-mu| >= c) <= p"
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q2 and Q3)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F5.3  INVERSE:  "given the bound, find mean and variance"
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q4 and Q5)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F5.4  STATEMENT MCQ:  "which is/are NOT Chebyshev"
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q5 and Q6)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F5.5  INTERPRETATION MCQ:  "what is it useful for"
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q6 and Q7)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F5.6  COMPOSITE:  bound vs actual
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[CLOSING SECTION (after Q7; usually the summary card)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F5 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   THREE FORMS:
     tail  (>= k sigma):  <= 1/k^2
     within(<  k sigma):  >= 1 - 1/k^2
     raw   (>= c):        <= sigma^2 / c^2

   TABLE: k=2 -> 3/4 ; k=3 -> 8/9 ; k=4 -> 15/16 ; k=5 -> 24/25

   THE SKILL: look at the right of the |X-mu|.
     "k sigma" -> form 1 ; a bare number c -> form 3 ; "within" -> form 2.
     c = k sigma connects forms 1 and 3.

   INVERSE (given the interval):
     centre = mean ; half-width = k sigma ; match to 1 - 1/k^2 (if within).

   MCQ CHECKLIST: structure |X-mu| ok? direction pairing ok? formula the right one?
     >= with <= ;  < with >= ; tail=1/k^2 ; within=1-1/k^2.
     and remember to read "NOT" if the question says NOT.

   BOUND vs ACTUAL:
     answer BOTH. the bound from Chebyshev, the actual from the distribution (or by reading
     the support, which is often all that is needed).

   WHY IT MATTERS: Chebyshev is in EVERY sitting we hold. this is the single highest-value
   topic in the course.

   TOP TRAPS:
     within vs outside (the 8/9 vs 1/9 fork)             <- the most common single error
     using form 1 when a bare c is given (or vice versa)
     not seeing the interval midpoint is the mean
     answering only the bound on a bound-vs-actual question
     missing the "NOT" in a statement MCQ
```
