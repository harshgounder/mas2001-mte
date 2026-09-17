# 14 MASTER STUDY ORDER: what to do, in what order

Built 16 Sep 2026. This is THE order document. It ties together everything we hold: the notes,
the slide decks, the reference cards, the patterns, the drill, the papers. Follow it top to
bottom.

Supersedes `reports/11-QUESTION-ATLAS/00-LEARN-ORDER.md` (that one was written before the
notes folder existed; this one covers every artifact we now have).

---

## 0. THE ARTIFACT INVENTORY (what exists, where)

```
   ┌─────────────────────────────────────────────────────────────────────┐
   │  A. THE NOTES          deck/notes/  (11 files)                       │
   │     the slides rewritten as teachable notes. READ THESE FIRST.       │
   │     you do NOT need to open a PDF to learn the theory.               │
   ├─────────────────────────────────────────────────────────────────────┤
   │  B. THE DECKS          the S&P batch-2 decks (text copies)           │
   │     L1-7, L8-9, L10-11 Cheb, L12-13, L14-15                          │
   │     these are PASS 2 / the visual check, NOT new teaching            │
   │     (except L10-11 Chebyshev, which IS new)                          │
   ├─────────────────────────────────────────────────────────────────────┤
   │  C. THE REFERENCE      deck/*.md  (15 files)                         │
   │     cheatsheet, terms, linguistics, methods, distributions, numbers,  │
   │     patterns, traps, questions, slide map, hidden layer, drill,      │
   │     mechanics. USE THESE WHILE SOLVING, not as reading material.     │
   ├─────────────────────────────────────────────────────────────────────┤
   │  D. THE PATTERNS       deck/07-PATTERNS.md                           │
   │     the mutation system. read AFTER two papers, then it pays off.    │
   ├─────────────────────────────────────────────────────────────────────┤
   │  E. THE PAPERS         md/paper-mte-*, paper-ete-*, resess-*, asgn-* │
   │     the drill material. papers FIRST, then assignments.              │
   ├─────────────────────────────────────────────────────────────────────┤
   │  F. THE ORIGINAL SLIDES the PDFs + md/ conversions                   │
   │     ONLY open these for (a) Chebyshev deck, (b) L1-7/L8-9/L12-13/    │
   │     L14-15 question blocks. Everything else is in the notes already. │
   └─────────────────────────────────────────────────────────────────────┘
```

---

## 1. THE MASTER ORDER, ONE PICTURE

```
   ┌──────────────────────────────────────────────────────────────┐
   │  PASS 0   TONIGHT  ·  1h40  ·  no new material, pure gating  │
   │  the hidden layer + Chebyshev + the formula sheet            │
   └───────────────────────────┬──────────────────────────────────┘
                               ▼
   ┌──────────────────────────────────────────────────────────────┐
   │  PASS 1   notes/01,02,03   ·  3h   ·  the foundations        │
   │  probability -> random variables -> pmf/cdf                  │
   └───────────────────────────┬──────────────────────────────────┘
                               ▼
   ┌──────────────────────────────────────────────────────────────┐
   │  PASS 2   notes/04,05  +  L1-7 & L8-9 question blocks  ·  3h │
   │  expectation, variance, continuous rv, first re-teach pass   │
   └───────────────────────────┬──────────────────────────────────┘
                               ▼
   ┌──────────────────────────────────────────────────────────────┐
   │  PASS 3   notes/06,07 + L12-13 & L14-15 blocks · 4h20       │
   │  binomial, Poisson, uniform, normal, exponential             │
   └───────────────────────────┬──────────────────────────────────┘
                               ▼
   ┌──────────────────────────────────────────────────────────────┐
   │  PASS 4   notes/08  ·  2h  ·  sampling and the CLT           │
   └───────────────────────────┬──────────────────────────────────┘
                               ▼
   ┌──────────────────────────────────────────────────────────────┐
   │  PASS 5   notes/09  ·  2h15  ·  estimation theory            │
   └───────────────────────────┬──────────────────────────────────┘
                               ▼
   ┌──────────────────────────────────────────────────────────────┐
   │  PASS 6   THE MOCK  ·  3h  ·  closed book, timed, then mark  │
   └───────────────────────────┬──────────────────────────────────┘
                               ▼
   ┌──────────────────────────────────────────────────────────────┐
   │  PASS 7   PAPERS -> ASSIGNMENTS -> ETE IN BLOCKS  ·  days    │
   │  + read 07-PATTERNS here, when you have seen two papers      │
   └───────────────────────────┬──────────────────────────────────┘
                               ▼
   ┌──────────────────────────────────────────────────────────────┐
   │  PASS 8   LAST DAY  ·  cheatsheet, traps, hidden set, memory │
   └──────────────────────────────────────────────────────────────┘
```

