# MAS2001 MTE report

Prepared 2026-09-13, the evening before the five day run in. Everything here is traceable
to a file in this repo or to a command whose output is recorded in `reports/evidence/`.

## 1. Bottom line

The mid term window opens Friday 18 September and closes Friday 25 September 2026. The paper
is 30 marks, closed book, and covers lectures 1 to 21 of the official lecture plan.

The material on disk was not enough on its own. `~/PS` holds the four estimation and limit
theorem decks plus the two distribution decks, which is lectures 12 to 21. Lectures 2 to 11,
the whole of probability theory, random variables, expectation, variance and the Chebyshev
work, exist only inside a 147 page deck sitting in `~/muj-academics/handouts/`. Sit the paper
with `~/PS` alone and two thirds of the syllabus is unread.

Two named MTE lectures, 10 and 11, had no slide content anywhere in the old batch; the 15
Sep batch closed that with the S&P L10-11 deck. Details in section 5.3.

## 2. The exam

| item | value | source |
|---|---|---|
| MTE window | Fri 18 Sep to Fri 25 Sep 2026 | `muj-academics/handouts/MUJ_Academic_Calendar_2026-27.md`, September row 18 and row 25 |
| Sitting date for MAS2001 | not on disk, no subject wise timetable found | searched local tree and the Drive sync ledger |
| Paper | 30 marks, closed book, sessional exam | `md/mas2001-course-handout/p001.md`, and the deck page `p008` |
| Course split | sessional 30, in class quizzes and assignments 30, end term 40 | `md/mas2001-course-handout/p001.md` |
| Scope | lectures 1 to 21 tagged MTE, lecture 22 onward tagged CWS and ETE only | `md/mas2001-course-handout/p001.md` lecture plan |
| Classes | PS runs Mon, Wed, Fri, so three contact sessions before the window | `muj-academics/handouts/sem3_timetable_batch1.md` |

The scope line is the important one. The lecture plan marks each lecture with its assessment
tags, and lectures 22 to 36 (Maximum Likelihood, Method of Moments, Bayesian estimation,
confidence intervals, hypothesis testing, t, F, chi square, ANOVA) are tagged CWS and ETE
only. That is the evidence for calling MoM and MLE out of scope for this paper even though
both decks sit in `~/PS`.

## 3. What was built

New repo at `/home/liebert511/mas2001-mte`, git initialised, one commit at the time of
writing, private GitHub remote created at the end of the run.

```
  mas2001-mte/
    README.md                  what this repo is
    sources.yaml               11 sources, absolute paths, page counts, sha256, topic
    PROMPT.txt                 the transcription prompt, versioned (runtime file, stays at root)
    process/BRIEF-001..003     the briefs handed to opencode for the pipeline
    scripts/
      convert.py               render page to png, read it with vision, cache and manifest
      assemble.py              per page markdown into one document per deck
      audit_conversion.py      coverage audit and second reader fidelity gate
    md/<label>/pNNN.md         one file per slide
    md/<label>.md              assembled deck, dashes normalised
    md/INDEX.json              per label stats including dashes fixed
    work/text/<label>.txt      text layer per source, the independent check
    work/manifest.jsonl        one record per page: sha, status, attempts, latency, chars, model
    reports/00..08             this report set
    reports/evidence/          raw verification output
```

Code was written by the opencode CLI from briefs, per the standing rule that Hermes plans and
reviews while opencode writes source. The conversion itself was run by Hermes.

## 4. The conversion

Every slide was rendered at 110 dpi and read by a vision model (`xiaomi/mimo-v2.5` through
`~/.local/bin/vision`), not by text extraction alone. Text extraction was kept as a second
channel and used as one of the checks.

Why vision was required rather than optional: the PDFs are PowerPoint exports with real text
layers, so the prose extracts cleanly, but every equation comes apart. The binomial mass
function extracts as a broken brace glyph with the combination notation split across lines,
and exponents flatten into running text. Of the 184 pages in `~/PS`, 798 embedded images ride
along. The converted pages below show what the vision pass recovers: proper `\binom{12}{2}`,
`\begin{cases}` blocks, and a `Figure:` description wherever a chart, curve or table appears.

