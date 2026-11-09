class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    if root is None:
        return None

    if root.value == p or root.value == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

result = lowest_common_ancestor(root, 4, 5)

if result:
    print("Lowest common ancestor:", result.value)
else:
    print("Ancestor not found")
