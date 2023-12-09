from memory_profiler import memory_usage
import time

def calculate_weigth(graph, path):
    # Calcular o peso total do caminho
    total_weight = 0
    for i in range(len(path) - 1):
        total_weight += graph[path[i]][path[i + 1]]['weight']
    return total_weight

def run_algorithm(algorithm, graph):
    start_time = time.time()
    max_mem_usage = memory_usage((algorithm, (graph,)), max_usage=True)
    result = algorithm(graph)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time, max_mem_usage