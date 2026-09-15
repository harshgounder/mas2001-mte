# Scout: new material batch (received 15 Sep 2026)

Quick scout of the 23 files dropped in ~/PS. Full extraction/classification is the next
phase; this is the reconnaissance.

## 1. What arrived (23 files)

```
  NEW SLIDE DECKS (5, reorganized course decks)
    S&P L1-7.pdf                       108p   the units 1-2 block (was the 147pp deck)
    S&P L8-9.pdf                        37p   expectation + independent rvs
    S&P L10-11 Chebyshev's inequality.pdf  9p  *** THE CHEBYSHEV DECK ***
    S&P L12-13 Discrete Probability Distribution.pdf  28p  (binomial + poisson)
    S&P L14-15 Continuous Probability Distribution.pdf 44p (uniform/normal/exp)
  ASSIGNMENTS (11)
    2024-2025-Assignment 1..5 + Episode 2       (last year's series)
    2025-2026-S&P_assignments_1-5.pdf           17p combined, THIS year's series
       structure: Section A memory MCQs, B concept, C analytical, D application
  PAPERS (13)
    MTE:  S&P_MTE_Sem-3_2024-2025 + 2025-2026 (both!)
    MTE SOLUTION SCHEMES: both years, with "how marks were given"
    ETE:  Sem-3 2024-25, Sem-3 2025-26, Sem-4 x2, Summer 2025-26
    RE-SESS: Sem-3 2025-26, Sem-4 2025-26
```

## 2. THE BIG CORRECTION: Chebyshev has slides after all

The claim "Chebyshev has zero teaching slides" was true of the OLD batch only. The new
batch contains `S&P L10-11 Chebyshev's inequality.pdf` (9 pages): theorem statement,
the k-sigma restatement, the complement form, and TWO worked examples:

- Q1: E(X)=3, E(X^2)=13, lower bound for P(-2<X<8) -> k=2.5, bound 21/25
- Q2: mu=10, sigma^2=4: (i) P(|X-10|>=3) <= 4/9 (ii) complement >= 5/9
  (iii) P(5<=X<15) (iv) constant C with P(|X-10|>=C) <= 0.04

Q2 is LITERALLY the 2025-26 MTE question 5 (same numbers). This deck is the source.

## 3. Papers: what they confirm about the exam

MTE format (both years): 30 marks, 90 min. Sections A (MCQ, 2 marks each), B (4-mark
problems), C (8-mark combined). All compulsory, calculator allowed, "missing data may be
assumed suitably" (THE re-skin licence).

2025-26 MTE questions seen:
```
  A1 pdf integrates to 1 (MCQ)              A2 Poisson mu=sigma (MCQ)
  A3 sufficiency definition (MCQ)           Q4 pdf with k on [0,4], find k, mean, var
  Q5 Chebyshev inverse: find C, P(|X-10|>=C)<=0.04  -> C=10 (this is deck Q2 iv)
  Q6 exponential mean 3: P(>1), P(<3)       Q7 normal n=9 sample mean 6.4..7.2
  Q8 unbiased estimator proof (3 marks)     Q9 typist letters, Poisson chance (5)
```

2024-25 MTE questions seen:
```
  A1 Poisson mean 0.5, Y=2X: E(Y), Var(Y) MCQ
  A2 triangular pdf on [0,2], find F(x) part MCQ
  A3 Chebyshev statement MCQ (spot the wrong forms)
  B1 X-2Y variance, independent Poissons, P(X=1)=P(X=2), P(Y=2)=P(Y=3)
  B2 exponential 1/4: >6, 7..12, <=5, mean, var
  B3 uniform(-1,1): Chebyshev upper bound + actual probability
  B4 train wait uniform [9:00-9:30]: P(wait<6), P(wait>10)
  C1 rainfall normal + at most 2 days + binomial P(X=1)=P(X=2) combined
```

## 4. SIBLINGS CONFIRMED REAL (were flagged "not asked", now asked)

```
  [CONFIRMED] Chebyshev inverse form (find C)          MTE 2025-26 Q5 + deck Q2iv
  [CONFIRMED] Var(X - Y) / X-2Y variance                MTE 2024-25 QB1
  [CONFIRMED] E(XY) = E(X)E(Y) under independence       Re-sess 2025-26 QA1 (MCQ!)
  [CONFIRMED] Var(2X-5Y) linear combination             2025-26 assignment Q11
  [CONFIRMED] Chebyshev uniform with actual comparison  MTE 2024-25 QB3
  [CONFIRMED] Chebyshev bound-vs-actual style           MTE 2024-25 QB3 (same)
  [CONFIRMED] exponential INTERVAL P(a<T<b)             MTE 2024-25 QB2 (7..12 min)
  [CONFIRMED] normal sample-mean n=9 (exact normal)     MTE 2025-26 Q7
  [CONFIRMED] sufficiency concept                       MTE 2025-26 A3 (MCQ)
  [CONFIRMED] consistency with bias formula Tn          Re-sess 2025-26 QA2
  [CONFIRMED] SE direction MCQ                          Re-sess 2025-26 QA3
  [CONFIRMED] Chebyshev statement-spotting MCQ          MTE 2024-25 QA3
  [CONFIRMED] k from E(X), E(X^2) first                  2024-25 style + deck Q1
  [CONFIRMED] uniform wait-time (train)                 MTE 2024-25 QB4
```

## 5. New observations, not seen before

```
  - "Episode 2" assignment (2024-25 series has a split assignment)
  - MTE Section structure A/B/C with fixed mark weights seen in BOTH years
  - "All questions are compulsory" both years; calculators allowed (formula use!)
  - useful z-values and phi() values are PRINTED in the paper (no memory needed for
    table values; they give phi(0.58)=0.219 etc)
  - the mujstella.in watermark: same reseller source for this year's uploads
  - re-sess questions re-use the same skeletons (shelf life pdf, Chebyshev k)
```

## 6. Next phase (pending user GO)

```
  1  extract all 23 files fully into md/ (same pipeline, new sources.yaml entries)
  2  count every question: assignments x11, papers x13, decks x5
  3  classify per the entry schema, update the atlas
  4  rebuild the type space with course-owned evidence only: mark siblings as
     CONFIRMED (appeared) vs HYPOTHETICAL (never seen)
  5  the Chebyshev deck changes its status: [H] -> [taught], keep it first priority
     anyway because it is 2 lectures and now proven to be asked
  6  update reports 09 (errata may need new entries from solution schemes),
     10 (slides-vs-syllabus: L10-11 now HAS slides), 05 (plan), and the atlas
```

## 7. Notes on extraction quality

- all files text-extractable except assignment 3 Episode 2 (240 chars, near-empty:
  likely scanned images; will need the vision pass)
- both solution schemes are scan-heavy (text present but sparse: 1.6-2.4K chars):
  need vision pass to read the marking details
- the mujstella watermark pollutes pdftotext output; the extractor must filter it
  (pattern: single/double char fragments + "mujstella" strings)
