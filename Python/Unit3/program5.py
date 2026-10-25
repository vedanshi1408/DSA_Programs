# Program 5: BST Deletion

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def delete(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        temp = root.right
        while temp.left:
            temp = temp.left
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

root = None
for x in [50, 30, 70, 20, 40]:
    root = insert(root, x)

print("Before deletion:")
inorder(root)

key = int(input("\nEnter value to delete: "))
root = delete(root, key)

print("After deletion:")
inorder(root)
print()