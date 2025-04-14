class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = dict()
        for c in s:
            if c not in hash:
                hash[c] = 0
            hash[c] += 1
        for i in range(len(s)):
            if hash[s[i]] == 1:
                return i
        return -1