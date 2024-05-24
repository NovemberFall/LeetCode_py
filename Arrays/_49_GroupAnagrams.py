from typing import List

class _49_groupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} # mapping charCount to List of Anagrams

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord('a')] += 1

            # Convert the list to a tuple to use it as a dictionary key
            key = tuple(count)
            if key not in res:
                res[key] = []
            res[key].append(s)

        return list(res.values())