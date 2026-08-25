class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #initialize the board
        board = [["." for _ in range(n)] for _ in range(n)]
        # sets to store the cols that are forbidden and
        # the forbidden diagonal values by the property that 
        # diagonals that go up have the same (row - col) and
        # diagonals that go down have the same (row + col)
        cols, updiag, downdiag = set(), set(), set()

        res = []

        def queen(row):
            if row == n: # if we have exhausted all the queens
                res.append(["".join(r) for r in board][:])

            # we iterate by cols instead of by [row][col]
            # because we know that if one queen has take a row,
            # no other queen can be placed on the same row
            for col in range(n):

                # in case the current col of the row we are exploring is forbidden
                # due to either another queen being placed in the same col in another row
                # or another queen has been placed in a diagonally reacheable spot
                if col in cols or row+col in updiag or row-col in downdiag:
                    continue
                
                # the usual backtracking template:
                # try this possibility, recur then un-try this possibility 
                cols.add(col)
                updiag.add(row+col)
                downdiag.add(row-col)
                board[row][col] = "Q"

                # find a valid psotition for a queen in the next row
                queen(row + 1)

                cols.remove(col)
                updiag.remove(row+col)
                downdiag.remove(row-col)
                board[row][col] = "."


        queen(0)

        return res

                