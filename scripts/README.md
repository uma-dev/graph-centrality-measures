# Graph Analysis & Network Measures

This project generates and analyzes a network using various graph theory metrics. Below is a summary of what the main script does, the outputs it produces, and the design intuition behind each step.

---

## 📦 Project Structure

```
graph_centrality_measures/
├── data/                  # Stores the network .graphml file
├── graphs/                # Modules for generating and loading networks
│   ├── generator.py       # Generates and saves an example network
│   └── loaders.py         # Loads a network from .graphml
├── metrics/               # Functions implementing each required metric
│   ├── degree_correlation.py
│   ├── clustering.py
│   ├── traversal.py
│   ├── independent_paths.py
│   ├── bottlenecks.py
│   ├── flow.py
│   ├── cuts.py
│   ├── shortest_paths.py
│   ├── centralities.py
│   ├── hubs_authorities.py
│   └── geodesic.py
├── visualization/         # Functions for plotting the network and capacities
│   └── plot_graph.py
├── output/                # Results figures (.png)
├── scripts/               # Main script to execute all tasks
│   └── network_x_ray.py
└── README.md              # This file
```

---

## 🚀 What the X Ray Script Does

1. **Load or generate** the example network:

   * If `data/my_graph.graphml` exists, it loads the network.
   * Otherwise, it calls the generator to create a directed graph (`DiGraph`), assigns random capacities to edges, and saves it.

2. **Plot** the full network:

   * Uses `visualization/plot_graph.py` to draw nodes, edges, and display capacities on edges.
   * Saves the figure as `output/main_graph.png`.

3. **Compute and display** all 20 requested metrics:

   1. Degree correlation coefficient
   2. Global and local clustering coefficients
   3. Breadth-first search (single-source and multi-source)
   4. Edge- and vertex-disjoint paths
   5. Bottleneck edge counts
   6. Maximum flow
   7. Minimum cut cardinality
   8. Shortest path lengths (Dijkstra)
   9. Katz centrality
   10. PageRank
   11. Closeness centrality
   12. Betweenness centrality
   13. Top nodes by betweenness centrality
   14. Shortest-path tree for specified node pairs
   15. All-pairs shortest paths for specified source/target sets
   16. Hubs and authorities (HITS algorithm)
   17. Average geodesic distance
   18. Maximum flow via augmenting path algorithm

4. **Save** any intermediate CSV files in `output/x_ray` as needed and print all results to the console.

---

**Run** the analysis from the project root with:

```bash
python scripts/network_x_ray.py
```

then inspect the `output/x_ray/` directory for figures and explore measures in `stdout`
