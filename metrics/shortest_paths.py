import networkx as nx
from typing import Any, List, Dict, Tuple


def shortest_path_length(
    graph: nx.Graph, u: Any, v: Any, weight: str = "weight"
) -> float:
    return nx.shortest_path_length(graph, u, v, weight=weight)


def shortest_path_tree(graph: nx.Graph, pairs: List[Tuple[Any, Any]]) -> nx.Graph:
    T = nx.DiGraph()
    for u, v in pairs:
        path = nx.shortest_path(graph, u, v)
        nx.add_path(T, path)
    return T


def all_pairs_shortest_paths(
    graph: nx.Graph, sources: List[Any], targets: List[Any]
) -> Dict[Tuple[Any, Any], List[Any]]:
    result = {}
    for u in sources:
        for v in targets:
            path = nx.shortest_path(graph, u, v)
            result[(u, v)] = path
    return result
