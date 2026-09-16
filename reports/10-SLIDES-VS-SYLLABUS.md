# Slides against the MTE syllabus

Built 14 September 2026. The question: for every lecture in the MTE scope, do teaching
slides exist on disk, and where.

Scope: lectures 1 to 21 of the official lecture plan (`md/mas2001-course-handout/p004.md`
and `p005.md`), which matches `~/PS/syllabus.txt` item for item.

Method: greps over the converted corpus (`md/`, 348 pages) and the raw text layers
(`work/text/`). A mention in a contents list, a plan table or a question paper is not
counted as teaching slides. Page by page source of truth: `reports/01-COVERAGE-MAP.md`.

## 1. Lecture by lecture

| lect | topic (lecture plan) | slides on disk | where |
|---|---|---|---|
| 1 | Introduction of the course | yes, admin, not examined | deck p001-p011 |
| 2 | Basic terminology and concepts of probability theory | yes | deck p012-p050 |
| 3-4 | Random variables, discrete and continuous | yes | deck p051-p062 and p112-p147 |
| 5-6 | PMF, PDF, CDF | yes | deck p063-p087, continuous cdf at p130 |
| 7 | Expectation of random variables | yes | deck p088-p094, continuous side p140-p147 |
| 8-9 | Expectation of random variables, independent random variables | half | expectation and variance p095-p111; the independence rules have NO slides, see 2.2 |
| 10-11 | Chebyshev's inequality | YES (new batch) | S&P L10-11 deck, 9p; CORRECTED 15 Sep, see 2.1 |
| 12 | Binomial distribution | yes | ppt3 p001-p018 |
| 13 | Poisson distribution | yes | ppt3 p019-p028 |
| 14 | Uniform distribution | yes | ppt4 p001-p006 |
| 15 | Normal distribution | yes | ppt4 p007-p037 |
| 16 | Exponential distribution | yes | ppt4 p038-p043 |
| 17 | Sampling: population, sample, standard error | yes | clt p001-p005 |
| 18 | Central limit theorem | yes | clt p006-p018 |
| 19 | Theory of Estimation: parameter, statistic, point and interval estimation | yes | ppt5 p001-p007 |
| 20-21 | Characteristics of a good estimator | yes | ppt5 p008-p021 and lms-theory p001-p030 |

Count: of the 21 MTE lectures, 18 examined lectures have full teaching slides on disk,
lectures 8-9 are half covered, and lecture 1 is an administrative introduction rather than
examined content. Counting that administrative deck as slide coverage gives 19 fully covered
lecture slots, 2 half-covered slots, and all 21 slots accounted for.

## 2. The gaps (re-audited 15 September)

### 2.1 Chebyshev's inequality, lectures 10-11: CORRECTED, the deck arrived

The 15 September batch added `~/PS/S&P L10-11 Chebyshev's inequality.pdf` (9 pages):
theorem statement, the sigma-version restatement, the complement form, and two worked
questions (Q1: E(X)=3, E(X^2)=13 lower bound for P(-2<X<8) = 21/25; Q2: mu=10, sigma^2=4,
four parts including find-C which is MTE 2025-26 Q5 verbatim).

What the old batch showed, kept for the record: every `cheb` hit across the original 11
sources was one of three kinds:

```
  deck p009                 syllabus contents list, one line, never taught in the deck
  handout p003, p004        the syllabus text and the lecture plan row
  assignment 1 p002, p003, p006   two MCQs, two short problems, one application, no teaching
  (the assembled copies repeat the same lines)
```

The topic is named in `~/PS/syllabus.txt` line 8, tagged MTE in the lecture plan, and
Assignment 1 gave it five items in the graded set. Past papers confirm it further: MTE
2024-25 QA3 (statement MCQ) and QB3 (bound vs actual), MTE 2025-26 Q5 (the find-C). Slides
now exist; `03-FORMULA-SHEET.md` section E, `04-QUESTION-BANK.md` section 6, and mock B1
remain the drill.

### 2.2 Independent random variables, second half of lectures 8-9: no slides

Independence is taught on disk only at the EVENT level: deck p027 (Independent Events),
p028 (the proposition and mutual independence), p045 (P(A n B) = P(A) P(B)). After that it
appears only as an assumption inside examples (p057 coins, p072 batteries, p082 dice) and
in the binomial conditions (ppt3 p008, p011). The random variable level rules appear in no
slide:

```
  E(XY) = E(X) E(Y)             only when X and Y are independent
  Var(X + Y) = Var(X) + Var(Y)  needs independence; Var(X - Y) also sums under independence
  Var(aX + b) = a^2 Var(X)      taught, deck p104-p105, covers the Var(2X) style scalings
```

These live only in the formula sheet (`03` sections C and D). One observation worth having:
Assignment 1 question 5 already used the sum rule (variance of the sum of two dice is 35/6,
twice the single die 35/12), so the rule is used in the graded set without being taught.
Ten minutes closes it: recompute Var(sum of two dice) = 35/6 from Var(one die) = 35/12 and
state both rules aloud.

## 3. No slides but out of MTE scope (for later planning)

```
  Bayesian estimation, lecture 24          no slides anywhere
  confidence intervals, lectures 25-28     slides exist, lms-theory p031-p039
  hypothesis testing, lectures 29-36       no slides anywhere
  method of moments, lecture 23            slides exist, lms-method-of-moments, 11 pages
  maximum likelihood, lecture 22           slides exist, lms-maximum-likelihood, 16 pages
```

The MTE block is almost complete on disk. The end term block is mostly missing except the
estimation methods and confidence intervals. If the course keeps going, the material for
lectures 24 and 29-36 has to come from class or the LMS.

## 4. Evidence commands

```
grep -rin 'cheb' md/                              contents lists, plan rows, questions only
grep -rin 'independen' md/notes-lecture-series-01-09/   events and example assumptions only
grep -rn 'E(XY)|E[X]E[Y]' md/                     no hits, the rule appears in no slide
grep -rin 'hypothesis|ANOVA|chi' md/              plan rows and outcome statements only
```

## 5. Disk state note

`~/PS` held two byte identical copies of the CLT deck (sha256 e48f4981ed69). On 14 September
the `(1)` copy was moved to the trash folder; it is recoverable at
`~/.local/share/Trash/files/`. The copy this repo converted and lists in `sources.yaml` is
untouched. Nothing else in `~/PS` or `~/muj-academics` changed.
