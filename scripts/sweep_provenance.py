#!/usr/bin/env python3
"""Wave A provenance sweep for the MAS2001 question instance ledger.

Two deterministic, offline passes:

  1. DESCRIPTION BACKFILL. A row whose summary is blank gets its real
     statement pulled from the source text, by block index. A backfill only
     happens when the source's block marker reproduces the DECLARED count for
     that source exactly. When it does not, the row is left blank and the
     mismatch is recorded, so we never fabricate a description from a
     misaligned file.

  2. PROVENANCE SWEEP. Every searchable row's text is scored against four
     reference corpora by distinctive 5-gram overlap. Verdict:
        verbatim / strong / family   evidence found (source named)
        open                         searched, no source
        unsearched                   no usable text to search
     A human-researched verdict is never overwritten (the 16 MTE rows and the
     30 four-deck rows are frozen).

    python3 scripts/sweep_provenance.py --check
    python3 scripts/sweep_provenance.py --write
"""
import argparse
import collections
import csv
import json
import os
import re
import sys

S2 = "/home/liebert511/mas2001-mte-s2/"
DEV = "/home/liebert511/mas2001-devore/"
AUD = "/home/liebert511/mas2001-mte-audit-v1/"

LEDGER = S2 + "reports/evidence/question-instance-ledger.csv"
REPORT = S2 + "reports/evidence/wave-a-sweep-20260916.json"

FROZEN_GROUPS = {"mte", "four-decks"}   # human-researched, never touched
FROZEN_IDS = {"cheb-Q1", "cheb-Q2"}     # report 20 has these; Q3 is errata-15

CORPORA = {
    "G&K-Fundamentals": DEV + "corpus-text/G-K-Fundamentals-Math-Stat.txt",
    "Hogg-Tanis-9e":    DEV + "corpus-text/Hogg-Tanis-9e.txt",
    "GGD-Vol1":         DEV + "corpus-text/GGD-Vol1-OCR-OCR.txt",
    "Davenport":        DEV + "corpus-text/Davenport-OCR.txt",
}

# marker candidates, tried in order; the first that reproduces the declared
# count exactly is used for backfill.
MARKERS = {
    "Qn":       r"^\s*Q\s*\d+\s*[.)]",
    "n_dot":    r"^\s*\d+\s*[.)]\s+\S",
    "Example":  r"^\s*Example\s*\d+",
    "sec_n":    r"^\s*[A-D]\s*\d+\s*(?:\s|$)",
    "roman_sub": r"^\s*\(\s*[ivxlcdm]+\s*\)",
}

# source_label -> (statement file, declared count)
SRC = {
    "assignment-2024-25-1":     (AUD + "text/asgn-2024-25-1.txt", 15),
    "assignment-2024-25-2":     (AUD + "text/asgn-2024-25-2.txt", 20),
    "assignment-2024-25-3":     (AUD + "text/asgn-2024-25-3.txt", 25),
    "assignment-2024-25-3-ep2": (AUD + "text/asgn-2024-25-3-ep2.txt", 25),
    "assignment-2024-25-4":     (AUD + "text/asgn-2024-25-4.txt", 16),
    "assignment-2024-25-5":     (AUD + "text/asgn-2024-25-5.txt", 24),
    "L10-11-chebyshev-deck":    (DEV + "corpus-text/L10-11-Cheb.txt", 3),
    "notes-lecture-series-01-09": (AUD + "text/notes-lecture-series-01-09.txt", 30),
    "ppt3-discrete-prob-dist":  (AUD + "text/ppt3-discrete-prob-dist.txt", 6),
    "ppt4-continuous-prob-dist":(AUD + "text/ppt4-continuous-prob-dist.txt", 7),
    "lms-standard-error-clt":   (AUD + "text/lms-standard-error-clt.txt", 5),
    "ppt5-estimation-summary":  (AUD + "text/ppt5-estimation-summary.txt", 5),
    "lms-theory-of-estimation": (AUD + "text/lms-theory-of-estimation.txt", 7),
}
# 2025-26 bundle labels point at the one file
SRC["assignment-2025-26-1"] = (DEV + "corpus-text/asgn-2025-26-bundle.txt", 24)
SRC["assignment-2025-26-2"] = (DEV + "corpus-text/asgn-2025-26-bundle.txt", 28)
# bundle: one file, per-assignment declared counts (report 18)
BUNDLE = (DEV + "corpus-text/asgn-2025-26-bundle.txt")
BUNDLE_DECL = {1: 19, 2: 36, 3: 25, 4: 21, 5: 18}

