class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            # using recursion
            m = len(text1)
            n = len(text2)
            dp = defaultdict(int)    
            def dfs(i, j):
                
                if i >= m or j >= n:
                    return 0

                if (i,j) in dp:
                    return dp[(i,j)]

                if text1[i] == text2[j]:
                    return 1 + dfs(i+1, j+1)
                
                ans = max(dfs(i+1, j), dfs(i, j+1))
                dp[(i,j)] = ans
                return ans

            return dfs(0,0)
        

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            # using tabulation
            m = len(text1)
            n = len(text2)
            dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
            for row in range(1, m + 1):
                for col in range(1, n + 1):
                    if text1[row - 1] == text2[col - 1]:
                        dp[row][col] = 1 + dp[row - 1][col - 1]
                    else:
                        dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])

            return dp[m][n]

        

                
