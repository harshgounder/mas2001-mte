# MAS2001 visual companion

This folder is separate from the existing deck documents and notes. It replaces selected ASCII sketches
with exact, scalable diagrams while leaving the audited study text unchanged.

## First visual set

| visual | primary source files |
|---|---|
| `assets/course-map.svg` | `deck/00-INDEX.md`, `deck/notes/00-NOTES-INDEX.md` |
| `assets/probability-tree.svg` | `deck/03-LINGUISTICS.md`, `deck/notes/01-probability-foundations.md` |
| `assets/dice-sum.svg` | `deck/notes/01-probability-foundations.md`, `deck/notes/02-random-variables.md` |
| `assets/pmf-to-cdf.svg` | `deck/notes/03-pmf-and-cdf.md` |
| `assets/distribution-gallery.svg` | `deck/05-DISTRIBUTIONS.md`, notes 06 and 07 |
| `assets/normal-table-conventions.svg` | `deck/06-NUMBERS.md`, `deck/notes/07-uniform-normal-exponential.md` |
| `assets/sampling-clt.svg` | `deck/notes/08-sampling-and-clt.md` |
| `assets/estimator-comparison.svg` | `deck/notes/09-estimation.md` |
| `assets/chebyshev-bound.svg` | `deck/notes/10-chebyshev-and-hidden.md` |
| `assets/study-roadmap.svg` | `deck/14-MASTER-STUDY-ORDER.md` |

## Rules

- SVG is the source format because formulas, labels, axes, and geometry must stay exact.
- A visual never upgrades a provenance claim or changes a numerical answer.
- Repeated ASCII formula boxes become styled callouts in later page layouts, not separate art.
- Every visual must name the Markdown sources it represents.
- Run `python3 deck/visuals-gpt56/build_visuals.py` to rebuild the assets deterministically.
- Run `python3 deck/visuals-gpt56/build_inventory.py` to rebuild the full fenced-block ledger.

## Coverage status

The first set covers the central diagrams shared across the deck. The remaining file-level
inventory belongs in `manifest.csv`; `planned` means the ASCII source has been inspected but
its replacement has not yet been drawn.

`source-notes/fenced-block-inventory.csv` accounts for every fenced block in all 27 original
Markdown files. Its broad structural-marker test intentionally over-selects styled callouts so
a later visual pass cannot silently lose a candidate.
