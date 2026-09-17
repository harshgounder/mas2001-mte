# Cross-paper repetition map, 17 Sep 2026

Question asked: was anything from a previous year repeated, did anything from the re-session or
ETE papers repeat, and what other patterns run across the papers.

Method: every skeleton probed by regex across all nine exam sittings plus our decks and
assignments. Boilerplate (headers, MUJstella watermarks, course code) stripped first, so the
hits below are real question content, not shared page furniture.

## The corpus set

```
  papers    MTE24, MTE25, ETE24S3, ETE25S3, ETE24S4, ETE25S4, ETE25SUM, RESS25S3, RESS25S4
  decks     chebyshev, ppt3 (discrete), ppt4 (continuous), clt, ppt5 (estimation)
  assignments  2024-25 #1 to #5, and the 2025-26 bundle
```

## 1. What repeats across years and instruments

```
  skeleton                     MTE24 MTE25 E24S3 E25S3 E24S4 E25S4 ESUM R25S3 R25S4  DECK  ASGN
  ────────────────────────────────────────────────────────────────────────────────────────────
  telephone exponential          X     X                        X                       ppt3 24-4,bundle
  Chebyshev mu=10 var=4                X           X                                    -    bundle
  electric cable 6x(1-x)                                                          X     -    24-1,bundle
  pens defective 1/10                          X                                       ppt3  bundle
  Poisson ratio recovery         X                                                       ppt3  24-2
  car hire firm                                                                  X     -      24-2,bundle
  radio tube life                                                                      -    24-1,bundle
  dice 600 throws                                                                      -    24-1,bundle
  normal 31% / 45                                                                  X    -      24-2
  machine 7 years                      X                                               clt    -
  insurance 5000 men                                                                   ppt3  bundle
  n keys door                                                                          -    24-1
  520 pages typos                                                                      -    24-2
```

Read the columns: the MTE papers and the ETE papers draw from the SAME skeleton pool. A
skeleton that appears in the 2024 MTE often returns in the 2025 MTE (telephone), or in an ETE
(Chebyshev mu10). Nothing in the pool is invented; it all rotates.

## 2. Yes, previous years repeat

```
  telephone exponential   MTE24 (mean 1/4) then MTE25 (mean 3)      SAME skeleton, constant changed
  Chebyshev mu10 var4     MTE25 Q5 then ETE25S3 B1                 SAME numbers, target changed
  electric cable 6x(1-x)  asgn24-1 then bundle2526 then RESS25S4    same density, 3 years running
  Poisson ratio recovery  MTE24 B1 then asgn24-2                   same P(X=2)=9P(X=4)+90P(X=6) family
  radio tube life         asgn24-1 then bundle2526                 same tube, both years
  car hire firm           asgn24-2 then RESS25S3, bundle2526        same firm
  dice 600 throws         asgn24-1 then bundle2526                 same 600 throws
  normal 31/45            asgn24-2 then ETE24S4                    same percentiles
```

## 3. Yes, the re-session papers repeat

```
  RESS25S4  carries the electric cable 6x(1-x)  (same family as the 2024-25 assignment #1)
  RESS25S3  carries the car hire firm           (same as assignment 2024-25 #2)
```
The re-session (re-sess) papers are re-sits; they reuse the in-syllabus skeletons rather than
writing new ones. This matches the ETE papers.

## 4. Yes, the ETE papers repeat the MTE and assignment material

```
  ETE25S3 B1  Chebyshev mu=10 var=4   also MTE25 Q5 and the 2025-26 bundle Q5
  ETE24S4 B5  the pmf-table plus CDF question, same shape as ETE25S4 B1
  ETE25SUM    the telephone exponential, same as MTE24/MTE25
  ETE papers that repeat: at least 3 of 5 in-syllabus ETE carry a skeleton from MTE or assignment
```

## 5. The chain pattern (the single most useful finding)

Several skeletons travel BOOK -> ASSIGNMENT -> PAPER, changing one constant each hop:

```
  telephone exponential
     G&K ch5 "lady speaks on the telephone" f(x)=Ae^(-x/5)
        -> assignment 2024-25 #2 Q20 (mean 6)
        -> MTE 2024 B2 (parameter 1/4)
        -> MTE 2025 Q6 (mean 3)
        -> ETE summer (same story)

  electric cable 6x(1-x)
     G&K "diameter of an electric cable" (Ex 5.3)
        -> assignment 2024-25 #1 Q3
        -> assignment 2025-26 bundle Q3
        -> ETE re-sess S4 C1

  Chebyshev mean 10 variance 4
     G&K -> our L10-11 deck Q2 -> MTE 2025 Q5 -> ETE S3 2025-26 B1
```

## 6. Other patterns across the papers

```
  P1  the FIVE distributions are fixed: binomial, Poisson, normal, exponential, uniform.
      no paper introduces a sixth.

  P2  Chebyshev is in every sitting (9 uses across 78 in-syllabus rows).

  P3  estimation questions are always one of the four properties:
      unbiasedness, efficiency, consistency, sufficiency.

  P4  the normal-inverse question is the hard slot: every paper has exactly one
      (find x for a tail, or solve mean and sd from two percentiles).

  P5  the E(X), E(X^2), E((2X+1)^2) triple (values -3, 6, 9) recurs in the deck, the
      2025-26 bundle and the summer paper.

  P6  the Poisson parameter-recovery form (P(X=2)=9P(X=4)+90P(X=6)) recurs in MTE24 and
      assignment 2024-25 #2, and the simpler P(X=1)=2P(X=2) in the deck.
```

## 7. Honest limits

- the probes are hand-written regexes for known skeletons; a skeleton I did not name is not
  probed. This finds what I looked for, not everything.
- the 5-gram whole-paper overlap test originally flagged ETE25S4 / ETE25SUM / RESS25S4 as a
  cluster at 13-18 percent, but 90 percent of that was shared boilerplate (headers, the
  MUJstella watermark line). After stripping boilerplate the true content overlap is small and
  specific, which is what section 1 lists.
- the paper conversions carry `[domain omitted by repository policy]` where the watermark
  domain was removed, by design.