---

## 2. PASS 0, TONIGHT, 1h40, THE GATING BLOCK

Do this FIRST. It gates four downstream topics and carries marks in every paper.

```
   ┌────┬───────────────────────────────────────────────┬──────┐
   │ #  │ WHAT                                          │ TIME │
   ├────┼───────────────────────────────────────────────┼──────┤
   │0.1 │ notes/10 PART A: Chebyshev, all of it          │ 30m  │
   │    │   (skip Q3, errata 15; do Q1 and Q2)          │      │
   ├────┼───────────────────────────────────────────────┼──────┤
   │0.2 │ notes/10 PART B: H1 independence rules         │ 25m  │
   │    │   E(XY), Var(X+Y), Var(X-Y), then the drill:   │      │
   │    │   35/12 -> 35/6 -> 35/54                       │      │
   ├────┼───────────────────────────────────────────────┼──────┤
   │0.3 │ deck/11-BEYOND-SLIDES.md, H3 to H7             │ 30m  │
   │    │   memoryless, landmarks, N x P, 1/p, nK/N      │      │
   ├────┼───────────────────────────────────────────────┼──────┤
   │0.4 │ deck/01-CHEATSHEET.md, read aloud, twice       │ 15m  │
   └────┴───────────────────────────────────────────────┴──────┘

   GATE: write all of H1-H7 on blank paper, no notes.
   ALSO: the Chebyshev deck's own pages, 9 pages, text at
         ~/mas2001-devore/corpus-text/L10-11-Cheb.txt
```

Why first: `07-PATTERNS.md` shows Chebyshev is graded 9+ times; H1 gates the dice variance,
Var(Xbar), every estimator variance and Poisson additivity. Doing this cold costs 1h40 now and
saves rework in PASS 3, 4 and 5.

---

## 3. PASS 1, THE FOUNDATIONS, 3h

```
   ┌────┬───────────────────────────────────────────────┬──────┐
   │1.1 │ notes/01-probability-foundations.md            │ 55m  │
   │    │   read fully, then DO the 3 worked examples     │      │
   │    │   (tournament, laptops, basketball) on paper    │      │
   ├────┼───────────────────────────────────────────────┼──────┤
   │1.2 │ notes/02-random-variables.md                   │ 45m  │
   │    │   the 36-cell dice grid, draw it yourself       │      │
   │    │   + deck/05-DISTRIBUTIONS.md first table        │      │
   ├────┼───────────────────────────────────────────────┼──────┤
   │1.3 │ notes/03-pmf-and-cdf.md                        │ 60m  │
   │    │   DO: gas pumps, find-k (the 10k²+9k=1 one),    │      │
   │    │   boards inspection, dice maximum M, the proof  │      │
   ├────┼───────────────────────────────────────────────┼──────┤
   │1.4 │ deck/04-METHODS.md sections 1-5                 │ 20m  │
   │    │   the solving paths for what you just read      │      │
   └────┴───────────────────────────────────────────────┴──────┘

   GATE: build a cdf from a pmf and back; one find-k of each type;
         the dice-max cdf with its squares (1,4,9,16,25,36).
```

---

## 4. PASS 2, EXPECTATION + VARIANCE + FIRST RE-TEACH, 3h15

