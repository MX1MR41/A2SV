class Solution:
    def coloredCells(self, n: int) -> int:
        # there is a pattern in the drawings
        tot = 1
        curr = 1
        extra = 0
        if n == 1:
            return tot

        while curr < n:
            tot += 4
            tot += 4 * extra
            extra += 1

            curr += 1

        return tot
