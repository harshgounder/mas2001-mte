# BRIEF 004: pipeline hardening (the six confirmed gaps and the two vision defaults)

Owner: Hermes (architect, auditor). Implementer: opencode CLI. Repo: /home/liebert511/mas2001-mte

Round 7 of the audit found six real defects in the conversion pipeline and two stale model
defaults. Five of the six defects were found by an independent peer harness written by a
different agent (codex CLI, 15 Sep) and copied into this repo as `tests/test_pipeline_audit.py`
(pristine reference kept outside the repo, assertions unchanged). I reproduced every one of
them myself by reading the code, so the line references below are mine, not the harness's
word. The harness is the acceptance instrument.

Everything here is standard library only. Nothing in this brief adds a dependency, makes a
network call outside the existing `~/.local/bin/vision` shell-out, or touches any file under
`md/`, `work/text/`, or `reports/`.

## THE HARD RULES FOR THIS ROUND

```
  1  Do NOT git commit and do NOT git push. Hermes audits the diff and commits.
  2  Modify ONLY these four files:
       scripts/convert.py
       scripts/audit_conversion.py
       tests/test_pipeline_audit.py                    (the working copy of the peer harness, see rule 8)
       process/BRIEF-004-pipeline-hardening.md         (this file, only if you must annotate)
     Any other file is out of bounds. If you find a real defect elsewhere, do NOT fix it.
     Record it in your report as a numbered finding with the file and line, and leave it.
  3  No em dashes and no en dashes anywhere, including comments and docstrings. The repo
     enforces this at assembly. Use a colon, a comma, or a hyphen.
  4  No AI-tell vocabulary (delve, leverage, robust, seamless, comprehensive, and the rest
     of the standing list). Plain words.
  5  python3 is /usr/bin/python3 (3.14.7). Standard library only. Do NOT install anything.
     There is no pytest in this environment and you must not add one: the verification
     harness is plain `unittest`, run as `python3 -B test_audit.py -v`.
  6  Another process (Hermes) may read the tree while you work. Report any file you did not
     change yourself.
  7  This is a study repo mid-exam-prep. Prefer a small, provably correct change over a
     redesign. Every behaviour change below has a test that must go from FAIL to PASS.
  8  A NOTE ON TEST OWNERSHIP, stated plainly so there is no ambiguity: the harness at
     `tests/test_pipeline_audit.py` is a working copy of an independent specification
     written by codex CLI; its pristine reference lives outside the repo at
     `~/mas2001-mte-audit-v1/test_audit.py` and Hermes keeps its assertions unchanged as an
     audit gate. The copy currently has 12 tests and 6 FAIL. Those six failures ARE the
     specification for this round. You are asked to STRENGTHEN the copy (add tests, tighten
     assertions), never to weaken one. A test that is edited to pass instead of the code
     being fixed is the single worst outcome of this round, and the audit will catch it by
     running the pristine reference's assertions unchanged. Do not touch the audit-v1
     directory; the sandbox blocks it anyway.
```

## VERIFIED STARTING STATE (I measured these this turn, do not re-derive unless you doubt them)

```
  repo            HEAD 0c641b7 == origin/master, 437 tracked, 3 untracked paths
                  (the brief, tests/, work/opencode/)
  run this first  python3 -B tests/test_pipeline_audit.py -v      (from the repo root)
                  current result: Ran 12 tests, FAILED (failures=6)
  corpus          348 converted pages; work/manifest.jsonl holds 355 rows, 348 unique pages;
                  the LATEST record for every one of the 348 pages has status "ok"
                  (355 rows because 7 pages were re-run at some point)
  ~/PS            34 files. sources.yaml declares 36 sources over 646 pages.
```

That manifest reading matters for G1: it tells you a stricter `is_done` will NOT send the
next run back over the 348 already-good pages. Keep it that way.

## THE DEFECTS

### G1: a truncated page is marked done forever (convert.py)

The resume gate is:

```python
  def is_done(md_path):                       # convert.py line 319
      return md_path.is_file() and md_path.stat().st_size > 0
```

`process_page` (line 326) uses `is_done(md_path)`, and `main`'s pending list (line 522) uses
the same function. So a page whose markdown is a title line and nothing else is treated as
finished for every future run. `transcribe` already distinguishes `"truncated"` and
`"error"` (lines 263, 267, 271, 277), and `make_record` writes that status into the manifest,
but nothing reads it back on the resume path.

Required:

