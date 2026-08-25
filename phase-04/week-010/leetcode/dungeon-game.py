class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # use dp starting from bottom-right up to the top-left
        m, n = len(dungeon), len(dungeon[0])

        dp = [[0]*n for _ in range(m)]
        last = dungeon[-1][-1]
        # we hp amount such that we can couteract the -hp and have the minimum hp i.e. 1
        if last <= 0: dp[-1][-1] = 1 - last
        # we have excess hp, so we only need the bare minimum
        else: dp[-1][-1] = 1


        for i in reversed(range(m)):
            for j in reversed(range(n)):
                # bottom-right, already don
                if (i,j) == (m-1, n-1): continue
                # last row
                if i == m-1: down, right = float("inf"), dp[i][j+1]
                # last column
                elif j == n-1: right, down = float("inf"), dp[i+1][j]

                else: right, down = dp[i+1][j], dp[i][j+1]

                curr = dungeon[i][j]
                best = min(right, down)

                temp = best - curr
                # we dn't need any more health point than the bare minimum
                if temp <= 0: dp[i][j] = 1
                # we need temp amount of hp since the cumulative is equal to temp
                else: dp[i][j] = temp

        return dp[0][0]
