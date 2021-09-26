import unittest
from Context import Greedy


class Greedy_test(unittest.TestCase):

    # uses testwrapper to execute various scenarios

    def setUp(self):
        ...

    def test_interval_scheduling(self):
        cases = [([(1, 3), (0, 2), (2, 5), (3, 6), (4, 6)], [(0, 2), (2, 5)])]
        self.run_cases(cases, Greedy.interval_scheduling)

    def test_interval_partitioning(self):
        cases = [([(1, 3), (0, 2), (2, 5), (3, 6), (4, 6)], [
                  [(0, 2), (2, 5)], [(1, 3), (3, 6)], [(2, 5)], [(3, 6)], [(4, 6)]])]
        self.run_cases(cases, Greedy.interval_partitioning)


    def test_max_overlap(self):
        cases = [([(1, 3), (0, 2), (2, 5), (3, 6), (4, 6)], 5)]
        self.run_cases(cases, Greedy.max_overlap)

    def run_cases(self, cases, to_test):
        # a case is a tuple (input, expected result)
        for _input, expected in cases:
            print(
                "\n\ntesting input : ",
                _input,
                "\nwith expected output : ",
                expected,
                "\n")
            output = to_test(_input)
            self.assertEquals(output, expected)

    def tearDown(self):
        ...
