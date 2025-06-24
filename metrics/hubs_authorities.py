import networkx as nx
from typing import Dict, Any, Tuple


def compute_hubs_authorities(
    graph: nx.DiGraph,
) -> Tuple[Dict[Any, float], Dict[Any, float]]:
    hubs, authorities = nx.hits(graph)
    return hubs, authorities
