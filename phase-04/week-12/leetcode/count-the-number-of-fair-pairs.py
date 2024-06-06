class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # sorting + binary search
        nums.sort()
        n = len(nums)
        ans = 0
        
        for i in range(n):
            num = nums[i]
            # the numbers whose sum with num would give lower and upper
            lo, hi = lower - num, upper - num

            # find the first occurence  of lo
            start = bisect.bisect_left(nums, lo, i + 1)
            # find the index just after the last occurence of hi
            end = bisect.bisect_right(nums, hi, i + 1)
            
            ans += end - start

        return ans
