class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins or self.mins[-1] >= val:
            self.mins.append(val)

    def pop(self) -> None:
        if not self.stack:
            return -1
        item = self.stack.pop()
        if item == self.mins[-1]:
            self.mins.pop()
        return item


    def top(self) -> int:
        if not self.stack:
            return -1
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.mins:
            return -1
        return self.mins[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()