import heapq
from typing import List


# class Solution:
#     def kSmallestPairs(self, nums1: __List[int], nums2: __List[int], k: int) -> __List[__List[int]]:
#         max_heap = []
#         for i in range(len(nums1)):
#             for j in range(len(nums2)):
#                 two_sum = nums1[i] + nums2[j]
#                 if len(max_heap) < k:
#                     heapq.heappush(max_heap, (-two_sum, [nums1[i], nums2[j]]))
#                 else:
#                     if -max_heap[0][0] > two_sum:
#                         heapq.heappush(max_heap, (-two_sum, [nums1[i], nums2[j]]))
#                         heapq.heappop(max_heap)
#
#         sorted_heap = sorted(max_heap, key=lambda x: -x[0])
#         result = []
#         while sorted_heap:
#             _, pair = sorted_heap.pop(0)
#             result.append(pair)
#         return result
#         # return [pair for _, pair in sorted(max_heap, key=lambda x: -x[0])]