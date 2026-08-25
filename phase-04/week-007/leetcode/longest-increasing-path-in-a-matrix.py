class Solution:
    def longestIncreasingPath(self, matrix):
        # classical dfs would cause a TLE, so use Dynamic Programming
        M, N = len(matrix), len(matrix[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)] # directions
        inbound = lambda r, c: 0 <= r < M and 0 <= c < N # validity of coordinate
        dp = dict()

        def dfs(r, c, moves):
            # has already been processed, therefore just return its value
            if (r, c) in dp: return dp[(r, c)]

            val = matrix[r][c]
            # the maximum path that could be taken starting from here
            _mov = 0

            for d_r, d_c in dirs:
                r_new, c_new = r + d_r, c + d_c

                if inbound(r_new, c_new) and matrix[r_new][c_new] > val:
                    _mov = max(_mov, dfs(r_new, c_new, moves + 1))

            # plus one to count the current square too
            total = _mov + 1
            dp[(r, c)] = total

            return total

        res = 0
        for i in range(M):
            for j in range(N):
                
                res = max(res, dfs(i, j, 0))

        return res
