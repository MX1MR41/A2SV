class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # counting
        # count the number of lines at each level (y-coordinate)
        # and multiple those lines with the number of lines above that y-coordinate
        # it also works without sorting and going upwards y by y, we can just process a
        # y coordinate then remove its contribution from the total
        # PS: using / instead of // will produce floats and consequently errors 
        # because python loses precision
        # when working with large number converted to float
        y_points = defaultdict(int)
        for x, y in points:
            y_points[y] += 1

        total_lines = 0
        for y, xs in y_points.items():
            total_lines += (xs * (xs - 1))//2

        res = 0
        for y, xs in y_points.items():
            curr_lines = (xs * (xs - 1))//2
            total_lines -= curr_lines

            res = (res + (curr_lines * total_lines)) % 1000000007

        return int(res)
