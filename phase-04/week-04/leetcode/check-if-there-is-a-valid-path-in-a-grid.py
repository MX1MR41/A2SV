class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # classic dfs
        M, N = len(grid), len(grid[0])
        # small function to check validity of a coordinate
        inbound = lambda r, c: 0 <= r < M and 0 <= c < N
        # the various streets' orientations represented as change vectors
        dirs = { 1: [(0,1), (0,-1)], 2: [(1,0), (-1,0)], 3: [(0,-1), (1,0)],
                 4: [(0,1), (1,0)], 5: [(-1,0), (0,-1)], 6: [(-1,0), (0,1)] }

        def dfs(r, c, visited):
            # destination arrived
            if [r,c] == [M-1,N-1]: return True
            # and already visited coordinate (street)
            if (r,c) in visited: return False

            visited.add((r,c))
            # the change vectors allowed by the current street's orientation
            for d_r, d_c in dirs[grid[r][c]]:
                r_new, c_new = r + d_r, c + d_c 

                if inbound(r_new, c_new):
                    # the vectors of the next valid coordinate
                    nxt_dir = dirs[grid[r_new][c_new]]
                    # if the next street allows incoming traffic from current coord
                    # we explore it
                    if (-d_r,-d_c) in nxt_dir:
                        res = dfs(r_new, c_new, visited)
                        if res: return True

            return False


        return dfs(0,0,set())




            
        
