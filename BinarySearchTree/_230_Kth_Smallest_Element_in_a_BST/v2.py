# Definition for a binary tree node.
from typing import Optional


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.res = 0

        self.dfs(root, k)
        return self.res

    def dfs(self, root, k):
        if not root:
            return

        self.dfs(root.left, k)

        self.cnt += 1
        if self.cnt == k:
            self.res = root.val

        self.dfs(root.right, k)