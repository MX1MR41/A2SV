class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        res = 0
        if costBoth < cost1 + cost2:
            res = costBoth * min(need1, need2)
            if need1 > need2:
                rem = need1 - need2
                if cost1 < costBoth:
                    res += cost1 * rem

                else:
                    res += costBoth * rem

            if need2 > need1:
                rem = need2 - need1
                if cost2 < costBoth:
                    res += cost2 * rem

                else:
                    res += costBoth * rem

        else:
            res = cost1 * need1 + cost2 * need2

        return res
        
