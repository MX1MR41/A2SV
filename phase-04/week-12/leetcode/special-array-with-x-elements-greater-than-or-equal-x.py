class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, n
        
        while l <= r:
            mid = (l + r) // 2
            ind = bisect_left(nums, mid)
            if n - ind > mid:
                l = mid + 1
            elif n - ind < mid:
                r = mid - 1
            else:
                return mid

        return -1

