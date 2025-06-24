from graphs.generators import get_synthetic_graphs
from analysis.centrality import compute_centralities
from analysis.visualization import visualize_graph_centralities_grid

for name, graph in get_synthetic_graphs():
    is_directed = graph.is_directed()
    df = compute_centralities(graph, directed=is_directed)
    visualize_graph_centralities_grid(graph, df, name)

    print(f"Done: {name}")
