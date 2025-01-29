import random


class RandomizedSet:

    def __init__(self):
        self.indexMap = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.indexMap:
            return False
        self.indexMap[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexMap:
            return False
        index = self.indexMap[val]
        lastElement = self.list[-1]
        if index != len(self.list) - 1:
            self.swap(index, len(self.list) - 1)
        self.indexMap[lastElement] = index
        self.indexMap.pop(val)
        self.list.pop()
        return True

    def swap(self, i, j):
        self.list[i], self.list[j] = self.list[j], self.list[i]

    def getRandom(self) -> int:
        return random.choice(self.list)
