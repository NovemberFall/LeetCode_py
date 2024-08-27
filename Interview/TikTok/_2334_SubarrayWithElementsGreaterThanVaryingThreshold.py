from typing import List


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        prev_small = [-1] * n
        next_small = [n] * n
        stack = []
        stack.append(0)

        for i in range(1, n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                prev_small[i] = stack[-1]
            stack.append(i)

        stack = []
        stack.append(n - 1)
        for i in range(n - 2, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                next_small[i] = stack[-1]
            stack.append(i)

        for i in range(n):
            length = next_small[i] - prev_small[i] - 1
            if (threshold / length) < nums[i]:
                return length

        return -1

