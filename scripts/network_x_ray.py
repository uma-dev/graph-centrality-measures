import os
import sys
import networkx as nx

# to run this script from the root directory as python scripts/network_x_ray.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from graphs.generators import generate_example_graph, save_graph_graphml
from graphs.loaders import load_graph

from analysis.visualization import plot_test_graph

from metrics.degree_correlation import degree_correlation_coefficient
from metrics.clustering import global_clustering, local_clustering
from metrics.traversal import bfs, multi_source_bfs
from metrics.independent_paths import k_edge_disjoint_paths, k_node_disjoint_paths
from metrics.bottlenecks import count_bottlenecks
from metrics.flow import max_flow
from metrics.cuts import min_cut_cardinality
from metrics.shortest_paths import (
    shortest_path_length,
    shortest_path_tree,
    all_pairs_shortest_paths,
)
from metrics.centralities import (
    katz_centrality,
    pagerank,
    closeness_centrality,
    betweenness_centrality,
    top_betweenness_nodes,
)
from metrics.hubs_authorities import compute_hubs_authorities
from metrics.geodesic import mean_geodesic_distance


def main():
    output_dir = "data"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "test_graph.graphml")

    if os.path.exists(output_path):
        print(f"[INFO] Graph already exists at {output_path}. Skipping generation.")
        graph = load_graph(output_path)
    else:
        print(f"[INFO] Graph doesnt exists at {output_path}. Generating.")
        graph = generate_example_graph()
        save_graph_graphml(graph, output_path)

    plot_test_graph(graph, output_path="output/x_ray/graph.png", title="Test graph")

    nodes = list(graph.nodes())
    u, v = nodes[0], nodes[1]
    sources = nodes[:3]
    targets = nodes[3:6]
    pairs = [(u, v), (nodes[2], nodes[5])]

    print(f"1) Degree correlation: {degree_correlation_coefficient(graph):.4f}")
    print(f"2a) Global clustering coefficient: {global_clustering(graph):.4f}")
    print("2b) Local clustering sample:")
    for node, value in list(local_clustering(graph).items())[:5]:
        print(f"    Node {node}: {value:.4f}")

    print(f"3a) BFS from node {u}: {bfs(graph, u)[:5]}...")
    print(f"3b) Multi-source BFS: {multi_source_bfs(graph, sources)}")

    print(f"4a) Edge-disjoint paths ({u}, {v}): {k_edge_disjoint_paths(graph, u, v)}")
    print(f"4b) Node-disjoint paths ({u}, {v}): {k_node_disjoint_paths(graph, u, v)}")

    print(f"5) Bottlenecks: {count_bottlenecks(graph, pairs)}")

    if graph.is_directed():
        print(f"6) Max flow ({u}, {v}): {max_flow(graph, u, v)}")
        print(f"7) Min cut cardinality ({u}, {v}): {min_cut_cardinality(graph, u, v)}")
    else:
        print("6) Skipped max flow (graph undirected)")
        print("7) Skipped min cut (graph undirected)")

    if nx.has_path(graph, u, v):
        print(
            f"8) Shortest path length ({u}, {v}): {shortest_path_length(graph, u, v)}"
        )
    else:
        print(f"8) No path exists between ({u}, {v})")

    print(f"9) Katz centrality sample:")
    for node, value in list(katz_centrality(graph).items())[:5]:
        print(f"    Node {node}: {value:.4f}")

    print(f"10) PageRank sample:")
    for node, value in list(pagerank(graph).items())[:5]:
        print(f"    Node {node}: {value:.4f}")

    print(f"11) Closeness centrality sample:")
    for node, value in list(closeness_centrality(graph).items())[:5]:
        print(f"    Node {node}: {value:.4f}")

    print(f"12) Betweenness centrality sample:")
    for node, value in list(betweenness_centrality(graph).items())[:5]:
        print(f"    Node {node}: {value:.4f}")

    print(f"15) Top 5 betweenness nodes: {top_betweenness_nodes(graph, k=5)}")

    print(
        f"16) Shortest path tree (pairs {pairs}): {shortest_path_tree(graph, pairs).edges()}"
    )

    print(f"17) All pairs shortest paths (sources {sources}, targets {targets}):")
    all_paths = all_pairs_shortest_paths(graph, sources, targets)
    for key, path in all_paths.items():
        print(f"    {key}: {path}")

    if graph.is_directed():
        hubs, authorities = compute_hubs_authorities(graph)
        print("18) Hubs sample:")
        for node, value in list(hubs.items())[:5]:
            print(f"    Node {node}: {value:.4f}")
        print("    Authorities sample:")
        for node, value in list(authorities.items())[:5]:
            print(f"    Node {node}: {value:.4f}")
    else:
        print("18) Skipped hubs/authorities (graph undirected)")

    print(f"19) Mean geodesic distance: {mean_geodesic_distance(graph):.4f}")

    if graph.is_directed():
        print(f"20) Max flow (augmenting path) ({u}, {v}): {max_flow(graph, u, v)}")
    else:
        print("20) Skipped max flow (graph undirected)")


if __name__ == "__main__":
    main()
