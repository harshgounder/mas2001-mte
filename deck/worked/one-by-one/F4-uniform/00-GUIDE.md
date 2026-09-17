# F4-uniform GUIDE: the explanation content behind the questions

This is the non-question content from the family file: the family intro, the
toolboxes, the section intros, decision trees, and the summary card. It is the
TEACHING layer. Read it first (it gives the method), then drill the q*.md files.

Source: deck/worked/F4-uniform.md (same content; this file just isolates it).


──────────────────────────────────────────────────────────────────────────────
[FAMILY INTRO / PREAMBLE (before the first question)]
──────────────────────────────────────────────────────────────────────────────

# F4 UNIFORM: every shape, every question, solved from zero

Source: our own material (MTE 2024-25 blocks B3 and B4, the ETE papers E25S4, and the ppt4
deck). Nothing invented. Every number machine-checked (6/6 checks pass).

```
  SHAPES IN THIS FILE
  F4.1  pdf + moments MCQ      name the mean                    1 question
  F4.2  length-ratio point     P(a<X<b)                         1 question (MTE!)
  F4.3  wait-time application  the trains question               1 question (MTE!)
  F4.4  composite with Chebyshev  bound vs actual                1 question (MTE!)
```

═══════════════════════════════════════════════════════════════════════════════
BEFORE ANY QUESTION: what "uniform" means
═══════════════════════════════════════════════════════════════════════════════

Uniform means EVERY VALUE IN THE RANGE IS EQUALLY LIKELY. The picture is a flat rectangle.

```
   +-------------------------------------------------------------------+
   |  X between a and b, written U(a, b):                                |
   |                                                                     |
   |     pdf     f(x) = 1 / (b - a)        for a <= x <= b               |
   |     MEAN    (a + b) / 2                                             |
   |     VARIANCE (b - a)^2 / 12                                         |
   |                                                                     |
   |  THE KEY IDEA: probability = LENGTH RATIO                           |
   |                                                                     |
   |            length of the part you want                              |
   |   P  =  ---------------------------------                           |
   |            length of the whole range                                |
   +-------------------------------------------------------------------+
```

THE PICTURE:

```
   f(x)
   1/(b-a) |######################|     flat top
           |######################|
           |######################|
           +-----[a==========b]---+
                 the rectangle. area = height x width = 1/(b-a) x (b-a) = 1 ✓

   asking P(c < X < d):
   1/(b-a) |      +########+      |
           |      +########+      |
           +------[c########d]----+-----+
                  the shaded piece. its width is (d-c).
                  probability = (d - c) / (b - a)
```

THE CLIPPING RULE (draw the rectangle every time to avoid this):

```
   +--------------------------------------------------------------+
   |  the part you want must be CLIPPED to the range.              |
   |                                                               |
   |  U(2,6), ask P(1 < X < 5):                                    |
   |     the part starts at 1, but the range starts at 2, so        |
   |     use 2, not 1: length = 5 - 2 = 3                          |
   |                                                               |
   |  U(2,6), ask P(X > 7):                                        |
   |     7 is outside the range, so this is impossible: P = 0      |
   +--------------------------------------------------------------+
```

═══════════════════════════════════════════════════════════════════════════════
F4.1  MOMENTS MCQ:  name the mean
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q1 and Q2)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F4.2  LENGTH-RATIO POINT
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q2 and Q3)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F4.3  WAIT-TIME APPLICATION:  the trains question
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[SECTION INTRO (between Q3 and Q4)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F4.4  COMPOSITE:  Uniform + Chebyshev  (bound vs actual)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


──────────────────────────────────────────────────────────────────────────────
[CLOSING SECTION (after Q4; usually the summary card)]
──────────────────────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════════════════════
F4 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   U(a,b):  f = 1/(b-a) | MEAN = (a+b)/2 | VAR = (b-a)^2/12 (so sd = (b-a)/sqrt(12))

   THE ONE IDEA: probability = LENGTH RATIO = (wanted length) / (b - a)

   CLIPPING: whatever you want must sit INSIDE [a,b].
        ask below a  -> start at a
        ask above b  -> end at b
        ask fully outside -> probability 0

   |X| FORMS:  P(|X - c| < d) = P(c-d < X < c+d), then clip.

   STORY PATTERN (trains, buses):  the WAIT is uniform on (0, interval-between-arrivals).
        the arrival window in the story is FLAVOUR, not the range.

   COMPOSITE: bound vs actual -> answer BOTH. read the support before integrating;
        sometimes the actual is 0 by inspection.

   TOP TRAPS:
     not clipping
     using the story's window instead of the wait's range
     skipping the "Also" half of a bound-vs-actual question
     mixing up (a+b)/2 (mean) with (b-a)/2 (half-width)
```
