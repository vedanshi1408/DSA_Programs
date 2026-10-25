# Program 4: BST Search

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)

root = None
for x in [50, 30, 70, 20, 40]:
    root = insert(root, x)

key = int(input("Enter element to search: "))

if search(root, key):
    print("Element found")
else:
    print("Element not found")