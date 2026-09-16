# Wave B: concept MCQ source hunt, 16 Sep 2026

Goal: find the exact home of the five MTE concept-check MCQs on public MCQ banks
(sanfoundry, examveda, mcqmate style). Ran over the rival multi-engine search rail
(web_search tool returns empty; parallel.ai returns 402 insufficient credit).

## Result

```
  MCQ                          verdict
  mte-M25-Q2  Poisson mean e   FOUND verbatim, CONFIRMED
      URL   examveda.com/in-a-poisson-distribution-if-mean-m-e-then-px-is-given-by-268365/
      proof fetched the page directly (curl). its schema.org QAPage block carries
      name: "In a Poisson Distribution, if mean (m) = e, then P(x) is given by"
      and the full four-option set a) e^(x-m)/x!  b) e^(m-x)/x!  c) x!/e^(m-x)
      d) x!/e^(x-m). word for word match to our M25-Q2.
      also on a Scribd "Poisson Distribution MCQs" set.
  mte-M25-Q3  sufficiency MCQ  not found (first pass)
  mte-M24-A1  Poisson Y=2X     not found. the literal wording returned only generic
                               Poisson theory pages (Wikipedia, GeeksforGeeks).
  mte-M24-A3  Chebyshev forms the literal wording ("is useful for / exact
                               probabilities / bounding") returned ZERO results.
                               the false-statement phrasing needs the MCQ bank
                               itself, not a general search.
  mte-M25-Q1  density integral not attempted this pass (needs the option text).
```

## Honest state

One of five located. The other four need either:
  - a direct fetch of the sanfoundry / examveda / mcqmate Chebyshev and estimation
    category pages and a phrase match, rather than a general search (next step);
  - or acceptance that they are generic textbook concept checks with no single home
    (the M24-A1 and M24-A3 rows are already labelled CONCEPT, which is a truthful
    verdict even without a source page).

## Rails note for the next pass

```
  web_search (hermes)        empty
  parallel-search MCP        402 insufficient credit (rotate key)
  rivalsearch MCP            WORKING (Bing + Yahoo), returns raw text
```

Wave B is not blocked, just unfinished. A focused fetch of the three MCQ-bank
category pages is the clean next move.
