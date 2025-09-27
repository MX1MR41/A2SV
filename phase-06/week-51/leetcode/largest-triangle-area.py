class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]

                    # Shoelace formula
                    area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0
                    res = max(res, area)

        return res
