class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # prefix sum
        # create an array of and range update it in a prefix sum manner
        # the maximum number is the minimum number of groups required
        
        _max = 0
        for l, r in intervals:
            _max = max(_max, l, r)

        range_sum = [0] * (_max + 2)

        for l, r in intervals:

            range_sum[l] += 1
            range_sum[r + 1] -= 1

        p = 0

        res = 0

        for i in range(len(range_sum)):
            p += range_sum[i]

            res = max(res, p)

        return res
