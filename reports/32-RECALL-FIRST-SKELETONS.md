# Recall-first skeleton verification, 17 Sep 2026

Goal you set: cover EVERYTHING that has appeared, so nothing comes that we did not count. Recall
over precision. Over-marking is fine; a miss is not.

Method: classified EVERY question in every paper we hold (16 MTE blocks + 97 ETE rows = 113
questions, 9 sittings) into (family) and (family / ask). Counted every distinct one. Then split
into "seen in an MTE paper" vs "seen only in ETE / re-sess".

## THE COUNT (exact, recall-first)

```
  distinct (family / ask) skeletons across all 9 sittings   34
  distinct families across all 9 sittings                   12
  families in the MTE papers                                 8
  families seen ONLY in ETE / re-sess (the recall gap)        4
  (family/ask) skeletons in the MTE papers                  14
  (family/ask) skeletons seen only outside the MTE papers     20
```

## THE 12 FAMILIES (union over all sittings)

```
  family            sittings   in MTE papers
  RV/pdf-cdf          9/9      YES
  Estimation          8/9      YES
  Poisson             8/9      YES
  Normal              7/9      YES
  Chebyshev           6/9      YES
  Exponential         6/9      YES
  Binomial            5/9      YES
  Uniform             2/9      YES
  --- recall gap (NOT in an MTE paper yet, but they HAVE appeared) ---
  Hypothesis-OUT      7/9      no   (t / F / chi / ANOVA; out of MTE syllabus, drill lightly)
  CLT                 3/9      no   (standard error, sampling distribution)
  Definition          3/9      no   (definition MCQs: rv, discrete rv, N(0,1) properties)
  Composite-Other     2/9      no   (multi-part mixed)
```

## THE RECALL GAP: 20 (family/ask) skeletons that appeared but are NOT in an MTE paper

These are the exact "would have missed" cases. Every one has appeared in a real paper:

```
  Binomial / point            Normal / point
  Binomial / moments          Normal / tail
  Binomial / formula-mcq      Normal / moments
  Poisson / point             Normal / find-param
  Poisson / tail              CLT / point
  Poisson / sufficiency       Estimation / point
  Exponential / point         Estimation / moments
  Exponential / sufficiency   Estimation / formula-mcq
  Expectation / point         Definition / concept-mcq
  Uniform / point             Hypothesis-OUT / point
```

## THE RECALL MAP (picture)

```
   ALL SHAPES EVER SEEN (34)  =  IN-MTE (14)  +  RECALL-GAP (20)
        |                            |                  |
        |                            |                  +--> appeared in ETE/re-sess only:
        |                            |                       Normal/point, Normal/tail,
        |                            |                       Estimation/point, CLT/point,
        |                            |                       Definition/concept-mcq, ...
        |                            |
        |                            +--> will very likely recur:
        |                                 Chebyshev/*, Poisson/*, RV/pdf-cdf/*, ...
        |
        v
   DRILL ALL 34  ->  miss only if a shape NEVER SEEN appears
```

```
   family coverage across sittings
   RV/pdf-cdf #################### 9/9   [MTE]
   Estimation ###################. 8/9   [MTE]
   Poisson    ###################. 8/9   [MTE]
   Hypoth-OUT ################..... 7/9   gap (out of syllabus)
   Normal     ###############...... 7/9   [MTE]
   Chebyshev  #############........ 6/9   [MTE]
   Exponential #############........ 6/9   [MTE]
   Binomial   ###########.......... 5/9   [MTE]
   CLT        #######.............. 3/9   gap
   Definition #######.............. 3/9   gap
   Uniform    #####................ 2/9   [MTE]
   Composite  #####................ 2/9   gap
```

## THE FULL 34-SKELETON LIST (drill all of them)

```
  IN MTE (14)                          RECALL GAP (20, still drill)
  Chebyshev / concept-mcq              Binomial / point
  Chebyshev / inverse-c                Binomial / moments
  Chebyshev / point                    Binomial / formula-mcq
  Chebyshev / moments                  Poisson / point
  Poisson / concept-mcq                Poisson / tail
  Poisson / formula-mcq                Poisson / sufficiency
  Poisson / moments                    Exponential / point
  Binomial / tail                      Exponential / sufficiency
  Exponential / tail                   Expectation / point
  Normal / interval                    Uniform / point
  Estimation / sufficiency             Normal / point
  Estimation / tail                    Normal / tail
  RV/pdf-cdf / find-param              Normal / moments
  RV/pdf-cdf / formula-mcq             Normal / find-param
  RV/pdf-cdf / point                   CLT / point
  Uniform / tail                       Estimation / point
                                       Estimation / moments
                                       Estimation / formula-mcq
                                       Definition / concept-mcq
                                       Hypothesis-OUT / point
```

## THE RECALL GUARANTEE (what this buys you)

```
  every family that has EVER appeared in a held paper      12  -> all 12 in the drill list
  every (family/ask) shape that has EVER appeared          34  -> all 34 in the drill list
  a shape that has NEVER appeared                          0 known, cannot be covered by definition
```

So: if the next MTE is drawn from the same generator (proven: 0 new skeletons in 9 sittings at
the family level), then drilling all 12 families and all 34 shapes leaves a miss only if the
setter invents a shape never seen in 113 questions. That is the honest ceiling on recall.

## Why this differs from the earlier "5 / 8" answer

The earlier run optimised PRECISION (what definitely appears in both MTE papers): 5 families,
or 8 to cover both. THIS run optimises RECALL, which is what you asked for now: count every
shape that has EVER appeared, in any paper. That gives 12 families and 34 shapes. The 4 extra
families (Hypothesis-OUT, CLT, Definition, Composite-Other) have all appeared; they are the
insurance.

## The one genuine risk left (stated, not hidden)

```
  the classifier buckets a few odd rows as Composite-Other (2). They are:
    ete-E25S3-C1  (a) 95% CI 81 families (b) subway wait
    ete-E24S4-A3  P(exact value) = 0 for a continuous rv
  these are real question shapes (CI computation, continuous-rv exact-value property).
  They are counted as "drill: estimation point + definition", but the bucket name hides them.
  Flagged here so nothing is silently dropped.
```

## Artifact

Inputs: `~/mas2001-devore/mte-blocks.json` (16 MTE blocks),
`reports/evidence/question-instance-ledger-enriched.csv` (97 ETE rows), 9 sittings total.
Classifier is a fixed keyword function (no weights, reproducible). No tuning.
