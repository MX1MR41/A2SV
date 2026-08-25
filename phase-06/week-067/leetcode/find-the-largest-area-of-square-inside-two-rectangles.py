class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:

        res = 0
        n = len(bottomLeft)
        rects = [bottomLeft[i] + topRight[i] for i in range(n)]
        rects.sort()

        def overlap(rect1, rect2):
            return not (
            rect1[2] <= rect2[0] 
            or rect1[3] <= rect2[1] 
            or rect2[2] <= rect1[0]
            or rect2[3] <= rect1[1])


        for i in range(n):
            a = rects[i]
            for j in range(i + 1, n):
                b = rects[j]

                if overlap(a, b):
                    x1 = [a[0], a[2]]
                    x2 = [b[0], b[2]]

                    

                    y1 = [a[1], a[3]]
                    y2 = [b[1], b[3]]

                    if y2 < y1:
                        y1, y2 = y2, y1

                    x = x1[1] - x2[0] if x2[1] > x1[1] else x2[1] - x2[0]
                    y = y1[1] - y2[0] if y2[1] > y1[1] else y2[1] - y2[0]




                    area = min(x, y) ** 2
                    res = max(res, area)

        return res


        
