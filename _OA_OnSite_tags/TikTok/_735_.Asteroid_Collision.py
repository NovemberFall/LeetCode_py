from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for a in asteroids:
            while stk and stk[-1] > 0 and a < 0:
                diff = stk[-1] + a
                if diff > 0:
                    a = 0
                elif diff < 0:
                    stk.pop()
                else:
                    stk.pop()
                    a = 0

            if a != 0:
                stk.append(a)

        return stk