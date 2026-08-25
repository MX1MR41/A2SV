class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # Dynamic programming
        # LCS but with ASCII values
        m = len(s1)
        n = len(s2)

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):

                if s1[i] == s2[j]:
                    dp[i][j] = ord(s1[i])

                if i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j] += dp[i - 1][j - 1]

                if i - 1 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])

                if j - 1 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1])



        return sum(ord(i) for i in s1) + sum(ord(i) for i in s2) - 2*dp[-1][-1]


        
