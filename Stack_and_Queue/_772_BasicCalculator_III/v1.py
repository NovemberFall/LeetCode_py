class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur = 0
        previous_operator = "+"
        s += "@"
        for c in s:
            if c == " ":
                continue
            if c.isdigit():
                cur = cur * 10 + int(c)
            else:
                if previous_operator in "*/":
                    stack.append(self.evaluate(previous_operator, stack.pop(), cur))
                else:
                    stack.append(self.evaluate(previous_operator, cur))
                cur = 0
                previous_operator = c
        return sum(stack)

    def evaluate(self, operator, x, y):
        if operator == "+":
            return x
        if operator == "-":
            return -x
        if operator == "*":
            return x * y
        if operator == "/":
            return int(x / y)
