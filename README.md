# mas2001-mte

Exam preparation repo for **MAS2001 Statistics and Probability**, Mid-Term Examination,
Manipal University Jaipur, B.Tech ECE Semester III, Section B.

Created 2026-09-13. MTE window per the official MUJ academic calendar: Friday 18 September
2026 to Friday 25 September 2026. Re-sessional examination: 6 to 7 October 2026.

## Why this repo exists

The course material was sitting as PowerPoint-exported PDFs spread across three
directories. The PDFs carry real text layers, but every equation in them is broken
by text extraction: exponents are flattened, binomial coefficients lose their
structure, and piecewise definitions come out as garbage. Roughly 800 embedded
images across the decks mean the formulas and diagrams are rasterised anyway.

So this repo holds a faithful markdown conversion of the whole MTE corpus, produced
page by page with a vision model, plus the analysis and revision material built on
top of that conversion.

## Source corpus

| label | pages | author | topic |
|---|---|---|---|
| ppt3-discrete-prob-dist | 28 | Dr. Ashish Kumar | discrete distributions, binomial |
| ppt4-continuous-prob-dist | 44 | Dr. Ashish Kumar | uniform, normal, exponential |
| ppt5-estimation-summary | 26 | Dr. Shamshad Ur Rasool | estimation, good estimator |
| lms-theory-of-estimation | 40 | Dr. Shamshad Ur Rasool | estimation, expanded |
| lms-standard-error-clt | 19 | Dr. Ashish Kumar | sampling, standard error, CLT |
| lms-method-of-moments | 11 | Dr. Ashish Kumar | method of moments |
| lms-maximum-likelihood | 16 | Dr. Ashish Kumar | maximum likelihood |
| notes-lecture-series-01-09 | 147 | Dr. Vivek Singh | lecture series 1 to 9, holds units 1 and 2 |
| mas2001-course-handout | 7 | Dept. of Maths and Stats | outcomes, assessment scheme |
| mas2001-assignment-1 | 6 | course faculty | problem set |
| mas2001-assignment-2 | 4 | course faculty | problem set |

Total 348 pages. The first seven came from `~/PS`. The 147 page lecture deck and the
course handout came from `~/muj-academics`, and they are the only place the MTE
syllabus units 1 and 2 exist on disk.

## Layout

```
sources.yaml       source manifest: absolute path, pages, author, sha256
PROMPT.txt         the transcription prompt, read at runtime by the pipeline
BRIEF-001-*.md     the brief handed to opencode for the pipeline code
scripts/           convert.py and assemble.py
sources -> md ->   md/<label>/pNNN.md (per page), md/<label>.md (assembled)
work/pages/        rendered PNGs
work/manifest.jsonl  one line per page attempt: status, latency, chars, flags
reports/           the MTE analysis and revision material
```

## Ground rules in force

1. Nothing in the source directories is moved or deleted. This repo reads them.
2. Source code in `scripts/` is written by opencode CLI, not by the agent. Hermes
   writes briefs, audits diffs, runs the code, and commits.
3. Every converted page is verifiable: the PNG it came from is kept, its sha256 is
   in the manifest, and the page markdown is diffable against the PDF text layer.
