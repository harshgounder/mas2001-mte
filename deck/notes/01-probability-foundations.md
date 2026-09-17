# 01 PROBABILITY FOUNDATIONS (lecture 2, notes p012-p050)

## 1. What statistics is (p012-p016) - not examined, but the framing

```
  statistics = the science of COLLECTION, PRESENTATION, ANALYSIS, INTERPRETATION
               of numerical data
```

```
   ┌───────────────────────────────────────────────────┐
   │  "All statistics are numerical statements,        │
   │   but not all numerical statements are            │
   │   statistics."                                    │
   └───────────────────────────────────────────────────┘
        Ram has 100 Rs in his pocket   ->  NOT statistics (one fact, no data set)
        avg age of 5th class is 10 yrs ->  IS statistics (a derived numerical statement)
```

Four limitations the slides list (worth a one-line recall, low exam weight):
1. not suited to qualitative phenomena
2. does not study individuals
3. statistical laws are not exact
4. liable to be misused (the customer-satisfaction survey only of loyal customers)

## 2. Probability, the intuition (p018-p019)

```
  P near 1  = event extremely likely
  P = 0.5   = a coin-flip situation
  P near 0  = rare event
  0 <= P(E) <= 1     ALWAYS
```

```
      0 ─────────── 0.5 ─────────── 1
    impossible      even          certain
      │              │              │
      rare        coin flip      common
```

## 3. Random experiment (p023)

```
  DEFINITION
  an experiment whose outcome cannot be predicted with certainty in advance,
  although ALL possible outcomes are known

  ┌────────────────┬──────────────────────────┐
  │ EXPERIMENT     │ POSSIBLE OUTCOMES        │
  ├────────────────┼──────────────────────────┤
  │ toss a coin    │ H, T                     │
  │ roll a die     │ 1,2,3,4,5,6              │
  │ draw a card    │ any one of 52            │
  │ pick a student │ any student in the class │
  └────────────────┴──────────────────────────┘

  note: we KNOW all outcomes, we do not know WHICH ONE occurs
```

## 4. Sample space S (p024)

```
  S = set of ALL possible outcomes

  one coin      S = {H, T}                       2 outcomes
  one die       S = {1,2,3,4,5,6}                6 outcomes
  two coins     S = {HH, HT, TH, TT}             4 outcomes
  two dice      S = {(1,1),(1,2),...,(6,6)}      6 x 6 = 36 outcomes
```

```
  ╔════════════════════════════════════════════════════════════╗
  ║  THE COUNTING RULE THAT SAVES MARKS                        ║
  ║  two dice are counted as 36 ORDERED pairs, not 21 unordered║
  ║  (1,2) and (2,1) are DIFFERENT outcomes                     ║
  ║  every dice probability (1/36, 2/36, 3/36...) assumes 36   ║
  ╚════════════════════════════════════════════════════════════╝
```

The 36 ordered-pair positions, with each cell displaying its sum:

```
        1    2    3    4    5    6      <- die 2
   ┌────┬────┬────┬────┬────┬────┐
 1 │ 2  │ 3  │ 4  │ 5  │ 6  │ 7  │
   ├────┼────┼────┼────┼────┼────┤
 2 │ 3  │ 4  │ 5  │ 6  │ 7  │ 8  │
   ├────┼────┼────┼────┼────┼────┤
 3 │ 4  │ 5  │ 6  │ 7  │ 8  │ 9  │    cell position = (row die, column die)
   ├────┼────┼────┼────┼────┼────┤    printed value = the sum; each cell = 1/36
 4 │ 5  │ 6  │ 7  │ 8  │ 9  │ 10 │
   ├────┼────┼────┼────┼────┼────┤
 5 │ 6  │ 7  │ 8  │ 9  │ 10 │ 11 │
   ├────┼────┼────┼────┼────┼────┤
 6 │ 7  │ 8  │ 9  │ 10 │ 11 │ 12 │
   └────┴────┴────┴────┴────┴────┘
        ^
      die 1

  count the 7s: 6 of them -> P(sum=7) = 6/36 = 1/6  (the most likely sum)
  count the 2s: 1 (top-left) -> 1/36
  count the 12s: 1 (bottom-right) -> 1/36
  the counts run 1,2,3,4,5,6,5,4,3,2,1 (sums 2..12) = the familiar triangle
```

## 5. Events and set algebra (p030-p040)

```
  outcome     a single possible result
  event       a SUBSET of S (a collection of outcomes)
  null event  the empty set, no outcomes
```

```
  ┌──────────────────────────────────────────────────────────┐
  │  A'   complement   "not A"     everything in S not in A  │
  │  A∪B  union        "A or B"    in A, or B, or BOTH       │
  │  A∩B  intersection "A and B"   in BOTH                   │
  │  disjoint / mutually exclusive : A∩B = ∅                 │
  └──────────────────────────────────────────────────────────┘
```

