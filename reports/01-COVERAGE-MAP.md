# MTE coverage map: every source page against the lecture plan

Built 2026-09-13 from the PDF text layers (`work/text/*.txt`), page by page. Page refs
are the `pNNN` numbers used by the conversion pipeline, so `ppt4 p023` means the 23rd
page of `ppt4-continuous-prob-dist`, which is `md/ppt4-continuous-prob-dist/p023.md`.

## 1. Master map

| lecture plan | topic | source | pages | in MTE |
|---|---|---|---|---|
| 1 | course intro | `notes-lecture-series-01-09` | p001-p011 | yes (admin, not examined) |
| 2 | statistics: definition, scope, limits | `notes-lecture-series-01-09` | p012-p022 | yes |
| 2 | random experiment, sample space, events | `notes-lecture-series-01-09` | p023-p028 | yes |
| 2 | probability axioms, set theory, Venn, conditional | `notes-lecture-series-01-09` | p029-p050 | yes |
| 3-4 | random variable, discrete vs continuous | `notes-lecture-series-01-09` | p051-p062 | yes |
| 5-6 | PMF, CDF, worked examples | `notes-lecture-series-01-09` | p063-p087 | yes |
| 7 | expectation of a discrete rv | `notes-lecture-series-01-09` | p088-p094 | yes |
| 8-9 | variance, shortcut formula, rules of variance | `notes-lecture-series-01-09` | p095-p111 | yes |
| 3-6 | continuous rv, pdf, cdf, expectation, variance | `notes-lecture-series-01-09` | p112-p147 | yes |
| 10-11 | Chebyshev's inequality | YES (arrived 15 Sep) | S&P L10-11 deck |
| 12 | binomial distribution | `ppt3-discrete-prob-dist` | p001-p018 | yes |
| 13 | Poisson distribution | `ppt3-discrete-prob-dist` | p019-p028 | yes |
| 14 | uniform (continuous) | `ppt4-continuous-prob-dist` | p001-p006 | yes |
| 15 | normal distribution | `ppt4-continuous-prob-dist` | p007-p037 | yes |
| 16 | exponential distribution | `ppt4-continuous-prob-dist` | p038-p043 | yes |
| 17 | population, sample, standard error | `lms-standard-error-clt` | p001-p005 | yes |
| 18 | central limit theorem | `lms-standard-error-clt` | p006-p018 | yes |
| 19 | estimation: parameter, statistic, point, interval | `ppt5-estimation-summary` | p001-p007 | yes |
| 20-21 | characteristics of a good estimator | `ppt5-estimation-summary` | p008-p021 | yes |
| 20-21 | same content, expanded, plus real-life numericals | `lms-theory-of-estimation` | p001-p030 | yes |
| 25 | confidence interval for a mean, sigma known | `lms-theory-of-estimation` | p031-p039 | no, out of MTE |
| 22 | maximum likelihood | `lms-maximum-likelihood` | p001-p016 | no, out of MTE |
| 23 | method of moments | `lms-method-of-moments` | p001-p011 | no, out of MTE |
| n/a | course outcomes, assessment scheme | `mas2001-course-handout` | p001-p007 | yes, reference |
| n/a | problem practice | `mas2001-assignment-1` | p001-p006 | yes, practice |
| n/a | problem practice | `mas2001-assignment-2` | p001-p004 | yes, practice |

## 2. The Chebyshev gap (CORRECTED 15 Sep: deck arrived)

Lectures 10 and 11 are Chebyshev's inequality, 2 of 21 MTE lectures. Status history: the
initial batch had no teaching slides for it anywhere; the 15 September batch added
`S&P L10-11 Chebyshev's inequality.pdf` (9 pages). The gap is closed.

Evidence, exhaustive (old batch):

```
grep -ril 'chebyshev' work/text/
  work/text/notes-lecture-series-01-09.txt   line 128, inside the course contents list only
  work/text/mas2001-course-handout.txt       inside the lecture plan table only
  work/text/mas2001-assignment-1.txt         inside Assignment 1 question 5 only
```

In the 147 page deck the word appears once, in the syllabus listing on p009, and never
as taught content. So the topic is examinable, is on the MTE syllabus, is used by
Assignment 1 and by both past MTE papers, and, as of 15 September, has its own deck
(`S&P L10-11`, 9 pages) to revise from.

Handling: read `S&P L10-11`; `reports/03-FORMULA-SHEET.md` covers it in full, and
`reports/04-QUESTION-BANK.md` adds worked problems, including the two variants the
course uses (bound on a sum of dice, bound on a binomial tail). Still the highest
marks-per-page topic in the syllabus.

## 3. Duplication and overlap found

1. `ppt5-estimation-summary` (26 pages) and `lms-theory-of-estimation` (40 pages) are the
   same deck at two trims. Measured by token similarity between every pair of pages, 13 of
   the 26 ppt5 pages have a match above 0.8 similarity in the theory deck, and the pairs
   line up on a one page offset (ppt5 p008 matches lms p009 at 1.00). The theory deck is the
   longer version and adds p031 to p039 on confidence intervals, which are out of MTE scope.
   Revising one is enough. Read ppt5 for the cleaner worked numericals near p022 to p025,
   and the theory deck for anything ppt5 dropped.
2. `~/PS/LMS -Standard Error & Central Limit Theorem.pdf` and its `(1)` sibling are
   byte identical, sha256 e48f4981ed69. Both copies still sit in `~/PS`. Nothing was
   deleted, `sources.yaml` lists the non `(1)` copy once.
3. `~/MUJ/` holds byte identical copies of PPT 3, 4 and 5 (sha256 9cc7f631, b3de25d8,
   2af21af1). Same content, second location on disk.
4. `notes-lecture-series-01-09` is Devore-derived for the RV and distribution theory
   (its slide text matches Devore's phrasing), plus MUJ framing slides at the front.
   The PPT decks cite Gupta and Kapoor. Both are on the handout reference list, so the
   mixed sourcing is expected, not an accident.

## 4. Pages where the text layer is empty or useless

These convert to nothing on their own and can only be recovered by the vision pass.
They are the pages worth checking first once the conversion lands.

| source | pages with empty or near empty text |
|---|---|
| `notes-lecture-series-01-09` | about 60 of 147 pages carry only the footer `MUJ \| DR VIVEK SINGH N`, so their real content is entirely in images |
| `ppt4-continuous-prob-dist` | p022, p023, p024, p025 (the standard normal table region), p002 |
| `lms-standard-error-clt` | p003, p009, p010 |
| `lms-theory-of-estimation` | p023, p024, p025, p026 |
| `lms-method-of-moments` | none |
| `ppt3-discrete-prob-dist` | none |

## 5. What this means for revision

Order of value per page of reading, MTE only:

1. `notes-lecture-series-01-09` p012 to p147, units 1 and 2, 136 pages. Irreplaceable.
2. `ppt3-discrete-prob-dist` p001 to p028 for binomial and Poisson, then
   `ppt4-continuous-prob-dist` p001 to p043 for uniform, normal, exponential.
3. `lms-standard-error-clt` p001 to p018 for standard error and the CLT.
4. `ppt5-estimation-summary` for the estimation block, with `lms-theory-of-estimation`
   p022 to p030 for the extra worked numericals.
5. Chebyshev: read `S&P L10-11` (arrived 15 Sep), then the formula sheet and question bank.

Total MTE-relevant pages: 136 + 28 + 43 + 18 + 26 = 251, plus 7 handout pages.
