import networkx as nx


def degree_correlation_coefficient(G: nx.Graph) -> float:
    """
    Compute the degree correlation coefficient (also called assortativity coefficient).

    It measures the tendency of nodes to connect to other nodes of similar degree.

    Returns:
        float: Pearson correlation coefficient of degree at either ends of an edge.
               Range: [-1, 1]
               - Positive: high-degree nodes tend to connect to other high-degree nodes.
               - Negative: high-degree nodes tend to connect to low-degree nodes.
               - Near zero: no correlation.
    """
    return nx.degree_pearson_correlation_coefficient(G)
