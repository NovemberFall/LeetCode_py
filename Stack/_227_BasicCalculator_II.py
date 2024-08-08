class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip() # Remove leading/trailing whitespace
        stack = [] # use a list as a stack
        lastSign = '+'
        num = 0

        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            if not c.isdigit() and c != ' ' or i == len(s) - 1:  # End of number or string
                if lastSign == '+':
                    stack.append(num)
                    lastSign = c
                elif lastSign == '-':
                    stack.append(-num)
                    lastSign = c
                elif lastSign == '*':
                    stack.append(stack.pop() * num)
                    lastSign = c
                elif lastSign == '/':
                    stack.append(int(stack.pop() / num)) # Ensure integer division
                    lastSign = c
                num = 0

        return sum(stack)
