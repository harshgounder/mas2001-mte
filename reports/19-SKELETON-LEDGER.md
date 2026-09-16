# Skeleton ledger: every course question traced by structure

Purpose: per the order of 16 Sep, the questions are copies of standard problems whose
constants get changed while the structure stays fixed. This ledger tracks each question by
its SKELETON (structural pattern), the source, the value deltas against the source, and
every other place the same skeleton appears in our materials.

Status legend: TRACED (source identified), PARTIAL (family identified, exact book or
exercise open), OPEN (still hunting).

Note on the Palaniammal scan on disk: its own running header reads "Probability and Random
Processes", while the course decks cite "Probability and Random Variables" (PHI Learning).
Same author, different title; the cited title is not yet located. OCR is running on the
scan in hand; if the pens or telephone item is absent there, "Probability and Random
Variables" remains a target.

Provenance pack (this report plus siblings, all on branch audit/provenance-accounting):
16 source provenance and confirmations, 17 ETE intake, 18 corpus accounting, 19 skeleton
ledger.

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
| S13 | Density k x^a (c - x)^b on (0, c), find k, mean, variance | M25-Q4, k x^3 (4-x)^2 | OPEN (inverse of the G&K 5.3 k-form) | - |
| S14 | Chebyshev, mean and variance given, find constant C for bound p | M25-Q5, 10, 4, 0.04 | L10-11 deck Q2(iv); family = G&K Chebyshev block | VERBATIM vs deck |
| S15 | Telephone exponential with mean m, ask two time probabilities | M25-Q6, mean 3 | same as S05 (G&K ch5#10) | theta 5 to 3; also circulates as a numbered StudyX item |
| S16 | Machine life ~ N(7, 1), sample n=9, probability average in window | M25-Q7, 7y, sd 1, n=9, 6.4-7.2 | bread-making machine classic (circulating; exact book open) | machine name dropped |
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

## Value-delta log (the mutation evidence)

- S05/S15 telephone theta: 5 (G&K) then 6 (asgn-24-25 #2 Q20) then 4 (M24-B2) then 3 (M25-Q6).
- S06 uniform Chebyshev interval: (-1,3) (G&K) then (-1,1) (M24-B3).
- S07 trains: 30-min subway (G&K) then 15-min trains 4 AM (M24-B4 and circulating copies).
- S26/S27 Chebyshev inverse: sigma 2 with 21/25 (G&K) then sigma 3 with 24/25 (ETE S4).
- S16 machine: "bread-making machine" (circulating original) then "a machine" (our M25-Q7).

## Source library acquisition status

| book | status |
|---|---|
| Devore 9e + solutions manual | FULL TEXT on disk, diffed |
| Gupta and Kapoor (FMS) | FULL TEXT on disk (college mirror), diffed; 13+ item matches |
| Hogg Tanis Zimmerman 9e | FULL TEXT on disk, diffed |
| Palaniammal, Probability and Random Processes | scan on disk, OCR RUNNING |
| GGD, Outline of Statistical Theory Vol 1 | scan on disk, OCR queued after Palaniammal |
| Feller Vol 1 | gated on archive.org (lending 401) and Scribd |
| Mc Clave, Statistics for Business and Economics | gated (archive lending; slides carry its style, L14-15 deck) |
| Sundarapandian | gated (Scribd, ResearchGate); not on archive.org |
| Devore 8e PDF | mirrors 403; 9e serves the diff |

---
Ledger v0.1, 16 Sep evening. Grows as hunts close. Evidence lives in report 16; counts in
report 18.
