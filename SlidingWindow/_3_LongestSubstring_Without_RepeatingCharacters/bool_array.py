class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        window = set()
        left = 0

        for right, c in enumerate(s):
            while c in window:
                window.remove(s[left])
                left += 1
            window.add(c)
            maxLen = max(maxLen, right - left + 1)
        return maxLen