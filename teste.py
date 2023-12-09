import numpy as np
import networkx as nx

def read_tsplib_file(file_path):
    points = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        read_coordinates = False
        for line in lines:
            if line.startswith("NODE_COORD_SECTION"):
                read_coordinates = True
                continue
            if line.startswith("EOF") or not read_coordinates:
                break
            parts = line.strip().split()
            if len(parts) >= 3:
                node_id, x, y = map(int, parts[:3])
                points[node_id] = (x, y)
    return points

def create_complete_graph(points):
    n = len(points)
    graph = np.zeros((n, n))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                dist = np.linalg.norm(np.array(points[i]) - np.array(points[j]))
                graph[i - 1][j - 1] = dist
    return graph

def minimum_spanning_tree(graph):
    G = nx.Graph()
    n = len(graph)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=graph[i][j])
    mst = nx.minimum_spanning_tree(G)
    return mst

def dfs(graph, start_node):
    stack = [start_node]
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in range(len(graph[node])):
                if graph[node][neighbor] > 0 and neighbor not in visited:
                    stack.append(neighbor)
    return list(visited)

def twice_around_the_tree(graph):
    mst = minimum_spanning_tree(graph)
    
    # Get the nodes in the order of the tour
    tour_nodes = dfs(nx.to_numpy_matrix(mst), 0)  # Start from node 0
    tour_nodes.append(tour_nodes[0])  # Complete the tour by returning to the starting node
    return tour_nodes

def calculate_tour_length(tour, graph):
    length = 0
    for i in range(len(tour) - 1):
        length += graph[tour[i] - 1][tour[i + 1] - 1]
    return length

if __name__ == "__main__":
    # Replace 'your_dataset.tsp' with the path to your TSPLIB dataset file
    file_path = 'a280.tsp'
    
    # Read the TSPLIB dataset file
    points = read_tsplib_file(file_path)
    
    # Create the complete graph
    graph = create_complete_graph(points)
    
    # Solve the TSP using Twice Around the Tree algorithm
    tour = twice_around_the_tree(graph)
    
    # Calculate the total tour length
    tour_length = calculate_tour_length(tour, graph)
    
    print("Optimal Tour:", tour)
    print("Total Tour Length:", tour_length)