```
   ┌────┬───────────────────────────────────────────────┬──────┐
   │2.1 │ notes/04-expectation-and-variance.md           │ 55m  │
   │    │   DO: the die (3.5), the p094 triple (209),     │      │
   │    │   the freezer 6-part chain, the magazine 3-vs-4 │      │
   ├────┼───────────────────────────────────────────────┼──────┤
   │2.2 │ notes/05-continuous-rv.md                      │ 65m  │
   │    │   DO: f=2x, the conditional 5/12, the bus       │      │
   │    │   triangle 6 parts, cdf->pdf, the hospital Y    │      │
   ├────┼───────────────────────────────────────────────┼──────┤
   │2.3 │ S&P L1-7 QUESTIONS ONLY (13 blocks, pass 2)     │ 45m  │
   │    │   text: ~/mas2001-devore/corpus-text/L1-7.txt   │      │
   │    │   these are the SAME skeletons as notes/01-03   │      │
   ├────┼───────────────────────────────────────────────┼──────┤
   │2.4 │ S&P L8-9 QUESTIONS ONLY (4 blocks)             │ 30m  │
   │    │   bus pdf, CDF-to-density, kidney E(Y), Pareto  │      │
   └────┴───────────────────────────────────────────────┴──────┘

   GATE: the freezer chain end to end. The L1-7 questions solved
         WITHOUT looking at the notes/01-03 answers.
   NOTE: do NOT read L1-7/L8-9 as new teaching. 54-55% of their
         5-grams exist in the notes deck already. They are pass 2.
```

---

## 5. PASS 3, THE DISTRIBUTION SHELF, 4h20

One template per distribution: setup, pmf/pdf, moments, the corpus question, the trap.

```
   ┌────┬────────────────────────────────────────────────┬──────┐
   │3.1 │ notes/06-binomial-poisson.md  PART A binomial  │ 55m  │
   │    │   DO: pens 3 parts, irregular die p=5/8,        │      │
   │    │   5-coin derivation                             │      │
   │    │   then L12-13 binomial block (pass 2)           │      │
   ├────┼────────────────────────────────────────────────┼──────┤
   │3.2 │ notes/06 PART B Poisson                        │ 50m  │
   │    │   DO: ratio lambda=10, THE NESTING 0.00145,     │      │
   │    │   insurance 0.1755, the tail 0.8753             │      │
   ├────┼────────────────────────────────────────────────┼──────┤
   │3.3 │ notes/07 PART A uniform                        │ 25m  │
   │    │   DO: U(2,6), the length ratio 0.50             │      │
   ├────┼────────────────────────────────────────────────┼──────┤
   │3.4 │ notes/07 PART B normal                         │ 70m  │
   │    │   DO: the 8.6 chain, the 45-62 interval, the    │      │
   │    │   20% inverse (3.792), the two-unknown (errata  │      │
   │    │   10: mu 37.2, sigma 28.2, cutoff 30.4)         │      │
   │    │   then L14-15 normals (pass 2)                  │      │
   ├────┼────────────────────────────────────────────────┼──────┤
   │3.5 │ notes/07 PART C exponential                    │ 40m  │
   │    │   DO: 15/hr under 3 min (0.5276), the           │      │
   │    │   conditional 0.6225, memoryless, unit conv     │      │
   │    │   then L14-15 exponential (pass 2)              │      │
   ├────┼────────────────────────────────────────────────┼──────┤
   │3.6 │ deck/05-DISTRIBUTIONS.md, the 9-slot grid       │ 20m  │
   │    │   mark which slots are ASKED vs a SIBLING       │      │
   └────┴────────────────────────────────────────────────┴──────┘

   GATE: one mixed question per distribution, closed book.
   TRAP CHECK before moving: the two table conventions (H8), the
         variance slot in N(mu,sigma^2), rate vs mean.
```

---

## 6. PASS 4, SAMPLING AND CLT, 1h40

```
   ┌────┬───────────────────────────────────────────────┬──────┐
   │4.1 │ notes/08-sampling-and-clt.md, read fully       │ 60m  │
   │    │   DO: lightbulbs (SE 20/10), ATM (0.0668),     │      │
   │    │   impurity (Z2=-0.94, 0.1645 table), LED       │      │
   │    │   machines n=9 (0.6898)                        │      │
   ├────┼───────────────────────────────────────────────┼──────┤
   │4.2 │ deck/04-METHODS.md sections 14-15              │ 15m  │
   │    │   the SE and CLT solving paths                  │      │
   │    ├───────────────────────────────────────────────┤      │
   │4.3 │ redo the machines n=9 case BLIND, then check   │ 25m  │
   │    │   (it is the template: normal pop, small n)     │      │
   └────┴───────────────────────────────────────────────┴──────┘

   GATE: the impurity question reproduced with the CORRECTED
         Z2 = -0.94, closed book. State which table you used.
```

