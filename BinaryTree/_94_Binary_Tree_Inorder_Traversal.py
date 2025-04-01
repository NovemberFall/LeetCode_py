# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        stk = [(root, 1)]
        while stk:
            node, count = stk.pop()
            if count == 1:
                stk.append((node, count + 1))
                if node.left:
                    stk.append((node.left, 1))
            if count == 2:
                stk.append((node, count + 1))
                if node.right:
                    stk.append((node.right, 1))
            if count == 3:
                continue

        return res