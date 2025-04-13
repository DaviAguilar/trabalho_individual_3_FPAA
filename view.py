# view.py
import networkx as nx
import matplotlib.pyplot as plt


def draw_hamiltonian_path(graph, path=None):
    """
    Desenha o grafo e destaca o Caminho Hamiltoniano, se fornecido.
    - graph: matriz de adjacência
    - path: lista com o caminho Hamiltoniano (opcional)
    """
    G = nx.Graph()
    n = len(graph)

    # Adiciona vértices
    for i in range(n):
        G.add_node(i)

    # Adiciona arestas
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] == 1:
                G.add_edge(i, j)

    pos = nx.spring_layout(G)

    # Desenha o grafo
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16, font_weight='bold')

    if path:
        # Cria lista de arestas do caminho Hamiltoniano
        hamiltonian_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        # Desenha as arestas do caminho em vermelho
        nx.draw_networkx_edges(G, pos, edgelist=hamiltonian_edges, edge_color='red', width=2)

    plt.title("Grafo com Caminho Hamiltoniano Destacado" if path else "Grafo Original")
    plt.savefig("assets/hamiltonian_path.png")
    plt.show()


def main():
    # Mesmo grafo de main.py
    graph = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ]

    # Exemplo de caminho Hamiltoniano (pode ser obtido de main.py)
    path = [0, 1, 2, 4, 3]  # Um caminho válido para o grafo

    draw_hamiltonian_path(graph, path)


if __name__ == "__main__":
    main()