STOP = set("""a an the of to in on at for and or is are was were be been being this that
these those with without from by as it its if then than so such not no nor but into over
under between each every all any some more most less least other another same own very
can could may might must shall should will would do does did done have has had having
let given suppose find value number solution example problem question marks section""".split())

WORD = re.compile(r"[a-z0-9]+")
WMARK = re.compile(r"^\s*[A-Z0-9]{16,22}\s*$")


def tokens(text):
    t = re.sub(r"[^a-z0-9]+", " ", text.lower())
    return [w for w in WORD.findall(t) if w not in STOP and len(w) > 1]


def grams(toks, n=5):
    return [tuple(toks[i:i + n]) for i in range(len(toks) - n + 1)]


def clean(path):
    if not os.path.exists(path):
        return ""
    t = open(path, encoding="utf-8", errors="ignore").read()
    return "\n".join(l for l in t.split("\n") if not WMARK.match(l)).replace("\f", "\n")


def split_by(text, marker):
    pat = re.compile(marker)
    blocks, cur = [], []
    for ln in text.split("\n"):
        if pat.match(ln) and sum(len(x) for x in cur) > 30:
            blocks.append("\n".join(cur).strip())
            cur = [ln]
        else:
            cur.append(ln)
    if cur:
        blocks.append("\n".join(cur).strip())
    blocks = [" ".join(b.split()) for b in blocks if len(b.strip()) > 15]
    # the leading header always lands as block 0; drop it unless it is itself
    # a marked item. then dedupe by leading marker id (some sources repeat a
    # marker across pages, e.g. the chebyshev deck prints Q2 three times).
    if blocks and not pat.match(blocks[0]):
        blocks = blocks[1:]
    seen, out = set(), []
    for b in blocks:
        m = pat.match(b)
        key = m.group(0).strip().lower() if m else b[:24].lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(b)
    return out


def resolve_blocks(label, text):
    """Return (blocks, marker_name) for the label, using declared count."""
    if label in ("assignment-2025-26-1", "assignment-2025-26-2"):
        n = 1 if label.endswith("1") else 2
        want = BUNDLE_DECL[n]
        # slice the file to this assignment then split
        lines = text.split("\n")
        cur, grab = None, []
        for ln in lines:
            m = re.match(r"^Assignment\s*#?\s*(\d)", ln.strip(), re.I)
            if m:
                cur = int(m.group(1))
            if cur == n:
                grab.append(ln)
            elif cur is not None and cur > n:
                break
        sub = "\n".join(grab)
        for name, m in MARKERS.items():
            b = split_by(sub, m)
            if len(b) == want:
                return b, name
        return [], "none"
    if label in SRC:
        path, want = SRC[label]
        body = clean(path)
        for name, m in MARKERS.items():
            b = split_by(body, m)
            if len(b) == want:
                return b, name
        return [], "none"
    return [], "no-source"


def load_corpora():
    out = {}
    for name, path in CORPORA.items():
        if not os.path.exists(path) or os.path.getsize(path) < 50000:
            print(f"  SKIP {name} (missing or stub)", file=sys.stderr)
            continue
        g = set(grams(tokens(clean(path)), 5))
        out[name] = g
        print(f"  {name:18s} {len(g):>8,} distinct 5-grams")
    return out


