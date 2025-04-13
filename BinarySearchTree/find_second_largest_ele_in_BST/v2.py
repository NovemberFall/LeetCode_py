# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution(object):
#     def secondLargest(self, root):
#         """
#         input: TreeNode root
#         return: int
#         """
#         # write your solution here
#         res = []
#         self.dfs(root, res)
#         if len(res) < 2:
#             return -2147483648
#         return res[-2]



