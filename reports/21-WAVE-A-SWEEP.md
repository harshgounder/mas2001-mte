# Wave A provenance sweep, 16 Sep 2026

First real pass at the 100%-trace target: every row in the question instance ledger
carrying a description and an evidence-backed verdict. Runs offline, reads only the
reference corpora already on disk, and never overwrites a human-researched verdict.

## What ran

`scripts/sweep_provenance.py` (two deterministic passes)

```
  pass 1  DESCRIPTION BACKFILL
          blank summary -> real statement text, by block index, from the source
          file. A backfill only lands when the source's marker reproduces the
          DECLARED block count exactly. On a mismatch the row stays blank and
          the source is recorded, so nothing is fabricated from a misaligned file.

  pass 2  PROVENANCE SWEEP
          each row's text is scored against 4 reference corpora by distinctive
          5-gram overlap (stopwords removed), verdict by hit count:
             verbatim   >=10 hits and >=20% of the row's grams
             strong     >=6 hits
             family     >=3 hits
             open       searched, no source
             unsearched no usable text
          frozen (never touched): the 16 MTE rows (human sourced, web-verified),
          the 30 four-deck rows, and cheb-Q1/Q2.
```

## Result: before -> after

```
  descriptions resolved   173 -> 274   (101 filled)
  descriptions pending    210 -> 109
  traced-like verdicts     37 ->  51
```

```
  verdict            count
  unsearched           201
  open                 130
  family                 9
  exact-text lead        9
  verbatim slide source  7
  CONCEPT                5
  RESKIN                 3
  strong                 3
  exact match            3
  RESKIN + CIRCULATING   2
  verbatim               2
  probable lead          2
  FAMILY / VERBATIM / OPEN / DECK / MIXED / family lead  1 each
```

per group:

```
  assignments-2024   open 39, family 5, strong 3, verbatim 2, unsearched 76
  assignments-2025   open 42, family 4, unsearched 6
  teaching           unsearched 57, open 3
  ete                unsearched 60, open 37
  chebyshev          open 1, unsearched 2
  mte                16 (frozen, human)
  four-decks         30 (frozen, human)
```

## Real findings this pass produced

1. ASSIGNMENT 4 AND ASSIGNMENT 5 ARE OUT OF MTE SCOPE. Both are hypothesis testing
   (t-test, F-test, ANOVA, type I/II errors). They sit in the ledger as 40 rows with
   empty summaries. They should not be in an MTE-scope corpus at all.
2. ASSIGNMENT 3 IS MOSTLY OUT OF SCOPE TOO. Its 25 items are MLE, method of moments,
   Bayesian estimation and confidence interval theory, all out of the MTE syllabus.
3. asgn-2024-25-3-ep2 IS EMPTY. The extracted text is 41 characters of whitespace.
   Its 25 rows carry no source and cannot be backfilled.
4. the source texts use DIFFERENT markers per file (Qn, n_dot, Example N, Roman
   subsections), which is why a naive sweep under-counts. The resolver now tries
   several markers and gates each on the declared count.
5. chebyshev deck repeats markers across pages (Q2 appears three times); the resolver
   dedupes by marker id.

## What is still open (honest)

```
  109 rows with no description:
      asgn-2024-25-3      25  (out of scope, but should be labelled so)
      asgn-2024-25-3-ep2  25  (empty source, acquisition needed)
      asgn-2024-25-5      24  (out of scope)
      30 teaching rows        (deck examples need an Example-N resolver tune)
      5  asgn-2025-26-1       (block-index drift at the tail)
  201 rows still unsearched:
      ete 60   (report 17 ids, need the rebuilt extraction)
      teaching 57  (short labels have no searchable text yet)
      asgn-2024 76
```

## Files

```
  scripts/sweep_provenance.py                      the sweep engine
  reports/evidence/wave-a-sweep-20260916.json      run record + per-group tallies
  reports/evidence/question-instance-ledger.csv    updated (274 descriptions, 51 verdicts)
```

The repo's own ledger test still passes: 43 tests OK, 383 rows.
