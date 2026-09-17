# F14 FOUNDATIONS: probability basics, events, independence (lectures 2-3)

Source: our own material (the lecture-series-01-09 deck by Dr. Vivek Singh, assignment-1's
MCQ sections). These are the FIRST lectures of the MTE scope and were the one block with no
worked file until now. Nothing invented. Numbers machine-checked.

```
  WHY THIS FILE EXISTS: the MTE scope (from ~/PS/syllabus.txt, confirmed against the
  repo's own 00-SCOPE-AND-EXAM-FACTS.md) runs lectures 1 to 21, and lectures 2 to 11
  live ONLY in the 147-page Dr. Vivek Singh deck. The lecture-2 basics (events,
  conditional probability, independence, the probability rules) are examinable and had
  no worked questions. This file closes that gap.

  SHAPES IN THIS FILE
  F14.1  the vocabulary (outcome, event, sample space, set operations)
  F14.2  the three probability rules (addition, multiplication, complement)
  F14.3  conditional probability (with the deck's own worked example)
  F14.4  independence (the definition + the test)
  F14.5  the assignment-1 MCQs 1 to 10 (solved with explanations)
  F14.6  the remaining definition MCQs from the papers that map here
```

═══════════════════════════════════════════════════════════════════════════════
F14.1  THE VOCABULARY (get these exact; MCQs trade on the differences)
═══════════════════════════════════════════════════════════════════════════════

```
   +--------------------+-----------------------------------------------------------+
   | outcome            | a possible result of the random phenomenon                |
   | experiment         | any process leading to an uncertain outcome               |
   | sample space (S)   | the set of ALL possible outcomes                          |
   | event              | any collection (subset) of outcomes from S                |
   | complement (A')    | all outcomes in S NOT in A                                |
   | union (A or B)     | outcomes in A, or B, or BOTH (at least one)               |
   | intersection (A&B) | outcomes in BOTH A and B                                  |
   | mutually exclusive | no two events share any outcome (A&B = empty set)         |
   +--------------------+-----------------------------------------------------------+
```

THE PICTURE (the two set operations on a die roll):
```
   S = {1,2,3,4,5,6}
   A = "even" = {2,4,6}          B = "greater than 4" = {5,6}

   UNION A u B    = {2,4,5,6}     (everything in either)
   INTERSECTION   = {6}           (only the overlap)
   COMPLEMENT A'  = {1,3,5}       (everything NOT even)
   A and B mutually exclusive?    NO (they share 6)
```

TRAP: "mutually exclusive" vs "independent" are DIFFERENT things and MCQs love the swap.
Mutually exclusive: they cannot both happen (P(A&B) = 0). Independent: one happening does
not change the other's probability (P(A&B) = P(A)P(B)). Two events with nonzero probability
CANNOT be both.

═══════════════════════════════════════════════════════════════════════════════
F14.2  THE THREE PROBABILITY RULES
═══════════════════════════════════════════════════════════════════════════════

```
   +---------------------------------------------------------------------------------+
   | THE THREE AXIOMS (Kolmogorov; the deck states them verbatim):                    |
   |   P(S) = 1                                                                       |
   |   P(A) >= 0 for every event A                                                    |
   |   disjoint A1, A2, ...: P(A1 u A2 u ...) = P(A1) + P(A2) + ...                   |
   +---------------------------------------------------------------------------------+
   | THE WORKING RULES:                                                               |
   |   complement:      P(A') = 1 - P(A)                                              |
   |   addition rule:   P(A u B) = P(A) + P(B) - P(A n B)                             |
   |   if mutually exclusive:  P(A u B) = P(A) + P(B)   (the -PnB term is 0)          |
   |   multiplication:  P(A n B) = P(A) x P(B|A) = P(B) x P(A|B)                      |
   |   if independent:  P(A n B) = P(A) x P(B)                                        |
   +---------------------------------------------------------------------------------+
```

THE VENN PICTURE (why the addition rule subtracts):
```
      +------- A -------+-------+------- B -------+
      |                 |XXXXXXX|                 |
      |    P(A) only    |overlap|    P(B) only    |
      |                 |XXXXXXX|                 |
      +-----------------+-------+-----------------+
   P(A) + P(B) counts the overlap TWICE, so subtract it once.
```

