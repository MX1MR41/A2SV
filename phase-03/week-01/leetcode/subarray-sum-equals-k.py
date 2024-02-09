class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = pre = 0 # variables to store the result and prefix sum
        seen = defaultdict(int) # map to hold the already seen prefix sums with their count
        seen[0] = 1 # initialize with prefix sum value 0 since we start our prefix with 0
        n = len(nums)

        for i in range(n):
            pre += nums[i]
            # if there was such a prefix value val such that val + k = pre,
            # that means we have passed a subarray whose sum is k, that we accumulated 
            # along with val and the other prefix sum values that we have seen so far 
            if pre - k in seen:
                # if there are x val's, we could've had x subarrays with sum k, 
                # by subtracting each val on its own from pre
                res += seen[pre - k]

            seen[pre] += 1

        return res
