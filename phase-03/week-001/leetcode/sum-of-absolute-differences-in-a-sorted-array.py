class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n, res = len(nums), []
        psum, ssum = [], [] # the prefix xum and suffix sum arrays
        p = s = 0 #counters for the prefix and suffix sum arrays respectively

        for i in nums: # populating the prefix sum array
            p += i
            psum.append(p)

        for i in nums[::-1]: #populating the suffix sum array
            s += i
            ssum.append(s)
        ssum.reverse()
    

        for i in range(n):
            curr = (nums[i] * i) - (nums[i] * (n - i - 1))
            curr += (ssum[i] - nums[i]) - (psum[i] - nums[i])

            res.append(curr)
            
        return res
        

        """
        for i and nums[i] the answer can be derived as:
            (nums[i] * i) - (nums[i] * (n-i-1))
            (nums[0] + nums[1] + ... + nums[i-1])) + 
            ((nums[i+1] + nums[i+2] + ... + nums[n-1]) - 
            
        """