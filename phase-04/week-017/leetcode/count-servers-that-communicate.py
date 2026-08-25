class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i,j, dir):
            if i < 0 or i >= m or j < 0 or j >= n: return 0

            if grid[i][j]: return True
            
            ans = dfs(i + dir[0], j + dir[1], dir)

            return ans

        res = 0

        for i in range(m):
            for  j in range(n):
                if grid[i][j]:
                    down = dfs(i+1, j, (1,0))
                    up = dfs(i-1, j, (-1,0))
                    right = dfs(i, j+1, (0,1))
                    left = dfs(i, j-1, (0,-1))

                    if any([down,up,right,left]):
                        res += 1

        return res
        


            
        
