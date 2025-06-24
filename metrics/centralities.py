import networkx as nx
from typing import Dict, Any, List


def katz_centrality(graph: nx.Graph, alpha: float = 0.1) -> Dict:
    return nx.katz_centrality(graph, alpha=alpha)


def pagerank(graph: nx.Graph, alpha: float = 0.85) -> Dict:
    return nx.pagerank(graph, alpha=alpha)


def closeness_centrality(graph: nx.Graph) -> Dict:
    return nx.closeness_centrality(graph)


def betweenness_centrality(graph: nx.Graph) -> Dict:
    return nx.betweenness_centrality(graph)


def top_betweenness_nodes(graph: nx.Graph, k: int = 10) -> List[Any]:
    bc = betweenness_centrality(graph)
    sorted_nodes = sorted(bc.items(), key=lambda x: x[1], reverse=True)
    return [n for n, _ in sorted_nodes[:k]]
