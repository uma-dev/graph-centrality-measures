import networkx as nx
from typing import Any


def min_cut_cardinality(graph: nx.DiGraph, s: Any, t: Any) -> int:
    cut_value, _ = nx.minimum_cut(graph, s, t)
    return int(cut_value)
