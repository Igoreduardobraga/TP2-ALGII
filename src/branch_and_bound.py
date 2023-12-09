import sys
import math

class Node:
    def __init__(self, path, reduced_matrix, cost, vertex, level):
        self.path = path
        self.reduced_matrix = reduced_matrix
        self.cost = cost
        self.vertex = vertex
        self.level = level

def copy_to_final(curr_path):
    final_path[:N + 1] = curr_path[:]
    final_path[N] = curr_path[0]

def first_min(reduced_matrix, i):
    min_val = sys.maxsize
    for k in range(N):
        if reduced_matrix[i][k] < min_val and i != k:
            min_val = reduced_matrix[i][k]
    return min_val

def second_min(reduced_matrix, i):
    first, second = sys.maxsize, sys.maxsize
    for j in range(N):
        if i == j:
            continue
        if reduced_matrix[i][j] <= first:
            second = first
            first = reduced_matrix[i][j]
        elif reduced_matrix[i][j] <= second and reduced_matrix[i][j] != first:
            second = reduced_matrix[i][j]
    return second

def reduce_matrix(reduced_matrix):
    cost = 0
    for i in range(N):
        row_min = first_min(reduced_matrix, i)
        if row_min != sys.maxsize:
            cost += row_min
            for j in range(N):
                if reduced_matrix[i][j] != sys.maxsize and reduced_matrix[i][j] != 0:
                    reduced_matrix[i][j] -= row_min

    for i in range(N):
        col_min = first_min(reduced_matrix, i)
        if col_min != sys.maxsize:
            cost += col_min
            for j in range(N):
                if reduced_matrix[j][i] != sys.maxsize and reduced_matrix[j][i] != 0:
                    reduced_matrix[j][i] -= col_min
    return cost

def branch_and_bound(adj_matrix):
    pq = []
    root = Node([-1] * (N + 1), adj_matrix, 0, 0, 0)
    root.cost = reduce_matrix(root.reduced_matrix)

    pq.append(root)

    while pq:
        min_node = pq.pop(0)
        i = min_node.vertex

        if min_node.level == N - 1:
            min_node.path[min_node.level] = i
            copy_to_final(min_node.path)
            return min_node.cost

        for j in range(N):
            if min_node.reduced_matrix[i][j] != sys.maxsize:
                new_path = min_node.path[:]
                new_path[min_node.level] = i
                new_matrix = [row[:] for row in min_node.reduced_matrix]
                for k in range(N):
                    new_matrix[i][k] = sys.maxsize
                    new_matrix[k][j] = sys.maxsize
                new_matrix[j][0] = sys.maxsize
                new_node = Node(new_path, new_matrix, min_node.cost + min_node.reduced_matrix[i][j], j, min_node.level + 1)
                new_node.cost += reduce_matrix(new_node.reduced_matrix)
                pq.append(new_node)
                pq.sort(key=lambda x: x.cost)

N = 4
adj_matrix = [[0, 10, 15, 20],
              [10, 0, 35, 25],
              [15, 35, 0, 30],
              [20, 25, 30, 0]]
final_path = [None] * (N + 1)

print("Minimum cost:", branch_and_bound(adj_matrix))
print("Path taken:", final_path)
