class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        # DP + combinatorics
        # A "divisor chain" is a list of unique nums where every num is divisble by
        # the number before it. The longest such divisor chain we could make has length 14
        # This is it => [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192].
        # Precompute the number of unique ways we can form "divisor chains" of every length
        # upto 14 and ending with every value upto maxValue and store in a 2d dp matrix
        # where dp[val][distinct] is the number of ways we can form an ideal array 
        # with "distinct" number of nums and ending with the num "val".
        # For any "divisor chain", we can form a bigger list of nums by repetition
        # eg. divisor chain => [1,2,4] we can form [1,1,2,2,2,4,4] or any other
        # to count the number of such arrays that can be formed with a "divisor chain" that 
        # has k distinct nums, there will be k-1 points where there will be an "increase"
        # [1,1 | 2,2,2 | 4,4], the lines represent said "increases". To count the number of
        # ideal arrays of length n and "divisor chain" with k distinct nums, we perform
        # Combinations(n - 1, k - 1), i.e. out of the n-1 possible spots, in how many ways
        # unique ways can we select k - 1 spots as "increase" spots

        MOD = 10**9 + 7

        max_distinct = min(n, 14)
        dp = [[0 for _ in range(max_distinct + 1)] for _ in range(maxValue + 1)]

        for val in range(1, maxValue + 1):
            dp[val][1] = 1

        for val in range(1, maxValue):
            for distinct in range(1, max_distinct):

                m = 2              
                while m * val <= maxValue:
                    dp[m * val][distinct + 1] += dp[val][distinct]
                    m += 1

        res = 0

        for val in range(1, maxValue + 1):

            for distinct in range(1, max_distinct + 1):
                ways = dp[val][distinct]
       
                spread = comb(n - 1, distinct - 1)
                res = (res + ways * spread) % MOD

        return res % MOD
            
