import networkx as nx
from typing import List, Dict, Any


def bfs(graph: nx.Graph, source: Any) -> List:
    """Simple BFS returning nodes visited."""
    return list(nx.bfs_tree(graph, source))


def multi_source_bfs(graph: nx.Graph, sources: List) -> Dict:
    """Multi-source BFS returning distance from sources."""
    return nx.multi_source_dijkstra_path_length(graph, sources)
