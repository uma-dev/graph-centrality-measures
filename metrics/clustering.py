import networkx as nx
from typing import Dict


def local_clustering(graph: nx.Graph) -> Dict:
    """Local clustering coefficient per node."""
    return nx.clustering(graph)


def global_clustering(graph: nx.Graph) -> float:
    """Global clustering coefficient (average of local)."""
    return nx.average_clustering(graph)
