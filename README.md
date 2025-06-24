# Graph Centrality Measures

Generates synthetic graphs, computes centrality measures, and visualizes the results in informative plots.  

## Features

✅ Generates synthetic graphs:  

- Erdős–Rényi
  ![Erdos-Renyi_centralities_grid](https://github.com/user-attachments/assets/95c420f1-2e25-4361-a0d8-f1c737a9159b)

- Watts–Strogatz
  ![Watts-Strogatz_centralities_grid](https://github.com/user-attachments/assets/05179bc6-decf-402d-bfd4-3ab273e2eea7)

- Barabási–Albert
  ![Barabasi-Albert_centralities_grid](https://github.com/user-attachments/assets/6a56b736-b139-4710-9965-15576d996bb3)

- Stochastic Block Model
  ![Stochastic-Block_centralities_grid](https://github.com/user-attachments/assets/3046a01f-0460-4d71-b132-25b113514ba2)

- Directed random graph
  ![Directed_centralities_grid](https://github.com/user-attachments/assets/13916346-e2b6-465d-822f-c17603bed2a1)


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
