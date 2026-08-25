class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # bfs + heap
        # start from the boundaries and move inwards computing trapped water volumes
        # using a min heap helps with processing the smallest boundary heights first so we
        # don't cause any "overflow" when computing trapped water volume
        
        m, n = len(heightMap), len(heightMap[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Directions for exploring neighbors
        inbound = lambda i, j : 0 <= i < m and 0 <= j < n  # Check if within grid bounds

        heap = []  # Min-heap to track the lowest boundary cells

        # Add all boundary cells to the heap and mark them visited
        for i in range(m):
            heappush(heap, (heightMap[i][0], i, 0))
            heightMap[i][0] = -1
            heappush(heap, (heightMap[i][-1], i, n - 1))
            heightMap[i][n - 1] = -1

        for j in range(n):
            heappush(heap, (heightMap[0][j], 0, j))
            heightMap[0][j] = -1
            heappush(heap, (heightMap[-1][j], m - 1, j))
            heightMap[m - 1][j] = -1

        volume = 0  # Total water trapped
        max_height = -1  # Tracks the maximum boundary height encountered

        while heap:
            height, i, j = heappop(heap)  # Process the smallest boundary cell

            # Update max_height to reflect the current effective water level
            max_height = max(max_height, height)

            # Calculate water trapped at this cell (if any)
            # if height is less than max_height, that means that we have explored a boundary
            # with height higher than this cell's, and we are guaranteed that because we are
            # using a min heap and if this cell wasn't bounded by max_height it would've
            # been explored first because it is lower
            volume += max_height - height

            # Explore all neighboring cells
            for di, dj in dirs:
                ni, nj = i + di, j + dj

                if inbound(ni, nj) and heightMap[ni][nj] != -1:  # Unvisited neighbor
                    # Add the neighbor to the heap; it becomes part of the boundary
                    heappush(heap, (heightMap[ni][nj], ni, nj))

                    # Mark as visited to avoid reprocessing
                    heightMap[ni][nj] = -1

        return volume
