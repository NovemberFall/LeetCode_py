from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize DP array where dp[i] is the fewest coins needed to make amount i
        # Set all to amount+1 (a value greater than any possible answer)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed to make amount 0

        # Build up the solution for each amount from 1 to amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    # If the coin can be used, update dp[i] if this coin gives a better result
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # If dp[amount] was updated, return it; otherwise, return -1 (amount can't be formed)
        return dp[amount] if dp[amount] != amount + 1 else -1