class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        stk.append(-1)
        maxLen = 0
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(i)
            else:
                stk.pop()
                if not stk:
                    stk.append(i)
                else:
                    maxLen = max(maxLen, i - stk[-1])

        return maxLen
