class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        res = []

        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):

                nums = set()
                for p in range(i, i + k):
                    for q in range(j, j + k):
                        nums.add(grid[p][q])

                nums = sorted(list(nums))

                
                curr = float("inf")

                for z in range(1, len(nums)):
                    curr = min(curr, nums[z] - nums[z - 1])

                if len(nums) == 1:
                    curr = 0

                row.append(curr)

            res.append(row)

        return res
                
