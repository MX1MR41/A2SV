class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # use binary search over the search space of possible differences
        # where the condition is by counting the number of differences possible
        # than the current difference we are examining
        nums.sort()
        n = len(nums)
        # return the number of pairs that give differences less than or equal to diff
        def count(diff):
            l = 0
            cnt = 0
            for r in range(1, n):
                while l < r and nums[r] - nums[l] > diff:
                    l += 1
                cnt += r - l
            return cnt

        l, r = 0, nums[-1] - nums[0]
        # binary search
        while l < r:
            mid = (l + r) // 2
            if count(mid) >= k:
                r = mid
            else:
                l = mid + 1

        return l
