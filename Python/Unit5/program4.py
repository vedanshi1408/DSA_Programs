# Program 4: Activity Selection

activities = [
    (1, 2),
    (3, 4),
    (0, 6),
    (5, 7),
    (8, 9),
    (5, 9)
]

activities.sort(key=lambda x: x[1])

selected = []
last_end = 0

for start, end in activities:
    if start >= last_end:
        selected.append((start, end))
        last_end = end

print("Selected Activities:")
for activity in selected:
    print(activity)

print("Total Activities:", len(selected))