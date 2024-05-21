class Node:
    """
    Node class for the doubly linked list.
    """
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """
    DoublyLinkedList class to manage the linked list.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """
        Inserts a new element at the end of the list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        """
        Inserts a new element at the beginning of the list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, prev_node, data):
        """
        Inserts a new element after a specified node.
        """
        if not prev_node:
            print("The given previous node cannot be None")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node
        new_node.prev = prev_node

    def remove(self, data):
        """
        Removes the first occurrence of a value from the list.
        """
        if self.head is None:
            return

        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                elif current == self.tail:
                    self.tail = current.prev
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                current = None  # break the loop after removal
                return
            current = current.next

    def print_list(self):
        """
        Prints the contents of the list in forward order.
        """
        current = self.head
        while current:
            print(current.data, end=" <=> ")
            current = current.next
        print("None")


# Example usage
if __name__ == "__main__":
    my_list = DoublyLinkedList()
    my_list.append(10)
    my_list.append(20)
    my_list.prepend(5)
    my_list.insert_after(my_list.head, 15)
    my_list.print_list()  # Output: 5 <=> 15 <=> 10 <=> 20 <=> None
    my_list.remove(15)
    my_list.print_list()  # Output: 5 <=> 10 <=> 20 <=> None
