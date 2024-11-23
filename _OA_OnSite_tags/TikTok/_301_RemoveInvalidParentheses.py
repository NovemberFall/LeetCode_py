from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        self.helper(res, s, 0, 0, ['(', ')'])
        return res

    def helper(self, res: List[str], s: str, left: int, right: int, pair: List[str]):
        stack = 0
        for right in range(right, len(s)):
            if s[right] == pair[0]:
                stack += 1
            if s[right] == pair[1]:
                stack -= 1
            if stack < 0:  # If stack becomes negative, it means there are more `)` than `(`, indicating an invalid parentheses sequence.
                break      # The break statement is executed, immediately exiting the for loop

        if stack < 0:  # if `)` is more than `(`
            for left in range(left, right + 1):
                if s[left] != pair[1]:
                    continue
                if left > 0 and s[left] == s[left - 1]:
                    continue

                # remove first `)` from `( ) )`
                self.helper(res, s[:left] + s[left + 1:], left, right, pair)
        elif stack > 0:  # if `(` is more than `)`
            # reverse the current str, `((())` => `))(((`, handle the current str from begining
            self.helper(res, s[::-1], 0, 0, [')', '('])
        elif stack == 0:
            res.append(s if pair[0] == '(' else s[::-1])



