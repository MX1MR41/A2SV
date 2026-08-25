class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        ans = float("inf")
        n = len(timePoints)
        for i in range(n):
            curr = timePoints[i]
            nxt = timePoints[(i + 1) % n]
            curr = int(curr[:2])*60 + int(curr[3:])
            nxt = int(nxt[:2])*60 + int(nxt[3:])
            if nxt < curr:
                nxt += 24*60
            ans = min(ans, nxt - curr)

        return ans
            
