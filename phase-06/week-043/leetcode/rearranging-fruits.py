class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:


        total = Counter(basket1 + basket2)

        if any(j % 2 for i, j in total.items()):
            return -1

        extra1 = []
        extra2 = []

        count1 = Counter(basket1)
        for i in count1:
            if count1[i] > total[i]//2:
                extra = count1[i] - total[i]//2
                extra1.extend([i] * extra)

        count2 = Counter(basket2)
        for i in count2:
            if count2[i] > total[i]//2:
                extra = count2[i] - total[i]//2
                extra2.extend([i] * extra)


        cost = 0

        global_min = min(basket1 + basket2)

        for a, b in zip(sorted(extra1), sorted(extra2, reverse = True)):
            cost += min( min(a,b), 2*global_min )


        return cost
