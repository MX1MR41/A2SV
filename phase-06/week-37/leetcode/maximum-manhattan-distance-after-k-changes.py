class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        cnt = Counter()

        res = 0

        for i in s:
            flips = k
            cnt[i] += 1

            v = sorted([cnt["N"], cnt["S"]])
            h = sorted([cnt["E"], cnt["W"]])

            vert = 0
            horz = 0

            vert = v[1] - v[0]
            horz = h[1] - h[0]

            if v[0]:
                if flips <= v[0]:

                    v[1] += flips
                    v[0] -= flips
                    vert = v[1] - v[0]
                    flips = 0

                else:
                    v[1] += v[0]
                    flips -= v[0]
                    v[0] = 0
                    vert = v[1] - v[0]

            if h[0]:
                if flips <= h[0]:

                    h[1] += flips
                    h[0] -= flips
                    horz = h[1] - h[0]
                    flips = 0

                else:
                    h[1] += h[0]
                    h[0] = 0
                    horz = h[1] - h[0]

            man = vert + horz

            res = max(res, man)

        return res
