# F12 Q7b | Hypothesis testing (OUT of MTE)

```
  family      F12 hypothesis-out
  source      our paper, ETE 2024-25 S3 A4 - the one-sided / two-tailed MCQ
  drill ref   00-QUESTIONS-ONLY.md -> F12-hypothesis-out Q7b
  also in     F12-hypothesis-testing.md (same content)
```

═══════════════════════════════════════════════════════════════════════════════
PART 1: THE QUESTION
═══════════════════════════════════════════════════════════════════════════════

```
Testing H0: mu = 1000 against H1: mu > 1000 leads to
   a) One sided right-tailed test   b) One sided left-tailed test
   c) Two tailed test               d) None of these
```

═══════════════════════════════════════════════════════════════════════════════
PART 2: THE FULL ANSWER, FROM ZERO (every step, nothing assumed)
═══════════════════════════════════════════════════════════════════════════════

EVERY STEP:

```
  STEP 1  read the DIRECTION in H1: "mu > 1000" points RIGHT.
  STEP 2  a directional alternative = ONE-SIDED; the tail follows H1's arrow.
  STEP 3  answer: option (a), one-sided right-tailed.
```

THE PICTURE:
```
   H1: mu > 1000        H1: mu < 1000        H1: mu != 1000
   ----+   [tail]--->   <---[tail]  +----    <--[t]  +  [t]-->
       (a) right            (b) left              (c) two-tailed
```

TRAP: H1 with ">" or "<" is one-sided (the tail on that side); H1 with "!=" is two-tailed.
The tail side follows the ARROW of H1, and the rejection region is where H1 claims the
parameter sits.
