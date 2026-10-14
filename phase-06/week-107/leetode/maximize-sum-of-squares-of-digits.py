class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res = []
        for _ in range(num):
            res.append(min(9, sum))
            sum -= min(9, sum)

        return "".join(map(str, res)) if sum == 0 else ""

        
