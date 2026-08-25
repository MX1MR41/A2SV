class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        l, r = n//2-1, n//2 
        al = bob = 0
        for _ in range(n//2):
            left, right = piles[l], piles[r]
            if left >= right:
                al += left
                bob += right

            else:
                al += right
                bob += left

            l -= 1
            r += 1

        return al > bob



