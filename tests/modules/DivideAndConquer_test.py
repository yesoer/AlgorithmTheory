import unittest
from Context import DivideAndConquer
from Context import run_cases


class TestDC(unittest.TestCase):

    def setUp(self):
        ...

    def tearDown(self):
        ...

    def test_inversions(self):
        cases = [([[2, 3, 4, 6, 5]], 1)]
        run_cases(self, cases, DivideAndConquer.inversions)

    def test_shortest_distance_wrapper(self):
        cases = [([[(1, 3), (1, 2), (3, 1), (2, 2), (5, 6)]], 1.0)]
        run_cases(self, cases, DivideAndConquer.shortest_distance_wrapper)
