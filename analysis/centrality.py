import networkx as nx
import pandas as pd


def compute_centralities(graph, directed=False):
    centralities = {
        "PageRank": nx.pagerank(graph),
        "Degree": nx.degree_centrality(graph),
        "Closeness": nx.closeness_centrality(graph),
    }

    if directed:
        hubs, authorities = nx.hits(graph)
        centralities["Hubs"] = hubs
        centralities["Authorities"] = authorities

    df = pd.DataFrame(centralities)
    df.index.name = "Node"
    return df
