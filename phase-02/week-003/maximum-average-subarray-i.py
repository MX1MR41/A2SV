class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = curr = sum(nums[:k]) # initializing window
        n = len(nums)
        for i in range(k, n):
            curr += - nums[i-k] + nums[i]
            ans = max(curr, ans)

        return ans/k
    

        