═══════════════════════════════════════════════════════════════════════════════
F14.3  CONDITIONAL PROBABILITY (the deck's own worked example)
═══════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTION 1 (our deck, lecture-series 01-09 - the digital camera example)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
   Of all individuals buying a digital camera:
        60% include an optional memory card  -> P(A) = 0.60
        40% include an extra battery          -> P(B) = 0.40
        30% include BOTH                      -> P(A n B) = 0.30
   Given that a buyer purchased an extra battery, find P(card was also purchased).
   Also find P(battery | card).
```

EVERY STEP:

```
  STEP 1  the definition: P(A|B) = P(A n B) / P(B)
  STEP 2  P(card | battery) = 0.30/0.40 = 0.75
          meaning: of all battery buyers, 75% also bought a card.
  STEP 3  P(battery | card) = 0.30/0.60 = 0.50
          meaning: of all card buyers, half also bought a battery.
  STEP 4  the two conditionals are DIFFERENT (0.75 vs 0.50) even though the numerator is
          the same 0.30. The denominator is what changes.
```

THE PICTURE (conditioning shrinks the world):
```
   full world:      |---- A (0.60) ----|-- B (0.40) --|
   given B:   the world SHRINKS to B; inside B, the A-part is 0.30/0.40 = 75%
   given A:   the world SHRINKS to A; inside A, the B-part is 0.30/0.60 = 50%
```

TRAP: the difference between P(A|B) and P(B|A) (the "inverse fallacy"). Here 0.75 vs 0.50.
MCQs test this swap directly.

═══════════════════════════════════════════════════════════════════════════════
F14.4  INDEPENDENCE (the definition and the test)
═══════════════════════════════════════════════════════════════════════════════

```
   DEFINITION: A and B are INDEPENDENT if P(A|B) = P(A)   (and dependent otherwise)
   EQUIVALENT TEST: A and B are independent if and only if
                        P(A n B) = P(A) x P(B)
```

THE TEST IN ACTION (on the camera numbers):
```
   P(A) x P(B) = 0.60 x 0.40 = 0.24
   but P(A n B) = 0.30
   0.24 != 0.30  ->  A and B are DEPENDENT (not independent).
   (makes sense: battery buyers are more likely to also buy a card.)
```

FOR MORE THAN TWO EVENTS (the deck's definition, verbatim logic):
```
   A1,...,An are MUTUALLY independent if for EVERY subset,
        P(intersection of the subset) = product of the individual probabilities.
   (pairwise independence alone is NOT enough for mutual independence.)
```

TRAP: the deck's own numbers are DEPENDENT. If an MCQ says "assume independence" then and
only then may you multiply. Never multiply P(A)P(B) unless the question grants independence.

═══════════════════════════════════════════════════════════════════════════════
F14.5  THE ASSIGNMENT-1 MCQs 1 to 10  (all from our own sheet)
═══════════════════════════════════════════════════════════════════════════════

```
   +----+------------------------------------------------------+--------+----------------+
   | #  | question                                             | answer | why            |
   +----+------------------------------------------------------+--------+----------------+
   | 1  | Which is a discrete random variable?                 | (C)    | count of       |
   |    | A) height  B) time  C) number of defective bulbs     | defects| defective      |
   |    | D) temperature                                       |        | bulbs is a     |
   |    |                                                      |        | COUNT (whole   |
   |    |                                                      |        | numbers); the  |
   |    |                                                      |        | rest are       |
   |    |                                                      |        | continuous     |
   +----+------------------------------------------------------+--------+----------------+
   | 2  | The CDF of a random variable is:                     | (B)    | F(x) = P(X<=x) |
   |    | A) P(X=x)  B) P(X<=x)  C) P(X>=x)  D) P(X>x)         | P(X<=x)| by definition  |
   +----+------------------------------------------------------+--------+----------------+
   | 3  | Which is true about a PMF?                           | (B)    | total prob = 1 |
   |    | A) can be negative B) sums to 1 over all values      | sum to | (PMFs never    |
   |    | C) decreasing D) only for continuous                 | 1      | negative for   |
   |    |                                                      |        | valid rv)      |
   +----+------------------------------------------------------+--------+----------------+
   | 4  | The expectation of a random variable represents its: | (A)    | expectation    |
   |    | A) average value  B) max  C) min  D) most likely     | average| = weighted     |
   |    |                                                      |        | mean value     |
   +----+------------------------------------------------------+--------+----------------+
   | 5  | Which gives an upper bound on P(|X - mean| big)?     | (D)    | that is        |
   |    | A) Bayes  B) binomial  C) CLT  D) Chebyshev          | Cheby- | EXACTLY        |
   |    |                                                      | shev   | Chebyshev's    |
   |    |                                                      |        | job            |
   +----+------------------------------------------------------+--------+----------------+
   | 6  | The conditional probability P(A|B) is defined as:    | (B)    | P(A n B)/P(B)  |
   |    | A) P(B)/P(A)  B) P(A n B)/P(B)                       |        | the definition |
   |    | C) P(A)+P(B)  D) P(A n B)/P(A)                       |        |                |
   +----+------------------------------------------------------+--------+----------------+
   | 7  | A box has 4 red and 6 blue balls; one is selected.   | (B)    | 4 red of 10    |
   |    | P(red)?   A) 0.2  B) 0.4  C) 0.6  D) 0.8             | 0.4    | total = 4/10   |
   +----+------------------------------------------------------+--------+----------------+
   | 8  | If P(A|B) = 1, then:                                 | (B)    | conditional    |
   |    | A) A impossible when B occurs  B) A always occurs    | A      | prob of 1 =    |
   |    | whenever B occurs  C) mutually exclusive  D) none    | always | certainty      |
   |    |                                                      | occurs | given B        |
   +----+------------------------------------------------------+--------+----------------+
   | 9  | A card is drawn from 52. P(an Ace)?                  | (A)    | 4 aces of 52   |
   |    | A) 1/13  B) 1/4  C) 4/13  D) 1/52                    | 1/13   | = 4/52 = 1/13  |
   +----+------------------------------------------------------+--------+----------------+
   | 10 | Chebyshev's inequality is applicable to:             | (B)    | it needs ONLY  |
   |    | A) only normal  B) any distribution with finite      | any    | mean and       |
   |    | mean and variance  C) only discrete  D) only cont.   | with   | variance, no   |
   |    |                                                      | finite | shape needed   |
   +----+------------------------------------------------------+--------+----------------+
