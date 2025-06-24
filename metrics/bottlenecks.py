import networkx as nx
from typing import List, Tuple, Dict, Any


def count_bottlenecks(
    graph: nx.Graph, pairs: List[Tuple[Any, Any]]
) -> Dict[Tuple[Any, Any], int]:
    result = {}
    for u, v in pairs:
        cut_value, _ = nx.minimum_edge_cut(graph, u, v), None
        result[(u, v)] = len(cut_value)
    return result
