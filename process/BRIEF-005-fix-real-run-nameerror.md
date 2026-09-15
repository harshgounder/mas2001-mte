# BRIEF 005: fix the real-run NameError in convert.py main() (one function, one line class)

Owner: Hermes (architect, auditor). Implementer: opencode CLI. Repo: /home/liebert511/mas2001-mte

Round 8. A real conversion run crashed on its first use. The cause is a variable that is only
assigned in the dry-run branch and after the processing loop, but read INSIDE the loop. This
is a regression introduced by round 7 (BRIEF-004), and the round-7 harness could not see it
because its only test that calls `main([])` uses a source that gets SKIPPED, so the loop body
never executes.

## THE HARD RULES (same as BRIEF-004)

```
  1  Do NOT git commit and do NOT git push. Hermes audits and commits.
  2  Modify ONLY scripts/convert.py. Nothing else. If you find a defect elsewhere, report it
     with file and line, do not fix it.
  3  No em dashes, no en dashes, anywhere, including comments.
  4  No AI-tell vocabulary. Plain words.
  5  stdlib only, no installs, no network. python3 is /usr/bin/python3 (3.14.7).
  6  Small provable change. Do not restructure main().
```

## THE DEFECT, exactly as it is on disk

File `scripts/convert.py`, in `main()`. Read these lines yourself before editing:

```python
    if args.dry_run:                                  # line 530
        ...
        latest = read_manifest_latest()               # line 536   <- assigned HERE
        ...

    started_wall = time.monotonic()                   # line 553
    rows = []
    for src in runnable:                              # line 555
        ...
        pending = [
            page
            for page in pages
            if args.force or not page_done(label, page, latest, OUT)   # line 562  <- READ HERE
        ]
```

`latest` is a local of `main()`. It is assigned at line 536 (inside the `if args.dry_run:`
branch) and again at line 593 (after the processing loop, for the per-label summary). On a
real (non-dry) run the loop at 555 executes before either assignment, so line 562 raises
`UnboundLocalError: cannot access local variable 'latest'`.

Reproduced for you, verbatim, by Hermes before writing this brief:

```
  python3 scripts/convert.py --label paper-mte-2025-26 ...
  Traceback (most recent call last):
    File "scripts/convert.py", line 615, in <module>
      sys.exit(main(sys.argv[1:]))
    File "scripts/convert.py", line 562, in main
      if args.force or not page_done(label, page, latest, OUT)
  UnboundLocalError: cannot access local variable 'latest' where it is not associated with a value
```

## THE FIX, in the shape Hermes wants it (you may improve it, see below)

Hoist one assignment so the loop and everything after it share a single manifest read:

```
  a  Read the manifest ONCE, before the `if args.dry_run:` branch, so both the dry-run
     path and the real-run path use the same snapshot:
         latest = read_manifest_latest()
  b  Delete the now-redundant assignment at line 536 (inside the dry-run branch) so the
     read happens once per run, not twice.
  c  The assignment at line 593 (after the loop) exists to pick up records the loop just
     appended. Decide and DOCUMENT which behaviour you keep:
       option 1 (recommended): keep 593 as a re-read, so the per-label summary reflects
         rows written by this run. One extra read per label, correct, and it is what the
         line was clearly for.
       option 2: drop it and pass the pre-loop snapshot. Cheaper, but then the summary
         cannot see this run's own writes. If you choose this, say so and say why.
     Either is acceptable. What is NOT acceptable: leaving a code path where `latest` can
     be read before assignment. If you would rather initialise it to {} at the top and
     keep both reads, that is also fine as long as there is no unbound path and you
     explain the choice.
```

Do not add a `try/except` around it. Do not use `global`. Do not rename the variable.

## VERIFICATION (all of it, report every result)

```
  V1  The new regression test, which Hermes already wrote and which FAILS today:
        cd ~/mas2001-mte; python3 -B tests/test_pipeline_audit.py -v
      Before your fix: ERROR, test_real_run_with_pending_page_does_not_crash.
      After your fix:  it must PASS and the run must be 29 tests, OK.
      It is in class RealRunSkipChecks, named test_real_run_with_pending_page_does_not_crash.
      Do NOT edit the test. If you believe it is wrong, say so and stop.

  V2  The full suite must be green:
        python3 -B tests/test_pipeline_audit.py
      expect: Ran 29 tests, OK. Report the exact final lines.

  V3  The real-world repro, run for real (this is the actual U01 job, 15 pages):
        cd ~/mas2001-mte; python3 scripts/convert.py --label paper-mte-2025-26 \
          --label paper-mte-2025-26-scheme --label paper-mte-2024-25 \
          --label paper-mte-2024-25-scheme
      expect: no traceback, 15 pages processed (the vision CLI is slow, a few minutes is
      normal), then a summary table and a nonzero count only if pages genuinely failed.
      Report the final table verbatim. If the vision CLI errors out (network, quota), say
      so plainly, do not fabricate a table.

  V4  Dry-run must still behave:
        python3 scripts/convert.py --dry-run
      expect: exit 0, "dry run: 298 pending page(s)" (all the 15 U01 pages plus the 283
      others that are still unconverted; the number is read from your run output).
        python3 scripts/convert.py --dry-run --label does-not-exist
      expect: nonzero exit, "unknown label(s): does-not-exist".

  V5  Dash and vocabulary check on the file you touched:
        python3 - <<'EOF'
        import pathlib
        t = pathlib.Path("scripts/convert.py").read_text(encoding="utf-8")
        print({n: t.count(c) for c, n in {"\u2014": "em", "\u2013": "en"}.items() if c in t} or "clean")
        EOF
      expect: clean

  V6  git status --short in ~/mas2001-mte
      expect: scripts/convert.py modified, plus whatever V3 legitimately produced under
      md/ and work/ (the U01 pages, the manifest rows, the summary). Report it verbatim.
      Do NOT stage or commit. Do NOT touch work/opencode/.
```

## REPORT BACK (in this order)

```
  1  V1 before/after: the exact unittest line before the fix and after.
  2  V2's exact final line and test count.
  3  The change you made, as a unified diff, plus one sentence on which option you took
     for the post-loop read and why.
  4  V3's final table verbatim, or the honest failure.
  5  V4's two exit codes and lines.
  6  V5's output and V6's exact git status.
  7  Anything in this brief that does not match what you find on disk. Do not follow a
     wrong line reference into a wrong edit; report it instead.
```

Do NOT commit. Do NOT push. Stop after the report.
