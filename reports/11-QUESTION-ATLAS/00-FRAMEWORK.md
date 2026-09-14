# Question Atlas: framework and method

Built 14 September 2026 for MAS2001. Purpose: every example, exercise and question in
every MTE-scope deck, analyzed one at a time, tagged against multiple taxonomies, so the
MTE question pattern becomes visible instead of guessed.

## 1. Order of work (one deck at a time, slide by slide, question by question)

```
  deck                        file                          status
  01 notes-lecture-series    01-deck-lec01-09.md           IN PROGRESS (this pass)
  02 ppt3 discrete           02-ppt3-discrete.md           pending
  03 ppt4 continuous         03-ppt4-continuous.md         pending
  04 clt                     04-clt.md                     pending
  05 estimation (ppt5+lms)   05-estimation.md              pending
  06 assignments 1 and 2     (later, per your instruction) pending
  07 mock and question bank cross-check (later)            pending
```

Out of MTE scope decks (lms-method-of-moments, lms-maximum-likelihood) get a compact
sweep at the end, not full entries, unless you say otherwise.

## 2. Entry schema (every question gets all of these)

```
  ID            Q<deck><number>, stable, never renumbered
  source        deck, page file, slide title
  question      the exact ask, verbatim math where it matters
  what it is    one-line plain description
  type          primary family (probability, distribution, expectation, estimation, ...)
  subtype       the specific kind within the family
  knowledge     definitions, formulas, conditions needed before starting
  approach      the method the slide teaches
  steps         the solve path, numbered, as the slide does it
  alternate     other valid ways to solve, with the tradeoff
  intent        what the setter is testing, why this example exists on this slide
  bloom         Remember / Understand / Apply / Analyze / Evaluate / Create
  dok           Webb depth of knowledge 1 to 4
  math_group    MATH taxonomy: A (factual/routine), B (transfer/application), C (justify/interpret)
  solo          Biggs SOLO: uni / multi / relational / extended
  gaise         GAISE level for stats items: A (basic), B (intermediate), C (advanced), or n/a
  difficulty    1 to 5
  traps         the mistakes this question catches
  exam_use      how the MTE could ask this; in-scope verdict
  verified      computed on the machine or cross-checked? how
```

## 3. Taxonomy definitions used (so tags are exact, not vibes)

- Bloom, revised (Anderson and Krathwohl 2001): Remember (recall), Understand (explain),
  Apply (use in routine situation), Analyze (decompose, connect), Evaluate (judge, compare),
  Create (produce new).
- Webb DOK: 1 recall/definition, 2 skill/concept with a decision, 3 strategic thinking,
  multi-step reasoning with justification, 4 extended investigation.
- MATH taxonomy (Smith et al. 1996), used to tag math assessment items: Group A factual
  knowledge, comprehension, routine procedures; Group B information transfer, applications
  in new contexts; Group C justifying and interpreting, implications, appreciation.
- SOLO (Biggs): unistructural (one fact), multistructural (several facts unconnected),
  relational (connected whole), extended abstract (beyond the given).
- GAISE (ASA guidelines) for statistics items: Level A basic literacy, Level B
  intermediate, Level C advanced.
- Task demand (Smith and Stein): memorization, procedures without connections,
  procedures with connections, doing mathematics.

## 4. Slide scan result (which slides carry questions at all)

```
  deck notes-lecture-series-01-09   pages 1-147   question-bearing: ~50 pages, see entries
  ppt3-discrete-prob-dist           pages 1-28    question-bearing: 12 pages
  ppt4-continuous-prob-dist         pages 1-44    question-bearing: 15 pages
  lms-standard-error-clt            pages 1-19    question-bearing: 12 pages
  ppt5-estimation-summary           pages 1-26    question-bearing: 8 pages
  lms-theory-of-estimation          pages 1-40    question-bearing: 14 pages
```

## 5. Progress log

```
  14 Sep: framework written. Deck 01 census done (annex in 01-deck-lec01-09.md), entries
          D1-Q001 and D1-Q002 written and machine-verified. Resume marker: next entry D1-Q003
          (basketball lineup, slides p048-p049).
```
