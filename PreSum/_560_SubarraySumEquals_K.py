from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = [0] * (len(nums) + 1)

        # Calculate prefix sum
        for i in range(1, len(nums) + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]

        count = 0
        preSumMap = {} # Use a dictionary (similar to HashMap)

        for i in range(len(preSum)):
            if (preSum[i] - k) in preSumMap:
                count += preSumMap[preSum[i] - k]

            preSumMap[preSum[i]] = preSumMap.get(preSum[i], 0) + 1

        return count
