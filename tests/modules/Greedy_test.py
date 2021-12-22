import unittest
from Context import Greedy
from Context import run_cases


class Greedy_test(unittest.TestCase):

    def setUp(self):
        ...

    def tearDown(self):
        ...

    ############
    # Intervals
    ############

    def test_interval_scheduling(self):
        cases = [([[(1, 3), (0, 2), (2, 5), (3, 6), (4, 6)]], [(0, 2), (3, 6)])]
        run_cases(self, cases, Greedy.interval_scheduling)

    def test_interval_partitioning(self):
        cases = [([[(1, 3), (0, 2), (2, 5), (3, 6), (4, 6)], True],
                  [[(0, 2), (3, 6)], [(1, 3), (4, 6)], [(2, 5)]])]
        run_cases(self, cases, Greedy.interval_partitioning)

    def test_max_overlap(self):
        cases = [([[(1, 3), (0, 2), (2, 5), (3, 6), (4, 6)]], 3)]
        run_cases(self, cases, Greedy.max_overlap)

    #############
    # Frequencies
    #############

    def test_huffman_wrapper(self):
        cases = [([[('m', 2 / 11), ('i', 4 / 11), ('s', 4 / 11),
                  ('p', 1 / 11)]], {'p': '100', 'm': '101', 'i': '11', 's': '0'}),
                  ([[('a', 0.4), ('b', 0.3), ('c', 0.2),
                  ('d', 0.1)]], {'a': '0', 'b': '11', 'c': '101', 'd': '100'})]
        run_cases(self, cases, Greedy.huffman_wrapper)

    ############
    # Graphs
    ############

    def test_dijkstra(self):
        cases = [([{1: [(1, 2, 0.5), (1, 5, 10)], 2: [(1, 2, 0.5), (2, 4, 5), (2, 3, 2)], 3: [(2, 3, 2), (3, 5, 1)], 4: [(2, 4, 5)], 5: [(3, 5, 1), (1, 5, 10)]}, 1, 5],
                  3.5)]
        run_cases(self, cases, Greedy.dijkstra)

    def test_mst_kruskal(self):
        cases = [([[1, 2, 3, 4, 5], [(1, 2, 0.5), (2, 4, 5), (2, 3, 2), (3, 5, 1), (1, 5, 10)]], [
                  (1, 2, 0.5), (3, 5, 1), (2, 3, 2), (2, 4, 5)])]
        run_cases(self, cases, Greedy.mst_kruskal)

    def test_mst_prim(self):
        cases = [([{1: [(1, 2, 0.5), (1, 5, 10)], 2: [(1, 2, 0.5), (2, 4, 5), (2, 3, 2)], 3: [(2, 3, 2), (3, 5, 1)], 4: [
                  (2, 4, 5)], 5: [(3, 5, 1), (1, 5, 10)]}], [(1, 2, 0.5, 1), (2, 3, 2, 1), (3, 5, 1, 1), (2, 4, 5, 1)])]
        run_cases(self, cases, Greedy.mst_prim)
