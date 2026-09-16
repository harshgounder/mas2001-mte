# Count register, locked 14 September and extended through U01 on 16 September 2026

MTE scope only. Everything out of the MTE syllabus is excluded entirely (not counted, not
to be sorted). Exclusion list at the bottom, with proof that nothing from it leaked in.

Counting rule (fixed, applied everywhere):
- one item = one question / example / exercise / problem block; multi part counts once
- counted: labeled problems and examples that derive a result or pose a concrete ask
- not counted: display examples (definition or concept illustrations), rhetorical prompts,
  theorem displays with proofs, formula-only slides, non-math illustrations, section
  headers, figure captions

## Locked counts

| corpus | pages | items | unique | notes |
|---|---|---|---|---|
| 01 notes-lecture-series-01-09 | 147 | 30 | 30 | 4 have no solution slide: p065, p066, p138, p139 |
| 02 ppt3-discrete-prob-dist | 28 | 6 | 6 | |
| 03 ppt4-continuous-prob-dist | 44 | 7 | 7 | |
| 04 lms-standard-error-clt | 19 | 5 | 5 | |
| 05 ppt5-estimation-summary | 26 | 5 | 5 | counted here; all 5 also repeated in lms-theory |
| 06 lms-theory-of-estimation | 40 | 7 | 2 | the 2 unique: sufficiency examples; other 5 repeat ppt5 |
| teaching subtotal | 304 | 60 | 55 | |
| assignment 1 | 6 | 24 | 24 | 10 MCQ, 6 short, 4 long, 4 application |
| assignment 2 | 4 | 28 | 28 | 12 section A, 8 B, 4 C, 4 D |
| U01 past MTE papers | 5 question pages | 16 | 16 | schemes excluded; 8 blocks per paper |
| GRAND TOTAL THROUGH U01 | - | 128 | 123 | |

Boundary flag: the battery 95 percent CI example (ppt5 p024, lms-theory p029) uses lecture 25
machinery. Kept in because "Point and Interval estimation" is on the MTE syllabus list itself.
If dropped from the running U01 total: 127 / 122.

## Excluded, out of MTE syllabus (user order, 14 Sep)

| source | pages | status |
|---|---|---|
| lms-maximum-likelihood | 16 | out of MTE, not counted, not sorted |
| lms-method-of-moments | 11 | out of MTE, not counted, not sorted |
| mas2001-course-handout | 7 | no questions on any page |
| lms-theory p031 to p040 | 10 | confidence interval block (lecture 25), carries no question items |

Verified: none of these appear in the 128 above. lms-theory's counted 7 items all sit in
p016 to p029, which is the lectures 19 to 21 estimation block.

## Excluded, not items (in-scope pages with no countable question)

- deck01 p012, p017: non-math illustrations of the statistics definition
- deck01 p021: discussion prompts to students, no answers exist
- deck01 p115 to p116: narrative about probability of an exact value
- deck01 p133, p136: section transition slides
- ppt4 p017, p020: unlabeled one-line or visual illustrations

## Boundary class (display examples), excluded by default

These are labeled "Example" on the slides but only restate or showcase a definition or
concept, with no derived problem. Excluded from the 128/123. Listed here so the line is
visible, not hidden:

- deck01 p023 random experiment examples, p024 sample space examples,
  p025 mutually exclusive examples plus counter example, p027 independence examples
- ppt5 p003 and lms-theory p003: terminology examples (one shared block)
- ppt5 p007 and lms-theory p008: point vs interval comparison values (one shared block)

If you want this class counted too: raw becomes 136, unique becomes 129. Default stays
128 / 123 unless you say widen.

## Deck 01 manifest (30 items)

1. p041-042 tournament, 4 parts, solved
2. p046-047 laptops and desktops, 4 parts, solved
3. p048-049 basketball lineup, 2 parts, solved
4. p050 camera conditional probability, solved
5. p052 Bernoulli coin example
6. p053 two coin X example
7. p054-055 dice sum pmf
8. p056 two coin Y example
9. p057-059 geometric N example plus verify sum equals 1
10. p060 car lifetime example
11. p065 gas station pumps, 3 parts, NO solution
12. p066 k probability function, 4 parts, NO solution (key sits in assignment 1 long Q2)
13. p067-069 tune-ups, 3 parts, solved
14. p070-071 contractor forms, 4 parts, solved
15. p072-073 flashlight batteries, 4 parts, solved
16. p080-081 boards inspection, 3 parts, solved
17. p082-083 dice maximum M, 2 parts, solved
18. p085 cdf nondecreasing proof, solved
19. p089 die roll E(X) example
20. p093 prove E[aX plus b], solved
21. p094 E(X), E(X squared), E(2X+1) squared, answer given
22. p107-108 freezer dealer, 4 parts, solved
23. p109-111 magazine orders, solved
24. p124-125 f(x) equals 2x, verify and P(X under 1/2), solved
25. p126 continuous conditional probability, solved
26. p127-129 bus waiting times, 6 parts, solved
27. p138 exercise, two cdfs, NO solution
28. p139 distribution function to density, NO solution
29. p142 hospitalization E(Y), answer given
30. p146-147 Pareto pdf, 5 parts, solved

## Assignment manifests

- Assignment 1: MCQs 1 to 10, short 1 to 6, long 1 to 4, application 1 to 4 = 24
- Assignment 2: section A 1 to 12, section B 1 to 8, section C 1 to 4, section D 1 to 4 = 28

## Verification notes

- every page of all decks read cover to cover in the 14 Sep session
- counts cross checked by two automated marker sweeps plus manual page by page reconciliation
- recheck after your "sure?" question: unique column attribution fixed (shared estimation
  items now counted once under ppt5 so the column sums to 55), exclusion list and boundary
  class written out explicitly, no other discrepancy found
- the earlier annex estimate of 23 items for deck 01 was written before the full read;
  the post read number is 30, and 30 is the number that stands
- U01 adds 16 top-level blocks. Each paper has 8; multi-part Section C and question 8 count
  once under the locked rule. The four solution schemes are answer evidence, not new items.
  Exact-question comparison found no U01 duplicate inside the original 112-item corpus.
