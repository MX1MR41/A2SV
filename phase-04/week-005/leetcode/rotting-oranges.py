class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        inbound = lambda r, c : 0 <= r < M and 0 <= c < N
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(q, visited, rotten):
            time = -1
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if (r,c) in visited: continue

                    visited.add((r,c))
                    rotten.add((r,c))
                    grid[r][c] = 2

                    for d_r, d_c in dirs:
                        r_new, c_new = r + d_r, c + d_c

                        if inbound(r_new, c_new) and grid[r_new][c_new] == 1:
                            grid[r_new][c_new] = 2

                            q.append((r_new,c_new))

                time += 1

            return time
        
        rotten, visited, Q = set(), set(), deque()
        oranges = 0

        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    oranges += 1

                    if grid[i][j] == 2: 
                        rotten.add((i,j))
                        Q.append((i,j))

        if not oranges: return 0


        time = bfs(Q, visited, rotten)

        if len(rotten) == oranges: return time
        else: return -1
        
