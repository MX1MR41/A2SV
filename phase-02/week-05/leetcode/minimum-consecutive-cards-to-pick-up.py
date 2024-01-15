class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = float("inf")
        d = {}
        n = len(cards)
        for i in range(n):
            a = cards[i]
            if a in d:
                ind = d[a]
                res = min(res, i-ind + 1)

            d[a] = i

        return res if res != float("inf") else -1

        