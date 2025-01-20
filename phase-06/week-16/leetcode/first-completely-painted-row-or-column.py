class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        row, col = dict(), dict()
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                num = mat[i][j]
                row[num] = i
                col[num] = j

        count_row, count_col = defaultdict(int), defaultdict(int)

        for index in range(len(arr)):
            num = arr[index]

            r, c = row[num], col[num]
            count_row[r] += 1
            if count_row[r] == n:
                return index

            count_col[c] += 1

            if count_col[c] == m:
                return index
