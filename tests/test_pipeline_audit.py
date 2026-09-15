"""Independent audit checks. No network calls or edits to the study repo.

Run with: python3 -B tests/test_pipeline_audit.py -v  (from the repo root)
Failures express desired behavior, not patches to the implementation.

This is the in-repo working copy of the peer audit harness written by codex CLI on
15 Sep 2026. The original lives at ~/mas2001-mte-audit-v1/test_audit.py and is kept as
the pristine reference. This copy differs from it in exactly one way: EVIDENCE is read
from the MTE_EVIDENCE environment variable, defaulting to the original directory, so
running it from the repo does not scatter generated files. Keep the assertions identical.
"""
import contextlib
import hashlib
import os
import io
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO = Path('/home/liebert511/mas2001-mte')
EVIDENCE = Path(os.environ.get('MTE_EVIDENCE', '/home/liebert511/mas2001-mte-audit-v1'))
sys.dont_write_bytecode = True
sys.path.insert(0, str(REPO / 'scripts'))
import convert
import assemble
import audit_conversion as audit


class CorpusChecks(unittest.TestCase):
    def test_source_identity_and_inventory(self):
        _, sources = convert.load_config()
        rows = []
        texts = EVIDENCE / 'text'
        texts.mkdir(exist_ok=True)
        for source in sources:
            pdf = Path(source['path'])
            digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
            count = convert.pdfinfo_pages(pdf)
            proc = subprocess.run(['pdftotext', '-layout', str(pdf), '-'], capture_output=True, check=True)
            text = proc.stdout.decode('utf-8', 'replace')
            (texts / (source['label'] + '.txt')).write_text(text)
            converted = sorted((REPO / 'md' / source['label']).glob('p*.md'))
            rows.append(dict(label=source['label'], path=str(pdf), pages=count,
                             sha256=digest, text_bytes=len(proc.stdout),
                             converted_pages=len(converted),
                             empty_text_pages=sum(not page.strip() for page in text.split('\f')[:count])))
            with self.subTest(label=source['label']):
                self.assertEqual(digest, source['sha256'])
                self.assertEqual(count, int(source['pages']))
        (EVIDENCE / 'source-inventory.json').write_text(json.dumps(rows, indent=2) + '\n')
        print('INVENTORY', json.dumps(dict(sources=len(rows), pages=sum(r['pages'] for r in rows), converted=sum(r['converted_pages'] for r in rows))))

    def test_assembled_documents_match_page_files(self):
        index = json.loads((REPO / 'md/INDEX.json').read_text())
        for label in index:
            bodies = [assemble.fix_dashes(p.read_text().strip())[0] for p in sorted((REPO / 'md' / label).glob('p*.md'))]
            expected = '# %s\n\n%s\n' % (label, '\n\n---\n\n'.join(b for b in bodies if b))
            with self.subTest(label=label):
                self.assertEqual((REPO / 'md' / (label + '.md')).read_text(), expected)

    def test_manifest_images_and_pages(self):
        rows = [json.loads(line) for line in (REPO / 'work/manifest.jsonl').read_text().splitlines() if line.strip()]
        latest = {(r['label'], r['page']): r for r in rows}
        missing_images = []
        for (label, page), row in latest.items():
            md = REPO / 'md' / label / ('p%03d.md' % page)
            png = REPO / 'work/pages' / label / ('p%03d.png' % page)
            with self.subTest(label=label, page=page):
                self.assertTrue(md.is_file())
                self.assertEqual(row['status'], 'ok')
                if png.is_file():
                    self.assertEqual(hashlib.sha256(png.read_bytes()).hexdigest(), row['png_sha256'])
                else:
                    missing_images.append(str(png))
        print('MANIFEST', json.dumps(dict(rows=len(rows), unique=len(latest), missing_images=len(missing_images))))
        self.assertFalse(missing_images)


