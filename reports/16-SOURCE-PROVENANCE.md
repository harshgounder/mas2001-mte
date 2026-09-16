# Source provenance of course questions, v0 (16 Sep 2026)

Status: working document. Provenance mapping is a separate analysis layer. It never imports
external text into the corpus or the question bank. Our questions stay ours; this file only
records where they trace back to.

## Why this file exists

The 16 Sep session found that course problem material traces back to fixed published
sources, and verified the first links against the actual textbook. Receipts below.

## Assets secured (stored OUTSIDE this repo: ~/mas2001-devore/)

- Devore, Probability and Statistics for Engineering and the Sciences, 9th ed. Full
  textbook PDF (7.9 MB) + extracted text (7.28M chars).
- Complete official solutions manual for the 9th edition (4.5 MB) + extracted text
  (1.49M chars).
- Extracted text of the queue decks (L1-7, L8-9, L12-13, L14-15, L10-11 Chebyshev, the
  2025-26 assignment bundle) at ~/mas2001-devore/corpus-text/ (analysis copies only).
- External textbooks are deliberately NOT committed here: license + bank purity.

## Verified links (each receipt re-checked on disk 16 Sep)

1. The course deck `notes-lecture-series-01-09` prints the Devore cover and citation on its
   own page p011 ("Text Book: Devore 8e, Cengage 2012"). The slide deck is course-owned; the
   citation is printed by the course itself.
2. Deck p041 basketball problem equals Devore "Exercises, Section 2.1, problem 1", word for
   word including parts a to d. Three independent confirmations:
   - the extracted full text of the textbook itself,
   - Rice University Stat 305 posted solution ("Solution to Exercise 2.1"),
   - Chegg question id DEVORESTAT9 2.1.001 (chapter 2, section 1, exercise 1).
3. Further deck items located in the book/manual: flashlight batteries (p072), magazine rack
   p109, freezer dealer p107; the Pareto slide (p146) cites "introduced in Exercise 10",
   which is Devore's own internal exercise numbering used by the slide author.
4. Exam side: MTE 2025-26 Q5 (Chebyshev find-C, mu=10, var=4, bound 0.04) is the L10-11
   Chebyshev deck's Q2(iv), word for word in both raw texts. The L10-11 deck holds three
   worked classics: Q1 (E(X)=3, E(X^2)=13, lower bound for P(-2<X<8)), Q2 (mu=10, var=4,
   find the constant C), Q3 (X on -1,1,3,5: direct computation versus the Chebyshev bound).
5. Skeleton reuse across years (same problem, changed constants): telephone call (rate 1/4
   in the 2024-25 paper, mean 3 minutes in 2025-26), trains every 15 minutes (2024-25 paper,
   and in the L-decks), pens defective 1/10 with 12 pens (L12-13 deck, ETE S3 2025-26,
   assignments).

## Source library (per the course's own reference pages)

- Units 1-2 slides cite Devore as Text Book (8e), with advanced references listed.
- ppt3/ppt4 cite S.C. Gupta and V.K. Kapoor (Fundamentals of Mathematical Statistics),
  S. Palaniammal (Probability and Random Variables), V. Sundarapandian (Probability,
  Statistics and Queuing Theory).
- ppt5 and the LMS decks cite Devore (8e/9e) and Gupta and Kapoor.

Negative results so far (keyword pass over the full Devore 9e text): "telephone
conversation", "15-minute intervals", "pen manufactured" do not appear in Devore. Those
items point at the other cited texts; acquisition of those PDFs is in flight (background
download job), after which the same local diff will run.

## Round 2 confirmations (16 Sep, evening pass)

All found by local text diff against the acquired full texts. Each match below is word for
word in the course material and in the named source.

- G&K "Example 6.18": the man with n keys problem = assignment 2024-25 #1, Q15.
- G&K "Example 5.16": radio tube with p.d.f. 100/x^2 for x >= 100 = assignment 2024-25
  #1, Q12.
- G&K "Example 6.48": a symmetric die thrown 600 times, lower bound for 80 to 120 sixes =
  assignment 2024-25 #1, Q10 (G&K also carries a 720-throw variant as an exercise).
- G&K uniform-distribution example: subway trains every half hour from midnight to six,
  wait at least twenty minutes, X uniform on (0, 30), answer 1/3 = assignment 2024-25 #2,
  Q9 and ETE S3 2025-26 C1(b).
- G&K: sigma = 2, Chebyshev with k = 2.5 gives P(-2 < X < 8) >= 21/25 = the Chebyshev
  deck's Q1 and the ETE S3 2024-25 B1 family.
- G&K exercise 15(b): compare the upper bound of P{|X - E(X)| >= 2 sqrt(V(X))} with the
  exact probability for X uniform on (-1, 3). Bound 1/4, exact 0. This is the skeleton of
  MTE 2024-25 QB3, whose version uses (-1, 1).
- G&K "manufacturer claims that at most 10 per cent of his product is defective, 18 units
  inspected" = the pens-problem family. The pens version (12 pens, box) was not found in
  the G&K text; candidates: Palaniammal or Sundarapandian.
- L1-7 deck: Q2 (computers of six faculty members) and Q3 (basketball lineup) are Devore
  exercises, word for word; the deck's own references page prints Devore 8e as Text Book.
- L12-13 deck references page prints: Gupta and Kapoor; Palaniammal; Sundarapandian.
  L14-15 deck adds Mc Clave, Statistics for Business and Economics, whose slide style and
  copyright line the L14-15 examples carry (uniform 2 to 6, N(8,5), exponential 15/hr).
- Palaniammal and Sundarapandian PDFs on disk are scans without a text layer; OCR is
  queued. Devore 8e mirrors refused (403); the 9e text serves the diff.

## Next phase (the ledger)

1. OCR the Palaniammal and Sundarapandian scans, then run the same signature diff.
2. Enumerate every question of the corpus into a block-level ledger (id, source file,
   scope verdict, provenance verdict with evidence line). The corpus accounting in report
   18 supplies the block counts; the ledger adds the per-block provenance column.
3. For each un-matched question, run skeleton search (same wording, different constants)
   against the source texts and then the web, and record the family it belongs to.

---
Report 16, added 16 Sep 2026. v0.1 (same day): round-2 source confirmations appended.

