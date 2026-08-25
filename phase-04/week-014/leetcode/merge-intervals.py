class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]

        curr = 1
        n = len(intervals)

        while curr < n:
            if intervals[curr][0] <= ans[-1][-1]:
                ans[-1][-1] = max(intervals[curr][1], ans[-1][-1])
                curr += 1

            else:
                ans.append(intervals[curr])
                curr += 1

        return ans



        
