class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # dijkstra: just bfs with heap instead of queue
        g = defaultdict(list)

        for u, v, wei in edges:
            g[u].append((v, wei))
            g[v].append((u, wei))

        def dijkstra(city):
            heap = [(0, city)]
            visited = set()

            while heap:
                dist, node = heappop(heap)
                if node in visited:
                    continue
                visited.add(node)
                for nei, d in g[node]:
                    if dist + d <= distanceThreshold:
                        heappush(heap, (d + dist, nei))
                        
            return len(visited)

        ans = [0, float("inf")]
        for city in range(n):
            cities = dijkstra(city)
            if cities <= ans[1]:
                ans = [city, cities]

        return ans[0]
