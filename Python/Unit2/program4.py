# Program 4: Stack Using List

stack = []

while True:
    print("\n1. Push  2. Pop  3. Display  4. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        stack.append(int(input("Enter value: ")))
        print("Element pushed")

    elif ch == "2":
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack is empty")

    elif ch == "3":
        print("Stack:", stack)

    elif ch == "4":
        break

    else:
        print("Invalid choice")