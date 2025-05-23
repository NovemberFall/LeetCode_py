from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if n + m != len(s3):
            return False

        @cache
        def dfs(i, j):
            if i < 0 and j < 0:
                return True

            if i >= 0 and s1[i] == s3[i + j + 1] and dfs(i - 1, j):
                return True
            if j >= 0 and s2[j] == s3[i + j + 1] and dfs(i, j - 1):
                return True

        return dfs(m - 1, n - 1)


'''
    m = 3, n = 4
    i = m - 1 = 2
    j = n - 1 = 3
    len(s3) = m + n - 1 = 6
    k =  len(s3) - 1 = 5
    
    i + j + 1 is the last index of len(s3)
'''