class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # this approach uses a monotonic stack to store indices
        # then when a num which is greater than the nums at the indices in the stack,
        # we keep popping indices out of that stack and setting their result in the res list
        # as the current num in the list at index i % n
        # the modulo part is essential cuz we are iterating the list twice to cover all nums
        n = len(nums)
        res = [-1 for _ in range(n)]
        stk = []

        for i in range(2 * n):

            while stk and nums[stk[-1]] < nums[i % n]:
                res[stk.pop()] = nums[i % n]
                
            if i < n: # we do this so we can keep track of the indices only once and no duplicates
                stk.append(i)

        return res


