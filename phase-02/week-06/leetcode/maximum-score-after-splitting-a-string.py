class Solution:
    def maxScore(self, s: str) -> int:
        cnt = Counter(s)
        res = 0
        z, o = 0, cnt["1"]
        n = len(s)

        for i in range(n-1):
            x = s[i]
            if x == "0":
                z += 1
            else:
                o -= 1

            res = max(res, z+o)

        return res
        