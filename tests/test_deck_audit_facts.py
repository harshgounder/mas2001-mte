"""Regression checks for high-risk facts corrected in the deck audit."""

import csv
import pathlib
import unittest


REPO = pathlib.Path(__file__).resolve().parent.parent


def read(relative_path):
    return (REPO / relative_path).read_text(encoding="utf-8")


class DeckAuditFacts(unittest.TestCase):
    def test_normal_table_pages_match_source_conversions(self):
        page_22 = read("md/ppt4-continuous-prob-dist/p022.md")
        page_23 = read("md/ppt4-continuous-prob-dist/p023.md")
        notes = read("deck/notes/07-uniform-normal-exponential.md")
        self.assertIn("cumulative probability", page_22)
        self.assertIn("P(0 < Z < z)", page_23)
        self.assertIn("TABLE 1 (p022, cumulative standard normal table)", notes)
        self.assertIn("TABLE 2 (p023, area from 0 to z)", notes)

    def test_estimator_expectation_keeps_each_coefficient(self):
        notes = read("deck/notes/09-estimation.md")
        self.assertIn("E(T3) = (λμ+μ+μ)/3", notes)
        self.assertNotIn("E(T3) = (λ/3)(μ+μ+μ)", notes)

    def test_impurity_precision_is_not_mislabeled(self):
        errata = read("reports/09-ERRATA.md")
        self.assertIn("0.4909 - 0.3264 = 0.1645", errata)
        self.assertIn("exact, no table rounding       0.16368", errata)
        self.assertIn("The slide's 0.1644 is not", errata)

    def test_chebyshev_source_event_is_preserved(self):
        notes = read("deck/notes/10-chebyshev-and-hidden.md")
        self.assertIn("P(-2<X<8)", notes)
        self.assertIn("P(-2<X<8) = P(|X-3|<5) >= 21/25", notes.replace("≥", ">="))

    def test_external_inventory_has_both_absent_palaniammal_titles(self):
        path = REPO / "reports/evidence/external-source-inventory-20260916.csv"
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        absent = {
            row["claimed_identity"]
            for row in rows
            if row["text_state"] == "absent"
        }
        self.assertIn("Palaniammal Probability and Random Variables", absent)
        self.assertIn("Palaniammal Probability and Random Processes", absent)

    def test_paper_inventory_separates_exams_and_schemes(self):
        index = read("deck/00-INDEX.md")
        self.assertIn("exam papers on disk                  9", index)
        self.assertIn("marking schemes on disk              2", index)


if __name__ == "__main__":
    unittest.main()
