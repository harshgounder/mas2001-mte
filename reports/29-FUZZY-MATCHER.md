# Fuzzy matcher: results and its honest ceiling, 17 Sep 2026

Built `scripts/fuzzy_provenance.py` to beat the exact sweep's false negatives on the scanned
G&K text. It works for ONE job and fails at another, and the difference matters.

## What it does well

OCR normalisation plus a distinctive-token rule. Its one proven win:

```
  ete-E24S3-B1  the Chebyshev inverse with bound 21/25
    report 16 says the source is G&K.
    exact sweep: "open" (the scan garbled the phrase).
    fuzzy matcher + manual read of the raw G&K text:
      "Now taking k=2.5, we get P(-2 < X < 8) ~ 21/25"
    -> report 16 CONFIRMED.
```

So for a DISTINCTIVE token (a fraction unique to one book), the matcher is right.

## What it does NOT do: attribute a source from numbers alone

The matcher's second signal (a distinctive number landing in a book) produces COINCIDENCES in a
3.5M-char text. Validation found these false positives:

```
  asn2025-1-MCQ-04  matched G&K on "11/2"
      the book has it inside an unrelated worked answer: "Ans. (ii) 5/26, (iii) 11/26"
  ete-E25S4-A9      matched on "3413"
      the book has it as a table value: "- 2'x'0:3413"
  ete-R25S4-B1      matched on "3749"
      the book has it as a table row: "...3708 .3729 .3749 .3770..."
```

A fraction like 11/2 coincides with 11/26; a 4-digit run coincides with a table entry. Number
matching is NOT reliable evidence on its own.

## Why I stopped tuning

Four iterations tightened the rule. Each fix removed some false positives and also removed a
real match, because the two signals (numbers, word grams) are entangled: generic method phrasing
("maximum likelihood estimator obtain") appears in every stats book, so gram overlap cannot
carry a source claim, and numbers cannot either. There is no threshold that is both precise and
complete on this data. Chasing one more decimal of threshold would be overfitting to the
examples I happened to check, which is worse than an honest conservative matcher.

## Final state: a conservative candidate generator

```
  verdict counts (non-frozen, 337 rows):
     59  unsearched (no text)
    175  open
     20  fuzzy-family
      5  fuzzy-strong
      1  fuzzy-verbatim
  frozen 46 (16 MTE + 30 decks, hand-verified, untouched)
```

The one surviving "verbatim" is itself a number coincidence, which proves the point: at these
thresholds the matcher is precise but nearly silent. That is the honest result.

## The correct fix (not built, stated plainly)

Reliable source attribution needs PHRASE matching on the OCR, not token matching. Concretely:
normalise both texts to a noise-tolerant alphabet, then run a sliding-window similarity (e.g.
SequenceMatcher or token-set ratio) at sentence granularity, and require a contiguous match of
15-plus normalised characters. That is a different algorithm from what is here, and it is the
right next step if exact attribution is wanted.

## Value delivered anyway

```
  1. one previously-open provenance line CLOSED with proof: E24S3-B1 -> G&K (21/25).
  2. the negative result is itself useful: it proves NUMBER matching is invalid for
     provenance, so nobody repeats this mistake.
  3. scripts/fuzzy_provenance.py --verify prints matched tokens + context, so any
     future candidate is one human glance from accept or reject.
```

Artifacts:
  scripts/fuzzy_provenance.py
  reports/evidence/fuzzy-match-20260917.json
