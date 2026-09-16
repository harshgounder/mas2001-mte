# Learning order: every slide and every question, sequenced

Built 16 September 2026, ~19:00 IST. Answers one question: in what order do the materials we
hold get read and drilled, for best learning per hour.

This is an ORDER doc. It does not replace the topic universe
(`00-MTE-TOPIC-UNIVERSE.md`) or the learn plan (`00-LEARN-PLAN.md`); it sits on top of both
and tells you which artifact to open next.

## 0. Ground truth used (verified on disk this session)

```
  slides we hold, converted to md/                     pages
    notes-lecture-series-01-09  (lectures 1-9)          147
    ppt3-discrete-prob-dist     (binomial, Poisson)      28
    ppt4-continuous-prob-dist   (uniform, normal, exp)   44
    lms-standard-error-clt      (sampling, CLT)          19
    ppt5-estimation-summary     (estimation)             26
    lms-theory-of-estimation    (estimation, deeper)     40
    mas2001-course-handout                                7
  batch-2 S&P decks, NOT converted (text copies only, ~/mas2001-devore/corpus-text/)
    S&P L1-7      108 pp  (text 30,466 ch)
    S&P L8-9       37 pp  (text 13,508 ch)
    S&P L10-11      9 pp  (text  6,224 ch)   Chebyshev, the only truly new one
    S&P L12-13     28 pp  (text 16,171 ch)
    S&P L14-15     44 pp  (text 32,573 ch)
  papers, converted: 2 MTE + 2 MTE schemes + 5 ETE + 2 re-sess + 1 summer = 12 files
  assignments, converted: mas2001-assignment-1 (6p), -2 (4p); 2024-25 1-5; 2025-26 bundle (17p)

  papers count 15, not 12: the count register says "7 papers" for the ETE family but the disk
  holds S3-2024-25, S3-2025-26, S4-2024-25, S4-2025-26, Summer, Re-sess-S3, Re-sess-S4 = 7,
  plus 2 MTE and their 2 schemes. Report 17 is right; any prose saying 5 ETE papers is wrong.
```

## 1. The dedup finding that sets the whole order

Measured, not assumed. Shared 5-word phrases between each batch-2 deck and the converted deck
it matches:

```
  L1-7   (30,466 ch) vs notes-lecture-series-01-09  -> 1,129 shared 5-grams (54% of the smaller)
  L8-9   (13,508 ch) vs notes-lecture-series-01-09  ->   456 shared (55%)
  L12-13 (16,171 ch) vs ppt3-discrete-prob-dist     ->   874 shared (53%)
  L14-15 (32,573 ch) vs ppt4-continuous-prob-dist   ->   630 shared (40%)
  L10-11 ( 6,224 ch) vs notes-lecture-series-01-09  ->    12 shared (2%)
```

and the shared strings are not boilerplate, they are the actual questions:

```
  L12-13 shares with ppt3:  "0 2301", "0 2824 0 3766", "0 1 pens in box", "0 00145 where e is"
  L14-15 shares with ppt4:  "0 12 statistics for business", "z value for 20 in", "0 8475..."
  L1-7   shares with notes: "x who can play either", "1 goon a m gupta", "x then lineups with x"
  L8-9   shares with notes: "y x 4 where x", "y between the limits x"
```

Reading:

```
  L1-7, L8-9   = re-teach of the Devore material in the notes deck (same textbook, same items)
  L12-13       = re-teach of ppt3, SAME pens numbers (0.2301, 0.2824/0.3766), same Poisson nesting
  L14-15       = re-teach of ppt4, plus the McClave slide line ("statistics for business")
  L10-11       = genuinely new (Chebyshev; 2% overlap, and that 2% is generic phrasing)
```

That is why the four big decks are placed AFTER their topic, not before: they are the second
pass and the visual check, not new teaching. The only deck that must come FIRST in its topic
is L10-11, because nothing else in batch 1 teaches Chebyshev at all.

## 2. The order (what to do, in this sequence)

### PASS 0, evening 16 Sep, 1h40, no new theory

```
  0.1  L10-11 Chebyshev deck, all 9 pages, read in full                   20 min
       text: ~/mas2001-devore/corpus-text/L10-11-Cheb.txt
       skip: Q3 slide p008 (errata 15, it states one row and works another)
       then write both inequality forms from memory, closed book           5 min
  0.2  independence rules of rvs [H1], from the formula sheet              25 min
       E(XY)=E(X)E(Y); Var(X+Y)=Var(X)+Var(Y); Var(X-Y)=same; contrast E(X+Y) always
       drill: Var(one die)=35/12 -> Var(sum)=35/6 -> the 35/54 Chebyshev bound
  0.3  the small hidden set [H3-H7]                                        35 min
       memoryless e^-1=0.3679 | landmarks 68.27/95.45/99.73 | N x P
       geometric E=1/p | hypergeometric mean nK/N
  0.4  formula sheet, sections A to I, read aloud                          15 min
  gate: all three hidden items reproduced on blank paper, no notes
```

