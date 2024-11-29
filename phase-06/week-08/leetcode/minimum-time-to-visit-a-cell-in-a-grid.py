class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # bfs + heap, dijkstra
        m, n = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1  

        
        heap = [(0, 0, 0)]  
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while heap:
            time, x, y = heapq.heappop(heap)
            if (x, y) == (m - 1, n - 1):
                return time
            if (x, y) in visited:
                continue
            visited.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    wait_time = max(grid[nx][ny], time + 1)

                    # assume each cell has a time parity
                    # i.e. if (i, j)'s time is t, then (ni, nj)'s time is t + 1
                    # the parity always alternates whether is you visit it immediately 
                    # or visit it after visting other cells to pass time
                    if wait_time % 2 != (time + 1) % 2:
                        wait_time += 1  

                    heapq.heappush(heap, (wait_time, nx, ny))

        return -1
