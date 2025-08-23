class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # minimal area of a rectangle inside the box [r1..r2] x [c1..c2]
        # that covers all 1s that lie inside that box.
        def min_area_box(r1, r2, c1, c2):
            minr, maxr = m, -1
            minc, maxc = n, -1
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if grid[i][j] == 1:
                        if i < minr: minr = i
                        if i > maxr: maxr = i
                        if j < minc: minc = j
                        if j > maxc: maxc = j
            if maxr == -1:  # no ones in this box
                return 0
            return (maxr - minr + 1) * (maxc - minc + 1)

        ans = m * n

        # 1) three horizontal stripes
        for a in range(1, m - 1):
            for b in range(a + 1, m):
                area = (min_area_box(0, a - 1, 0, n - 1) +
                        min_area_box(a, b - 1, 0, n - 1) +
                        min_area_box(b, m - 1, 0, n - 1))
                if area < ans: ans = area

        # 2) three vertical stripes
        for a in range(1, n - 1):
            for b in range(a + 1, n):
                area = (min_area_box(0, m - 1, 0, a - 1) +
                        min_area_box(0, m - 1, a, b - 1) +
                        min_area_box(0, m - 1, b, n - 1))
                if area < ans: ans = area

        # 3) first cut horizontal, then cut top or bottom vertically
        for r in range(1, m):
            # cut the top rectangle vertically
            for c in range(1, n):
                area = (min_area_box(0, r - 1, 0, c - 1) +
                        min_area_box(0, r - 1, c, n - 1) +
                        min_area_box(r, m - 1, 0, n - 1))
                if area < ans: ans = area
            # cut the bottom rectangle vertically
            for c in range(1, n):
                area = (min_area_box(0, r - 1, 0, n - 1) +
                        min_area_box(r, m - 1, 0, c - 1) +
                        min_area_box(r, m - 1, c, n - 1))
                if area < ans: ans = area

        # 4) first cut vertical, then cut left or right horizontally
        for c in range(1, n):
            # cut the left rectangle horizontally
            for r in range(1, m):
                area = (min_area_box(0, r - 1, 0, c - 1) +
                        min_area_box(r, m - 1, 0, c - 1) +
                        min_area_box(0, m - 1, c, n - 1))
                if area < ans: ans = area
            # cut the right rectangle horizontally
            for r in range(1, m):
                area = (min_area_box(0, m - 1, 0, c - 1) +
                        min_area_box(0, r - 1, c, n - 1) +
                        min_area_box(r, m - 1, c, n - 1))
                if area < ans: ans = area

        return ans
