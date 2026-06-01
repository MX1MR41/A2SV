class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)

        count = 1
        res = 0
        for i in range(len(cost)):
            if count % 3 == 0:
                count += 1
                continue

            res += cost[i]
            count += 1

        return res

        
