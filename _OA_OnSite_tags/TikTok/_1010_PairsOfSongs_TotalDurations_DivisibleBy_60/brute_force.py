from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        n = len(time)
        for i in range(n):
            for j in range(i + 1, n):
                res += (time[i] + time[j]) % 60 == 0
        return res