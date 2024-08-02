class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # use a static sliding window of size of number of ones 
        # doubling the array accounts for circularity
        ones = nums.count(1)
        nums += nums
        ans = wind = nums[:ones].count(0)

        ind = ones
        while ind < len(nums):
            if not nums[ind]:
                wind += 1

            if not nums[ind-ones]:
                wind -= 1

            ans = min(ans, wind)

            ind += 1


        return ans
        
