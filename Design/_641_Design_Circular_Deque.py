class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.size = 0
        self.items = [None] * k
        self.first = 0
        self.last = k - 1

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.first = (self.first - 1 + len(self.items)) % len(self.items)
        self.items[self.first] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.last = (self.last + 1) % len(self.items)
        self.items[self.last] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.first = (self.first + 1) % len(self.items)
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.last = (self.last - 1 + len(self.items)) % len(self.items)
        self.size -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        :rtype: int
        """
        return -1 if self.isEmpty() else self.items[self.first]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        :rtype: int
        """
        return -1 if self.isEmpty() else self.items[self.last]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.size == len(self.items)

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


def test():
    # Initialize deque with capacity 3
    deque = MyCircularDeque(3)

    # Print initiliaze
    print("first:", deque.first, "last:", deque.last)

    # Test insertLast
    print(deque.insertLast(10), "deque.items:", deque.items, "first:", deque.first, "last:", deque.last)  # True
    print(deque.insertLast(20), "deque.items:", deque.items, "first:", deque.first, "last:", deque.last)  # True

    # Test insertFront
    print(deque.insertFront(5), "deque.items:", deque.items, "first:", deque.first, "last:", deque.last)  # True
    print(deque.insertFront(1), "deque.items:", deque.items, "first:", deque.first, "last:", deque.last)  # True

    # Test getFront and getRear
    print(deque.getFront(), "first:", deque.first, "last:", deque.last)  # 1
    print(deque.getRear(), "first:", deque.first, "last:", deque.last)  # 20



if __name__ == "__main__":
    print("test:")
    test()


