class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def count_leaf_nodes(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Leaf nodes:", count_leaf_nodes(root))
