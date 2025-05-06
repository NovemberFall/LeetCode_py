class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None  # Pointer to the first element
        self.tail = None  # Pointer to the last element
        self.size = 0

    def __str__(self):
        cur = self.head
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, value):
        """
        Adds an element to the back of the queue.
        """
        new_node = Node(value)
        if self.isEmpty():
            self.head = self.tail = new_node  # Special case for empty queue
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        """
        Removes and returns the element at the front of the queue.
        Raises an IndexError if the queue is empty.
        """
        if self.isEmpty():
            raise IndexError("Dequeue from empty queue")
        removed = self.head
        self.head = self.head.next
        if self.head is None:  # Handle case where queue becomes empty after dequeue
            self.tail = None
        self.size -= 1
        return removed.value

    def peek(self):
        """
        Returns the element at the front of the queue without removing it.
        Raises an IndexError if the queue is empty.
        """
        if self.isEmpty():
            raise IndexError("Peek from empty queue")
        return self.head.value


# Driver Code
if __name__ == "__main__":
    queue = Queue()
    for i in range(1, 11):
        queue.enqueue(i)
    print(f"Queue: {queue}")
    print(f"Peek: {queue.peek()}")

    for _ in range(1, 6):
        remove = queue.dequeue()
        print(f"Dequeue: {remove}")
    print(f"Queue: {queue}")
    print(f"Peek: {queue.peek()}")
