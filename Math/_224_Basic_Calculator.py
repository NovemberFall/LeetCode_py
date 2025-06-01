class Solution:
    def calculate(self, s: str) -> int:
        index = [0]

        def evaluate(s):
            curNum = 0
            stack = []
            lastOperator = '+'
            while index[0] < len(s):
                ch = s[index[0]]
                index[0] += 1
                if ch == ' ':
                    continue

                if ch.isdigit():
                    curNum = curNum * 10 + int(ch)
                elif ch == '(':
                    curNum = evaluate(s)
                elif ch in "+-":
                    if lastOperator == '+':
                        stack.append(curNum)
                    elif lastOperator == '-':
                        stack.append(-curNum)
                    lastOperator = ch
                    curNum = 0
                elif ch == ')':
                    break

            # ✅ Final processing to handle the last number
            if lastOperator == '+':
                stack.append(curNum)
            elif lastOperator == '-':
                stack.append(-curNum)

            return sum(stack)

        return evaluate(s)


