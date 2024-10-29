from BinarySearchTree import TreeNode
from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __int__(self):
        self.pre = float('-inf')

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        # visit the left subtree
        left = self.isValidBST(root.left)

        if root.val <= self.pre:
            return False

        self.pre = root.val

        # visit the right subtree
        right = self.isValidBST(root.right)

        return left and right
