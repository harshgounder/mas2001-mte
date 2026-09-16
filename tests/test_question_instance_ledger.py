"""Unit tests for scripts/build_question_instance_ledger.py.

The structured-data tests read the real reports on disk because those reports are the
sources the ledger reuses; the fixture tests exercise --output and --check without
touching the repository. Run with:

    python3 -B tests/test_question_instance_ledger.py -v
"""

import pathlib
import sys
import tempfile
import unittest
from collections import Counter

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.dont_write_bytecode = True
if str(REPO / "scripts") not in sys.path:
    sys.path.insert(0, str(REPO / "scripts"))
import build_question_instance_ledger as ledger


EXPECTED_GROUP_COUNTS = {
    "teaching": 60,
    "chebyshev": 3,
    "assignments-2025": 52,
    "assignments-2025-bundle": 119,
    "mte": 16,
    "ete": 97,
    "assignments-2024": 125,
    "four-decks": 30,
}

EXPECTED_SOURCE_COUNTS = {
    "notes-lecture-series-01-09": 30,
    "ppt3-discrete-prob-dist": 6,
    "ppt4-continuous-prob-dist": 7,
    "lms-standard-error-clt": 5,
    "ppt5-estimation-summary": 5,
    "lms-theory-of-estimation": 7,
    "L10-11-chebyshev-deck": 3,
    "assignment-2025-26-1": 24,
    "assignment-2025-26-2": 28,
    "assignment-2025-26-bundle-1": 19,
    "assignment-2025-26-bundle-2": 36,
    "assignment-2025-26-bundle-3": 25,
    "assignment-2025-26-bundle-4": 21,
    "assignment-2025-26-bundle-5": 18,
    "paper-mte-2024-25": 8,
    "paper-mte-2025-26": 8,
    "E24S3": 15,
    "E25S3": 14,
    "E24S4": 14,
    "E25S4": 19,
    "E25SUM": 18,
    "R25S3": 8,
    "R25S4": 9,
    "assignment-2024-25-1": 15,
    "assignment-2024-25-2": 20,
    "assignment-2024-25-3": 25,
    "assignment-2024-25-3-ep2": 25,
    "assignment-2024-25-4": 16,
    "assignment-2024-25-5": 24,
    "sp-l1-7": 13,
    "sp-l8-9": 4,
    "sp-l12-13-discrete": 6,
    "sp-l14-15-continuous": 7,
}

EXPECTED_ETE_SCOPES = {"IN": 56, "BOUNDARY": 3, "PARTIAL": 3, "OUT": 35}

EXPECTED_MTE_VERDICTS = {
    "CONCEPT": 5,
    "RESKIN": 3,
    "RESKIN + CIRCULATING": 2,
    "FAMILY": 1,
    "VERBATIM": 1,
    "FAMILY + CIRCULATING": 1,
    "OPEN": 1,
    "DECK": 1,
    "MIXED": 1,
}

PENDING_ID_STEMS = [
    "teach-ppt3",
    "teach-ppt4",
    "teach-lms-se-clt",
    "teach-ppt5",
    "teach-lms-theory",
    "cheb-",
    "asn2025-",
    "asn2024-",
]


def real_text(rel):
    return (REPO / rel).read_text(encoding="utf-8")


def by_id(rows):
    return {row["instance_id"]: row for row in rows}


class RealLedgerChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = ledger.generate_rows(REPO)

    def test_exact_total_of_502(self):
        self.assertEqual(len(self.rows), 502)
        self.assertEqual(ledger.TOTAL_INSTANCES, 502)

    def test_exact_group_counts(self):
        counts = Counter(row["corpus_group"] for row in self.rows)
        self.assertEqual(dict(counts), EXPECTED_GROUP_COUNTS)
        self.assertEqual(sum(counts.values()), 502)

    def test_exact_source_counts(self):
        counts = Counter(row["source_label"] for row in self.rows)
        self.assertEqual(dict(counts), EXPECTED_SOURCE_COUNTS)
        self.assertEqual(sum(counts.values()), 502)

    def test_instance_ids_are_unique(self):
        ids = [row["instance_id"] for row in self.rows]
        self.assertEqual(len(ids), len(set(ids)))

    def test_group_order_is_fixed_and_contiguous(self):
        groups = [row["corpus_group"] for row in self.rows]
        self.assertEqual(groups, sorted(groups, key=ledger.GROUP_ORDER.index))
        seen = []
        for group in groups:
            if not seen or seen[-1] != group:
                seen.append(group)
        self.assertEqual(seen, ledger.GROUP_ORDER)
        self.assertEqual(list(EXPECTED_GROUP_COUNTS.keys()), ledger.GROUP_ORDER)

    def test_ordering_key_is_sorted(self):
        keys = [ledger.ordering_key(row) for row in self.rows]
        self.assertEqual(keys, sorted(keys))

    def test_block_order_is_dense_per_source(self):
        orders = {}
        for row in self.rows:
            orders.setdefault(row["source_label"], []).append(row["block_order"])
        for source_label, values in orders.items():
            self.assertEqual(values, list(range(1, len(values) + 1)), source_label)

    def test_every_row_is_gross_and_family_unassigned(self):
        for row in self.rows:
            self.assertEqual(row["status"], "gross")
            self.assertEqual(row["content_family_id"], "")

    def test_header_is_exact_and_ordered(self):
        expected = [
            "instance_id",
            "corpus_group",
            "source_label",
            "block_order",
            "page_start",
            "page_end",
            "summary",
            "scope",
            "description_state",
            "provenance_verdict",
            "provenance_source",
            "evidence_locator",
            "content_family_id",
            "status",
        ]
        self.assertEqual(ledger.FIELDS, expected)
        self.assertEqual(ledger.render_csv([]).splitlines()[0], ",".join(expected))


class PlaceholderHonestyChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = ledger.generate_rows(REPO)
        cls.index = by_id(cls.rows)

    def test_seeded_placeholders_say_pending(self):
        for stem in PENDING_ID_STEMS:
            matches = [r for r in self.rows if r["instance_id"].startswith(stem)]
            self.assertTrue(matches, stem)
            for row in matches:
                self.assertEqual(row["description_state"], "pending", row["instance_id"])

    def test_pending_rows_do_not_claim_a_description(self):
        for row in self.rows:
            if row["description_state"] == "pending":
                self.assertEqual(row["summary"], "")
                self.assertEqual(row["provenance_verdict"], "unsearched")

    def test_no_pending_row_is_marked_resolved(self):
        states = {row["description_state"] for row in self.rows}
        self.assertEqual(states, {"pending", "resolved"})

    def test_resolved_rows_have_summary_and_locator(self):
        for row in self.rows:
            if row["description_state"] == "resolved":
                self.assertTrue(row["summary"], row["instance_id"])
                self.assertTrue(row["evidence_locator"], row["instance_id"])

    def test_placeholder_counts(self):
        def count(stem):
            return len([r for r in self.rows if r["instance_id"].startswith(stem)])

        self.assertEqual(count("teach-ppt3"), 6)
        self.assertEqual(count("teach-ppt4"), 7)
        self.assertEqual(count("teach-lms-se-clt"), 5)
        self.assertEqual(count("teach-ppt5"), 5)
        self.assertEqual(count("teach-lms-theory"), 7)
        self.assertEqual(count("cheb-"), 3)
        self.assertEqual(count("asn2025-"), 52)
        self.assertEqual(count("asn2024-"), 125)

    def test_assignment_2025_ids_encode_section_manifests(self):
        a1 = [r["instance_id"] for r in self.rows if r["source_label"] == "assignment-2025-26-1"]
        a2 = [r["instance_id"] for r in self.rows if r["source_label"] == "assignment-2025-26-2"]
        self.assertEqual(len(a1), 24)
        self.assertEqual(len(a2), 28)
        for number in range(1, 11):
            self.assertIn("asn2025-1-MCQ-%02d" % number, a1)
        for number in range(1, 7):
            self.assertIn("asn2025-1-SHORT-%02d" % number, a1)
        for number in range(1, 13):
            self.assertIn("asn2025-2-A-%02d" % number, a2)

    def test_assignment_2024_q_counts(self):
        counts = Counter(
            row["source_label"]
            for row in self.rows
            if row["corpus_group"] == "assignments-2024"
        )
        self.assertEqual(
            counts["assignment-2024-25-3-ep2"], 25
        )
        self.assertEqual(
            [counts[label] for label, _ in ledger.ASSIGNMENT_2024_COUNTS],
            [15, 20, 25, 25, 16, 24],
        )

    def test_deck01_fallback_seeds_pending(self):
        fallback = ledger.build_rows(
            real_text(ledger.ETE_REL),
            real_text(ledger.MTE_REL),
            real_text(ledger.DECK_REL),
            "",
            real_text(ledger.BUNDLE_REL),
        )
        deck01 = [r for r in fallback if r["source_label"] == "notes-lecture-series-01-09"]
        self.assertEqual(len(deck01), 30)
        self.assertTrue(all(r["description_state"] == "pending" for r in deck01))
        self.assertTrue(all(r["summary"] == "" for r in deck01))
        self.assertEqual(ledger.validate_rows(fallback), [])

    def test_existing_383_rows_are_preserved(self):
        original = [
            r
            for r in self.rows
            if r["corpus_group"] != "assignments-2025-bundle"
        ]
        self.assertEqual(len(original), 383)
        counts = Counter(r["corpus_group"] for r in original)
        self.assertEqual(
            dict(counts),
            {
                "teaching": 60,
                "chebyshev": 3,
                "assignments-2025": 52,
                "mte": 16,
                "ete": 97,
                "assignments-2024": 125,
                "four-decks": 30,
            },
        )

    def test_bundle_group_is_119_resolved_rows(self):
        bundle = [
            r for r in self.rows if r["corpus_group"] == "assignments-2025-bundle"
        ]
        self.assertEqual(len(bundle), 119)
        for row in bundle:
            self.assertEqual(row["description_state"], "resolved")
            self.assertTrue(row["summary"])
            self.assertEqual(row["scope"], "in-scope")
            self.assertEqual(row["provenance_verdict"], "unsearched")
            self.assertTrue(row["instance_id"].startswith("asgnbundle-"))

    def test_bundle_group_pages_stay_in_assignment_ranges(self):
        ranges = {
            "assignment-2025-26-bundle-1": (1, 4),
            "assignment-2025-26-bundle-2": (5, 8),
            "assignment-2025-26-bundle-3": (9, 11),
            "assignment-2025-26-bundle-4": (12, 14),
            "assignment-2025-26-bundle-5": (15, 17),
        }
        bundle = [
            r for r in self.rows if r["corpus_group"] == "assignments-2025-bundle"
        ]
        for row in bundle:
            low, high = ranges[row["source_label"]]
            self.assertTrue(low <= int(row["page_start"]) <= high, row["instance_id"])
            self.assertTrue(low <= int(row["page_end"]) <= high, row["instance_id"])


