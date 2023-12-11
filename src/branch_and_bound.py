import math
from utils import calculate_weigth

def calculate_lower_bound(graph, node, visited):
    edges = [graph[node][neighbour]['weight'] for neighbour in graph[node] if neighbour not in visited]
    return sum(sorted(edges)[:2])

def branch_and_bound(graph):
    best_cost = math.inf
    best_path = None
    stack = [({'node': 1, 'visited': set([1]), 'path': [1], 'bound': 0}, 0)]

    while stack:
        current_data, current_bound = stack.pop()
        node, visited, path = current_data['node'], current_data['visited'], current_data['path']

        if len(path) == len(graph):
            total_cost = calculate_weigth(graph, path)
            if total_cost < best_cost:
                best_cost = total_cost
                best_path = path
            continue

        for neighbour in graph[node]:
            if neighbour not in visited:
                new_visited = visited.copy()
                new_visited.add(neighbour)
                new_bound = current_bound + calculate_lower_bound(graph, neighbour, new_visited)
                if new_bound < best_cost:
                    new_path = path + [neighbour]
                    stack.append(({'node': neighbour, 'visited': new_visited, 'path': new_path, 'bound': new_bound}, new_bound))
        stack.sort(key=lambda x: x[1])

    return best_cost, best_path
