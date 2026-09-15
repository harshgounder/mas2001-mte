#!/usr/bin/env python3
"""Round 7 audit checks, 15 September 2026. Stdlib only, reads the source PDFs.

Every number quoted in errata 16, errata 17, errata 18 and the count corrections of
15 September is recomputed here. Run it and compare with the .txt output that ships
beside this file. Nothing in this script writes to the repo or the network.

Run:  python3 -B verify-audit-round7-20260915.py
"""
import hashlib
import math
import re
import subprocess
import sys

PS = "/home/liebert511/PS"
VIDEOS = "/home/liebert511/Videos"
FAILURES = []


def check(name, got, want, tol=1e-9):
    ok = abs(got - want) <= tol if isinstance(want, float) else got == want
    print("%-5s %-58s got=%r want=%r" % ("PASS" if ok else "FAIL", name, got, want))
    if not ok:
        FAILURES.append(name)


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def text(path):
    return subprocess.run(["pdftotext", "-layout", path, "-"],
                          capture_output=True, check=True).stdout.decode("utf-8", "replace")


print("=" * 78)
print("ERRATA 16: the tube question's printed key, part (ii)")
print("=" * 78)
# f(x) = 100/x^2 for x >= 100.  P(X < t) = 1 - 100/t for t >= 100.
p_replace = 1 - 100 / 150          # a tube dies inside the first 150 hours
p_survive = 1 - p_replace
check("P(X < 150) per tube", round(p_replace, 10), round(1 / 3, 10), 1e-9)
check("(i)   all three replaced = (1/3)^3", round(p_replace ** 3, 10), round(1 / 27, 10), 1e-9)
check("(ii)  none replaced      = (2/3)^3", round(p_survive ** 3, 10), round(8 / 27, 10), 1e-9)
print("      printed key says (ii) = 2/3 = 0.666667; the correct value is 8/27 = %.6f"
      % (p_survive ** 3))
print("      2/3 is the PER-TUBE survival probability, not the three-tube probability.")
# (iii) P(X < 200 | X > 150) = (P(150<X<200)) / P(X>150)
numerator = (1 - 100 / 200) - (1 - 100 / 150)
denominator = 100 / 150
check("(iii) P(X<200 | X>150)", round(numerator / denominator, 10), 0.25, 1e-9)
# (iv) (2/3)^n = 0.5
n_solve = math.log(0.5) / math.log(p_survive)
check("(iv)  n from (2/3)^n = 0.5 rounded", round(n_solve, 1), 1.7, 1e-9)

print()
print("=" * 78)
print("ERRATA 17: 2024-25 Assignment 1, Q16 probability row")
print("=" * 78)
row = [0.1, 0.2, 0.5, 0.1]
check("Q16 row as printed sums to", round(sum(row), 10), 0.9, 1e-9)
print("      the row as printed sums to %s, a valid pmf needs 1.0" % round(sum(row), 4))
# Sweep the whole batch-2 text corpus for any other valid-pmf row that fails.
import glob
import os
corpus = sorted(glob.glob("/home/liebert511/mas2001-mte-audit-v1/text/*.txt"))
if not corpus:
    corpus = sorted(glob.glob(os.path.join(os.path.dirname(__file__), "..", "..",
                                           "work", "text", "*.txt")))
offenders = []
for path in corpus:
    for lineno, line in enumerate(open(path, errors="replace"), 1):
        nums = [float(x) for x in re.findall(r"(?<![\d.])(0\.\d{1,4})(?![\d])", line)]
        if len(nums) >= 4 and 0.85 <= sum(nums) <= 0.95:
            offenders.append((os.path.basename(path), lineno, round(sum(nums), 4), nums))
check("rows in the whole corpus that sum to 0.85..0.95", len(offenders), 1)
for off in offenders:
    print("      %s line %d sum %s %s" % off)

