from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
        return self.dfs(jobDifficulty, d - 1, 0)

    def dfs(self, jobDifficulty: List[int], day: int, pos: int) -> int:
        if day == 0:
            # Find the maximum difficulty from `pos` to the end of the array
            cur_max = jobDifficulty[pos]
            for i in range(pos, len(jobDifficulty)):
                cur_max = max(cur_max, jobDifficulty[i])
            return cur_max

        cur_max = float("-inf")
        min_difficulty = float("inf")

        # Try out all ranges for that day
        for i in range(pos, len(jobDifficulty) - day):
            cur_max = max(cur_max, jobDifficulty[i])
            min_difficulty = min(min_difficulty, cur_max + self.dfs(jobDifficulty, day - 1, i + 1))

        return min_difficulty
