# Deck 01: notes-lecture-series-01-09 (Dr. Vivek Singh, lectures 1-9)

Source: `md/notes-lecture-series-01-09/` 147 pages, assembled at `md/notes-lecture-series-01-09.md`.
This file: one entry per question, in slide order. Solution slides that only restate a
previous question are noted in the annex, not re-entered.

Provenance note that matters for the MTE: this deck is Devore-derived for units 1 and 2
(textbook cover on p011, slide phrasing matches Devore 8e chapters 1-4), with MUJ framing
slides at front. The MTE paper is set from this course's material, so these examples are the
closest thing to a question bank for lectures 2-9.

## Annex: census of pages with questions or examples (drives the work order)

```
  page   what                                                        ID
  005-007  admin text, course outcomes (no questions)                -
  012-013  statistics intro, one illustrative "Ram has 100 Rs"       (illustration)
  017      limitations, customer survey example (discussion)         (illustration)
  020-022  applications lists, three discussion questions            (discussion)
  023      random experiment, 4 experiment examples (identify-only)  (illustration)
  024      sample space, 4 examples (toss one/two coins, two dice)   (illustration)
  025      mutual exclusivity, 2 examples + counterexample          (illustration)
  026      mutual exclusivity rule statement                        -
  027      independence, 2 examples                                (illustration)
  028      independence formal definition                          -
  041-042  basketball tournament, Q with parts a-d, solution p042    D1-Q001
  043-045  formulas: P(n,r), C(n,r), axioms, rules (no questions)    -
  046-047  faculty computers Q2 with solution p047                   D1-Q002
  048-049  basketball lineup Q3 with solution p049                   D1-Q003
  050      conditional probability, camera example (worked)          D1-Q004
  052-054  rv definition, coin/dice examples                         D1-Q005
  055-056  sum-of-two-dice pmf + two-coin pmf complete               D1-Q005 cont.
  057-059  geometric rv derivation                                  D1-Q006
  060-061  car lifetime, discrete rv remark                          (illustration)
  062-063  continuous rv definition                                  -
  065      gas station pumps, parts a-c                            D1-Q007
  066      pmf with k, parts i-iv                                  D1-Q008
  067-069  tune-up cylinders, parts a-c with plots                    D1-Q009
  070-071  building permit forms, parts a-d                          D1-Q010
  072-073  flashlight batteries, parts a-d                           D1-Q011
  074-075  cdf definition                                            -
  078      density-cdf relation remark                              -
  080-081  computer boards inspection, parts a-c                    D1-Q012
  082-083  dice maximum M, parts a-b                                 D1-Q013
  084      cdf step plot (illustration)                             -
  085      cdf nondecreasing proof                                 D1-Q014
  089      single fair die expectation (example)                     D1-Q015
  093-094  E(aX+b) proof + X table with E(2X+1)^2                    D1-Q016
  095-099  variance definition slides                                -
  100-106  variance properties, shortcut formula, rules              (statements)
  107-108  freezer models, parts a-d with solution p108              D1-Q017
  109-111  magazine order, parts with solution p110-111              D1-Q018
  112-123  continuous rv framing, pdf definition, remarks            -
  124-126  pdf example 2x, P(X<=1/2), conditional example            D1-Q019
  127-129  bus transfer waiting time, parts a-f with solution p128-129 D1-Q020
  130-135  cdf definition and propositions                          -
  136-137  f from F proposition                                     -
  138      CDF exercise, two densities (i)(ii)                      D1-Q021
  139      F(x) = (x-1)^4/16, find pdf + P(2<=x<=3)                  D1-Q022
  140-147  continuous expectation, Pareto exercise (a-e, solution)   D1-Q023
  (plus p142 hospital kidney, p146 Pareto; split during entry)
```

## Entries

### D1-Q001: basketball tournament, four universities (slides p041, solution p042)

