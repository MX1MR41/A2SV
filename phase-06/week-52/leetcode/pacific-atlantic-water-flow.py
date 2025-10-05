class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        inbound = lambda i,j : 0 <= i < m and 0 <= j < n
        atlantic = set()
        pacific = set()

        que = deque()
        seen = set()

        for i in range(m):
            que.append((i, n-1))

        for j in range(n):
            que.append((m -1 , j))


        while que:
            for _ in range(len(que)):
                i, j = que.popleft()
                if (i, j) in seen:
                    continue

                seen.add((i, j))
                atlantic.add((i, j))

                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if inbound(ni, nj) and (ni, nj) not in seen and heights[ni][nj] >= heights[i][j]:
                        que.append((ni, nj))

        que = deque()
        seen = set()

        for i in range(m):
            que.append((i, 0))

        for j in range(n):
            que.append((0 , j))


        while que:
            for _ in range(len(que)):
                i, j = que.popleft()
                if (i, j) in seen:
                    continue

                seen.add((i, j))
                pacific.add((i, j))

                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if inbound(ni, nj) and (ni, nj) not in seen and heights[ni][nj] >= heights[i][j]:
                        que.append((ni, nj))


        res = []
        for cell in pacific:
            if cell in atlantic:
                res.append(list(cell))

        return res
            
        
        
