class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # modified code from subsets question
        # https://leetcode.com/problems/subsets/
        
        nums.sort()
        # changing res from list to set is the only modification made  
        res = set() 

        def sub(start, comb):
            res.add(tuple(sorted(comb[:])))  

            for i in range(start, len(nums)):
                comb.append(nums[i])
                sub(i + 1, comb)  
                comb.pop()

        sub(0, [])
        return res