class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxx = nums[:]
        n = len(nums)
        for i in range(1, n):
            maxx[i] = max(maxx[i], maxx[i - 1])

        minn = res = float("inf")
        for i in range(n - 1, -1, -1):
            minn = min(nums[i], minn)
            ins = maxx[i] - minn
            if ins <= k:
                res = i

        return res if res != float("inf") else -1
        
        
