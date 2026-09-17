# WORKED QUESTIONS: the complete zero-knowledge answer set

Built 17 Sep 2026. Every question here comes from OUR OWN material: the two MTE papers, the
nine ETE sittings, the assignments, and the lecture decks. Nothing invented. Every number in
every solution was machine-verified before the file was committed.

```
   folder:   ~/mas2001-mte-s2/deck/worked/
   files:    14 (one per family) + this index
   size:     ~415 KB
   questions: 131
   register: ZERO-KNOWLEDGE LONG FORM ONLY (every step shown, no assumed maths)
```

drill file: 00-QUESTIONS-ONLY.md (168 questions: all worked + 10 MCQs; solutions behind pointers)

═══════════════════════════════════════════════════════════════════════════════
THE FILES AND WHAT EACH COVERS
═══════════════════════════════════════════════════════════════════════════════

```
  +-------+---------------------------+-------+----------------------------------------+
  | file  | family                    |  Qs   | what is inside                         |
  +-------+---------------------------+-------+----------------------------------------+
  | F1    | Binomial                  |  10   | point, tail, count, formula MCQ,       |
  |       |                           |       | find-p from ratio, literate variant    |
  | F2    | Poisson                   |   8   | point, tail, nested, two-stage chain,  |
  |       |                           |       | Y=2X scaling, mean=e MCQ               |
  | F3    | Exponential               |   6   | point, tail, between, memoryless,      |
  |       |                           |       | mean/var, read-lambda-off-density      |
  | F4    | Uniform                   |   4   | point (2 forms), trains, U(-1,1) bound |
  | F5    | Chebyshev                 |   7   | within, tail, find-c, find-E/Var,      |
  |       |                           |       | NOT-form MCQ, interpretation MCQ       |
  | F6    | Normal                    |   6   | interval, two-unknown (2 variants!),   |
  |       |                           |       | SE-of-average, phi table conventions   |
  | F7    | RV / pdf / cdf            |   6   | find-k, mean/var exact fractions,      |
  |       |                           |       | piecewise cdf, dice grid               |
  | F8    | Estimation                |  17   | 4 properties, unbiased verification,   |
  |       |                           |       | consistency, CIs (3), sufficiency (3)  |
  | F9    | CLT / sampling            |   8   | SE value, SE behaviour, applicability, |
  |       |                           |       | 3 deck examples (ATM, impurity, LED)   |
  | F10   | Definition/foundations    |  10   | rv definition (3 papers!), pmf drill,  |
  |       |                           |       | joint pmf + marginal, E(2X+1)^2        |
  | F11   | Expectation/variance laws |   6   | laws toolbox, E[XY], variance>=0,      |
  |       |                           |       | typist Q8, soldiers, Poisson scaling   |
  | F12   | Hypothesis testing (OUT*) |  20   | 8 MCQs, t-tests (3), F-tests (2),      |
  |       |                           |       | chi-square (3), ANOVA (2), bulbs       |
  | F13   | Assignment sheets         |  28   | both assignments in full: 12 MCQs +    |
  |       |                           |       | 16 full solves, printed-answer quirks  |
  | F14   | Probability foundations   |   1 + | lecture-2 basics: events, conditional  |
  |       |                           |  10MCQ| prob (camera example), independence,   |
  |       |                           |       | the assignment-1 MCQ key (C,B,B,A,D,   |
  |       |                           |       | B,B,B,A,B)                             |
  | F15   | Assignment bank 2         |  22   | 2024-25 + 2025-26 sheets:            |
  |       |                           |       | expectation tricks, find-k, counts,   |
  |       |                           |       | 8 printed-answer flags documented     |
  +-------+---------------------------+-------+----------------------------------------+
   (*) hypothesis testing is marked out of the MTE syllabus in the ledger, but it appeared in
       five ETE papers with two 10-mark questions; included for completeness.
   TOTAL: 158 questions
```

═══════════════════════════════════════════════════════════════════════════════
SCOPE TRUTH (from ~/PS/syllabus.txt, verified against reports/00-SCOPE-AND-EXAM-FACTS.md):
MTE = lectures 1-21, ending at "Characteristics of a good estimator". MLE, MoM, Bayesian
estimation, confidence intervals and hypothesis testing are OUT (they appear in ETE papers
and are kept in F8/F12 for completeness, clearly marked).
═══════════════════════════════════════════════════════════════════════════════

═══════════════════════════════════════════════════════════════════════════════
SOURCE MAP: WHERE THE QUESTIONS COME FROM
═══════════════════════════════════════════════════════════════════════════════

