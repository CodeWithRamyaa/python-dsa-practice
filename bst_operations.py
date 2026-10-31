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
    elif value > root.data:
        root.right = insert(root.right, value)

    return root


def search(root, value):
    if root is None or root.data == value:
        return root

    if value < root.data:
        return search(root.left, value)

    return search(root.right, value)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


root = None

numbers = list(map(int, input("Enter numbers: ").split()))

for number in numbers:
    root = insert(root, number)

print("BST in sorted order:")
inorder(root)

target = int(input("\nEnter number to search: "))

if search(root, target):
    print("Element found.")
else:
    print("Element not found.")
