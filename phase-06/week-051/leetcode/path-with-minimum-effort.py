class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # bfs + heap + dijkstra
        heap = [(0, 0, 0)]
        m, n = len(heights), len(heights[0])

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        inbound = lambda i, j: 0 <= i < m and 0 <= j < n
        seen = set()

        while heap:
            e, r, c = heappop(heap)

            if (r, c) == (m - 1, n - 1):
                return e

            if (r, c) in seen:
                continue

            seen.add((r, c))

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if inbound(nr, nc) and (nr, nc) not in seen:
                    ne = max(e, abs(heights[r][c] - heights[nr][nc]))
                    heappush(heap, (ne, nr, nc))
