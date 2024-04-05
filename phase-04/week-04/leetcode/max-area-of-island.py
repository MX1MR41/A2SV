class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # recursive approach
        M, N = len(grid), len(grid[0])
        # pre check for validity of coordinate (row,column)
        inbound = lambda r, c : 0 <= r < M and 0 <= c < N
        # the four directions
        dirs = [(0,1), (0,-1), (1,0), (-1, 0)]

        def dfs(r,c,visited):
            if (r,c) in visited: return 0 
            visited.add((r,c))
            curr = 1
            for d_r, d_c in dirs:
                r_new, c_new = r + d_r, c + d_c
                
                if inbound(r_new, c_new) and grid[r_new][c_new]:
                    curr += dfs(r_new,c_new,visited)

            return curr

        res = 0
        visited = set()
        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    curr = dfs(i,j,visited)

                    res = max(res, curr)

        return res



            
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # iterative approach
        M, N = len(grid), len(grid[0])
        inbound = lambda r, c : 0 <= r < M and 0 <= c < N
        dirs = [(0,1), (0,-1), (1,0), (-1, 0)]

        stk, visited, res = [], set(), 0
    
        for i in range(M):
            for j in range(N):

                if grid[i][j]:
                    stk.append((i,j))
                    curr = 0

                    while stk:
                        r,c = stk.pop()
                        if (r,c) in visited: continue
                        curr += 1
                        visited.add((r,c))

                        for d_r, d_c in dirs:
                            r_new, c_new = r + d_r, c + d_c
                            if inbound(r_new, c_new) and grid[r_new][c_new]:
                                stk.append((r_new,c_new))

                    res = max(res, curr)


        return res

