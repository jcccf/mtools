import networkx as nx
from collections import defaultdict
from .. import mgroup


def depths(dg):
  """Return the depths of nodes in a directed
  graph."""
  depths = defaultdict(int)
  for (u, v) in nx.dfs_edges(dg):
    depths[v] = max(depths[v], depths[u] + 1)
  return depths


def breadths(dg, root):
  """Return the breadth-first-search depth of
  nodes in a directed graph"""
  breadths = {}
  for (u, v) in nx.bfs_edges(dg, root):
    if u not in breadths:
      breadths[u] = 0
    if v not in breadths:
      breadths[v] = breadths[u] + 1
  return breadths


def depth(dg):
  """Returns the depth of a directed graph.
  A single node has depth 0."""
  depths = defaultdict(int)
  for (u, v) in nx.dfs_edges(dg):
    depths[v] = max(depths[v], depths[u] + 1)
  if len(depths) > 0:
    return max(depths.values())
  elif len(dg.nodes()) == 0:  # No nodes in graph
    return None
  else:  # Nodes but no edges in graph
    return 0


def reach(dg, root, cumulative=True):
  """Return a dictionary indicating the number of
  nodes reachable from the root(s) n steps away"""
  reach = defaultdict(int)
  brs = breadths(dg, root)
  for b in brs.itervalues():
    reach[b] += 1
  if cumulative:
    reach = mgroup.dict.cumulative(reach)
  return reach


def roots(dg):
  """Get roots of a directed graph in O(n)"""
  return [n for n, d in dg.in_degree().iteritems() if d == 0]


def leaves(dg):
  """Get leaves of a directed graph"""
  return [n for n, d in dg.out_degree().iteritems() if d == 0]


def degree_centrality(dg, n):
  """Get the degree centrality of a single node"""
  return dg.degree(n) / (len(dg) - 1.0)
