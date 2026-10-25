# Program 3: Circular Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

def insert(value):
    global head
    new = Node(value)

    if head is None:
        head = new
        new.next = head
    else:
        temp = head
        while temp.next != head:
            temp = temp.next
        temp.next = new
        new.next = head

def display():
    if head is None:
        print("List is empty")
        return

    temp = head
    while True:
        print(temp.data, end=" -> ")
        temp = temp.next
        if temp == head:
            break
    print("(back to head)")

while True:
    print("\n1. Insert  2. Display  3. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        insert(int(input("Enter value: ")))
    elif ch == "2":
        display()
    elif ch == "3":
        break
    else:
        print("Invalid choice")