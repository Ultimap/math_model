def dekstra(graph, costs, parents, start, end):
    processed = []

    def find_lower_cost_node(costs):
        lower_cost = INFINITY
        lower_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lower_cost and node not in processed:
                lower_cost = cost
                lower_cost_node = node
        return lower_cost_node

    node = find_lower_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lower_cost_node(costs)
    return parents, costs

# Ваш граф
graph = {
    'A': {'B': 14, 'D': 78, 'E': 47, 'F': 28, 'J': 96},
    'B': {'A': 14, 'C': 29, 'F': 45, 'N': 73},
    'C': {'B': 29, 'F': 41, 'N': 70, 'J': 72},
    'D': {'A': 78, 'E': 56, 'J': 31},
    'E': {'A': 47, 'D': 56},
    'F': {'A': 28, 'B': 35, 'C': 41, 'N': 55, 'M': 40, 'Q': 44},
    'G': {'N': 6},
    'N': {'B': 72, 'C': 70, 'F': 55, 'G': 6, 'M': 48},
    'M': {'F': 40, 'N': 48, 'R': 32},
    'R': {'M': 32, 'Q': 19},
    'Q': {'F': 44, 'R': 19, 'P': 47},
    'P': {'A': 73, 'Q': 47, 'K': 20, 'O': 39},
    'K': {'P': 20, 'J': 35},
    'J': {'A': 96, 'D': 31, 'E': 72, 'K': 25, 'O': 30},
    'O': {'P': 39, 'J': 30}
}

# Найдем кратчайший путь от вершины O до вершины G
INFINITY = float('inf')
start = 'O'
end = 'G'
costs = {node: INFINITY for node in graph}
costs[start] = 0
parents = {node: None for node in graph}
parents, costs = dekstra(graph, costs, parents, start, end)

# Восстановление пути
path = []
while end is not None:
    path.append(end)
    end = parents[end]
path.reverse()

print("Кратчайший путь от вершины O до вершины G:", path)
