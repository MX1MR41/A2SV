class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # greedy
        # same as https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/
        # if we have a set of nums S, whose elements can be summed up to form integers upto k,
        # adding k + 1 into the set will help us form all the numbers upto 2*k + 1.
        # OR, if S can form upto and excluding k, adding k into S will help S form all nums upto 2*k-1
       

        patches = 0
        next_num = 1  
        ind = 0       

        while next_num <= n:  
            # if nums[ind] is already within the range of numbers that can be formed, we can use it
            # immediately to increase our range
            if ind < len(nums) and nums[ind] <= next_num:
                next_num += nums[ind]
                ind += 1  

            # if either next_num hasn't reached nums[ind] yet, or we have run out of nums but still
            # haven't reach n, we keep adding the immediately next required number to our set and
            # extend our range by that much
            else:
                next_num += next_num
                patches += 1

        return patches
