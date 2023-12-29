class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        inds = [i[0] for i in points] # only the x indices, we dont need the y indices
        inds.sort()
        m = 0

        for i in range(len(inds)-1):
            area = inds[i+1] - inds[i]
            m = max(area, m)

        return m
        