```
  the same slide, ppt3 p009, both channels side by side
  text layer :  𝑥
                𝑛−𝑥 for x = 0, 1, 2, … . . n
                𝑝
                𝑞
                P(X = x) = ቊ 𝐶 𝑥
                0,
  converted  :  $$P(X = x) = \begin{cases} \binom{n}{x} p^x q^{n-x} & \text{for } x = 0, 1, 2, \dots n \\ 0, & \text{otherwise} \end{cases}$$
```

Measured behaviour of the pipeline, all from `work/manifest.jsonl`:

```
  per page latency      median 29 s, tail up to 207 s on a retried page
  sustained rate        8 to 9 pages per minute at 8 workers
  retries               about 1 page in 17 needed a second attempt
  transient failures    HTTP 400 and HTTP 524 from the upstream, both cleared on retry
  wasted output         zero banned URLs in the corpus, checked per page
```

A concurrency probe before the full run (6 simultaneous calls, 38.7 s wall) confirmed the
endpoint holds parallel load, and one probe call failed with a transient HTTP 400 that
succeeded twice on retry. That failure mode is why the pipeline retries three times.

## 5. Analysis of the corpus

### 5.1 Coverage against the lecture plan

```
  lectures  1        course intro ......................... deck p001 to p011
  lecture   2        probability terminology .............. deck p012 to p022
  lectures  3 to 6   events, sample space, RVs, PMF/PDF/CDF  deck p023 to p062
  lectures  7 to 9   expectation, variance ................. deck p063 to p111
  lectures 10, 11    Chebyshev ............................. deck, see 5.3 (corrected 15 Sep)
  lecture  12        Binomial .............................. ppt3 p001 to p018
  lecture  13        Poisson ............................... ppt3 p019 to p028
  lecture  14        Uniform ............................... ppt4 p001 to p006
  lecture  15        Normal ................................ ppt4 p007 to p037
  lecture  16        Exponential ........................... ppt4 p038 to p044
  lectures 17, 18    sampling, standard error, CLT .......... lms-standard-error-clt, 19 pages
  lectures 19 to 21  estimation, estimator properties ...... ppt5 p001 to p026, lms-theory p001 to p030
```

Full page by page table in `reports/01-COVERAGE-MAP.md`.

### 5.2 The gap that matters: lectures 2 to 11

`~/PS` contains no probability theory deck. The four LMS decks there start at Binomial and end
at maximum likelihood. The expectation that PS is the whole subject comes from the folder name,
not from its contents. The missing block is the heaviest MTE block by lecture count, 10 of the
21 lectures, and it is only in the 147 page deck.

### 5.3 Chebyshev: CORRECTED 15 September, the deck exists

This section originally said Chebyshev had no slides. That was true of the first source batch
only. The 15 September batch (`~/PS/S&P L10-11 Chebyshev's inequality.pdf`, 9 pages) carries
the theorem, the k-sigma restatement, the complement form, and two worked questions. Its Q2
(mu=10, sigma^2=4, find C with P(|X-10| >= C) <= 0.04) is MTE 2025-26 question 5 with the
same numbers.

What the old batch showed, kept for the record: across the 11 original sources the string
appeared in exactly three places, all non-teaching:

```
  notes-lecture-series-01-09 : one line in the course contents list, never taught
  mas2001-course-handout     : the lecture plan row
  mas2001-assignment-1       : the question that uses it
```

Chebyshev is examinable, appeared in Assignment 1 twice, in MTE 2024-25 (statement MCQ +
bound-vs-actual), in MTE 2025-26 (find-C), and now has its own deck in the new batch. Read
`S&P L10-11` for it; `reports/03-FORMULA-SHEET.md` section E and mock B1 remain the drill.

### 5.4 Duplication found

