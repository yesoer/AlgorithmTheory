import unittest
from Context import Greedy
from Context import run_cases


class Greedy_test(unittest.TestCase):

    def setUp(self):
        self.intervals1 = [(1, 3), (0, 2), (2, 5), (3, 6), (4, 6)]
        self.intervals2 = [(2, 3), (3, 8), (1, 10), (2, 5), (8, 9)]
        self.intervals3 = [(1, 3), (3, 8), (2, 5), (0, 3), (0, 2)]

        self.frequencies1 = [('m', 2 / 11), ('i', 4 / 11), ('s', 4 / 11), ('p', 1 / 11)]
        self.frequencies2 = [('a', 0.4), ('b', 0.3), ('c', 0.2), ('d', 0.1)]
        self.frequencies3 = [('a', 1/6), ('b', 1/6), ('c', 1/6), ('d', 1/6), ('e', 1/6), ('f', 1/6)]

        self.vertices1 = list(range(4))
        self.vertices2 = list(range(5))
        self.vertices3 = list(range(6))
        
        self.edges1 = [(u, v, u + v) for u in self.vertices1 for v in self.vertices1]
        self.edges2 = [(0, 1, 0.5), (1, 3, 5), (1, 2, 2), (2, 4, 1), (0, 4, 10)]
        self.edges3 = [(0, 1, 10), (1, 2, 10), (2, 0, .5), (1, 3, 2), (3, 4, 2), (4, 2, 5), (2, 5, 3)]

        self.directed_graph1 = Greedy.graph_from_list(self.vertices1, self.edges1, True)
        self.directed_graph2 = Greedy.graph_from_list(self.vertices2, self.edges2, True)
        self.directed_graph3 = Greedy.graph_from_list(self.vertices3, self.edges3, True)

        self.undirected_graph1 = Greedy.graph_from_list(self.vertices1, self.edges1, False)
        self.undirected_graph2 = Greedy.graph_from_list(self.vertices2, self.edges2, False)
        self.undirected_graph3 = Greedy.graph_from_list(self.vertices3, self.edges3, False)


    def tearDown(self):
        ...

    ############
    # Intervals
    ############

    def test_interval_scheduling(self):
        cases = [
                ( [self.intervals1], [(0, 2), (2, 5)] ),
                ( [self.intervals2], [(2, 3), (3, 8), (8, 9)] ),
                ( [self.intervals3], [(0, 2), (2, 5)] )
                ]
        run_cases(self, cases, Greedy.interval_scheduling)

    def test_interval_partitioning(self):
        arg1 = [self.intervals1, True]
        res1 = [[(0, 2), (2, 5)], [(1, 3), (3, 6)], [(4, 6)]]

        arg2 = [self.intervals2, True]
        res2 = [[(2, 3), (3, 8), (8, 9)], [(2, 5)], [(1, 10)]]

        arg3 = [self.intervals3, True]
        res3 = [[(0, 2), (2, 5)], [(1, 3), (3, 8)], [(0, 3)]]

        cases = [(arg1, res1), (arg2, res2), (arg3, res3)]

        run_cases(self, cases, Greedy.interval_partitioning)

    def test_max_overlap(self):
        cases = [
                ( [self.intervals1], 3 ),
                ( [self.intervals2], 3 ),
                ( [self.intervals3], 3 )
                ]
        run_cases(self, cases, Greedy.max_overlap)

    #############
    # Frequencies
    #############

    def test_huffman_wrapper(self):
        cases = [(
                    [self.frequencies1, True], 
                    {'p': '100', 'm': '101', 'i': '11', 's': '0'}
                ),
                (
                    [self.frequencies2, True], 
                    {'a': '0', 'b': '11', 'c': '101', 'd': '100'}
                ),
                (
                    [self.frequencies3, True], 
                    {'a': '00', 'b': '01', 'c': '110', 'd': '111', 'e': '100', 'f': '101'}
                )]
        run_cases(self, cases, Greedy.huffman_wrapper)

    ############
    # Graphs
    ############

    def test_dijkstra(self):
        cases = [
                    ( [self.directed_graph1, 0, 3], ([3, 0], 3) ),
                    ( [self.directed_graph2, 0, 4], ([4, 2, 1, 0], 3.5) ),
                    ( [self.directed_graph3, 0, 5], ([5, 2, 4, 3, 1, 0], 22) )
                ]
        run_cases(self, cases, Greedy.dijkstra)

    def test_mst_kruskal(self):
        cases = [
                    ([self.vertices1, self.edges1], [(0, 0, 0), (0, 1, 1), (0, 2, 2), (0, 3, 3)]),
                    ([self.vertices2, self.edges2], [(0, 1, 0.5), (2, 4, 1), (1, 2, 2), (1, 3, 5)]),
                    ([self.vertices3, self.edges3], [(2, 0, 0.5), (1, 3, 2), (3, 4, 2), (2, 5, 3), (4, 2, 5)])
                ]
        run_cases(self, cases, Greedy.mst_kruskal)

    def test_mst_prim(self):
        cases = [
                    ([self.undirected_graph1], [(0, 1, 1), (0, 2, 2), (0, 3, 3)]),
                    ([self.undirected_graph2], [(0, 1, 0.5), (1, 2, 2), (2, 4, 1), (1, 3, 5)]),
                    ([self.undirected_graph3], [(2, 0, 0.5), (2, 5, 3), (4, 2, 5), (3, 4, 2), (1, 3, 2)])
                ]
        run_cases(self, cases, Greedy.mst_prim)
