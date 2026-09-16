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
| total blocks | 378 exact | corrected gross count is 383, then 502 once the 119 bundle rows are added | report 18 corrected |
| duplicate treatment | known duplicates not double counted | the arithmetic included five row-5/row-6 overlaps | gross and net counts separated |
| text-layer sufficiency | vision not required to count questions | text-marker counting missed image-based blocks | page images remain required for completeness checks |
| assignment bundle scope | the 17-page 2025-26 bundle PDF covered only assignments 3 to 5, about 65 items | a direct text-layer enumeration finds all five assignments and 119 items (19+36+25+21+18), one row per occurrence | report 18 corrected; reports/evidence/assignment-bundle-ledger-20260916.csv added |

## Evidence layers now present

- `reports/evidence/corpus-page-ledger.csv`: exactly 646 declared source pages, with source
  hash, conversion state, text hash, markdown state, image state, and marker hints.
- `reports/evidence/deck-block-ledger-20260916.csv`: 30 manually verified blocks across
  L1-7, L8-9, L12-13, and L14-15, including the five blocks missed in PR 10.
- `reports/evidence/external-source-inventory-20260916.csv`: hash-locked external reference
  assets, verified identities, text state, and explicit absent rows for Palaniammal and
  Sundarapandian.
- `reports/evidence/question-instance-ledger.csv`: 502 gross question instances. Each row
  has a stable id, corpus group, source label, order, description state, scope, provenance
  state, source field, locator, family-id slot, and gross status. The 210 rows whose
  descriptions have not yet been extracted are marked pending with blank summaries.
- `reports/evidence/assignment-bundle-ledger-20260916.csv`: the exact 119-item ledger for
  the 17-page 2025-26 assignment bundle (assignments 1 to 5), with item id, section, label,
  order, page span, statement, extraction state, structural candidate, match status,
  2024-locator slot, evidence locator, and scope. The item-level split is 63 in-scope and
  56 out-of-scope. Seventeen layout-split statements carry reviewed summaries.
- Report 17: 97 ETE blocks with scope verdicts. This is an intake ledger, not a completed
  provenance ledger.

## Test-harness defect found while checking the new ledger

The new page-ledger tests pass 34 of 34. An initial run of
`tests/test_pipeline_audit.py` appeared to expose four production failures, but that result
was false: the test hardcoded `/home/liebert511/mas2001-mte` and silently imported code
from a different worktree. The four production fixes already exist on `master`.

PR 13 changes the harness to resolve its own repository and makes the gitignored page PNG
root explicit through `MTE_PAGE_ROOT`. With the existing artifact directory supplied, all
34 pipeline tests pass while importing production modules from the tested worktree. A
clean worktree without the artifact directory now fails only the image-presence check,
honestly, instead of borrowing files from another checkout.

## Remaining work, with no completion claim

1. acquire verified Palaniammal and Sundarapandian sources; GGD and Davenport OCR are
   complete, and their first signature sweep did not identify an exact open MTE source;
2. rebuild the ETE extraction so all 97 ids are present before source matching;
3. (done 16 Sep) the 17-page 2025-26 assignment bundle is enumerated exactly: 119 items
   across assignments 1 to 5, see reports/evidence/assignment-bundle-ledger-20260916.csv;
   enumeration is complete, but source matching is not. Assignments 3 to 5 have overlap
   spot checks, assignments 1 and 2 have no year-over-year comparison, and every row remains
   not_assessed with a blank 2024 locator;
4. replace the 210 pending descriptions in the 502-row instance ledger;
5. attach a source locator, URL, or explicit unresolved status to every question row;
6. deduplicate by content family only after every instance has an evidence-backed family id;
7. merge the worktree-safe test-harness correction in PR 13.

External book and web text remains a reference layer only. Nothing from those sources is
to be copied into `md/` or the course question bank.
