class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # dp
        # this is an 0-1 knapsack dp
        # we gather all the possible powers, then we iterate over them while
        # computing the total number of ways we could form any sum using a dp array
        # we use two dp arrays; prev_dp which stores the number of ways to form any num from
        # 0 to n, upto just the previous index of pows i.e. pows[i - 1].
        # curr_dp will be used to calculate the new dp of forming nums using pows[i]

        MOD = 10**9 + 7

        pows = []
        i = 1
        while i**x <= n:
            pows.append(i**x)
            i += 1

        m = len(pows)


        prev_dp = [0 for _ in range(n + 1)]
        prev_dp[pows[0]] = 1


        for ind in range(1, m):
            curr_pow = pows[ind]

            curr_dp = [0 for _ in range(n + 1)]
            curr_dp[curr_pow] += 1

            for prev_num in range(n + 1):
                summ = curr_pow + prev_num
                if summ > n:
                    continue

                curr_dp[summ] = (curr_dp[summ] + prev_dp[prev_num]) % MOD

            for i in range(n + 1):
                curr_dp[i] = (curr_dp[i] + prev_dp[i]) % MOD

            prev_dp = curr_dp

        
        return prev_dp[n] % MOD
