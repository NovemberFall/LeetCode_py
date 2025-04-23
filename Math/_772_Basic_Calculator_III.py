class Solution:
    def calculate(self, s: str) -> int:
        self.index = 0
        return self.evaluate(s + "+")

    def evaluate(self, s: str) -> int:
        stack = []
        lastOperator = '+'
        curNum = 0
        while self.index < len(s):
            curChar = s[self.index]
            self.index += 1
            if curChar == ' ':
                continue
            if curChar.isdigit():
                curNum = curNum * 10 + int(curChar)
            elif curChar == '(':
                curNum = self.evaluate(s)
            else:
                if lastOperator == '+':
                    stack.append(curNum)
                elif lastOperator == '-':
                    stack.append(-curNum)
                elif lastOperator == '*':
                    stack.append(stack.pop() * curNum)
                elif lastOperator == '/':
                    stack.append(int(stack.pop() / curNum))

                lastOperator = curChar
                curNum = 0
                if curChar == ')':
                    break

        return sum(stack)
