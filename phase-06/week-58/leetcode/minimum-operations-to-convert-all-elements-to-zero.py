class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # monotonick stack
        # for each nums[i], the widest the subarray we can choose to apply the operation
        # on it is as far to the left and to the right where nums[i] is the smallest
        # in that range from left to right. This is to include all of its occurences.
        # To find out such ranges of each i\nums[i], we can use a monotonic stack.
        # Once we found the intervals of each nums[i], our answer is going to be the same
        # as the number of unique intervals we have, because each interval is a logical
        # unit that needs to be operated on individually

        n = len(nums)

        left_bound = [i for i in range(n)]
        stk = []

        for i in range(n):
            num = nums[i]
            left = i

            while stk and stk[-1][-1] >= num:
                lleft, lnum = stk.pop()
                left = lleft

            left_bound[i] = left
            stk.append((left, num))
            

        right_bound = [i for i in range(n)]
        stk = []

        for i in range(n - 1, -1, -1):
            num = nums[i]
            right = i

            while stk and stk[-1][-1] >= num:
                rright, rnum = stk.pop()
                right = rright

            right_bound[i] = right
            stk.append((right, num))


        intervals = set()

        for i in range(n):
            # already zero, no operations required, so skip
            if nums[i] == 0:
                continue

            left = left_bound[i]
            right = right_bound[i]

            intervals.add((left, right))


        return len(intervals)
