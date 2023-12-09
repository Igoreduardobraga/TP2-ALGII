import tsplib95

def load_dataset(path):
    problema = tsplib95.load(path)
    grafo = problema.get_graph()
    return grafo

def read_input(path):
    with open(path, "r") as f:
        lines = f.readlines()
        tour = [int(line.strip()) for line in lines if lines.strip().isdigit()]
        return tour