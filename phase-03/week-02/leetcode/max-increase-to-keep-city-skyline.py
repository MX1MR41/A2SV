class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # each view for each cardinal drection has one max height building 
        # of that row if we're seeing from east or west; 
        # or of that column if we're seeing from north or south
        # we can increase every building's height to the either the max of its row or max of its column
        # but we'll have to choose the minimum of those two since if we surpass that, 
        # we would alter the respective view
        n = len(grid)
        # stores the max building as seen from the north or south for each column
        down = [0 for _ in range(n)] 
        # stores the max building as seen from east or west for each row
        right = [] 
        for i in grid:
            right.append(max(i))
        
        for i in range(n):
            for j in range(n):
                down[j] = max(down[j], grid[i][j])

        res = 0

        for i in range(n):
            for j in range(n):
                # for each building, increase it to the minimum of its row's max or its column's max
                res += min(down[j], right[i]) - grid[i][j]

        return res
                
        
        