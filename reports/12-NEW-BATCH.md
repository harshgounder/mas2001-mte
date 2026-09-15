# New batch inventory and processing queue

Listed 15 September 2026. 23 batch-2 files in ~/PS, all catalogued. Processing: one unit at a
time, 10-20 pages per unit, nothing skipped.

## 1. THE LIST

### A. Papers (11 files) - highest value (they show what is asked)

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

Count correction 15 Sep: an earlier revision of this table carried rows A12-A14 for three
"(1)" and "(2)" paper copies. Those files do not exist, in ~/PS or anywhere on disk, and no
such sources.yaml entry exists. The rows were wrong and are deleted. Every paper duplicate
claim in this repo is sha-scoped: the only byte-identical duplicate that actually exists is
`asgn-copy-2025-26` (`~/PS/Assignment 2_MAS2001-2.pdf`, sha 5ff197311b60) matching
`mas2001-assignment-2` (`~/Videos/Assignment 2_MAS2001-2.pdf`)
```

### B. Assignments (7 files, + 2 extra sources) - this year's set is new

SCOPE WARNING, added 15 Sep after reading all of these page by page (see section 6.1).
IN MTE scope: B1's assignment-1 and assignment-2 sections, B2, B3. That is 91 question blocks
of lectures 1 to 18 drill, 36 of them with printed answers, the largest single block of new
MTE material in the batch. OUT of MTE scope: B1's assignments 3-5, B4, B5, B6, B7 (their
covers are MLE, MoM, sufficiency, Bayesian, confidence intervals, hypothesis testing,
F-test, ANOVA = lectures 22 to 36).

```
  B1  2025-2026-S&P_assignments_1-5.pdf                   17   THIS year, combined 1-5
                                                               sections: A memory MCQ, B concept,
                                                               C analytical, D application
                                                               IN MTE SCOPE: assignment 1 (19
                                                               blocks) + assignment 2 (36 blocks,
                                                               WITH printed answers). Assignments
                                                               3-5 are lecture 22+ and out of scope.
  B2  2024-2025-Assignment 1.pdf                           2   IN MTE SCOPE (15 blocks): cover is
                                                               RVs, cdf, pmf, expectation, Chebyshev
                                                               = lectures 1-11. NOT a revision file.
  B3  2024-2025-Assignment 2.pdf                           2   IN MTE SCOPE (20 blocks): cover is
                                                               CLT, binomial, Poisson, uniform,
                                                               normal, exponential = lectures 12-18.
                                                               Carries the memoryless questions.
  B4  2024-2025-Assignment 3.pdf                           3   OUT of MTE: cover is MLE, MoM,
                                                               sufficient statistics, Bayesian,
                                                               confidence intervals (lectures 22-28)
  B5  2024-2025-Assignment 3 Episode 2.pdf                 2   *** IMAGE-ONLY (240 chars): vision
                                                               pass *** OUT of MTE, same block as B4
  B6  2024-2025-Assignment 4.pdf                           3   OUT of MTE: hypothesis testing, Type I
                                                               and II errors, critical region (29-30)
  B7  2024-2025-Assignment 5.pdf                           3   OUT of MTE: t-tests, F-test, ANOVA
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
  CHECKED, NOT NEW (byte-identical copies already catalogued):
    - 2024-2025-Assignment 2.pdf = the batch-1 assignment-2 source file (sha 5ff19731,
      same bytes, different path; the batch-1 copy lives in ~/Videos)
    - (an earlier revision claimed three "(1)"/"(2)" paper copies here; recheck 15 Sep found
      no such files anywhere on disk, so that claim is deleted. Sha-verified duplicates in the
      whole corpus are one pair, listed above)
  SAME FAMILY, DIFFERENT EDITION (a second keyed edition, NOT a plain copy):
    - MAS2001-Assignment 1 .pdf carries Dr. Ruchika Mehta as faculty (batch-1 copy is
      Dr. Vivek Singh) AND a different pmf row in long Q2: p(x) = k, 2k, 2k, 3k, 3k, k^2,
      2k^2, 7k^2 + k, which normalises to 12k + 10k^2 = 1 (root 0.0782), against the
      batch-1 row 0, k, 2k, 2k, 3k, k^2, 2k^2, 7k^2 + k (10k^2 + 9k = 1, root 1/10).
      Its key column carries different digits. Treat it as a second edition to compare at
      U05, not as a duplicate; a vision pass on its key column is mandatory there.
  NEW ORGANIZATION / CONTENT MIX (verify page by page during processing):
    - L1-7, L8-9 (may contain re-arranged + updated versions of old material)
  MOSTLY DUPLICATE OF OLD DECKS (verify during processing):
    - L12-13 (~79 percent pages match ppt3)
    - L14-15 (~87 percent pages match ppt4)
  the dedup pass used text fingerprints; final verdict per page happens in processing

  TWO MARKS TO SETTLE IN THE DECKS (open, must be resolved at U12/U13):
    both are [H] hidden blocks in batch 1, and both decks are near-unreadable text-wise
    (L8-9: 8456 chars over 37 pages, a slide deck, not a prose deck; L1-7: 24521 over 108).
    A grep of their text layers finds no "independent random variable" and no
    E(XY) / Var(X+Y) restatement, and L1-7's slide titles stop at set theory and events.
    If either deck is what its filename claims, the independence-rules [H] retires and
    three atlas files need a line. If not, it confirms the [H] for a converted source.
    The [H] for memoryless (A2 Q5 + A2 C1) and the landmarks 68.27 / 95.45 / 99.73
    (A2 A11) is CONFIRMED already: a full grep of the 348 converted pages finds those
    numbers only inside the assignment paper that asks them, never on a teaching slide.
