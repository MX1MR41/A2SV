class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: [x[0], -x[1]])

        res = []
        for s, e in intervals:
            if res and res[-1][0] <= s and res[-1][1] >= e:
                continue

            res.append((s, e))

        return len(res)
        
