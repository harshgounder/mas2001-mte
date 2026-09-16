"""Unit tests for scripts/build_corpus_page_ledger.py.

Everything runs on temporary fixtures; pdftotext is mocked so no real PDF is read
and nothing is written outside the temp directory. Run with:

    python3 -B tests/test_corpus_page_ledger.py -v
"""

import json
import pathlib
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.dont_write_bytecode = True
if str(REPO / "scripts") not in sys.path:
    sys.path.insert(0, str(REPO / "scripts"))
import build_corpus_page_ledger as ledger


def completed(text):
    if isinstance(text, str):
        text = text.encode("utf-8")
    return subprocess.CompletedProcess(args=[], returncode=0, stdout=text, stderr=b"")


def fake_runner(mapping):
    """A subprocess.run stand-in keyed on the PDF path in the pdftotext command."""

    def run(cmd, **kwargs):
        key = str(cmd[-2])
        if key not in mapping:
            raise AssertionError("unexpected pdftotext call: %r" % (cmd,))
        value = mapping[key]
        if isinstance(value, Exception):
            raise value
        if value is None:
            return subprocess.CompletedProcess(args=cmd, returncode=1, stdout=b"", stderr=b"")
        return completed(value)

    return run


def make_source(label, pdf, pages, topic="topic", sha="deadbeef"):
    return {
        "label": label,
        "path": str(pdf),
        "pages": str(pages),
        "topic": topic,
        "sha256": sha,
    }


class LedgerTestBase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory(prefix="mas2001-ledger-")
        self.root = pathlib.Path(self._tmp.name)
        (self.root / "work").mkdir(parents=True, exist_ok=True)
        (self.root / "md").mkdir(exist_ok=True)

    def tearDown(self):
        self._tmp.cleanup()

    def make_pdf(self, name="deck.pdf"):
        pdf = self.root / name
        pdf.write_bytes(b"%PDF-1.4 stub\n")
        return pdf

    def write_md(self, label, page, text):
        path = self.root / "md" / label / ("p%03d.md" % page)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def write_manifest(self, records):
        path = self.root / "work" / "manifest.jsonl"
        with open(path, "w", encoding="utf-8") as handle:
            for record in records:
                handle.write(json.dumps(record) + "\n")
        return path


class HeaderAndShapeChecks(LedgerTestBase):
    def test_header_is_exact_and_ordered(self):
        expected = [
            "source_index",
            "label",
            "page",
            "declared_pages",
            "source_path",
            "source_sha256",
            "topic",
            "latest_manifest_status",
            "latest_model",
            "md_path",
            "md_exists",
            "md_chars",
            "png_exists",
            "raw_text_chars",
            "raw_text_sha256",
            "block_marker_count",
            "record_state",
        ]
        self.assertEqual(ledger.FIELDS, expected)
        self.assertEqual(ledger.render_csv([]).splitlines()[0], ",".join(expected))

    def test_exact_row_count_for_declared_pages(self):
        pdf_a = self.make_pdf("a.pdf")
        pdf_b = self.make_pdf("b.pdf")
        sources = [make_source("a", pdf_a, 2), make_source("b", pdf_b, 3)]
        mapping = {str(pdf_a): "a1\fa2\f", str(pdf_b): "b1\fb2\fb3\f"}
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner(mapping)) as run:
            rows = ledger.build_rows(sources, {}, self.root)
        run.assert_called()
        self.assertEqual(len(rows), 5)
        self.assertEqual([row["source_index"] for row in rows], [1, 1, 2, 2, 2])
        keys = [(row["source_index"], row["label"], row["page"]) for row in rows]
        self.assertEqual(sorted(keys), sorted(set(keys)))

    def test_no_page_gaps_per_source(self):
        pdf = self.make_pdf()
        source = make_source("deck", pdf, 4)
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner({str(pdf): "p1\fp2\fp3\fp4\f"})):
            rows = ledger.build_rows([source], {}, self.root)
        pages_by_label = {}
        for row in rows:
            pages_by_label.setdefault(row["label"], []).append(row["page"])
        self.assertEqual(pages_by_label, {"deck": [1, 2, 3, 4]})
        self.assertEqual(rows[-1]["page"], 4)

    def test_declared_columns_track_sources_yaml(self):
        pdf = self.make_pdf()
        source = make_source("deck", pdf, 2, topic="Discrete distributions", sha="abc123")
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner({str(pdf): "one\ftwo\f"})):
            rows = ledger.build_rows([source], {}, self.root)
        for row in rows:
            self.assertEqual(row["declared_pages"], 2)
            self.assertEqual(row["topic"], "Discrete distributions")
            self.assertEqual(row["source_sha256"], "abc123")
            self.assertEqual(row["source_path"], str(pdf))


