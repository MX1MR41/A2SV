class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # bfs + queue + dp
        # Create a visited hashmap that will store the minimum cost it took
        # to get to visited[(row, col)].
        # Traverse the grid starting from (0, 0) in a bfs manner
        # for every (i, j), try the immediate neighbor based on the sign with cost + 0
        # then try the other possible neighbors of different signs with cost + 1.
        # Expand a cell (i, j) only if the cost it took to reach it is less than
        # its last minimum cost, i.e. visited[(i, j)]


        dirs = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        m, n = len(grid), len(grid[0])

        inbound = lambda i, j: 0 <= i < m and 0 <= j < n

        visited = defaultdict(lambda: float("inf"))

        que = deque([(0, (0, 0))])

        while que:

            for _ in range(len(que)):
                cost, (i, j) = que.popleft()

                if cost >= visited[(i, j)]:
                    continue

                visited[(i, j)] = min(visited[(i, j)], cost)

                sign = grid[i][j]
                di, dj = dirs[sign]
                ni, nj = i + di, j + dj

                if inbound(ni, nj) and cost < visited[(ni, nj)]:
                    que.append((cost, (ni, nj)))

                for d in range(1, 5):
                    if d != sign:
                        di, dj = dirs[d]
                        ni, nj = i + di, j + dj

                        if inbound(ni, nj) and cost + 1 < visited[(ni, nj)]:
                            que.append((cost + 1, (ni, nj)))

        return visited[(m - 1, n - 1)]
