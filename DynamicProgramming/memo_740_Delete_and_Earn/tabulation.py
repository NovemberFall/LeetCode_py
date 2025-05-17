from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = [0] * 10010  # since 1 <= nums[i] <= 10^4
        n = len(nums)
        max_num = 0
        for x in nums:
            count[x] += 1
            max_num = max(max_num, x)

        dp = [[0] * 2 for _ in range(max_num + 1)]
        for i in range(1, max_num + 1):  # i represent current num
            dp[i][1] = dp[i - 1][0] + i * count[i]
            dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])

        return max(dp[max_num][1], dp[max_num][0])