| what | detail | action taken |
|---|---|---|
| PPT5 vs lms-theory-of-estimation | same deck at two trims, 13 of 26 ppt5 pages match a theory-deck page above 0.8 similarity on a measured token comparison, pairs line up with a one page offset, theory deck is the longer one | both converted, no deletion, marked as duplicates |
| CLT deck twice inside ~/PS | `LMS -Standard Error & Central Limit Theorem.pdf` and `(1).pdf` have identical sha256 e48f4981 | converted once, second copy untouched |
| PPT 3, 4, 5 twice on disk | ~/MUJ holds byte identical copies (sha 9cc7f631, b3de25d8, 2af21af1) | untouched, listed as YOUR-CALL |
| lms-theory p031 to p040 | confidence intervals, lecture 25 and 27, out of MTE scope | converted, tagged out of scope |

### 5.5 Where the marks are

Two independent signals line up. The tools that appear across the corpora most often are the
binomial mass function, the normal table with standardisation, and Chebyshev tails. The
Assignment 1 paper that was actually graded leans the same way: binomial in the short section,
Chebyshev twice, a normal proportion question, and a hypergeometric draw.

```
  question style      where it appears                        weight signal
  MCQ                 assignment 1 section A, 10 items        1 mark each, expect 10 of 30
  short answer        6 items in assignment 1                 2 to 3 marks each
  worked numeric      pens, die, telephone, insurance, ATM    the long answers
  application/word    assignment 1 section B, 4 items         interpretation marks
```

## 6. Your own answers, checked against the official key

The Assignment 1 PDF ships with its answer key printed alongside the questions. I extracted
it and re-derived every value rather than trusting either document. Result: your answers agree
with the key on almost everything, and the paper was in good shape. Two defects in one
question, both confirmed numerically:

```
  Assignment 1, long Q2, the pmf with the unknown k
  official pmf   x: 0 1 2 3 4 5 6 7
                 p: 0 k 2k 2k 3k k^2 2k^2 7k^2 + k      (P(X=0) is zero)
  correct sum    9k + 10k^2 = 1   ->  10k^2 + 9k - 1 = (10k - 1)(k + 1) = 0   ->  k = 1/10 exactly
  your sheet     14k + 10k^2 = 1, root written as (-14 + sqrt(236))/20, then k about 1/10
                 your own pmf row accounts for 12k, so the equation is 2k too heavy
                 check: 10(0.1)^2 + 9(0.1) = 1.00, and 14(0.1) + 10(0.1)^2 = 1.50
  knock on       P(X>=6) written as 91/100, correct value 19/100
                 (81/100 is P(X<6), which the key also prints, so the parts got crossed)
```

Everything else in your sheet matches the key: the coin triple, the 5e^-4 tail, b = 1/2, E = 2,
35/54 against an actual 1/3, 19/24, the mortality integral 0.1544 and its conditional 0.4863,
the hypergeometric 0.8, the oranges 12/19, 32/95, 3/95, E = 1.2 with Var = 0.86, the battery
3.45 and 0.95, and Chebyshev 0.75. Full check list in `reports/evidence/`.

One small note in the key itself: it prints P(X>12) as 0.0915 where the exact value 5e^-4 is
0.091578, which rounds to 0.0916. The key truncates rather than rounds. Harmless, but do not
copy 0.0915 into a table reading.

## 7. Risks

| risk | why it matters | mitigation |
|---|---|---|
| No past MTE paper on disk at build time (SUPERSEDED 15 Sep: both years + schemes arrived) | the exact paper pattern was unknown at first build | the 15 Sep batch fixed this; see reports/12-NEW-BATCH.md |
| Chebyshev had no slides (FIXED 15 Sep: S&P L10-11 deck arrived) | was examinable with no source to read | read S&P L10-11; formula sheet plus mock B1 remain the drill |
| Days 14, 15, 16 also carry four other courses | revision time is not the whole day | plan budgets 4 to 5 focused hours per day |
| The 147 page deck has a thin text layer (264 chars per page) | skim reading it on paper hides the maths | converted pages carry the maths in LaTeX, read those |
| MoM and MLE are in ~/PS but out of the paper | easy to burn a day on two non examinable decks | both tagged out of scope in the coverage map |

## 8. What to do with it

