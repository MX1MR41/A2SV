class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonic stack + dp + prefix
        # for each height h, we need to find the number of heights to its left and
        # to its right that are equal to or higher than it. Using those we can
        # form an area of height h and length number of said neighboring heights.
        # use a monotonic stack where the top of the stack contains the largest
        # height so far. For each h, we keep popping from stack as long as valid
        # heights are on the top of the stack and we count the number of pops as
        # valid immediate neighboring heights. Then store that height along the 
        # number of pops (valid neighboring heights) onto the stack. The number
        # of valid neighboring heights is also stored so that for later when
        # computing for another height, we can use that number for this height too
        # since it is an overlapping problem.
        # Do this from both ends of the array to store number of heights from both
        # ends, then the answer will be the maximum of which elements multiplied
        # by the sum of the number of its neighboring heights.

        n = len(heights)
        stk = []
        prefix = []
        suffix = []

        for i in range(n):
            h = heights[i]
            count = 0
            while stk and stk[-1][0] >= h:
                valid_height, previous_count = stk.pop()
                count += 1 + previous_count

            stk.append((h, count))

            prefix.append(count)


        stk = []
        for i in range(n - 1, -1, -1):
            h = heights[i]
            count = 0
            while stk and stk[-1][0] >= h:
                valid_height, previous_count = stk.pop()
                count += 1 + previous_count

            stk.append((h, count))

            suffix.append(count)

        
        suffix.reverse()


        res = 0
        for i in range(n):
            h = heights[i]
            area = h * (1 + prefix[i] + suffix[i])
            res = max(res, area)

        return res
