import unittest
from Context import DynamicProgramming
from Context import run_cases


class TestDP(unittest.TestCase):

    def setUp(self):
        ...

    def tearDown(self):
        ...

    def test_weighted_scheduling(self):
        cases = [([[(1, 2, 1), (1, 4, 0), (2, 5, 2),
                    (3, 4, 1), (3, 5, 2), (4, 5, 2), (4, 6, 2)]], 3)]
        run_cases(self, cases, DynamicProgramming.weighted_scheduling)
