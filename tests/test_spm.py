import io
import unittest
from contextlib import redirect_stdout

from spm import SemioticPerpetuum, main


class TestSemioticRuntime(unittest.TestCase):
    def test_runtime_feedback_progression(self) -> None:
        spm = SemioticPerpetuum()
        seeds = spm.create_seed_signs(["proof", "thought"])
        chains = spm.run_runtime(seed_signs=seeds, cycles=3)

        self.assertEqual(len(chains), 3)
        self.assertEqual(chains[0].cycle_count, 1)
        self.assertEqual(chains[1].cycle_count, 2)
        self.assertEqual(chains[2].cycle_count, 3)
        self.assertEqual(chains[0].total_interpretants, 2)
        self.assertEqual(chains[1].total_interpretants, 2)
        self.assertEqual(chains[2].total_interpretants, 2)
        self.assertGreaterEqual(len(spm.signs), 8)

    def test_start_command_runs(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main(["start", "--seed", "alpha,beta", "--cycles", "2"])

        text = output.getvalue()
        self.assertEqual(exit_code, 0)
        self.assertIn("ORION Semiotic Perpetuum Runtime", text)
        self.assertIn("Cycle 1", text)
        self.assertIn("Cycle 2", text)


if __name__ == "__main__":
    unittest.main()
