class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # bfs + heap
        heap = [(0, 0, 0, 2)]

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(moveTime), len(moveTime[0])

        inbound = lambda i, j: 0 <= i < m and 0 <= j < n

        visited = defaultdict(lambda: float("inf"))

        while heap:

            t, i, j, mo = heappop(heap)

            if visited[(i, j)] <= t:
                continue

            if (i, j) == (m - 1, n - 1):

                return t

            visited[(i, j)] = t

            move = 2 if mo == 1 else 1

            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if inbound(ni, nj):
                    nei = moveTime[ni][nj]
                    if t >= nei:
                        new_time = t + move
                    else:
                        new_time = nei + move

                    if visited[(ni, nj)] > new_time:
                        heappush(heap, (new_time, ni, nj, move))
