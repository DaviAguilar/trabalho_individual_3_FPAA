# Trabalho Individual 3 - Caminho Hamiltoniano

## Descrição do Projeto

Este projeto implementa um algoritmo em Python para encontrar um **Caminho Hamiltoniano** em um grafo representado por uma matriz de adjacência. Um Caminho Hamiltoniano é um caminho em um grafo que visita cada vértice exatamente uma vez. O algoritmo utiliza **backtracking** para explorar todas as possibilidades de caminhos até encontrar um válido ou determinar que nenhum existe.

O projeto também inclui uma visualização opcional do grafo e do caminho encontrado, usando as bibliotecas **NetworkX** e **Matplotlib**.

### Lógica do Algoritmo (Explicação Linha a Linha)

O código principal está em `main.py`:

- **Função `is_valid(v, pos, path, graph)`**:
  - Verifica se o vértice `v` pode ser adicionado na posição `pos` do caminho.
  - Condições: `v` deve ser adjacente ao vértice anterior (`graph[path[pos-1]][v] == 1`) e não pode estar no caminho (`v not in path`).
- **Função `hamiltonian_path_util(graph, path, pos, n)`**:
  - Função recursiva que tenta construir o caminho.
  - Caso base: se `pos == n` (todos os vértices foram incluídos), retorna `True`.
  - Para cada vértice `v`, verifica se é válido, adiciona ao caminho, chama recursivamente para o próximo vértice, e faz backtracking se necessário.
- **Função `hamiltonian_path(graph)`**:
  - Inicializa o caminho começando pelo vértice 0 e chama `hamiltonian_path_util`.
  - Retorna o caminho encontrado ou `None` se não existir.
- **Função `main()`**:
  - Define um grafo de exemplo (5 vértices) e executa o algoritmo, exibindo o resultado.

O código em `view.py` (ponto extra) desenha o grafo e destaca o caminho Hamiltoniano:
- Converte a matriz de adjacência em um grafo NetworkX.
- Usa Matplotlib para desenhar vértices, arestas e destacar o caminho em vermelho.
- Salva a imagem em `assets/hamiltonian_path.png`.

## Como Executar o Projeto

### Pré-requisitos
- Python 3.8 ou superior
- Bibliotecas (para visualização, ponto extra):
  ```bash
  pip install -r requirements.txt