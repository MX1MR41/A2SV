class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        # the approach works by iterating in reverse and comparing the last
        # element with the current element.  Everytime we find a num out of place
        # we compute the steps needed to fix it and assign the fixed calue to the index
        n = len(nums)
        last = nums[-1] 
        res = 0  

        for i in reversed(range(n - 1)):
            curr = nums[i]

            if curr > last: 
                ops = curr // last 

                if curr % last:
                    ops += 1  

                last = curr // ops  
                res += ops - 1 

            else:
                last = curr 

        return res  