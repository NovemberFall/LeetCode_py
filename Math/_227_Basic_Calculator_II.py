class Solution:
    def calculate(self, s: str) -> int:
        index = [0]

        def evaluate(s: str) -> int:
            stack = []
            curNum = 0
            lastOperator = "+"

            while index[0] < len(s):
                curChar = s[index[0]]
                index[0] += 1

                if curChar == ' ':
                    continue
                if curChar.isdigit():
                    curNum = curNum * 10 + int(curChar)
                else:
                    if lastOperator == '+':
                        stack.append(curNum)
                    elif lastOperator == '-':
                        stack.append(-curNum)
                    elif lastOperator == '*':
                        stack.append(stack.pop() * curNum)
                    else:
                        stack.append(int(stack.pop() / curNum))

                    lastOperator = curChar
                    curNum = 0

            if lastOperator == '+':
                stack.append(curNum)
            elif lastOperator == '-':
                stack.append(-curNum)
            elif lastOperator == '*':
                stack.append(stack.pop() * curNum)
            else:
                stack.append(int(stack.pop() / curNum))

            return sum(stack)

        return evaluate(s)

