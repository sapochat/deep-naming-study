import tempfile, unittest
from pathlib import Path
from deep_naming_study.study import scaffold_study, validate_brief, validate_study

BRIEF = {"project":"Test","purpose":"Find a durable name","audience":"Readers","voice":"Dry","source_inspiration":"Public offices","mechanism":"Quiet institutional judgment","dead_lanes":["labs"],"rubric":["range","sound","durability"]}

class StudyTests(unittest.TestCase):
    def test_scaffold(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "study"; scaffold_study(BRIEF, root)
            self.assertEqual(validate_study(root), [])
    def test_bad_brief(self):
        self.assertTrue(validate_brief({"project":"Thin","rubric":["one"]}))
    def test_missing_stage(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "study"; scaffold_study(BRIEF, root)
            (root / "04-blind-critics" / "README.md").unlink()
            (root / "04-blind-critics").rmdir()
            self.assertTrue(any("04-blind-critics" in e for e in validate_study(root)))

if __name__ == "__main__": unittest.main()
