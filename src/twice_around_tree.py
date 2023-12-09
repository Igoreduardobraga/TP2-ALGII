import numpy as np
from scipy.spatial import distance
import networkx as nx

def create_complete_graph(points):
    n = len(points)
    graph = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance.euclidean(points[i], points[j])
            graph[i][j] = dist
            graph[j][i] = dist
    return graph

def minimum_spanning_tree(graph):
    G = nx.Graph()
    n = len(graph)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=graph[i][j])
    return nx.minimum_spanning_tree(G)

def twice_around_the_tree(graph):
    mst = minimum_spanning_tree(graph)
    tour = list(nx.dfs_preorder_nodes(mst, source=0))
    tour.append(tour[0])  # Complete the tour by returning to the starting node
    return tour

def calculate_tour_length(tour, graph):
    length = 0
    for i in range(len(tour) - 1):
        length += graph[tour[i]][tour[i + 1]]
    return length

# Example usage
if __name__ == "__main__":
    # Example points (replace with your own dataset)
    points = [(0, 0), (1, 2), (2, 3), (4, 0)]
    
    # Create the complete graph
    graph = create_complete_graph(points)
    
    # Solve the TSP using Twice Around the Tree algorithm
    tour = twice_around_the_tree(graph)
    
    # Calculate the total tour length
    tour_length = calculate_tour_length(tour, graph)
    
    print("Optimal Tour:", tour)
    print("Total Tour Length:", tour_length)