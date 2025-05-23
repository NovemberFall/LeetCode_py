from functools import cache
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        @cache
        def dfs(i, j):
            if i == m or j == n:
                return 0

            use = nums1[i] * nums2[j] + dfs(i + 1, j + 1)
            return max(use, dfs(i + 1, j), dfs(i, j + 1))

        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)

        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        return dfs(0, 0)


