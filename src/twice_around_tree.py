import networkx as nx

def calculate_graph_weight(graph, hamiltonian_cycle):
    weight = 0
    for i in range(len(hamiltonian_cycle) - 1):
        u, v = hamiltonian_cycle[i], hamiltonian_cycle[i + 1]
        weight += graph[u][v]['weight'] 
    
    weight += graph[hamiltonian_cycle[-1]][hamiltonian_cycle[0]]['weight']
    return weight

def twice_around_tree(graph):
    cycle = list(nx.dfs_preorder_nodes(nx.minimum_spanning_tree(graph), 1))
    weight = calculate_graph_weight(graph, cycle)
    return cycle, weight