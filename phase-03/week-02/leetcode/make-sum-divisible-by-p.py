class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # modified code from subarray-sums-divisible-by-k
        # https://leetcode.com/problems/subarray-sums-divisible-by-k/

        # remain = total_sum % p; need to find a subarray sum whose sum % p == remain
        # let deduct = sum of subarray to be removed; pre = total prefix sum upto current index
        # (pre - deduct) % p = remain -> pre % p - deduct % p = remain
        # since modding by p again won't make a difference -> deduct % p = pre % p - remain % p
        # if we stored the prefix % p, we can simplify to deduct = (pre - remain) % p

        # we will store the prefix sum % p for at every iteration

        n = len(nums)
        tot = sum(nums)
        if not tot % p:
            return 0

        res = n
        remain = tot % p
        seen = {0: -1} # prefix offset purpose
        prefix_sum = 0

        for i in range(n):
            prefix_sum += nums[i]
            deduct = (prefix_sum - remain) % p

            if deduct in seen:

                res = min(res, i - seen[deduct])

            extra_sum = prefix_sum % p
            seen[extra_sum] = i

        return res if res < n else -1
