class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rmfreq = [0] * 60
        res = 0
        for t in time:
            if t % 60 == 0:
                res += rmfreq[0]
            else:
                res += rmfreq[60 - t % 60]
            rmfreq[t % 60] += 1
        return res