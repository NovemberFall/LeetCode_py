from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inMap = {}
        for i in range(len(inorder)):
            inMap[inorder[i]] = i

        return self.construct(inMap, preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def construct(self, inMap, preorder, pLeft, pRight, inorder, inLeft, inRight):
        if pLeft > pRight:
            return None

        root = TreeNode(preorder[pLeft])
        leftSize = inMap[preorder[pLeft]] - inLeft
        root.left = self.construct(inMap, preorder, pLeft + 1, pLeft + leftSize, inorder, inLeft, inLeft + leftSize - 1)
        root.right = self.construct(inMap, preorder, pLeft + leftSize + 1, pRight, inorder, inLeft + leftSize + 1,inRight)
        return root