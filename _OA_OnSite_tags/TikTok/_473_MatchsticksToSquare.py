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

        def backtracking(index):
            if index == len(matchsticks):
                return True

            for j in range(4):
                if sides[j] + matchsticks[index] > target:
                    continue

                sides[j] += matchsticks[index]
                if backtracking(index + 1):
                    return True
                sides[j] -= matchsticks[index]
            return False


        return backtracking(0)





