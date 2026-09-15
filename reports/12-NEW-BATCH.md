# New batch inventory and processing queue

Listed 15 September 2026. 23 files in ~/PS, all catalogued. Processing: one unit at a
time, 10-20 pages per unit, nothing skipped.

## 1. THE LIST

### A. Papers (13 files) - highest value (they show what is actually asked)

```
  #   file                                              pages  notes
  A1  S&P_MTE_Sem-3_2025-2026.pdf                          3   THIS year MTE (Sep 17 2025). Readable.
  A2  S&P_MTE_Sem-3_2025-2026solutionscheme.pdf            4   mark scheme. SCAN-HEAVY: needs vision pass
  A3  S&P_MTE_Sem-3_2024-2025.pdf                          2   last year MTE. Readable.
  A4  S&P_MTE_Sem-3_2024-2025solutions-scheme-...pdf       6   mark scheme + "how marks were given". SCAN-HEAVY: vision
  A5  S&P_ETE_Sem-3_2025-26.pdf                            2   ETE Nov 2025
  A6  S&P_ETE_Sem-3_2024-25.pdf                            2   ETE Nov 2024
  A7  S&P_ETE_Sem-4_2024-25.pdf                            2   ETE sem4 variant
  A8  S&P_ETE_Sem-4_2025-26_mujstella.pdf                  3   ETE sem4 variant
  A9  S&P_ETE_Summer_2025-26_mujstella.pdf                 2   summer ETE
  A10 S&P_Re-sess_Sem-3_2025-26.pdf                        2   re-sessional Nov 2025
  A11 S&P_Re-sess_Sem-4_2025-26_mujstella.pdf              2   re-sess variant
  (A5-A11 readable; watermark noise filtered in analysis)
```

### B. Assignments (11 files) - this year's set is new

```
  B1  2025-2026-S&P_assignments_1-5.pdf                   17   THIS year, combined 1-5
                                                               sections: A memory MCQ, B concept,
                                                               C analytical, D application
  B2  2024-2025-Assignment 1.pdf                           2
  B3  2024-2025-Assignment 2.pdf                           2
  B4  2024-2025-Assignment 3.pdf                           3
  B5  2024-2025-Assignment 3 Episode 2.pdf                 2   *** IMAGE-ONLY (240 chars): vision pass ***
  B6  2024-2025-Assignment 4.pdf                           3
  B7  2024-2025-Assignment 5.pdf                           3
```

### C. Decks (5 files) - the reorganized course decks

```
  C1  S&P L1-7.pdf                                       108   units 1-2 block (probability, rv,
                                                               pmf/cdf, expectation, variance)
                                                               fingerprint: PARTIAL overlap with old
                                                               147pp deck (~29 pages match; rest needs
                                                               page-level check during processing)
  C2  S&P L8-9.pdf                                        37   expectation + independent rvs
                                                               fingerprint: mostly unmatched vs old
                                                               (new organization/content mix)
  C3  S&P L10-11 Chebyshev's inequality.pdf                9   *** THE CHEBYSHEV DECK ***
                                                               theorem, k-sigma form, complement, 2 worked Qs
  C4  S&P L12-13 Discrete Probability Distribution.pdf    28   binomial + poisson
                                                               fingerprint: 22/28 pages match ppt3 (dup-ish)
  C5  S&P L14-15 Continuous Probability Distribution.pdf  44   uniform/normal/exponential
                                                               fingerprint: 39/45 pages match ppt4 (dup-ish)
```

## 2. WHAT IS GENUINELY NEW (first-pass verdict)

```
  CERTAINLY NEW:
    - the Chebyshev deck (C3) - the old batch had NO Chebyshev slides at all
    - both MTE papers + BOTH SOLUTION SCHEMES (never seen)
    - all ETE and re-sess papers (never seen)
    - 2025-26 assignments 1-5 (this year's set)
    - 2024-25 assignments 1-5 + Episode 2 (last year's set)
  NEW ORGANIZATION / CONTENT MIX (verify page by page during processing):
    - L1-7, L8-9 (may contain re-arranged + updated versions of old material)
  MOSTLY DUPLICATE OF OLD DECKS (verify during processing):
    - L12-13 (~79 percent pages match ppt3)
    - L14-15 (~87 percent pages match ppt4)
  the dedup pass used text fingerprints; final verdict per page happens in processing
```

## 3. PROCESSING QUEUE (one unit at a time, 10-20 pages per unit)