Why first: these carry marks in every graded set we hold, they have no teaching slide, and
they are prerequisites for the CLT and estimation work later. Doing them cold on day one is
the cheapest marks in the whole paper.

### PASS 1, Thu 17 Sep morning, 3h

```
  1.1  notes-lecture-series-01-09, p012-p050  (probability foundations)  50 min
       events, set ops, axioms, addition/complement/multiplication rules, C(n,r),
       conditional definition, event independence
       do IN THIS READING: D1-1 tournament (p041-042), D1-2 laptops (p046-047),
       D1-3 basketball (p048-049), D1-4 camera (p050)
  1.2  notes deck p051-p062 + p112-p147  (random variables)              50 min
       Bernoulli, counting rv, dice sum, two coins, geometric, taxonomy, continuous intro
       DO: D1-5..D1-10 (the ten opening examples), D1-24 f=2x, D1-27 pdf/pair, D1-28 F'=f
  1.3  notes deck p063-p087  (pmf and cdf)                                50 min
       pmf conditions, find k (15k and 9k+10k^2), cdf build, F(b)-F(a-1), graphs
       DO: D1-12 (with A1 long 2), D1-14 gas pumps, D1-15 batteries, D1-16 boards,
           D1-17 dice max, D1-18 nondecreasing proof
  gate: build a cdf from a pmf and back; one find-k from each type; tournament set answers on paper
```

### PASS 2, Thu 17 Sep midday, 3h15

```
  2.1  notes deck p088-p094 + p140-p147  (expectation)                   55 min
       E(X), E[h(X)], E(aX+b) proof, continuous integrals, convergence
       DO: D1-20 proof, D1-21 (the p094 triple), D1-22 freezer six-part chain, D1-23 revenue h3/h4
  2.2  notes deck p095-p111  (variance)                                  50 min
       Var definitions, shortcut E(X^2)-mu^2, Var(c), Var(cX), V(aX+b), sd=|a|sd
       DO: D1-25 continuous conditional 5/12, D1-26 bus triangle (errata 13: use Y<2 not 3),
           D1-29 Y=X+4, D1-30 Pareto with its k>1 / k>2 conditions
  2.3  S&P L1-7 deck, text sweep, questions only                         50 min
       text: L1-7.txt. this is a re-teach; read only its 13 question blocks:
       L17-01 faculty computers, L17-02 basketball, L17-03 camera, L17-04 rare-disease Bayes,
       L17-05 gas pumps (Devore Ex 2.3), L17-06 pmf with k (OPEN), L17-07 cylinder pmf,
       L17-08 county forms (Devore Ch3 Ex14), L17-09 flashlight batteries, L17-10 boards,
       L17-11 dice maximum, L17-12 cdf nondecreasing, L17-13 E(X) on -3/6/9
       these 13 are the SAME skeletons as D1-1..D1-18: do them as the second pass
  2.4  S&P L8-9 deck, text sweep, questions only                          40 min
       L89-01 bus waiting pdf, L89-02 CDF-to-density (OPEN), L89-03 kidney E(Y),
       L89-04 Pareto moments
  gate: the freezer chain end to end; the L1-7 question set solved without looking at D1 answers
```

### PASS 3, Thu 17 Sep evening, 4h, the shelf

One template per distribution: setup conditions, pmf/pdf, mean, variance, the corpus question,
the trap.

```
  3.1  BINOMIAL                                                           60 min
       ppt3 p001-p018 first (slides teach it), then the L12-13 binomial block as pass 2
       DO: pens three parts (p3 p013-016), irregular die p=5/8 (p017-018), 5-coin p002-007
       DO: assignment-2 A2, A9, D3 + assignment-1 long 2
       DO: E24S3-A1, E24S3-B3, E24S3-B4, E25S3-A3, E25S3-B2 (pens again), R25S4-B2, E25SUM-Q3
  3.2  POISSON                                                            60 min
       ppt3 p019-p028, then L12-13 Poisson examples 1-3
       DO: insurance 0.1755 (errata 1), ratio lambda=10 (p025), THE NESTING 32e^-10 = 0.00145,
           approximation 0.1755
       DO: A2 A3, A7, A12, B1 (rejected 0.2424), C3 (0.8753), D2, D3 + E25SUM-Q17
  3.3  UNIFORM                                                            30 min
       ppt4 p001-p006, then L14-15 uniform example
       DO: p4 p006 length ratio, A2 A4, A10 (clipping), B2, B8 (|X| intervals), C4 (rounding)
  3.4  NORMAL                                                             75 min
       ppt4 p007-p037, then L14-15 normals
       DO: the 8.6 chain (p032-033), 45-62 interval (A2 B3), 20% inverse (p034-037),
           5000 batteries (A2 B4), 10000 bulbs (A2 D1), landmarks (A2 A11)
           THEN the two-unknown system (A2 C2, errata 10: sigma 28.2, mu 37.2, cutoff 30.4)
           AND the L14-15 N(8,5) pair + inverse cutoff
       TRAP: identify which table the question gives (phi vs F) BEFORE substituting
  3.5  EXPONENTIAL                                                        45 min
       ppt4 p038-p043, then L14-15 exponential example
       DO: 15/hr under 3 min (p042-043), A2 MCQ Q5, B5 (0.6225, errata 9), B7, C1 (memoryless),
           D2 (unit conversion), E24S4-A4, E25S4-A5, R25S3-B1, E24S4-C1b
  gate: one mixed question per distribution, closed book, before moving on
```