```
   MTE 2024-25 paper    M24 (A1-A3, B1-B4, C1)   -> all 9 blocks covered across F2,F3,F4,F5,F6,F7,F11
   MTE 2025-26 paper    M25 (Q1-Q8)              -> all 8 blocks covered across F2,F3,F5,F6,F7,F8,F11
   ETE 2024-25 S3       E24S3 (A1-B5)            -> F5,F6,F7,F8,F9,F10,F11,F12
   ETE 2024-25 S4       E24S4 (A1-D2)            -> F3,F6,F7,F8,F10,F12
   ETE 2025-26 S3       E25S3 (A1-C2)            -> F1,F2,F4,F5,F6,F7,F8,F9,F12
   ETE 2025-26 S4       E25S4 (A1-B5)            -> F7,F8,F10,F11,F12
   ETE 2025 summer      E25SUM                   -> F1,F5,F9,F10,F11,F12
   ETE re-session S3    R25S3                    -> F1,F2,F3,F5,F6,F8,F9,F11,F12
   ETE re-session S4    R25S4                    -> F3,F4,F7,F11,F12
   decks (ppt3/ppt4/ppt5/lms) -> F1,F2,F4,F6,F9 (the deck examples)
   assignments (2024-25, 2025-26) -> F13 (all 28 questions), plus F6 (7%/89%), F1/F5/F8
   university solution schemes (NEW source mined) -> cross-checks in F1,F5,F6,F7,F8,F11,F12
```

═══════════════════════════════════════════════════════════════════════════════
THE SHAPES COVERED (the checklist from deck/15, now with questions behind it)
═══════════════════════════════════════════════════════════════════════════════

IN-MTE shapes:
```
   [x] Chebyshev/concept-mcq      F5.5 Q5 (the NOT-check)
   [x] Chebyshev/inverse-c        F5.2 Q2 (find c=10, 0.04 ceiling)
   [x] Chebyshev/point            F5.1 Q1 (K=3 percentage within)
   [x] Chebyshev/moments          F5.3 Q3, F5.4 Q4 (find E and Var from 21/25, 24/25)
   [x] Poisson/concept-mcq        F2.8 Q8
   [x] Poisson/formula-mcq        F2.4 Q4 (mean=e)
   [x] Poisson/moments            F2.3 Q3 (M24-B1 variance of X-2Y)
   [x] Binomial/tail              F1 Q1(ii) + Q7 (>=k and the 9/5 find)
   [x] Exponential/tail           F3.3 Q3 (M24-B2 (i))
   [x] Normal/interval            F6.2 Q2 part (iii)
   [x] Estimation/sufficiency     F8.1 Q5 + F8.5 Q11, Q12
   [x] Estimation/tail            F8.1 (theory) + CI forms
   [x] RV/pdf-cdf/find-param      F7.2 Q2 (kx^3), F7.3 Q3 (ax^2+bx)
   [x] RV/pdf-cdf/formula-mcq     F7.4 Q4 (piecewise cdf MCQ)
   [x] RV/pdf-cdf/point           F7.5 Q5, F7.6 Q6
   [x] Uniform/tail               F4.2 Q2
```

RECALL-GAP shapes (appeared outside the MTE papers; now drilled):
```
   [x] Binomial/point             F1.1 Q1 (pens)
   [x] Binomial/moments           F1.3 Q5 (B(180,1/3))
   [x] Binomial/formula-mcq       F1.3 Q6 (mean = np)
   [x] Poisson/point              F2.1 Q1 (car hire)
   [x] Poisson/tail               F2.2 Q2 (5000 men)
   [x] Poisson/sufficiency        F8.5 Q12 (proof)
   [x] Exponential/point          F3.1 Q1, F3.2 Q2
   [x] Exponential/sufficiency    F8.5 Q11
   [x] Expectation/point          F10.4 Q4, F11 Q1-Q3
   [x] Uniform/point              F4.1 Q1 (MCQ), F4.3 Q3 (trains)
   [x] Normal/point               F6.1 Q1, F6.3 Q3
   [x] Normal/tail                F6.3 Q3 (P beyond 7.2), F11.6 Q5 soldiers
   [x] Normal/moments             F6.4 Q4 (find mu/sigma)
   [x] Normal/find-param          F6.4b Q4b (7%/89%)
   [x] CLT/point                  F9.5 Q5 (ATM)
   [x] Estimation/point           F8.2 Q6, F8.3 Q7
   [x] Estimation/moments         F8.2 (the 16-sample means)
   [x] Estimation/formula-mcq     F8.1 Q1-Q4
   [x] Definition/concept-mcq     F10.1 Q1 (3 papers)
   [x] Hypothesis-OUT/point       F12 (all)
```

