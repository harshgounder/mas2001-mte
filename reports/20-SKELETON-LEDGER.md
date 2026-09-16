# Skeleton ledger: every course question traced by structure

Purpose: per the order of 16 Sep, the questions are copies of standard problems whose
constants get changed while the structure stays fixed. This ledger tracks each question by
its SKELETON (structural pattern), the source, the value deltas against the source, and
every other place the same skeleton appears in our materials.

Status legend: TRACED (source identified), PARTIAL (family identified, exact book or
exercise open), OPEN (still hunting).

Correction on the "Palaniammal" scan: the file obtained from archive.org (item
in.ernet.dli.2015.136274, whose page suggests Palaniammal) is actually Davenport,
"Probability and Random Processes: An Introduction for Applied Scientists and Engineers"
(its own running headers, chapter set and 1960s references identify it). Probes for pens,
telephone, insurance, subway, 21/25 all return zero in its OCR, so it is irrelevant to our
items. Palaniammal's cited titles (Probability and Random Variables; Probability and Random
Processes, PHI) remain unlocated; ResearchGate and Academia.edu copies are gated.

Provenance pack (this report plus siblings, all on branch audit/provenance-accounting):
16 source provenance and confirmations, 17 ETE intake, 18 corpus accounting, 19 Hermes
session cross-check and correction register, 20 skeleton ledger (this report; renumbered
from 19 when the cross-check line landed in the merge of 16 Sep).

## MTE skeletons (16 blocks, from the evening sweep)

