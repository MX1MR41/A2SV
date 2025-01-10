from collections import defaultdict
import heapq

def can_defeat_all_monsters(n, m, danger_levels, edges):
    graph = defaultdict(list)
    
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)

    def bfs(start):
        min_heap = []
        heapq.heappush(min_heap, (danger_levels[start - 1], start))  
        visited[start] = True

        size_s = 0  
        defeated = 0  

        while min_heap:
            current_danger, node = heapq.heappop(min_heap)

            if current_danger > defeated:
                return False

            size_s += 1
            defeated += 1

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    heapq.heappush(min_heap, (danger_levels[neighbor - 1], neighbor))

        return size_s == n

    for i in range(1, n + 1):
        if danger_levels[i - 1] == 0 and not visited[i]:
            if bfs(i):
                return "YES"

    return "NO"



results = []

for _ in range(int(input())):
    n, m = map(int, input().split())
    danger_levels = list(map(int, input().split()))
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    result = can_defeat_all_monsters(n, m, danger_levels, edges)
    results.append(result)

print("\n".join(results))


