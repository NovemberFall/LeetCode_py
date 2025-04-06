# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        return self.dfs(root, 0, targetSum)

    def dfs(self, root, partial, target):
        if root is None:
            return False

        partial += root.val
        if root.left is None and root.right is None:
            return partial == target

        return self.dfs(root.left, partial, target) or self.dfs(root.right, partial, target)
