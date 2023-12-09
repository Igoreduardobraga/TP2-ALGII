import sys
import tsplib95
from twice_around_tree import twice_around_tree

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python script.py <nome_do_dataset>")
        sys.exit(1)

    nome_dataset = sys.argv[1]
    nome_arquivo_csv = 'resultados_tsp.csv'
    grafo = tsplib95.load(f'testes/{nome_dataset}.tsp').get_graph()
    num = len(grafo.nodes)

    resultado = twice_around_tree(grafo)
    print(resultado)