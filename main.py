# main.py
def is_valid(v, pos, path, graph):
    """
    Verifica se o vértice v pode ser adicionado na posição pos do caminho.
    - v deve ser adjacente ao vértice anterior.
    - v não deve estar no caminho atual.
    """
    # Verifica se v é adjacente ao vértice anterior
    if graph[path[pos - 1]][v] == 0:
        return False

    # Verifica se v já está no caminho
    if v in path:
        return False

    return True


def hamiltonian_path_util(graph, path, pos, n):
    """
    Função recursiva que tenta construir um Caminho Hamiltoniano.
    - graph: matriz de adjacência
    - path: lista com o caminho atual
    - pos: posição atual no caminho
    - n: número de vértices
    """
    # Caso base: se todos os vértices foram incluídos
    if pos == n:
        return True

    # Tenta adicionar cada vértice ao caminho
    for v in range(n):
        if is_valid(v, pos, path, graph):
            path[pos] = v
            if hamiltonian_path_util(graph, path, pos + 1, n):
                return True
            path[pos] = -1  # Backtracking: remove v do caminho

    return False


def hamiltonian_path(graph):
    """
    Encontra um Caminho Hamiltoniano no grafo.
    - graph: matriz de adjacência
    Retorna o caminho encontrado ou None se não existir.
    """
    n = len(graph)
    path = [-1] * n

    # Começa pelo vértice 0
    path[0] = 0

    if hamiltonian_path_util(graph, path, 1, n):
        return path
    return None


def main():
    # Exemplo de grafo (matriz de adjacência)
    graph = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ]

    result = hamiltonian_path(graph)
    if result:
        print("Caminho Hamiltoniano encontrado:", result)
    else:
        print("Nenhum Caminho Hamiltoniano existe.")


if __name__ == "__main__":
    main()