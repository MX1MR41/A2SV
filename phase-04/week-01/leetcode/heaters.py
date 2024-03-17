class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res = 0
        houses.sort()
        heaters.sort()

        for h in houses:
            l = bisect_right(heaters, h) - 1
            r = bisect_left(heaters, h)

            if l < 0:
                res = max(res, heaters[0] - h)

            elif r >= len(heaters):
                res = max(res, h - heaters[-1])

            else:
                res = max(res, min(h - heaters[l], heaters[r] - h))

        return res