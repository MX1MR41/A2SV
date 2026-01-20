class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            for j in range(i):
                if j | (j + 1) == i:
                    res.append(j)
                    break
            else:
                res.append(-1)

        return res
        
