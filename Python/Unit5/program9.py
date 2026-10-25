# Program 9: Floyd-Warshall Algorithm

INF = float('inf')

dist = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

n = len(dist)

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(
                dist[i][j],
                dist[i][k] + dist[k][j]
            )

print("Shortest Distance Matrix:")

for row in dist:
    print([x if x != INF else "INF" for x in row])