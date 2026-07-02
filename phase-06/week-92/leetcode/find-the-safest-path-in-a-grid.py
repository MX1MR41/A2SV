class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # bfs + heap
        m, n = len(grid), len(grid[0])

        safe = [[float("inf") for _ in range(n)] for _ in range(m)]

        que = deque()
        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:
                    que.append((i, j))

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        inbound = lambda i, j: 0 <= i < m and 0 <= j < n


        s = 0
        while que:
            for _ in range(len(que)):
                i, j = que.popleft()

                if safe[i][j] <= s:
                    continue

                
                safe[i][j] = s

                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if not inbound(ni, nj) or safe[ni][nj] <= s + 1:
                        continue

                    que.append((ni, nj))

            s += 1


        res = float("inf")
        heap = [(-safe[0][0], 0, 0)]
        seen = set([(0, 0)])

        while heap:
            s, i, j = heappop(heap)
            s = -s

            res = min(res, s)
            if (i, j) == (m - 1, n - 1):
                break

            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if not inbound(ni, nj) or (ni, nj) in seen:
                    continue
                
                heappush(heap, (-safe[ni][nj], ni, nj))
                seen.add((ni, nj))

        return res

        




        

        




        
