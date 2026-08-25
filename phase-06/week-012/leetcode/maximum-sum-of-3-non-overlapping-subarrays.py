class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # prefix sum + dp + sliding window
        # Precompute the earliest maximum sum upto and exluding an index for every index
        # both from the left as prefix, and from the right as suffix. 
        # Store said maximum sums alongside their respective start indices
        # Slide a window over the array and compute the current choice as
        # sum of window + maximum earliest sum from the left + maximum earliest sum from the right


        n = len(nums)

        # prefix[i] = (earliest maximum sum before and excluding i, starting index of said sum)
        prefix = [(0, 0) for _ in range(n)]
        # suffix[i] = (earliest maximum sum after and excluding i, starting index of said sum)
        suffix = [(0, n - 1) for _ in range(n)]

        # current max sum and starting index
        pre_max = window = sum(nums[:k])
        pre_ind = 0

        # slide a window and find out the maximum sum window
        for right in range(k, n):
            # already precomputed the max window before right, so we update it
            prefix[right] = (pre_max, pre_ind)

            left = right - k
            window += nums[right]
            window -= nums[left]

            # if current window sum is larger, then we have found a new max window
            if window > pre_max:
                pre_max = window
                pre_ind = left + 1


        # same logic for suffix max too, just in reverse
        suff_max = window = sum(nums[n - k :])
        suff_ind = n - k
        for left in range(n - k - 1, -1, -1):
            suffix[left] = (suff_max, suff_ind)
            right = left + k
            window -= nums[right]
            window += nums[left]

            if window >= suff_max:
                suff_max = window
                suff_ind = left

        
        res = [0, 0, 0, 0] # initial answer

        window = sum(nums[:k]) # initial window

        for left in range(n - k):
            # slide window by one and add nums[right] and deduct nums[left]
            right = left + k
            window += nums[right]
            window -= nums[left]

            # best pre_computed choices from either end of the current window
            pre_max, pre_ind = prefix[left + 1]
            suff_max, suff_ind = suffix[right]

            # current candidate
            curr = window + pre_max + suff_max

            if curr > res[0]:
                res = [curr, pre_ind, left + 1, suff_ind]

        return res[1:]
