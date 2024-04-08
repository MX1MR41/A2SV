class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        M, N = len(board), len(board[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
        inbound = lambda r, c : 0 <= r < M and  0 <= c < N

        def dfs(r,c, visited):
            if (r,c) not in visited:
                visited.add((r,c))
                if board[r][c] == "M": 
                    board[r][c] = "X"
                    return

                M = 0
                for d_r, d_c in dirs:
                    r_new, c_new = r + d_r, c + d_c
                    if inbound(r_new, c_new):
                        if board[r_new][c_new] == "M": 
                            M += 1

                if M: 
                    board[r][c] = str(M)
                    return 
                 
                board[r][c] = "B"
                for d_r, d_c in dirs:
                    r_new, c_new = r + d_r, c + d_c
                    if inbound(r_new, c_new): 
                        dfs(r_new, c_new, visited)

        visited = set()
        dfs(*click, visited)

        return board


        
