# Program 9: Prim's Algorithm

import heapq

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5)],
    'D': [('B', 4), ('C', 5)]
}

visited = set()
heap = [(0, 'A')]
total = 0

while heap:
    weight, node = heapq.heappop(heap)

    if node in visited:
        continue

    visited.add(node)
    total += weight
    print(node, "Weight:", weight)

    for neighbour, cost in graph[node]:
        if neighbour not in visited:
            heapq.heappush(heap, (cost, neighbour))

print("Minimum Cost:", total)