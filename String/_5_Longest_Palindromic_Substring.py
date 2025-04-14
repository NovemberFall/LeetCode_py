class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            length = max(len1, len2)

            if length > end - start + 1:
                start = i - (length - 1) // 2
                end = i + length // 2
            print(length, start, end)
        return s[start: end + 1]

    def expandAroundCenter(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1
