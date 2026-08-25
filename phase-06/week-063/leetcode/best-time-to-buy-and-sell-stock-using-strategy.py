class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        # sliding window
        # the window consists of the k-subarray we can modify
        # as we move the window one element at a time, we modify the contributions of
        # the three elements: the elements at the left, right and middle of the winodw
        n = len(prices)
        res = sum(prices[i] * strategy[i] for i in range(n))

        curr = 0
        for i in range(k, n):
            curr += prices[i] * strategy[i]

        for i in range(k//2, k):
            curr += prices[i]

        res = max(res, curr)

        for i in range(k, n):
            # the newly added element to the right of the window
            curr -= prices[i] * strategy[i]
            curr += prices[i]

            # the middle element in the window
            curr -= prices[i - k//2]

            # the last element removed from the left of the window
            curr += prices[i - k] * strategy[i - k]

            res = max(res, curr)

        return res



        [0,1,2,3,4,5,6,7,8]

        
