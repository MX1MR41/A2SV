class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        m = numRows
        if m == 1:
            return s
            
        mat = [['' for _ in range(n)] for _ in range(m)]
        
        next_dir = {
            (1, 0) : (-1, 1),
            (-1, 1): (1, 0)
        }

        inbound = lambda i, j : 0 <= i < m and 0 <= j < n

        i = j = 0
        di, dj = 1, 0

        for letter in s:
            mat[i][j] = letter
            ni = i + di
            nj = j + dj
            if not inbound(ni, nj):
                di, dj = next_dir[(di, dj)]
                ni = i + di
                nj = j + dj

            i = ni
            j = nj

  

        res = ""
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    res += mat[i][j]

        return res
            
        
