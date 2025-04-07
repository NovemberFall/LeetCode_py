# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        input: TreeNode root
        return: int
        """
        # write your solution here
        if root is None:
            return 0
        self.res = root.val
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, prev):
        if root is None:
            return
        if prev < 0:
            cur = root.val
        else:
            cur = prev + root.val
        self.res = max(self.res, cur)

        self.dfs(root.left, cur)
        self.dfs(root.right, cur)

