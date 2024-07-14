class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # sorting + binary search + prefix-sum-ish

        combined = sorted(list(zip(difficulty, profit)))

        # binary search
        def search(w):
            l, r = 0, len(combined) - 1
            ans = -1
            while l <= r:
                mid = (l+r)//2
                if combined[mid][0] <=w:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1

            return ans



        prefix_profit = []
        max_profit = 0
        # we use a prefix calculation technique to store the max profit possible
        # upto each job's difficulty
        for diff, pro in combined:
            max_profit = max(max_profit, pro)
            prefix_profit.append(max_profit)

        ans = 0
        for w in worker:
            ind = search(w)
            if combined[ind][0] <= w:
                ans += prefix_profit[ind]

        return ans
