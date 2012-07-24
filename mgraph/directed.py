import networkx as nx
from collections import defaultdict


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


def roots(dg):
  """Get roots of a directed graph in O(n)"""
  return [n for n, d in dg.in_degree().iteritems() if d == 0]


def degree_centrality(dg, n):
  """Get the degree centrality of a single node"""
  return dg.degree(n) / (len(dg) - 1.0)
