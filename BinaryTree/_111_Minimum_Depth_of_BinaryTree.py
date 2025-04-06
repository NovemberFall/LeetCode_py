# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.dfs(root)

    def dfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return float('inf')

        if root.left is None and root.right is None:
            return 1

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return min(left, right) + 1
