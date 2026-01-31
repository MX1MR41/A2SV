class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # dijkstra + bfs + heap + dynamic programming
        # for every s in source perform dijkstra to find the minimum distance to all
        # its reachable nodes
        # then use dynamic programming dp where dp[i] if the min cost to convert source[:i + 1] to target[:i + 1]
        # populate the dp by slicing the source string by the possible sources lengths
        # and computing dp[i] as dp[i - k] + cost of converting source[i - k:i + 1] to target[i - k: i + 1]
        g = defaultdict(lambda: defaultdict(lambda: float("inf")))
        for i in range(len(original)):
            u = original[i]
            v = changed[i]
            w = cost[i]

            g[u][v] = min(g[u][v], w)

        def dijkstra(source):
            heap = [(0, source)]
            seen = set()

            while heap:
                d, node = heappop(heap)
                if node in seen:
                    continue

                seen.add(node)
                g[source][node] = min(g[source][node], d)

                for nei in g[node]:
                    if nei in seen:
                        continue

                    heappush(heap, (d + g[node][nei], nei))

        seeds = list(g.keys())
        for node in seeds:
            dijkstra(node)

        n = len(source)
        dp = [float("inf") for _ in range(n)]

        lengths = sorted(list(set(len(i) for i in original)))

        for i in range(n):

            if source[i] == target[i]:
                dp[i] = dp[i - 1] if i - 1 >= 0 else 0

            # we only need to check the lengths of the source node
            for l in lengths:
                j = i - l + 1

                if j < 0:
                    continue

                u = source[j : i + 1]
                v = target[j : i + 1]

                if g[u][v] != float("inf"):

                    prev_cost = dp[j - 1] if j - 1 >= 0 else 0
                    dp[i] = min(dp[i], prev_cost + g[u][v])

        return dp[-1] if dp[-1] != float("inf") else -1

        
