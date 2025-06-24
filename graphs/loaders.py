import networkx as nx


def load_graph(path: str) -> nx.Graph:
    """
    Load a graph from .graphml file.

    Args:
        path: Path to .graphml file

    Returns:
        nx.Graph or nx.DiGraph
    """
    graph = nx.read_graphml(path)
    print(f"[INFO] Graph loaded from {path}")
    return graph
