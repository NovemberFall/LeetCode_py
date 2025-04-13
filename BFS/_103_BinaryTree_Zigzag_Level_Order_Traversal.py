from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        reverse = False
        q = [root]

        while q:
            size = len(q)
            line = []
            for _ in range(size):
                node = q.pop(0)
                line.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if reverse:
                res.append(line[::-1])
            else:
                res.append(line)

            reverse = not reverse
        return res