```

TRAPS hiding in this set:
```
   Q1: height/time/temperature are continuous (any value in a range); only a COUNT is
       discrete. Watch for "number of ..." phrasings.
   Q8: P(A|B)=1 does NOT mean A and B are the same event or mutually exclusive. It means:
       inside the B-world, A is certain.
   Q10: Chebyshev is distribution-FREE. "Only normal" is the classic wrong answer (that
        would be the empirical rule, which IS normal-only).
```

═══════════════════════════════════════════════════════════════════════════════
F14.6  (the two OUT-of-scope definition MCQs moved to their families: the one-sided test MCQ
to F12, the CI definition MCQ to F8; see those files)
═══════════════════════════════════════════════════════════════════════════════

═══════════════════════════════════════════════════════════════════════════════
F14 SUMMARY CARD
═══════════════════════════════════════════════════════════════════════════════

```
   THE VOCABULARY TRAPS:
     mutually exclusive = cannot both happen (P(A n B) = 0)
     independent         = one does not change the other (P(A n B) = P(A)P(B))
     (nonzero-probability events cannot be both)

   THE RULES:
     complement   P(A') = 1 - P(A)
     addition     P(A u B) = P(A) + P(B) - P(A n B)
     multiplication P(A n B) = P(A) x P(B|A)
     independence test: P(A n B) ?= P(A) x P(B)

   THE ASSIGNMENT-1 MCQ KEY (10 answers): C, B, B, A, D, B, B, B, A, B

   THE CLASSIC SWAPS THE EXAM LIKES:
     P(A|B) vs P(B|A)          (0.75 vs 0.50 in the camera example)
     mutually exclusive vs independent
     Chebyshev (any distribution) vs empirical rule (normal only)
     discrete (counts) vs continuous (measurements)
```
