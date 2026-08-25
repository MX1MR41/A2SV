class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0
        while nums != sorted(nums):
            ops += 1

            
            
            minn = [-1, float("inf")]
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < minn[1]:
                    minn = [i, nums[i] + nums[i + 1]]

            

            nums[minn[0]] += nums[minn[0] + 1]

            for i in range(minn[0] + 1, len(nums) - 1):
                nums[i] = nums[i + 1]

            nums.pop()


            
            


        return ops
        
