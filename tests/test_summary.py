import unittest

from examples.decision_summary import summarize


class SummaryTests(unittest.TestCase):
    def record(self, capability, learning):
        return {"name": "fictional_test", "capability_checks_passed": capability,
                "learning_evidence_supports_use": learning}

    def test_admission_does_not_imply_training_use(self):
        result = summarize(self.record(True, False))
        self.assertEqual(result["capability_admission"], "admitted")
        self.assertEqual(result["training_use"], "not_supported")
        self.assertTrue(result["fictional"])

    def test_missing_evidence_is_not_a_failure(self):
        self.assertEqual(summarize(self.record(None, None))["capability_admission"],
                         "pending")
        self.assertEqual(summarize(self.record(True, None))["training_use"], "pending")

    def test_rejected_capability_is_not_eligible(self):
        self.assertEqual(summarize(self.record(False, None))["training_use"],
                         "not_eligible")

    def test_inconsistent_promotion_is_rejected(self):
        for capability in (False, None):
            with self.subTest(capability=capability), self.assertRaises(ValueError):
                summarize(self.record(capability, True))

    def test_strings_and_numbers_cannot_impersonate_decisions(self):
        for value in ("false", 0, 1, [], {}):
            with self.subTest(value=value), self.assertRaises(ValueError):
                summarize(self.record(value, None))

    def test_supported_use_is_separate(self):
        self.assertEqual(summarize(self.record(True, True))["training_use"], "supported")


if __name__ == "__main__":
    unittest.main()
