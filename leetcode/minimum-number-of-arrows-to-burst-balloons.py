class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        lastInd = points[0][1]
        arrows = 1

        for i in points[1:]:
            if i[0] <= lastInd:
                lastInd = min(lastInd, i[1])
            else:
                arrows += 1
                lastInd = i[1]


        return arrows


        