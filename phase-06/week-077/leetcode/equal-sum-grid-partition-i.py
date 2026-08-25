class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        pre = []
        for row in grid:
            pre.append(sum(row))

        tot = sum(pre)

        

        for i in range(1, len(pre)):
            pre[i] += pre[i - 1]


        for i in range(1, len(pre)):
            if tot - pre[i -1] == pre[i - 1]:
                return True

        pre = []
        for j in range(len(grid[0])):
            summ = 0
            for i in range(len(grid)):
                summ += grid[i][j]

            pre.append(summ)

        for i in range(1, len(pre)):
            pre[i] += pre[i - 1]

        

        for i in range(1, len(pre)):
            if tot - pre[i -1] == pre[i - 1]:
                return True

        return False
        
