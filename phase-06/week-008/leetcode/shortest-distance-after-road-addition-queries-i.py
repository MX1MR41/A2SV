class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # single source shortest path algorithm + dp
        # ususally sssp would need n iterations to work since there might be backward edges and cycles
        # but this problem guarantees that all edges are unidirectional hence no cycles
        # so one pass will suffice
        
        g = defaultdict(list)
        for i in range(n - 1):
            g[i].append(i + 1)

        dp = [i for i in range(n)]

        ans = []

        for u, v in queries:
            g[u].append(v)

            tempdp = dp[::]
            # for _ in range(n):
            for node in range(n):
                for nei in g[node]:
                    tempdp[nei] = min(tempdp[nei], tempdp[node] + 1)

            dp = tempdp[::]
            ans.append(dp[-1])

        return ans
