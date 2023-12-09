import argparse
from criar_grafo import carregar_problema_tsp, carregar_solucao_optima, calcular_peso_solucao_optima
from metricas import executarAlgoritmo, salvar_em_csv
from twice_around_the_tree import twiceAroundTheTreeTSP

parser = argparse.ArgumentParser(description='Executar algoritmos TSP em um dataset específico.')
parser.add_argument('dataset', help='Nome do dataset (sem a extensão do arquivo)')
args = parser.parse_args()

nome_dataset = args.dataset
nome_arquivo_csv = 'resultados_tsp.csv'

grafo = carregar_problema_tsp(f'testes/{nome_dataset}.tsp')
tour_otima = carregar_solucao_optima(f'testes/{nome_dataset}.opt.tour')
peso_otimo = calcular_peso_solucao_optima(grafo, tour_otima)

num_cidades = len(grafo.nodes)

for algoritmo in [twiceAroundTheTreeTSP]:
    resultado = executarAlgoritmo(algoritmo, grafo, peso_otimo)
    salvar_em_csv(resultado, nome_arquivo_csv, nome_dataset, num_cidades)