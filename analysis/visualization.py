import matplotlib.pyplot as plt
import networkx as nx
import os
from typing import Union
import pandas as pd


def visualize_graph_centralities_grid(
    graph: Union[nx.Graph, nx.DiGraph],
    centrality_df: pd.DataFrame,
    name: str,
    output_dir: str = "output",
    layout_seed: int = 42,
) -> None:
    """
    Generate a grid of centrality visualizations for the graph.

    Args:
        graph (nx.Graph or nx.DiGraph): The graph to visualize.
        centrality_df (pd.DataFrame): DataFrame of centralities per node.
        name (str): Name of the graph.
        output_dir (str): Directory to save the output image.
        layout_seed (int): Random seed for graph layout.
    """
    os.makedirs(output_dir, exist_ok=True)

    centralities_to_plot = [
        "PageRank",
        "Degree",
        "Closeness",
    ]

    # --- Adjust layout ---
    k_value = 1.5 / (len(graph.nodes()) ** 0.5)  # bigger k = more spacing
    pos = nx.spring_layout(graph, k=k_value, seed=layout_seed)

    n_cols = 3
    n_rows = (len(centralities_to_plot) + n_cols - 1) // n_cols
    fig, axes = plt.subplots(
        n_rows, n_cols, figsize=(5.5 * n_cols, 4.5 * n_rows), dpi=200
    )
    axes = axes.flatten()

    for i, centrality in enumerate(centralities_to_plot):
        ax = axes[i]

        # --- Normalize color map ---
        nodes = nx.draw_networkx_nodes(
            graph,
            pos,
            node_size=80,  # smaller nodes
            cmap=plt.cm.plasma,
            node_color=centrality_df[centrality].values,
            ax=ax,
            edgecolors="black",
            linewidths=0.3,
        )

        nx.draw_networkx_edges(
            graph,
            pos,
            alpha=0.25,
            width=0.8,
            edge_color="gray",
            ax=ax,
        )

        nx.draw_networkx_labels(
            graph,
            pos,
            font_size=6,
            font_color="black",
            font_family="sans-serif",
            ax=ax,
        )

        ax.set_title(f"{centrality} Centrality", fontsize=12)
        cbar = plt.colorbar(nodes, ax=ax)
        cbar.set_label("Centrality", fontsize=9)
        cbar.ax.tick_params(labelsize=8)
        ax.axis("off")

    plt.suptitle(f"{name} - Centralities", fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    output_path = os.path.join(output_dir, f"{name}_centralities_grid.png")
    plt.savefig(output_path)
    plt.close()

    print(f"[INFO] Centralities grid saved: {output_path}")


def plot_test_graph(graph, output_path="output/x_ray/graph.png", title="Test Graph"):
    plt.figure(figsize=(12, 10))

    pos = nx.spring_layout(graph, seed=42, k=1.5)
    is_directed = graph.is_directed()

    # Draw nodes and edges
    nx.draw_networkx_nodes(
        graph,
        pos,
        node_size=180,
        node_color="skyblue",
        edgecolors="black",
        linewidths=0.4,
    )
    nx.draw_networkx_edges(
        graph,
        pos,
        arrowstyle="->" if is_directed else "-",
        arrows=is_directed,
        alpha=0.5,
        width=0.6,
        edge_color="gray",
    )
    nx.draw_networkx_labels(graph, pos, font_size=8)

    if nx.get_edge_attributes(graph, "capacity"):
        edge_labels = nx.get_edge_attributes(graph, "capacity")
        nx.draw_networkx_edge_labels(
            graph, pos, edge_labels=edge_labels, font_size=6, label_pos=0.5
        )

    plt.title(title)
    plt.axis("off")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    print(f"[INFO] Graph plotted and saved to: {output_path}")
