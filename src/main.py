import sys
import tsplib95
from twice_around_tree import twice_around_tree
from christofides import christofides
from read_input import load_dataset
import time
import csv
import os
from memory_profiler import memory_usage

def run_algorithm(algorithm, graph):
    start_time = time.time()
    max_mem_usage = memory_usage((algorithm, (graph,)), max_usage=True, interval=1)
    result = algorithm(graph)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time, max_mem_usage

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python script.py <nome do algoritmo>")
        sys.exit(1)

    nome_algoritmo = sys.argv[1]

    testes = [arquivo for arquivo in os.listdir("testes/") if arquivo.endswith(".tsp")]
    testes_ordenados = sorted(testes, key=lambda arquivo: os.path.getsize(os.path.join("testes/", arquivo)))

    with open('resultados.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nome do Teste', 'Custo', 'Tempo de Execução', 'Uso Máximo de Memória'])

        for teste in testes_ordenados:
            caminho_teste = os.path.join("testes/", teste)
            grafo = tsplib95.load(caminho_teste).get_graph()

            if nome_algoritmo == 'twice':
                resultado, execution_time, max_mem_usage = run_algorithm(twice_around_tree, grafo)
            elif nome_algoritmo == 'christofides':
                resultado, execution_time, max_mem_usage = run_algorithm(christofides, grafo)

            writer.writerow([teste, resultado, execution_time, max_mem_usage])
            print(f"{teste} - Custo: {resultado}, Tempo: {execution_time}, Memória: {max_mem_usage}")
