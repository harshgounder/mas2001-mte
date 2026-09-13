# BRIEF 002: dash normalization and run robustness

Owner: Hermes. Implementer: opencode CLI. Repo: /home/liebert511/mas2001-mte

Two defects found in the audit of BRIEF-001 output. Fix both, change nothing else.

## Defect 1: em dashes reach the assembled documents

The repository has a hard rule: no em dash (U+2014) and no en dash (U+2013) in any
file, for any reason. The reader model emits them inside transcribed slide titles
(4 of the 11 pilot pages carried one).

PROMPT.txt has already been updated to forbid them at the source, but pages converted
before that change, and any page where the model ignores the rule, will still carry
them. So `assemble.py` must clean them on the way into the assembled document.

Required behaviour in `assemble.py`, in `assemble_label`:

- replace U+2014 and U+2013 with a plain hyphen before writing `md/<label>.md`
- count the replacements per label and add `dashes_fixed` to that label's entry in
  `md/INDEX.json` and to the console line
- leave `md/<label>/pNNN.md` untouched, those are the raw per-page transcription and
  stay verbatim

Also add the same check as a report to `convert.py`: after a run, count pages whose
markdown still contains U+2014 or U+2013 and print the count in the final summary
table as a `dashes` column next to `banned`. Do not rewrite page files.

## Defect 2: one raising page kills the whole run

In `convert.py`, `main` does `future.result()` inside the as_completed loop with no
guard. If any page raises outside the handled paths (a write error, a manifest error,
anything not caught inside `process_page`), the whole run dies and the remaining
futures in that label are abandoned.

Required behaviour:

- wrap the `future.result()` call so an unexpected exception is logged with the label
  and page, appended to the manifest as `status: "error"` with the exception text as
  the note, and the run continues
- keep the run resumable as it is today

## Acceptance (Hermes runs these)

```
python3 -c "import ast,sys; ast.parse(open('scripts/convert.py').read()); ast.parse(open('scripts/assemble.py').read())"
python3 scripts/convert.py --dry-run
python3 scripts/assemble.py
grep -c $'\u2014' md/lms-method-of-moments.md md/*.md
```
The grep must report zero for every assembled document. The per-page files may still
contain them.

Do not run a full conversion. Do not touch `sources.yaml`, `PROMPT.txt`, or anything
under `work/` or `md/`.
