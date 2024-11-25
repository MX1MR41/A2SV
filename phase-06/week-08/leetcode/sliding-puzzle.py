class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # bfs over the possible set of moves
        zero = []
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    zero = [i, j]
                    break

        que = deque([(board, zero)])

        seen = set()
        moves = 0
        while que:

            for _ in range(len(que)):
                board, (i, j) = que.popleft()
                if tuple(board[0] + board[1]) in seen:
                    continue

                seen.add(tuple(board[0] + board[1]))
                if board == [[1, 2, 3], [4, 5, 0]]:
                    return moves

                move1 = [i[::] for i in board]
                move1[0][j], move1[1][j] = move1[1][j], move1[0][j]
                que.append((move1, (1 - i, j)))

                if j < 2:
                    move2 = [i[::] for i in board]
                    move2[i][j], move2[i][j + 1] = move2[i][j + 1], move2[i][j]
                    que.append((move2, (i, j + 1)))

                if j > 0:
                    move3 = [i[::] for i in board]
                    move3[i][j], move3[i][j - 1] = move3[i][j - 1], move3[i][j]
                    que.append((move3, (i, j - 1)))

            moves += 1

        return -1
