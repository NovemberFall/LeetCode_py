class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        res = 0
        lastSign = 1;
        stack = [] # Use a list as a stack

        for i in range(len(s)):
            c = s[i]
            if c == ' ':
                continue
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '+':
                res += lastSign * num
                num = 0
                lastSign = 1
            elif c == '-':
                res += lastSign * num
                num = 0
                lastSign = -1
            elif c == '(':
                stack.append(res)
                stack.append(lastSign)
                lastSign = 1
                res = 0
            elif c == ')':
                res += lastSign * num
                num = 0
                res *= stack.pop() # Sign before parenthesis
                res += stack.pop() # Result calculated before parenthesis

        if num != 0:
            res += lastSign * num

        return res