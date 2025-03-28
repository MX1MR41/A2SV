class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # heap + bfs + binary search
        # use a min heap to explore the grid in increasing order of cell values
        # maintain a set to track visited cells and a dictionary to store
        # max points attainable for each value encountered
        # after processing the grid, use binary search to quickly answer each query

        res = defaultdict(int)  
        m, n = len(grid), len(grid[0])
        inbound = lambda i, j: 0 <= i < m and 0 <= j < n  
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]  

        seen = set()  

        heap = [(grid[0][0], 0, 0)]  
        max_seen = 0  

        while heap:
            cell, i, j = heappop(heap)

            if (i, j) in seen:  
                continue

            seen.add((i, j))
            max_seen = max(max_seen, cell + 1)  # update max value encountered

            
            if max_seen <= cell + 1:
                res[cell + 1] = max(res[cell + 1], len(seen))
            res[max_seen] = max(res[max_seen], len(seen))

            
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if inbound(ni, nj) and (ni, nj) not in seen:
                    heappush(heap, (grid[ni][nj], ni, nj))

        arr = sorted(res.items())  

        res = []
        for q in queries:
            l, r = 0, len(arr) - 1
            temp = 0
            while l <= r:  
                mid = (l + r) // 2
                if arr[mid][0] <= q:
                    temp = mid
                    l = mid + 1
                else:
                    r = mid - 1

            
            if arr[temp][0] <= q:
                res.append(arr[temp][1])
            else:
                res.append(0)

        return res
