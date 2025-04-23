class Solution:
    def calculate(self, s: str) -> int:
        self.index = 0
        return self.evaluate(s + "+")

    def evaluate(self, s: str) -> int:
        stack = []
        curNum = 0
        lastOperator = "+"

        while self.index < len(s):
            curChar = s[self.index]
            self.index += 1

            if curChar == ' ':
                continue
            if curChar.isdigit():
                curNum = curNum * 10 + int(curChar)
            else:
                if lastOperator == "+":
                    stack.append(curNum)
                elif lastOperator == "-":
                    stack.append(-curNum)
                elif lastOperator == "*":
                    stack.append(stack.pop() * curNum)
                elif lastOperator == "/":
                    # Perform previous '/' operation
                    # Use int(a / b) for integer division that truncates towards zero (like Java)
                    # Note: Python's // operator floors, which differs for negative results.
                    stack.append(int(stack.pop() / curNum))
                lastOperator = curChar
                curNum = 0
        return sum(stack)