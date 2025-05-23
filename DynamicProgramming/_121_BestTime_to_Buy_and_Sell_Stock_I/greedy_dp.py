from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Max profit found so far (start at 0, as no transaction gives 0 profit)
        max_profit = 0
        # Minimum price seen so far (initialize with the first day's price)
        min_price = prices[0]

        # Iterate through prices starting from the second day
        for i in range(1, len(prices)):
            cur_price = prices[i]

            # Calculate profit if selling today
            potential_profit = cur_price - min_price

            # Update max profit if selling today gives more profit
            max_profit = max(max_profit, potential_profit)

            # Update the minimum price seen so far
            min_price = min(min_price, cur_price)

        # Return the overall maximum profit
        return max_profit