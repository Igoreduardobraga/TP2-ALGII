def calculate_weigth(graph, path):
    # Calcular o peso total do caminho
    total_weight = 0
    for i in range(len(path) - 1):
        total_weight += graph[path[i]][path[i + 1]]['weight']
    return total_weight