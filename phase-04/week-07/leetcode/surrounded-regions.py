class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # approach uilizes a multi-source bfs where the sources are THE "O"s located at border
        # from them we exhaustively bfs possibly un-capture-able "O"s
        # at the the end, if there ar any "O"s left that means they can be captured
        M, N = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        inbound = lambda r, c: 0 <= r < M and 0 <= c < N
        que, visited =  deque(), set()

        # we identify border "O"s and add them into the queue
        for i in [0,M-1]:
            for j in range(N):
                if board[i][j] == "O":
                    que.append((i,j))
        for i in range(M):
            for j in [0,N-1]:
                if board[i][j] == "O":
                    que.append((i,j))


        def bfs(que, visited):
            while que:
                for _ in range(len(que)):
                    r, c = que.popleft()

                    if (r,c) in visited: continue
                    visited.add((r,c))
                    # mark as "N" for "No, can't be captured"
                    board[r][c] = "N"

                    for d_r, d_c in dirs:
                        r_new, c_new = r + d_r, c + d_c

                        if inbound(r_new, c_new) and board[r_new][c_new] == "O":
                            que.append((r_new, c_new))

        bfs(que, visited)

        for i in range(M):
            for j in range(N):
                # meaning it was not reached from a border "O", hence can be captured
                if board[i][j] == "O": board[i][j] = "X"
                # meaning it was captured, we undo what we did to it
                elif board[i][j] == "N": board[i][j] = "O"


            
