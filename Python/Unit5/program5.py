# Program 5: Fractional Knapsack

items = [
    (60, 10),
    (100, 20),
    (120, 30)
]

capacity = 50
total_value = 0

items.sort(key=lambda x: x[0] / x[1], reverse=True)

for value, weight in items:
    if capacity >= weight:
        total_value += value
        capacity -= weight
    else:
        total_value += value * (capacity / weight)
        break

print("Maximum Value:", total_value)