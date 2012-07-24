from .. import directed
import unittest
import networkx as nx


class TestDirected(unittest.TestCase):

  def setUp(self):
    self.d4 = nx.DiGraph([(1, 2), (2, 3), (1, 4)])
    self.ds = nx.DiGraph([(1, 2), (3, 4), (4, 6)])

  def test_depth_empty(self):
    g = nx.DiGraph()
    self.assertEqual(directed.depth(g), None)

  def test_depth_single_node(self):
    g = nx.DiGraph()
    g.add_node(1)
    self.assertEqual(directed.depth(g), 0)

  def test_depth_simple(self):
    self.assertEqual(directed.depth(self.d4), 2)

  def test_depth_disconnected(self):
    self.assertEqual(directed.depth(self.ds), 2)

  def test_degree_centrality(self):
    self.assertEqual(directed.degree_centrality(self.d4, 1), 2.0 / 3)
    self.assertEqual(directed.degree_centrality(self.d4, 2), 2.0 / 3)

  def test_roots(self):
    self.assertEqual(directed.roots(self.d4), [1])
    self.assertEqual(sorted(directed.roots(self.ds)), sorted([1, 3]))
