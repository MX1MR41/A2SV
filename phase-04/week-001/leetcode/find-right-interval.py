class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # approach uses binary search over the search space of 
        # the first elements of the intervals, to find the "right" interval for each
        n = len(intervals)
        # mapping the start elements with their original indices
        # since we will lose the original indices when we sort them
        d = {intervals[i][0]:i for i in range(n)}
        starts = sorted([i[0] for i in intervals])

        res = []

        for i in intervals:
            end = i[1]
            # finds the first occurence of end if it is present
            # or its suitable position to be inserted if it not present
            ans = bisect_left(starts, end)              

            # validating our ans
            if 0 <= ans < n and starts[ans] >= end:
                res.append(d[starts[ans]])
            else:
                res.append(-1)

        return res

        