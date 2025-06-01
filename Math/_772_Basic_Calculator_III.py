class Solution:
    def calculate(self, s: str) -> int:
        index = [0]

        def evaluate(s: str) -> int:
            stack = []
            lastOperator = '+'
            curNum = 0
            while index[0] < len(s):
                curChar = s[index[0]]
                index[0] += 1
                if curChar == ' ':
                    continue
                if curChar.isdigit():
                    curNum = curNum * 10 + int(curChar)
                elif curChar == '(':
                    curNum = evaluate(s)
                elif curChar in "+-*/":
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
                elif curChar == ')':
                    break;

            if lastOperator == '+':
                stack.append(curNum)
            elif lastOperator == '-':
                stack.append(-curNum)
            elif lastOperator == '*':
                stack.append(stack.pop() * curNum)
            elif lastOperator == '/':
                stack.append(int(stack.pop() / curNum))
            return sum(stack)

        return evaluate(s + "+")