class MathematicalChecks(unittest.TestCase):
    def test_mock_T4_is_not_smallest_variance(self):
        variances = [1, 1/2, 1/3, 3/4]
        self.assertEqual(min(range(4), key=variances.__getitem__), 2)
        print('MOCK_VARIANCES', variances)

    def test_fixed_three_observation_estimator_is_not_consistent(self):
        # IID N(mu,1) supplies a counterexample for every n >= 3.
        probability_outside = math.erfc(math.sqrt(3/2))
        self.assertGreater(probability_outside, 0.08)
        print('FIXED_T3_P_ABSOLUTE_ERROR_GT_1', probability_outside)

    def test_key_numerics(self):
        phi = lambda x: (1 + math.erf(x/math.sqrt(2))) / 2
        k = (-12 + math.sqrt(184)) / 20
        values = dict(exp_conditional=(1-math.exp(-.5))/(1-math.exp(-1)),
                      impurity=phi((3.8-4)/(1.5/math.sqrt(50)))-phi((3.5-4)/(1.5/math.sqrt(50))),
                      variant_k=k, variant_p_gt6=7*k*k+k, variant_p_ge6=9*k*k+k,
                      variant_p_lt6=11*k+k*k,
                      battery_sd=math.sqrt(12.85-3.45**2),
                      binomial_1=15*.08*.92**14, binomial_ge1=1-.92**15)
        self.assertAlmostEqual(values['exp_conditional'], .6224593312018546)
        self.assertAlmostEqual(12*k+10*k*k, 1)
        print('NUMERIC_RECHECK', json.dumps(values, sort_keys=True))


class PipelineChecks(unittest.TestCase):
    def test_nonzero_vision_exit_is_not_accepted(self):
        with patch.object(convert, 'call_vision', return_value=(1, 'HTTP 402: exhausted', 'failure')), patch.object(convert.time, 'sleep'):
            text, status, attempts, _ = convert.transcribe(Path('/unused'), 'prompt', 'test', 100)
        print('NONZERO_EXIT', dict(text=text, status=status, attempts=attempts))
        self.assertNotEqual(status, 'ok')

    def test_failed_source_makes_dry_run_fail(self):
        config = dict(dpi=110, max_tokens=100, workers=1, page_dir='work/pages', out_dir='md')
        with patch.object(convert, 'load_config', return_value=(config, [dict(label='missing', path='/does-not-exist.pdf', pages='1')])):
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                result = convert.main(['--dry-run'])
        self.assertNotEqual(result, 0)

    def test_empty_second_reading_cannot_pass(self):
        self.assertLess(audit.numeric_agreement('## Estimation\nNo numeric content.', ''), .8)

    def test_fidelity_detects_sign_reversal(self):
        self.assertLess(audit.numeric_agreement('Mean = -3, variance = 4', 'Mean = +3, variance = 4'), .8)

    def test_fidelity_model_change_invalidates_cached_reading(self):
        with tempfile.TemporaryDirectory(prefix='mas2001-fidelity-test-') as tmp:
            root = Path(tmp)
            primary = root / 'md/deck/p001.md'
            second = root / 'fidelity/deck/p001.md'
            primary.parent.mkdir(parents=True)
            second.parent.mkdir(parents=True)
            primary.write_text('## Mean\n3\n')
            second.write_text('## Cached from old model\n3\n')
            args = audit.parse_args(['--fidelity', '1', '--fidelity-model', 'new-reader'])
            with patch.object(audit, 'MD_ROOT', root/'md'), patch.object(audit, 'FIDELITY_ROOT', root/'fidelity'), patch.object(audit, 'FIDELITY_MD', root/'result.md'), patch.object(audit, 'call_vision', return_value='## New reading\n3\n') as call:
                with contextlib.redirect_stdout(io.StringIO()):
                    audit.run_fidelity(args)
            self.assertTrue(call.called)

    def test_truncated_page_is_not_permanently_done(self):
        with tempfile.TemporaryDirectory(prefix='mas2001-resume-test-') as tmp:
            root = Path(tmp)
            md = root / 'md/deck/p001.md'
            md.parent.mkdir(parents=True)
            md.write_text('## Incomplete formula\n')
            with patch.object(convert, 'OUT', root/'md', create=True), patch.object(convert, 'PAGEROOT', root/'pages', create=True), patch.object(convert, 'MANIFEST', root/'manifest.jsonl', create=True):
                result = convert.process_page('deck', 1, Path('/unused.pdf'), 110, 'prompt', 'test', 100, False)
            self.assertTrue(result['ran'])


