class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # bfs + heap

        visited = set()

        dirs = [(0,1), (0,-1), (1,0), (-1, 0)]
        m, n = len(moveTime), len(moveTime[0])
        inbound = lambda i,j : 0 <= i < m and 0 <= j < n

        heap = [(0,0,0)]

        while heap:
            # print(heap)
            t, i, j = heappop(heap)

            if (i, j) in visited:
                continue

            visited.add((i, j))

            if (i,j) == (m-1, n-1):
                return t

            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if inbound(ni, nj) and (ni, nj) not in visited:
                    new_time = max(moveTime[ni][nj] + 1, t + 1)
      
                    heappush(heap, (new_time, ni, nj))

