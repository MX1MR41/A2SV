class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = defaultdict(int)
        def dfs(day):
            if day > days[-1]: return 0
            
            if day in dp: return dp[day]

            i = 0
            while i < len(days) and days[i] < day:
                i += 1
            if i == len(days): return 0

            new_day = days[i]
            one = dfs(new_day + 1) + costs[0]
            seven = dfs(new_day + 7) + costs[1]
            thirty = dfs(new_day + 30) + costs[2]


            dp[day] = min(one, seven, thirty)
            return dp[day]

        return dfs(days[0])
