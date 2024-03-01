class Solution:
    def totalNQueens(self, n: int) -> int:
        # modified code from n-queens problem
        # https://leetcode.com/problems/n-queens/
        board = [["." for _ in range(n)] for _ in range(n)]
        res, cols, updiag, downdiag = [], set(), set(), set()
        res = []
        def queen(row):
            if row == n: 
                res.append(["".join(r) for r in board][:])
            for col in range(n):
                if col in cols or row+col in updiag or row-col in downdiag:
                    continue
                cols.add(col)
                updiag.add(row+col)
                downdiag.add(row-col)
                board[row][col] = "Q"
                queen(row + 1)
                cols.remove(col)
                updiag.remove(row+col)
                downdiag.remove(row-col)
                board[row][col] = "."
                
        queen(0)

        return len(res)