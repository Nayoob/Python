# Node class represents each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # points to the next node


# LinkedList class manages the list
class LinkedList:
    def __init__(self):
        self.head = None  # start of the list

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_beginning(5)
ll.insert_at_end(30)

ll.display()
