class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # approach utilizes a multisource BFS 
        # where at the beginning the sources are all the cells that are 0
        # then every iteration of BFS explores the next closest non-zero cells
        # and assigns the number of bfs iterations so far as the distance
        # from that cell to the closest zero cell
        M, N = len(mat), len(mat[0])
        inbound = lambda r, c: 0 <= r < M and 0 <= c < N
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        

        def bfs(que, visited):
            path = 0
            while que:
                for _ in range(len(que)):
                    r, c = que.popleft()

                    if (r, c) in visited: continue
                    visited.add((r, c))

                    if mat[r][c]:
                        ans[r][c] = path

                    for d_r, d_c in dirs:
                        r_new, c_new = r + d_r, c + d_c

                        if inbound(r_new, c_new) and mat[r_new][c_new]:
                            que.append((r_new, c_new))

                path += 1

        ans = mat[::]
        que = deque()

        for i in range(M):
            for j in range(N):
                if not mat[i][j]:
                    que.append((i, j))


        bfs(que, set())

        return ans
