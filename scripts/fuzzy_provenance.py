#!/usr/bin/env python3
"""Fuzzy provenance matcher for the MAS2001 corpus.

The exact 5-gram sweep produces FALSE NEGATIVES on the scanned books: the G&K
text on disk is OCR noise ("Fo.r example", "o.f", "a~d~t"), so a phrase that IS
present never matches. This matcher fixes that:

  1. OCR normalisation before tokenising (Fo.r -> for, o.f -> of, split words
     rejoined, punctuation noise collapsed).
  2. Numeric signatures: distinctive numbers in a question (21/25, 520 pages,
     6x(1-x), lambda=10) matched separately from words, because numbers survive
     OCR far better than words.
  3. Word-level fuzzy: 3-gram overlap with a Levenshtein-tolerant token compare,
     so "chebycnev" still counts as "chebyshev".

Output: per-row fuzzy verdict + the best fuzzy phrase, written to a new file so
the canonical ledger and the exact sweep output are both untouched.

    python3 scripts/fuzzy_provenance.py --check
    python3 scripts/fuzzy_provenance.py --write
"""
import argparse
import collections
import csv
import difflib
import json
import os
import re
import sys

S2 = "/home/liebert511/mas2001-mte-s2/"
DEV = "/home/liebert511/mas2001-devore/"

IN_LEDGER = S2 + "reports/evidence/question-instance-ledger-enriched.csv"
OUT_LEDGER = S2 + "reports/evidence/question-instance-ledger-fuzzy.csv"
REPORT = S2 + "reports/evidence/fuzzy-match-20260917.json"

CORPORA = {
    "G&K-Fundamentals": DEV + "corpus-text/G-K-Fundamentals-Math-Stat.txt",
    "Hogg-Tanis-9e":    DEV + "corpus-text/Hogg-Tanis-9e.txt",
    "GGD-Vol1":         DEV + "corpus-text/GGD-Vol1-OCR-OCR.txt",
    "Davenport":        DEV + "corpus-text/Davenport-OCR.txt",
}

# full statement text per row id (same injection the exact sweep uses), so a
# short manifest label still has real content to match.
EXTRA_TEXT = {}
try:
    _ete = json.load(open(DEV + "ete-blocks.json", encoding="utf-8"))
    for k, v in _ete.items():
        EXTRA_TEXT["ete-" + k] = v
        m = re.match(r"^(.+)-(\d+)$", k)
        if m:
            EXTRA_TEXT["ete-%s-Q%s" % (m.group(1), m.group(2))] = v
except Exception:
    pass
try:
    _mte = json.load(open(DEV + "mte-blocks.json", encoding="utf-8"))
    for k, v in _mte.items():
        EXTRA_TEXT["mte-" + k] = v
except Exception:
    pass

FROZEN_GROUPS = {"mte", "four-decks"}

STOP = set("""a an the of to in on at for and or is are was were be been being this that
these those with without from by as it its if then than so such not no nor but into over
under between each every all any some more most less least other another same own very
can could may might must shall should will would do does did done have has had having
let given suppose find value number solution example problem question marks section""".split())

WORD = re.compile(r"[a-z0-9]+")
NUM = re.compile(r"\d+(?:[./]\d+)*")


def norm_ocr(t):
    """Repair the common scan noise so tokens line up with the question text."""
    t = t.lower()
    # letter-dot-letter the OCR inserts inside words: Fo.r, o.f, a:particle
    t = re.sub(r"(?<=[a-z])[.:;,'\u00b7](?=[a-z])", "", t)
    # stray tildes, bars, brackets inside words
    t = re.sub(r"[~^`|\\_\[\]{}]", " ", t)
    # the reseller watermark tags
    t = re.sub(r"\bmsv[0-9a-z]{15,}\b", " ", t)
    # collapse split hyphens: "typo-graphical" -> "typographical"
    t = re.sub(r"(?<=[a-z])-(?=[a-z])", "", t)
    return t


def tokens(t):
    t = norm_ocr(t)
    t = re.sub(r"\$[^$]*\$", " ", t)
    return [w for w in WORD.findall(t) if w not in STOP and len(w) > 1]


def numbers(t):
    """Distinctive numeric signatures only. A common value like 0.5 or a bare
    single digit is NOT distinctive, so it is excluded; fractions, 3+ digit
    runs, and multi-digit decimals are kept, because those survive OCR and
    rarely coincide by chance. LaTeX fractions (\\frac{21}{25}) are unfolded to
    21/25 first, since the question text is written in LaTeX and the book text
    is OCR, so only the digits survive both."""
    # unfold LaTeX fractions FIRST, before norm_ocr strips the backslashes:
    # \frac{21}{25} -> 21/25
    t = re.sub(r"\\?frac\s*\{\s*(\d+)\s*\}\s*\{\s*(\d+)\s*\}", r"\1/\2", t)
    t = norm_ocr(t)
    # the book writes spaced fractions "21 / 25" or "21/ 25"
    t = re.sub(r"\b(\d{1,3})\s*/\s*(\d{1,3})\b", r"\1/\2", t)
    out = set()
    # no leading \b: LaTeX can glue a digit to a word ("geq21/25")
    out |= {m.group(0) for m in re.finditer(r"\d{1,3}/\d{1,3}\b", t)}
    out |= {m.group(0) for m in re.finditer(r"\d{3,}\b", t)}
    out |= {m.group(0) for m in re.finditer(r"\d\.\d{2,}\b", t)}
    return out


def grams(ts, n=3):
    return set(tuple(ts[i:i + n]) for i in range(len(ts) - n + 1))


