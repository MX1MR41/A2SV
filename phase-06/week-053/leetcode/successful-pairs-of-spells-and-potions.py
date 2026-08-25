class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # sorting  + binary search
        potions.sort()
        res = []

        m = len(potions)
        n = len(spells)

        for i in range(n):
            spell = spells[i]
            need = success/spell

            l, r = 0, m - 1
            ans = bisect_left(potions, need)

            res.append(m - ans)

        return res
        
