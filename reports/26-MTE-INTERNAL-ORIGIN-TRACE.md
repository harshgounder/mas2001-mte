# Do the MTE questions come from our own material? 17 Sep 2026

Question asked: do any of the 16 MTE blocks come from the assignments, the lecture decks, or
any other material WE hold, rather than from an external book.

Method: every MTE block's text was matched by distinctive 4-gram overlap against the internal
corpus only (our assignments, our lecture decks, our module decks). All `paper-*` files were
EXCLUDED so the paper could not match itself.

## Result: 5 of 16 MTE blocks have an INTERNAL origin

```
  block    internal source                         match      what changed
  ─────────────────────────────────────────────────────────────────────────────
  M25-Q7   lms-standard-error-clt deck, Example 3   18/22 82%  none, VERBATIM
  M25-Q5   L10-11 Chebyshev deck, Q2               6/6  100%   verbatim stem
  M25-Q4   asgn 2024-25 #1, Q7                     6/9   67%   0-1 -> 0-4, target changed
  M24-B2   asgn 2024-25 #2, Q20                    8/20  40%   mean 6 -> 1/4
  M25-Q1   asgn 2025-26 bundle, Q1(f)              3/6   50%   same axiom check
```

The other 11 blocks have no internal match; their origins are the external books (G&K,
Walpole, H&T) already recorded in report 16.

## The five internal matches, verified by reading the source text

1. M25-Q7 IS A LECTURE SLIDE, VERBATIM.
   MTE:  "The average life of a machine is 7 years with a standard deviation of 1 year..."
   deck: lms-standard-error-clt, "Example: 3. The average life of a machine is 7 years with a
          standard deviation of 1 year. If the lives of these machines follow the normal
          distribution, find the probability..." (identical)
   The MTE removed "bread-making" (the Walpole tell) and kept the slide's numbers. So this
   question is taught in class, then examined. Not a book import.

2. M25-Q5 IS OUR CHEBYSHEV DECK QUESTION.
   MTE:  "A random variable X has mean = 10 and variance = 4. Using Chebyshev's inequality,
          find the value of the constant c..."
   deck: S&P L10-11 Chebyshev, "Q2. A random variable X has mean mu = 10 and variance
          sigma^2 = 4. Using Chebyshev's inequality, find the following..." (same stem).
   Already recorded as verdict DECK in report 16. This is the cleanest internal case.

3. M25-Q4 IS AN ASSIGNMENT QUESTION, RE-TARGETED.
   MTE:  "A random variable X is distributed between the values 0 and 4 so that its
          probability density function is..."
   asgn: 2024-25 #1 Q7 (and 2025-26 bundle Q9), "A random number X is distributed at random
          between the values 0 and 1 so that its..." (0-1 changed to 0-4).

4. M24-B2 IS AN ASSIGNMENT QUESTION, CONSTANT CHANGED.
   MTE:  "The length of time a person speaks over phone follows exponential distributions
          with parameter 1/4..."
   asgn: 2024-25 #2 Q20, "The length of a time a person speaks over phone follows exponential
          distributions with mean 6..." (mean 6 changed to parameter 1/4, same story).
   Note: the MTE block was ALSO traced to G&K chapter 5 (the telephone example). So this is a
   G&K example that reached the assignment, then the paper.

5. M25-Q1 IS AN ASSIGNMENT AXIOM CHECK.
   MTE:  "If f(x) is the probability density function of a continuous random variable, then
          the integral from -inf to +inf..."
   asgn: 2025-26 bundle Q1(f), "If f(x) is probability density function of a continuous random
          variable, then integral f(x) dx = ..." (the same total-mass check).

## The pattern this reveals (the important part)

```
  THE MTE IS BUILT FROM TWO LAYERS:

  layer 1  OUR OWN MATERIAL (5 blocks)
             the lecture/module decks (2: M25-Q7, M25-Q5)
             the assignments (3: M25-Q4, M24-B2, M25-Q1)
           the setter takes a class slide or a graded assignment item and re-asks it.

  layer 2  THE TEXTBOOKS (the other 11)
             G&K dominant, then Walpole, then H&T/Devore.

  THE CHAIN FOR SEVERAL BLOCKS IS: book -> assignment -> MTE.
     the telephone exponential: G&K ch5 -> assignment 2024-25 #2 Q20 -> MTE 2024 B2 and
     MTE 2025 Q6 (mean changed each time: 6 -> 1/4 -> 3).
     the Chebyshev inverse pair: G&K -> ETE/assignment -> MTE.
```

## What this means for study

```
  1. the module decks ARE the exam. M25-Q7 and M25-Q5 are deck items re-asked. Reading the
     decks is not optional, it is where 2 of 16 verified blocks came from.
  2. the assignments are exam rehearsal. 3 of 16 blocks are assignment items re-asked with one
     constant or target changed. Do the 2024-25 and 2025-26 assignments: they feed the paper.
  3. the mutation pattern is consistent: same skeleton, change one constant or target.
     telephone 6 -> 1/4 -> 3, cable 0-1 -> 0-4.
```

## Honest limits

- 4-gram overlap with the internal corpus finds literal text reuse. A block re-worded heavily
  would not match, so 5 is a floor, not a ceiling.
- M24-B2 matched BOTH the assignment (internal, 40%) and G&K (external). Both are true; the
  assignment is the nearer ancestor.
- the matching is on our text extractions, which carry the reseller watermark tags
  (`MSV16OVAX...`), already stripped before matching.
