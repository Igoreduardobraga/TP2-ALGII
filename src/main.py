import sys
import tsplib95
from twice_around_tree import twice_around_tree
from christofides import christofides
from branch_and_bound import branch_and_bound
from utils import run_algorithm
import csv
import os

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Para rodar o código utilize a seguinte linha para execução: python src/main.py <nome do algoritmo>")
        sys.exit(1)

    nome_algoritmo = sys.argv[1]

    testes = [arquivo for arquivo in os.listdir("testes/") if arquivo.endswith(".tsp")]
    testes_ordenados = sorted(testes, key=lambda arquivo: os.path.getsize(os.path.join("testes/", arquivo)))

    if nome_algoritmo == 'twice':
        with open('resultados/resultados_twice.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome do Teste', 'Custo', 'Tempo de Execução', 'Memória'])

            for teste in testes_ordenados:
                caminho_teste = os.path.join("testes/", teste)
                grafo = tsplib95.load(caminho_teste).get_graph()
                resultado, execution_time, max_mem_usage = run_algorithm(twice_around_tree, grafo)
                writer.writerow([teste, resultado, execution_time, max_mem_usage])
                print(f"{teste} - Custo: {resultado}, Tempo: {execution_time}, Memória: {max_mem_usage}")

    elif nome_algoritmo == 'christofides':
        with open('resultados/resultados_christofides.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome do Teste', 'Custo', 'Tempo de Execução', 'Memória'])

            for teste in testes_ordenados:
                caminho_teste = os.path.join("testes/", teste)
                grafo = tsplib95.load(caminho_teste).get_graph()
                resultado, execution_time, max_mem_usage = run_algorithm(christofides, grafo)
                writer.writerow([teste, resultado, execution_time, max_mem_usage])
                print(f"{teste} - Custo: {resultado}, Tempo: {execution_time}, Memória: {max_mem_usage}")
    
    elif nome_algoritmo == 'branch':
        with open('resultados/resultados_branch.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome do Teste', 'Custo', 'Tempo de Execução', 'Memória'])

            for teste in testes_ordenados:
                caminho_teste = os.path.join("testes/", teste)
                grafo = tsplib95.load(caminho_teste).get_graph()
                resultado, execution_time, max_mem_usage = run_algorithm(branch_and_bound, grafo)
                writer.writerow([teste, resultado, execution_time, max_mem_usage])
                print(f"{teste} - Custo: {resultado}, Tempo: {execution_time}, Memória: {max_mem_usage}")