class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = []
        for _ in range(m - 1):
            row = "."
            row += "#" * (n - 1)
            res.append(row)

   
        res.append("." * n)

        return res


        
