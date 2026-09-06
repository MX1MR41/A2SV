class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp
        # dp[s_index][t_index] = number of t[0...t_index] subs that can be formed
        # upto s_index.
        # it can be simplified by only storing dp[i - 1], the previous state, only

        n = len(s)
        m = len(t)
        dp = [0 for _ in range(m)]

        if s[0] == t[0]:
            dp[0] = 1

        for i in range(1, n):
            prev = dp
            curr = [0 for _ in range(m)]

            for j in range(m):
                if s[i] != t[j]:
                    continue


                if j - 1 >= 0:
                    # s[i] can be the the t[j] for subs that end in t[j - 1]
                    # that were formed upto s[i - 1]
                    curr[j] += prev[j - 1]
                else:
                    curr[j] = 1

            for j in range(m):
                curr[j] += prev[j]

            dp = curr

        return dp[-1]
