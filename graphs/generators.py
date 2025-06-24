import networkx as nx


def get_synthetic_graphs():
    graphs = []
    probs = [[0.8, 0.05], [0.05, 0.8]]

    erdos_renyi_graph = nx.erdos_renyi_graph(n=180, p=0.02)
    watts_strogatz_graph = nx.watts_strogatz_graph(n=200, k=5, p=0.4)
    barabasi_albert_graph = nx.barabasi_albert_graph(n=200, m=2)
    stochastic_block_model = nx.stochastic_block_model([20, 10], probs)
    np_random_graph = nx.gnp_random_graph(n=120, p=0.01, directed=True)

    graphs.append(("Erdos-Renyi", erdos_renyi_graph))
    graphs.append(("Watts-Strogatz", watts_strogatz_graph))
    graphs.append(("Barabasi-Albert", barabasi_albert_graph))
    graphs.append(("Stochastic-Block", stochastic_block_model))
    graphs.append(("Directed", np_random_graph))

    return graphs