```

## 3. PROCESSING QUEUE (one unit at a time, 10-20 pages per unit)

```
  UNIT   content                                              pages  status
  U01    A1+A2+A3+A4: both MTE papers + both schemes           15    NEXT
  U02    A5+A6+A10: ETE S3 x2 + re-sess S3                    6     queued
  U03    A7+A8+A9+A11: ETE S4 x2 + summer + re-sess S4        9     queued
  U04    B1: 2025-26 assignments 1-5 combined, A1+A2 only     17    queued (skip 3-5, out of scope)
  U05    B2+B3: 2024-25 assignments 1 and 2 (IN scope)         4    PROMOTED 15 Sep: MTE drill,
                                                                      ahead of the ETE papers
  U05b   B4..B7: 2024-25 assignments 3,3-ep2,4,5 (OUT scope)  11    last, revision only
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
  total pages: 288 | 19 units (+ U05b, a split of the old U05: 288 is unchanged)
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

## 6.1 The assignment files, read 15 Sep (NEW, this closes the gap below)

Every assignment file was read on 15 Sep, text layer first (vision where the layer is empty,
which is only Assignment 3 Episode 2). "Read" means every question stem of every page was
extracted and inspected; it does NOT mean a full transcription of all 91 blocks, which is
U04/U05 work. What is actually in them:

Every count below was re-derived from the file itself on 15 Sep by enumerating question
labels, not estimated. Counts are BLOCKS (a multi-part question counts once), except where
the row says parts.

```
  file                               blocks  parts   layer   content                            MTE
  2024-2025-Assignment 1                 16    -      good    RVs, cdf, pmf, expectation,
                                                            Chebyshev. Labels Q1..Q16, with
                                                            no Q14 in the source at all.     IN (1-11)
  2024-2025-Assignment 2                 20    32     good    CLT, binomial, Poisson, uniform,
                                                            normal, exp. Q1 is a 12-part
                                                            recall block, Q2..Q20 are
                                                            problems.                        IN (12-18)
  2025-26 set, assignment 1              19    -      good    probability, RVs, pmf, Chebyshev
                                                            (Q1 is an 11-part MCQ block)     IN (1-11)
  2025-26 set, assignment 2              36    -      good    binomial..normal, exp, CLT, ALL
                                                            WITH PRINTED ANSWERS             IN (12-18)
  2025-26 set, assignments 3-5           45    -      good    Q22..Q45 continue the combined
                                                            file; MLE, MoM, Bayesian, CI,
                                                            tests, ANOVA                     OUT
  2024-2025-Assignment 3                 22    -      good    labels A1..A10, B1..B5, C1..C5
                                                            (no C3 in the extract); MLE, MoM,
                                                            sufficiency, Bayesian, CI        OUT
  2024-2025-Assignment 3 Episode 2        2    -      NONE    image-only scan, vision pass
                                                            needed before any claim           OUT
  2024-2025-Assignment 4                 16    -      good    hypothesis testing, Type I/II,
                                                            critical region                  OUT
  2024-2025-Assignment 5                 15    -      good    labels A1..A10, B1..B5; t-tests,
                                                            F-test, chi-square, ANOVA        OUT
```

In-scope assignment questions available as MTE drill: 16 + 20 + 19 + 36 = 91 blocks, of which
the 2025-26 assignment 2 supplies 36 WITH printed answers. That is larger than the whole
batch-1 assignment corpus (52 blocks) and it was not in the repo.

Overlap check, because a repeat would be worthless work: the 2024-25 assignment 2 and the
2025-26 set are DIFFERENT questions from the batch-1 assignment 2 already converted. Probed
by named stem (800 families, bombs, 520 pages, cellphones, subway, soldiers, Compu World,
washers, shelf life, bulbs): zero stem overlap with the batch-1 paper. New drill either way.

The memoryless property, which batch-1 met only inside one MCQ plus one question part, now
has real worked questions behind it. Verified by grep on 15 Sep (corrected: an earlier draft
of this paragraph also claimed the 68.27/95.45/99.73 landmarks were covered here. They are
NOT: that string appears in NO batch-2 file. The landmark MCQ sits in the BATCH-1 assignment
2, which is the `mas2001-assignment-2` source in ~/Videos and its byte-identical twin in ~/PS,
nothing else. Claim retracted.)

```
  2024-2025-Assignment 2 Q1(xii)  "Which continuous distribution follows memoryless property"
  2024-2025-Assignment 2 Q15      component survives 10 months given it survived 9 (0.6065)
  2025-26 set, assignment 2 Q19   repair: at least 10h given more than 9h (0.6065)
  2025-26 set, assignment 2 Q20   P(X < 1 | X < 2) for exponential mean 2 (0.5679)
```

Two queue consequences, both applied:
- U05 is no longer "out of scope, do not sort". It is 4 pages (both files) of IN-scope MTE
  drill and is promoted ahead of the ETE papers.
- U04 must split: the 2025-26 set is one file carrying assignment 1 (in), assignment 2 (in,
  with answers) and assignments 3-5 (out). Read A1 and A2, skip 3-5.

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
