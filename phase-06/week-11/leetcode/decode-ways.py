class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        if n == 1:
            return 1 if s != "0" else 0
        
        dp = [[0, 0] for _ in range(n)]

        if s[0] != "0":
            dp[0] = [1, 0] 
            dp[1][0] = 1 if s[1] != "0" else 0
            if s[0] != "0" and int(s[:2]) <= 26:
                dp[1][1] = 1

        for i in range(2, n):

            dp[i][0] = sum(dp[i - 1]) if s[i] != "0" else 0
            if int(s[i - 1: i + 1]) <= 26 and s[i - 1] != "0":
                dp[i][1] = sum(dp[i - 2])


        return sum(dp[-1])
