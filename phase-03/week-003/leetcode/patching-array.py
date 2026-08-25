class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # if we have a consecutive range of [1,x], 
        # we can form all the number from 1 to x
        # so by starting from the left, whenever we meet a num which is either
        # less than or equal to the last num (which represents the range)
        # we add it to x, thereby making the generation potential upto x + said num
        # if the next +1 number isnt present, we patch it in, because if we skip
        # any nums in between, we wont be able to generate all nums
        N = len(nums)
        res = 0
        curr = 0
        i = 0
        while curr < n:
            if i < N and nums[i] <= curr + 1:
                curr += nums[i]
                i += 1
            else:
                res += 1
                curr += curr + 1

        return res



        