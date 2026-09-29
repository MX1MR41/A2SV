class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        # dp
        # think of ( and ) as opposing values that can cancel each other, like 1 and -1
        # a valid parentheses string is one who total sum is 0, 
        # so all that is needed is to enumerate all possible paths as sums and see if there is 
        # a zero sum at dp[0][0]
        if grid[-1][-1] != ")":
            return False

        m, n = len(grid), len(grid[0])

        dp = [[set() for _ in range(n)] for _ in range(m)]

        dp[-1][-1].add(1)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                val = 1 if grid[i][j] == ")" else -1

                curr = dp[i][j]
                if i < m - 1:
                    down = dp[i + 1][j]
                    for p in down:
                        q = p + val

                        # all valid values are within this range, also minimizes the search space
                        if 0 <= q <= m*n:
                            curr.add(q)
                if j < n - 1:
                    right = dp[i][j + 1]
                    for p in right:
                        q = p + val
                        if 0 <= q <= m*n:
                            curr.add(q)


        return 0 in dp[0][0]
        
