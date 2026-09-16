# 13 EXAM MECHANICS: format, marks, time, scoring

## 1. The format

```
   ┌───────────────────────────────────────────────────────┐
   │  MAS2001 Statistics and Probability, MID TERM         │
   │                                                        │
   │    marks    30                                        │
   │    scope    lectures 1 to 21                          │
   │    sections A (MCQ)  B (short)  C (long)               │
   │    ALL compulsory, no choice                          │
   │    CLOSED BOOK, no formula sheet                       │
   └───────────────────────────────────────────────────────┘
```

## 2. The time budget (90 minutes, 30 marks)

```
   0 min ────┐
             │ read the whole paper first          3 min
   3 min ────┤
             │ Section A  (MCQs, ~1.5 min each)   20 min
  23 min ────┤
             │ Section B  (short, show the setup) 35 min
  58 min ────┤
             │ Section C  (the estimator/comp)    25 min
  83 min ────┤
             │ check and sweep for missed parts    7 min
  90 min ────┘

   RULE: the estimator-comparison question is the standard
   6-to-8 mark item. Budget for it. Do not let the MCQs starve it.
```

## 3. What earns marks (from the schemes)

```
   DO                                    DO NOT
   ─────────────────────────────────     ──────────────────────────────
   state "X ~ B(12, 0.1)" first          drop a bare number
   write the formula on its own line     forget z -> X conversion
   keep exact values to the end          round early and carry it
   for "show that", every algebra step   write 0.549 for 0.5499
   for comparisons, name the winner      compare a BIASED estimator's
     AND the reason                        variance against unbiased
   Chebyshev: bound AND exact value       mix phi and F table conventions
```

## 4. Section tactics as a tree

```
   ┌──────────────── SECTION A (MCQ) ────────────────┐
   │ read the BOUNDARY word twice (at least/more)     │
   │ two options differ only by sign -> you erred     │
   │ "which is NOT" -> test each option               │
   │ Chebyshev applicability -> "no distribution"     │
   └───────────────────────┬──────────────────────────┘
                           ▼
   ┌──────────────── SECTION B (short) ───────────────┐
   │ one question per topic, identify the dist fast    │
   │ the SETUP line is worth a mark even if arithmetic │
   │   slips                                           │
   │ "find k" -> always show the normalisation eq      │
   └───────────────────────┬──────────────────────────┘
                           ▼
   ┌──────────────── SECTION C (long) ────────────────┐
   │ estimator comparison OR a composite               │
   │   1. unbiased first (compute E of each)           │
   │   2. then variances of the SURVIVORS              │
   │   3. then name the winner                         │
   │ composite: do the INNER model first               │
   └───────────────────────────────────────────────────┘
```

## 5. The last-hour checklist

```
   ┌──┐ 1. read 01-CHEATSHEET once, aloud, slowly
   ├──┤ 2. write the five distributions' mean/variance from memory
   ├──┤ 3. write the three Chebyshev thresholds: 3/4, 8/9, 15/16
   ├──┤ 4. write the hidden set: memoryless, landmarks, N x P, 1/p, nK/N
   ├──┤ 5. read the 10-item trap list
   └──┘ 6. no new material. nothing below lecture 22. no MLE, no MoM.
```

## 6. Confidence map (honest)

```
   STRONGEST  ████████████████████  five dists' moments, binomial/Poisson
                                   point+tail, normal/CLT numerics,
                                   estimator comparison
   MEDIUM     ██████████████        Chebyshev inverse, two-unknown normal,
                                   exponential conditional, composition
   WATCH      ████████              the hidden set H1-H8 if not drilled,
                                   min-n siblings, MSE comparison
   SAFEST BET ████████████████████  the MTE paper skeletons (15 of 16
                                   traced): those patterns REPEAT
```

## 7. Sources this deck draws on (all in the repo)

```
   reports/03-FORMULA-SHEET.md    the verified closed forms
   reports/04-QUESTION-BANK.md    the worked answers
   reports/09-ERRATA.md           all 21 source errata
   reports/16,17,18,19,20         provenance, intake, accounting, cross-check
   reports/11-QUESTION-ATLAS/     topic universe, learn order, type space, mutations
   md/                            the converted slides and papers
   ~/mas2001-devore/corpus-text/  the batch-2 deck texts and the OCR books
```

## 8. The deck folder map, one more time

```
   ~/mas2001-mte-s2/deck/
   ┌──────────────────────────────────────────────────────┐
   │ README.md          the folder map                     │
   │ 00-INDEX.md        the exam, the tree, the order      │
   │ 01-CHEATSHEET.md   the whole paper in formulas        │
   │ 02-TERMS.md        every term + its trap              │
   │ 03-LINGUISTICS.md  wording -> ask -> move             │
   │ 04-METHODS.md      method per question type           │
   │ 05-DISTRIBUTIONS.md 5 dists, 9 slots                  │
   │ 06-NUMBERS.md      every constant                     │
   │ 07-PATTERNS.md     the mutation system                │
   │ 08-TRAPS.md        20 traps + 21 errata               │
   │ 09-QUESTIONS.md    the tagged inventory               │
   │ 10-SLIDE-MAP.md    page -> topic -> question          │
   │ 11-BEYOND-SLIDES.md  the 8 hidden items               │
   │ 12-DRILL.md        50 practice items                  │
   │ 13-EXAM-MECHANICS.md  this file                       │
   ├──────────────────────────────────────────────────────┤
   │ notes/             THE ACTUAL NOTES (11 files)        │
   │   00-NOTES-INDEX   the map                            │
   │   01..10           lecture-by-lecture teaching notes  │
   └──────────────────────────────────────────────────────┘
```
