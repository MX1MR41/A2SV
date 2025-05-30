class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # backtracking + bit manipulation
        # try every possible way of moving from the source node to the target
        # and keep track of the visited cells as a bitmask, where i'th bit is 0 if i'th
        # cell hasn't been visited, and 1 if it has been visited.
        # count the cells left to right, top to bottom and assign them from 0 to m*n - 1

        m, n = len(grid), len(grid[0])
        inbound = lambda i, j: 0 <= i < m and 0 <= j < n
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        cells = m * n

        def ith_cell(i, j):
            i += 1
            j += 1
            cell = (i - 1) * n + j

            return cell - 1

        # a bitmask with all the bits from 0 to cell - 1 set as 1
        all_visited = (1 << cells) - 1

        for i in range(m):
            for j in range(n):

                # this cell will can't be visited so the bit should be turned off
                if grid[i][j] == -1:
                    cell = ith_cell(i, j)
                    all_visited &= ~(1 << cell)

        def dfs(i, j, mask):
            cell = ith_cell(i, j)
            mask |= 1 << cell

            if grid[i][j] == 2: # target reached
                if mask == all_visited: # all visit-able cells visited
                    return 1

                return 0

            count = 0

            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if inbound(ni, nj) and grid[ni][nj] in (0, 2):
                    nei = ith_cell(ni, nj)
                    if not (mask & (1 << nei)):
                        count += dfs(ni, nj, mask)

            return count

        start_found = False
        for i in range(m):
            if start_found:
                break

            for j in range(n):
                if grid[i][j] == 1:
                    start = [i, j]
                    start_found = True
                    break

        res = dfs(start[0], start[1], 0)

        return res
