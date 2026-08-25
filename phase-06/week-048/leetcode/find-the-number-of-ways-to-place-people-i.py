class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # sorting
        # once the points are sorted in increasing order of x and decreasing order of y,
        #  points[i] and points[i + k] can be valid if no point[i + 1 ... i + k - 1]
        # is located inside or on them

        points.sort(key=lambda x: [x[0], -x[1]])

        res = 0

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                can = True

                x2, y2 = points[j]
                if x2 < x1 or y2 > y1:
                    continue
                for k in range(i + 1, j):
                    x3, y3 = points[k]
                    if x1 <= x3 <= x2 and y1 >= y3 >= y2:
                        can = False
                        break

                if can:

                    res += 1

        return res