class ResumeRuleChecks(unittest.TestCase):
    """G1: done is a non-empty md file AND a latest manifest record of ok."""

    def _setup(self, tmp, status_record):
        root = Path(tmp)
        md = root / 'md/deck/p001.md'
        md.parent.mkdir(parents=True)
        md.write_text('## Page\ncontent\n')
        manifest = root / 'manifest.jsonl'
        if status_record is not None:
            manifest.parent.mkdir(parents=True, exist_ok=True)
            manifest.write_text(json.dumps(status_record) + '\n')
        return root, manifest

    def _process(self, root, manifest):
        with patch.object(convert, 'OUT', root/'md', create=True), \
             patch.object(convert, 'PAGEROOT', root/'pages', create=True), \
             patch.object(convert, 'MANIFEST', manifest, create=True):
            return convert.process_page('deck', 1, Path('/unused.pdf'), 110, 'prompt', 'test', 100, False)

    def test_latest_record_truncated_means_pending(self):
        with tempfile.TemporaryDirectory(prefix='mas2001-resume-rule-') as tmp:
            record = dict(label='deck', page=1, status='truncated')
            root, manifest = self._setup(tmp, record)
            self.assertTrue(self._process(root, manifest)['ran'])

    def test_latest_record_ok_is_done(self):
        with tempfile.TemporaryDirectory(prefix='mas2001-resume-rule-') as tmp:
            record = dict(label='deck', page=1, status='ok')
            root, manifest = self._setup(tmp, record)
            self.assertFalse(self._process(root, manifest)['ran'])

    def test_latest_record_error_is_pending(self):
        with tempfile.TemporaryDirectory(prefix='mas2001-resume-rule-') as tmp:
            record = dict(label='deck', page=1, status='error')
            root, manifest = self._setup(tmp, record)
            self.assertTrue(self._process(root, manifest)['ran'])

    def test_no_record_at_all_is_pending(self):
        with tempfile.TemporaryDirectory(prefix='mas2001-resume-rule-') as tmp:
            root, manifest = self._setup(tmp, None)
            self.assertTrue(self._process(root, manifest)['ran'])

    def test_last_row_wins(self):
        with tempfile.TemporaryDirectory(prefix='mas2001-resume-rule-') as tmp:
            root, manifest = self._setup(tmp, dict(label='deck', page=1, status='truncated'))
            with open(manifest, 'a') as handle:
                handle.write(json.dumps(dict(label='deck', page=1, status='ok')) + '\n')
            self.assertFalse(self._process(root, manifest)['ran'])


class TranscribeExitChecks(unittest.TestCase):
    """G2: a nonzero vision exit must not be recorded as ok."""

    def test_exit_one_with_text_gets_distinct_status(self):
        with patch.object(convert, 'call_vision', return_value=(1, 'HTTP 402: exhausted', 'failure')), \
             patch.object(convert.time, 'sleep'):
            text, status, attempts, note = convert.transcribe(Path('/unused'), 'prompt', 'test', 100)
        self.assertEqual(status, 'exit_1')
        self.assertTrue(text)

    def test_exit_zero_still_ok(self):
        with patch.object(convert, 'call_vision', return_value=(0, '## Mean\n3\n', '')), \
             patch.object(convert.time, 'sleep'):
            _, status, _, _ = convert.transcribe(Path('/unused'), 'prompt', 'test', 100)
        self.assertEqual(status, 'ok')


class AgreementChecks(unittest.TestCase):
    """G3: empty second reading, signed numbers, and the no-numeric outcome."""

    def test_no_numeric_primary_is_not_perfect_agreement(self):
        agreement = audit.numeric_agreement('## Estimation\nNo numeric content.', '## Estimation\nAlso none.')
        self.assertEqual(agreement, 0.0)
        self.assertTrue(agreement.reason)

    def test_identical_numeric_readings_still_pass(self):
        primary = 'Mean = 3, SD = 1.5, n = 50'
        agreement = audit.numeric_agreement(primary, primary)
        self.assertEqual(agreement, 1.0)
        self.assertEqual(agreement.reason, '')

    def test_minus_is_a_sign_but_subtraction_is_not(self):
        self.assertEqual(audit.numeric_tokens('Mean = -3'), ['-3'])
        self.assertEqual(audit.numeric_tokens('Mean = +3'), ['3'])
        self.assertEqual(audit.numeric_tokens('3 - 4'), ['3', '4'])
        self.assertEqual(audit.numeric_tokens('x - 4'), ['4'])
        self.assertEqual(audit.numeric_tokens('alpha - 4'), ['4'])
        self.assertEqual(audit.numeric_tokens('-4 and 5'), ['-4', '5'])

    def test_empty_second_reading_returns_none_with_reason(self):
        agreement = audit.numeric_agreement('Mean = 3', '')
        self.assertEqual(agreement, 0.0)
        self.assertTrue(agreement.reason)

    def test_no_second_reading_verdict_in_fidelity(self):
        with tempfile.TemporaryDirectory(prefix='mas2001-fidelity-empty-') as tmp:
            root = Path(tmp)
            primary = root / 'md/deck/p001.md'
            primary.parent.mkdir(parents=True)
            primary.write_text('## Mean\n3\n')
            args = audit.parse_args(['--fidelity', '1', '--fidelity-model', 'new-reader'])
            with patch.object(audit, 'MD_ROOT', root/'md'), \
                 patch.object(audit, 'FIDELITY_ROOT', root/'fidelity'), \
                 patch.object(audit, 'FIDELITY_MD', root/'result.md'), \
                 patch.object(audit, 'call_vision', return_value='   ') as call:
                with contextlib.redirect_stdout(io.StringIO()):
                    audit.run_fidelity(args)
            self.assertTrue(call.called)
            table = (root / 'result.md').read_text()
            self.assertNotIn('| PASS |', table)
            self.assertIn('NO_SECOND_READING', table)


