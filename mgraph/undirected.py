import networkx as nx
import numpy.linalg
eigenvalues = numpy.linalg.eigvals


def algebraic_connectivity(G):
  L = nx.normalized_laplacian(G)
  e = eigenvalues(L)
  # print sorted(e, reverse=True)[0], sorted(e, reverse=True)[1]
  return sorted(e)[1]
  # print("Largest eigenvalue:", max(e))
  # print("Smallest eigenvalue:", min(e))
