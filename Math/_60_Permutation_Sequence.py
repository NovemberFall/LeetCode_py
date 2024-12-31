class Solution:
    def __init__(self):
        self.count = 0
        self.res = ""

    def getPermutation(self, n: int, k: int) -> str:
        visited = [False] * (n + 1)
        self.dfs(n, k, visited, [])
        return self.res

    def dfs(self, n: int, k: int, visited: list, path: list):
        if self.res:
            return

        if len(path) == n:
            self.count += 1
            if self.count == k:
                self.res = ''.join(map(str, path))
            return

        for i in range(1, n + 1):
            if visited[i]:
                continue

            visited[i] = True
            path.append(i)
            self.dfs(n, k, visited, path)
            path.pop()
            visited[i] = False