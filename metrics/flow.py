import networkx as nx
from typing import Any


def max_flow(graph: nx.DiGraph, s: Any, t: Any) -> float:
    flow_value, _ = nx.maximum_flow(graph, s, t)
    return flow_value
