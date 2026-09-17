# F13-assignments GUIDE: the explanation content behind the questions

This is the non-question content from the family file: the family intro, the
toolboxes, the section intros, decision trees, and the summary card. It is the
TEACHING layer. Read it first (it gives the method), then drill the q*.md files.

Source: deck/worked/F13-assignments.md (same content; this file just isolates it).


──────────────────────────────────────────────────────────────────────────────
[FAMILY INTRO / PREAMBLE (before the first question)]
──────────────────────────────────────────────────────────────────────────────

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


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q8 and Q9)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F13.3  ASSIGNMENT-2 SECTIONS C+D:  the 6 full solves
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q15 and Q16)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F13.4  ASSIGNMENT-1 SHORT ANSWERS:  the 6 questions
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q21 and Q22)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F13.5  ASSIGNMENT-1 LONG ANSWERS:  the 3 questions
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q24 and Q25)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F13.6  ASSIGNMENT-1 APPLICATIONS:  the 4 questions
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[CLOSING SECTION (after Q28; usually the summary card)]
──────────────────────────────────────────────────────────────────────────────

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
