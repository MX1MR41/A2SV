class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # dp
        day_set = set(days)  # To quickly check if a day is a travel day
        last_day = days[-1]  # The last day of travel
        dp = [0] * (last_day + 1)  # dp[i] is the min cost to cover up to day i

        for day in range(1, last_day + 1):
            if day not in day_set:
                dp[day] = dp[day - 1]  # No travel, cost is the same as the previous day
            else:
                # Consider all ticket options
                dp[day] = min(
                    dp[max(0, day - 1)] + costs[0],  # 1-day pass
                    dp[max(0, day - 7)] + costs[1],  # 7-day pass
                    dp[max(0, day - 30)] + costs[2]  # 30-day pass
                )

        return dp[last_day]
