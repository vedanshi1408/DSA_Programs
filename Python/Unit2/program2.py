# Program 2: Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

head = None

def display():
    temp = head
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")

while True:
    print("\n1. Insert  2. Display  3. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        value = int(input("Enter value: "))
        new = Node(value)

        if head is None:
            head = new
        else:
            temp = head
            while temp.next:
                temp = temp.next
            temp.next = new
            new.prev = temp

    elif ch == "2":
        display()

    elif ch == "3":
        break

    else:
        print("Invalid choice")