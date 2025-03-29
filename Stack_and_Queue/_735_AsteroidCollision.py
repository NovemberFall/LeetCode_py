from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:  # if negative win
                    stack.pop()
                elif diff > 0:
                    a = 0 # set a = 0, means no input push to stack, and it will end the while loop
                else:
                    stack.pop()
                    a = 0

            if a:
                stack.append(a)

        return stack


