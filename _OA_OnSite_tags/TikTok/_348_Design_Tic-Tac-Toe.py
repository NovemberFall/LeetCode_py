class TicTacToe:

    def __init__(self, n: int):
        self.size = n
        self.diagonal = 0
        self.anti_diagonal = 0
        self.rows = [0] * n
        self.cols = [0] * n

    def move(self, row: int, col: int, player: int) -> int:
        player_id = 1 if player == 1 else -1

        if row == col:
            self.diagonal += player_id
            if self.diagonal == self.size or self.diagonal == -self.size:
                return player

        if row + col + 1 == self.size:
            self.anti_diagonal += player_id
            if self.anti_diagonal == self.size or self.anti_diagonal == -self.size:
                return player

        self.rows[row] += player_id
        self.cols[col] += player_id

        if self.rows[row] == self.size or self.rows[row] == -self.size or self.cols[col] == self.size or self.cols[col] == -self.size:
            return player

        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)