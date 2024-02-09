class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # modified code from subarray-sum-equals-k
        # https://leetcode.com/problems/subarray-sum-equals-k
        res = pre = 0 # variables to store the result and prefix sum
        seen = defaultdict(int) # map to hold the already seen prefix sums with their count
        seen[0] = 1 # initialize with prefix sum value 0 since we start our prefix with 0
        n = len(nums)

        for i in range(n):
            pre += nums[i]
            val = pre - goal
            # if there was such a prefix value val such that val + goal = pre,
            # that means we have passed a subarray whose sum is goal, that we accumulated 
            # along with val and the other prefix sum values that we have seen so far 
            if val in seen:
                # if there are x val's, we could've had x subarrays with sum goal, 
                # by subtracting each val on its own from pre
                res += seen[val]

            seen[pre] += 1

        return res