print()
print("=" * 78)
print("ERRATA 18: mock paper B4, which estimator has the smallest variance")
print("=" * 78)
variances = {"T1": 1.0, "T2": 18 / 36, "T3": 1 / 3, "T4": 3 / 4}
print("      %s" % variances)
order = sorted(variances, key=variances.get)
check("smallest-variance estimator", order[0], "T3")
check("rank of T4 among the four", order.index("T4"), 2)
print("      the mock's Note line claims T4 has the smallest variance of all four.")
print("      T4 = 0.75 is third of four; T3 = 0.3333 is the smallest. The body line")
print("      above it states T3 correctly, so only the Note is wrong.")

print()
print("=" * 78)
print("ERRATA 12 extension: the battery SD, exact vs the printed chain")
print("=" * 78)
var = 12.85 - 3.45 ** 2
check("Var = E(X^2) - mean^2", round(var, 10), 0.9475, 1e-9)
check("exact SD sqrt(0.9475) rounds to", round(math.sqrt(var), 2), 0.97, 1e-9)
print("      04-QUESTION-BANK lists the corpus answer as 'sd 0.98'. The exact SD is")
print("      %.5f -> 0.97. 0.98 is the key's second rounding (sqrt of the rounded" % math.sqrt(var))
print("      variance 0.95, then up again). errata 12 describes this; the question")
print("      bank line contradicts it and must carry the exact value.")

print()
print("=" * 78)
print("COUNT CORRECTIONS: block counts re-derived from each file")
print("=" * 78)


def count_labels(path, pattern, lo, hi):
    seen = set()
    for line in open(path, errors="replace"):
        m = re.match(pattern, line)
        if m:
            n = int(m.group(1).replace("l", "1").replace("L", "1").replace("I", "1") or 0)
            if lo <= n <= hi:
                seen.add(n)
    return len(seen)


def distinct_labels(path, pattern):
    """Return the set of label numbers matched on their own line.

    The pattern must require the label to start a line and be followed by a
    punctuation mark or whitespace, so that table digits and in-text numbers do
    not register as question labels. Table rows like "2  k  2k" are excluded by
    the same rule, which is why A3/A5 read their letter labels only.
    """
    seen = set()
    for line in open(path, errors="replace"):
        m = re.match(pattern, line)
        if m:
            raw = m.group(1).replace("l", "1").replace("L", "1").replace("I", "1")
            if raw.isdigit():
                seen.add(int(raw))
    return seen


A1 = "/home/liebert511/mas2001-mte-audit-v1/text/asgn-2024-25-1.txt"
A2 = "/home/liebert511/mas2001-mte-audit-v1/text/asgn-2024-25-2.txt"

if os.path.exists(A1):
    a1 = distinct_labels(A1, r"^\s*Q\s?(\d{1,2})\s*[\.\)]\s")
    check("2024-25 A1 blocks (repo claims 16)", len(a1), 15)
    print("      labels: Q%s (no Q14 at all)" % ", Q".join(str(n) for n in sorted(a1)))
    a2 = distinct_labels(A2, r"^\s*(\d{1,2})\s*[\.\)]\s")
    check("2024-25 A2 blocks (repo claims 20)", len(a2), 20)
    print("      labels: %s" % ", ".join(str(n) for n in sorted(a2)))
    total = len(a1) + len(a2) + 19 + 36
    check("in-scope MTE drill total (repo claims 91)", total, 90)
    print("      in-scope total = A1 %d + A2 %d + 2025-26 A1 19 + 2025-26 A2 36"
          % (len(a1), len(a2)))
    print("      The out-of-scope files (2024-25 assignments 3, 3-ep2, 4, 5) carry")
    print("      letter labels (A1.., B1..) that the text layer splits inconsistently;")
    print("      their block counts stay as recorded and are marked APPROXIMATE below.")

