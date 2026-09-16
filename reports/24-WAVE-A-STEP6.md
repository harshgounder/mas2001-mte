# Wave A step 6: ETE extraction and the teaching tail, 16 Sep 2026

Status of the two buckets that block a full trace.

## ETE tail: mostly resolved

The ETE block dump (`~/mas2001-devore/ete-blocks.json`, 82 blocks) covers the ledger's 97 ETE
ids except 15. A key-mapping bug was found and fixed: the summer paper dump numbers items as
`E25SUM-1` while the ledger uses `ete-E25SUM-Q1`, so those 18 rows never matched before. With
the alias added, ETE unsearched dropped from 60 to 7.

```
  ETE 97 rows:  open 86, strong 2, family 2, unsearched 7
  the 7 unsearched: E24S3-A1, E24S3-B6, E25S3-A1, E24S4-A4, E25S4-A10, E25S4-B6, E25S4-C2
  these are short-label rows (for example "F-test compares variances") with no block in the
  dump. They need the rebuilt extraction, not a guess.
```

## Teaching tail: 30 rows stay pending, honestly

The 30 ppt/lms teaching rows are ORDERED PLACEHOLDERS seeded by the builder with no page
references and no summary (see `seed_teaching` in `build_question_instance_ledger.py`). The
declared counts (ppt3 6, ppt4 7, ppt5 5, clt 5, lms-theory 7) come from the count register's
counting rule, which excludes display examples.

A paragraph-level scan of the converted decks finds problem-shaped paragraphs but the counts
do not align:

```
  ppt3      want 6   scan finds 6    (5-coin, pens 12, pens part iii, Poisson ex 1-3)
  ppt4      want 7   scan finds 11   (normal chain, exponential, etc, includes display rows)
  ppt5      want 5   scan finds 2
  clt       want 5   scan finds 13   (most are concept statements, not problems)
  lms-theory want 7  scan finds 5
```

Forcing a 1:1 map on these would put a wrong statement against a row id, which is exactly the
fabrication this project forbids. They stay blank and unsearched until the count register is
extended to carry page refs for the ppt/lms decks (the deck-01 rows already do, which is why
those 30 resolved cleanly).

## What this leaves

```
  unsearched 119 =
    74   the out-of-scope assignment rows (marked scope OUT; no match expected)
    30   the teaching placeholders above
    15   the ETE tail (7) plus the bundle-2025 tail (5) plus 3 misc
  everything else carries a verdict.
```

## Next clean moves (in order)

1. extend the count register with page refs for ppt3/ppt4/ppt5/clt/lms-theory, then the 30
   teaching rows resolve mechanically;
2. fetch the four remaining concept MCQs from the MCQ-bank category pages (wave B);
3. decide the final opens (C1 rain set, pens) which remain gated on external texts.
