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
- The file downloaded under a Palaniammal name was misidentified. OCR title pages show it
  is Davenport, Probability and Random Processes, and it has been renamed outside the
  repo. No verified Palaniammal or Sundarapandian PDF was found on disk in the 16 Sep
  cross-check. The earlier claim that both were present was false. Devore 8e mirrors
  refused (403); the 9e text serves the diff.

## Round 3 confirmations (same evening, assignment and ETE items)

- G&K "Example 5.3": the electric cable problem, p.d.f. f(x) = 6x(1-x) on (0,1), check
  pdf / find b with P(X<b) = P(X>b) = assignment 2024-25 #1, Q3, and re-sessional S4 C1.
- G&K "Example 7.24": the car hire firm with two cars, Poisson demands mean 1.5, neither
  car used and demand refused = assignment 2024-25 #2, Q11, and re-sessional S3 B2.
- G&K chapter 8 exercise set: "In a normal distribution, 31% of the items are under 45 and
  8% are over 64. Find the mean and variance" = assignment 2024-25 #2, Q17, and ETE S4
  2024-25 B4 (G&K prints a companion variant on the same page).
- G&K "Example 5.13": bakery sales density (bread, hundreds of pounds) shares the chapter
  with the telephone, cable and radio-tube examples, the family source of the deck's
  continuous-distribution items.
- ETE sweep status: all seven papers segmented (82 auto-blocks; the manual enumeration
  stands at 97). Distinctive ETE blocks now mapped: 21/25 and 24/25 Chebyshev inverses
  (G&K), subway (G&K example), cable (G&K 5.3), car hire (G&K 7.24), normal 31/45 (G&K
  chapter 8), pens (deck and assignment family, source pending OCR), E(X) -3/6/9 table
  (deck family across assignment and summer paper); the testing-topic blocks (t, F,
  chi-square, ANOVA) sit outside MTE scope and carry standard textbook forms.
- Historical status at that point: the pens problem book, the rain set N(2.6, 34.5),
  kx^3(4-x)^2, the ax^2+bx mean-0.5 block, and the 5/3 binomial block were open. The scan
  then called Palaniammal was later identified as Davenport. GGD volume one OCR completed;
  verified Palaniammal texts remain absent.

## MTE block-by-block provenance (v0, evening of 16 Sep)

All sixteen MTE blocks (2024-25 and 2025-26) have been run against the extracted full texts
of Devore 9e, Gupta and Kapoor, and Hogg and Tanis 9e, plus targeted web hunts. That sweep
does not prove that every block was copied, and it does not justify any claim about
originality. Ten blocks have a source or family lead, five are generic concept checks,
and one composite block remains open. Verdict classes: VERBATIM (word for word), RESKIN (same problem,
constants or interval changed), FAMILY (same skeleton in the source), CIRCULATING (lives on
question-bank sites), CONCEPT (definition check derivable from any text), DECK (the course
slide is the immediate origin).

