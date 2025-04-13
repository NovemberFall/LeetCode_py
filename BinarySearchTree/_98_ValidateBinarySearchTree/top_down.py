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

        if not (left < root.val < right):
            return False

        return self.isBST(root.left, left, root.val) and self.isBST(root.right, root.val, right)