---

## 7. PASS 5, ESTIMATION, 2h15

```
   ┌────┬───────────────────────────────────────────────┬──────┐
   │5.1 │ notes/09-estimation.md, read fully             │ 70m  │
   │    │   DO BOTH comparison sets on paper, all steps:  │      │
   │    │   set 1 -> lambda=0, t1/t3 unbiased, t1 wins    │      │
   │    │   set 2 -> lambda=1, all unbiased, T3 wins      │      │
   │    │   + the consistency trap (fixed n is NOT it)    │      │
   ├────┼───────────────────────────────────────────────┼──────┤
   │5.2 │ the 3 real-life numerics                       │ 25m  │
   │    │   205 ms (state estimator AND estimate),        │      │
   │    │   0.93, the battery CI (7.81, 8.99) [boundary]  │      │
   ├────┼───────────────────────────────────────────────┼──────┤
   │5.3 │ lms-theory p024-p025 ONLY (sufficiency)        │ 25m  │
   │    │   SKIP p031-p040 entirely, out of MTE           │      │
   ├────┼───────────────────────────────────────────────┼──────┤
   │5.4 │ deck/04-METHODS.md section 16                  │ 15m  │
   │    │   the estimator-comparison protocol             │      │
   └────┴───────────────────────────────────────────────┴──────┘

   GATE: both comparison sets reproduced fully with the winner named
         and the reason stated, plus the mock B4 layout.
```

---

## 8. PASS 6, THE MOCK, 3h

```
   ┌────┬───────────────────────────────────────────────┬──────┐
   │6.1 │ reports/07-MOCK-PAPER.md, CLOSED BOOK, TIMED   │ 90m  │
   ├────┼───────────────────────────────────────────────┼──────┤
   │6.2 │ mark it against reports/08-MOCK-SOLUTIONS.md   │ 30m  │
   │    │   (errata 18: the B4 note is wrong, T4 is       │      │
   │    │   THIRD of four, not smallest)                  │      │
   ├────┼───────────────────────────────────────────────┼──────┤
   │6.3 │ repair ONLY the misses, then redo those parts  │ 40m  │
   ├────┼───────────────────────────────────────────────┼──────┤
   │6.4 │ deck/08-TRAPS.md, the 10-item list, aloud      │ 20m  │
   └────┴───────────────────────────────────────────────┴──────┘

   GATE:
     24+/30  -> proceed to PASS 7
     18-23   -> the next morning goes to the WEAKEST pass only
     <18     -> the next morning re-reads notes/01-05 (the base)
```

---

## 9. PASS 7, PAPERS AND ASSIGNMENTS, several days

Order matters: papers reveal the SHAPE, assignments give the VOLUME.

```
   ┌────┬───────────────────────────────────────────────┬──────┐
   │7.1 │ MTE 2025-26 paper, closed book, then mark      │ 60m  │
   │    │   md/paper-mte-2025-26.md + the scheme          │      │
   ├────┼───────────────────────────────────────────────┼──────┤
   │7.2 │ MTE 2024-25 paper, same                        │ 60m  │
   ├────┼───────────────────────────────────────────────┼──────┤
   │7.3 │ READ deck/07-PATTERNS.md NOW                   │ 30m  │
   │    │   you have seen two papers, so the mutation     │      │
   │    │   system will click. Then re-scan both papers   │      │
   │    │   and label every question with its RADICAL.    │      │
   ├────┼───────────────────────────────────────────────┼──────┤
   │7.4 │ deck/09-QUESTIONS.md, the tagged inventory     │ 20m  │
   │    │   confirm your labels against it                │      │
   ├────┼───────────────────────────────────────────────┼──────┤
   │7.5 │ 2025-26 assignment bundle, assignments 1 and 2 │ 2h   │
   │    │   (the in-scope part). The full bundle has 119  │      │
   │    │   rows; assignments 3-5 get a separate light pass.│    │
   ├────┼───────────────────────────────────────────────┼──────┤
   │7.6 │ 2024-25 assignments 1 and 2 (in MTE scope)     │ 1h30 │
   ├────┼───────────────────────────────────────────────┼──────┤
   │7.7 │ 2024-25 assignments 3, 3-ep2, 4, 5  (LIGHT)    │ 45m  │
   ├────┼───────────────────────────────────────────────┼──────┤
   │7.8 │ ETE S3 and S4, IN blocks only (56 of 97)       │ 2h   │
   │    │   where the same skeletons reappear under       │      │
   │    │   exam wording                                  │      │
   ├────┼───────────────────────────────────────────────┼──────┤
   │7.9 │ re-sess papers, IN blocks only                 │ 40m  │
   ├────┼───────────────────────────────────────────────┼──────┤
   │7.10│ asgn-faculty-variant: DEDUP ONLY, do not drill │ 10m  │
   │    │   its key (k=1/10) contradicts its row (0.0782) │      │
   └────┴───────────────────────────────────────────────┴──────┘
```

