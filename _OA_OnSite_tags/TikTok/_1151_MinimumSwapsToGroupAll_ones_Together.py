from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        if len(data) < 3:
            return 0

        # count the total number of 1
        oneCnt = 0
        for num in data:
            oneCnt += num

        maxOneCnt, curOneCnt = 0, 0
        left, right = 0, 0
        while right < len(data):
            if right - left < oneCnt:
                curOneCnt += data[right]
            else:
                curOneCnt += data[right]
                curOneCnt -= data[left]
                left += 1

            if right - left + 1 == oneCnt:
                maxOneCnt = max(maxOneCnt, curOneCnt)

            right += 1


        return oneCnt - maxOneCnt

