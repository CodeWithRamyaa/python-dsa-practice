class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data if slow else None


head = None
current = None

numbers = list(map(int, input("Enter numbers: ").split()))

for number in numbers:
    new_node = Node(number)

    if head is None:
        head = new_node
        current = new_node
    else:
        current.next = new_node
        current = new_node

print("Middle element:", find_middle(head))