```
  UNIT   content                                              pages  status
  U01    A1+A2+A3+A4: both MTE papers + both schemes           15    NEXT
  U02    A5+A6+A10: ETE S3 x2 + re-sess S3                    6     queued
  U03    A7+A8+A9+A11: ETE S4 x2 + summer + re-sess S4        9     queued
  U04    B1: 2025-26 assignments 1-5 combined                 17    queued
  U05    B2..B7: 2024-25 assignments + Episode 2              15    queued
  U06    C3: Chebyshev deck                                    9     queued (critical)
  U07    C4 part 1: L12-13 p1-15                              15    queued
  U08    C4 part 2: L12-13 p16-28                             13    queued
  U09    C5 part 1: L14-15 p1-15                              15    queued
  U10    C5 part 2: L14-15 p16-30                             15    queued
  U11    C5 part 3: L14-15 p31-44                             14    queued
  U12    C2 part 1: L8-9 p1-19                                19    queued
  U13    C2 part 2: L8-9 p20-37                               18    queued
  U14    C1 part 1: L1-7 p1-18                                18    queued
  U15    C1 part 2: L1-7 p19-36                               18    queued
  U16    C1 part 3: L1-7 p37-54                               18    queued
  U17    C1 part 4: L1-7 p55-72                               18    queued
  U18    C1 part 5: L1-7 p73-90                               18    queued
  U19    C1 part 6: L1-7 p91-108                              18    queued
  total pages: 283 | 19 units
```

## 4. Per-unit protocol (so nothing is missed)

```
  for each unit, every page:
    1  read the page (text layer; vision pass for the flagged scan-heavy files)
    2  every question/example on it -> entry (type, subtype, approach, steps, knowledge,
       intent, taxonomies per the framework file)
    3  every page gets a dedup verdict vs the existing corpus: NEW / DUPLICATE / UPDATED
    4  count questions, update the running register
    5  record: unit summary + anything odd (errata, watermark traps, ambiguities)
  after each unit: append to reports/13-NEW-BATCH-PROCESSING.md, commit
```

## 5. Known quality traps

```
  - mujstella watermark fragments pollute every pdf's text layer (must be filtered)
  - A2, A4 are scan-heavy: text layer sparse, vision pass mandatory for marking detail
  - B5 (Episode 2) is image-only: vision pass mandatory
  - the MTE 2025-26 paper text layer has re-ordered fragments (about:srcdoc artifacts):
    careful page-order reading needed, not raw grep
```

## 6. Scout findings (from the v1 scout, folded in here)

The first read already established these. Kept because they change prior conclusions.

```
  CHEBYSHEV HAS SLIDES AFTER ALL (the old "zero slides" claim was old-batch only):
    C3 (L10-11) carries the theorem, the k-sigma restatement, the complement form and
    two worked questions. Its Q2 (mu=10, sigma^2=4, find C with P(|X-10|>=C)<=0.04)
    is literally MTE 2025-26 Q5, same numbers. The deck is the source.

  PAPERS CONFIRM SIBLINGS (14 items previously flagged "not asked" that ARE asked):
    Var(X-2Y) via independent Poissons .............. MTE 2024-25 B1
    E(XY)=E(X)E(Y) MCQ ............................... Re-sess 2025-26 QA1
    Chebyshev find-C inverse ......................... MTE 2025-26 Q5 + C3 Q2
    Chebyshev bound vs actual probability ............ MTE 2024-25 B3
    exponential interval P(a<T<b) .................... MTE 2024-25 B2
    uniform wait-time story (train) .................. MTE 2024-25 B4
    normal sample-mean n=9 (exact normal) ............ MTE 2025-26 Q7
    sufficiency concept MCQ .......................... MTE 2025-26 A3
    consistency with bias formula .................... Re-sess 2025-26 QA2
    SE direction MCQ ................................. Re-sess 2025-26 QA3
    Chebyshev statement-spotting MCQ ................. MTE 2024-25 QA3
    k from E(X), E(X^2) first ........................ C3 Q1 style
    Var(2X-5Y) linear combination .................... 2025-26 assignment Q11
    exponential mean/var in one problem .............. MTE 2024-25 B2

  EXAM FORMAT (from the actual papers, both years):
    30 marks, 90 minutes, all compulsory, calculator allowed,
    "missing data may be assumed suitably" (the official re-skin licence)
    Sections: A = MCQs (2 marks each), B = 4-mark problems, C = 8-mark combined
    useful z and phi values are PRINTED in the paper

  WATERMARK NOTE: mujstella.in fragments are reseller watermarks on THIS year's PDFs;
  same content as the course PDFs, the watermark is not course content.
```
