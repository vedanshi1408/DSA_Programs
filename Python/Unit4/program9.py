# Program 9: Kruskal's Minimum Spanning Tree

edges = [
    (4, 'A', 'B'),
    (3, 'A', 'C'),
    (1, 'B', 'C'),
    (2, 'B', 'D'),
    (5, 'C', 'D'),
    (6, 'C', 'E'),
    (3, 'D', 'E')
]

parent = {}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    parent[find(a)] = find(b)

vertices = set()

for weight, u, v in edges:
    vertices.add(u)
    vertices.add(v)

for vertex in vertices:
    parent[vertex] = vertex

total_cost = 0
count = 0

print("Minimum Spanning Tree:")

for weight, u, v in sorted(edges):
    if find(u) != find(v):
        union(u, v)
        print(u, "-", v, "Weight:", weight)
        total_cost += weight
        count += 1

        if count == len(vertices) - 1:
            break

print("Minimum Cost:", total_cost)