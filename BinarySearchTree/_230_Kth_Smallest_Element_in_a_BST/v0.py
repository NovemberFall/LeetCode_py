# Definition for a binary tree node.
from typing import Optional


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.dfs(root, res)
        return res[k - 1]

    def dfs(self, root, res):
        if not root:
            return

        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)
