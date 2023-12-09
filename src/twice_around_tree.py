import networkx as nx
from utils import calculate_weigth

def twice_around_tree(graph):
    # Construir a árvore geradora mínima
    min_spanning_tree = nx.minimum_spanning_tree(graph)

    # Obter o caminho em pré-ordem da busca em profundidade
    dfs_path = list(nx.dfs_preorder_nodes(min_spanning_tree, source=1))

    # Retornar ao ponto de partida para completar o ciclo
    dfs_path.append(dfs_path[0])

    return calculate_weigth(graph, dfs_path)
