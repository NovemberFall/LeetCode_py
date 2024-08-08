from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, word, 0):
                    return True
        return False

    def dfs(self, board: List[List[str]], i: int, j: int, word: str, index: int) -> bool:
        if index == len(word):
            return True

        if (i < 0 or i >= len(board)) or (j < 0 or j >= len(board[0])) or board[i][j] != word[index]:
            return False

        tmp = board[i][j]
        board[i][j] = '*'

        res = (self.dfs(board, i + 1, j, word, index + 1) or
               self.dfs(board, i, j + 1, word, index + 1) or
               self.dfs(board, i - 1, j, word, index + 1) or
               self.dfs(board, i, j - 1, word, index + 1))

        board[i][j] = tmp
        return res
