# Program 5: Stack Using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

top = None

def push(value):
    global top
    new = Node(value)
    new.next = top
    top = new

def pop():
    global top
    if top is None:
        print("Stack is empty")
    else:
        print("Popped:", top.data)
        top = top.next

def display():
    temp = top
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

while True:
    print("\n1. Push  2. Pop  3. Display  4. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        push(int(input("Enter value: ")))
    elif ch == "2":
        pop()
    elif ch == "3":
        display()
    elif ch == "4":
        break
    else:
        print("Invalid choice")