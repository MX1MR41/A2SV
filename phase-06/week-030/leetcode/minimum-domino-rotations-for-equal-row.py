class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        count = Counter()
        n = len(tops)

        for i in range(n):
            if tops[i] != bottoms[i]:
                count[tops[i]] += 1
                count[bottoms[i]] += 1
            else:
                count[tops[i]] += 1




        res = n

        topcnt = Counter(tops)
        botcnt = Counter(bottoms)

        for num, freq in count.items():
            if freq >= n:
                curr = n - max(topcnt[num], botcnt[num])
                res = min(res, curr)

        return res if res != n else -1
        
