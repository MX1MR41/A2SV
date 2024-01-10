class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = float("inf")

        for i in range(n):
            a = nums[i]
            l, r = i +1, n-1
            while l < r:
                b,c = nums[l], nums[r]
                tsum = a + b + c
                # if we have found a closer sum
                if abs(target - tsum) < abs(target - res):
                    res = tsum

                # if the sum is the target, no more computation is needed
                if tsum == target:
                    return target

                elif tsum < target:
                    l += 1
                elif tsum > target:
                    r -= 1

        return res


        