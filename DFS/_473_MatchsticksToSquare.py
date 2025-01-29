from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        size = len(matchsticks)
        if matchsticks is None or size < 4:
            return False
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total / 4
        sides = [0] * 4
        matchsticks.sort(reverse=True)

        return self.backtracking(matchsticks, sides, target, 0)

    def backtracking(self, matchstricks, sides, target, index: int) -> bool:
        if index == len(matchstricks):
            return True

        for i in range(4):
            if sides[i] + matchstricks[index] <= target:
                sides[i] += matchstricks[index]
                if self.backtracking(matchstricks, sides, target, index + 1):
                    return True
                sides[i] -= matchstricks[index]
        return False
