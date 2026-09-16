# 09 QUESTIONS: the tagged MTE question inventory

## THE QUESTION INVENTORY AS A GRID

```
                    the two MTE papers (16 blocks)
   ┌──────┬──────────────────────────────────────────────┐
   │ M24  │ A1 A2 A3 B1 B2 B3 B4 C1(OPEN)                │
   │ M25  │ Q1 Q2 Q3 Q4 Q5 Q6 Q7 Q8                      │
   └──────┴──────────────────────────────────────────────┘
      10 source/family leads   5 concept checks   1 open composite

                    assignments (A1 + A2 = 52 blocks)
   ┌──────┬──────────────────────────────────────────────┐
   │ A1   │ 10 MCQ  6 short  4 long  4 application       │
   │ A2   │ 12 A  8 B  4 C  4 D                          │
   └──────┴──────────────────────────────────────────────┘

                    the teaching decks (60 blocks)
   ┌──────────┬───────────────────────────────────────────┐
   │ notes    │ 30 blocks (D1-1 .. D1-30)                  │
   │ ppt3     │ 6   ppt4  │ 7   clt  │ 5   ppt5  │ 5       │
   │ lms-th   │ 7 (2 unique)                               │
   └──────────┴───────────────────────────────────────────┘

                    re-teach decks (30 blocks, pass 2)
   ┌──────────┬───────────────────────────────────────────┐
   │ L1-7     │ 13    L8-9  │ 4    L12-13 │ 6   L14-15 │ 7 │
   └──────────┴───────────────────────────────────────────┘
```

## THE SLOT COVERAGE MAP (what is asked vs what is one mutation away)

```
                  SLOT:  1  2  3  4  5  6  7  8  9
                         pt tl iv mo pa in ct cd co
   ┌─────────────┬──────────────────────────────────┐
   │ BINOMIAL    │  X  X  S  X  X  S  X  S  S       │
   │ POISSON     │  X  X  .  X  X  .  X  .  X       │
   │ UNIFORM     │  X  X  X  X  S  S  .  .  S       │
   │ NORMAL      │  X  X  X  X  X  X  X  .  X       │
   │ EXPONENTIAL │  X  X  X  X  X  .  .  X  X       │
   └─────────────┴──────────────────────────────────┘
     X = asked in our corpus
     S = a sibling, one mutation away, NOT yet asked  <- risk
     . = no evidence

   the S cells are where the next paper can surprise you.
   the four highest-risk siblings: normal one-unknown,
   binomial interval, CLT-for-a-sum, discrete conditional.
```

## PROVENANCE TRUTH, VISUALISED

```
   enumeration state

   base ledger                383  ███████████████████████████████
   assignment bundle PR 14    119  ██████████
                              ---
   combined                   502

   MTE evidence state, 16 blocks

   source or family lead       10  ██████████
   generic concept check        5  █████
   open composite               1  █
```

The 502 count measures enumerated question instances, not unique questions and not sourced
questions. No content-family ids have been assigned yet, so corpus-wide deduplication and
source attribution remain open work.

Every MTE-scope question block we hold, tagged by distribution, slot (the nine in 07-PATTERNS),
and where it lives. This is the drill list. "In scope" means lectures 1-21.

The nine slots: 1 point, 2 tail, 3 interval, 4 moments, 5 parameter, 6 inverse, 7 count,
8 conditional, 9 compose.

## A. The two MTE papers (16 blocks, evidence states kept separate)

```
  id        source page      question                                  dist      slot  status
  M24-A1    mte 2024 p001    Poisson transform concept                  Poi        4    generic concept
  M24-A2    mte 2024 p001    triangular density, mean, variance        contin    4+5  traced G&K 8-1-5
  M24-A3    mte 2024 p001    Chebyshev forms, pick the false ones      Cheb       -    concept
  M24-B1    mte 2024 p001    Var(X-2Y), lambda 2, mu 3, answer 14      Poisson   4    VERBATIM G&K
  M24-B2    mte 2024 p001    f(x)=Ae^-x/5 telephone                    Exp       4    reskin G&K ch5 ex10
  M24-B3    mte 2024 p001    Chebyshev interval (-1,1) vs (-1,3)       Cheb      2    reskin G&K ex15b
  M24-B4    mte 2024 p001    uniform wait, answer 1/3                  Unif      3    G&K subway
  M24-C1    mte 2024 p002    rain N(2.6,34.5) + 5/3 binomial week      Normal+Bin 9   OPEN (composite)
  M25-Q1    mte 2025 p001    axiom of total mass                       prob       -    concept
  M25-Q2    mte 2025 p001    substitution drill                        prob       -    concept
  M25-Q3    mte 2025 p001    sufficient statistics MCQ                 Est        -    concept cross-check
  M25-Q4    mte 2025 p001    density kx^3(4-x)^2, find k, mean, var    contin     4+5  ABES sample (asks SD)
  M25-Q5    mte 2025 p001    Chebyshev find c, mu 10, var 4, bound .04  Cheb     6    deck L10-11 Q2(iv)
  M25-Q6    mte 2025 p001    exponential reskin, mean 5 -> 3           Exp        4    G&K ch5 ex10 reskin
  M25-Q7    mte 2025 p001    machine life sample mean, n=9             Normal     3    Walpole P&S 8.25
  M25-Q8    mte 2025 p002    (i) Poisson notes (ii) estimation chapter  Poi+Est    9    mixed
```

## B. Assignment 1 (24 blocks) and Assignment 2 (28 blocks)

