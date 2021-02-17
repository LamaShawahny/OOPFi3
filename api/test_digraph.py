import unittest
from DiGraph import DiGraph
from nodedata import nodedata
from edgedata import edgedata
from copy import copy, deepcopy


class test_digraph(unittest.TestCase):

    # Add/Remove nodes and edges
    def test_getnodes(self):
        gg=DiGraph()
        gg.add_node(1)
        gg.add_node(2)
        gg.add_node(2)
        gg.remove_node(2)
        gg.remove_node(2)
        gg.add_node(2)
        gg.add_node(2)
        gg.add_node(2)
        gg.remove_node(2)
        gg.remove_node(2)
        gg.add_node(3)
        gg.add_node(3)
        gg.remove_node(3)
        gg.add_node(3)



        x=gg.v_size()
        y= 2
        self.assertEqual(x, y)

    def test_add_edge(self):
        gg = DiGraph()
        gg.add_node(1)
        gg.add_node(2)
        gg.add_node(3)
        gg.add_node(4)
        gg.add_node(5)
        gg.add_node(6)
        gg.add_node(7)
        gg.add_node(8)
        gg.add_edge(1,2,10)
        gg.add_edge(1,3,9)
        gg.add_edge(5,7,2)
        gg.add_edge(2,1,3)
        gg.add_edge(1,2,2)
        gg.add_edge(3,2,9)
        gg.remove_edge(1,2)
        gg.remove_edge(7,8)
        x=gg.e_size()
        y=4
        self.assertEqual(x, y)

    def test_remove_node(self):
        gg = DiGraph()
        gg.add_node(1)
        gg.add_node(2)
        gg.add_node(3)
        gg.add_node(4)
        gg.add_node(5)
        gg.add_node(6)
        gg.add_node(7)
        gg.add_node(8)
        gg.remove_node(1)
        gg.remove_node(2)
        gg.remove_node(3)
        gg.add_node(9)
        x=gg.v_size()
        y=6
        self.assertEqual(x, y)

    def test_v_size(self):
        gg = DiGraph()
        gg.add_node(1)
        gg.add_node(2)
        gg.add_node(3)
        gg.add_node(4)
        gg.add_node(5)
        gg.add_node(6)
        gg.add_node(7)
        gg.add_node(8)
        x=gg.v_size()
        y = 8
        self.assertEqual(x, y)


if __name__ == '_main_':
    unittest.main(verbosity=True)