### PASS 4, Fri 18 Sep morning, 2h

```
  4.1  lms-standard-error-clt, p001-p018, read in full                    60 min
       population vs sample, SRS, SE = sigma/sqrt(n), scaling law, CLT statement and conditions,
       z with the SE denominator, the "average of n" template
       DO: lightbulbs 20->10 (p005), ATM, impurity (errata 6: z=-0.94, answer 0.1644), LED,
           machines n=9 exact-normal fallback
       DO: E24S3-A5 (SE), R25S3-A3 (n up SE down), E25SUM-Q9, Q10, E25S3-B5
  gate: the impurity question reproduced with the corrected Z, closed book
```

### PASS 5, Fri 18 Sep midday, 2h30

```
  5.1  ppt5-estimation-summary, p001-p021, read in full                   60 min
       parameter/statistic/estimator/estimate, point vs interval, CI shape, unbiasedness,
       force-unbiased with a constant, consistency, efficiency, sufficiency
       DO: response time 205 ms (p022), packets 0.93 (p023), battery CI (p024, boundary),
           comparison set 1 (t1 wins, t2 biased), comparison set 2 (T3 wins, vars 3/29/1/3)
       DO: E25S3-A1, A2, E24S4-A1, E25S4-B3, R25S3-A2, R25S4-A3, MTE 2025-26 Q3 (sufficiency MCQ)
  5.2  lms-theory-of-estimation, the TWO unique items only                30 min
       lt p024-p025 sufficiency (Neyman-Fisher, Poisson sum, exponential xbar)
       SKIP lt p031-p040 entirely: the CI block is out of MTE
  gate: both comparison sets reproduced fully, plus the mock B4 T4-trap layout
```

### PASS 6, Fri 18 Sep evening, 3h, integration

```
  6.1  reports/07-MOCK-PAPER.md, closed book, timed                          90 min
  6.2  mark it against reports/08-MOCK-SOLUTIONS.md                          30 min
  6.3  repair only the misses, then redo the failed parts                    40 min
  6.4  formula sheet sections A-I, read aloud                                20 min
  gate: 24/30 or better. 18-23: Saturday morning goes to the weakest stage only.
        below 18: Saturday morning goes to the lectures 1-6 block, re-read
```

### PASS 7, Sat 19 to Thu 24 Sep, papers and assignments as drill

Order matters here: papers first (they show the shape), then assignments (they are the
practice), then the repeats as timed speed work.

```
  7.1  MTE 2025-26 paper, closed book, untimed, then mark it               60 min
       md/paper-mte-2025-26.md + md/paper-mte-2025-26-scheme.md
  7.2  MTE 2024-25 paper, same                                        60 min
  7.3  the two scheme files read as marking guidance (red pen allocations)
  7.4  the 2025-26 assignment bundle, assignments 1 and 2 in full      2h
       these are lectures 1-11 and 12-18 material, the closest thing to setter-authored drill
  7.5  the 2024-25 assignments 1 and 2 (in MTE scope)                  1h30
  7.6  2024-25 assignments 3, 3-Ep2, 4, 5 (out of scope, one pass, no deep work)   45 min
  7.7  ETE S3 and S4 papers, IN blocks only (56 of the 97 blocks)      2h
       this is where the same skeletons re-appear under exam wording
  7.8  re-sess papers, IN blocks only                                  40 min
  7.9  the 2025-26 assignment 1 second edition (asgn-faculty-variant)  DEDUP ONLY
       its own row gives k=0.0782, its key prints k=1/10: log as errata, do not drill it
```

### PASS 8, the last day before the paper

