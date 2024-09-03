from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        isPrime = [True] * (right + 1)
        self.generate_primes(isPrime)
        ans = []
        for p in range(left, right + 1):
            if (isPrime[p]):
                ans.append(p)

        if len(ans) <= 1:
            return [-1, -1]
        mn = float('inf')
        n1, n2 = -1, -1
        for i in range(len(ans) - 1):
            if ans[i + 1] - ans[i] == mn:
                if n1 > ans[i]:
                    n1 = ans[i]
                    n2 = ans[i + 1]
            if ans[i + 1] - ans[i] < mn:
                n1 = ans[i]
                n2 = ans[i + 1]
                mn = ans[i + 1] - ans[i]
        return [n1, n2]

    def generate_primes(self, isPrime):
        isPrime[0] = isPrime[1] = False
        n = len(isPrime)
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False
