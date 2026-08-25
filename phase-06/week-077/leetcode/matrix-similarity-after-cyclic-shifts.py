class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        start = mat
        mat = [deque(row) for row in mat]
        m = len(mat)
        for _ in range(k):
            for i in range(0, m, 2):
                mat[i].append(mat[i].popleft())

            for i in range(1, m, 2):
                mat[i].append(mat[i].popleft())


        for i in range(m):
            for j in range(len(mat[0])):
                if mat[i][j] != start[i][j]:
                    return False

        return True


        