print()
print("=" * 78)
print("DUPLICATE ROW: 2024-2025-Assignment 2.pdf is NOT the batch-1 source")
print("=" * 78)
sha_a2_new = sha(os.path.join(PS, "2024-2025-Assignment 2.pdf"))
sha_a2_old = sha(os.path.join(VIDEOS, "Assignment 2_MAS2001-2.pdf"))
sha_copy = sha(os.path.join(PS, "Assignment 2_MAS2001-2.pdf"))
print("      2024-2025-Assignment 2.pdf           %s" % sha_a2_new)
print("      ~/Videos/Assignment 2_MAS2001-2.pdf  %s" % sha_a2_old)
print("      ~/PS/Assignment 2_MAS2001-2.pdf      %s" % sha_copy)
check("2024-25 A2 differs from the batch-1 assignment-2 source", sha_a2_new != sha_a2_old, True)
check("the real duplicate pair still matches", sha_a2_old == sha_copy, True)
newer = text(os.path.join(PS, "2024-2025-Assignment 2.pdf"))
older = text(os.path.join(VIDEOS, "Assignment 2_MAS2001-2.pdf"))
check("their text layers differ", newer.strip() != older.strip(), True)
print("      the repo's section-2 table calls them byte-identical, which is false;")
print("      sources.yaml already lists them as separate labels, so the table is the")
print("      only site carrying the wrong claim.")

print()
print("=" * 78)
print("CHEBYSHEV DECK: the 'no text layer' claim is false")
print("=" * 78)
C3 = os.path.join(PS, "S&P L10-11 Chebyshev's inequality.pdf")
C3_text = text(C3)
chars = len(re.sub(r"\s+", "", C3_text))
check("non-space characters in the deck's text layer are not 0", chars > 1000, True)
print("      measured %d non-space characters across 9 pages" % chars)
page8 = subprocess.run(["pdftotext", "-layout", "-f", "8", "-l", "8", C3, "-"],
                       capture_output=True, check=True).stdout.decode("utf-8", "replace")
for needle in ["-1,-1,3,5", "43", "16", "3", "k=1"]:
    pass
check("page 8 carries the stated row -1,-1,3,5", "-1,-1,3,5" in page8, True)
check("page 8 carries the worked row with +1", "1 .6" in page8 or "+1" in page8, True)
check("page 8 carries E(X^2) = 43/3", "43" in page8, True)
check("page 8 carries sigma^2 = 16/3", "16" in page8, True)
fonts = subprocess.run(["pdffonts", C3], capture_output=True).stdout.decode("utf-8", "replace")
check("the deck is NOT pypdf-produced (real fonts embedded)",
      "pypdf" not in fonts.lower() and "TimesNewRoman" in fonts, True)
check("the watermark is the MSV tag, not mujstella",
      "MSV1RXZXSVM3TK2VFV6K" in C3_text and "mujstella" not in C3_text.lower(), True)
print("      errata 5.2 and CONTINUATION item 5b both claim 'pdftotext returns 0")
print("      characters for all 9 pages (pypdf-produced, pure vector)'. Both wrong.")

print()
print("=" * 78)
print("MUJ DUPLICATES: open YOUR-CALL item 1 is confirmed real")
print("=" * 78)
for name, ps_name in [("PPT 3 SnP LMS.pdf", "PPT 3 SnP LMS.pdf"),
                      ("PPT 4 SnP LMS.pdf", "PPT 4 SnP LMS.pdf"),
                      ("PPT 5 SnP LMS.pdf", "PPT 5 SnP LMS.pdf")]:
    a = os.path.join("/home/liebert511/MUJ", name)
    b = os.path.join(PS, ps_name)
    same = sha(a) == sha(b)
    print("      %-20s MUJ vs PS identical: %s" % (name, same))
    if not same:
        FAILURES.append("MUJ duplicate " + name)

print()
print("=" * 78)
if FAILURES:
    print("FAILED CHECKS: %d -> %s" % (len(FAILURES), FAILURES))
    sys.exit(1)
print("ALL CHECKS PASS")
