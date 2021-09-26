import unittest
from Context import Greedy


class Greedy_test(unittest.TestCase):

    # uses testwrapper to execute various scenarios

    def setUp(self):
        ...

    def test_interval_scheduling(self):
        # a case is a tuple (input, expected result)
        cases = [([(1, 3), (0, 2), (2, 5), (3, 6), (4, 6)], [(0, 2), (2, 5)])]

        for _input, expected in cases:
            print(
                "\n\ntesting input : ",
                _input,
                "\nwith expected output : ",
                expected,
                "\n")
            output = Greedy.interval_scheduling(_input)
            self.assertEquals(output, expected)

    def test_interval_partitioning(self):
        # a case is a tuple (input, expected result)
        cases = [([(1, 3), (0, 2), (2, 5), (3, 6), (4, 6)], [
                  [(0, 2), (2, 5)], [(1, 3), (3, 6)], [(2, 5)], [(3, 6)], [(4, 6)]])]

        for _input, expected in cases:
            print(
                "\n\ntesting input : ",
                _input,
                "\nwith expected output : ",
                expected,
                "\n")
            output = Greedy.interval_partitioning(_input)
            self.assertEquals(output, expected)

    def tearDown(self):
        ...
