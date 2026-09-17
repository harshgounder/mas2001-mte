# HOW AND WHY: methodology and count rules

Re-audited 17 Sep 2026. This file explains what the worked bank contains, how its counts
are defined, how its study categories were formed, and what cannot be inferred from them.

## 1. Four counts, four units

The numbers below answer different questions. Do not substitute one for another.

| count | unit | meaning |
|---:|---|---|
| 160 | `QUESTION` headers | literal grep count across F1-F15, including two pointer-only stubs |
| 179 | solved-content items | audited instructional items after expanding embedded tables and grouped content, while excluding pointer-only and repeated content |
| 183 | source-question units | solved content split where one worked block combines multiple numbered source questions |
| 180 | drill units | current `00-QUESTIONS-ONLY.md`, after adding the 12 F13 Section A MCQs to the prior 168-unit drill |

The 160 header total is reproducible with:

```sh
rg '^QUESTION ' deck/worked/F*.md | wc -l
```

The other totals require the audit's item rules. A header may be a pointer rather than a
solution, a table may solve several MCQs without separate `QUESTION` headers, and one worked
block may represent more than one numbered source question. This is why header, content,
source-unit, and drill totals differ.

The per-file header counts are:

```text
F1  10   F2   8   F3   6   F4   4   F5   7
F6   6   F7   6   F8  18   F9   8   F10 10
F11  6   F12 20   F13 28   F14  1   F15 22
                                              total 160
```

F13 also contains a 12-MCQ answer table, and F14 contains a 10-MCQ answer table. Those
embedded items explain part of the difference between a header count and a content count.
The audit report records the full reconciliation and the source-unit split.

## 2. Source boundary

The exam-paper set used here contains nine papers in total:

- two MTE papers, 2024-25 and 2025-26;
- seven ETE, summer, or re-session papers.

The bank also draws on course assignments, lecture decks, LMS modules, and course reference
material. External textbook files are a reference layer and do not by themselves establish
that a question originated there. A source label is evidence to inspect, not a corpus-wide
provenance guarantee.

Relevant locations:

```text
md/paper-mte-*.md                         two MTE papers and their schemes
md/paper-ete-*.md, md/paper-resess-*.md  seven ETE-family papers
md/mas2001-assignment-*.md                current assignment sheets
md/ppt*.md, md/lms-*.md                  teaching material
reports/16-SOURCE-PROVENANCE.md           current provenance findings
reports/18-CORPUS-ACCOUNTING.md            gross corpus accounting
reports/22-WORKED-BANK-METHODOLOGY-AUDIT.md this count and claim audit
```

## 3. Scope and selection

The stated MTE scope is lectures 1 to 21, ending with characteristics of a good estimator.
Maximum likelihood, method of moments, Bayesian estimation, confidence intervals, and
hypothesis testing are outside that stated MTE boundary. Some are retained in F8 and F12 as
clearly marked ETE or boundary practice.

Selection favoured supplied MTE questions, then related ETE questions, then course-deck and
assignment practice. The worked bank is a selected study set. It is not a complete copy of
every question in the larger corpus, and it does not establish a fixed cap of two or three
questions for every category.

## 4. Categories, skeletons, and mutations

The decision manual now uses a working 36-category study taxonomy:

```text
16 categories observed in the supplied MTE papers
20 recall-gap categories drawn from the wider course material
36 total study categories
```

These categories group a family with an ask type, such as `Normal/find-param` or
`Binomial/tail`. They are useful because different asks can require different methods inside
the same distribution family.

This is a study taxonomy, not proof that there are exactly 36 possible exam forms. Category
boundaries depend on tagging choices, and a future paper can combine or alter methods in a
way that is not represented here.

The term `skeleton` refers to a recurring structure within a category. The mutation labels
record common changes:

```text
M0  values, names, or context change
M1  given and target are reversed
M2  a condition is added or changed
M3  the target quantity changes
M4  two methods are composed
```

Supporting files:

```text
deck/15-DECISION-MANUAL.md
reports/20-SKELETON-LEDGER.md
reports/11-QUESTION-ATLAS/00-MUTATION-ANALYSIS.md
reports/11-QUESTION-ATLAS/00-TYPE-SPACE-AUDIT.md
```

## 5. Calculation and coverage status

Construction commits recorded batches of arithmetic checks, but that history is not proof
that every current number is correct. The wider audit still lists line-level recomputation as
in progress. Treat the worked solutions as reviewed study material that can still contain an
error, and report any mismatch against the source or a fresh calculation.

The two supplied MTE papers are represented in the bank. That is retrospective coverage of
two known papers. It is not a backtest of future-paper prediction, and it is not a success
rate. The category checklist likewise measures whether the selected study categories have a
pointer, not whether those categories predict a future exam.

## 6. Prediction limits

Past-paper recurrence can support prioritisation, but this corpus is too small and too
dependent for a calibrated probability forecast. In particular:

- two MTE papers do not support a defensible topic probability for the next MTE;
- ETE questions come from a broader syllabus and cannot be treated as equivalent MTE trials;
- course decks and assignments are teaching material, not independent exam sittings;
- repeated or near-duplicate questions inflate naive frequency counts;
- a new combination, wording, or topic can appear even when all known items are covered.

No file in this bank should claim a 100 percent backtest, a guaranteed mark, a guaranteed
topic, or exhaustive coverage of all future question forms.

## 7. Practical use

Use `00-QUESTIONS-ONLY.md` for cold attempts, then follow its pointer into F1-F15. Use
`deck/15-DECISION-MANUAL.md` to choose a method after identifying the distribution and the
ask. Give priority to in-scope MTE material, and treat ETE and confidence-interval material
as boundary or later practice.
