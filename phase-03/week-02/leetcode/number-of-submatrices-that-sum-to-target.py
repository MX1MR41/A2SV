class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        sub_sum = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                top = sub_sum[i-1][j] if i > 0 else 0
                left = sub_sum[i][j-1] if j > 0 else 0
                top_left = sub_sum[i-1][j-1] if min(i,j) > 0 else 0
                sub_sum[i][j] = matrix[i][j] + top + left - top_left

        res = 0
        for r1 in range(rows):
            for r2 in range(r1, rows):
                cnt = defaultdict(int)
                cnt[0] = 1
                for c in range(cols):
                    curr = sub_sum[r2][c] - (sub_sum[r1-1][c] if r1 > 0 else 0)

                    diff = curr - target
                    res += cnt[diff]
                    cnt[curr] += 1

        return res
        