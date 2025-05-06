# stack implementation using a linked list.
# node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    # Initializing a stack.
    def __init__(self):
        self.head = None
        self.size = 0

    # String representation of the stack
    def __str__(self):
        cur = self.head
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    # Get the current size of the stack
    def getSize(self):
        return self.size

    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0

    # Get the top item of the stack
    def peek(self):
        # Sanitary check to see if we are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.value

    # Push a value into the stack.
    def push(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node # Special case for empty stack
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1


    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        removed = self.head
        self.head = self.head.next
        self.size -= 1
        return removed.value


# Driver Code
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")