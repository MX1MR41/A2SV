class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # monotonic stack
        # finding the next smaller element
        ans = prices[::]
        stk = []
        for i, p in enumerate(prices):
            while stk and stk[-1][1] >= p:
                ind, prev = stk.pop()
                prices[ind] -= p

            stk.append((i, p))

        return prices
