import networkx as nx
from utils import calculate_weigth

# Função para criar um grafo euleriano a partir de uma MST e um grafo original
def create_eulerian_graph(tree, graph):
    # Encontre os nós com grau ímpar na MST
    odd_degree_nodes = [n for n in tree.nodes() if tree.degree(n) % 2 == 1]

    # Encontre o emparelhamento de peso mínimo em um subgrafo do grafo original contendo apenas os nós de grau ímpar
    min_weight_matching = nx.algorithms.matching.min_weight_matching(nx.subgraph(graph, odd_degree_nodes), maxcardinality=True)

    
    # Cria um novo grafo euleriano, copiando a MST e adicionando as arestas do emparelhamento mínimo
    eulerian_graph = nx.MultiGraph(tree)
    eulerian_graph.add_edges_from(min_weight_matching)
    return eulerian_graph

# Função para encontrar o caminho mais curto em um grafo euleriano
def find_shortest_path(eulerian_graph):
    # Encontra um circuito euleriano no grafo euleriano começando a partir do nó de origem 1
    eulerian_circuit = list(nx.eulerian_circuit(eulerian_graph, source=1))

    # Inicializa uma lista para armazenar o caminho final
    path = []
    # Adiciona os nós visitados ao caminho, garantindo que não haja repetições, e termina o ciclo no primeiro nó
    for edge in eulerian_circuit:
        if edge[0] not in path:
            path.append(edge[0])
    path.append(eulerian_circuit[0][0])
    return path

# Função principal que implementa o algoritmo de Christofides
def christofides(graph):
    # Encontra a Minimum Spanning Tree (MST) do grafo original
    min_span_tree = nx.minimum_spanning_tree(graph)

    # Cria um grafo euleriano a partir da MST e do grafo original
    eulerian_graph = create_eulerian_graph(min_span_tree, graph)

    # Encontra o caminho mais curto no grafo euleriano
    shortest_path = find_shortest_path(eulerian_graph)

    # Calcule o peso total do caminho encontrado
    total_weight = calculate_weigth(graph, shortest_path)

    return total_weight