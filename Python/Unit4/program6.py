# Program 6: Social Network Graph Analysis

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

def display_friends(graph):
    for person in graph:
        print(person, ":", graph[person])

def mutual_friends(graph, person1, person2):
    if person1 not in graph or person2 not in graph:
        print("Person not found")
        return

    common = set(graph[person1]) & set(graph[person2])
    print("Mutual friends:", sorted(common))

print("Social Network:")
display_friends(graph)

p1 = input("Enter first person (A-F): ").upper()
p2 = input("Enter second person (A-F): ").upper()

mutual_friends(graph, p1, p2)