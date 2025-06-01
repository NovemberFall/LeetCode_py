from typing import List


class ProductOfArrayExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = [1] * n
        postfix = [1] * n

        # Fill prefix array
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]

        # Fill postfix array
        postfix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]

        # Calculate result array
        for i in range(n):
            if i - 1 < 0:
                res[i] = postfix[i + 1] * 1
                continue
            if i + 1 >= n:
                res[i] = prefix[i - 1] * 1
                continue
            res[i] = prefix[i - 1] * postfix[i + 1]

        return res




