# U01 second-reader record, 16 September 2026

Independent read pass over the U01 source check in PR 1, plus the operational probes taken
with it. Commands and verbatim model output are quoted; nothing here edits converted pages.
Renders regenerate with `pdftoppm -png -r 300` (or 600) on the sources under `~/PS`.

## A. Line-level reads against the rendered sources

1. `paper-mte-2024-25-scheme` p004, mean value. Fresh read of the 300 dpi render:
   `MEAN=2.6`. The pre-PR transcription printed 3.6 in three places; the fix to 2.6 is
   correct.

2. `paper-mte-2025-26-scheme` p004, question label: read `Q-8 (ii)`; the pre-PR line
   `Q8 (11)` was a misread. Fix correct.

3. `paper-mte-2025-26-scheme` p004, the `i.e.` line. Read log across two models, two
   resolutions and two prompt styles:
   - the digit 0: the original codex source check (against the PDF), the 300 dpi check
     recorded in PR 1, and two independent anti-correction reads at 300 dpi in this pass
     (`i.e. E(t^2) != 0`, shape described as a plain round zero with nothing attached).
   - theta squared: one 600 dpi read in this pass.
   - excluded as invalid: an early 150 dpi read with a permissive prompt (permissive
     prompts silently repair this source; the same protocol error started the dispute),
     one garbled crop read, and two band crops that sliced the line horizontally.
   Verdict on this record: the source prints `E(t^2) != 0`; the PR 1 change to `!= 0` and
   errata 21 stand. Confidence is high on the weight of independent reads but not absolute;
   if a human opens page 4 and reads theta squared, reopen errata 21.
   Correction to this repository's review trail: an earlier internal note in the same
   session called the codex item a false positive on the strength of the excluded
   permissive read. That note is retracted here.

4. `paper-mte-2024-25-scheme` p003, inequality: the line prints `<=` (read:
   `= 1 - P[-2/sqrt3 <= X <= 2/sqrt3]`), so the codex claim of a strict `<` in the source
   does not survive and the PR's decision to leave that line unchanged is correct.

## B. New errata verified from disk

- Errata 19 (2024-25 QA2). Paper options as transcribed: a) 2x - x^2/2 - 1/2,
  b) 2x - x^2/2, c) x - x^2/2 + 1, d) 2x - x^2/2 - 1. Direct integration for
  1 <= x <= 2 gives F(x) = 2x - x^2/2 - 1, which is option d and passes F(1) = 1/2 and
  F(2) = 1. Option b equals 3/2 at x = 1. Confirmed.
- Errata 20 (2025-26 Q4). The scheme prints infinite bounds on the normalisation and
  moment lines while the density is supported on 0 < x < 4 and the evaluation uses 0 to 4.
  Recomputed independently: 15/1024, 16/7, 40/7, 24/49 are all consistent with the finite
  bounds. Confirmed.

## C. Claim spot checks for PR 3

- `md/ppt4-continuous-prob-dist/p044.md` is a references page; the exponential range
  p038 to p043 is right.
- 2024-25 paper marks as transcribed: [2] [2] [2] / [4] x 4 / [4+4] = 30. The
  3x2, 4x4, 8-mark format claim holds.

## D. Operational probes, 16 September

- `~/.local/bin/vision` bare call: provider=cc model=gpt-5.6-luna, answered OK.
- Ollama chat lane: HTTP 401 on a minimal POST (re-probed 16 September). Conversion runs
  must pass `--model gpt-5.6-luna` until that lane returns.
- `~/PS` arrivals recount: `find ~/PS -maxdepth 1 -newermt '2026-09-15 00:00' -type f`
  gives 23 (25 when counted from 14 September 00:00). The "24" in an earlier revision of
  the checklist is not reproducible.

## E. Residual uncertainties (flagged, not blocking)

- Top-right corner text on `paper-mte-2025-26-scheme` p004: reads differ ("6 (c)" in this
  pass, "Page 4" in PR 1). Cosmetic, no exam impact.
- The red mark at the end of the `i.e.` line: "circled 1" in PR 1, "circled 0" in one read
  here. Mark counts change no answer.
- Single-symbol reads can flip across scale and prompt style. Treat the mathematics in
  errata 21, not the glyph dispute, as the study-relevant product.
