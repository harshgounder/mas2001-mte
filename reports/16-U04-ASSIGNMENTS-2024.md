# U04 audit: 2024-25 assignments

Date: 16 September 2026  
Scope: six source files, 15 pages

## Processing and page review

All 15 pages converted with `gpt-5.6-luna` through commandcode and returned `ok`. Every page
was then checked against its rendered source. The review made four transcription or format
repairs:

- assignment 1 Q2: restored `upturned faces` after the model produced a nonsense word
- assignment 1 Q6: restored the second `2k` probability that the model omitted and rebuilt
  the nested table as valid Markdown
- assignment 3 episode 2 page 2: changed the false page heading from section D to the
  continued section C; the real section D heading remains lower on the page
- assignments 4 and 5: escaped four currency symbols that otherwise opened broken math spans

## Edition identity

`2024-2025-Assignment 3.pdf` and `2024-2025-Assignment 3 Episode 2.pdf` are different
editions, not duplicate files. They share much of sections A and B, but differ at A10, B2,
several section C questions, and D3 through D5. Both are retained under separate labels.

## Defects and cautions in the faculty sources

These statements remain verbatim in the converted pages.

1. Assignment 1 skips Q14, moving directly from Q13 to Q15. Q16 gives probabilities
   `0.1, 0.2, 0.5, 0.1`, which sum to 0.9 and therefore do not define a probability
   distribution. Q5 asks for `Var|X|`; comparison with the same Chebyshev template elsewhere
   suggests `Var(X)` was intended. As printed, the inequality alone does not uniquely
   determine the mean and variance without an unstated equality-and-centring assumption.

2. Assignment 2 item 1(i) prints binomial `p = 20`, and item 1(v) prints `p = 25` while also
   calling the result a Poisson distribution. A binomial probability must lie from 0 to 1;
   the likely intended values are 0.20 and 0.25. Item 1(iii) deliberately or accidentally
   proposes binomial mean 5 and standard deviation 3, which is impossible because binomial
   variance cannot exceed its mean.

3. Assignment 2 Q8 asks for a number of students but labels its supplied answer `46 marks`.
   Q12 gives the standard-normal area from 0 to 1.15 as 0.3746; standard tables give about
   0.3749. Q17 reverses the second normal-table pair, printing `phi(0.19) = 0.50` where the
   intended fact is `phi(0.50) = 0.19`. Q18 prints `phi(0.866) = 0.051`, which is not a
   standard mean-to-z or cumulative-normal value and is inconsistent with its supplied
   at-most-four answer.

4. In the first assignment 3 edition, A5 prints `E(T1)` for both statistics. The episode 2
   edition confirms that the second expression belongs to `E(T2)`. In both editions, D2 asks
   whether an estimator based on a fixed sample of three observations is consistent. No
   estimator sequence indexed by increasing sample size is defined, so consistency cannot be
   decided as written.

5. The first assignment 3 edition describes a known population variance in C3 but supplies
   the t critical value 2.262 rather than the corresponding normal critical value 1.96. Its
   D4 requests a 99 percent interval for ten observations but supplies 1.833, the common
   two-sided 90 percent t critical value with nine degrees of freedom, not the 99 percent
   value.

6. Assignment 4 Q10(A) and assignment 5 B1 attach `cm` to a variance; the unit should be
   square centimetres. Assignment 4 Q16 names its alternative as `H0: theta = 4`; that second
   hypothesis should be `H1`. Q10(B) asks for evidence to support an equality null, although
   a standard test can only reject or fail to reject it.

7. Assignment 5 B2 labels battery-life variances in hours rather than square hours. B4 shifts
   between people and families for the same consumer counts. Its section D numbering skips
   D4 and moves from D3 directly to D5.

## Cross-page integrity

- assignment 3 D4 starts at the bottom of page 2 and continues on page 3
- assignment 4 Q8 starts on page 1 and continues on page 2
- assignment 4 Q13 starts on page 2 and continues on page 3

The assembled documents preserve each continuation without inventing a new question.

