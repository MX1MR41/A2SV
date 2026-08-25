class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        i = 0
        count = 0
        n = len(nums)

        while i <= n - 3:
            if nums[i] == 0:
                count += 1
                for j in range(i, i + 3):
                    nums[j] = 1 if nums[j] == 0 else 0

            i += 1

        return count if 0 not in nums else -1
            

            
        
