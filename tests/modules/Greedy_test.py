import unittest
from Context import Greedy


class Greedy_test(unittest.TestCase):

    # uses testwrapper to execute various scenarios

    def setUp(self):
        ...

    ############
    # Intervals
    ############

    def test_interval_scheduling(self):
        cases = [([(1, 3), (0, 2), (2, 5), (3, 6), (4, 6)], [(0, 2), (3, 6)])]
        self.run_cases(cases, Greedy.interval_scheduling)

    def test_interval_partitioning(self):
        cases = [([(1, 3), (0, 2), (2, 5), (3, 6), (4, 6)],
                  [[(0, 2), (3, 6)], [(1, 3), (4, 6)], [(2, 5)]])]
        self.run_cases(cases, Greedy.interval_partitioning)

    def test_max_overlap(self):
        cases = [([(1, 3), (0, 2), (2, 5), (3, 6), (4, 6)], 3)]
        self.run_cases(cases, Greedy.max_overlap)

    def test_interval_lateness(self):
        cases = [([
            (1, 3, 5), (0, 2, 3), (2, 5, 7), (3, 6, 6), (4, 6, 8)], [(0, 2, 3), (3, 6, 6)])]
        self.run_cases(cases, Greedy.interval_lateness)

    #############
    # Frequencies
    #############

    def test_huffman_wrapper(self):
        cases = [([('m', 2 / 11), ('i', 4 / 11), ('s', 4 / 11), ('p', 1 / 11)], {'p': '011', 'm': '010', 'i': '00', 's': '1'})]
        self.run_cases(cases, Greedy.huffman_wrapper)
        print_something(self)
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
