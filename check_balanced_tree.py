class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def check_balance(root):
    if root is None:
        return 0

    left_height = check_balance(root.left)

    if left_height == -1:
        return -1

    right_height = check_balance(root.right)

    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return 1 + max(left_height, right_height)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

if check_balance(root) == -1:
    print("Tree is not balanced")
else:
    print("Tree is balanced")
