class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if (x + y) < target:
            return False
        if x == target or y == target or (x + y) == target:
            return True

        if (x > y):
            return target % self.gcd(x, y) == 0
        else:
            return target % self.gcd(y, x) == 0

    def gcd(self, x, y) -> int:
        if y == 0:
            return x
        return self.gcd(y, x % y)

