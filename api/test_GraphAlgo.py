import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from nodedata import nodedata
from edgedata import edgedata
from copy import copy, deepcopy


class test_digraph(unittest.TestCase):

    # Add/Remove nodes and edges
    def test_shortestpath(self):
        gg = DiGraph()
        gg.add_node(1)
        gg.add_node(2)
        gg.add_node(3)
        gg.add_node(4)
        gg.add_node(5)
        gg.add_node(6)
        gg.add_node(7)
        gg.add_edge(1,2,10)
        gg.add_edge(2,3,9)
        gg.add_edge(5,7,2)
        gg.add_edge(2,1,3)
        gg.add_edge(3,4,2)
        gg.add_edge(4,5,9)
        gg.add_edge(1,5,90)
        graph3 = GraphAlgo()
        graph3.init(gg)
        self.assertEqual(graph3.shortest_path(1, 5), (30,[1,2,3,4,5]))
        self.assertEqual(graph3.shortest_path(2, 3), (9, [2, 3]))

    def connected_component(self):
        gg = DiGraph()
        gg.add_node(1)
        gg.add_node(2)
        gg.add_node(3)
        gg.add_node(4)
        gg.add_node(5)
        gg.add_node(6)
        gg.add_node(7)
        gg.add_edge(1, 2, 10)
        gg.add_edge(2, 3, 9)
        gg.add_edge(5, 7, 2)
        gg.add_edge(2, 1, 3)
        gg.add_edge(3, 4, 2)
        gg.add_edge(4, 5, 9)
        gg.add_edge(1, 5, 90)
        graph3 = GraphAlgo()
        graph3.init(gg)
        lis=[2,5]
        lis2=[7]
        self.assertEqual(graph3.connected_component(1), lis)
        self.assertEqual(graph3.connected_component(5), lis2)

    def connected_components(self):
        gg = DiGraph()
        gg.add_node(1)
        gg.add_node(2)
        gg.add_node(3)
        gg.add_node(4)
        gg.add_edge(1, 2, 5)
        gg.add_edge(1, 3, 5)
        gg.add_edge(2, 3, 5)
        gg.add_edge(3, 4, 5)
        gg.add_edge(4, 1, 5)
        lis=[[2,3],[3],[4],[1]]
        graph3 = GraphAlgo()
        graph3.init(gg)
        self.assertEqual(graph3.connected_components(), lis)





if __name__ == '_main_':
    unittest.main(verbosity=True)