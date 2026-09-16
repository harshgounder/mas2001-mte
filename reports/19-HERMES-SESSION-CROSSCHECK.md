# Hermes session cross-check and correction register, 16 Sep 2026

Session audited: `20260916_090342_906ae3`, titled `Load PS course data and me...`.
The database read used the exact session id supplied by the user, not either similarly
named session. The latest stored message is id 281530.

## What the session actually did after the earlier handoff

1. It downloaded Hogg and Tanis 9e and Goon, Gupta and Dasgupta volume 1 outside the repo.
2. It started a page-by-page Tesseract OCR job for a scan mislabeled as Palaniammal,
   followed by the Goon, Gupta and Dasgupta scan. The first scan's title pages identify it
   as Davenport, Probability and Random Processes, not Palaniammal.
3. It searched the two MTE papers against Devore, Gupta and Kapoor, Hogg and Tanis, and
   web question sites.
4. It pushed commit `5976d5d` to PR 10 with a sixteen-row MTE table.
5. It began an ETE phrase sweep, but its parser extracted only 46 of the 97 registered ETE
   blocks. Four paper groups returned zero blocks: E24S3, E25S4, R25S3, and R25S4.
6. It ended after that partial sweep. No completed 97-block ETE provenance result was
   written to the repo.

The session table contains 679 physical message rows. That number includes replay and
compaction artifacts, so it is not a count of 679 distinct research actions.

## Corrections to claims in PR 10

| issue | prior claim | cross-check result | correction |
|---|---|---|---|
| source files | Palaniammal and Sundarapandian PDFs were on disk | neither is verified; the supposed Palaniammal scan is Davenport | file renamed outside repo and report 16 corrected |
| MTE provenance | all 16 blocks traced; no block original | after the follow-up search, 10 have a source or family lead, 5 are generic concept checks, and composite C1 remains open | report 16 corrected; originality claim removed |
| ETE provenance | sweep in progress over all 97 | parser produced only 46 blocks and skipped four paper groups | treat sweep as incomplete and do not cite its phrase hits as provenance |
| deck pages | 109, 38, 29, 45 and Chebyshev 10 | PDF and `sources.yaml` counts are 108, 37, 28, 44 and 9 | report 18 corrected |
| four-deck blocks | 11 + 3 + 6 + 5 = 25 | visual page audit gives 13 + 4 + 6 + 7 = 30 | report 18 and deck ledger corrected |
| total blocks | 378 exact | corrected gross count is 383 | report 18 corrected |
| duplicate treatment | known duplicates not double counted | the arithmetic included five row-5/row-6 overlaps | gross and net counts separated |
| text-layer sufficiency | vision not required to count questions | text-marker counting missed image-based blocks | page images remain required for completeness checks |

## Evidence layers now present

- `reports/evidence/corpus-page-ledger.csv`: exactly 646 declared source pages, with source
  hash, conversion state, text hash, markdown state, image state, and marker hints.
- `reports/evidence/deck-block-ledger-20260916.csv`: 30 manually verified blocks across
  L1-7, L8-9, L12-13, and L14-15, including the five blocks missed in PR 10.
- `reports/evidence/external-source-inventory-20260916.csv`: hash-locked external reference
  assets, verified identities, text state, and explicit absent rows for Palaniammal and
  Sundarapandian.
- Report 17: 97 ETE blocks with scope verdicts. This is an intake ledger, not a completed
  provenance ledger.

## Pipeline defects found while checking the new ledger

The new page-ledger tests pass 34 of 34. The inherited `tests/test_pipeline_audit.py`
suite currently fails four of 34 tests:

1. a failed forced render can reuse a stale final PNG;
2. a failed page can let a real run exit zero;
3. provider-error text can overwrite verified markdown;
4. a truncation retry can ignore the second process exit code.

These failures are reproducible on commit `5976d5d`. They predate the page-ledger files
and need a separate code fix through opencode.

## Remaining work, with no completion claim

1. finish the GGD OCR, search it and Davenport under their correct identities, and acquire
   verified Palaniammal and Sundarapandian sources;
2. rebuild the ETE extraction so all 97 ids are present before source matching;
3. enumerate the 17-page 2025-26 assignment bundle exactly;
4. create one row per question instance across the full 383-plus corpus;
5. attach a source locator, URL, or explicit unresolved status to every question row;
6. deduplicate by content family only after every instance has an evidence-backed family id;
7. fix and retest the four pipeline failure-semantics defects.

External book and web text remains a reference layer only. Nothing from those sources is
to be copied into `md/` or the course question bank.
