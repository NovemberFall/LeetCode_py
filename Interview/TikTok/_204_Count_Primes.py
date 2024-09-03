class Solution:
    def countPrimes(self, n: int) -> int:
        # Step 1: Initialize the isPrime array
        isPrime = [True] * n

        # Step 2: Iterate from 2 to sqrt(n)
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                # Mark multiples of i as non-prime
                for j in range(i * i, n, i): # j takes on the values i * i, i * i + i, i * i + 2 * i, ..., n in each iteration.
                    isPrime[j] = False

        # Step 3: Count the remaining prime numbers
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count