class PageMappingChecks(LedgerTestBase):
    def test_form_feed_maps_pages_without_off_by_one(self):
        pdf = self.make_pdf()
        source = make_source("deck", pdf, 3)
        text = "ALPHA\n\fBRAVO\n\fCHARLIE\n\f"
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner({str(pdf): text})) as run:
            rows = ledger.build_rows([source], {}, self.root)
        run.assert_called_once()
        self.assertEqual([row["page"] for row in rows], [1, 2, 3])
        self.assertEqual(rows[0]["raw_text_chars"], len("ALPHA\n"))
        self.assertEqual(rows[0]["raw_text_sha256"], ledger.sha256_text("ALPHA\n"))
        self.assertEqual(rows[1]["raw_text_sha256"], ledger.sha256_text("BRAVO\n"))
        self.assertEqual(rows[2]["raw_text_sha256"], ledger.sha256_text("CHARLIE\n"))
        self.assertEqual([row["record_state"] for row in rows], ["pending"] * 3)

    def test_trailing_form_feed_makes_no_phantom_page(self):
        pdf = self.make_pdf()
        source = make_source("deck", pdf, 2)
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner({str(pdf): "ONE\fTWO\f"})):
            rows = ledger.build_rows([source], {}, self.root)
        self.assertEqual(len(rows), 2)
        self.assertNotIn("source_page_count_mismatch", [row["record_state"] for row in rows])

    def test_missing_trailing_form_feed_still_maps_last_page(self):
        pdf = self.make_pdf()
        source = make_source("deck", pdf, 2)
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner({str(pdf): "ONE\fTWO"})):
            rows = ledger.build_rows([source], {}, self.root)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[1]["raw_text_sha256"], ledger.sha256_text("TWO"))
        self.assertEqual(rows[1]["record_state"], "pending")

    def test_empty_page_keeps_its_slot(self):
        pdf = self.make_pdf()
        source = make_source("deck", pdf, 3)
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner({str(pdf): "ONE\f\fTHREE\f"})):
            rows = ledger.build_rows([source], {}, self.root)
        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[1]["raw_text_chars"], 0)
        self.assertEqual(rows[1]["raw_text_sha256"], "")
        self.assertEqual(rows[2]["raw_text_sha256"], ledger.sha256_text("THREE"))

    def test_pdftotext_runs_once_per_pdf(self):
        pdf = self.make_pdf()
        source = make_source("deck", pdf, 5)
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner({str(pdf): "a\fb\fc\fd\fe\f"})) as run:
            ledger.build_rows([source], {}, self.root)
        self.assertEqual(run.call_count, 1)