```
  id            D1-Q001
  source        deck 01, p041 (ask), p042 (solution), lectures 2-3 block, sample space and events
  provenance    Devore-derived exercise (ch 2, counting sample spaces); MUJ deck reuse
  question      Four universities 1-4, tournament: R1 games 1v2 and 3v4, winners meet for the
                championship, losers also play. Outcome "1324" means 1 beats 2, 3 beats 4, then
                1 beats 3 and 2 beats 4. (a) list all outcomes in S; (b) list A = 1 wins the
                tournament; (c) list B = 2 gets into the championship game; (d) list A u B,
                A n B, and A'.
  what it is    Build a sample space from structural constraints, then do set operations on events.
  type          Probability foundations
  subtype       Sample space construction + event algebra (union/intersection/complement)
  knowledge     definition of sample space and event; union, intersection, complement notation;
                the tournament structure (who plays whom is fixed by earlier results)
  approach      Encode each outcome as a 4-character string (R1 winners, then championship and
                consolation results); enumerate by constraint, not by brute listing.
  steps         (a) R1 has 4 results (1 or 2 wins; 3 or 4 wins), championship has 2 results,
                consolation 2 results, but consistent strings: 16 total. Slide lists 16.
                (b) A = outcomes where the first character is 1: 1324, 1342, 1423, 1432 (4).
                (c) B = outcomes where 2 appears first or second: 8 outcomes.
                (d) A u B = 12 outcomes; A n B = empty, since 1 and 2 cannot both reach the
                final (one eliminates the other in R1); A' = the 12 outcomes where 1 does not win.
  alternate     Tree enumeration (R1 -> final -> consolation) produces the same 16. For (b),
                symmetry says P(1 wins) = 1/4 without listing, but the question asks for the list.
  intent        Force model-based enumeration instead of blind counting, then exercise the
                algebra of events, especially the disjointness in (d).
  bloom         Understand (a-c), Analyze (d: connect structure to the empty intersection)
  dok           2 (skill and concept, multi-step within a defined system)
  math_group    A for (a)-(c) as routine procedure; B for (d) as structure transfer; tag B
  solo          multistructural for the lists, relational for (d)
  gaise         n/a (pure probability)
  difficulty    2 of 5 (low conceptual load, high care needed when listing)
  traps         listing fewer than 16 by missing "loser plays too" outcomes; assuming 1 and 2
                can meet in the final (A n B nonempty); miscounting B as "2 wins tournament"
  exam_use      in scope, lectures 2-3; a listing question of exactly this shape can appear
  verified      regenerated all 16 strings on the machine from the structural constraints;
                every set (S, A, B, A u B, A n B, A') matches the slide exactly
```

### D1-Q002: laptop and desktop setups (slides p046, solution p047)

```
  id            D1-Q002
  source        deck 01, p046 (ask), p047 (solution), lecture 2 block, equally likely outcomes
  provenance    Devore-derived exercise; six faculty computers, two laptops, four desktops
  question      Two of six setups done per day, chosen at random from six (15 equally likely
                outcomes). (a) P(both laptops); (b) P(both desktops); (c) P(at least one
                desktop); (d) P(at least one of each type).
  what it is    Counting equally likely outcomes with combinations, then complement and union.
  type          Probability foundations
  subtype       Equally likely outcomes via C(n,r); complementary events; mutually exclusive
                events combined with the complement
  knowledge     C(n,r); equally likely model; complement rule P(A') = 1 - P(A); mutually
                exclusive events have P(A n B) = 0 and then P(A u B) = P(A) + P(B)
  approach      Count favourable selections with combinations over a fixed denominator of
                C(6,2) = 15; where the direct count is awkward, go through the complement.
  steps         (a) C(2,2)/15 = 1/15.
                (b) C(4,2)/15 = 6/15 = 2/5.
                (c) A = both laptops; C = at least one desktop; C' = A, so P(C) = 1 - 1/15
                = 14/15.
                (d) at least one of each = 1 - P(A u B) = 1 - 1/15 - 2/5 = 8/15, valid because
                A n B = empty (both-laptops and both-desktops cannot coexist).
  alternate     Direct count for (d): C(2,1) C(4,1)/15 = 8/15, same number, fewer subtleties.
                Worth doing both to see why the complement route needs the disjointness check.
  intent        Two ideas: the complement turns "at least" phrasing into easy subtraction, and
                a union of mutually exclusive events adds probabilities without correction.
  bloom         Apply
  dok           2
  math_group    A (routine procedure with a decision: direct count versus complement)
  solo          multistructural
  gaise         n/a
  difficulty    2 of 5
  traps         computing at least one desktop as P(one desktop) + something, double counting;
                using 2/5 + 1/15 without checking A n B = empty; forgetting the total is fixed
                at 15 by the problem statement
  exam_use      in scope, lecture 2; classic one-mark-per-part shape, very likely style
  verified      C(6,2) = 15, C(2,2)=1, C(4,2)=6, C(2,1)C(4,1)=8; all four parts recomputed on
                the machine and matched to the slide (1/15, 2/5, 14/15, 8/15)
```

(resume marker: next entry D1-Q003, lineup question, slides p048-p049)
