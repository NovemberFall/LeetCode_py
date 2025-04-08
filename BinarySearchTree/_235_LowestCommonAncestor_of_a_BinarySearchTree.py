class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        val = root.val
        pVal = p.val
        qVal = q.val
        if val > pVal and val > qVal:
            return self.lowestCommonAncestor(root.left, p, q)
        elif val < pVal and val < qVal:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
