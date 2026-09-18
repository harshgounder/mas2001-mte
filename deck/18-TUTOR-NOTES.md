# 18 TUTOR NOTES: the top 40, one at a time

Ledger of the walkthrough series. One question per sitting, user says "done" to advance.
Each block: the wording decode, why it works, methods, the fast exam path, edge cases,
self-checks. Questions from deck/17-TOP-40-CANDIDATES.md.

Progress: Q1 done (18 Sep). Next: A2.

═══════════════════════════════════════════════════════════════════════════
Q1 = A1 · Chebyshev forms, spot the fake · `***` · 2 marks · MCQ
real source: MTE 2024-25, block A3 (the actual paper)
family: Chebyshev, graded 9+ times across the papers and assignments
═══════════════════════════════════════════════════════════════════════════

## The question, verbatim

If X is a random variable with mean mu and variance sigma^2 and K is any positive
number, then which of the following is/are NOT the Chebyshev's inequality?
(a) P{|X - mu| >= k sigma} <= 1/k^2
(b) P{|X - mu| < k sigma} >= 1 - (1/k^2)
(c) P{|X - mu| >= k} <= k^2/sigma^2
(d) P{|X - mu| < k sigma} >= sigma^2/k^2

## The words, decoded

```
  +---------------------------------------------------------------+
  | "which ... is/are NOT"      multi-select: pick EVERY failure.  |
  |                             expect a PAIR, the setter builds  |
  |                             the options as two valid + two    |
  |                             broken twins.                     |
  | "K is any positive number"  the gate: k > 0, and k counts      |
  |                             SIGMAS (standard deviations).     |
  | "mean mu and variance s^2"  only these two numbers may appear  |
  |                             in the statement.                 |
  | "Chebyshev's inequality"    the distribution-free bound: the   |
  |                             one result that never asks what    |
  |                             shape X is.                       |
  +---------------------------------------------------------------+
```

The trap family: two legal forms dressed up with (i) a stray sigma and (ii) a flipped
fraction or a swapped bound. Check units first, fraction second, done.

## The fact (the whole topic in two lines)

```
  TAIL    P( |X - mu| >= k*sigma ) <= 1 / k^2
  MIDDLE  P( |X - mu| <  k*sigma ) >= 1 - 1 / k^2        <- complement of the tail
```

Complement pipeline (why the middle form looks the way it does):

```
  P(tail) <= 1/k^2
      |  P(not tail) = 1 - P(tail)
      v
  P(middle) = 1 - P(tail) >= 1 - 1/k^2        (subtracting a smaller quantity
                                               flips the direction: >=)
```

## The picture

```
                    shape does not matter
            .-'''-.
          .'       `.          k = the number of SIGMAS
         /           \         the SAME bound fits every shape
        /             \
   ----+---+-----+----+---+----
       |<--kσ-->| μ  |<--kσ-->|
       ^TAIL            TAIL^
       each tail <= 1/(2k^2)  ->  both tails <= 1/k^2
       middle ( -kσ, +kσ ) >= 1 - 1/k^2
```

## The ruler (units check)

```
  sigma is the RULER. k counts rulers.
     |-----|-----|-----|-----|
     0    1σ    2σ    3σ    4σ
  legal  :  |X - mu| compared against  k · sigma
  decoy  :  |X - mu| compared against  k alone     (rule broken)
```

The two legality checks, applied to ANY claimed form:

```
  CHECK 1  deviation side: |X - mu| versus k·sigma ?    no -> NOT Chebyshev
  CHECK 2  bound: exactly 1/k^2 (tail) or 1 - 1/k^2 (middle)?
           anything with a flipped fraction or a stray sigma -> NOT Chebyshev
