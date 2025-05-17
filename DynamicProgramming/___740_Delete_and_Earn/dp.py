from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = max(nums)
        count = [0] * (max_num + 1)
        for x in nums:
            count[x] += x  # accumulate points for number x

        # start DP operations to calculate the final result:
        dp = [0] * (max_num + 1)
        dp[0] = count[0]
        dp[1] = max(count[0], count[1])
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + count[i])
        return dp[max_num]



