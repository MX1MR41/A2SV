class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    
        N = len(grid)
        dirs = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

        inbound = lambda r, c :  0 <= r < N and 0 <= c < N

        def bfs(q, visited):
            path = 1
            

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if [r,c] == [N-1,N-1]: return path
                    if (r,c) in visited: continue
                    
                    visited.add((r,c))

                    for d_r, d_c in dirs:
                        r_new, c_new = r + d_r, c + d_c
                        if inbound(r_new, c_new) and grid[r_new][c_new] == 0: 
                            q.append((r_new, c_new))

                path += 1

            return -1


        if grid[0][0] != 0: return -1

        return bfs(deque([(0,0)]), set())




        
