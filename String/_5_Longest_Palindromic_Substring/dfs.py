class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        self.dfs(0, s)
        return self.res

    def dfs(self, start, s):
        if start == len(s):
            return

        for end in range(start, len(s)):
            # check substring s[start:end]
            if self.is_palindrome(s, start, end):
                if end - start + 1 > len(self.res):
                    self.res = s[start:end + 1]
        self.dfs(start + 1, s)

    def is_palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
