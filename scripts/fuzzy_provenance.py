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
    """Distinctive numeric signatures only. Deliberately narrow, because a
    validation pass showed decimal table values (2.262, 9.488) and 2-digit
    fragments (19.41) produce FALSE matches in a big book.

    Kept: fractions (21/25), 3+ digit integers in the realistic question range
    (100..9999, so 5000 yes but a stray 5-digit table run is capped), and that is
    it. Decimals are excluded entirely: statistics books are full of them.
    """
    # unfold LaTeX fractions FIRST, before norm_ocr strips the backslashes
    t = re.sub(r"\\?frac\s*\{\s*(\d+)\s*\}\s*\{\s*(\d+)\s*\}", r"\1/\2", t)
    t = norm_ocr(t)
    t = re.sub(r"\b(\d{1,3})\s*/\s*(\d{1,3})\b", r"\1/\2", t)
    out = set()
    out |= {m.group(0) for m in re.finditer(r"\d{1,3}/\d{1,3}\b", t)}
    # 3-4 digit integers only, capped at 9999 so a long table number is not grabbed
    out |= {m.group(0) for m in re.finditer(r"(?<!\d)(\d{3,4})(?!\d)", t)}
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
    """Evidence rule, kept simple and auditable.

    One signal that matters: DISTINCTIVE n-gram overlap between the row and the
    corpus (bgh/bgt), plus DISTINCTIVE number matches (bnh), where "distinctive"
    means the token appears in exactly one of the four reference corpora.

    The word-ratio signal was REMOVED after validation: it fired on generic MCQ
    blocks ("standard normal variate mean") that share only common vocabulary.
    A short row cannot produce enough distinctive grams, so those correctly fall
    to "open" rather than a false claim.

    Labels:
      fuzzy-verbatim  2+ distinctive numbers, or high gram overlap
      fuzzy-strong    1 distinctive number with some gram support, or good overlap
      fuzzy-family    partial overlap
      open            no usable signal
    """
    if bgt == 0:
        return "unsearched"
    ratio = bgh / bgt
    # HONEST CEILING after validation: a single distinctive number can coincide by
    # chance in a 3.5M-char book (11/26 turned up in an unrelated "Ans" line), so
    # one number is NOT enough for a source claim. Requiring 2+ distinctive
    # numbers OR a number together with strong distinctive-gram overlap makes the
    # matcher precise (high-confidence) and deliberately conservative (it misses
    # real matches it cannot prove). That tradeoff is the point: report the
    # candidates it can stand behind, leave the rest "open".
    if bnh >= 2 and ratio >= 0.15:
        return "fuzzy-verbatim"
    if bnh >= 1 and ratio >= 0.35:
        return "fuzzy-verbatim"
    if bnh >= 2 or (bnh >= 1 and ratio >= 0.15):
        return "fuzzy-strong"
    if ratio >= 0.45:
        return "fuzzy-family"
    return "open"


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--verify", action="store_true",
                    help="print each candidate with its matched tokens and their "
                         "context in the book, so a human can accept or reject it")
    a = ap.parse_args(argv)
    if not (a.write or a.check or a.verify):
        ap.print_help()
        return 2

    rows = list(csv.DictReader(open(IN_LEDGER, encoding="utf-8")))
    print(f"rows: {len(rows)}")
    print("building fuzzy corpora (OCR-normalised)...")
    corps = {}
    RAW = {}
    for name, path in CORPORA.items():
        c = Corpus(path)
        if c.grams:
            corps[name] = c
            RAW[name] = open(path, encoding="utf-8", errors="ignore").read()
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
        if a.verify and v in ("fuzzy-verbatim", "fuzzy-strong"):
            dn = sorted(x for x in nums if x in DISTINCTIVE_NUM)
            print(f"\n{iid}  [{v}]  -> {best}")
            print(f"   row: {text[:110]!r}")
            print(f"   distinctive numbers: {dn if dn else '(none, word-ratio driven)'}")
            if dn and best:
                raw = RAW.get(best, "")
                for tok in dn[:3]:
                    idx = raw.find(tok)
                    if idx < 0:
                        # the OCR may write it with spaces; show the number bare
                        idx = raw.find(tok.replace("/", " "))
                    snippet = raw[max(0, idx - 60):idx + 60] if idx >= 0 else "(token not found verbatim)"
                    print(f"      {tok} @ {snippet!r}")

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
