class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # sorting
        # once the points are sorted in increasing order of x and decreasing order of y,
        # points[i] and points[i + k] can be valid if no point[i + 1 ... i + k - 1]
        # is located inside or on them.
        # to simplify we compress the coordinates by only taking the y values, since
        # the points were sorted in incresing x order, every y[i + k] will be located
        # after y[i]. 
        # we check every possible pairing (y1, y2), but as we do so, we keep track of
        # the maximum value of y2 we have seen so far for y1's loop. and if the new y2
        # happens to be less than or equal to max_y2, it means it will be located on
        # or inside the rectangle we would make with y1 and y2

        points.sort(key=lambda x: [x[0], -x[1]])

        ys = [p[1] for p in points]

        res = 0

        for i in range(len(ys)):
            y1 = ys[i]
            max_y2 = float("-inf")
            for j in range(i + 1, len(ys)):
                y2 = ys[j]
                if y2 > y1:
                    continue

                if max_y2 < y2:
                    res += 1

                max_y2 = max(max_y2, y2)


        return res
