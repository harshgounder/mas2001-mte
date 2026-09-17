# Fuzzy matcher: what it does and what it found, 17 Sep 2026

Built `scripts/fuzzy_provenance.py` to fix the exact sweep's false negatives. The G&K text on
disk is a noisy scan ("Fo.r example", "o.f", "a~d~t"), so exact 5-gram phrases fail even when
the problem IS present.

## What the matcher does

```
  1. OCR normalisation: Fo.r -> for, o.f -> of, letter-dot-letter removed, watermark
     tags (MSV...) stripped, split hyphens rejoined.
  2. LaTeX-aware numbers: \frac{21}{25} unfolded to 21/25, so a fraction in the question
     matches the digits in the OCR book.
  3. DISTINCTIVE-only evidence: a word or number counts only if it appears in exactly ONE
     of the four reference corpora. So "probability" and the t-table constant 2.262 do not
     count; a fraction like 21/25 (unique to G&K) does.
  4. Verdict from two signals: distinctive-number matches + distinctive-word ratio.
```

## The fix it provided (the headline)

```
  ETE in-syllabus traced, exact sweep:    1
  ETE in-syllabus traced, fuzzy matcher: 24 candidate (15 verbatim + 9 strong)
```

The key case: `ete-E24S3-B1`, the Chebyshev inverse with the bound 21/25. report 16 says it
comes from G&K. The exact sweep said "open". The fuzzy matcher confirms `21/25` is present in
G&K (unique to that corpus), so the report-16 claim is CONFIRMED where the exact matcher
failed.

## Honest limits (found during validation, not hidden)

1. NUMBER-ONLY MATCHING IS NOT ENOUGH. A first version counted any number hit, and a validation
   pass showed false positives: a blood-sample question matched H&T on t-table constants (2.262,
   3.841), which appear in every stats book. Fixed by requiring distinctive-only numbers.

2. THE t-TABLE CONSTANTS STILL LEAK. Even after the distinctive filter, constants like 2.262
   and 3.841 survive when they appear in only one OCR corpus (the other scan garbled them). So
   several ETE "fuzzy-verbatim" rows are driven by a t-table constant, which is weak evidence.
   These should be treated as CANDIDATES, verified by hand, not as settled fact.

3. SEVERAL FLAGGED ROWS ARE OUT OF SCOPE. The strongest "fuzzy-verbatim" ETE rows
   (E24S3-B5, E24S4-C1, E24S4-D1) are hypothesis-testing items, which are not MTE syllabus, so
   their provenance is moot for exam prep.

## State of the artifact

```
  scripts/fuzzy_provenance.py                       the matcher
  reports/evidence/fuzzy-match-20260917.json        the run record
  reports/evidence/fuzzy-verbatim verdicts          47 corpus-wide (excl. frozen)
```

The matcher is a CANDIDATE GENERATOR. Its job is to point at where a question likely came from
so a human confirms. It is NOT a settlement; the number-only leaks prove it.

## What it means for the trace numbers

```
  MTE 15/16            unchanged, hand-verified, trust it
  ETE in-syllabus      1 -> 24 candidates, of which the strong ones need a look
  the true ETE figure  now bounded: >=1, plausibly ~15 to 24, pending verification of the
                       distinctive-number hits
```

## Next step

Add a `--verify` mode that, for each candidate, prints the exact matched token and its context
in the book, so a human can accept or reject each in one pass. That converts candidates into
settled verdicts without guessing.
