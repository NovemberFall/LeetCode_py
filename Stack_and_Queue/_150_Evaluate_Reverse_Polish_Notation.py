from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token == '+':
                r, l = stk.pop(), stk.pop()
                stk.append(l + r)
            elif token == '-':
                r, l = stk.pop(), stk.pop()
                stk.append(l - r)
            elif token == '*':
                r, l = stk.pop(), stk.pop()
                stk.append(l * r)
            elif token == '/':
                r, l = stk.pop(), stk.pop()
                stk.append(int(l / r))
            else:
                stk.append(int(token))
        assert len(stk) == 1
        return stk[-1]