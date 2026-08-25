class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # prefix sum + suffix sum
        n = len(nums)


        suff = nums[:]
        for i in range(n - 2, -1, -1):
            suff[i] += suff[i + 1]


        count = pre = 0
        for i in range(n - 1):
            pre += nums[i]
            if pre >= suff[i + 1]:
                count += 1

        return count
        
