class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # rotate whole array then rotate the first portion upto k then rotate the remaining
        def helper(arr, i, j):
            while (i < j):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            return arr
            
        if k > len(nums):
            k %= len(nums)
            
        if (k > 0):
            helper(nums, 0, len(nums) - 1)
            helper(nums, 0, k - 1)      
            helper(nums, k, len(nums) - 1)  
