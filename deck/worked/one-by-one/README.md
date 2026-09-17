# ONE-BY-ONE: every question its own file

Built 17 Sep 2026, audited same day. 196 files (180 question files + 15 family guides + this README): every question from the worked set as its own
file, PLUS a 00-GUIDE.md per family carrying the non-question explanation content
(toolboxes, decision trees, summary cards) so the folder is lossless vs the family files.
Format per question file: PART 1 = the question alone. PART 2 = the full answer from zero
(every step, nothing assumed, all the ASCII visuals). Split mechanically from the
family files, so nothing is lost: each file carries the same content as its block
in the parent F-file.

═══════════════════════════════════════════════════════════════════════════════
FOLDER MAP (180 files)
═══════════════════════════════════════════════════════════════════════════════

```
  folder                    files   what is inside
  ──────────────────────────────────────────────────────────────────────────
  F1-binomial/               10     point, tail, count, moments, mcq,
                                    find-p, ratio, literate variant, 7b
  F2-poisson/                 8     point, tail, nesting, chain, scaling,
                                    recovery, mcqs, the 5000-men
  F3-exponential/             6     tails, between, memoryless, formula,
                                    lambda-off-density, moments
  F4-uniform/                 4     story wait-time, clipping, U(-1,1)
  F5-chebyshev/               7     within, find-c, inverse, NOT-mcq,
                                    interpretation, bound-vs-actual
  F6-normal/                  6     interval, two-unknown x2, SE-of-average,
                                    inverse drill, mcq
  F7-rv-pdf-cdf/              6     find-k, mean/var fractions, piecewise cdf,
                                    dice grid, pdf-from-cdf
  F8-estimation/             17     unbiased, consistency, sufficiency x3,
                                    CIs, MLE-mcq, estimators, t^2 bias
  F9-clt-sampling/            8     SE value, applicability, deck examples
  F10-rv-foundations/        10     rv definition, pmf drills, joint pmf,
                                    lecture-deck drills
  F11-expectation/            6     laws, scaling, typist, soldiers
  F12-hypothesis-out/        20     MCQs + t/F/chi2/ANOVA (OUT of MTE, kept)
  F13-assignment/            40     28 full solves + 12 Section-A MCQs
  F14-prob-basics/           11     camera example + M1-M10 MCQs
  F15-assignment-bank2/      21     the 2024-25/2025-26 sheet questions
  ──────────────────────────────────────────────────────────────────────────
  TOTAL                     180
```

Naming: `qNN.md` = a full worked question (NN in the same order as the parent
file). `mcqNN.md` / `mNN.md` = concept MCQs from a table.

═══════════════════════════════════════════════════════════════════════════════
HOW TO USE
═══════════════════════════════════════════════════════════════════════════════

```
  DRILL MODE (recommended):
     1. open 00-QUESTIONS-ONLY.md, pick a question cold
     2. attempt it with pen and paper
     3. then open this folder's matching file: read PART 1 (confirm the ask),
        then PART 2 (the full answer from zero) and compare with your attempt
     4. if the numbers differ, the parent F-file's TRAP section shows the
        near-miss that usually causes it

  READ MODE:
     just read the files in family order (F1, F2, F3, ...). each is
     self-contained: question, decode, steps, answer, check, traps.

  EXAM-EVE MODE:
     F5 (chebyshev), F2 (poisson), F3 (exponential) = the three that
     appear in BOTH MTE papers. then F6 Q2 (the composite).
```

═══════════════════════════════════════════════════════════════════════════════
WHAT IS NOT HERE
═══════════════════════════════════════════════════════════════════════════════

```
  - the two "pointer-only" blocks (F8-11b, F15-19) were cross-references,
    not questions; their content lives inside the files they point to
    (F8 estimation q05, F13 assignment q08).
  - the shape checklists and methodology: see ../00-INDEX.md and
    ../00-HOW-AND-WHY.md in the parent folder.
```

═══════════════════════════════════════════════════════════════════════════════
VERIFICATION
═══════════════════════════════════════════════════════════════════════════════

```
  split date    17 Sep 2026, from the corrected working tree
  files         180 (158 worked blocks + 22 MCQs from tables)
  size          ~850 KB
  scan          no em dashes, no banned words (checked at build)
  content       each file = its parent block verbatim (PART 1 question,
                PART 2 answer) plus a header card. nothing invented.
```
