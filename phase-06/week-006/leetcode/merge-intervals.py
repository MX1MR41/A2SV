class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorting
        
        intervals.sort()

        ans = []
        for s, e in intervals:
            if ans:
                lasts, laste = ans[-1]
                if s <= laste:
                    if e > laste:
                        ans[-1][1] = e
                else:
                    ans.append([s, e])
            else:
                ans.append([s, e])


        return ans
