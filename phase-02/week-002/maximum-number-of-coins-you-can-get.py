class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # we can sort the piles and then start from second to last 
        # and keep iterating backwards by 2 and adding the pile at that index
        # this works because we can assume that Alice takes the first to last (largest)
        # then you take the second to last at every n//3 iteration
        piles.sort()
        ans = 0
        n = len(piles)
        i = n -2
        for _ in range(n//3):
            ans += piles[i]
            i -= 2

        return ans

        