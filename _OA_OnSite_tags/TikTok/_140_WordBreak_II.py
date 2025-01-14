from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        res = []
        count = [0] * 26

        # Count characters in the dictionary words
        for word in wordDict:
            for c in word:
                count[ord(c) - ord('a')] += 1

        # Check if all characters in `s` exist in the dictionary
        for c in s:
            if count[ord(c) - ord('a')] == 0:
                return res

        # Convert wordDict to a set for fast lookups
        wordSet = set(wordDict)

        # Call DFS helper function
        self.dfs(s, 0, len(s), [], res, wordSet)
        return res

    def dfs(self, s: str, index: int, n: int, cur: list[str], res: list[str], wordSet: set[str]) -> None:
        if index == n:
            res.append(" ".join(cur))
            return

        for i in range(index, n):
            if s[index:i + 1] in wordSet:
                cur.append(s[index:i + 1])
                self.dfs(s, i + 1, n, cur, res, wordSet)
                cur.pop()  # Backtrack
