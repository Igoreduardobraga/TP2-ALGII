import networkx as nx
from utils import calculate_weigth

# Função para encontrar o peso de um circuito Hamiltoniano usando o algoritmo "twice around the tree"
def twice_around_tree(graph):
    # Constroi a árvore geradora mínima
    min_spanning_tree = nx.minimum_spanning_tree(graph)

    # Obtem o caminho em pré-ordem da busca em profundidade
    dfs_path = list(nx.dfs_preorder_nodes(min_spanning_tree, source=1))

    # Retorna ao ponto de partida para completar o ciclo
    dfs_path.append(dfs_path[0])

    # Retrona o peso do ciclo
    return calculate_weigth(graph, dfs_path)
