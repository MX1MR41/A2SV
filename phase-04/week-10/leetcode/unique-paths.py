class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom-up dp
        # start from the destination - last cell- 
        # since you can only move right of down from a cell, the total number of ways
        # you can reach the last cell is by moving one step down and counting all possible ways from there
        # or moving one step right and counting all possible ways from there
        dp = [[0]*n for _ in range(m)]

        dp[-1][-1] = 1
        if m > 1: dp[-2][-1] = 1
        if n > 1: dp[-1][-2] = 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):

                if (i,j) == (m-1, n-1): continue
                
                down = dp[i+1][j] if i < m -1 else 0
                right = dp[i][j+1] if j < n - 1 else 0
                
                dp[i][j] = down + right

        
        return dp[0][0]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # math solution
        # for the robot to reach the end (m-1,n-1) from (0,0),
        # it has to make a total of m-1 moves down and a total of n-1 moves down
        # so it has to make a total of (m-1 + n-1) = (m + n - 2) moves
        # from these moves after we choose m-1 moves, the rest will all be n-1 moves and viceversa
        # so we need to choose either m-1 or n-1 from the total uniquely i.e. combinations
        return comb(m + n - 2, m - 1) # same as comb(m + n - 2, n - 1)

        
