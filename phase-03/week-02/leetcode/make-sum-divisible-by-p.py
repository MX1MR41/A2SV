class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # modified code from subarray-sums-divisible-by-k
        # https://leetcode.com/problems/subarray-sums-divisible-by-k/
        n = len(nums)
        tot = sum(nums) 
        if not tot % p:
            return 0

        res = n
        rem = tot % p
        seen = {0:-1}
        pre = 0
        for i in range(n):
            pre += nums[i]
            extra_sum = pre % p
            temp = (pre - rem) % p
            if temp in seen:
                res = min(res, i - seen[temp])
            seen[extra_sum] = i

        return res if res < n else -1


        
        