from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['' for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                board[i][j] = '.'

        self.dfs(res, board, n, 0)
        return res

    def dfs(self, res:list[list[str]], board: list[list[str]], n: int, rowIndex: int) -> None:
        if rowIndex == n:
            level = []
            for row in board:
                sb = []
                sb.append(row)
                level.append(sb)
            res.append(level)
            return

        for colIndex in range(n):
            if self.isValid(rowIndex, colIndex, n, board):
                board[rowIndex][colIndex] = 'Q'
                self.dfs(res, board, n, rowIndex + 1)
                board[rowIndex][colIndex] = '.'

    def isValid(self, rowIndex, colIndex, n, board):
        for i in range(rowIndex):
            if board[i][colIndex] == 'Q':
                return False

        i, j = rowIndex - 1, colIndex - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i, j = rowIndex - 1, colIndex + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

