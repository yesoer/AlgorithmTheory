import unittest
from Context import DivideAndConquer
from Context import run_cases


class TestDC(unittest.TestCase):

    def setUp(self):
        self.nums1 = [2, 3, 4, 6, 5]
        self.nums2 = [5, 4, 3, 2, 1]
        self.nums3 = [7, 3, 1, 5, 6, 10, 8, 9, 2, 4]

        self.points1 = [(1, 3), (1, 2), (3, 1), (3, 3), (5, 6)]
        self.points2 = [(1, 1), (3, 1), (2, 3), (3, 4), (6, 3), (1, 6), (4, 6), 
                        (6, 6)]
        self.points3 = [(1, 1), (1, 3), (1, 5), (2, 6), (3, 3), (3, 4)]

    def tearDown(self):
        ...

    def test_inversions(self):
        cases = [
                ([self.nums1], 1),
                ([self.nums2], 10),
                ([self.nums3], 20)
                ]
        run_cases(self, cases, DivideAndConquer.inversions)

    def test_shortest_distance_wrapper(self):
        cases = [
                ([self.points1], 1.0),
                ([self.points2], 1.4142135623730951),
                ([self.points3], 1.),
                ]
        run_cases(self, cases, DivideAndConquer.shortest_distance_wrapper)
