import networkx as nx
from utils import calculate_weigth

def create_eulerian_graph(MST, graph):
    odd_degree_nodes = [n for n in MST.nodes() if MST.degree(n) % 2 == 1]
    min_weight_matching = nx.algorithms.matching.min_weight_matching(nx.subgraph(graph, odd_degree_nodes), maxcardinality=True)

    eulerian_graph = nx.MultiGraph(MST)
    eulerian_graph.add_edges_from(min_weight_matching)
    return eulerian_graph

def find_shortest_path(eulerian_graph):
    eulerian_circuit = list(nx.eulerian_circuit(eulerian_graph, source=1))
    path = []
    for edge in eulerian_circuit:
        if edge[0] not in path:
            path.append(edge[0])
    path.append(eulerian_circuit[0][0])
    return path

def christofides(graph):
    min_span_tree = nx.minimum_spanning_tree(graph)
    eulerian_graph = create_eulerian_graph(min_span_tree, graph)
    shortest_path = find_shortest_path(eulerian_graph)
    total_weight = calculate_weigth(graph, shortest_path)

    return total_weight