ASCII Venn diagrams:

```
     (a) two events            (b) A ∩ B               (c) A ∪ B
   ┌───────────────┐        ┌───────────────┐       ┌───────────────┐
   │   ┌───┐┌───┐  │        │   ┌───┐┌───┐  │       │   ┌───┐┌───┐  │
   │  ( A  )( B )  │        │  ( A ▓)(▓ B ) │       │  (▓A▓▓)(▓▓B▓) │
   │   └───┘└───┘  │        │   └───┘└───┘  │       │   └───┘└───┘  │
   └───────────────┘        └───────────────┘       └───────────────┘
      plain A, B              overlap shaded            both shaded

     (d) A'                    (e) mutually exclusive
   ┌───────────────┐        ┌───────────────┐
   │▓▓▓┌───┐▓▓▓▓▓▓▓│        │  ┌───┐ ┌───┐  │
   │▓▓( A  )▓▓▓▓▓▓▓│        │ ( A  ) ( B )  │   <- no overlap at all
   │▓▓▓└───┘▓▓▓▓▓▓▓│        │  └───┘ └───┘  │
   └───────────────┘        └───────────────┘
     everything but A
```

Demorgan, drawn as the two rules the slides state:

```
   (A ∪ B)' = A' ∩ B'          (A ∩ B)' = A' ∪ B'
   "neither" = not-A and not-B  "not both" = not-A or not-B
```

## 6. Mutually exclusive vs independent (p025-p028) - THE classic trap

```
   MUTUALLY EXCLUSIVE                INDEPENDENT
   ────────────────────              ────────────
   cannot happen together            one happening does not change
   A ∩ B = ∅                         the chance of the other
   P(A ∪ B) = P(A) + P(B)            P(A ∩ B) = P(A) x P(B)
                                     or  P(A|B) = P(A)
```

```
  ╔═══════════════════════════════════════════════════════════════╗
  ║  THEY ARE NOT THE SAME, AND THEY ARE NOT OPPOSITES            ║
  ║                                                               ║
  ║  exclusive  ->  CANNOT both happen  ->  knowing A KILLS B     ║
  ║                                        (so NOT independent,   ║
  ║                                         when P > 0)           ║
  ╚═══════════════════════════════════════════════════════════════╝
```

Worked: the die counter-example (p025)

```
   A = even = {2,4,6}      B = prime = {2,3,5}
   A ∩ B = {2}  -> they SHARE the outcome 2
   -> NOT mutually exclusive

   A = even = {2,4,6}      B = odd = {1,3,5}
   A ∩ B = ∅    -> mutually exclusive
```

Worked: coin + die independence (p027)

```
   A = head,  P(A) = 1/2
   B = 6,     P(B) = 1/6
   P(A ∩ B) = 1/2 x 1/6 = 1/12      -> independent
```

Worked: draw + replace (p027) -> independent.  draw, no replace -> dependent.

Mutual independence of n events (p028): for EVERY subset of size k (k = 2..n),

```
   P(Ai1 ∩ Ai2 ∩ ... ∩ Aik) = P(Ai1) P(Ai2) ... P(Aik)
```

## 7. Counting: the engine of half the course (p043)

```
        ORDER MATTERS ?          ORDER DOES NOT MATTER ?
        ────────────────         ────────────────────────
        PERMUTATION              COMBINATION
        P(n,r) = n!/(n-r)!       C(n,r) = n!/(r!(n-r)!)
        "arrangements"           "choose", "committee", "sets of"

        with REPEATED items:
        n! / (n1! n2! ... nk!)     n1, n2... are the repeat counts
```

```
  ┌─────────────────────────────────────────────────────────┐
  │ WORD TRIGGERS                                           │
  │   "arrange", "lineup", "order", "rank"  -> PERMUTATION  │
  │   "choose", "select", "committee", "set" -> COMBINATION  │
  └─────────────────────────────────────────────────────────┘
  and C(n,r) = C(n,n-r)   (choosing r to keep = choosing n-r to drop)
```

## 8. The axioms and rules (p044-p045)

```
  AXIOMS
    P(S) = 1
    P(A) >= 0
    disjoint A1,A2,... :  P(A1 ∪ A2 ∪ ...) = P(A1) + P(A2) + ...

  RULES
    addition       P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
    disjoint case  P(A ∪ B) = P(A) + P(B)
    multiplication P(A ∩ B) = P(A) P(B|A) = P(B) P(A|B)
    independent    P(A ∩ B) = P(A) P(B)
    complement     P(A') = 1 - P(A)
```

The addition-rule picture (why you subtract the overlap):

