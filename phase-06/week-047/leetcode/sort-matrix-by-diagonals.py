class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:


        groups = defaultdict(list)

        m, n = len(grid), (len(grid[0]))

        for i in range(m):
            for j in range(n):

                group = i - j
                groups[group].append(grid[i][j])

        for group in groups:
            if group >= 0:
                groups[group].sort()
            else:
                groups[group].sort(reverse = True)

        for i in range(m):
            for j in range(n):
                group = i - j
                grid[i][j] = groups[group].pop()

        return grid
        
