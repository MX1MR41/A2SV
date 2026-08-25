class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # prefix sum
        n = len(nums)
        pre = [0] * (n + 1)

        for l, r in queries:
            pre[l] += 1
            pre[r + 1] -= 1

        for i in range(1, n + 1):
            pre[i] += pre[i - 1]

        for i in range(n):
            nums[i] -= min(nums[i], pre[i])
            if nums[i] > 0:
                return False

        return True
