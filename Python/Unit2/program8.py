# Program 8: Queue Using List

queue = []

while True:
    print("\n1. Enqueue  2. Dequeue  3. Display  4. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        queue.append(int(input("Enter value: ")))
        print("Element added")

    elif ch == "2":
        if queue:
            print("Removed:", queue.pop(0))
        else:
            print("Queue is empty")

    elif ch == "3":
        print("Queue:", queue)

    elif ch == "4":
        break

    else:
        print("Invalid choice")