```

## The option audit (the actual solve)

```
  opt | deviation side    | bound       | verdict
  ----+-------------------+-------------+-------------------------------------
  (a) | |X-mu| >= k·sigma | 1/k^2       | VALID   (tail form)
  (b) | |X-mu| <  k·sigma | 1 - 1/k^2   | VALID   (middle form, the complement)
  (c) | |X-mu| >= k       | k^2/sigma^2 | NOT     (sigma fell off the ruler, and
      |                   |             |          the fraction is inverted: the
      |                   |             |          raw-units form would need
      |                   |             |          sigma^2/k^2, not k^2/sigma^2)
  (d) | |X-mu| <  k·sigma | sigma^2/k^2 | NOT     (bound swapped: must be 1-1/k^2)
  ----+-------------------+-------------+-------------------------------------

  ANSWER: (c) and (d) are NOT the Chebyshev inequality.
```

Kill shot for (c), so it never feels like trust:

```
  take sigma^2 = 100, k = 1. option (c) would claim
      P( |X - mu| >= 1 ) <= 1/100 = 0.01
  now let X = mu +/- 10, each with probability 1/2.
      then |X - mu| = 10 >= 1 ALWAYS, so P = 1.
  1 <= 0.01 is false, so (c) cannot be an inequality that always holds.
```

## The k-table (memorize three numbers)

```
     k   |  1/k^2  |  middle >= 1 - 1/k^2  | comment
     1   |   1     |  0                   | vacuous, never bites
     2   |  1/4    |  3/4                 | the standard ask
     3   |  1/9    |  8/9                 |
     4   |  1/16   | 15/16                | the flex
  memorize: 3/4, 8/9, 15/16  (this is literally item 3 of the deck's last-hour list)
```

## The 40-second exam protocol

```
  STEP 1 (10s)  circle "NOT" and "any positive k"
  STEP 2 (20s)  per option: units check, then bound check
  STEP 3 (10s)  mark BOTH failures, move on. this MCQ is a 2-mark gift.

  flowchart:
     "which are NOT ...?"
        |
        v
     for each option:  |X-mu| vs k·sigma ?
        |no  ---------------------------> MARK as NOT-Cheb
        |yes
        v
     bound exactly 1/k^2 or 1-1/k^2 ?
        |no  ---------------------------> MARK as NOT-Cheb
        |yes
        v
     valid form. leave it. next option.
```

## One fact, five disguises (the family, all inside the top 40)

```
  A1  spot the fake form        <- this question (real M24-A3)
  B1  find the constant c       (real M25-Q5: mu=10, var=4, P<=0.04 -> find c)
  C7  inverse: recover mu, var  (P(-2<X<8) >= 21/25 -> find E(X), Var(X))
  B2  bound vs exact value      (dice: bound 35/54 vs exact 1/3)
  A10 the numbers themselves    (3/4, 8/9, 15/16 as a quick MCQ)
```

## Edge cases (the marks live here)

```
  1. k <= 1: the bound goes vacuous (1 or worse). "any positive k" may be
     WRITTEN for k <= 1, it just says nothing. It bites only for k > 1.
  2. >= vs >: tail form uses >= on the outside; middle form uses <. The real
     options follow this exactly. A form that flips these is suspect.
  3. weaker-but-true decoys: P(middle) >= 1/2 is TRUE for k = 3 (8/9 implies
     1/2), but it is not THE inequality. In "which is NOT" questions, only the
     exact textbook forms count as valid.
  4. applicability sibling (the assignment MCQs): "Chebyshev requires the
     distribution to be normal" is FALSE. Zero distribution needed, only mu
     and sigma^2.
  5. the L10-11 deck's own Q3 mis-states its row (errata 15). Drill deck Q1
     and Q2 only.
```

## Self-checks (answers below the bar)

```
  a) k = 3: the middle bound is ____.
  b) true or false: Chebyshev works without knowing the distribution.
  c) which is/are NOT valid forms:
     (a) P(|X-mu| >= 4σ) <= 1/16
     (b) P(|X-mu| <  4σ) >= 15/16
     (c) P(|X-mu| >= 4σ) <= 16/σ^2
     (d) P(|X-mu| <  4)  >= 15/16
  ------------------------------------------------
  answers: a) 8/9   b) TRUE   c) (c) and (d). Note (d) is the sneaky one: right
  number, but the deviation side lost its sigma.
```

Done marker: user replies "done" -> next block = A2, the random variable definition
(asked three times across ETE papers).
