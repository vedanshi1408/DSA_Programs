# Program 8: Prim's Minimum Spanning Tree

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 3, 'B': 1, 'D': 5},
    'D': {'B': 4, 'C': 5}
}

visited = {'A'}
edges = []
total_cost = 0

while len(visited) < len(graph):
    min_weight = float('inf')
    selected_edge = None

    for node in visited:
        for neighbor, weight in graph[node].items():
            if neighbor not in visited and weight < min_weight:
                min_weight = weight
                selected_edge = (node, neighbor, weight)

    if selected_edge is None:
        print("Graph is disconnected")
        break

    u, v, weight = selected_edge
    edges.append((u, v, weight))
    visited.add(v)
    total_cost += weight

print("Minimum Spanning Tree:")
for u, v, weight in edges:
    print(u, "-", v, "Weight:", weight)

if len(visited) == len(graph):
    print("Minimum Cost:", total_cost)