from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return self.createBST(arr)

    def createBST(self, arr):
        if not arr:
            return None
        return self.bst(arr, 0, len(arr) - 1)

    def bst(self, arr, start, end):
        if start > end:
            return None

        mid = (start + end) >> 1
        root = TreeNode(arr[mid])
        root.left = self.bst(arr, start, mid - 1)
        root.right = self.bst(arr, mid + 1, end)
        return root
