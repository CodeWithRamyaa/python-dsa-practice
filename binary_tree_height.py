class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_height(root):
    if root is None:
        return 0

    return 1 + max(
        tree_height(root.left),
        tree_height(root.right)
    )


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)

print("Tree height:", tree_height(root))
