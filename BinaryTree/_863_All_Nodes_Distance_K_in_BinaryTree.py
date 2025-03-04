from typing import List

from BinaryTree import TreeNode


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.add_parent(root, None)
        ans = []
        visited = set()
        self.dfs(target, visited, ans, k)
        return ans

    def add_parent(self, cur, parent):
        if cur is None:
            return
        if cur:
            cur.parent = parent
            self.add_parent(cur.left, cur)
            self.add_parent(cur.right, cur)

    def dfs(self, cur, visited, ans, distance):
        if not cur:
            return
        if cur in visited:
            return
        visited.add(cur)
        if distance == 0:
            ans.append(cur.val)
            return
        self.dfs(cur.parent, visited, ans, distance - 1)
        self.dfs(cur.left, visited, ans, distance - 1)
        self.dfs(cur.right, visited, ans, distance - 1)
