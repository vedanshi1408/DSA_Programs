# Program 10: Kruskal's Algorithm

edges = [
    (2, 'A', 'B'),
    (3, 'A', 'C'),
    (1, 'B', 'C'),
    (4, 'B', 'D'),
    (5, 'C', 'D')
]

parent = {}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    parent[find(a)] = find(b)

for edge in edges:
    parent[edge[1]] = edge[1]
    parent[edge[2]] = edge[2]

total = 0

for weight, u, v in sorted(edges):
    if find(u) != find(v):
        union(u, v)
        print(u, "-", v, "Weight:", weight)
        total += weight

print("Minimum Cost:", total)