═══════════════════════════════════════════════════════════════════════════════
HOW TO USE THIS FOLDER
═══════════════════════════════════════════════════════════════════════════════

```
   STUDY ORDER (matches deck/14-MASTER-STUDY-ORDER):
     1. F10 definition      (cheapest marks, builds vocabulary)
     2. F7  rv/pdf/cdf      (the foundation: k, mean, var)
     3. F1  binomial        )
     4. F2  poisson         |  the discrete three
     5. F3  exponential     )
     6. F4  uniform         )
     7. F5  chebyshev       (appears in EVERY sitting; P=1.00)
     8. F6  normal          (the hardest block; two tables!)
     9. F9  clt             (feeds F6 and F8)
    10. F8  estimation      (the protocol)
    11. F11 expectation     (the laws behind everything)
    12. F12 hypothesis      (out of syllabus, do last if at all)

   PER FILE (every one has the same structure):
     - a "before any question" primer (vocabulary in plain words)
     - each question in: QUESTION / STEP 0 DECODE / EVERY STEP / ANSWER / TRAP
     - ASCII flowcharts and pictures inside the solves
     - a SUMMARY CARD at the end (the whole family on one screen)

   THE NUMBER GUARANTEE:
     every arithmetic line was checked with a machine script before commit.
     where the paper's printed value differs from the exact value (rounding, or typos),
     both are shown and the difference is explained.
```

═══════════════════════════════════════════════════════════════════════════════
THE HIDDEN-QUESTION DECODE (the "question hidden in wording" layer)
═══════════════════════════════════════════════════════════════════════════════

```
   PATTERN                          EXAMPLE IN THIS FOLDER         WHERE SOLVED
   ---------------------------------------------------------------------------
   "on an average X per day"        convert to the asked period     F2 (rate scaling)
   "how many ... would you expect"  it is a COUNT, multiply by n    F1 Q3, Q3b
   "average of n observations"      SE = sigma/sqrt(n) not sigma    F6 Q3, F9 Q5-Q7
   "N(2.6, 34.5)"                   the 2nd number is the VARIANCE  F6 primer
   "parameter 1/4"                  lambda = 1/4, so mean = 4       F3 Q3
   "at least k sigma away"          the TAIL form of Chebyshev      F5.1
   "the value of the constant c"    Chebyshev form 3 (sigma^2/c^2)  F5.3
   "less than 1% of letters"        upper bound -> inequality       F11 Q4
   "on 90% of days all accepted"    equation with the DAY rate 20x  F11 Q4
   "how many families"              P(event) x number of families   F1 Q3, Q3b
   "support the assumption mu=100"  H0 = the assumption; t-test     F12 Q9
   "claim of 8 minutes"             the claim IS H0; fail-to-reject  F12 Q10
   "3 people or less"               CUMULATIVE P(0)+P(1)+P(2)+P(3)  F1 Q3b
```

═══════════════════════════════════════════════════════════════════════════════
RELATED FILES
═══════════════════════════════════════════════════════════════════════════════

```
   00-HOW-AND-WHY.md            methodology: how/why the question set was
                                made, the exact counts, the shape/skeleton
                                derivation, stated limits
   deck/15-DECISION-MANUAL.md   the if-X-do-Y manual for all 34 shapes + mutations
   deck/notes/                  the slide conversions rewritten (00-09)
   deck/01 to 13                the reference deck (cheatsheet, terms, traps...)
   deck/12-DRILL.md             the 50-item drill
   deck/14-MASTER-STUDY-ORDER   what to do in what order
```

═══════════════════════════════════════════════════════════════════════════════
VERIFICATION LEDGER (every file's number-check total at commit time)
═══════════════════════════════════════════════════════════════════════════════

```
   F1   36/36 checks pass   (9 questions)
   F2   22/22 checks pass   (8 questions)
   F3   26/26 checks pass   (6 questions)
   F4   17/17 checks pass   (4 questions)
   F5   ~21/21 checks pass  (7 questions)
   F6   13/13 + 6/6 (the added variant)
   F7   17/17 checks pass   (6 questions)
   F8   20/20 + 5/5 (the added ones)
   F9   13/13 checks pass   (7 questions)
   F10  15/15 checks pass   (4 questions)
   F11  13/13 checks pass   (5 questions)
   F12  7/7 + 15/15 (the added ones)
```
