class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # prefix max and suffix max
        # for each index i, precompute and store the greatest number seen sof far from 0 to i - 1
        # and from i + 1 to n - 1. Then iterate once more over every index considering it as the
        # second of the triplet values and using its precomputed maxes from both sides to 
        # compute the best possible value that could be obtained if index i was the middle triplet

        res = 0

        n = len(nums)

        pre_max = []
        max_pre = 0
        for i in range(n):
            pre_max.append(max_pre)

            max_pre = max(max_pre, nums[i])

        suff_max = []
        max_suff = 0
        for i in range(n - 1, -1, -1):
            suff_max.append(max_suff)

            max_suff = max(max_suff, nums[i])

        suff_max.reverse()

        for i in range(n):
            num = nums[i]
            curr = (pre_max[i] - num) * suff_max[i]

            res = max(res, curr)

        return res
