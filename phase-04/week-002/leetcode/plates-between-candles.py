from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = []
        for i in range(len(s)):
            if s[i] == '|':
                candles.append(i)

        res = []
        for start, end in queries:
            l, r = -1, -1
            l = bisect_left(candles, start)
            r = bisect_right(candles, end) - 1

            if (l != -1) and (r != -1) and (r > l):
                res.append((candles[r] - candles[l]) - (r - l))
            else:
                res.append(0)
        
        return res