| # | skeleton (structure) | our version | source | value deltas |
|---|---|---|---|---|
| S01 | Poisson mean m, Y=2X, ask E(Y), Var(Y) | M24-A1, m=0.5 | bank-standard skeleton (exact open) | - |
| S02 | Triangular pdf on (0,2) peak at 1, ask CDF piece | M24-A2 | G&K 8-1-5 triangular family | piece to identify |
| S03 | List of Chebyshev forms, pick the false | M24-A3 | definitional, any text | - |
| S04 | Poisson ratio conditions fix lambda and mu, ask Var(X-2Y) | M24-B1, lambda=2, mu=3 | G&K Poisson example (answer 14) | VERBATIM |
| S05 | Person speaks on telephone, exponential density A e^(-x/theta), ask A, then tail/middle/short probabilities | M24-B2 (param 1/4, asks >6, 7-12, <=5 + mean/var) | G&K ch5 exercise 10 (theta=5, asks >10, <5, 5-10) | theta 5 to 4; asks renumbered; mean/var added |
| S06 | Uniform on (a,b), compare Chebyshev bound vs actual for abs(X-E(X)) >= 2 sqrt(V(X)) | M24-B3, interval (-1,1) | G&K exercise 15(b), interval (-1,3), bound 1/4 exact 0 | interval changed; same bound value |
| S07 | Trains every T minutes from time A to B, passenger uniform window, ask wait thresholds | M24-B4, T=15, 4 AM, 9:00-9:30, <6 and >10 | G&K subway example (T=30, midnight-6, >=20 min); 4 AM form circulates on question sites | T and window changed |
| S08 | Rainfall X ~ N(m, v) per day, thresholds + weekly binomial count | M24-C1a, N(2.6, 34.5) | OPEN | - |
| S09 | Binomial with mean fixed and P(X=1)=P(X=2), ask var and tails | M24-C1b, mean 5/3 | OPEN (classic skeleton) | - |
| S10 | Density integral equals 1 recognition | M25-Q1 | definitional | - |
| S11 | Poisson pmf with mean = e, substitute | M25-Q2 | definitional drill | - |
| S12 | Sufficiency definition | M25-Q3 | H&T 6.7 concept | - |
| S13 | Density k x^a (c - x)^b on (0, c), find k, mean, variance | M25-Q4, k x^3 (4-x)^2 | ABES Institute sample paper Q6(b) (cross-check); originating book still open | sample asks standard deviation, paper asks variance |
| S14 | Chebyshev, mean and variance given, find constant C for bound p | M25-Q5, 10, 4, 0.04 | L10-11 deck Q2(iv); family = G&K Chebyshev block | VERBATIM vs deck |
| S15 | Telephone exponential with mean m, ask two time probabilities | M25-Q6, mean 3 | same as S05 (G&K ch5#10) | theta 5 to 3; also circulates as a numbered StudyX item |
| S16 | Machine life ~ N(7, 1), sample n=9, probability average in window | M25-Q7, 7y, sd 1, n=9, 6.4-7.2 | Walpole, Myers, Myers, Ye, Probability and Statistics for Engineers and Scientists, Problem 8.25 (cross-check verified; Chegg and Vaia copies confirm the number) | "bread-making" dropped; same 7, 1, 9, 6.4, 7.2 values |
| S17 | Typist letters Poisson application, two conditions | M25-Q8(i) | circulating: Bartleby, StudyX, Studocu Poisson notes; found inside an exam compilation (CourseHero 229513024) | exact book open |
| S18 | t unbiased for theta, show t^2 biased for theta^2 | M25-Q8(ii) | G&K estimation chapter exercise 6 | VERBATIM |

## Assignment and ETE skeletons (confirmed so far)

| # | skeleton | our occurrences | source |
|---|---|---|---|
| S19 | Cable p.d.f. 6x(1-x), check, find median-point b, CDF, interval prob | asgn-24-25 #1 Q3; re-sess S4 C1 | G&K Ex 5.3 |
| S20 | Car hire Poisson mean 1.5, neither used / refused | asgn-24-25 #2 Q11; re-sess S3 B2 | G&K Ex 7.24 |
| S21 | Normal 31% under 45, 8% over 64, find mean and sd | asgn-24-25 #2 Q17; ETE S4 24-25 B4 | G&K ch8 exercise set |
| S22 | Radio tube life 100/x^2, replacement probabilities | asgn-24-25 #1 Q12 | G&K Ex 5.16 |
| S23 | Man with n keys, mean and variance of trials (with/without elimination) | asgn-24-25 #1 Q15 | G&K Ex 6.18 |
| S24 | Symmetric die 600 times, lower bound for 80-120 sixes | asgn-24-25 #1 Q10 | G&K Ex 6.48 |
| S25 | Book 520 pages 390 errors, Poisson, 5 pages no error | asgn-24-25 #2 Q5 | G&K Ex 7.27 |
| S26 | Chebyshev inverse: P(-2<X<8) >= 21/25 find E, Var | asgn-24-25 #1 Q5; ETE B1; Chebyshev deck Q1 | G&K (sigma=2, k=2.5) |
| S27 | Chebyshev inverse: P(4<X<16) >= 24/25 find E, Var | ETE S4 24-25 B3 | G&K family (variant) |
| S28 | Pens 10% defective, box of 12, exactly/at least/none | deck L12-13; ETE S3 25-26 B2; assignments | OPEN; confirmed circulating (askfilo x2, StudyX x2, Chegg); candidates: Palaniammal or Sundarapandian |

## Round 4 additions (cross-check merge + same-evening G&K matches)

- Cross-check (report 19 line) closed two opens: M25-Q7 = Walpole Problem 8.25;
  M25-Q4 = ABES Institute sample paper Q6(b). Both folded into the table above.
- G&K "Example 7.26": six coins tossed 6,400 times, Poisson approximation = assignment
  2024-25 #2, Q6, word for word.
- G&K "Example 7.30": Poisson variate with P(X=2) = 9P(X=4) + 90P(X=6) = assignment
  2024-25 #2, Q1(iv) (G&K then asks the skewness coefficient; our version asks mean and
  variance).
- G&K chapter 8 exercise: soldiers' heights, mean 68.22, variance 10.8, over six feet in
  a regiment of 1,000 = assignment 2024-25 #2, Q12, word for word (same phi table values
  printed).
- Cross-check corrections now live in report 16 and report 18 (superseding the earlier
  lines): 383 gross instances, 646-page corpus ledger, deck block count 30, and the
  originality language removed where it outran the evidence. The machine-readable layers
  (corpus page ledger, deck block ledger, question instance ledger, external source
  inventory) are in reports/evidence/ on this branch.

