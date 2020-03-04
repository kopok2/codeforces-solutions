import unittest
from unittest.mock import patch

from cdf_479A import CodeforcesTask479ASolution


class TestCDF479A(unittest.TestCase):
    def test_479A_acceptance_1(self):
        mock_input = ['1', '2', '3']
        expected = '9'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask479ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_479A_acceptance_2(self):
        mock_input = ['2', '10', '3']
        expected = '60'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask479ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
