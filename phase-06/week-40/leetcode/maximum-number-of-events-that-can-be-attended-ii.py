class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # dp + binary search
        # usual pick or no-pick dynamic programming, but to find the next viable option after a pick,
        # we use binary search

        n = len(events)

        def find(t):
            l, r = 0, n - 1
            res = n
            while l <= r:
                mid = (l + r) // 2
                if events[mid][0] > t:
                    res = mid
                    r = mid - 1
                else:
                    l = mid + 1

            return res

        events.sort()

        dp = {}

        def dfs(i, k):
            if (i, k) in dp:
                return dp[(i, k)]

            if i == n or k == 0:
                return 0

            res = 0

            end = events[i][1]
            nxt_ind = find(end)

            choose = events[i][2] + dfs(nxt_ind, k - 1)

            not_choose = dfs(i + 1, k)

            res = max(choose, not_choose)

            dp[(i, k)] = res

            return res

        return dfs(0, k)


# Bottom-up version

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)

        events.sort()

        starts = [e[0] for e in events]

        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):

            end_time = events[i][1]

            import bisect

            next_index = bisect.bisect_right(starts, end_time, lo=i)

            for j in range(1, k + 1):

                choose = events[i][2] + dp[next_index][j - 1]

                not_choose = dp[i + 1][j]

                dp[i][j] = max(choose, not_choose)

        return dp[0][k]
