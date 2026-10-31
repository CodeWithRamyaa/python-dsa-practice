class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def display_forward(self):
        current = self.head

        while current:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")

    def display_backward(self):
        current = self.head

        if not current:
            print("None")
            return

        while current.next:
            current = current.next

        while current:
            print(current.data, end=" <-> ")
            current = current.prev

        print("None")


dll = DoublyLinkedList()

for n in map(int, input("Enter numbers: ").split()):
    dll.append(n)

print("Forward:")
dll.display_forward()

print("Backward:")
dll.display_backward()
