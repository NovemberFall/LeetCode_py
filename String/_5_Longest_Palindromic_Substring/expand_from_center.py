class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # odd case
            odd_str = self.extend(s, i, i)
            if len(odd_str) > len(res):
                res = odd_str
            # even case
            even_str = self.extend(s, i, i + 1)
            if len(even_str) > len(res):
                res = even_str
        return res

    def extend(self, s, l, r) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]