class ManifestChecks(LedgerTestBase):
    def test_last_manifest_row_wins(self):
        pdf = self.make_pdf()
        source = make_source("deck", pdf, 1)
        self.write_manifest(
            [
                {"label": "deck", "page": 1, "status": "error", "model": "first"},
                {"label": "deck", "page": 1, "status": "ok", "model": "second"},
            ]
        )
        latest = ledger.parse_manifest_latest(self.root / "work" / "manifest.jsonl")
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner({str(pdf): "one\f"})):
            rows = ledger.build_rows([source], latest, self.root)
        self.assertEqual(rows[0]["latest_manifest_status"], "ok")
        self.assertEqual(rows[0]["latest_model"], "second")

    def test_last_manifest_row_wins_in_reverse_order(self):
        pdf = self.make_pdf()
        source = make_source("deck", pdf, 1)
        self.write_manifest(
            [
                {"label": "deck", "page": 1, "status": "ok", "model": "first"},
                {"label": "deck", "page": 1, "status": "truncated", "model": "second"},
            ]
        )
        latest = ledger.parse_manifest_latest(self.root / "work" / "manifest.jsonl")
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner({str(pdf): "one\f"})):
            rows = ledger.build_rows([source], latest, self.root)
        self.assertEqual(rows[0]["latest_manifest_status"], "truncated")
        self.assertEqual(rows[0]["latest_model"], "second")

    def test_manifest_missing_leaves_status_blank(self):
        pdf = self.make_pdf()
        source = make_source("deck", pdf, 1)
        latest = ledger.parse_manifest_latest(self.root / "work" / "manifest.jsonl")
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner({str(pdf): "one\f"})):
            rows = ledger.build_rows([source], latest, self.root)
        self.assertEqual(rows[0]["latest_manifest_status"], "")
        self.assertEqual(rows[0]["latest_model"], "")


class RecordStateChecks(LedgerTestBase):
    def test_nonempty_markdown_is_converted(self):
        pdf = self.make_pdf()
        source = make_source("deck", pdf, 2)
        self.write_md("deck", 1, "some text\n")
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner({str(pdf): "one\ftwo\f"})):
            rows = ledger.build_rows([source], {}, self.root)
        self.assertEqual(rows[0]["record_state"], "converted")
        self.assertTrue(rows[0]["md_exists"])
        self.assertEqual(rows[0]["md_chars"], len("some text\n"))
        self.assertEqual(rows[1]["record_state"], "pending")

    def test_empty_markdown_is_pending(self):
        pdf = self.make_pdf()
        source = make_source("deck", pdf, 1)
        self.write_md("deck", 1, "")
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner({str(pdf): "one\f"})):
            rows = ledger.build_rows([source], {}, self.root)
        self.assertTrue(rows[0]["md_exists"])
        self.assertEqual(rows[0]["md_chars"], 0)
        self.assertEqual(rows[0]["record_state"], "pending")

    def test_missing_source_does_not_shell_out(self):
        source = make_source("gone", self.root / "nope.pdf", 2)
        with patch.object(ledger.subprocess, "run") as run:
            rows = ledger.build_rows([source], {}, self.root)
        run.assert_not_called()
        self.assertEqual(len(rows), 2)
        self.assertEqual([row["record_state"] for row in rows], ["missing_source", "missing_source"])
        self.assertEqual(rows[0]["raw_text_sha256"], "")

    def test_page_count_mismatch_flags_all_declared_pages(self):
        pdf = self.make_pdf()
        source = make_source("deck", pdf, 3)
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner({str(pdf): "only-one\f"})):
            rows = ledger.build_rows([source], {}, self.root)
        self.assertEqual(len(rows), 3)
        self.assertEqual(
            [row["record_state"] for row in rows],
            ["source_page_count_mismatch"] * 3,
        )
        self.assertEqual(rows[0]["raw_text_sha256"], ledger.sha256_text("only-one"))
        self.assertEqual(rows[2]["raw_text_sha256"], "")

    def test_pdftotext_failure_is_mismatch(self):
        pdf = self.make_pdf()
        source = make_source("deck", pdf, 2)
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner({str(pdf): None})):
            rows = ledger.build_rows([source], {}, self.root)
        self.assertEqual(
            [row["record_state"] for row in rows],
            ["source_page_count_mismatch"] * 2,
        )

    def test_png_presence_is_reported(self):
        pdf = self.make_pdf()
        source = make_source("deck", pdf, 2)
        png = self.root / "work" / "pages" / "deck" / "p001.png"
        png.parent.mkdir(parents=True, exist_ok=True)
        png.write_bytes(b"png")
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner({str(pdf): "one\ftwo\f"})):
            rows = ledger.build_rows([source], {}, self.root)
        self.assertTrue(rows[0]["png_exists"])
        self.assertFalse(rows[1]["png_exists"])


