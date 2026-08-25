class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # any distance between two points where the horizontal and vertical
        # distances are equal can juust be traversed diagonally, and any leftover
        # will be traversed either vertically or horizontally respectively
        res = 0
        n = len(points)
        for i in range(1, n):
            x, y = points[i]
            px, py = points[i - 1]

            hor = abs(x - px)
            vert = abs(y - py)

            res += min(hor, vert) + max(hor, vert) - min(hor, vert)
            #      (diagonal dist)  (      leftover distance      ) 

        return res
        