## Value-delta log (the mutation evidence)

- S05/S15 telephone theta: 5 (G&K) then 6 (asgn-24-25 #2 Q20) then 4 (M24-B2) then 3 (M25-Q6).
- S06 uniform Chebyshev interval: (-1,3) (G&K) then (-1,1) (M24-B3).
- S07 trains: 30-min subway (G&K) then 15-min trains 4 AM (M24-B4 and circulating copies).
- S26/S27 Chebyshev inverse: sigma 2 with 21/25 (G&K) then sigma 3 with 24/25 (ETE S4).
- S16 machine: "bread-making machine" (circulating original) then "a machine" (our M25-Q7).

## Teaching deck skeletons (summary level, sweep of 16 Sep)

| deck | items | provenance note |
|---|---|---|
| notes-lecture-series-01-09 (30 items) | Devore-derived | verified samples: p041 = Devore Ex 2.1 verbatim, p072 flashlight, p107 freezer, p109 magazine, p146 cites Devore's own exercise numbering; class-level conclusion consistent with the deck's printed Text Book |
| ppt3-discrete (6 items) | G&K / Palaniammal class | p027 insurance example (5,000 men age 42) present; pens-family items; the deck prints the Indian trio as references |
| ppt4-continuous (7 items) | Mc Clave style | p042-043 customers-arrive exponential example matches the Mc Clave slide family; references print Mc Clave |
| ppt5-estimation (5 items) | standard estimation texts | p007 average response time example, p019 sample-size example; estimation block texts |
| lms-standard-error-clt (5 items) | Devore 9e class | p014 chemical product example; p017-018 machine-life example (the same skeleton as M25-Q7, S16) |
| lms-theory-of-estimation (7 items) | overlaps ppt5 | same two example families as ppt5 |

## Source library acquisition status

| book | status |
|---|---|
| Devore 9e + solutions manual | FULL TEXT on disk, diffed |
| Gupta and Kapoor (FMS) | FULL TEXT on disk (college mirror), diffed; 13+ item matches |
| Hogg Tanis Zimmerman 9e | FULL TEXT on disk, diffed |
| Palaniammal, Probability and Random Processes | the archive copy turned out to be Davenport (see correction); genuine copies gated (ResearchGate, Academia) |
| GGD, Outline of Statistical Theory Vol 1 | scan on disk, OCR COMPLETE, swept: classical exercise sets (items attributed to Parzen, Hoel, Banach, Bizley); contains a DIFFERENT pens problem (2.21, 100 from 1,000 with 10 defective) and a different insurance problem (5.17); no match for our opens |
| Feller Vol 1 | gated on archive.org (lending 401) and Scribd |
| Mc Clave, Statistics for Business and Economics | gated (archive lending; slides carry its style, L14-15 deck) |
| Sundarapandian | gated (Scribd, ResearchGate); not on archive.org |
| Devore 8e PDF | mirrors 403; 9e serves the diff |

## Opens: working verdict after the OCR wave

The pens (12, 1/10), rain (N(2.6, 34.5)) and k x^3 (4-x)^2 items are NOT in any acquired
text: Devore 9e, Gupta and Kapoor, Hogg and Tanis 9e, GGD volume one, Davenport. The pens
item circulates verbatim on question-answer sites (askfilo x2, StudyX x2, Chegg); rain and
density have no site copies found yet. Working class: "question-bank compilation or
mutated custom", not the six known books. Remaining acquisition targets that could still
close them: Palaniammal (both titles, gated everywhere), Sundarapandian (gated), Feller
and Mc Clave (lending-only). Status stays OPEN with the class noted.

---
Ledger v0.2, 16 Sep late evening (renumbered to 20; cross-check line merged). Grows as
hunts close. Evidence lives in report 16; counts in report 18; machine-readable layers in
reports/evidence/ (corpus page ledger, deck block ledger, question instance ledger,
external source inventory).
