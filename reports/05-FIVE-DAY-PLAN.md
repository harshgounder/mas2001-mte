# Five day plan to the MTE

Window opens Friday 18 September 2026 and closes Friday 25 September. Paper is 30 marks,
closed book. Today is Sunday 13 September, so there are five clear days: 13, 14, 15, 16, 17.

Reading refs are files in this repo. `md/<label>.md` is the assembled document,
`md/<label>/pNNN.md` is a single slide.

## Day 0, today, Sunday 13 September (evening, 3 hours)

Goal: know exactly what the paper can ask, and close the one hole that had no source (Chebyshev; the deck has since arrived).

1. Read `reports/00-SCOPE-AND-EXAM-FACTS.md` and `reports/01-COVERAGE-MAP.md`. 20 minutes.
   Outcome: you can say out loud which lectures are in scope (1 to 21) and which are not (22+).
2. Read `reports/03-FORMULA-SHEET.md` end to end. 40 minutes. Do not memorise yet, just map.
3. Chebyshev block, since the deck is short and the topic is cheap marks. `reports/03-FORMULA-SHEET.md` section E
   then `reports/04-QUESTION-BANK.md` section 6. 60 minutes. Re-derive the dice bound 35/54
   and the 19/24 bound by hand without looking.
4. Reproduce the two Chebyshev bounds from memory on blank paper. 20 minutes.
5. Skim `md/notes-lecture-series-01-09.md` p001 to p011, the course framing, once. 40 minutes.

Gate to pass before sleeping: you can write the Chebyshev inequality in both forms and
explain why it needs no distributional assumption.

## Day 1, Monday 14 September (4 hours, classes run as normal)

Goal: units 1 and 2, the 136 pages that only exist in the lecture deck.

1. `md/notes-lecture-series-01-09.md` p012 to p050. Statistics framing, random experiment,
   sample space, events, set relations, probability axioms, conditional probability.
   Read with the formula sheet section A open. 110 minutes.
2. Work the combinatorics problems on p046 and p048 properly, on paper. 30 minutes.
3. `md/notes-lecture-series-01-09.md` p051 to p087. Random variable, discrete rv, pmf, cdf,
   the pump example, the expected value slides. 80 minutes.
4. `md/notes-lecture-series-01-09.md` p088 to p111. Expectation, variance, the shortcut
   formula, rules of variance. 60 minutes.

Gate: write the pmf and cdf of the 3 children example from scratch, then check against
`md/mas2001-assignment-1/p001.md` and the key in `reports/04-QUESTION-BANK.md` section A.

## Day 2, Tuesday 15 September (4 hours)

Goal: continuous random variables, then the two big discrete distributions.

1. `md/notes-lecture-series-01-09.md` p112 to p147. Continuous rv, pdf, cdf, expectation,
   variance, the Pareto exercise on the last pages. 100 minutes.
2. `md/ppt3-discrete-prob-dist.md` p001 to p018, binomial. 60 minutes. Do the pens problem
   and the irregular die problem on paper before reading the solution slides.
3. `md/ppt3-discrete-prob-dist.md` p019 to p028, Poisson. 50 minutes. Learn the
   approximation conditions cold: n large, p small, np moderate.
4. Twenty minutes of pure recall: write E and Var for binomial and Poisson, plus the
   conditions for each, from memory.

Gate: solve "10 percent of pens defective, box of 12, find P(at least 2 defective)" without
looking. Answer is 1 minus (0.2824 + 0.3766) = 0.3410.

## Day 3, Wednesday 16 September (4.5 hours)

Goal: the four continuous distributions and the CLT block. This is the heaviest single day.

1. `md/ppt4-continuous-prob-dist.md` p001 to p006, uniform. 30 minutes.
2. p007 to p037, normal. 130 minutes. This is the largest single block in the paper's
   potential and the one with the most worked practice. Drill standardisation in both
   directions, forward from X to probability and inverse from probability to X.
3. p038 to p043, exponential. 50 minutes. Drill the lambda versus 1/lambda trap until it
   is automatic.
4. `md/lms-standard-error-clt.md` p001 to p018. 70 minutes. Standard error, then the CLT
   statement and the three worked examples.

Gate: state the CLT precisely, including the n greater than or equal to 30 rule of thumb,
and explain the difference between the sigma population and the standard error sigma over
root n.

## Day 4, Thursday 17 September (4.5 hours)

Goal: estimation block, then a full timed paper, then fix what the paper exposes.

