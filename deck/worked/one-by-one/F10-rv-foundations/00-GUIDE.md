# F10-definition-foundations GUIDE: the explanation content behind the questions

This is the non-question content from the family file: the family intro, the
toolboxes, the section intros, decision trees, and the summary card. It is the
TEACHING layer. Read it first (it gives the method), then drill the q*.md files.

Source: deck/worked/F10-definition-foundations.md (same content; this file just isolates it).


──────────────────────────────────────────────────────────────────────────────
[FAMILY INTRO / PREAMBLE (before the first question)]
──────────────────────────────────────────────────────────────────────────────

# F10 DEFINITION AND FOUNDATION QUESTIONS: solved from zero

Source: our own material (the ETE papers E25S4, E25SUM, R25S4, E24S3, E25S3). Nothing invented.
All numbers machine-checked (5/5).

WHY THIS FILE EXISTS: these are pure-recall marks. They are the cheapest marks on the paper
and students lose them by not having the definitions word-perfect. Every sentence here has
appeared in a real paper.

```
  SHAPES IN THIS FILE
  F10.1  what a random variable is       3 questions (all near-identical)
  F10.2  the pmf find-k drill            1 question (with a twist: three k-terms)
  F10.3  the joint pmf + marginal        1 question
  F10.4  the expectation chain           (covered in F1-F3; summarized here)
```

═══════════════════════════════════════════════════════════════════════════════
F10.1  WHAT A RANDOM VARIABLE IS
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q1 and Q2)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F10.2  THE PMF FIND-K DRILL  (with the three-k-terms twist)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q2 and Q3)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F10.3  THE JOINT PMF AND THE MARGINAL  (a two-variable extension)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q3 and Q4)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F10.4  THE EXPECTATION CHAIN (recap; the full treatment is in F1-F3)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[CLOSING SECTION (after Q10; usually the summary card)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F10 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   RANDOM VARIABLE      = a FUNCTION from the sample space to the real numbers
   DISCRETE rv          = countable values
   P(exact value) = 0   for a CONTINUOUS rv
   STANDARD NORMAL      = mean 0, variance 1
   CDF range            = [0, 1]

   PMF RULE              sum of all probabilities = 1  (this is the only tool for find-k)
     if terms include k^2 -> quadratic in k -> two roots -> DISCARD the negative one

   JOINT PMF            P(x,y) = K(...)
     find K:  sum over the WHOLE grid, set = 1
     marginal of X:  sum the joint over all y

   EXPECTATION
     E(X)   = sum x P(x)
     E(X^2) = sum x^2 P(x)
     E[(2X+1)^2]: EXPAND first (4X^2+4X+1), then 4E(X^2)+4E(X)+1
     E[(2X+1)^2] is NOT [E(2X+1)]^2

   TOP TRAPS:
     rv is a function, not a constant/probability/event
     missing a hidden k-term in a long pmf expression
     keeping the negative root of a quadratic
     marginalising over the wrong variable
     squaring the expectation instead of the variable
```
