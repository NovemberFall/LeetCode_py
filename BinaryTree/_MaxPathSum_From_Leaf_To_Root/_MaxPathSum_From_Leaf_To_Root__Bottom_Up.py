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
            return -float('inf')

        # when it is a leaf node
        if root.left is None and root.right is None:
            return root.val
        leftTree = self.maxPathSumLeafToRoot(root.left)
        rightTree = self.maxPathSumLeafToRoot(root.right)
        return max(leftTree, rightTree) + root.val