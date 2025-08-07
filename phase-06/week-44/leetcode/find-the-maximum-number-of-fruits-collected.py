class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        # dp + bfs
        # player (0, 0) can only move diagonally to the target
        # player (n - 1, 0) can move in any way rightwards while staying below the diagonal
        # player (0, n - 1) can move in any way downwards while staying above the diagonal
        # for those two players, we simulate each move and choose the best using dp

        n = len(fruits)

        inbound = lambda i, j: 0 <= i < n and 0 <= j < n
        
        diag = 0
        for i in range(n):
            diag += fruits[i][i]

        dp = [[0 for _ in range(n)] for _ in range(n)]

        
        bdirs = [(1, -1), (1, 0), (1, 1)] # player_b's moves
        cdirs = [(-1, 1), (0, 1), (1, 1)] # player_c's moves

        dp[0][n - 1] = fruits[0][n - 1] # base case

        bset = set([(0, n - 1)]) # the source for the bfs

        while bset:
            new_bset = set()

            for i, j in bset:
                for di, dj in bdirs:
                    ni, nj = i + di, j + dj
                    if not inbound(ni, nj) or ni >= nj:
                        continue

                    dp[ni][nj] = max(dp[ni][nj], fruits[ni][nj] + dp[i][j])

                    new_bset.add((ni, nj))

            bset = new_bset

        dp[n - 1][0] = fruits[n - 1][0]
        cset = set([(n - 1, 0)])

        while cset:
            new_cset = set()

            for i, j in cset:
                for di, dj in cdirs:
                    ni, nj = i + di, j + dj
                    if not inbound(ni, nj) or ni <= nj:
                        continue

                    dp[ni][nj] = max(dp[ni][nj], fruits[ni][nj] + dp[i][j])

                    new_cset.add((ni, nj))

            cset = new_cset

        
        return diag + dp[n - 1][n - 2] + dp[n - 2][n - 1]