class BlockMarkerChecks(LedgerTestBase):
    def test_block_markers_count_question_shaped_lines_only(self):
        text = "Q1 find x\nExample 4 compute\nsome prose\nExercise 2 solve\nProblem 7\nqqq\n"
        self.assertEqual(ledger.count_block_markers(text), 4)

    def test_marker_count_is_not_a_final_count_field(self):
        pdf = self.make_pdf()
        source = make_source("deck", pdf, 1)
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner({str(pdf): "Q1 a\nQ2 b\n"})):
            rows = ledger.build_rows([source], {}, self.root)
        self.assertIn("block_marker_count", rows[0])
        self.assertEqual(rows[0]["block_marker_count"], 2)


class CheckChecks(LedgerTestBase):
    def _rows(self, pdf_text="one\ftwo\f", pages=2):
        pdf = self.make_pdf()
        source = make_source("deck", pdf, pages)
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner({str(pdf): pdf_text})):
            return ledger.build_rows([source], {}, self.root)

    def test_clean_ledger_has_no_problems(self):
        rows = self._rows()
        self.assertEqual(ledger.check_ledger(ledger.render_csv(rows), rows), [])

    def test_check_detects_stale_generated_content(self):
        rows = self._rows()
        stale = ledger.render_csv(rows).replace("pending", "converted")
        problems = ledger.check_ledger(stale, rows)
        self.assertTrue(any("stale generated content" in problem for problem in problems))

    def test_check_detects_header_mismatch(self):
        rows = self._rows()
        text = ledger.render_csv(rows).replace("block_marker_count", "block_count", 1)
        problems = ledger.check_ledger(text, rows)
        self.assertTrue(any("header mismatch" in problem for problem in problems))

    def test_check_detects_missing_row_and_page_gap(self):
        rows = self._rows()
        lines = ledger.render_csv(rows).splitlines(keepends=True)
        truncated = "".join(lines[:-1])
        problems = ledger.check_ledger(truncated, rows)
        self.assertTrue(any("row count mismatch" in problem for problem in problems))
        self.assertTrue(any("page gap" in problem for problem in problems))

    def test_check_detects_extra_key(self):
        rows = self._rows()
        lines = ledger.render_csv(rows).splitlines(keepends=True)
        extra = "1,ghost,9,9,/x,,, ,,md/ghost/p009.md,false,0,false,0,,0,pending\n"
        problems = ledger.check_ledger("".join(lines) + extra, rows)
        self.assertTrue(any("unexpected key" in problem for problem in problems))

    def test_check_detects_empty_ledger(self):
        rows = self._rows()
        self.assertTrue(ledger.check_ledger("", rows))


class DeterminismChecks(LedgerTestBase):
    def test_render_is_byte_for_byte_repeatable(self):
        pdf = self.make_pdf()
        source = make_source("deck", pdf, 3)
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner({str(pdf): "a\fb\fc\f"})):
            first = ledger.render_csv(ledger.build_rows([source], {}, self.root))
            second = ledger.render_csv(ledger.build_rows([source], {}, self.root))
        self.assertEqual(first, second)

    def test_output_has_no_em_or_en_dash(self):
        rows = self._rows_for_dash_test()
        text = ledger.render_csv(rows)
        self.assertNotIn("\u2014", text)
        self.assertNotIn("\u2013", text)

    def test_module_source_has_no_em_or_en_dash(self):
        text = (REPO / "scripts" / "build_corpus_page_ledger.py").read_text(encoding="utf-8")
        self.assertNotIn("\u2014", text)
        self.assertNotIn("\u2013", text)

    def _rows_for_dash_test(self):
        pdf = self.make_pdf()
        source = make_source("deck", pdf, 1, topic="plain topic")
        with patch.object(ledger.subprocess, "run", side_effect=fake_runner({str(pdf): "one\f"})):
            return ledger.build_rows([source], {}, self.root)


