class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        M, N = len(grid), len(grid[0])
        inbound = lambda r, c: 0 <= r < M and 0 <= c < N

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r, c, visited):
            if (r,c) in visited: return

            visited.add((r,c))

            for d_r, d_c in dirs:
                r_new, c_new = r + d_r, c + d_c

                if inbound(r_new, c_new) and grid[r_new][c_new] == "1":
                    dfs(r_new, c_new, visited)

        ISLANDS = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1" and (i,j) not in visited:
                    ISLANDS += 1
                    dfs(i,j, visited)

        return ISLANDS


        
