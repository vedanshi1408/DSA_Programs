# Program 10: Dijkstra's Shortest Path

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8},
    'D': {'B': 5, 'C': 8}
}

dist = {node: float('inf') for node in graph}
dist['A'] = 0
visited = set()

while len(visited) < len(graph):
    current = None

    for node in graph:
        if node not in visited:
            if current is None or dist[node] < dist[current]:
                current = node

    if current is None or dist[current] == float('inf'):
        break

    visited.add(current)

    for neighbor, weight in graph[current].items():
        new_dist = dist[current] + weight

        if new_dist < dist[neighbor]:
            dist[neighbor] = new_dist

print("Shortest distances from A:")
for node in dist:
    print("A to", node, "=", dist[node])