| block | problem | verdict | origin / evidence |
|---|---|---|---|
| M24-A1 | Poisson mean 0.5, Y=2X, E and Var MCQ | CONCEPT | standard bank skeleton |
| M24-A2 | triangular pdf CDF MCQ | FAMILY | G&K section 8-1-5, triangular distribution |
| M24-A3 | Chebyshev forms, pick the false ones MCQ | CONCEPT | definitions in G&K / Devore |
| M24-B1 | P(X=1)=P(X=2), P(Y=2)=P(Y=3), Var(X-2Y) | VERBATIM | G&K Poisson chapter example ("Find the variance of X - 2Y", lambda=2, mu=3, answer 14) |
| M24-B2 | phone speech exponential, parameter 1/4 | RESKIN | G&K chapter 5 exercise 10, "lady speaks on the telephone" f(x)=Ae^(-x/5) [Shivaji Univ 1990]; mean 5 changed to 4 |
| M24-B3 | U(-1,1) Chebyshev bound versus actual | RESKIN | G&K exercise 15(b) with interval (-1,3), bound 1/4, exact 0; interval changed to (-1,1) |
| M24-B4 | trains every 15 min, 4 AM, arrival 9:00-9:30 | FAMILY + CIRCULATING | G&K subway example (uniform wait on (0,30), answer 1/3); the 4 AM form circulates on StudyX, Gauthmath, Transtutors |
| M24-C1 | rainfall N(2.6, 34.5) four parts + binomial week; binomial mean 5/3 part | OPEN | not found in Devore, G&K, H&T, Davenport OCR, or GGD volume 1 OCR; verified Palaniammal and Sundarapandian texts are absent, so their contents have not been searched |
| M25-Q1 | density integral MCQ | CONCEPT | axiom of total mass |
| M25-Q2 | Poisson mean e MCQ | CONCEPT | substitution drill |
| M25-Q3 | sufficiency MCQ | CONCEPT | H&T section 6.7, sufficient statistics |
| M25-Q4 | f = kx^3(4-x)^2, find k, mean, variance | RESKIN + CIRCULATING | ABES Institute sample paper Q6(b) carries the same support and density and asks for k, mean and standard deviation; the MTE changes standard deviation to variance; a Brainly repost carries the same family; originating book still open |
| M25-Q5 | Chebyshev find c, mu=10, var=4, bound 0.04 | DECK | L10-11 Chebyshev deck Q2(iv) word for word |
| M25-Q6 | telephone conversation, mean 3 | RESKIN + CIRCULATING | G&K chapter 5 exercise 10 re-skinned (mean 5 to 3); the same text circulates as a numbered item on StudyX |
| M25-Q7 | machine life 7 years, 9 samples | RESKIN | Walpole, Myers, Myers and Ye, Probability and Statistics for Engineers and Scientists, Problem 8.25 in the 8e index and retained in 9e; a university sheet identifies page 242; the exam deletes "bread-making" and keeps part (a) with the same 7, 1, 9, 6.4 and 7.2 values |
| M25-Q8 | (i) typist letters (ii) t^2 biased | MIXED | (i) circulating (Bartleby, StudyX, Studocu Poisson notes); (ii) G&K estimation chapter exercise 6, verbatim |

Result: 16 of 16 blocks were searched, but only 10 have a source or problem-family lead.
Five generic concept checks do not have an identified origin, and the composite C1 rain
and binomial block remains open. Labels such as CONCEPT and CIRCULATING are not provenance proof. The
mutation pattern supported by current evidence is: the telephone problem appears with mean 5 (G&K
original), 6, 4 and 3 across our materials; the uniform-Chebyshev comparison moves (-1,3)
to (-1,1); the trains problem keeps its skeleton across years.

Web evidence for the two follow-up corrections:

- Walpole Problem 8.25 indexed by book, chapter and problem number:
  <https://www.vaia.com/en-us/textbooks/math/probability-and-statistics-for-engineers-and-scientists-8-edition/chapter-8/problem-25-the-average-life-of-a-bread-making-machine-is-7-y/>
- University homework explicitly identifying it as Problem 8.25, page 242:
  <https://bashmuhndsa.wordpress.com/wp-content/uploads/2017/09/ie331-hw5-ch8-9.pdf>
- ABES Institute sample question-paper collection containing the kx^3(4-x)^2 problem:
  <https://naac.abesit.in/wp-content/uploads/2024/07/Sample-Question-Papers.pdf>
- Public repost of the same density family:
  <https://brainly.in/question/61111014>

## Next phase (the ledger)

1. GGD volume one and Davenport OCR are complete. A signature sweep found generic
   rainfall and fountain-pen material in GGD, but no exact open MTE signature in either
   text. Acquire verified Palaniammal and Sundarapandian texts before using either name
   for attribution, then run the same comparison for the pen problem, rain set,
   kx^3(4-x)^2 and the remaining ETE items.
2. Run the same block-by-block sweep for the 97 ETE / summer / re-sess blocks (first pass
   already shows Chebyshev, subway, pens, E(X) table and CLT overlaps).
3. Web hunt the still-open items (C1 rain set, Q4 density, bread-machine book, 5/3
   binomial) with exact-phrase searches and capture the source page links as evidence.

---
Report 16, added 16 Sep 2026. v0.1 (same day): round-2 source confirmations appended.