---

## 10. PASS 8, THE LAST DAY

```
   ┌────┬───────────────────────────────────────────────┬──────┐
   │8.1 │ deck/01-CHEATSHEET.md, twice, aloud            │ 40m  │
   ├────┼───────────────────────────────────────────────┼──────┤
   │8.2 │ every mean/variance pair, from memory           │ 15m  │
   │    │   + the three Chebyshev values (3/4, 8/9, 15/16)│      │
   ├────┼───────────────────────────────────────────────┼──────┤
   │8.3 │ the hidden set H1-H7, from memory              │ 15m  │
   ├────┼───────────────────────────────────────────────┼──────┤
   │8.4 │ deck/08-TRAPS.md, the 10-item list             │ 10m  │
   ├────┼───────────────────────────────────────────────┼──────┤
   │8.5 │ deck/13-EXAM-MECHANICS.md, the time budget     │ 10m  │
   └────┴───────────────────────────────────────────────┴──────┘
   NO new material. Nothing below lecture 22. No MLE, no MoM.
```

---

## 11. THE DEPENDENCY GRAPH (why this order)

```
   H1 indep rules ──┬──▶ Chebyshev sums (35/6)
                    ├──▶ Var(Xbar) ──▶ CLT standard error
                    ├──▶ estimator variances
                    └──▶ Poisson additivity
   ─────────────────────────────────────────────────────
   T2 probability ──▶ T3 rv ──▶ T4 pmf/cdf ──▶ T5 E ──▶ T6 Var
                                                         │
                                       ┌─────────────────┴─────────┐
                                       ▼                           ▼
                                  T7 Chebyshev              T13 sampling ──▶ T14 CLT
                                                                              │
                                                                              ▼
                                                                    T15 estimation ──▶ T16 props
   ─────────────────────────────────────────────────────
   T8/T9 (discretes) and T10/T11/T12 (continuous)
        all hang off T4 and need T5/T6 for their moment questions

   READING ORDER MUST FOLLOW THE ARROWS. That is exactly the pass order.
```

---

## 12. THE ARTIFACT-TO-PASS TABLE (one lookup)

