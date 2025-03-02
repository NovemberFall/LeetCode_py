class Solution:
    maxLen = float('-inf')
    res = ""

    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            # odd-len palindormes
            oddLeft, oddRight = i, i
            self.extendPalindrome(s, oddLeft, oddRight)

            # even-len palindormes
            evenLeft, evenRight = i, i + 1
            self.extendPalindrome(s, evenLeft, evenRight)
        return self.res

    def extendPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > self.maxLen:
                self.res = s[left: right + 1]
                self.maxLen = (right - left + 1)
            left -= 1
            right += 1
