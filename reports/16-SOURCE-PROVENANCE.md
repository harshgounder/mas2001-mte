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
   Chebyshev deck's Q2(iv), word for word in both raw texts. The L10-11 deck in turn holds
   the classic pair Q1 (E(X)=3, E(X^2)=13, lower bound for P(-2<X<8)) and Q2.
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

## Next phase (the ledger)

1. Acquire Gupta and Kapoor, Palaniammal, Sundarapandian texts; run the same keyword and
   signature-phrase diff.
2. Enumerate every question of the corpus into a block-level ledger (id, source file,
   scope verdict, provenance verdict with evidence line).
3. For each un-matched question, run skeleton search (same wording, different constants)
   against the source texts and then the web, and record the family it belongs to.

---
Report 16, added 16 Sep 2026. Status: v0, receipts verified the same day.