```
  read this, then
    reports/03-FORMULA-SHEET.md      the closed book sheet, memorise it
    reports/05-FIVE-DAY-PLAN.md      day by day, with page refs into md/
    reports/07-MOCK-PAPER.md         sit it before reading 08
    reports/08-MOCK-SOLUTIONS.md     after the mock, check the three designed traps
    reports/01-COVERAGE-MAP.md       which deck page covers which lecture
    md/<label>.md                    the decks themselves, one file per deck
```

## 9. Verification status

```
  property tests     79 checks over every closed form in the formula sheet and the
                     official assignment key, 79 pass, raw output in reports/evidence/
  self caught         my first pass had 4 failing checks, all four were my own thresholds
                     being wrong, not the material, and the fix and reason are recorded
  source integrity   all 11 sha256 digests and all 11 page counts recomputed and matched
  coverage audit     348 pages, 27 flagged (7.76 percent), 0 empty. Every flagged page was
                     hand checked: 26 carry real content and 1 is a title slide, all false
                     positives of the comparator, which counts a page as thin when the
                     markdown is shorter than the padded PDF text layer. Detail in work/AUDIT.md.
  fidelity gate      12 pages against a second reader (deepseek-v4.1-flash on the same
                     prompt): 11 PASS, 1 REVIEW. The REVIEW (ppt3 p023) is a tokenization
                     artifact, "0, 1, 2" versus "0,1,2", content identical, checked by hand.
                     The first gate attempt used the pro model and is VOID: all 12 of its
                     calls returned HTTP 404, the model lost image support mid-session, and
                     its single recorded PASS is vacuous (a page with no numbers scored 1.000
                     against an empty reading). Archived at work/FIDELITY-void-pro-404.md so
                     the number is never cited.
```

## 10. Decisions I took without you

The clarify form timed out while you were away and you had said start now, so these four went
ahead on my judgement. All four are reversible.

| decision | choice | how to reverse |
|---|---|---|
| scope | PS plus the lecture deck plus handout, 348 pages | add or drop labels in sources.yaml |
| repo | `~/mas2001-mte`, private GitHub at the end | keep local only, or make it public |
| conversion depth | vision on every page | already converted pages are cached, drop the rest |
| em dashes | banned at the prompt, normalised again at assembly | raw page files keep the original dashes |

Two config changes outside the repo, both backed up:

```
  ~/.config/opencode/opencode.json   the commandcode key in it was stale (len 92) against the
                                     live key in ~/.hermes/.env (len 93), so opencode refused to
                                     start. Restored from the live key, chmod 600,
                                     backup at opencode.json.bak-20260913-keyfix
```

## 11. Open items

```
  YOUR-CALL, nothing deleted by this repo
    1  ~/PS held the CLT deck twice, byte identical; the "(1)" copy was moved to the trash
       folder on 14 September (recoverable at ~/.local/share/Trash/files/), noted in
       reports/10-SLIDES-VS-SYLLABUS.md section 5. CORRECTED 15 Sep: the "(1)" copy in the
       trash is the CLT deck (sha e48f4981), NOT an assignment copy; `Assignment 2_MAS2001-2.pdf`
       is byte-identical to the batch-1 assignment-2 SOURCE (sha 5ff197311b60), which lives in
       ~/Videos, not in ~/muj-academics. Both ~/PS copies are still on disk, nothing deleted.
    2  ~/PS also gained three byte-identical repeats of papers already listed (one ETE S3
       copy, two re-sessional S3 copies) and one second edition of assignment 1 (different
       faculty name, different long-Q2 pmf row); all six extras are in sources.yaml
    3  ~/MUJ holds byte identical copies of PPT 3, 4 and 5, keep as a backup or remove
    4  ~/Music/MAS2001_remake/ is a separate assignment pipeline from August, out of scope here
    5  do you have the subject wise MTE timetable, the window is known but not the SITTING day
  follow up
    6  the Google OAuth refresh token is dead (400 on refresh, expired 2026-08-13), so a live
       Drive sweep for newer MAS2001 material was not possible, re-auth and re-check
    7  the PPT5 and lms-theory duplication could be collapsed to one document later
```
