class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(1, n):
            for j in range(i):
                if nums[i] + nums[j] < target:
                    ans += 1

        return ans