# HOW AND WHY: the methodology behind the question set

Built 17 Sep 2026, on direct request ("is there any file that says how u made them and why
only those, same for the shapes and skeletons"). Until now the answer lived scattered across
report files; this is the single file that states it end to end.

Everything below is traceable to a file on disk. Where a number is a count, the counting rule
is stated. Where a claim is a judgement call, it is labelled as one.

═══════════════════════════════════════════════════════════════════════════════
1. THE EXACT QUESTION COUNTS (three different numbers, all real)
═══════════════════════════════════════════════════════════════════════════════

Three counts float around this project. They measure different things, and all three are
correct. This is the reconciliation:

```
   +--------+-----------------------------------------------------------------+
   |  158   | WORKED QUESTIONS. A worked question = a full zero-knowledge      |
   |        | solution: question block + steps + answer + traps.               |
   |        | = 160 header blocks minus 2 cross-reference stubs                |
   |        |   (F8 QUESTION 11b and F15 QUESTION 19 are pointers to questions  |
   |        |    solved elsewhere, not standalone questions).                  |
   +--------+-----------------------------------------------------------------+
   |  160   | the same 158 plus those 2 cross-reference stubs. counted by       |
   |        | grepping "^QUESTION n" headers across the F-files.                |
   +--------+-----------------------------------------------------------------+
   |  168   | DRILL ENTRIES in 00-QUESTIONS-ONLY.md: the 158 worked questions   |
   |        | PLUS the 10 assignment-1 MCQs (M1-M10), which live inside F14.5   |
   |        | as a table and get their own drill entries.                       |
   +--------+-----------------------------------------------------------------+
```

the current exact numbers on disk:

```
   per-file worked questions (headers, stubs included):
     F1  binomial              10        F9  clt/sampling           8
     F2  poisson                8        F10 definition/foundations 10
     F3  exponential            6        F11 expectation laws        6
     F4  uniform                4        F12 hypothesis testing     20
     F5  chebyshev              7        F13 assignment sheets      28
     F6  normal                 6        F14 foundations             1 (+10 MCQ table)
     F7  rv/pdf/cdf             6        F15 assignment bank 2      22
     F8  estimation            18
     ------------------------------------------------------------
     headers total            160   (158 real + 2 stubs)
   drill file entries         168   (158 + 10 MCQs)
```

═══════════════════════════════════════════════════════════════════════════════
2. WHERE THE QUESTIONS ACTUALLY LIVE (file by file)
═══════════════════════════════════════════════════════════════════════════════

```
   THE QUESTIONS themselves (this is the folder):
      /home/liebert511/mas2001-mte-s2/deck/worked/

      F1-binomial.md                ...  F15-assignment-bank-2.md
      00-QUESTIONS-ONLY.md             the drill file (all questions, no solutions)
      00-INDEX.md                      the map into the folder
```

every question in these files was copied from, or is a direct variant of, one of these SOURCE
documents (all on disk, all from the course itself):

```
   SOURCE TYPE                               WHERE ON DISK
   MTE papers (2)                            md/paper-mte-2024-25.md, paper-mte-2025-26.md
   MTE official solution schemes (2)         md/paper-mte-*-scheme.md   <- NEW this session
   ETE papers (7 sittings)                   md/paper-ete-*, md/paper-resess-*
   the slide decks (ppt3/ppt4/ppt5)          md/ppt3-discrete-prob-dist.md etc
   the lecture-notes deck (147 pages)        md/notes-lecture-series-01-09.md
   the LMS modules                           md/lms-*.md
   assignment sheets (both years)            md/mas2001-assignment-1/2.md
                                             + ~/mas2001-mte-audit-v1/text/asgn-*.txt
   textbook-derived (G&K, Walpole, Devore)   ~/mas2001-devore/sources/  (PDFs)
```

═══════════════════════════════════════════════════════════════════════════════
3. HOW THE QUESTIONS WERE SELECTED (the inclusion rule)
═══════════════════════════════════════════════════════════════════════════════

The selection rule, stated plainly. A question was included if and only if:

```
   R1. IT EXISTS IN OUR MATERIAL. Traced to a source document by text match.
       nothing invented, nothing "typical for this topic". if it has no
       on-disk origin, it is not in the set.

   R2. IT IS IN MTE SCOPE. The MTE scope = lectures 1 to 21, ending at
       "Characteristics of a good estimator" (~/PS/syllabus.txt).
       OUT: MLE, method of moments, Bayesian estimation, confidence
       intervals, hypothesis testing, t-test, F-test, chi-square, ANOVA.
       F8 and F12 carry some OUT-of-scope material from the ETE papers,
       and both files say so in their headers.
```

R2 has one deliberate exception, and it is worth stating why:

```
   THE EXCEPTION: F12 (hypothesis testing, 20 questions) is majority
   out-of-scope. It exists because the ETE papers contain two 10-mark
   hypothesis questions and the whole family appears in five sittings.
   Cost of including: one file to skip. Cost of EXCLUDING if the setter
   reaches for it: a whole 10-mark question with no drill behind it.
   Asymmetric risk, so it stays, clearly marked.
```

and an ordering preference, not a hard rule:

```
   P1. QUESTIONS FROM OUR OWN PAPERS FIRST (MTE, then ETE), because those
       are the ones the setter demonstrably uses.
   P2. THEN deck/assignment questions, because those are what the course
       expects you to be able to do.
   P3. THEN textbook-lineage questions when a paper item traces to a book.
```

═══════════════════════════════════════════════════════════════════════════════
4. WHY "ONLY THOSE" QUESTIONS (the two caps explained)
═══════════════════════════════════════════════════════════════════════════════

Two numbers cap the set, and both were chosen, not accidental:

```
   CAP 1: "2-3 questions per shape" (user directive).
     the set does NOT include every question in the corpus. it includes
     enough per shape to see the pattern, its variants, and its traps.
     examples of one shape, three sizes of it:
        binomial tail: pens "at least" (F1 Q1), bombs "at least 2" (F1 Q4),
                       families "at most 2" (F1 Q3)   = 3 sizes
        chebyshev inverse: 21/25 case (F5 Q3), 24/25 case (F5 Q4) = 2 sizes
     when a fourth question added nothing new, it was left out.

   CAP 2: THE CORPUS ITSELF.
     the source material is what it is: 2 MTE papers, 7 ETE sittings,
     2 assignment sheets + 2 more bank sheets, 4 decks, 4 LMS modules.
     every question in those documents is either in the set, pointed to,
     or genuinely redundant with something already in it.
```

what was deliberately NOT added (and why):

```
   invented "predicted" questions      -> user rule: dont invent it.
   textbook exercises without a paper
      trace (hundreds exist in Devore) -> dilutes; the papers only used a
                                          handful of book items, those are in.
   duplicate variants (same shape, same
      numbers, different paper)        -> noted as "asked twice" in the
                                          source line, not re-solved.
```

═══════════════════════════════════════════════════════════════════════════════
5. THE SHAPES AND SKELETONS: WHAT THEY ARE AND HOW THEY WERE DERIVED
═══════════════════════════════════════════════════════════════════════════════

Definitions first, because the two words get used loosely:

```
   FAMILY   = the distribution or topic: Binomial, Poisson, Normal, Estimation...
              (12 families in total)
   SHAPE    = (family, ask-type): "Binomial/point", "Chebyshev/inverse-c",
              "Normal/find-param"... the thing that decides WHICH method you run.
   SKELETON = a shape plus its structural details: which constants vary, which
              phrasing recurs. the setter's template. ("Poisson ratio conditions
              fix lambda and mu, ask Var(X-2Y)" is a skeleton.)
   MUTATION = the setter's change lever: M0 reskin, M1 invert, M2 re-condition,
              M3 re-target, M4 compose.
```

where each layer is documented on disk:

```
   +-----------------------------+--------------------------------------------------+
   | what                        | file                                             |
   +-----------------------------+--------------------------------------------------+
   | the 12 families             | reports/11-QUESTION-ATLAS/00-MTE-TOPIC-UNIVERSE.md|
   | the 34 shapes + IF/THEN     | deck/15-DECISION-MANUAL.md (Part 6 checklist)     |
   | the shape list + recall gap | reports (32-RECALL-FIRST-SKELETONS, on lane-c)    |
   | per-question skeleton trace | reports/20-SKELETON-LEDGER.md (S01-S28)          |
   | mutation analysis           | reports/11-QUESTION-ATLAS/00-MUTATION-ANALYSIS.md |
   | type-space audit            | reports/11-QUESTION-ATLAS/00-TYPE-SPACE-AUDIT.md  |
   | the count register          | reports/11-QUESTION-ATLAS/00-COUNT-REGISTER.md    |
   | provenance per source       | reports/16-SOURCE-PROVENANCE.md                   |
   +-----------------------------+--------------------------------------------------+
```

HOW THE SHAPES WERE DERIVED (the actual method, step by step):

```
   1. INDEX EVERY QUESTION in all 9 sittings + decks + assignments, with a
      (family, ask-verb) tag. -> the question-instance ledger (383 rows
      gross, in reports/evidence/question-instance-ledger.csv)

   2. GROUP BY (family, ask). Each group that appears at least once becomes
      a SHAPE. 34 (family,ask) shapes emerged.

   3. SPLIT BY PROVENANCE:
        shapes seen in the MTE papers      -> the 14 in-MTE shapes
        shapes seen ONLY outside the MTE   -> the 20 recall-gap shapes
      The recall-gap list is the safety net: "it's OK to mark something
      that does not come; it is NOT OK for something to come that we had
      not counted" (user's rule).

   4. TRACE EACH MTE BLOCK TO ITS SKELETON. For every one of the 16 MTE
      blocks: name the structure, find the source (paper / deck / book),
      record the value deltas. That is the S01-S18 table in the skeleton
      ledger.

   5. EXTRACT THE MUTATION LEVERS from the deltas. When a question repeats
      with one thing changed, that thing IS the setter's lever: value swap
      (M0), ask inverted (M1), condition added (M2), target changed (M3),
      two shapes joined (M4).
```

WHY 34 SHAPES AND NOT FEWER (why precision was not the goal):

```
   a smaller shape set (say, "the 8 families") misses ask-type entirely:
      "Normal/find-param" and "Normal/tail" are the same family but need
      different methods (solve two equations vs read a table).
   a larger set (every individual question) overfits: two questions with
      the same shape would count as different, and coverage % becomes
      meaningless.
   34 is the level at which the METHOD changes. that is the right unit.
```

═══════════════════════════════════════════════════════════════════════════════
6. HOW THE WORKED SOLUTIONS WERE BUILT (the quality process)
═══════════════════════════════════════════════════════════════════════════════

Every file in deck/worked/ was produced under the same five gates:

```
   GATE 1: SOURCE. The question is quoted from the on-disk source, with the
           source named in the header line.

   GATE 2: MACHINE-CHECKED NUMBERS. Every number in every solution was
           computed in python BEFORE being written. Hand-guessed values were
           wrong often enough to be discarded as a method (examples caught:
           p(5) on the flashlight, F=9.17 vs a hand guess of 27.97, chi2
           3.6458 vs a hand guess of 7.5).

   GATE 3: ZERO-KNOWLEDGE REGISTER. Every step shown, every symbol decoded,
           no assumed maths. "the long explain-from-nothing answers" (user
           directive).

   GATE 4: SCANS. No em dashes, no banned AI-tell words, no leftover
           thinking text. Checked mechanically at commit time.

   GATE 5: COMMIT ONLY WHEN GREEN. Each file committed with its check count
           in the commit message. The full ledger is at the bottom of
           00-INDEX.md.
```

═══════════════════════════════════════════════════════════════════════════════
7. WHAT THE COVERAGE CLAIM ACTUALLY IS (and its limits)
═══════════════════════════════════════════════════════════════════════════════

The claim, stated precisely so it cannot be over-read:

```
   CLAIMED:  every one of the 16 MTE paper blocks (2 papers x 8 blocks) has
             at least one worked question at its shape. verified by a
             fingerprint audit (each block's key numbers/phrases searched
             across the F-files).
   CLAIMED:  36/36 shape probes pass (the 34 checklist shapes + 2 extras).
   CLAIMED:  every worked number machine-checked before commit.

   NOT CLAIMED: that these are the ONLY questions that can come. the paper
                can always surprise with a new mutation.
   NOT CLAIMED: that the 158 is exhaustive of the corpus. it is capped by
                the 2-3-per-shape rule; the corpus itself is bigger (the
                instance ledger counts 383+ gross instances).
   NOT CLAIMED: that doing these guarantees any mark. coverage is not
                execution (see the probability analysis delivered in chat).
```

═══════════════════════════════════════════════════════════════════════════════
8. THE ONE-PAGE ANSWER (if you only remember one screen)
═══════════════════════════════════════════════════════════════════════════════

```
   WHERE:   ~/mas2001-mte-s2/deck/worked/    (F1-F15 + drill + index)
            the drill file: 00-QUESTIONS-ONLY.md (168 entries)

   HOW:     every question traced to a source file; every number computed in
            python first; zero-knowledge steps; scans; commit messages carry
            the check counts.

   WHY ONLY THOSE: 2-3 per shape (user cap), in-scope per ~/PS/syllabus.txt,
            own-papers-first ordering, nothing invented.

   SHAPES/SKELETONS: 12 families -> 34 (family,ask) shapes -> skeletons in
            the S01-S28 ledger -> mutation levers M0-M4. documented in
            reports/20-SKELETON-LEDGER.md, deck/15-DECISION-MANUAL.md,
            reports/11-QUESTION-ATLAS/00-MUTATION-ANALYSIS.md.
```
