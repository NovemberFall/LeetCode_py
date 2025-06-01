from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result_set = set()
        n = len(s)
        max_score = 0
        max_len = 0

        # Calculate max number of matched parentheses
        l = r = 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                r += 1
        max_score = min(l, r)

        def dfs(index: int, curStr: List[str], score: int):
            nonlocal max_len
            if score < 0 or score > max_score:
                return
            if index == n:
                if score == 0 and len(curStr) >= max_len:
                    candidate = ''.join(curStr)
                    if len(curStr) > max_len:
                        result_set.clear()
                        max_len = len(curStr)
                    result_set.add(candidate)
                return

            c = s[index]
            if c == '(':
                dfs(index + 1, curStr, score)  # Not use '('
                curStr.append(c)  # Use '('
                dfs(index + 1, curStr, score + 1)
                curStr.pop()
            elif c == ')':
                dfs(index + 1, curStr, score)  # Not use ')'
                curStr.append(c)  # Use ')'
                dfs(index + 1, curStr, score - 1)
                curStr.pop()
            else:
                curStr.append(c)
                dfs(index + 1, curStr, score)
                curStr.pop()

        dfs(0, [], 0)
        return list(result_set)