class ParserReuseChecks(unittest.TestCase):
    def test_parse_sources_matches_convert(self):
        sys.path.insert(0, str(REPO / "scripts"))
        import convert

        text = (
            "dpi: 110\n"
            "sources:\n"
            "  - label: x\n"
            '    path: "/tmp/x.pdf"\n'
            '    pages: 2\n'
            '    topic: "a: b # not a comment"\n'
        )
        self.assertEqual(ledger.parse_sources(text), convert.parse_sources_yaml(text))

    def test_fallback_parser_used_when_reuse_unavailable(self):
        text = "sources:\n  - label: y\n    pages: 1\n"
        with patch.object(ledger, "_reuse_parse_sources_yaml", return_value=None):
            scalars, sources = ledger.parse_sources(text)
        self.assertEqual(sources, [{"label": "y", "pages": "1"}])
        self.assertEqual(scalars, {})


class MainChecks(LedgerTestBase):
    def _sources_yaml(self, pdf):
        return (
            "dpi: 110\n"
            "sources:\n"
            "  - label: deck\n"
            '    path: "%s"\n'
            "    pages: 2\n"
            '    topic: "demo"\n'
            "    sha256: abc\n"
        ) % pdf

    def test_main_writes_and_check_passes_then_fails_on_tamper(self):
        pdf = self.make_pdf()
        (self.root / "sources.yaml").write_text(self._sources_yaml(pdf), encoding="utf-8")
        self.write_manifest([])
        out = self.root / "reports" / "evidence" / "corpus-page-ledger.csv"
        with patch.object(ledger, "ROOT", self.root), patch.object(
            ledger.subprocess, "run", side_effect=fake_runner({str(pdf): "one\ftwo\f"})
        ):
            self.assertEqual(ledger.main(["--output", str(out)]), 0)
            self.assertTrue(out.is_file())
            self.assertEqual(ledger.main(["--check", "--output", str(out)]), 0)
            out.write_text(
                out.read_text(encoding="utf-8").replace("pending", "converted"),
                encoding="utf-8",
            )
            self.assertEqual(ledger.main(["--check", "--output", str(out)]), 1)

    def test_check_missing_ledger_exits_nonzero(self):
        pdf = self.make_pdf()
        (self.root / "sources.yaml").write_text(self._sources_yaml(pdf), encoding="utf-8")
        self.write_manifest([])
        out = self.root / "reports" / "evidence" / "absent.csv"
        with patch.object(ledger, "ROOT", self.root), patch.object(
            ledger.subprocess, "run", side_effect=fake_runner({str(pdf): "one\ftwo\f"})
        ):
            self.assertEqual(ledger.main(["--check", "--output", str(out)]), 1)

    def test_default_output_lives_under_reports_evidence(self):
        pdf = self.make_pdf()
        (self.root / "sources.yaml").write_text(self._sources_yaml(pdf), encoding="utf-8")
        self.write_manifest([])
        with patch.object(ledger, "ROOT", self.root), patch.object(
            ledger.subprocess, "run", side_effect=fake_runner({str(pdf): "one\ftwo\f"})
        ):
            self.assertEqual(ledger.main([]), 0)
        expected = self.root / "reports" / "evidence" / "corpus-page-ledger.csv"
        self.assertTrue(expected.is_file())
        header = expected.read_text(encoding="utf-8").splitlines()[0]
        self.assertEqual(header, ",".join(ledger.FIELDS))


if __name__ == "__main__":
    unittest.main()
