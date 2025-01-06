# File: Topic5/doubly_linked_list_dynamic_tracking.py

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
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def remove(self, data):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current and current.data != data:
            current = current.next
        if current is None:
            print(f"{data} not found in the list.")
            return
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == self.head:
            self.head = current.next
        print(f"Removed {data} from the list.")

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Example usage:
dll = DoublyLinkedList()
dll.append("Order1")
dll.append("Order2")
dll.append("Order3")
dll.display()  # Order1 <-> Order2 <-> Order3 <-> None

dll.remove("Order2")
dll.display()  # Order1 <-> Order3 <-> None