```
  id         question                                     dist      slot
  A1 MCQ1    3 children, coin, pmf and cdf                discrete   1+3
  A1 MCQ5    Chebyshev applicability                      Cheb       2
  A1 MCQ10   Chebyshev applicability                      Cheb       2
  A1 short1  pmf 1/8 3/8 3/8 1/8 + cdf                    discrete   3
  A1 short2  mortality pdf P(X>12) = 0.0916               contin     2
  A1 short3  f(x)=6x(1-x), valid pdf, b=1/2               contin     5+1
  A1 short4  geometric expectation, E=2                   geom(gap)  4
  A1 short5  dice Chebyshev 35/54 vs 1/3                  Cheb       9
  A1 short6  600 throws, 19/24                            Bin+Cheb   9
  A1 long1   mortality integral + conditional 0.4863       contin     3+8
  A1 long2   pmf with unknown k, k=1/10, P(X<6)=0.81      discrete   5+3
  A1 long3   lot of 25, 5 defective, mean 0.8 both ways   Hyper(no slide!) 7
  A1 long4   four bad oranges 12/19, 32/95, 3/95          discrete   3
  A1 app1    sensor batch, E=1.2, Var=0.86                discrete   4
  A1 app2    CDF 0.15,0.50,0.80,1.00                       discrete   4
  A1 app3    battery E=3.45, Var=0.9475, sd=0.97          discrete   4
  A1 app4    marks Chebyshev, 75 percent                  Cheb       9
  A2 A2      binomial moments                              Bin        4
  A2 A3      Poisson                                      Poi        1
  A2 A4      uniform E, Var                              Unif       4
  A2 A7      Poisson                                      Poi        see source
  A2 A9      binomial max successes                      Bin        4
  A2 A10     uniform parameters                          Unif       5
  A2 A11     normal 68/95/99.7 landmarks                 Normal(no slide!) 4
  A2 A12     Poisson additivity                          Poi(no slide!) 9
  A2 B1      Poisson rejected P(X>=4)=0.2424             Poi        2
  A2 B2      uniform                                      Unif       see source
  A2 B3      normal interval 45-62                       Normal     3
  A2 B4      5000 batteries N x P                        Normal     7
  A2 B5      exponential conditional 0.6225              Exp(no slide! 8)   8
  A2 B8      uniform |X| intervals                       Unif       3
  A2 C1      exponential memoryless                      Exp(no slide!) 8
  A2 C2      two-unknown normal 37.2/28.2/30.4           Normal     5+6
  A2 C3      Poisson P(X>2)=0.8753                       Poi        2
  A2 C4      uniform rounding                            Unif       1
  A2 D1      10000 bulbs N x P                           Normal     7
  A2 D2      exponential unit conversion                 Exp        5
  A2 D3      binomial moments                            Bin        4
  A2 MCQ5    exponential memoryless                      Exp        8
  A2 MCQ11   normal landmarks                            Normal     4
```

## C. The teaching decks' own questions (60 blocks, the practice pool)

```
  notes deck (30 blocks, p041 to p147)       see 10-SLIDE-MAP.md for the page-by-page list
  ppt3 (6 blocks)  5-coin, pens x3, irregular die x2
  ppt4 (7 blocks)  uniform, normal chain, inverse, exponential
  clt (5 blocks)   lightbulbs, ATM, impurity, LED, machine
  ppt5 (5 blocks)  response time, packets, battery CI, comparison set 1, set 2
  lms-theory (7 total, 2 unique)  sufficiency examples
```

## D. The re-teach deck questions (30 blocks, use as pass 2)

```
  L1-7  13 blocks: L17-01..L17-13 (faculty computers, basketball, camera, rare disease,
        gas pumps, cylinder pmf [OPEN], county forms, batteries, boards, dice max, cdf proof,
        E on -3/6/9)
  L8-9   4 blocks: L89-01..L89-04 (bus pdf, CDF-to-density [OPEN], kidney E(Y), Pareto)
  L12-13 6 blocks: L1213-01..06 (5-coin [OPEN], pens, irregular die, Poisson x3 [one OPEN])
  L14-15 7 blocks: L1415-01..07 (uniform, normal with mean 8 and sd 5, inverse cutoff, exponential
        McClave)
```

## E. The open items (no source found yet)

```
  M24-C1   rain set + 5/3 binomial composite        in scope, no source
  L17-06   pmf table with k and CDF questions        four-deck, open
  L17-13   pmf on -3/6/9, transformed expectation    four-deck, open
  L89-02   CDF to density                            four-deck, open
  L1213-01 exactly 3 heads in 5 tosses               four-deck, open
  L1213-03 irregular die even outcomes               four-deck, open
  L1213-04 Poisson relation P1 = 0.2 P2              four-deck, open
  L1213-05 Poisson calls exactly two each minute     four-deck, open
  L1213-06 life-insurance Poisson approximation      four-deck, open
  (the pens question circulates in several versions, but its originating source is OPEN)
```

## F. Provenance state (honest, as of 16 Sep)

```
  Enumeration: 383 rows on this branch, plus 119 assignment-bundle rows on PR 14.
  Combined after merge: 502 gross instances.

  MTE evidence: 10 source or family leads, 5 generic concept checks, 1 open composite.
  A concept check confirms mathematical type, not copying or source provenance.

  Corpus-wide source matching is incomplete. No row carries a content family id yet, so
  neither the unique-question count nor a corpus-wide sourced percentage is known.
```
