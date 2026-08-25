class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for u, v, t in times:
            g[u].append((v, t))


        heap = [(0, k)]
        minimum_time = 0

        seen = set()

        while heap:

            cost, node = heappop(heap)
            if node in seen: continue
            seen.add(node)

            minimum_time = max(minimum_time, cost)


            for nei, t in g[node]:
                if nei not in seen:
                    heappush(heap, (cost + t, nei))

        if len(seen) != n: return -1
        return minimum_time
        
