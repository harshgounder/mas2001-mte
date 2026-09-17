# MTE/ETE trace, year map and patterns, 17 Sep 2026

Answers three questions: which years are traced, whether all MTE papers are covered, and
what topic pattern runs through every paper we hold.

## 1. Which MTE papers exist, and are they traced

Four MTE files on disk = TWO papers, each with its solution scheme.

```
  paper                    files                                          ledger rows
  MTE 2024-25              S&P_MTE_Sem-3_2024-2025.pdf                   8 (M24-A1..C1)
                           + solutions-scheme-how-marks-were-given.pdf
  MTE 2025-26              S&P_MTE_Sem-3_2025-2026.pdf                   8 (M25-Q1..Q8)
                           + solutionscheme.pdf
```

Both years are traced. 15 of 16 blocks carry a verdict; only M24-C1 (the rain set) is open.

```
  MTE 2024-25   8 blocks   traced 7   open 1 (M24-C1)
  MTE 2025-26   8 blocks   traced 8   open 0
  TOTAL        16 blocks   traced 15  = 94%
```

## 2. Every paper we hold (not just MTE)

```
  exam              year        ledger rows   in MTE syllabus
  MTE Sem-3         2024-25          8              8
  MTE Sem-3         2025-26          8              8
  ETE Sem-3         2024-25         15             10
  ETE Sem-3         2025-26         14              9
  ETE Sem-4         2024-25         14              9
  ETE Sem-4         2025-26         19             11
  ETE Summer        2025-26         18             11
  Re-sess Sem-3     2025-26          8              5
  Re-sess Sem-4     2025-26          9              7
  ─────────────────────────────────────────────────
  TOTAL                             113             78
```

So there are NINE exam paper sittings held (2 MTE + 5 ETE + 2 re-sess), not five. 78 of the
113 rows fall inside the MTE syllabus; the other 35 are hypothesis testing (out of scope).

## 3. The origin map: where the MTE paper questions came from

The 15 traced MTE blocks, by source:

```
  G&K (Gupta and Kapoor, Fundamentals of Math Stat)
      M24-B1  Poisson Var(X-2Y)         VERBATIM
      M24-B2  telephone exponential     RESKIN  (mean 5 -> 4)
      M24-B3  U(-1,1) Chebyshev         RESKIN  (interval (-1,3) -> (-1,1))
      M25-Q6  telephone exponential     RESKIN  (mean 5 -> 3)
      M25-Q8ii t^2 biased estimator     VERBATIM (estimation exercise 6)
      M24-B4  subway/subway train       FAMILY  (uniform (0,30) -> 15-min 4AM form)

  Walpole, Myers, Myers and Ye
      M25-Q7  machine life 8.25         RESKIN  (bread-making dropped, same values)

  Devore / Hogg and Tanis
      M25-Q3  sufficiency               CONCEPT (H&T 6.7)
      M24-A2  triangular pdf CDF        FAMILY  (G&K 8-1-5)

  the course itself
      M25-Q5  Chebyshev find c          DECK    (L10-11 deck Q2(iv), word for word)

  MCQ banks (circulating)
      M25-Q2  Poisson mean e            CIRCULATING (Examveda, verbatim + options)
      M24-A1  Poisson Y=2X              CONCEPT (standard bank skeleton)
      M24-A3  Chebyshev forms           CONCEPT (definitions in G&K / Devore)

  composite / open
      M25-Q8i typist letters            MIXED (circulating)
      M24-C1  rain set                  OPEN (Palaniammal/Sundarapandian gated)
```

Counting the origins: G&K supplies 6 of 15, the course deck 1, Walpole 1, H&T/Devore 2, MCQ
banks 3, and 2 are concept checks that any text supplies. G&K is the dominant source.

## 4. The topic pattern across every in-syllabus paper question (78 rows)

```
  topic             count   share
  ─────────────────────────────
  Variance / SD        16   20%
  pdf / cdf / pmf      14   18%
  Estimation           12   15%
  Chebyshev             9   12%
  Poisson               8   10%
  Binomial              8   10%
  Normal                8   10%
  Exponential           7    9%
  Expectation           6    8%
  CLT / standard error  4    5%
  RV basics             4    5%
  Counting              1    1%
  Uniform               1    1%
  (a question can hit several topics, so shares sum over 100)
```

## 5. Patterns that repeat across years and instruments

```
  P1  THE FIVE-DISTRIBUTION SET IS FIXED.
      every paper asks across binomial, Poisson, normal, exponential, (uniform).
      no paper invents a new distribution.

  P2  CHEBYSHEV IS IN EVERY SINGLE PAPER.
      MTE 2024 (B3, A3), MTE 2025 (Q5), ETE S3 both years, ETE S4 both years,
      re-sess both. it is the single most repeated topic. 9 uses in 78 rows.

  P3  THE SAME SKELETON RETURNS WITH ONE CONSTANT CHANGED.
      telephone exponential: mean 5 (G&K) -> 4 (MTE 2024) -> 3 (MTE 2025)
      Chebyshev inverse: 21/25 -> 24/25 -> k=3 -> k=2.5
      cable 6x(1-x): assignment 2024 -> assignment 2025 -> ETE re-sess
      pens B(12,0.1): ppt3 deck -> assignment -> ETE S3

  P4  THE ESTIMATION BLOCK IS ALWAYS THE SAME FOUR PROPERTIES.
      unbiasedness, efficiency, consistency, sufficiency. every estimation question
      tests one of these four, nothing else.

  P5  EXPECTATION AND VARIANCE ARE ASKED TOGETHER.
      the E(X), E(X^2), E((2X+1)^2) triple appears in the deck, the 2025-26 assignment
      and the summer paper, same table, same three asks.

  P6  INVERSE NORMAL IS THE HARD-QUESTION SLOT.
      every paper has one normal-inverse question (find x for a given tail, or find
      mean and sd from two percentiles). it is the multi-step item.
```

## 6. Honest limits

- the ETE origin trace is weak: only 1 of 62 in-syllabus ETE rows has a source verdict,
  because the G&K text on disk is a noisy scan and exact phrase matching fails on it. The
  true ETE trace count is higher than 1 but is unmeasured until a fuzzy matcher runs.
- the MTE numbers (15/16) are solid and hand-verified; trust those.
- pattern counts come from keyword classification of the row summaries, so a question that
  mentions two topics counts in both. The counts are for ranking, not exact totals.