```
  a  A page is done only when its LATEST manifest record has status "ok" AND the markdown
     file is non-empty. Build the latest-record map once per run from work/manifest.jsonl
     (the file is append-only, so the LAST row for a (label, page) pair wins), in the same
     spirit as the existing manifest handling at line 292.
  b  A missing manifest record counts as NOT done, so an unrecorded page is retried rather
     than assumed good.
  c  A manifest row whose status is "truncated" or "error" counts as NOT done.
  d  Do not rewrite the 348 "ok" rows and do not delete anything from the manifest. It is
     an append-only provenance log; a retry appends a new row.
  e  With the current corpus, `python3 scripts/convert.py --dry-run` must still report
     0 pending pages. That is the regression guard: if your change makes the existing
     348-page corpus look unfinished, the change is wrong. State the measured number in
     your report.
```

### G2: a nonzero vision exit is recorded as success (convert.py)

In `transcribe` (line 232), the retry loop breaks as soon as `out` is non-empty:

```python
        if out:
            ...
            text = out
            status = "truncated" if TRUNCATED_MARKER in err else "ok"      # line 271
            break
```

`call_vision` returns `(proc.returncode, stdout, stderr)` (line 229). Nothing consults
`returncode` on that branch, so a shell-out that exits nonzero while still printing something
(a provider error body on stdout, an HTTP 402 message, a partial answer before a crash) is
recorded as `"ok"`. The existing `~/.local/bin/vision` prints its own failures to stderr and
exits nonzero, so this is reachable.

Required: a nonzero `returncode` with non-empty `out` must NOT be recorded as `"ok"`. Decide
and document which of these you do, and why:

```
  a  treat it as a retryable failure (same path as an empty read), OR
  b  keep the text but record a distinct non-ok status (for example "exit_<code>") so the
     page is retried under G1 and the evidence is not lost.
```

Either is acceptable. Silently calling it `"ok"` is not. Whatever you choose must be visible
in the manifest and must make the page eligible for a retry.

### G3: an empty or missing second reading scores a perfect agreement (audit_conversion.py)

```python
  def numeric_agreement(primary, second):                        # line 378
      primary_counts = Counter(numeric_tokens(primary))
      second_counts = Counter(numeric_tokens(second))
      total = sum(primary_counts.values())
      if total == 0:
          return 1.0                                             # line 383
      ...
```

Two separate holes:

```
  a  an EMPTY second reading: numeric_tokens("") is [], every token count is 0, so
     matched stays 0, but total is the PRIMARY's count, so the ratio is 0.0 only when the
     primary has numbers. If the primary is text without numbers, total = 0 and it returns
     1.0. Either way the function has no way to say "the second reader produced nothing".
     Verify the real behaviour with the two concrete inputs in the harness
     (test_empty_second_reading_cannot_pass, test_fidelity_detects_sign_reversal) before
     you change anything, and say in your report what they actually returned.
  b  the caller decides PASS at `agreement >= 0.8` (line 466) without checking that the
     second reading exists at all. A blank second reading that scores 1.0 therefore PASSES.
```

Required:

```
  c  An empty or whitespace-only second reading must never reach PASS. It must produce
     verdict REVIEW (or a distinct verdict such as NO_SECOND_READING) with a recorded
     reason string, so the FIDELITY.md row says why.
  d  The "nothing to compare" case must be its own outcome, not an agreement of 1.0. If the
     primary genuinely holds zero numeric tokens, say so (for example agreement None with
     reason "primary has no numeric tokens") rather than reporting perfect agreement.
  e  numeric_agreement must compare SIGNED numbers. `numeric_tokens` uses
     NUM_RE = re.compile(r"\d[\d,]*(?:\.\d+)?") (line 41), which cannot see a leading minus,
     so "Mean = -3" and "Mean = +3" tokenize identically and score 1.0. A sign flip is
     exactly the kind of transcription error this gate exists to catch. Detect a preceding
     "-" or an explicit "+" (watch for a hyphen used as a dash, and for a minus that is
     really a subscript separator) and include the sign in the token. Say in your report
     how you distinguished a sign from a dash, with the inputs you tested.
     CAUTION: this tightens a gate. Run the real fidelity path afterwards (see the
     acceptance section) and report whether any previously PASSing page flips to REVIEW.
     If one does, report it as a finding rather than tuning the threshold downward.
```

### G4: the fidelity cache survives a model change (audit_conversion.py)

