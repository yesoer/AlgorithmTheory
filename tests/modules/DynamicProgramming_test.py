import unittest
from Context import DynamicProgramming
from Context import run_cases


class TestDP(unittest.TestCase):

    def setUp(self):
        self.weighted_intervals1 = [(1, 2, 1), (1, 4, 0), (2, 5, 2), (3, 4, 1), 
                                    (3, 5, 2), (4, 5, 2), (4, 6, 2)]
        self.weighted_intervals2 = [(2, 3, 2), (3, 8, 4), (1, 10, 8), (2, 5, 3), 
                                    (8, 9, 3)]
        self.weighted_intervals3 = [(1, 3, 3), (3, 8, 4), (2, 5, 3), (0, 3, 3), (0, 2, 1)]

    def tearDown(self):
        ...

    def test_weighted_scheduling(self):
        cases = [
                ([self.weighted_intervals1], 4),
                ([self.weighted_intervals2], 9),
                ([self.weighted_intervals3], 7)
                ]
        run_cases(self, cases, DynamicProgramming.weighted_scheduling)
