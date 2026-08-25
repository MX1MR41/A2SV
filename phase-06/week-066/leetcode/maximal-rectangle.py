class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # dynamic programming +  monotonic stack
        # just the largest rectangle in histogram problem on steroids
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])

        for j in range(n):
            for i in range(1, m):
                if matrix[i][j] != 0:
                    matrix[i][j] += matrix[i - 1][j]

        left = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):

            stack = []
            for j in range(n):
                left_bound = j
                h = matrix[i][j]

                while stack and stack[-1][-1] >= h:
                    last_bound, last_h = stack.pop()
                    left_bound = last_bound

                stack.append((left_bound, h))

                left[i][j] = left_bound

        right = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):

            stack = []
            for j in range(n - 1, -1, -1):
                right_bound = j
                h = matrix[i][j]
                while stack and stack[-1][-1] >= h:
                    last_bound, last_h = stack.pop()
                    right_bound = last_bound

                stack.append((right_bound, h))

                right[i][j] = right_bound

        res = 0
        for i in range(m):
            for j in range(n):

                height = matrix[i][j]
                left_bound = left[i][j]
                right_bound = right[i][j]

                width = right_bound - left_bound + 1

                curr_area = height * width
                res = max(res, curr_area)

        return res