```python
        if second_path.is_file():                                  # line 454
            second = read_text(second_path)
        else:
            second = call_vision(png_path, prompt, args.fidelity_model, config["max_tokens"])
            if second:
                write_text_atomic(second_path, second + "\n")
```

`second_path` is `FIDELITY_ROOT / label / pNNN.md` (line 452). The reading is cached with no
record of which model produced it, so re-running with a different `--fidelity-model` reuses
the old model's reading and reports agreement as though the new model had read the page. The
repo has a live example of why this matters: `work/FIDELITY-void-pro-404.md` exists because a
first fidelity attempt used a dead model, and the docs go out of their way to say its number
must never be cited.

Required: the cached second reading must be tied to the model that produced it.

```
  a  Recommended: a sidecar stamp per label, for example
     work/fidelity/<label>/_model.json holding {"model": "<id>", "written": "<utc iso>"},
     written atomically with the first page cached for that label. On a run, if the stamp
     is absent or names a different model, IGNORE the cache and re-read every page for that
     label (do not delete the old files: overwrite them, and keep the old stamp under a
     suffixed name if you want a record).
  b  A different shape is acceptable if it is simpler and equally provable, for example a
     stamp per page. What is not acceptable: reusing a reading whose provenance is unknown.
  c  The old cache from the codex model may be present under work/fidelity/. Leave the
     existing files in place; a model change should cause them to be re-read and overwritten,
     not deleted by hand.
```

### G5: --dry-run returns 0 when a source is skipped (convert.py)

In `main` (the skip loop at lines 488-494; 488 is `runnable = []` and 490 is the
`verify_source(src)` call), sources failing `verify_source` (line 173, which returns a reason
string for a relative path, a missing file, or a sha256 mismatch) are logged as SKIPPED and
dropped from `runnable`. The dry-run branch then prints the pending table and returns 0
(line 511). So a corpus with a missing or corrupted source reports a clean dry run.

Note the interaction this creates, which is the actual bug: a source that fails verification
is silently converted into "no pages pending", which is indistinguishable from "everything is
up to date".

Required:

```
  a  In dry-run mode, a skipped source must make the command exit NONZERO and must name the
     label and the reason in the output. Do not print a reassuring pending table for it.
  b  Decide and document the behaviour in a real (non-dry) run. My recommendation: a skipped
     source exits nonzero at the END of the run, after the runnable sources have been
     processed, with the skip reasons listed, so a partial corpus is never reported as a
     clean success. Your call, but state it.
  c  The existing test test_failed_source_makes_dry_run_fail patches load_config to return
     one source whose path does not exist and asserts main(["--dry-run"]) != 0. Make that
     the contract.
```

### G6: the two vision model defaults contradict the standing directive

The user's directive of 15 Sep is: use glm-5.3-flash for vision. `~/.local/bin/vision`
already defaults to it on the ollama-cloud path, and I verified it live on a slide page the
same day. The two scripts pin the old model and would silently override the CLI default:

```
  scripts/convert.py            line 25   DEFAULT_MODEL = "xiaomi/mimo-v2.5"
  scripts/audit_conversion.py   line 34   DEFAULT_FIDELITY_MODEL = "xiaomi/mimo-v2.5-pro"
```

Required:

```
  a  convert.py               DEFAULT_MODEL = "glm-5.3-flash"
  b  audit_conversion.py      DEFAULT_FIDELITY_MODEL = "glm-5.3-flash"
  c  Leave the --model and --fidelity-model flags exactly as they are: still overridable,
     same flag names, same help text shape. Only the default value changes.
  d  Add one short comment line beside each default recording WHEN it changed and why:
     "user directive 2026-09-15: glm-5.3-flash on ollama-cloud". Keep it to one line.
  e  Do NOT change README.md, CONTINUATION.md or any doc. Hermes owns the docs. If a doc
     now looks stale to you, report it, do not edit it.
```

## THE VERIFICATION HARNESS (strengthen it, do not weaken it)

`tests/test_pipeline_audit.py` is a plain `unittest` file with 12 tests (the working copy of
the peer harness; run it from the repo root).
today and those six failures ARE the specification for this round. For each defect above,
make the corresponding test pass, and add tests for the parts the existing harness does not
cover:

