class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # bfs + heap + dijkstra 
        # trying to find the path with the least number of obstacles can be rephrased
        # as trying to find the path with the least weights
        # this makes the problem a shortest path problem where we first explore all
        # the options with the least number of obstacles
        # store movement options with their obstacles in a heap to explore the least 
        # obstacles options first
        rows, cols = len(grid), len(grid[0])
        heap = []

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        inbound = lambda row, col: 0 <= row < rows and 0 <= col < cols 

        visited = set()

        heap.append((0, (0, 0)))

        while heap:
            obstacles, (row, col) = heappop(heap)
            if (row, col) == (rows - 1, cols - 1):
                return obstacles

            if (row, col) in visited:
                continue

            visited.add((row, col))
            for drow, dcol in directions:
                newrow, newcol = row + drow, col + dcol
                if inbound(newrow, newcol) and (newrow, newcol) not in visited:
                    newobstacles = obstacles + grid[newrow][newcol]
                    heappush(heap, (newobstacles, (newrow, newcol)))

        


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # bfs + dp
        # we initialize the dp of every cell as infinity then for each cell we are in,
        # if exploring a neighbor from this cell would result in a smaller dp for the
        # neighbor than its original dp, we update it as so and add it to the queue
        rows, cols = len(grid), len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        inbound = lambda row, col: 0 <= row < rows and 0 <= col < cols 

        dp = [[float("inf") for _ in range(cols)] for _ in range(rows)]

        dp[0][0] = 0
        que = deque([(0, 0)])

        while que:
            r, c = que.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if inbound(nr, nc) and dp[r][c] + grid[nr][nc] < dp[nr][nc]:
                    dp[nr][nc] = dp[r][c] + grid[nr][nc]
                    que.append((nr, nc))

        return dp[-1][-1]

        
