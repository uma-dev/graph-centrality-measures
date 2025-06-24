import networkx as nx


def mean_geodesic_distance(graph: nx.Graph) -> float:
    return nx.average_shortest_path_length(graph)
