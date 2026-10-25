# Program 7: AI Search using BFS

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": ["H"],
    "F": [],
    "G": [],
    "H": []
}

def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    parent = {start: None}

    while queue:
        node = queue.popleft()

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()
            print("Goal found!")
            print("Path:", " -> ".join(path))
            return

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in parent:
                    parent[neighbor] = node
                    queue.append(neighbor)

    print("Goal not found")


print("Available Nodes: A, B, C, D, E, F, G, H")
start = input("Enter start node: ").upper()
goal = input("Enter goal node: ").upper()

if start in graph and goal in graph:
    bfs(graph, start, goal)
else:
    print("Invalid node")