class FidelityStampChecks(unittest.TestCase):
    """G4: the cached second reading is tied to the model that produced it."""

    def _run(self, root, model, vision_return):
        args = audit.parse_args(['--fidelity', '1', '--fidelity-model', model])
        with patch.object(audit, 'MD_ROOT', root/'md'), \
             patch.object(audit, 'FIDELITY_ROOT', root/'fidelity'), \
             patch.object(audit, 'FIDELITY_MD', root/'result.md'), \
             patch.object(audit, 'call_vision', return_value=vision_return) as call:
            with contextlib.redirect_stdout(io.StringIO()):
                audit.run_fidelity(args)
        return call

    def test_same_model_uses_cache_without_calling_vision(self):
        with tempfile.TemporaryDirectory(prefix='mas2001-stamp-same-') as tmp:
            root = Path(tmp)
            primary = root / 'md/deck/p001.md'
            second = root / 'fidelity/deck/p001.md'
            primary.parent.mkdir(parents=True)
            second.parent.mkdir(parents=True)
            primary.write_text('## Mean\n3\n')
            second.write_text('## Cached\n3\n')
            (root / 'fidelity/deck/_model.json').write_text(json.dumps(dict(model='new-reader')) + '\n')
            call = self._run(root, 'new-reader', 'should not be used')
            self.assertFalse(call.called)
            self.assertEqual(second.read_text(), '## Cached\n3\n')

    def test_stamp_written_with_first_cached_page(self):
        with tempfile.TemporaryDirectory(prefix='mas2001-stamp-write-') as tmp:
            root = Path(tmp)
            primary = root / 'md/deck/p001.md'
            primary.parent.mkdir(parents=True)
            primary.write_text('## Mean\n3\n')
            self._run(root, 'new-reader', '## New reading\n3\n')
            stamp = json.loads((root / 'fidelity/deck/_model.json').read_text())
            self.assertEqual(stamp['model'], 'new-reader')
            self.assertIn('written', stamp)
            self.assertTrue((root / 'fidelity/deck/p001.md').is_file())


class DefaultModelChecks(unittest.TestCase):
    """G6: the standing directive of 15 Sep pins the vision defaults."""

    def test_defaults_are_glm(self):
        self.assertEqual(convert.DEFAULT_MODEL, 'glm-5.3-flash')
        self.assertEqual(audit.DEFAULT_FIDELITY_MODEL, 'glm-5.3-flash')


class RealRunSkipChecks(unittest.TestCase):
    """G5b: a real run ends nonzero when a source is skipped."""

    def test_failed_source_makes_real_run_fail(self):
        config = dict(dpi=110, max_tokens=100, workers=1, page_dir='work/pages', out_dir='md')
        sources = [dict(label='missing', path='/does-not-exist.pdf', pages='1')]
        with tempfile.TemporaryDirectory(prefix='mas2001-real-run-') as tmp:
            root = Path(tmp)
            (root / 'PROMPT.txt').write_text('prompt\n')
            with patch.object(convert, 'load_config', return_value=(config, sources)), \
                 patch.object(convert, 'ROOT', root), \
                 patch.object(convert.convert_test_harness, '_root', root), \
                 patch.object(convert.time, 'sleep'):
                buf_out, buf_err = io.StringIO(), io.StringIO()
                with contextlib.redirect_stdout(buf_out), contextlib.redirect_stderr(buf_err):
                    result = convert.main([])
        self.assertNotEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
