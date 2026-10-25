# Program 9: Circular Queue

size = 3
queue = [None] * size
front = rear = -1

while True:
    print("\n1. Enqueue  2. Dequeue  3. Display  4. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        if (rear + 1) % size == front:
            print("Queue is full")
        else:
            value = int(input("Enter value: "))
            if front == -1:
                front = 0
            rear = (rear + 1) % size
            queue[rear] = value

    elif ch == "2":
        if front == -1:
            print("Queue is empty")
        else:
            print("Removed:", queue[front])
            if front == rear:
                front = rear = -1
            else:
                front = (front + 1) % size

    elif ch == "3":
        if front == -1:
            print("Queue is empty")
        else:
            i = front
            while True:
                print(queue[i], end=" ")
                if i == rear:
                    break
                i = (i + 1) % size
            print()

    elif ch == "4":
        break

    else:
        print("Invalid choice")