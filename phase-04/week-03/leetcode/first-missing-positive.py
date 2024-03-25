class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # approach uses cyclic sort to sort in O(n) time
        # then utilizes a simple pointer check to validate the first missing +ve number
        
        n = len(nums)


        for i in range(n):
            num = nums[i]
            # since we are assuming that all nums from 1 to n are the ones present in the array,
            # our conditions make sure that
            # a) the numbers are within range
            # b) the number at index i is not equal to i + 1
            # c) the number at the index of where the current number should be i.e nums[nums[i] - 1]
            # is not equal to itself, this will avoid infinite loops
            while 0 < num <= n and num != i + 1 and nums[num-1] != num:
                nums[i], nums[num - 1] = nums[num - 1], num
                num = nums[i]


        
        
        i = 0
        # find first +ve number index
        while i < n and nums[i] < 0:
            i += 1

        res = 1
        # find first missing +ve num
        while i < n:
            
            if nums[i] != res:
                break
            res += 1

            i += 1

        return res
        