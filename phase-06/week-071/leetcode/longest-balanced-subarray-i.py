class Solution:
    def longestBalanced(self, nums: List[int]) -> int:

        res = 0
        n = len(nums)
        for i in range(n):
            ev = set()
            odd = set()
            for j in range(i, n):
                if nums[j] % 2:
                    odd.add(nums[j])
                else:
                    ev.add(nums[j])

                if len(ev) == len(odd):
                    res = max(res, j - i + 1)

        return res
        
