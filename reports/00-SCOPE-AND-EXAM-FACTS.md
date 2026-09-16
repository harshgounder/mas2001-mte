# MAS2001 MTE: exam facts and scope

Every line here is traceable to a file on disk. Sources are listed at the bottom.

## 1. Dates

| item | date | source |
|---|---|---|
| Today | Sunday 13 September 2026 | session context |
| MTE window opens | Friday 18 September 2026 | MUJ academic calendar, "Start of MTE" |
| MTE window closes | Friday 25 September 2026 | MUJ academic calendar, "End of MTE" |
| Answer scripts shown | Wednesday 30 September 2026 | MUJ academic calendar |
| Re-sessional examination | 6 and 7 October 2026 | MUJ academic calendar |
| End term exam | course.json says 2026-11-18 | ~/muj-academics/courses/MAS2001/course.json |

The calendar publishes the MTE as a window, not a per subject slot. No file on disk
gives the subject-wise MTE date for MAS2001. Treat 18 to 25 September as the hard
boundary and expect the paper inside that window.

Study days available from today: 13, 14, 15, 16, 17 September. Five clear days before
the window opens. Classes continue on Mon, Wed, Fri (PS slots: Mon 2:00 pm AB1 327,
Wed 2:00 pm AB1 327, Fri 2:00 pm AB2 112).

## 2. Weight and format

From the official course handout, assessment plan:

| component | marks | notes |
|---|---|---|
| Mid-Term Examination | 30 | closed book |
| Class Work Sessional (CWS) | 30 | quiz, assignment |
| End Term Exam | 40 | closed book |
| total | 100 | |

MTE is 30 percent of the course grade.

## 3. MTE scope, from the official lecture plan

The handout lecture plan tags every lecture with the assessments that cover it. Lectures
tagged `MTE, CWS, ETE` are in scope for the mid-term. Lectures tagged `CWS, ETE` only
are in scope for the end term but not the mid-term.

IN SCOPE (lectures 1 to 21):

| lect | topic | CO |
|---|---|---|
| 1 | Introduction of the course | MAS2001.1 |
| 2 | Basic terminology and concepts of probability theory | MAS2001.1 |
| 3-4 | Random variables, discrete and continuous | MAS2001.1 |
| 5-6 | PMF, PDF, CDF | MAS2001.1 |
| 7 | Expectation of random variables | MAS2001.1 |
| 8-9 | Expectation, independent random variables | MAS2001.1 |
| 10-11 | Chebyshev's inequality | MAS2001.1 |
| 12 | Binomial distribution | MAS2001.2 |
| 13 | Poisson distribution | MAS2001.2 |
| 14 | Uniform distribution (continuous) | MAS2001.2 |
| 15 | Normal distribution | MAS2001.2 |
| 16 | Exponential distribution | MAS2001.2 |
| 17 | Sampling concepts: population, sample, standard error | MAS2001.3 |
| 18 | Central Limit Theorem | MAS2001.2 |
| 19 | Theory of estimation: parameter, statistic, point and interval estimation | MAS2001.3 |
| 20-21 | Characteristics of a good estimator | MAS2001.3 |

OUT OF SCOPE for the MTE (lecture 22 onward, tagged CWS and ETE only):

| lect | topic |
|---|---|
| 22 | Maximum likelihood estimation |
| 23 | Method of moments |
| 24 | Introduction to Bayesian estimation |
| 25, 27 | Confidence intervals for means |
| 28 | Confidence intervals, Student t |
| 29-30 | Hypothesis testing, level of significance, critical region, Type I and II errors |
| 31-32 | t-tests, one mean and two means |
| 33 | F-test |
| 34 | Chi-square test for independence of attributes |
| 35-36 | ANOVA one way |

This matches `~/PS/syllabus.txt` exactly, which is the MTE syllabus handed out in class
and stops at "Characteristics of a good estimator".

## 4. Source to scope mapping

| scope block | lectures | where the material lives | pages |
|---|---|---|---|
| probability theory, RVs, PMF/PDF/CDF, expectation | 2 to 9 | `notes-lecture-series-01-09` | 147 |
| Chebyshev's inequality | 10 to 11 | `sp-l10-11-chebyshev` | 9 |
| binomial and discrete distributions | 12 | `ppt3-discrete-prob-dist` | 28 |
| Poisson, uniform, normal, exponential | 13 to 16 | `ppt4-continuous-prob-dist` | 44 |
| sampling, standard error, CLT | 17 to 18 | `lms-standard-error-clt` | 19 |
| estimation intro, point and interval, good estimator | 19 to 21 | `ppt5-estimation-summary`, `lms-theory-of-estimation` | 26 + 40 |
| listed teaching-page inventory | | | 313, not deduplicated |
| end-term only, still converted | 22 to 23 | `lms-method-of-moments`, `lms-maximum-likelihood` | 11 + 16 |
| course facts, assessment scheme | | `mas2001-course-handout` | 7 |
| problem practice | | `mas2001-assignment-1`, `mas2001-assignment-2` | 6 + 4 |

Coverage warning worth stating plainly: lectures 2 to 11 exist in exactly one place on
disk, the 147 page Dr. Vivek Singh deck in `~/muj-academics/handouts`. The `~/PS` folder
does not contain them. Any revision that starts and ends inside `~/PS` will walk into the
paper having never opened units 1 and 2.

## 5. Course outcomes the MTE assesses

- MAS2001.1 Understand probability and random variables to analyse uncertainty problems. Target 85 percent of students at level 3.
- MAS2001.2 Apply probability distributions to model and analyse engineering problems. Target 70 percent at level 2.
- MAS2001.3 Describe point and interval estimators for parameter estimation. Target 70 percent at level 2.

Lectures 1 to 11 carry CO1, 12 to 18 carry CO2, 19 to 21 carry CO3. The paper therefore
leans on CO1 and CO2 by lecture count.

## 6. References on the handout

1. Goon, Gupta, Dasgupta, An Outline of Statistical Theory, Vol II, World Press, 2022.
2. Kendall and Stuart, The Advanced Theory of Statistics, Vol II, 1962.
3. Casella and Berger, Statistical Inference, 2nd ed, Thomson Duxbury, 2007.
4. Hogg, Tanis, Zimmerman, Probability and Statistical Inference, 9th ed, 2023.
5. Feller, An Introduction to Probability Theory and Its Applications, Vol I, 3rd ed, 2008.

Casella and Berger is the standard reference for lectures 19 to 21. Hogg is the
friendliest for lectures 2 to 16.

## Sources

- `~/muj-academics/courses/MAS2001/MAS2001_Course_Handout.pdf`, sha256 600361e9666d..., 7 pages
- `~/muj-academics/handouts/MUJ_Academic_Calendar_2026-27.md`
- `~/muj-academics/handouts/sem3_timetable_batch1.md`
- `~/muj-academics/courses/MAS2001/course.json`
- `~/PS/syllabus.txt`
- `~/muj-academics/handouts/Lecture notes MAS2001_SnP_1_9.pdf`, sha256 96e4e4053587..., 147 pages
