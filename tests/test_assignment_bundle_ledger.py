"""Unit tests for scripts/build_assignment_bundle_ledger.py.

The real-ledger tests read the bundle text layer on disk because that file is the
source the ledger reuses; the fixture tests exercise --output and --check without
leaving artifacts in the repository. Run with:

    python3 -B tests/test_assignment_bundle_ledger.py -v
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
import build_assignment_bundle_ledger as bundle

BUNDLE_PATH = bundle.DEFAULT_BUNDLE
LEDGER_PATH = REPO / bundle.LEDGER_REL

EXPECTED_ASSIGNMENT_COUNTS = {1: 19, 2: 36, 3: 25, 4: 21, 5: 18}

EXPECTED_SOURCE_COUNTS = {
    "assignment-2025-26-bundle-1": 19,
    "assignment-2025-26-bundle-2": 36,
    "assignment-2025-26-bundle-3": 25,
    "assignment-2025-26-bundle-4": 21,
    "assignment-2025-26-bundle-5": 18,
}

EXPECTED_PAGE_RANGES = {
    1: (1, 4),
    2: (5, 8),
    3: (9, 11),
    4: (12, 14),
    5: (15, 17),
}

ALLOWED_FAMILIES = {
    "",
    "memory_based",
    "concept_based",
    "analytical_based",
    "application_based",
}


def by_id(rows):
    return {row["item_id"]: row for row in rows}


class RealLedgerChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = bundle.generate_rows(BUNDLE_PATH)
        cls.index = by_id(cls.rows)

    def test_exact_total_of_119(self):
        self.assertEqual(len(self.rows), 119)
        self.assertEqual(bundle.EXPECTED_TOTAL, 119)

    def test_exact_assignment_counts(self):
        counts = Counter(row["assignment"] for row in self.rows)
        self.assertEqual(dict(counts), EXPECTED_ASSIGNMENT_COUNTS)
        self.assertEqual(sum(counts.values()), 119)
        self.assertEqual(bundle.ASSIGNMENT_COUNTS, EXPECTED_ASSIGNMENT_COUNTS)

    def test_exact_source_label_counts(self):
        counts = Counter(row["source_label"] for row in self.rows)
        self.assertEqual(dict(counts), EXPECTED_SOURCE_COUNTS)
        self.assertEqual(sum(counts.values()), 119)

    def test_item_ids_are_unique(self):
        ids = [row["item_id"] for row in self.rows]
        self.assertEqual(len(ids), len(set(ids)))

    def test_assignment_order_is_fixed_and_contiguous(self):
        numbers = [row["assignment"] for row in self.rows]
        self.assertEqual(numbers, sorted(numbers))
        seen = []
        for number in numbers:
            if not seen or seen[-1] != number:
                seen.append(number)
        self.assertEqual(seen, [1, 2, 3, 4, 5])

    def test_order_is_dense_within_each_assignment(self):
        orders = {}
        for row in self.rows:
            orders.setdefault(row["assignment"], []).append(row["order"])
        for assignment, values in orders.items():
            self.assertEqual(values, list(range(1, len(values) + 1)), assignment)

    def test_page_ranges_match_declared_assignment_ranges(self):
        for assignment, (low, high) in EXPECTED_PAGE_RANGES.items():
            subset = [row for row in self.rows if row["assignment"] == assignment]
            self.assertTrue(subset, assignment)
            self.assertEqual(min(row["page_start"] for row in subset), low)
            self.assertEqual(max(row["page_end"] for row in subset), high)
            for row in subset:
                self.assertTrue(low <= row["page_start"] <= high, row["item_id"])
                self.assertTrue(low <= row["page_end"] <= high, row["item_id"])
                self.assertLessEqual(row["page_start"], row["page_end"])

    def test_pdf_typo_45_is_recorded_as_a4(self):
        row = self.index["asgnbundle-5-A04"]
        self.assertEqual(row["assignment"], 5)
        self.assertEqual(row["order"], 4)
        self.assertEqual(row["item_label"], "A4")
        self.assertIn("45", row["evidence_locator"])
        self.assertIn("A4", row["evidence_locator"])
        self.assertIn("alternative hypothesis", row["summary"])
        self.assertNotIn("asgnbundle-5-45", self.index)

    def test_assignment_5_section_counts_include_the_typo(self):
        subset = [row for row in self.rows if row["assignment"] == 5]
        counts = Counter(row["section"] for row in subset)
        self.assertEqual(counts, {"A": 6, "B": 4, "C": 4, "D": 4})

    def test_assignment_3_section_counts(self):
        subset = [row for row in self.rows if row["assignment"] == 3]
        counts = Counter(row["section"] for row in subset)
        self.assertEqual(counts, {"A": 10, "B": 5, "C": 5, "D": 5})

    def test_every_summary_is_present_and_normalized(self):
        for row in self.rows:
            self.assertTrue(row["summary"], row["item_id"])
            self.assertNotIn("\u2014", row["summary"])
            self.assertNotIn("\u2013", row["summary"])
            self.assertNotIn("\n", row["summary"])

    def test_extraction_state_is_honest(self):
        states = Counter(row["extraction_state"] for row in self.rows)
        self.assertEqual(set(states), {"text_extracted", "text_layout_recovered"})
        self.assertEqual(sum(states.values()), 119)

    def test_no_2024_match_is_claimed(self):
        for row in self.rows:
            self.assertEqual(row["match_status"], "not_assessed")
            self.assertEqual(row["matched_2024_locator"], "")

    def test_structural_candidate_only_where_the_heading_states_it(self):
        for row in self.rows:
            self.assertIn(row["structural_family_candidate"], ALLOWED_FAMILIES)
            if row["assignment"] in (3, 4, 5):
                self.assertEqual(row["structural_family_candidate"], "")
            else:
                self.assertTrue(row["structural_family_candidate"], row["item_id"])

    def test_source_labels_follow_the_required_scheme(self):
        labels = {row["source_label"] for row in self.rows}
        self.assertEqual(
            labels,
            {
                "assignment-2025-26-bundle-1",
                "assignment-2025-26-bundle-2",
                "assignment-2025-26-bundle-3",
                "assignment-2025-26-bundle-4",
                "assignment-2025-26-bundle-5",
            },
        )

    def test_header_is_exact_and_ordered(self):
        expected = [
            "item_id",
            "source_label",
            "assignment",
            "section",
            "item_label",
            "order",
            "page_start",
            "page_end",
            "summary",
            "extraction_state",
            "structural_family_candidate",
            "match_status",
            "matched_2024_locator",
            "evidence_locator",
        ]
        self.assertEqual(bundle.FIELDS, expected)
        self.assertEqual(bundle.render_csv([]).splitlines()[0], ",".join(expected))


class ParserChecks(unittest.TestCase):
    def test_expected_label_sequences(self):
        self.assertEqual(len(bundle.expected_labels(1)), 19)
        self.assertEqual(len(bundle.expected_labels(2)), 36)
        self.assertEqual(len(bundle.expected_labels(3)), 25)
        self.assertEqual(len(bundle.expected_labels(4)), 21)
        self.assertEqual(len(bundle.expected_labels(5)), 18)
        self.assertEqual(bundle.expected_labels(3)[:11], [
            "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "B1"
        ])
        self.assertEqual(bundle.expected_labels(5)[:6], ["A1", "A2", "A3", "45", "A5", "A6"])

    def test_canonical_label_corrects_only_the_45_typo(self):
        self.assertEqual(bundle.canonical_label(5, "45"), "A4")
        self.assertEqual(bundle.canonical_label(5, "A5"), "A5")
        self.assertEqual(bundle.canonical_label(3, "45"), "45")

    def test_label_id_part_pads_numbers(self):
        self.assertEqual(bundle.label_id_part(1, "Q1"), "Q01")
        self.assertEqual(bundle.label_id_part(3, "A10"), "A10")
        self.assertEqual(bundle.label_id_part(4, "1"), "01")
        self.assertEqual(bundle.label_id_part(5, "45"), "A04")

    def test_bundle_text_has_exactly_17_pages(self):
        text = bundle.read_text(BUNDLE_PATH)
        pages = text.split("\f")
        if pages and pages[-1] == "":
            pages.pop()
        self.assertEqual(len(pages), 17)

    def test_wrong_page_count_is_rejected(self):
        text = bundle.read_text(BUNDLE_PATH).replace("\f", "", 1)
        with self.assertRaises(ValueError):
            bundle.build_rows(text)


class ValidationChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = bundle.generate_rows(BUNDLE_PATH)

    def test_clean_rows_have_no_problems(self):
        self.assertEqual(bundle.validate_rows(self.rows), [])

    def test_validate_flags_assignment_count_drift(self):
        rows = [dict(row) for row in self.rows]
        rows.pop()
        problems = bundle.validate_rows(rows)
        self.assertTrue(any("total item count" in p for p in problems))
        self.assertTrue(any("assignment 5" in p for p in problems))

    def test_validate_flags_duplicate_id(self):
        rows = [dict(row) for row in self.rows]
        rows[-1]["item_id"] = rows[0]["item_id"]
        problems = bundle.validate_rows(rows)
        self.assertTrue(any("duplicate item_id" in p for p in problems))

    def test_validate_flags_page_out_of_range(self):
        rows = [dict(row) for row in self.rows]
        rows[0]["page_end"] = 99
        problems = bundle.validate_rows(rows)
        self.assertTrue(any("page_end out of range" in p for p in problems))

    def test_validate_flags_empty_summary(self):
        rows = [dict(row) for row in self.rows]
        rows[0]["summary"] = ""
        problems = bundle.validate_rows(rows)
        self.assertTrue(any("empty summary" in p for p in problems))

    def test_validate_flags_unearned_structural_candidate(self):
        rows = [dict(row) for row in self.rows]
        target = [r for r in rows if r["assignment"] == 3][0]
        target["structural_family_candidate"] = "memory_based"
        problems = bundle.validate_rows(rows)
        self.assertTrue(
            any("unearned structural candidate" in p for p in problems)
        )

    def test_validate_flags_unearned_match_status(self):
        rows = [dict(row) for row in self.rows]
        rows[0]["match_status"] = "matched"
        problems = bundle.validate_rows(rows)
        self.assertTrue(any("non-honest match_status" in p for p in problems))

    def test_validate_flags_unearned_2024_locator(self):
        rows = [dict(row) for row in self.rows]
        rows[0]["matched_2024_locator"] = "assignment-2024-25-1-Q01"
        problems = bundle.validate_rows(rows)
        self.assertTrue(any("unearned 2024 locator" in p for p in problems))


class CheckChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = bundle.generate_rows(BUNDLE_PATH)

    def test_clean_ledger_has_no_problems(self):
        self.assertEqual(
            bundle.check_ledger(bundle.render_csv(self.rows), self.rows), []
        )

    def test_check_detects_stale_generated_content(self):
        text = bundle.render_csv(self.rows).replace(
            "text_extracted", "stale_state", 1
        )
        problems = bundle.check_ledger(text, self.rows)
        self.assertTrue(any("stale generated content" in p for p in problems))

    def test_check_detects_header_mismatch(self):
        text = bundle.render_csv(self.rows).replace("item_label", "label", 1)
        problems = bundle.check_ledger(text, self.rows)
        self.assertTrue(any("header mismatch" in p for p in problems))

    def test_check_detects_row_count_mismatch(self):
        lines = bundle.render_csv(self.rows).splitlines(keepends=True)
        problems = bundle.check_ledger("".join(lines[:-1]), self.rows)
        self.assertTrue(any("row count mismatch" in p for p in problems))

    def test_check_detects_duplicate_id(self):
        lines = bundle.render_csv(self.rows).splitlines(keepends=True)
        problems = bundle.check_ledger("".join(lines + [lines[1]]), self.rows)
        self.assertTrue(any("duplicate item_id" in p for p in problems))

    def test_check_detects_order_mismatch(self):
        lines = bundle.render_csv(self.rows).splitlines(keepends=True)
        lines[1], lines[2] = lines[2], lines[1]
        problems = bundle.check_ledger("".join(lines), self.rows)
        self.assertTrue(any("row order mismatch" in p for p in problems))

    def test_check_detects_empty_ledger(self):
        self.assertTrue(bundle.check_ledger("", self.rows))


class MainChecks(unittest.TestCase):
    def test_write_check_and_tamper(self):
        with tempfile.TemporaryDirectory(prefix="mas2001-bundle-") as tmp:
            out = pathlib.Path(tmp) / "assignment-bundle-ledger-20260916.csv"
            self.assertEqual(bundle.main(["--output", str(out)]), 0)
            self.assertTrue(out.is_file())
            self.assertEqual(
                len(out.read_text(encoding="utf-8").splitlines()), 120
            )
            self.assertEqual(bundle.main(["--check", "--output", str(out)]), 0)
            out.write_text(
                out.read_text(encoding="utf-8").replace(
                    "text_extracted", "stale_state", 1
                ),
                encoding="utf-8",
            )
            self.assertEqual(bundle.main(["--check", "--output", str(out)]), 1)

    def test_check_missing_ledger_exits_nonzero(self):
        with tempfile.TemporaryDirectory(prefix="mas2001-bundle-") as tmp:
            missing = pathlib.Path(tmp) / "absent.csv"
            self.assertEqual(bundle.main(["--check", "--output", str(missing)]), 1)

    def test_default_output_lives_under_reports_evidence(self):
        self.assertEqual(
            bundle.LEDGER_REL,
            pathlib.Path("reports")
            / "evidence"
            / "assignment-bundle-ledger-20260916.csv",
        )


class DeterminismAndDashChecks(unittest.TestCase):
    def test_render_is_byte_for_byte_repeatable(self):
        first = bundle.render_csv(bundle.generate_rows(BUNDLE_PATH))
        second = bundle.render_csv(bundle.generate_rows(BUNDLE_PATH))
        self.assertEqual(first, second)

    def test_on_disk_ledger_matches_a_fresh_build(self):
        self.assertTrue(LEDGER_PATH.is_file())
        problems = bundle.check_ledger(
            LEDGER_PATH.read_text(encoding="utf-8"),
            bundle.generate_rows(BUNDLE_PATH),
        )
        self.assertEqual(problems, [])

    def test_csv_has_no_em_or_en_dash(self):
        text = bundle.render_csv(bundle.generate_rows(BUNDLE_PATH))
        self.assertNotIn("\u2014", text)
        self.assertNotIn("\u2013", text)

    def test_module_source_has_no_em_or_en_dash(self):
        text = (REPO / "scripts" / "build_assignment_bundle_ledger.py").read_text(
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
