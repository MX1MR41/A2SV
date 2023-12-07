class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        
        for p in range(len(points) - 1):
            
            xi, yi = points[p]
            xj,  yj = points[p+1]
            x_diff = abs(xi - xj)
            y_diff = abs(yi - yj)


            if x_diff == y_diff:  # on the same line diagonally
                time += x_diff
                continue

            elif xi == xj and yi != yj: # on the same line vertically
                time += y_diff
                continue

            elif xi != xj and yi == yj: # on the same line horizontally
                time += x_diff
                continue

            else: # everything else
                time += min(x_diff, y_diff) + abs(x_diff - y_diff) 




        return time
        