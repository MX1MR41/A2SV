class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # dijkstra, heap
        g = defaultdict(list)

        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, 2*w))

        heap = [(0, 0)]
        seen = set()
        while heap:
            tot, node = heappop(heap)
            if node in seen:
                continue

            seen.add(node)

            if node == n - 1:
                return tot

            for nei, w in g[node]:

                heappush(heap, (tot + w, nei))

        return -1


        
