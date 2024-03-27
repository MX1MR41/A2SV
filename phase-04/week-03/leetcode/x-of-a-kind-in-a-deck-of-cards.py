class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cnt = Counter(deck)
        m = len(cnt)
        if gcd(*list(cnt.values())) > 1:
            return True

        return False
        