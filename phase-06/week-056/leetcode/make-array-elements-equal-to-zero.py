class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        
        count = 0
        pre = nums[:]
        suf = nums[:]

        for i in range(1, len(nums)):
            pre[i] += pre[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suf[i] += suf[i + 1]

        for i in range(len(nums)):
            if nums[i] != 0:
                continue

            if pre[i] == suf[i]:
                count += 2

            if abs(pre[i] - suf[i]) == 1:
                count += 1

        return count
