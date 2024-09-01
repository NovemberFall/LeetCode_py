from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isBST(root, float('-inf'), float('inf'))

    def isBST(self, root: TreeNode, left: float, right: float) -> bool:
        if root is None:
            return True

        x = root.val

        if left < x < right:
            return self.isBST(root.left, left, x) and self.isBST(root.right, x, right)

        return False