1. `md/ppt5-estimation-summary.md` all 26 pages. 90 minutes. Then
   `md/lms-theory-of-estimation.md` p022 to p030 for the extra worked numericals only.
2. Sit `reports/07-MOCK-PAPER.md` closed book, 90 minutes, no formula sheet. Mark it with
   the worked solutions in `reports/08-MOCK-SOLUTIONS.md`.
3. Spend the rest of the day on whatever the mock exposed. Re-derive every formula you
   failed to recall. 90 minutes.

Gate: 24 or more out of 30 on the mock, with no formula looked up during the sitting.

## Day 5, Friday 18 September, window opens

1. Formula sheet read twice, out loud, 40 minutes.
2. The three Chebyshev values (k=2 gives 3/4, k=3 gives 8/9, k=4 gives 15/16) and the four
   distribution mean-variance pairs (binomial np and npq, Poisson lambda and lambda,
   uniform (a+b)/2 and (b-a)^2/12, exponential 1/lambda and 1/lambda^2, normal mu and sigma^2)
   from memory. 20 minutes.
3. No new material. Nothing below lecture 22.

## Re-pin, Monday 14 September evening (supersedes Days 0 and 1)

Written after the slides-versus-syllabus audit in `10-SLIDES-VS-SYLLABUS.md`. Four slots
remain before the window opens on Friday 18: tonight, then Tuesday, Wednesday and Thursday
17, the last clear day. The plan below assumes Days 0 and 1 were partial at best.

Tonight, 3 hours, covers what Day 0 and Day 1 were for:

1. Chebyshev block. `S&P L10-11` deck (arrived 15 Sep), then `reports/03-FORMULA-SHEET.md`
   section E, then `reports/04-QUESTION-BANK.md` section 6. 60 minutes. Re-derive the dice
   bound 35/54 and the 19/24 bound on paper without looking. Gate: write both forms of the
   inequality from memory and say why it needs no distributional assumption.
2. `md/notes-lecture-series-01-09.md` p012 to p062, one fast pass with the formula sheet
   open. 60 minutes. The examinable skeleton: sample space, axioms, conditional probability,
   event independence, random variable, discrete versus continuous.
3. `md/notes-lecture-series-01-09.md` p063 to p111, second pass at exam depth. 60 minutes.
   PMF/CDF layout, expectation, variance, the shortcut formula, the rules of variance.
4. If anything slips, it moves to Tuesday morning, not to 2 am.

The independence gap, 10 minutes, before Tuesday's distributions block: from
`reports/03-FORMULA-SHEET.md` sections C and D write down E(XY) = E(X)E(Y) under
independence and Var(X + Y) = Var(X) + Var(Y), then recompute Var(sum of two dice) = 35/6
from Var(one die) = 35/12. Assignment 1 already graded this rule, it is cheap to own.

Tuesday 15 September: Day 2 as written above, unchanged (continuous rv block, binomial,
Poisson).
Wednesday 16 September: Day 3 as written above, unchanged (uniform, normal, exponential,
standard error, CLT). This is the heaviest day; protect it.
Thursday 17 September: Day 4 as written above, unchanged (estimation block, then the mock
closed book, then repair what it exposes).

Checkpoint on Thursday after the mock: 24 or more out of 30 means stay the course. 18 to 23
means Friday morning goes to the weak block only, no new material. Below 18 means the weak
block is almost certainly the units 1 and 2 deck or the CLT, and Friday morning goes there
before the formula sheet drill.

## Weekly shape of a study day

```
  20 min   read the day's slide range once, fast, no notes
  90 min   second pass with the formula sheet open, derive every formula you meet
  60 min   problems, on paper, before reading the solution slides
  40 min   recall drill, blank paper, from memory
  30 min   redo yesterday's failures only
```

## Order of priority if a day collapses

1. Chebyshev, because it is guaranteed cheap marks when known (deck arrived 15 Sep, S&P L10-11).
2. Binomial and Poisson closed forms plus the exponential rate trap.
3. Standard error and the CLT, the whole of lectures 17 and 18 is usually one clean question.
4. Normal standardisation in both directions.
5. The estimation comparison layout.

## What to ignore

Maximum likelihood (lecture 22), method of moments (23), Bayesian estimation (24),
confidence interval mechanics (25, 27, 28), hypothesis testing and all the tests
(29 to 36). All of it is formally out of the mid term. Read the slides only if a CWS
deadline puts them back in play.
