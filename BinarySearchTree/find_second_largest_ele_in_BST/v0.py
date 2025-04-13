# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def secondLargest(self, root):
        """
        input: TreeNode root
        return: int
        """
        # write your solution here
        res = []
        self.dfs(root, res)
        if len(res) < 2:
            return -2147483648
        return res[-2]

    def dfs(self, root, res):
        if root is None:
            return

        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)


"""
   TC = O(N), we have visited every node from this BST.
   SC = O(N), my reslut store all value in ascending order, the space need O(N)
"""