def verdict(count, n):
    if n == 0:
        return "unsearched"
    if count >= 10 and count / n >= 0.20:
        return "verbatim"
    if count >= 6:
        return "strong"
    if count >= 3:
        return "family"
    return "open"


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if not (a.write or a.check):
        ap.print_help()
        return 2

    rows = list(csv.DictReader(open(LEDGER, encoding="utf-8")))
    print(f"ledger rows: {len(rows)}")
    print("loading corpora...")
    corpora = load_corpora()

    # cache resolved blocks per label, and record mismatches
    cache, markers, mismatches = {}, {}, {}

    def blocks_for(label):
        if label in cache:
            return cache[label]
        # the source file (bundle uses its own path)
        if label in ("assignment-2025-26-1", "assignment-2025-26-2"):
            text = clean(BUNDLE)
        elif label in SRC:
            text = clean(SRC[label][0])
        else:
            text = ""
        b, m = resolve_blocks(label, text)
        cache[label] = b
        markers[label] = m
        if not b and text:
            mismatches[label] = True
        return b

    filled = swept = frozen = 0
    for r in rows:
        iid, group = r["instance_id"], r["corpus_group"]
        label, order = r["source_label"], int(r["block_order"])
        if not r["summary"].strip():
            b = blocks_for(label)
            idx = order - 1
            if 0 <= idx < len(b):
                r["summary"] = b[idx][:500]
                r["description_state"] = "resolved"
                filled += 1
        if group in FROZEN_GROUPS or iid in FROZEN_IDS:
            frozen += 1
            continue
        text = r["summary"].strip()
        toks = tokens(text)
        g = list(dict.fromkeys(grams(toks, 5)))
        if not g:
            r["provenance_verdict"] = "unsearched"
            continue
        best, bn, bph = None, 0, []
        for name, gs in corpora.items():
            hits = [x for x in g if x in gs]
            if len(hits) > bn:
                best, bn, bph = name, len(hits), hits
        v = verdict(bn, len(g))
        r["provenance_verdict"] = v
        if best and v not in ("open", "unsearched"):
            r["provenance_source"] = best
        if bph:
            base = (r["evidence_locator"] or "").split(";")[0].strip()
            r["evidence_locator"] = base + " ; " + (best or "") + ": " + \
                " | ".join(" ".join(x) for x in bph[:4])
        swept += 1

    by_v = collections.Counter(r["provenance_verdict"] for r in rows)
    by_g = collections.defaultdict(collections.Counter)
    for r in rows:
        by_g[r["corpus_group"]][r["provenance_verdict"]] += 1
    desc = collections.Counter(r["description_state"] for r in rows)

    print(f"\ndescriptions filled : {filled}")
    print(f"rows swept          : {swept}")
    print(f"rows frozen         : {frozen}")
    print(f"description state   : {dict(desc)}")
    print(f"marker used per src : { {k: v for k, v in sorted(markers.items())} }")
    print(f"count mismatches    : {sorted(mismatches)}")
    print("\nverdicts:")
    for k, v in by_v.most_common():
        print(f"  {v:4d}  {k}")
    print("\nper group:")
    for g in sorted(by_g):
        print(f"  {g:20s} {dict(by_g[g])}")

    if a.write:
        fields = list(rows[0].keys())
        with open(LEDGER + ".tmp", "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)
        os.replace(LEDGER + ".tmp", LEDGER)
        out = {
            "rows": len(rows), "descriptions_filled": filled,
            "rows_swept": swept, "rows_frozen": frozen,
            "desc_state": dict(desc), "by_verdict": dict(by_v),
            "by_group": {g: dict(c) for g, c in by_g.items()},
            "markers": markers, "count_mismatches": sorted(mismatches),
            "frozen_groups": sorted(FROZEN_GROUPS), "frozen_ids": sorted(FROZEN_IDS),
            "corpora": {k: len(v) for k, v in corpora.items()},
        }
        with open(REPORT, "w", encoding="utf-8") as fh:
            json.dump(out, fh, indent=2)
        print("\nwrote", LEDGER)
        print("wrote", REPORT)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
