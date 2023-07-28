class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a new node at the end
    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    # Function to print the list
    def print_list(self):
        if self.head is None:
            print("List is empty")
            return

        if self.is_circular():
            current = self.head
            print(current.data, end=" ")
            while current.next != self.head:
                current = current.next
                print(current.data, end=" ")
        else:
            current = self.head
            print(current.data, end=" ")
            while current.next:
                current = current.next
                print(current.data, end=" ")
        print()

    # Function to convert the singly linked list to a circular linked list
    def convert_to_circular(self):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = self.head  # Make the last node point to the head

    # Function to check if the linked list is circular
    def is_circular(self):
        if self.head is None:
            return False

        current = self.head.next
        while current and current is not self.head:
            current = current.next

        return current == self.head


# Testing
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(3)
linked_list.insert(2)
linked_list.insert(4)

print("Original List:")
linked_list.print_list()

linked_list.convert_to_circular()
print("Converted to Circular Linked List:")
linked_list.print_list()
