from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        is_travel_needed = set(days)
        last_day = days[-1]
        dp = [0] * (last_day + 1)

        for day in range(1, last_day + 1):
            if day not in is_travel_needed:
                dp[day] = dp[day - 1]
            else:
                one_day = costs[0] + dp[max(0, day - 1)]
                seven_day = costs[1] + dp[max(0, day - 7)]
                thirty_day = costs[2] + dp[max(0, day - 30)]
                dp[day] = min(one_day, seven_day, thirty_day)

        return dp[last_day]




