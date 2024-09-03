class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:
    def __init__(self):
        self.array = [None] * 10_000

    def put(self, key: int, value: int) -> None:
        index = self.getIndex(key)
        head = self.array[index]
        node = head
        while node:
            if node.key == key:
                node.val = value
                return
            node = node.next

        new_node = Node(key, value)
        new_node.next = self.array[index]
        self.array[index] = new_node

    def getIndex(self, key: int) -> int:
        return hash(key) % len(self.array)

    def get(self, key: int) -> int:
        index = self.getIndex(key)
        node = self.array[index]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        index = self.getIndex(key)
        node = self.array[index]
        prev = None
        while node:
            if node.key == key:
                if prev is None:
                    self.array[index] = node.next
                if prev:
                    prev.next = node.next
                return
            prev = node
            node = node.next

