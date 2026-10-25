# Program 10: Deque

from collections import deque

dq = deque()

while True:
    print("\n1. Add Front  2. Add Rear")
    print("3. Remove Front  4. Remove Rear")
    print("5. Display  6. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        dq.appendleft(int(input("Enter value: ")))
    elif ch == "2":
        dq.append(int(input("Enter value: ")))
    elif ch == "3":
        if dq:
            print("Removed:", dq.popleft())
        else:
            print("Deque is empty")
    elif ch == "4":
        if dq:
            print("Removed:", dq.pop())
        else:
            print("Deque is empty")
    elif ch == "5":
        print("Deque:", list(dq))
    elif ch == "6":
        break
    else:
        print("Invalid choice")