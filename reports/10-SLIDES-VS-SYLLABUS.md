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
| 10-11 | Chebyshev's inequality | NO | no teaching slide anywhere, see 2.1 |
| 12 | Binomial distribution | yes | ppt3 p001-p018 |
| 13 | Poisson distribution | yes | ppt3 p019-p028 |
| 14 | Uniform distribution | yes | ppt4 p001-p006 |
| 15 | Normal distribution | yes | ppt4 p007-p037 |
| 16 | Exponential distribution | yes | ppt4 p038-p043 |
| 17 | Sampling: population, sample, standard error | yes | clt p001-p005 |
| 18 | Central limit theorem | yes | clt p006-p018 |
| 19 | Theory of Estimation: parameter, statistic, point and interval estimation | yes | ppt5 p001-p007 |
| 20-21 | Characteristics of a good estimator | yes | ppt5 p008-p021 and lms-theory p001-p030 |

Count: of the 21 MTE lectures, 17 have full teaching slides on disk, lectures 8-9 are half
covered (the expectation and variance rules exist, the independence rules do not), and
lectures 10 and 11 have no slides at all.

## 2. The two gaps

### 2.1 Chebyshev's inequality, lectures 10-11: no slides anywhere

Every hit for `cheb` in the corpus is one of three kinds:

```
  deck p009                 syllabus contents list, one line, never taught in the deck
  handout p003, p004        the syllabus text and the lecture plan row
  assignment 1 p002, p003, p006   two MCQs, two short problems, one application, no teaching
  (the assembled copies repeat the same lines)
```

No slide defines the inequality, proves it or works an example. The topic is named in
`~/PS/syllabus.txt` line 8, tagged MTE in the lecture plan, and Assignment 1 already gave it
five items in the graded set: two MCQs (p002 questions 5 and 10), two short-answer problems
(p003 questions 5 and 6, the dice bound 35/54 and the 600-throw bound 19/24), and the marks
application (p006 question 4). This repo carries it in three places instead:
`03-FORMULA-SHEET.md` section E, `04-QUESTION-BANK.md` section 6, and mock question B1.

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
