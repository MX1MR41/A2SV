class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # dp
        # think of the problem in a reverse manner: instead of finding the minimum number of 
        # elements to delete, find the longest valid mountain array you can make.
        # For each index, find the longest increasing subsequence upto that index from both ends.
        # Then the minimum number of elements to delete would be the length of the array - the 
        # length of the longest VALID mountain array

        n = len(nums)

        
        pre = [1] * n # will store the longest subsequence from the left to each index
        suff = [1] * n # will store the longest subsequence from the right to each index

        for i in range(1, n):
            a = nums[i]
            for j in reversed(range(i)):
                b = nums[j]
                if b < a:
                    pre[i] = max(pre[i], 1 + pre[j])



        nums.reverse()

        for i in range(1, n):
            a = nums[i]
            for j in reversed(range(i)):
                b = nums[j]
                if b < a:
                    suff[i] = max(suff[i], 1 + suff[j])

        suff.reverse()



        ans = float("inf")
        for i in range(1, n-1):
            # a valid mountain array needs at least one element from both ends
            if pre[i] > 1 and suff[i] > 1:
                ans = min(ans, n - (pre[i] + suff[i] - 1))

        return ans


