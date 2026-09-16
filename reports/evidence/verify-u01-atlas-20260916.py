#!/usr/bin/env python3
"""Recompute U01 atlas counts and numeric answers with the standard library."""

import math
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
ATLAS = ROOT / "reports/11-QUESTION-ATLAS/02-u01-mte-papers.md"


def close(name, got, want, tolerance=5e-7):
    assert abs(got - want) <= tolerance, "%s: got %r want %r" % (name, got, want)
    print("PASS", name, "%.9f" % got)


text = ATLAS.read_text(encoding="utf-8")
ids = re.findall(r"^## (M(?:24|25)-Q[^,]+)", text, re.MULTILINE)
assert len(ids) == 16
assert len(set(ids)) == 16
print("PASS atlas IDs", len(ids), "unique")

fields = (
    "source:", "question:", "what it is / type / subtype:",
    "knowledge / approach / steps:", "alternate:", "intent:",
    "bloom / dok / math_group / solo / gaise:", "difficulty / task demand:",
    "traps:", "exam_use / verdict:", "verified:",
)
for field in fields:
    assert text.count("**" + field + "**") == 16, field
print("PASS schema fields", len(fields), "x 16")

close("M25 Q6 P(T>1)", math.exp(-1 / 3), 0.716531311)
close("M25 Q6 P(T<3)", 1 - math.exp(-1), 0.632120559)
close("M25 Q8 part ii p", -math.log(0.9) / 4000, 0.0000263401, 5e-11)
close("M24 QB2 P(T>6)", math.exp(-1.5), 0.223130160)
close("M24 QB2 P(7<T<12)", math.exp(-1.75) - math.exp(-3), 0.123986875)
close("M24 QB2 P(T<=5)", 1 - math.exp(-1.25), 0.713495203)

p = 0.2084
week = sum(math.comb(7, k) * p**k * (1 - p) ** (7 - k) for k in range(3))
close("M24 QC1 P(K<=2)", week, 0.837219240)
close("M24 QC1 binomial P(X>=1)", 1 - (2 / 3) ** 5, 211 / 243)
close("M24 QC1 binomial P(X<=1)", (2 / 3) ** 5 + 5 * (1 / 3) * (2 / 3) ** 4, 112 / 243)

print("ALL U01 ATLAS CHECKS PASS")