```
  8.1  formula sheet, two passes, 40 min
  8.2  every distribution mean/variance pair and the three Chebyshev values, from memory
  8.3  the hidden set (memoryless, landmarks, N x P, 1/p, nK/N) from memory, 15 min
  8.4  the 10-item trap list
  8.5  no new material, nothing below lecture 22
```

## 3. The artifact-order table (which file, when)

```
  order  artifact                              file                              pass
  1      Chebyshev deck                        corpus-text/L10-11-Cheb.txt       theory (new)
  2      formula sheet A-I                     reports/03-FORMULA-SHEET.md       reference
  3      lecture notes 1-9 (all 147 pp)        md/notes-lecture-series-01-09/    theory (main)
  4      S&P L1-7 questions only               corpus-text/L1-7.txt              pass 2
  5      S&P L8-9 questions only               corpus-text/L8-9.txt              pass 2
  6      ppt3 discrete (p1-28)                 md/ppt3-discrete-prob-dist/       theory
  7      S&P L12-13 questions only             corpus-text/L12-13.txt            pass 2
  8      ppt4 continuous (p1-44)               md/ppt4-continuous-prob-dist/     theory
  9      S&P L14-15 questions only             corpus-text/L14-15.txt            pass 2
  10     lms-standard-error-clt (p1-19)        md/lms-standard-error-clt/        theory
  11     ppt5 estimation (p1-21)               md/ppt5-estimation-summary/       theory
  12     lms-theory estimation (p24-25 only)   md/lms-theory-of-estimation/      theory (2 items)
  13     mock paper + solutions                reports/07- and 08-               integration
  14     MTE 2025-26 + scheme                  md/paper-mte-2025-26*.md          drill
  15     MTE 2024-25 + scheme                  md/paper-mte-2024-25*.md          drill
  16     2025-26 assignment bundle             PS/2025-2026-S&P_assignments_1-5  drill
  17     2024-25 assignments 1 and 2           md/asgn-2024-25-{1,2}.md          drill
  18     2024-25 assignments 3,3ep2,4,5        md/asgn-2024-25-{3,3-ep2,4,5}.md  light
  19     ETE + re-sess + summer papers        md/paper-ete-*.md, resess-*.md    drill (IN only)
  NEVER  lms-maximum-likelihood (16p)          OUT of MTE
  NEVER  lms-method-of-moments (11p)           OUT of MTE
  NEVER  course handout (7p)                   no questions
  NEVER  lt p031-p040 (10p)                    CI block, OUT of MTE
```

## 4. The rules that make this the efficient order

```
  R1  hidden prerequisites first. They gate 4 downstream topics (Chebyshev sums, CLT
      variances, estimator variances, Poisson additivity). Cost now: 1h40. Cost later: rework.
  R2  read a topic's own deck BEFORE its S&P re-teach. The re-teach is the second pass, so
      it lands on warm material and doubles as the visual/dedup check.
  R3  never read both of a pair cold. The pairs, with the shared-phrase evidence in section 1,
      are (notes, L1-7), (notes, L8-9), (ppt3, L12-13), (ppt4, L14-15).
  R4  the only deck that goes first is L10-11, because nothing else teaches Chebyshev.
  R5  every question is done with its deck or with its paper, never read later in a batch.
      Reading a question without solving it is the single biggest waste of the 9 days left.
  R6  papers before assignments. Papers reveal the shape (30 marks, 90 min, A/B/C, all
      compulsory), assignments are the volume drill; doing them in this order stops the
      assignment wording from hiding the exam wording.
  R7  out-of-scope material gets one light pass and no more (assignments 3-5, 35 of 97 ETE
      blocks, lt CI block). It is revision for the ETE, not for the MTE.
  R8  errata first every time you touch a source: errata 1-15 + 19-21. A wrong printed key
      costs marks if you drill it.
  R9  the mock is the only closed-book, timed artifact before the real thing. Do it once in
      full and once more only on the failed parts. Do not re-run the whole mock for comfort.
```

## 5. What this order is NOT allowed to claim

```
  - the S&P decks are not "new material" for four of five of them; the shared 5-gram counts
    above are the evidence, and reading them as new teaching would waste the 9 days we have
  - the pens, rain and kx^3(4-x)^2 sources are still OPEN; no drill claim depends on them
  - the 2025-26 bundle's 119 items are enumerated but their 2024 matches are NOT assessed, so
    treating them as 119 fresh items would double-count. Do assignments 1-2 of the bundle
    (the in-scope part) and treat 3-5 as the repeat sets they are
  - the two re-sess and one summer paper have 35 OUT blocks each family; only the IN blocks
    are drill
```

---
Learn order v1, 16 Sep 2026. Numbers in section 0 and section 1 were computed on disk this
session (page counts from md/, char counts and shared-5-gram overlays from the corpus-text
copies). The errors/lies fix and the deep audit still wait for the user's go.
