# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.construct(nums, 0, len(nums) - 1)

    def construct(self, nums, left, right):
        if left > right:
            return None

        mid = (left + right) >> 1
        root = TreeNode(nums[mid])
        root.left = self.construct(nums, left, mid - 1)
        root.right = self.construct(nums, mid + 1, right)
        return root
