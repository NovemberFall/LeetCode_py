class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        window = set()
        slow, fast = 0, 0

        while fast < len(s):
            if s[fast] not in window:
                window.add(s[fast])
                fast += 1
            else:
                window.remove(s[slow])
                slow += 1

            maxLen = max(maxLen, len(window))

        return maxLen