```
   ┌──────────────────────────────────┬──────┬──────────────────────┐
   │ ARTIFACT                         │ PASS │ ROLE                 │
   ├──────────────────────────────────┼──────┼──────────────────────┤
   │ notes/10 (Chebyshev + hidden)    │ 0    │ GATING, read first   │
   │ deck/11-BEYOND-SLIDES.md         │ 0    │ GATING               │
   │ deck/01-CHEATSHEET.md            │ 0,8  │ read aloud           │
   │ notes/01 probability             │ 1    │ theory               │
   │ notes/02 random variables        │ 1    │ theory               │
   │ notes/03 pmf/cdf                 │ 1    │ theory               │
   │ notes/04 expectation/variance    │ 2    │ theory               │
   │ notes/05 continuous rv           │ 2    │ theory               │
   │ L1-7 questions                   │ 2    │ pass 2               │
   │ L8-9 questions                   │ 2    │ pass 2               │
   │ notes/06 binomial/Poisson        │ 3    │ theory               │
   │ notes/07 uniform/normal/exp      │ 3    │ theory               │
   │ L12-13, L14-15 questions         │ 3    │ pass 2               │
   │ notes/08 sampling/CLT            │ 4    │ theory               │
   │ notes/09 estimation              │ 5    │ theory               │
   │ lms-theory p024-025              │ 5    │ 2 unique items only  │
   │ mock + solutions                 │ 6    │ integration gate     │
   │ MTE papers + schemes             │ 7    │ drill, shape first   │
   │ deck/07-PATTERNS.md              │ 7    │ after 2 papers       │
   │ deck/09-QUESTIONS.md             │ 7    │ label your radicals  │
   │ assignments (bundle, 2024-25)    │ 7    │ drill, volume        │
   │ ETE + re-sess IN blocks          │ 7    │ drill under wording  │
   │ deck/12-DRILL.md                 │ any  │ as a ladder, 7 rungs │
   │ deck/04-METHODS.md               │ while│ lookup while solving │
   │ deck/08-TRAPS.md                 │ while│ lookup               │
   │ deck/02-TERMS.md                 │ while│ lookup               │
   │ deck/03-LINGUISTICS.md           │ while│ lookup, before drills│
   │ deck/06-NUMBERS.md               │ while│ lookup               │
   │ deck/05-DISTRIBUTIONS.md         │ while│ lookup               │
   │ deck/10-SLIDE-MAP.md             │ while│ only if you open PDFs│
   │ deck/13-EXAM-MECHANICS.md        │ 8    │ night before         │
   │ lms-MLE, lms-MoM, handout        │ NEVER│ out of scope         │
   │ lms-theory p031-p040             │ NEVER│ out of scope         │
   └──────────────────────────────────┴──────┴──────────────────────┘
```

---

## 13. IF TIME IS SHORT (fallbacks, in priority order)

```
   ONLY 1 DAY (7h20 core, plus 40m review reserve):
      PASS 0 (1h40) + notes/01-03 skim (1h) + notes/06,07 skim (2h)
      + mock (1h30) + cheatsheet (40m) + traps (30m)
      -> the hidden layer + the shelf + the mock. Highest marks/hour.

   ONLY 1 EVENING (3h40):
      PASS 0 (1h40) + the two MTE papers, closed book, then mark (2h)
      -> you will at least recognise every question shape.

   ONLY 1 HOUR:
      deck/01-CHEATSHEET.md read aloud, twice.
      + the five distributions' mean/variance from memory.
      -> the single highest-value hour available.
```

---

## 14. RULES THAT MAKE THIS ORDER WORK

```
   R1  hidden prerequisites FIRST. they gate 4 downstream topics. 1h40.
   R2  read a topic's NOTES before its S&P re-teach deck.
   R3  never read both of a pair cold:
         (notes deck, L1-7)  (notes deck, L8-9)
         (ppt3, L12-13)      (ppt4, L14-15)
   R4  only L10-11 goes first, nothing else teaches Chebyshev.
   R5  every question is done WITH its deck or paper, never read in a batch.
   R6  papers BEFORE assignments (shape first, volume second).
   R7  out-of-scope gets ONE light pass, never more.
   R8  read deck/08-TRAPS.md before opening raw source PDFs. The guided question
       blocks in PASS 2 and PASS 3 may come earlier.
   R9  the mock is the only timed closed-book artifact; do not re-run it
       for comfort, only the failed parts.
   R10 the notes replace the PDFs for learning. Open the PDFs only for the
       Chebyshev deck and the four S&P question blocks.
```

---

## 15. THE DAILY SHAPE (once you are in PASS 1+)

```
   ┌────────────────────────────────────────────────────────┐
   │  09:00  read one notes/ chapter end to end,  no solving │
   │  10:00  solve every worked example in it on PAPER       │
   │  11:00  the pass-2 deck block (if the pass has one)     │
   │  12:00  break                                            │
   │  13:00  deck/12-DRILL.md, one rung                      │
   │  14:00  mistakes: go to deck/04-METHODS for the slot   │
   │  15:00  break                                            │
   │  16:00  the pass gate (blank paper, no notes)          │
   │  17:00  done. No new material after this.              │
   └────────────────────────────────────────────────────────┘
   do NOT read two chapters without solving between them.
   the solve step is where the marks come from.
```

---

Master study order v1, 16 Sep 2026. Time estimates computed from the page counts and the
worked-example density in each notes file. The errors/lies fix and the deep audit still await
the user's go.
