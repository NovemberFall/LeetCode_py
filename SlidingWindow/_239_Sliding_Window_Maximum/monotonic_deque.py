from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque() # # store indices, values are in decreasing order

        for i, num in enumerate(nums):

            # 1. Maintain decreasing deque
            # Remove all elements smaller than current num
            # because they can never be the maximum
            while dq and nums[dq[-1]] <= num:
                dq.pop()

            # Add current index
            dq.append(i)

            # 2. Remove elements out of the window
            # If the front index is too old (out of window), remove it
            if i - dq[0] >= k:
                dq.popleft()

            # 3. Record result when window is valid
            # The front of deque is always the maximum
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res