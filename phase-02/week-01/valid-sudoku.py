class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ind ={ 0: [0,0], 1: [0,3], 2: [0,6], 
               3: [3,0], 4: [3,3], 5: [3,6],
               6: [6,0], 7: [6,3], 8: [6,6] }

        sudx, sudy = defaultdict(set),  defaultdict(set)
        # dictionaries to hold the row and column that a certain number has been at in a another cell, in sudoku the numbers cant be in the same col or row as in any other cell

        for i in range(9):
            cnt = defaultdict(int)

            x, y = ind[i]

            for j in range(3):
                if board[x+j][y] != '.' and (cnt[board[x+j][y]] or x+j in sudx[board[x+j][y]] or y in sudy[board[x+j][y]]):
                    return False
                cnt[board[x+j][y]] += 1
                sudx[board[x+j][y]].add(x+j)
                sudy[board[x+j][y]].add(y)

                if board[x+j][y+1] != '.' and (cnt[board[x+j][y+1]] or x+j in sudx[board[x+j][y+1]] or y+1 in sudy[board[x+j][y+1]]):
                    return False
                cnt[board[x+j][y+1]] += 1
                sudx[board[x+j][y+1]].add(x+j)
                sudy[board[x+j][y+1]].add(y+1)

                if board[x+j][y+2] != '.' and (cnt[board[x+j][y+2]] or x+j in sudx[board[x+j][y+2]] or y+2 in sudy[board[x+j][y+2]]):
                    return False
                cnt[board[x+j][y+2]] += 1
                sudx[board[x+j][y+2]].add(x+j)
                sudy[board[x+j][y+2]].add(y+2)


        return True
        