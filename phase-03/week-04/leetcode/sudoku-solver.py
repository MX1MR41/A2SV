class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # checks if putting a number c at board[row][col] is valid
        def isValid(board, row, col, c):
            for i in range(9):
                if board[row][i] == c or board[i][col] == c:
                    return False
                # if 'c' exists in the same 3x3 sub-grid
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
                    return False
            return True  

        def solve(board):
            # traversing cell by cell, not [i][j] by [i][j]
            for i in range(9):
                # traversing [i][j] by [i][j]
                for j in range(9):
                    
                    if board[i][j] == '.':
                    
                        for c in map(str, range(1, 10)):
                            if isValid(board, i, j, c):
                                board[i][j] = c
                                # recursively attempt to solve the puzzle with the updated board
                                if solve(board):
                                    return True  
                                else:
                                    
                                    board[i][j] = '.'  
                        return False 
            return True 

        
        solve(board)