class StructuredParsingChecks(unittest.TestCase):
    def test_parses_97_ete_rows(self):
        rows = ledger.parse_ete_rows(real_text(ledger.ETE_REL))
        self.assertEqual(len(rows), 97)
        self.assertEqual(
            Counter(r["scope"].split(",")[0].strip() for r in rows), EXPECTED_ETE_SCOPES
        )
        self.assertEqual(len(set(r["instance_id"] for r in rows)), 97)

    def test_parses_16_mte_rows(self):
        rows = ledger.parse_mte_rows(real_text(ledger.MTE_REL))
        self.assertEqual(len(rows), 16)
        self.assertEqual(
            Counter(r["provenance_verdict"] for r in rows), EXPECTED_MTE_VERDICTS
        )
        self.assertEqual(len(set(r["instance_id"] for r in rows)), 16)

    def test_parses_30_deck_rows(self):
        rows = ledger.parse_deck_rows(real_text(ledger.DECK_REL))
        self.assertEqual(len(rows), 30)
        self.assertEqual(len(set(r["instance_id"] for r in rows)), 30)

    def test_parses_30_deck01_manifest_items(self):
        rows = ledger.parse_deck01_manifest(real_text(ledger.REGISTER_REL))
        self.assertEqual(len(rows), 30)
        self.assertEqual(rows[0]["page_start"], "41")
        self.assertEqual(rows[0]["page_end"], "42")
        self.assertEqual(rows[-1]["page_start"], "146")
        self.assertEqual(rows[-1]["page_end"], "147")

    def test_ete_pipe_inside_summary_is_preserved(self):
        rows = ledger.parse_ete_rows(real_text(ledger.ETE_REL))
        target = [r for r in rows if r["instance_id"] == "ete-E25S3-B1"][0]
        self.assertIn("|X-10|", target["summary"])
        self.assertEqual(target["scope"], "IN")

    def test_ete_scope_is_carried_and_provenance_unsearched(self):
        rows = ledger.generate_rows(REPO)
        ete = [r for r in rows if r["corpus_group"] == "ete"]
        self.assertEqual(len(ete), 97)
        for row in ete:
            self.assertEqual(row["provenance_verdict"], "unsearched")
            self.assertEqual(row["provenance_source"], "")
        scopes = Counter(r["scope"].split(",")[0].strip() for r in ete)
        self.assertEqual(dict(scopes), EXPECTED_ETE_SCOPES)

    def test_mte_provenance_carried_without_upgrade(self):
        index = by_id([r for r in ledger.generate_rows(REPO) if r["corpus_group"] == "mte"])
        self.assertEqual(index["mte-M25-Q5"]["provenance_verdict"], "DECK")
        self.assertIn("L10-11", index["mte-M25-Q5"]["provenance_source"])
        self.assertEqual(index["mte-M24-B1"]["provenance_verdict"], "VERBATIM")
        self.assertEqual(index["mte-M24-C1"]["provenance_verdict"], "OPEN")
        self.assertIn("Palaniammal", index["mte-M24-C1"]["provenance_source"])

    def test_deck_provenance_carried(self):
        index = by_id(
            [r for r in ledger.generate_rows(REPO) if r["corpus_group"] == "four-decks"]
        )
        first = index["deck-L17-01"]
        self.assertEqual(first["provenance_verdict"], "exact-text lead")
        self.assertEqual(first["provenance_source"], "Devore")
        self.assertEqual(first["page_start"], "31")
        self.assertEqual(first["summary"], "faculty computer setup selection")

    def test_deck01_resolved_rows_come_from_manifest(self):
        rows = [
            r
            for r in ledger.generate_rows(REPO)
            if r["source_label"] == "notes-lecture-series-01-09"
        ]
        self.assertEqual(len(rows), 30)
        self.assertTrue(all(r["description_state"] == "resolved" for r in rows))
        self.assertTrue(any("basketball lineup" in r["summary"] for r in rows))


class ValidationChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = ledger.generate_rows(REPO)

    def test_clean_rows_have_no_problems(self):
        self.assertEqual(ledger.validate_rows(self.rows), [])

    def test_validate_flags_pending_row_with_summary(self):
        rows = [dict(row) for row in self.rows]
        for row in rows:
            if row["description_state"] == "pending":
                row["summary"] = "should not be here"
                break
        problems = ledger.validate_rows(rows)
        self.assertTrue(any("pending row has a summary" in p for p in problems))

    def test_validate_flags_group_count_drift(self):
        rows = [dict(row) for row in self.rows]
        rows[0]["corpus_group"] = "ghost"
        problems = ledger.validate_rows(rows)
        self.assertTrue(any("unknown group" in p for p in problems))
        self.assertTrue(any("teaching" in p for p in problems))


class CheckChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = ledger.generate_rows(REPO)

    def test_clean_ledger_has_no_problems(self):
        self.assertEqual(ledger.check_ledger(ledger.render_csv(self.rows), self.rows), [])

    def test_check_detects_stale_generated_content(self):
        text = ledger.render_csv(self.rows).replace("gross", "stale", 1)
        problems = ledger.check_ledger(text, self.rows)
        self.assertTrue(any("stale generated content" in p for p in problems))

    def test_check_detects_header_mismatch(self):
        text = ledger.render_csv(self.rows).replace("content_family_id", "family", 1)
        problems = ledger.check_ledger(text, self.rows)
        self.assertTrue(any("header mismatch" in p for p in problems))

    def test_check_detects_row_count_mismatch(self):
        lines = ledger.render_csv(self.rows).splitlines(keepends=True)
        problems = ledger.check_ledger("".join(lines[:-1]), self.rows)
        self.assertTrue(any("row count mismatch" in p for p in problems))

    def test_check_detects_duplicate_id(self):
        lines = ledger.render_csv(self.rows).splitlines(keepends=True)
        duplicated = lines[1]
        problems = ledger.check_ledger("".join(lines + [duplicated]), self.rows)
        self.assertTrue(any("duplicate instance_id" in p for p in problems))

    def test_check_detects_order_mismatch(self):
        lines = ledger.render_csv(self.rows).splitlines(keepends=True)
        lines[1], lines[2] = lines[2], lines[1]
        problems = ledger.check_ledger("".join(lines), self.rows)
        self.assertTrue(any("row order mismatch" in p for p in problems))

    def test_check_detects_empty_ledger(self):
        self.assertTrue(ledger.check_ledger("", self.rows))


class MainChecks(unittest.TestCase):
    def test_write_check_and_tamper(self):
        with tempfile.TemporaryDirectory(prefix="mas2001-qil-") as tmp:
            out = pathlib.Path(tmp) / "question-instance-ledger.csv"
            self.assertEqual(ledger.main(["--output", str(out)]), 0)
            self.assertTrue(out.is_file())
            self.assertEqual(len(out.read_text(encoding="utf-8").splitlines()), 503)
            self.assertEqual(ledger.main(["--check", "--output", str(out)]), 0)
            out.write_text(
                out.read_text(encoding="utf-8").replace("gross", "stale", 1),
                encoding="utf-8",
            )
            self.assertEqual(ledger.main(["--check", "--output", str(out)]), 1)

    def test_check_missing_ledger_exits_nonzero(self):
        with tempfile.TemporaryDirectory(prefix="mas2001-qil-") as tmp:
            missing = pathlib.Path(tmp) / "absent.csv"
            self.assertEqual(ledger.main(["--check", "--output", str(missing)]), 1)

    def test_default_output_lives_under_reports_evidence(self):
        self.assertEqual(
            ledger.LEDGER_REL,
            pathlib.Path("reports") / "evidence" / "question-instance-ledger.csv",
        )


class DeterminismAndDashChecks(unittest.TestCase):
    def test_render_is_byte_for_byte_repeatable(self):
        first = ledger.render_csv(ledger.generate_rows(REPO))
        second = ledger.render_csv(ledger.generate_rows(REPO))
        self.assertEqual(first, second)

    def test_csv_has_no_em_or_en_dash(self):
        text = ledger.render_csv(ledger.generate_rows(REPO))
        self.assertNotIn("\u2014", text)
        self.assertNotIn("\u2013", text)

    def test_module_source_has_no_em_or_en_dash(self):
        text = (REPO / "scripts" / "build_question_instance_ledger.py").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("\u2014", text)
        self.assertNotIn("\u2013", text)

    def test_test_source_has_no_em_or_en_dash(self):
        text = pathlib.Path(__file__).read_text(encoding="utf-8")
        self.assertNotIn("\u2014", text)
        self.assertNotIn("\u2013", text)


if __name__ == "__main__":
    unittest.main()
