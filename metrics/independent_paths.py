import networkx as nx
from typing import Any


def k_edge_disjoint_paths(graph: nx.Graph, u: Any, v: Any) -> int:
    return nx.edge_connectivity(graph, u, v)


def k_node_disjoint_paths(graph: nx.Graph, u: Any, v: Any) -> int:
    return nx.node_connectivity(graph, u, v)
