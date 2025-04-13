import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        k = len(nums)
        maxVal = -float('inf')  # get the max value in heap
        for i in range(len(nums)):
            # insert every first element in each array
            if len(nums[i]):
                heap.append((nums[i][0], i, 0))  # (value, array_index, element_index)
                maxVal = max(nums[i][0], maxVal)

        heapq.heapify(heap)
        # res is a 2-element array
        # res[0]: lower bound, res[1]: upper bound
        res = [-float('inf'), float('inf')]
        while len(heap) == k:
            minVal, array_index, ele_index = heapq.heappop(heap)
            # update the result
            # compare the current range maxVal - minVal to the range in result
            if maxVal - minVal < res[1] - res[0]:
                res = [minVal, maxVal]
            if ele_index < len(nums[array_index]) - 1:
                # update the maxVal when we want to insert element in heap
                maxVal = max(maxVal, nums[array_index][ele_index + 1])
                heapq.heappush(heap, (nums[array_index][ele_index + 1], array_index, ele_index + 1))
        return res

