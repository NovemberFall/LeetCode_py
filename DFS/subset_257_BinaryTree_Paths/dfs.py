# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        path = []

        def dfs(root: TreeNode) -> None:
            if root is None:
                return
            path.append(str(root.val))
            if root.left is None and root.right is None:
                res.append("->".join(path))
            else:
                dfs(root.left)
                dfs(root.right)
            path.pop()
        dfs(root)
        return res