```
  G1  the existing test_truncated_page_is_not_permanently_done covers the truncated case.
      ADD a test for the manifest-driven rule: with a latest record of
      {"status": "truncated"} the page is pending; with {"status": "ok"} it is done; with no
      record at all it is pending. Use tmp paths, never the real corpus.
  G2  ADD a test asserting that a (returncode=1, stdout="HTTP 402: exhausted") pair does not
      yield status "ok", and that the recorded status is the one you chose in G2.
  G3  test_empty_second_reading_cannot_pass and test_fidelity_detects_sign_reversal already
      exist. ADD a test for the None/"no numeric tokens" outcome, and a test that a genuine
      agreement of 1.0 on two identical numeric readings STILL passes (do not break the
      happy path while tightening the gate).
  G4  test_fidelity_model_change_invalidates_cached_reading already exists. ADD the
      inverse: SAME model, cache present, call_vision must NOT be called (the cache is
      still useful, and a fix that disables caching entirely would be rejected).
  G5  the existing test_failed_source_makes_dry_run_fail covers dry-run. ADD the real-run
      contract you chose in G5b.
  G6  ADD a test that asserts convert.DEFAULT_MODEL == "glm-5.3-flash" and
      audit.DEFAULT_FIDELITY_MODEL == "glm-5.3-flash", so a future edit cannot silently
      revert them.
```

Constraints on the harness: stdlib only, no network, no writes to the study repo outside a
`tempfile.TemporaryDirectory`, and it must stay runnable as
`python3 -B tests/test_pipeline_audit.py -v` from the repo root. Keep the existing tests and
their assertions intact, including the ones that already pass.

## ACCEPTANCE (I run these myself, from the repo root unless stated)

```
  A1  cd ~/mas2001-mte; python3 -B tests/test_pipeline_audit.py -v
      expect: Ran <N> tests, OK, with N > 12 (the six failures fixed and the added tests
      present). Report N and the exact final line.
  A2  cd ~/mas2001-mte; python3 scripts/convert.py --dry-run
      expect: exit 0, "0 pending page(s)", and the 348-page corpus NOT reported as pending.
  A3  cd ~/mas2001-mte; python3 scripts/convert.py --dry-run --label does-not-exist
      expect: nonzero exit (existing behaviour, must not regress).
  A4  A real fidelity run over a couple of pages against the NEW default model, writing to
      the real work/fidelity/ cache:
        python3 scripts/audit_conversion.py --fidelity 2 --fidelity-model glm-5.3-flash
      expect: two pages read, a printed agreement and verdict per page, FIDELITY.md
      rewritten, and the model stamp present. Report the two agreement numbers and whether
      any page reads REVIEW. This one needs the network to reach the vision CLI, so if it
      fails for a connectivity or quota reason, say so plainly and report what the failure
      was: do not fabricate an agreement number.
  A5  cd ~/mas2001-mte; python3 - <<'EOF'
      import pathlib
      bad = {"\u2014": "em dash", "\u2013": "en dash"}
      targets = [pathlib.Path("scripts/convert.py"),
                 pathlib.Path("scripts/audit_conversion.py"),
                 pathlib.Path("tests/test_pipeline_audit.py")]
      for p in targets:
          t = p.read_text(encoding="utf-8", errors="replace")
          hits = {n: t.count(c) for c, n in bad.items() if c in t}
          print(p, hits if hits else "clean")
      EOF
      expect: every line reads "clean".
  A6  python3 -c "import sys; sys.path.insert(0,'scripts'); import convert, audit_conversion;
      print(convert.DEFAULT_MODEL, audit_conversion.DEFAULT_FIDELITY_MODEL)"
      expect: glm-5.3-flash glm-5.3-flash
  A7  git status --short   in ~/mas2001-mte
      expect: the two script files modified plus tests/test_pipeline_audit.py modified,
      nothing else. (tests/ and the brief are new untracked files; list whatever you see,
      verbatim. Do not stage anything.)
```

## REPORT BACK

Return, in this order:

```
  1  A1's exact final line and the test count.
  2  For each of G1 to G6: what you changed, in one or two lines, with file and line.
  3  A2 and A3's measured exit codes and output lines.
  4  A4's two agreement numbers and verdicts, or the honest failure reason.
  5  A7's exact git status output.
  6  Every place this brief was wrong, ambiguous, or impossible. Specifically: if any line
     number, function name, count or claimed behaviour above does not match what you find on
     disk, say so and do not follow the brief into it. I am the architect, not the compiler,
     and a brief that is confidently wrong is worse than an open question.
  7  Any defect you found in a file you were forbidden to touch, as a numbered finding with
     file, line, and evidence. Do not fix it.
```

Do NOT commit. Do NOT push. Stop after the report.
