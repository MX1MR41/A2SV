class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # greedy
        hi = diff = 0
        res = 0

        for num in nums:
            curr = diff * num
            res = max(curr, res)
            hi = max(num, hi)
            diff = max(diff, hi - num)

        return res
        
