class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        # BFS + bitmask
        # go through the search space using bfs
        # a space can defined with (row, col, energy, collected litter, moves)
        # to keep track of the collecte litter efficiently, use bitmask

        m, n = len(classroom), len(classroom[0])

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        valid = lambda i, j: 0 <= i < m and 0 <= j < n

        
        # start row and column
        sr = sc = -1
        lits = []
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "S":
                    sr, sc = i, j

                if classroom[i][j] == "L":
                    lits.append((i, j))

        full_mask = (1 << len(lits)) - 1

        # mapping to keep track of the best energy we had at (row, column, mask)
        best_energy = defaultdict(lambda: -1)

        que = deque([(sr, sc, energy, 0, 0)])

        while que:
            for _ in range(len(que)):
                r, c, e, mask, moves = que.popleft()

                # first state that collected all the litter with the least moves
                if mask == full_mask:
                    return moves

                # no energy to perform any more moves
                if e <= 0:
                    continue

                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if valid(nr, nc) and classroom[nr][nc] != "X":
                        new_mask = mask
                        ne = e - 1

                        if classroom[nr][nc] == "L":
                            ind = lits.index((nr, nc))
                            new_mask |= 1 << ind # collect this litter

                        if classroom[nr][nc] == "R":
                            ne = energy # replenish energy
                        
                        # since the last time we were at this state we had less energy,
                        # we can explore more his time, so we put it in the queue
                        if best_energy[(nr, nc, new_mask)] < ne:
                            best_energy[(nr, nc, new_mask)] = ne
                            que.append((nr, nc, ne, new_mask, moves + 1))

        return -1
