from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        # if max(nums1) < 0 and min(nums2) > 0:
        #     return max(nums1) * min(nums2)
        #
        # if min(nums1) > 0 and max(nums2) < 0:
        #     return min(nums1) * max(nums2)

        dp = [[-float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                product = nums1[i - 1] * nums2[j - 1]
                dp[i][j] = max(
                    dp[i - 1][j - 1] + product,  # continue previous subsequence
                    dp[i - 1][j],                # skip nums1[i - 1]
                    dp[i][j - 1],                # skip nums2[j - 1]
                    product                      # start new subsequence with current pair
                )
        return dp[m][n]