class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSumLeafToRoot(self, root):
        """
        input: TreeNode root
        return: int
        """
        # write your solution here
        if root is None:
            return 0
        self.maxPathSum = float('-inf')
        self.dfs(root, 0)
        return self.maxPathSum

    def dfs(self, node, curSum):
        if node is None:
            return
        if node.left is None and node.right is None:
            self.maxPathSum = max(self.maxPathSum, curSum + node.val)
            return

        self.dfs(node.left, curSum + node.val)
        self.dfs(node.right, curSum + node.val)
        return