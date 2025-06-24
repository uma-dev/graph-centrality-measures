# Graph Centrality Measures

Generates synthetic graphs, computes centrality measures, and visualizes the results in informative plots.  

## Features

✅ Generates synthetic graphs:  

- Erdős–Rényi  
- Watts–Strogatz  
- Barabási–Albert  
- Stochastic Block Model  
- Directed random graph

✅ Computes multiple centralities:  

- PageRank  
- Degree  
- Closeness  
- (Hubs & Authorities for directed graphs)

✅ Visualizes:  

- Single graph per centrality  
- Summary grid per graph (all centralities in one image)  
- Saves results to `/output` folder  

---

## Project Structure

```bash
graph_analysis_project/
├── graphs/ # Graph generators (synthetic)
├── analysis/ # Centrality computation & visualization
├── output/ # Results (.png)
├── main.py # Main runner script
├── requirements.txt # Python dependencies
└── README.md
```

---

## Installation and usage

Use `uv` or `pip`:

```bash
uv pip install -r requirements.txt
pip install -r requirements.txt

python main.py # run the main script
```

Results will be shown in:

```bash
/output/*.png

```
