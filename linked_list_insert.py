class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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

    def insert(self, data, position):
        new_node = Node(data)

        if position < 0:
            print("Invalid position")
            return

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        for _ in range(position - 1):
            if current is None:
                print("Invalid position")
                return
            current = current.next

        if current is None:
            print("Invalid position")
            return

        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


ll = LinkedList()

for n in map(int, input("Enter numbers: ").split()):
    ll.append(n)

value = int(input("Enter value to insert: "))
position = int(input("Enter position (starting from 0): "))

ll.insert(value, position)

print("Updated Linked List:")
ll.display()
