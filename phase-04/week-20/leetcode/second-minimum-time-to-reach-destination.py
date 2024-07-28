class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n + 1)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        queue = deque([(1, 1)])
        first_dist = [-1] * (n + 1)
        second_dist = [-1] * (n + 1)
        first_dist[1] = 0

        while queue:
            node, count = queue.popleft()
            current_time = first_dist[node] if count == 1 else second_dist[node]

            if (current_time // change) % 2:
                current_time = change * (current_time // change + 1) + time
            else:
                current_time += time

            for neighbor in graph[node]:
                if first_dist[neighbor] == -1:
                    first_dist[neighbor] = current_time
                    queue.append((neighbor, 1))
                elif second_dist[neighbor] == -1 and first_dist[neighbor] != current_time:
                    if neighbor == n:
                        return current_time
                    second_dist[neighbor] = current_time
                    queue.append((neighbor, 2))
        
        return 0
