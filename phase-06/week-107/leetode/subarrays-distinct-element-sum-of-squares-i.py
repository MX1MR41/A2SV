class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for l in range(n):
            for r in range(l, n):
                s = set()
                for i in range(l, r + 1):
                    s.add(nums[i])

                res += len(s) ** 2

                del s

        return res

        
