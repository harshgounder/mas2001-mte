# 07 PATTERNS: how the setters mutate questions

## THE MUTATION TREE (intent vs incidentals)

```
                        A QUESTION
                             │
             ┌───────────────┴───────────────┐
             ▼                               ▼
      ┌──────────────┐               ┌────────────────┐
      │  INTENT      │               │  INCIDENTALS   │
      │  (RADICAL)   │               │  (SURFACE)     │
      ├──────────────┤               ├────────────────┤
      │ distribution │               │ numbers        │
      │ the ask      │               │ names          │
      │ solve path   │               │ units          │
      │              │               │ story dressing │
      └──────┬───────┘               └────────┬───────┘
             │                                │
       STAYS THE SAME                  CHANGES CONSTANTLY
       when reskinned                  (this is the M0 operator)
```

## THE FIVE OPERATORS AS A TREE

```
              ┌─────────────────┐
              │ M0 RE-SKIN      │  numbers/names/units/story
              │ TYPE UNCHANGED  │  <- ~90% of what the setters do
              └─────────────────┘
              ┌─────────────────┐
              │ M1 INVERT       │  swap given <-> asked
              │ NEW NODE        │  x->P  becomes  P->x
              └─────────────────┘
              ┌─────────────────┐
              │ M2 RE-CONDITION │  flip a structural condition
              │ NEW NODE        │  replace/no-replace, n<30 vs n≥30
              └─────────────────┘
              ┌─────────────────┐
              │ M3 RE-TARGET    │  same setup, different target
              │ NEW NODE        │  P(=k)->P(≤k)->P(>k)->conditional
              └─────────────────┘
              ┌─────────────────┐
              │ M4 COMPOSE      │  nest two models / chain
              │ ALWAYS NEW      │  Poisson per min then binomial
              └─────────────────┘
```

## THE NINE SLOTS AS A 3x3 GRID

```
   ┌───────────────┬───────────────┬───────────────┐
   │ 1 POINT       │ 2 TAIL        │ 3 INTERVAL    │
   │ P(X=k)        │ P(X>k)        │ P(a≤X≤b)      │
   ├───────────────┼───────────────┼───────────────┤
   │ 4 MOMENTS     │ 5 PARAMS      │ 6 INVERSE     │
   │ E, Var        │ recover λ,p   │ x for given P │
   ├───────────────┼───────────────┼───────────────┤
   │ 7 COUNT       │ 8 CONDITIONAL │ 9 COMPOSE     │
   │ N x P         │ P(A|B)        │ nest two      │
   └───────────────┴───────────────┴───────────────┘

   every question in every paper we hold is one cell, one distribution.
```

## THE VALUE-DELTA IDEA, DRAWN

```
   the skeleton (a textbook question)
   ┌────────────────────────────────────┐
   │ exponential, mean 5, find P(X>12)  │
   └────────────────────────────────────┘
                    │
     ┌──────────────┼──────────────┬──────────────┐
     ▼              ▼              ▼              ▼
  mean 5        mean 6         mean 4        mean 3
  (G&K orig)   (reskin)       (reskin)      (our paper)
     │              │              │              │
     └──────────────┴──────────────┴──────────────┘
                    │
          SAME solve path every time.
          Only the number moved.

   -> know the RADICAL cold, and the story changing costs nothing.
```

The course does not write new questions. It takes a skeleton from a textbook, reskins the
story, and sometimes flips the target. This file is the mutation system, the value deltas we
have actually seen, the new question types the system implies, and the siblings one mutation
away. Read it after you have done two papers; it turns the paper into a pattern you recognise.

## 1. The two layers of a question

```
  INTENT      the deep structure: which distribution, which ask, which solve path.
              This is the RADICAL. It does not change when the story changes.
  INCIDENTALS the numbers, names, units, story dressing, which slot the answer is asked in.
              This is the SURFACE. It NEVER changes the type.
```

That single split is the whole system. When a question looks new, find its radical: if the
radical is old, it is an old question wearing a costume.

## 2. The mutation operators

```
  M0 RE-SKIN      change numbers, names, units, story. TYPE UNCHANGED.
                  pens become sensors become bulbs. Same math.
                  examples: telephone mean 5 -> 6 -> 4 -> 3; subway 30min -> 4AM 15min
  M1 INVERT       swap given and asked. NEW NODE.
                  x -> P(x) becomes P -> x. moments -> parameters.
  M2 RE-CONDITION flip a structural condition. NEW NODE when the formula changes.
                  replacement on/off; n<30 vs n>=30; discrete vs continuous.
  M3 RE-TARGET    same setup, different target. NEW NODE when the method differs.
                  P(=k) -> P(<=k) -> P(>k) -> conditional -> expected count.
                  example: ABES asks SD, our paper asks VARIANCE on the same density.
  M4 COMPOSE      nest two models, or chain outputs. ALWAYS NEW NODE.
                  Poisson per-minute then binomial over the minute.
```

## 3. The change table (does it create a new type or not)