def fuzzy_eq(a, b, thr=0.80):
    if a == b:
        return True
    if abs(len(a) - len(b)) > 2:
        return False
    return difflib.SequenceMatcher(None, a, b).ratio() >= thr


class Corpus:
    def __init__(self, path):
        self.grams = set()
        self.nums = set()
        self.words = set()
        if not os.path.exists(path) or os.path.getsize(path) < 50000:
            return
        raw = open(path, encoding="utf-8", errors="ignore").read()
        toks = tokens(raw)
        self.grams = grams(toks, 3)
        self.words = set(toks)
        self.nums = numbers(raw)

    def score(self, toks, nums, distinctive_words=None, distinctive_nums=None):
        """Return (gram_hits, gram_total, num_hits, num_total, distinct_word_ratio).
        Only distinctive words/numbers count, so common vocabulary and common
        table values do not inflate the score."""
        g = grams(toks, 3)
        gh = sum(1 for x in g if x in self.grams)
        ws = {w for w in set(toks) if distinctive_words is None or w in distinctive_words}
        wh = sum(1 for x in ws if x in self.words)
        ns = {x for x in nums if distinctive_nums is None or x in distinctive_nums}
        nh = sum(1 for x in ns if x in self.nums)
        return gh, len(g), nh, len(ns), (wh / len(ws) if ws else 0.0)


def verdict(bgh, bgt, bnh, word_ratio):
    """Evidence rule, kept simple and documented so it is auditable.

    Two signals, both restricted to DISTINCTIVE tokens (a token that appears in
    exactly one of the four reference corpora):
      - distinctive number matches (bnh): strong, because 21/25 or 520 or 0.2301
        landing in exactly one book is not coincidence.
      - distinctive word ratio (word_ratio): the share of the row's distinctive
        words that the corpus contains.

    Labels:
      fuzzy-verbatim  distinctive number + strong word support, or 2+ distinctive
                      numbers, or very high word ratio
      fuzzy-strong    a distinctive number, or high word ratio
      fuzzy-family    partial signal
      open            no signal
    """
    if bgt == 0:
        return "unsearched"
    ratio = bgh / bgt
    if (bnh >= 1 and word_ratio >= 0.50) or bnh >= 2 or word_ratio >= 0.90:
        return "fuzzy-verbatim"
    if bnh >= 1 or ratio >= 0.45 or word_ratio >= 0.70:
        return "fuzzy-strong"
    if ratio >= 0.25 or word_ratio >= 0.40:
        return "fuzzy-family"
    return "open"


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if not (a.write or a.check):
        ap.print_help()
        return 2

    rows = list(csv.DictReader(open(IN_LEDGER, encoding="utf-8")))
    print(f"rows: {len(rows)}")
    print("building fuzzy corpora (OCR-normalised)...")
    corps = {}
    for name, path in CORPORA.items():
        c = Corpus(path)
        if c.grams:
            corps[name] = c
            print(f"  {name:18s} {len(c.grams):>8,} 3-grams  {len(c.nums):>6,} numbers")

    # a word OR number is distinctive when it appears in only ONE corpus, so
    # shared statistics vocabulary ("probability", "distribution") and common
    # table values (1.96, 3.841) do not count as evidence of a source.
    word_corpus_count = collections.Counter()
    for c in corps.values():
        for w in c.words:
            word_corpus_count[w] += 1
    DISTINCTIVE = {w for w, n in word_corpus_count.items() if n == 1}
    num_corpus_count = collections.Counter()
    for c in corps.values():
        for x in c.nums:
            num_corpus_count[x] += 1
    DISTINCTIVE_NUM = {x for x, n in num_corpus_count.items() if n == 1}
    print(f"  distinctive words: {len(DISTINCTIVE):,}   distinctive numbers: {len(DISTINCTIVE_NUM):,}")

    counts = collections.Counter()
    by_group = collections.defaultdict(collections.Counter)
    for r in rows:
        iid, group = r["instance_id"], r["corpus_group"]
        if group in FROZEN_GROUPS:
            counts["frozen"] += 1
            by_group[group][r["provenance_verdict"]] += 1
            continue
        text = r["summary"].strip()
        # use the full block text where the summary is a short manifest label
        extra = EXTRA_TEXT.get(iid, "")
        if len(tokens(text)) < 6 and len(tokens(extra)) > len(tokens(text)):
            text = extra
        toks = tokens(text)
        nums = numbers(text)
        if not toks:
            counts["unsearched"] += 1
            by_group[group]["unsearched"] += 1
            continue
        best, bgh, bgt, bnh, bnt = None, 0, 0, 0, 0
        bwr = 0.0
        for name, c in corps.items():
            gh, gt, nh, nt, wr = c.score(toks, nums, DISTINCTIVE, DISTINCTIVE_NUM)
            if (nh, gh) > (bnh, bgh):
                best, bgh, bgt, bnh, bnt, bwr = name, gh, gt, nh, nt, wr
        v = verdict(bgh, bgt, bnh, bwr)
        counts[v] += 1
        by_group[group][v] += 1

    print("\nfuzzy verdicts (non-frozen rows):")
    for k, n in counts.most_common():
        print(f"  {n:4d}  {k}")
    print("\nper group:")
    for g in sorted(by_group):
        print(f"  {g:20s} {dict(by_group[g])}")

    if a.write:
        with open(REPORT, "w", encoding="utf-8") as fh:
            json.dump({"rows": len(rows), "by_verdict": dict(counts),
                       "by_group": {g: dict(c) for g, c in by_group.items()},
                       "corpora": {k: len(v.grams) for k, v in corps.items()}},
                      fh, indent=2)
        print("\nwrote", REPORT)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
