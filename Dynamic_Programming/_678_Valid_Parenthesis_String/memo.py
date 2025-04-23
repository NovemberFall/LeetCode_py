class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        return self.dfs(0, 0, s, dp)

    def dfs(self, index, openCount, str, dp) -> bool:
        if index == len(str):
            return openCount == 0
        if openCount < 0:
            return False
        if dp[index][openCount] != -1:
            return dp[index][openCount] == 1

        isValid = False
        c = str[index]
        if c == '(':
            isValid = self.dfs(index + 1, openCount + 1, str, dp)
        elif c == ')':
            isValid = self.dfs(index + 1, openCount - 1, str, dp)
        else:
            isValid = self.dfs(index + 1, openCount + 1, str, dp) or \
                      self.dfs(index + 1, openCount - 1, str, dp) or \
                      self.dfs(index + 1, openCount, str, dp)

        dp[index][openCount] = isValid
        return isValid