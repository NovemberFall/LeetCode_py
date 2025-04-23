from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.is_travel_needed = set(days)
        self.last_day = days[-1]
        dp = [-1] * (self.last_day + 1)
        return self.dfs(dp, days, costs, 1)

    def dfs(self, dp: List[int], days: List[int], costs: List[int], cur_day: int) -> int:
        if cur_day > self.last_day:
            return 0
        if cur_day not in self.is_travel_needed:
            return self.dfs(dp, days, costs, cur_day + 1)
        if dp[cur_day] != -1:
            return dp[cur_day]

        one_day = costs[0] + self.dfs(dp, days, costs, cur_day + 1)
        seven_day = costs[1] + self.dfs(dp, days, costs, cur_day + 7)
        thirty_day = costs[2] + self.dfs(dp, days, costs, cur_day + 30)

        dp[cur_day] = min(one_day, seven_day, thirty_day)
        return dp[cur_day]

