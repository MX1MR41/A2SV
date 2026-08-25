class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum + modular arithmetic
        # for every index i and sum[0...i], we can subtract either sum[0...i - k]
        # or sum[0...i - 2*k] or sum[0...i - 3*k], etc
        # the sums at i, i - 2*k, i - 3*k, etc can be grouped into the same group 
        # based on their modulo with k. So for every modulo group, we need to store the
        # smallest prefix sum seen so far, and when we compute at index i we will deduct
        # the smallest prefix sum group i's modulo group
        
        # intialize as high as possible because we will minimize it
        mod_group = defaultdict(lambda : float("inf")) 

        # an edge case: subarrays of size of multiples of k
        mod_group[k - 1] = 0

        res = float("-inf")
        prefix_sum = 0
        n = len(nums)

        for i in range(n):
            prefix_sum += nums[i]
            mod = i % k
            best = mod_group[mod]
            
            res = max(res, prefix_sum - best)

            if prefix_sum < mod_group[mod]:
                mod_group[mod] = prefix_sum
            

        return res
        
