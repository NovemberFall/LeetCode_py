class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        if not s or not p:
            return res
        # this map records for each of the distinct characters in s, how many chars are needed.
        # e.g. s = "abbc", map = {'a':1, 'b':2, 'c':1}
        # when we get an instance of 'a' in p, we let count of 'a' decremented by 1
        # and only when the count is from 1 to 0, we have 'a' totally matched.
        counter = self.countMap(p)
        # Record how many distinct chars have been matched
        # mach == len(counter), we find an anagram
        match = 0
        # We have a sliding window of size s.length(), and since the size is fixed,
        # we only need to record the end index of the sliding window
        # Also, when move the sliding window by one step from left to right,
        # what we only need to change is
        # 1. remove the leftmost char at the previous sliding window
        # 2. add the rightmost char at the current sliding window
        slow = 0  # left pointer of the sliding window
        for fast in range(len(s)):
            letter = s[fast]
            if letter in counter:
                counter[letter] -= 1
                if counter[letter] == 0:
                    match += 1
            # When window size reaches the length of p
            if fast - slow + 1 == len(p):
                if match == len(counter):
                    res.append(slow)
                left_char = s[slow]
                if left_char in counter:
                    if counter[left_char] == 0:
                        match -= 1
                    counter[left_char] += 1
                slow += 1

        return res

    def countMap(self, p):
        dict = {}
        for letter in p:
            dict[letter] = dict.get(letter, 0) + 1
        return dict
