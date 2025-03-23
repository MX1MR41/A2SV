class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # SSSP Dijkstra
        MOD = 10**9 + 7
        graph = defaultdict(list)
        
        # Build graph
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        # Initialize distances and ways arrays.
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        
        # Min-heap: (current_time, node)
        heap = [(0, 0)]
        
        while heap:
            time, node = heapq.heappop(heap)
            
            # Skip if we already found a better route.
            if time > dist[node]:
                continue
            
            for neighbor, t in graph[node]:
                new_time = time + t
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heapq.heappush(heap, (new_time, neighbor))
                elif new_time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
        
        return ways[n - 1]
