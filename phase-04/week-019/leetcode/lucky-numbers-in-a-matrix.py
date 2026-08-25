class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        cols_maxes = defaultdict(int)
        rows_mins = defaultdict(int)
        ans = []

        for i in range(m):
            rows_mins[i] = min(matrix[i])


        for j in range(n):
            for i in range(m):
                cols_maxes[j] = max(cols_maxes[j], matrix[i][j])

        ans = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == rows_mins[i] == cols_maxes[j]:
                    ans.append(matrix[i][j])

        return ans
