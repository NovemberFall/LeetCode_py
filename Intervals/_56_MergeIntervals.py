from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            prev = res[-1]
            cur = intervals[i]
            if prev[1] >= cur[0]:
                prev[1] = max(prev[1], cur[1])
            else:
                res.append(cur)

        return res