class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        prefix = 0
        for num in nums:
            prefix <<= 1
            prefix |= num
            res.append(not prefix % 5)

        return res
        
