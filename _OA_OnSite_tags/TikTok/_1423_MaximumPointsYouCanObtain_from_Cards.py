from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        res = 0
        for p in cardPoints[:k]:
            res += p
        # res = sum(cardPoints[:k]

        cur = res

        # range(start, stop, step)
        for i in range(k - 1, -1, -1):
            cur -= cardPoints[i]
            cur += cardPoints[len(cardPoints) - k + i]
            res = max(res, cur)

        return res


