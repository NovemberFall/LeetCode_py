from random import random


class RandomizedSet:

    def __init__(self):
        self.map = dict()
        self.list = list()

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        index = self.map[val]
        lastElement = self.list[-1]
        if index != len(self.list) - 1:
            self.swap(index, len(self.list) - 1)
        self.map[lastElement] = index
        self.map.pop(val)
        self.list.pop()
        return True

    def swap(self, i, j):
        self.list[i], self.list[j] = self.list[j], self.list[i]

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()