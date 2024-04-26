class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # index the board in Boustrophedon style and use bfs to find the shortest path
        n, val, vals, flag = len(board), 1, defaultdict(int), False

        for i in reversed(range(n)):
            if flag:
                for j in reversed(range(n)):
                    vals[val] = (i, j)
                    val += 1
                flag = False
            else:
                for j in range(n):
                    vals[val] = (i, j)
                    val += 1
                flag = True

        visited = set()
        que = deque([1])

        def bfs():
            moves = 0

            while que:
                for _ in range(len(que)):
                    curr = que.popleft()
                    if curr in visited: continue
                    visited.add(curr)

                    if curr >= n ** 2: return moves

                    for d_x in range(1, 7):
                        new = curr + d_x
                        if new not in vals: continue

                        r, c = vals[new]

                        if board[r][c] != -1: new = board[r][c]

                        if new not in visited: que.append(new)

                moves += 1

            return moves

        ans = bfs()

        return ans if n ** 2 in visited else -1
