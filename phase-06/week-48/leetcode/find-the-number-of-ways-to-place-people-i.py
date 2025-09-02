class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x: [-x[0], x[1]])

        res = 0

        for i in range(len(points)):
            r1, c1 = points[i]
            for j in range(i + 1, len(points)):
                can = True

                r2, c2 = points[j]
                if r2 > r1 or c2 < c1:
                    continue
                for k in range(i + 1, j):
                    r3, c3 = points[k]
                    if r1 <= r3 <= r2 or c1 <= c3 <= c2:
                        can = False
                        break

                if can:
                    res += 1

        return res
