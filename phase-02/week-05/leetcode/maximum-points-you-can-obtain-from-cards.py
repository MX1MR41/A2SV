class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n, tot = len(cardPoints), sum(cardPoints)
        last_ind = n - k
        small = wind = sum(cardPoints[:last_ind])
        for i in range(last_ind, n):
            wind += cardPoints[i]
            wind -= cardPoints[i - last_ind]
            small = min(small, wind)
        return tot - small