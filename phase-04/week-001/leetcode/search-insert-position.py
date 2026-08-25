class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = r

        while l <= r:
            mid = (l + r) // 2
            num = nums[mid]

            if num == target:
                return mid

            elif num < target:
                l = mid + 1

            else:
                r = mid - 1
                res = mid


        return res if nums[res] >= target else res + 1
        