```
   ┌──────────────────────────────┐
   │   ┌───────┬───────┐          │
   │   │   A   │  A∩B  │    B     │   P(A)+P(B) counts A∩B TWICE
   │   │       │ counted│         │   subtract it ONCE
   │   │       │ twice │         │
   │   └───────┴───────┘          │
   └──────────────────────────────┘
```

## 9. Worked example 1: tournament (p041-p042)

Four universities 1,2,3,4. Round 1: 1v2, 3v4. Winners play for the title, losers play too.

```
   one outcome is written as a 4-letter code, e.g. 1324:
     1 beats 2, 3 beats 4 (round 1)   then  1 beats 3, 2 beats 4
```

```
   S = { 1324, 1342, 1423, 1432,
         2314, 2341, 2413, 2431,
         3124, 3142, 4123, 4132,
         3214, 3241, 4213, 4231 }                    -> 16 outcomes
```

```
  (b) A = 1 wins the tournament  -> 1 must be FIRST in the code
      A = {1324, 1342, 1423, 1432}                    4 outcomes

  (c) B = 2 gets into the final  -> 2 must be 1st or 2nd
      B = {2314, 2341, 2413, 2431, 3214, 3241, 4213, 4231}   8 outcomes

  (d) A ∪ B = 12 outcomes
      A ∩ B = ∅   because 1 and 2 CANNOT both reach the final
      A'    = S - A = 12 outcomes
```

## 10. Worked example 2: faculty laptops (p046-p047)

6 faculty, 2 chose laptop, 4 chose desktop. Only 2 setups per day, the 2 are chosen randomly.

```
  total outcomes  = C(6,2) = 15   (choose 2 of the 6 computers)

   (a) both laptops  = C(2,2)/15 = 1/15
   (b) both desktops = C(4,2)/15 = 6/15 = 2/5
   (c) at least one desktop : complement is "both laptops" = A
       P(C) = 1 - P(A) = 1 - 1/15 = 14/15
   (d) at least one of each type:
       1 - P(A ∪ B) = 1 - 1/15 - 2/5 = 1 - 1/15 - 6/15 = 8/15
       (A and B are disjoint, so no overlap to subtract)
```

## 11. Worked example 3: basketball lineup (p048-p049)

```
  STARTING LINEUP = 2 guards + 2 forwards + 1 center

  Part (a): 3 centers, 4 guards, 4 forwards, 1 swing player X
  ─────────────────────────────────────────────────────────
    no X         C(4,2) x C(4,2) x C(3,1) = 6 x 6 x 3 = 108
    X as guard   C(4,1) x C(4,2) x C(3,1) = 4 x 6 x 3 =  72
    X as forward C(4,2) x C(4,1) x C(3,1) = 6 x 4 x 3 =  72
                                              TOTAL = 252 lineups

  Part (b): 5 guards, 5 forwards, 3 centers, 2 swing (X and Y)
             choose 5 of the 15 at random; P(valid lineup)?
  ─────────────────────────────────────────────────────────
    neither X nor Y   C(5,2)C(5,2)C(3,1)          = 300
    X only            C(5,1)C(5,2)C(3,1) x2 cases = 300
    Y only            same                         = 300
    both X and Y      C(5,1)C(5,1)C(3,1) + 2C(5,2)C(3,1) = 135
                                          TOTAL = 1035

    P = 1035 / C(15,5) = 1035/3003
```

```
  ┌──────────────────────────────────────────────────────────────┐
  │ THE METHOD: split into disjoint cases by WHO of the swing     │
  │ players is used, count each case, ADD. Never double count.    │
  │  no X,no Y  +  X only  +  Y only  +  both X and Y = total     │
  └──────────────────────────────────────────────────────────────┘
```

## 12. Conditional probability (p050)

```
   P(A|B) = P(A ∩ B) / P(B),     P(B) > 0
```

Worked: digital camera buyers

```
   60% buy a memory card      P(A) = .60
   40% buy an extra battery   P(B) = .40
   30% buy both               P(A∩B) = .30

   P(card | battery) = .30/.40 = .75
   P(battery | card) = .30/.60 = .50
```

```
  ┌────────────────────────────────────────────────────────────┐
  │ NOTE THE TWO ANSWERS ARE DIFFERENT. .75 is NOT .50.         │
  │ The denominator is WHAT YOU ARE CONDITIONING ON.           │
  │ P(A|B) and P(B|A) are different numbers.                    │
  └────────────────────────────────────────────────────────────┘
```

The tree that makes it obvious:

```
                       all buyers
                      ┌────┴────┐
                   battery    no battery
                    (.40)       (.60)
                  ┌──┴──┐
              card  no card
              (.30)  (.10)
                    ^
              .30/.40 = .75  <- of the battery buyers, 75% also took a card
```

---
That is lecture 2 in full. The two things to carry forward: (1) the 36-cell dice grid,
(2) exclusive is not independent.
