# NOTES: the whole course, written out

These are real notes. Every slide is rewritten as something you can read and learn from
without opening a PDF. Worked examples keep their exact numbers. Diagrams are ASCII so they
render anywhere.

## The map

```
                    MAS2001 STATISTICS AND PROBABILITY
                    ===================================
                              │
        ┌─────────────────────┴─────────────────────┐
        │                                           │
   ┌────▼─────┐                              ┌──────▼──────┐
   │PART 1    │                              │PART 2       │
   │PROBABILITY│                             │INFERENCE    │
   │lect 2-9   │                             │lect 17-21   │
   └────┬─────┘                              └──────┬──────┘
        │                                           │
   ┌────▼──────────┐                          ┌─────▼───────┐
   │T2 foundations │                          │T13 sampling │
   │T3 rand vars   │                          │T14 CLT      │
   │T4 pmf/pdf/cdf │                          │T15 estim'n  │
   │T5 expectation │                          │T16 props    │
   │T6 variance    │                          └─────────────┘
   │T7 chebyshev   │
   └────┬──────────┘
        │
   ┌────▼──────────────────────────┐
   │T8 binomial  T9 poisson         │  DISCRETE
   │T10 uniform  T11 normal  T12 exp│  CONTINUOUS
   └───────────────────────────────┘
```

## File list

```
  file                          covers                             lecture
  00-NOTES-INDEX.md             this map                           -
  01-probability-foundations.md lecture 2, notes p012-p050          2
  02-random-variables.md        notes p051-p062                     3-4
  03-pmf-and-cdf.md             notes p063-p087                     5-6
  04-expectation-and-variance.md notes p088-p111                    7-9
  05-continuous-rv.md           notes p112-p147                     5-6 cont
  06-binomial-poisson.md        ppt3 (28 pages)                     12-13
  07-uniform-normal-exponential.md ppt4 (44 pages)                  14-16
  08-sampling-and-clt.md        lms-standard-error-clt (19 pages)   17-18
  09-estimation.md              ppt5 (26 pages) + lms-theory        19-21
  10-chebyshev-and-hidden.md    Chebyshev deck + H1-H8              10-11
```

## How the numbers in these notes were handled

The slides have the errata listed in `../08-TRAPS.md`. In these notes I write the CORRECT
value and mark the slide's wrong value inline with `[slide prints X]`. That way the note is
right and you still know what the slide said.

## The one picture to hold in your head for the whole course

```
  PROBLEM  ──▶ which of these four? ──▶ which slot? ──▶ method ──▶ answer
                     │
        ┌────────────┼────────────┬──────────────┐
        ▼            ▼            ▼              ▼
   named dist   named dist    sampling       estimator
   DISCRETE     CONTINUOUS    of a mean      comparison
        │            │            │              │
     binomial     uniform      CLT + SE      E, Var, pick
     poisson      normal                       the winner
                  exponential
        │
   ──▶ then the 9 slots (point, tail, interval, moments, params,
       inverse, count, conditional, compose) tell you WHICH formula
```
