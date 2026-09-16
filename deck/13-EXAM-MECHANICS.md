# 13 EXAM MECHANICS: format, marks, time, scoring

## 1. The format

```
  paper       MAS2001 Statistics and Probability mid term
  marks       30 total
  scope       lectures 1 to 21
  sections    A MCQ, B short answers, C longer. All compulsory (no choice).
  closed book no formula sheet allowed, so the sheet in 01-CHEATSHEET must be memorised
  time        budget 90 minutes as the working assumption; confirm from the paper header
```

The exact section split and the per-question marks are on the two MTE papers we hold
(md/paper-mte-2024-25/ and md/paper-mte-2025-26/ plus their schemes). Read the schemes: they
show where the red-pen marks are allocated, which tells you what earns a mark (a stated formula,
a correct substitution) vs what does not (a bare number).

## 2. The time budget (90 minutes, 30 marks)

```
  reading the whole paper first                          3 min
  Section A, MCQs, fast, no long working, ~1.5 min each  ~20 min
  Section B, short answers, show the two-line setup      ~35 min
  Section C, the estimator/composite question            ~25 min
  check and sweep for missed parts                       7 min
```

Rule: the estimator-comparison question is the standard 6 to 8 mark item. Budget for it, do
not leave it starved by the MCQs.

## 3. What earns marks (from the schemes)

```
  DO
    state the distribution and its parameters before computing: "X ~ B(12, 0.1)"
    write the formula you are using on its own line, then substitute
    keep exact values, round only the final answer
    for a "show that" write every algebra step, the marks are on the steps
    for a comparison, name the winner and give the reason ("smallest variance among unbiased")
    for Chebyshev, when the distribution is known, give BOTH the bound and the exact value
  DO NOT
    drop a bare number with no setup (loses the method marks)
    use the wrong sign in F(b) - F(a-1)
    forget to convert z back to the X scale in an inverse question
    round early and carry the rounded value
    write "0.549" when the exact value is 0.5499 and it was asked to 4 places
```

## 4. Section-by-section tactics

```
  Section A (MCQ)
    read the boundary word (at least / more than) twice, it decides the option
    if two options differ only by sign, you have made a sign error somewhere, recheck
    "which is NOT" / "which is false" questions: test each option, do not guess
    Chebyshev applicability MCQs: the answer is "no distribution needed"

  Section B (short)
    one question per topic, so identify the distribution fast and go
    the setup line is worth a mark even if the arithmetic slips
    for "find k" always show the normalisation equation

  Section C (long)
    this is the estimator comparison or a composite. Follow the part chain.
    unbiased first (E of each), then variances of the survivors, then the winner.
    for a composite (Poisson then binomial), do the inner model, then the outer.
```

## 5. The last-hour checklist

```
  1  read 01-CHEATSHEET once, aloud, slowly
  2  write the five distributions' mean/variance from memory
  3  write the three Chebyshev thresholds (3/4, 8/9, 15/16)
  4  write the hidden set: memoryless, landmarks, N x P, 1/p, nK/N
  5  read the 10-item trap list (08-TRAPS, part 2 end)
  6  no new material, nothing below lecture 22, do not touch MLE or MoM
```

## 6. The confidence notes (honest)

```
  strongest: the five distributions' moments and pmf/pdf, binomial and Poisson point/tail,
             normal and CLT numerics, the estimator comparison
  medium:    Chebyshev inverse, two-unknown normal, exponential conditional, composition
  watch:     the hidden set (H1-H8) if not drilled, the min-n siblings, MSE comparison
  the paper's own MTE skeletons (15 of 16 traced) are the safest bet: those patterns repeat
```

## 7. Sources this deck draws on (all in the repo)

```
  reports/03-FORMULA-SHEET.md    the verified closed forms
  reports/04-QUESTION-BANK.md    the worked answers
  reports/09-ERRATA.md           all 21 source errata
  reports/16,17,18,19,20         provenance, intake, accounting, cross-check, skeleton ledger
  reports/11-QUESTION-ATLAS/     topic universe, learn order, type space, mutation analysis
  md/                            the converted slides and papers
  ~/mas2001-devore/corpus-text/  the batch-2 deck texts and the OCR of the external books
```