```
  change                                   new type?
  numbers only                             NO
  names / units / story only               NO
  rounding / decimal places                NO
  same formula, different answer slot       NO
  forward -> inverse                       YES
  point -> tail or interval                YES
  unconditional -> conditional             YES
  single -> expected count                 YES
  independence assumed -> not assumed      YES
  with replacement -> without              YES
  n small -> n large (if the distribution changes)  MAYBE
  one model -> two models nested           YES
  E -> Var -> E[h(X)]                      YES
  efficiency -> MSE comparison             YES
```

## 4. The value-delta log (mutations used on US, with the source)

```
  telephone exponential   mean 5 (G&K ch5 ex10) -> 6 -> 4 -> 3      M0 x3
  uniform Chebyshev       (-1,3) G&K ex15b -> (-1,1)                  M0
  subway/train wait       30-min subway G&K -> 15-min 4AM window      M0 + M2
  Chebyshev inverse       sigma 2, 21/25 G&K -> sigma 3, 24/25        M0
  machine life            "bread-making machine" -> "a machine"        M0
  density kx^3(4-x)^2     ABES sample asks SD, our paper asks VAR      M3
  pens defective          G&K family of 18 -> 12 pens, 3 parts         M0 (source OPEN)
  Poisson Y=2X variance   G&K answer 14 -> VERBATIM (uncostumed)       M0
  t^2 biased estimator    G&K estimation ex6 -> VERBATIM               M0
  six-coins 6400          G&K 7.26 family                              M0
  Poisson 9P/90P          G&K 7.30 family                              M0
  soldiers 68.22          G&K ch8 family                               M0
```

Pattern: nearly all mutations are M0 (reskin). M3 (retarget) appears once in the confirmed
set. M4 (compose) is rarer still. So the highest-value prep is: know the radicals cold and be
ready for the story to change, because the story almost always changes and the radical almost
never does.

## 5. The nine slots (the template every distribution shares)

```
  slot 1  point          P(X = k)
  slot 2  tail           P(X > k), P(X >= k), complement
  slot 3  interval       P(a <= X <= b)
  slot 4  moments        E, Var, E(X^2)
  slot 5  parameters     recover a parameter from a given probability or moment
  slot 6  inverse        quantile / cutoff / min n
  slot 7  expected count N x P
  slot 8  conditional    P(A | B) inside the model
  slot 9  composition    nest two models
```

Every question in every paper is one of these nine, on one of the five distributions. That is
the whole exam space. (The per-distribution coverage grid is in 05-DISTRIBUTIONS.md.)

## 6. New type nodes the radical analysis generates (be ready for these)

```
  7.a  DESIGN / MIN-SIZE INVERSION   "how large must n be so that ..."          HIGH RISK
       binomial: smallest n so P(at least one) > 0.9  -> n = 22
       CLT: smallest n for an SE target               -> n = 35
       Chebyshev: k for a given guarantee
  7.b  PARAMETER RECOVERY (general)  solve for l, p, mu, sigma from a probability or moment
       examples seen: p=5/8, l=10, l=2.3026, mu=87.18, b=5.5, moment matching
  7.c  DERIVED-VARIABLE ALGEBRA      min/max/sum/difference of rvs
       two dice max (2m-1)/36, Poisson sum additivity, B+B is B
  7.d  CONDITIONAL ON AN INEQUALITY  P(X=k | X>=j) = P(X=k)/P(X>=j) = 0.3207 (A2 B5)
  7.e  DECISION / OPTIMISATION       choose the best option from an expectation
       magazine 3 vs 4 copies, capacity sizing, which estimator to use
  7.f  APPROXIMATION CHOICE          Poisson for binomial (asked), binomial->normal with a
                                      continuity idea (z = 1.123)
  7.g  MSE / BIAS-VARIANCE           MSE(T4) = 25.75 vs Var(T3) = 0.3333, the honest compare
  7.h  SHEET GAPS                    geometric E and Var, hypergeometric mean: needed, not on
                                      the provided sheet
```

## 7. Siblings one mutation away (not yet asked, risk-ranked)

```
  rank  sibling                                    the mutation from something asked
  1     normal one-unknown recovery                from the two-unknown system, drop one equation
  2     binomial two-sided interval P(2<=X<=4)     from the one-sided tails (0.3367)
  3     CLT for a SUM not a mean                   sigma scales by sqrt(n)
  4     discrete conditional P(X=k | X>=j)         from the continuous conditional
  5     min-n design (binomial 22, CLT 35)         from the parameter recovery family
  6     geometric variance / tail                  from the geometric mean (graded once)
  7     independence CHECK question                from the independence rules
  8     MSE comparison                             from the efficiency question with bias allowed
  9     Poisson between-values                     from the tail family
  10    valid-cdf check                           from the find-k normalisation
```

These are the questions most likely to appear that we have NOT drilled. If time is short, do
the top four.

## 8. The recognition routine (apply to any unseen question)

```
  1 read the story, ignore the numbers
  2 name the distribution (or "none", if it is event probability)
  3 name the slot (1 to 9 above)
  4 if a slot-5 or slot-6, it is an inversion: set up, solve, convert back
  5 if two distributions appear, it is slot 9: do the inner one first
  6 check the boundary word (at least / more than) and the support
  7 check the units
  8 then compute
```
