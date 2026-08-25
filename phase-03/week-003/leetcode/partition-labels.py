class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # store the starting and ending indices for each letter
        # gather them as ranges for each letter and sort the ranges
        # then merge intervals just like https://leetcode.com/problems/merge-intervals/
        
        first = dict()
        last = dict()

        for i, c in enumerate(s):
            if c not in first:
                first[c] = i

            last[c] = i

        intervals = []

        for letter in set(s):
            s = first[letter]
            e = last[letter]

            intervals.append([s, e])

        intervals.sort()


        res = []
        for s, e in intervals:
            if not res:
                res.append([s, e])
                continue

            
            if s < res[-1][-1]:
                res[-1][1] = max(res[-1][-1], e)
            else:
                res.append([s, e])


        return [e - s + 1 for s, e in res]

