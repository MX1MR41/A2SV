class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # binary search inside binary search
        bottom = [(x, y) for x, y in points if y == 0]
        right = [(x, y) for x, y in points if (x == side and 0 < y < side)]
        up = [(x, y) for x, y in points if y == side]
        left = [(x, y) for x, y in points if x == 0 and 0 < y < side]

        points = []
        for x, y in bottom:
            points.append(x)

        for x, y in right:
            points.append(side + y)

        for x, y in up:
            points.append(2 * side + (side - x))

        for x, y in left:
            points.append(3 * side + (side - y))

        points.sort()

        n = len(points)
        points += [4 * side + p for p in points]

        def check(d):
            for s in range(n):
                curr_idx = s
                valid = True

                for _ in range(k - 1):

                    next_idx = bisect.bisect_left(
                        points, points[curr_idx] + d, curr_idx + 1
                    )

                    if next_idx == len(points):
                        valid = False
                        break

                    curr_idx = next_idx

                if valid:

                    if points[s + n] - points[curr_idx] >= d:
                        return True

            return False

        res = 0

        l, r = 0, 10**9

        while l <= r:
            mid = (l + r) // 2

            if check(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return res
