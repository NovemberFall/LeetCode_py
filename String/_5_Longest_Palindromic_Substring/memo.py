class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        self.s = s
        self.dp = {}  # add memo
        self.dfs(0)
        return self.res

    def dfs(self, start):
        if start == len(self.s):
            return
        for end in range(start, len(self.s)):
            if self.is_palindrome(start, end):
                if end - start + 1 > len(self.res):
                    self.res = self.s[start:end + 1]
        self.dfs(start + 1)

    def is_palindrome(self, l, r):
        if (l, r) in self.dp:
            return self.dp[(l, r)]

        # base case
        if l >= r:
            self.dp[(l, r)] = True
            return True

        if self.s[l] == self.s[r] and self.is_palindrome(l + 1, r - 1):
            self.dp[(l, r)] = True
        else:
            self.dp[(l, r)] = False
        return self.dp[(l, r)]