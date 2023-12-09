import tsplib95

def load_dataset(path):

    def convert_to_int(valor):
        return int(float(valor))
    
    grafo = []

    with open(path, 'r') as arquivo:
        linhas = arquivo.readlines()
        coord_section = False
        coordenadas = {}

        for linha in linhas:
            partes = linha.split()

            if len(partes) > 0:
                if partes[0] == 'NODE_COORD_SECTION':
                    coord_section = True
                elif partes[0] == 'EOF':
                    coord_section = False
                elif coord_section:
                    no, x, y = map(convert_to_int, partes)
                    coordenadas[no] = (x, y)

    for u, pos_u in coordenadas.items():
        node_row = []
        for v, pos_v in coordenadas.items():
            if u != v:
                distance = ((pos_u[0] - pos_v[0]) ** 2 + (pos_u[1] - pos_v[1]) ** 2) ** 0.5
                node_row.append(distance)
            else:
                node_row.append(0)
        grafo.append(node_row)

    return grafo

def read_input(path):
    with open(path, "r") as f:
        lines = f.readlines()
        tour = [int(line.strip()) for line in lines if lines.strip().isdigit()]
        return tour