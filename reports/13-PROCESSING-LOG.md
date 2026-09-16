# Batch 2 processing log

Per-unit record for conversion, source checking, atlas entry, deduplication and count work.
A unit is not complete until every column below is complete.

| unit | sources | pages | conversion | source check | atlas | dedup | counts |
|---|---|---:|---|---|---|---|---|
| U01 | four MTE papers and schemes, 2024-25 and 2025-26 | 15 | complete | complete | open | open | open |
| U02-U19 | see `12-NEW-BATCH.md` | 283 | not started | not started | not started | not started | not started |

## U01: MTE papers and solution schemes

### Conversion

- Commit `32265ae` converted all 15 pages across four labels with `glm-5.3-flash`.
- The manifest holds an `ok` record for each U01 page.
- Labels: `paper-mte-2025-26`, `paper-mte-2025-26-scheme`, `paper-mte-2024-25`, and
  `paper-mte-2024-25-scheme`.

### Source check, 16 September 2026

All 15 page files were reviewed against the rendered source. The handwritten scheme pages
with disputed details were rendered again at 300 dpi. Corrections include the 2025 paper
date, question labels, page labels, red mark allocations, the 2024 scheme's printed 2.6,
and a missing factor of 2/3.

The earlier verifier report mixed content defects with expected URL filtering. Fifteen
reported footer omissions were the result of `PROMPT.txt` rule 7, not missing course content.
The prompt now says to preserve the visible footer wording and replace only the domain with
`[domain omitted by repository policy]`. One reported strict-inequality defect also did not
survive the 300 dpi check: the source prints `<=`, and the transcription already matched it.

The review found three source defects, recorded as errata 19 to 21:

1. The 2024 paper's QA2 CDF key marks B, but direct integration gives option D.
2. The 2025 scheme's Q4 normalization and mean lines print infinite integration bounds even
   though the stated support and the numerical work use 0 to 4.
3. The 2025 scheme's Q8(ii) changes `E(t^2) - theta^2 != 0` into `E(t^2) != 0`; the correct
   inference is `E(t^2) != theta^2`.

### Work still open

- Write full atlas entries for every U01 question using the 19-field schema.
- Give every question a NEW, DUPLICATE or UPDATED verdict against the batch-1 corpus.
- Update `00-COUNT-REGISTER.md` and the confirmed-question type map.
- Reshape the mock paper only after those question-level comparisons are recorded.
