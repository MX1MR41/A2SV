class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        curr_max_jump = 0

        for i in range(n):
            # if the current index is greater than the maximum jump we have
            if i > curr_max_jump:
                return False

            # we update our current maximum jump which we got from the previous index
            # by comparing it to the maximum jump we can do from the current index  
            curr_max_jump = max(curr_max_jump, i + nums[i])

        return True