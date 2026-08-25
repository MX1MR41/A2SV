class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # dp inside dp
        # instead of a triple loop, we store leftwise and rightwise max choices
        m, n = len(points), len(points[0])

        prev = points[0]

        for i in range(1, m):
            left = [0] * n
            right = [0] * n

            left[0] = prev[0]
            for j in range(1, n):
                left[j] = max(left[j - 1] - 1, prev[j])

            right[n - 1] = prev[n - 1]
            for j in range(n - 2, -1, -1):
                right[j] = max(right[j + 1] - 1, prev[j])

            for j in range(n):
                points[i][j] += max(left[j], right[j])

            prev = points[i]

        return max(prev)
