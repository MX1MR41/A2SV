class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        # recursively minimize the polygon one triangle at a time
        # while minimizing the answer
        dp = defaultdict(int)
        def dfs(i, j):
            if (i,j) in dp: return dp[(i,j)]
            if i + 1 == j:
                return 0
                
            curr = float("inf")
            for k in range(i+1, j):
                temp = dfs(i, k) + dfs(k, j) + values[i] * values[k] * values[j]
                curr = min(curr, temp)

            dp[(i,j)] = curr if curr != float(inf) else 0
            return curr

        return dfs(0, len(values) - 1)
