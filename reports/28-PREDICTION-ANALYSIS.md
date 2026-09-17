# Prediction analysis: what can actually be predicted, 17 Sep 2026

Question asked: use prediction algorithms (linear, exponential, log, quadratic, polynomial) on
the papers, learn the source mix per exam, and build a question bank that hits 80-100 percent
of the next MTE.

I will not do curve-fitting that looks clever and predicts nothing. Here is what the data
supports and what it does not.

## 1. The hard constraint first (honest)

```
  MTE sittings held:   2   (2024-25, 2025-26)
  MTE questions:      16   (8 per paper)
```

A linear model needs 2 points (fits, predicts nothing). A quadratic needs 3. A polynomial of
degree d needs d+1. With 2 MTE papers, ANY polynomial, exponential, or log fit is
interpolation, not prediction. Fitting a quadratic through 2 points is exact and useless.

So: NO regression on the MTE series is honest. Anyone who fits a curve here is lying about
what the curve knows.

## 2. What DOES have enough data: the generator, not the series

The MTE is not a time series. It is a DRAW from a generator. The generator is visible across
ALL nine sittings (2 MTE + 5 ETE + 2 re-sess), 78 in-syllabus questions. That is where the
statistics live.

```
  distinct (topic x ask) skeletons observed:  29
  in-syllabus paper questions:                78
```

## 3. The strongest test I can actually run: hold out one year

Train the topic pool on everything EXCEPT the 2025 MTE, then ask: would the pool have covered
the held-out 2025 paper.

```
  train pool topics: RV/pdf 29, Poisson 31, Normal 20, Exponential 19, Binomial 14,
                     Chebyshev 13, Estimation 13, Uniform 7, CLT/SE 4
  held-out MTE 2025: 8 questions

  coverage: 8 of 8 topics were in the pool = 100 percent
```

That is a real backtest, not a curve. Result: the topic pool is stable enough that a paper
drawn from it lands entirely inside a pool learned from other sittings.

## 4. The prediction that works is a PROBABILITY DISTRIBUTION, not a number

What we can state, with the data behind it:

```
  TOPIC           P(appears in an MTE)   evidence
  Chebyshev       1.00                   in EVERY sitting held (9/9 rows have it)
  one Normal q    1.00                   every paper has exactly one normal item
  one Poisson q   ~0.9                   MTE24, MTE25, most ETE
  one Binomial q  ~0.8
  one Exponential q ~0.8                 MTE24 (B2), MTE25 (Q6)
  Estimation      ~0.7
  Uniform         ~0.3
  CLT/SE          ~0.3
```

So the honest "prediction" is a ranked topic distribution plus the 9-slot ask matrix, NOT a
forecast of specific questions.

## 5. Source mix: is it stable enough to forecast?

```
  paper     source mix (traced blocks)
  MTE24     G&K 6, concept 1, open 1                 -> G&K-DOMINATED
  MTE25     G&K 2, MCQ-bank 2, H&T 1, deck 1,
            Walpole 1, concept 1                     -> MIXED
```

The mixes are NOT the same. 2024 is almost all G&K; 2025 spread across three books and the
MCQ banks. With two samples, "the source mix is stable" is NOT supported. I will not claim it.

What IS supported, from the cross-paper map (report 27):
- G&K is the single largest source overall (9 of 44 traced rows corpus-wide).
- the course decks feed the paper directly (M25-Q7 is a CLT-deck example verbatim).
- the assignments feed the paper directly (3 of 16 MTE blocks are assignment items).

## 6. What a bank that "gets 80-100 percent" actually requires

The 80-100 percent is achievable, but by COVERAGE, not by forecasting specific questions. The
mechanism that works:

```
  1. enumerate the skeleton pool  (done: 29 skeletons, report 27 + 00-MTE-TOPIC-UNIVERSE)
  2. for each skeleton, generate every mutation the setters use
     (M0 reskin, M1 invert, M3 re-target, M4 compose; report 07-PATTERNS)
  3. source-match each generated item to G&K / Walpole / H&T / the decks,
     so the bank mirrors the real provenance
  4. a bank that covers all 29 skeletons x the 9 ask slots x the common mutations
     contains the next paper WITH HIGH PROBABILITY, because the paper is a draw
     from that same pool
```

Coverage argument, stated honestly: if the paper is drawn from a pool of 29 skeletons and the
bank covers all of them plus their mutations, then the probability of a miss equals the
probability the setter invents a NEW skeleton. Across 9 sittings we have seen 0 new skeletons,
only reskins of the same ones. That is the real basis for a high hit rate. It is a coverage
claim, not a forecast.

## 7. Verdict on each thing you asked for

```
  linear prediction on MTE       NOT HONEST (2 points)
  exponential / log / quadratic  NOT HONEST (2 points)
  polynomial                     NOT HONEST (2 points)
  hold-out topic coverage test   HONEST, run it, 8/8 = 100 percent
  source-mix stability forecast  NOT SUPPORTED (2 samples, mixes differ)
  skeleton-pool coverage bank    HONEST and the right path -> 80-100 percent by coverage
```

## 8. Next concrete step

Build the skeleton-coverage bank: one entry per (skeleton x slot) with its real source
reference and 2-3 mutations. That is the artifact that can actually cover the next paper.
