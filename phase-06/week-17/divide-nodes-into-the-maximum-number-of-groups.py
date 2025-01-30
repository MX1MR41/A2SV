from collections import defaultdict, deque
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # Step 1: Check if the graph is bipartite
        color = {}
        def isBipartite(node):
            q = deque([node])
            color[node] = 0  # Start coloring from 0
            while q:
                cur = q.popleft()
                for nei in g[cur]:
                    if nei not in color:
                        color[nei] = 1 - color[cur]  # Alternate colors
                        q.append(nei)
                    elif color[nei] == color[cur]:
                        return False  # Odd-length cycle found, graph is not bipartite
            return True

        # Check all components for bipartiteness
        for node in range(1, n + 1):
            if node not in color:  # Unvisited node, start BFS
                if not isBipartite(node):
                    return -1  # Graph is not bipartite

        # Step 2: Find max BFS depth for each connected component
        seen = set()
        def bfs_max_depth(start):
            q = deque([start])
            visited = set([start])
            level = 0
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    for nei in g[node]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
                level += 1
            return level

        # Find all connected components
        res = 0
        for node in range(1, n + 1):
            if node not in seen:
                component = set()
                q = deque([node])
                while q:
                    v = q.popleft()
                    if v in seen:
                        continue
                    seen.add(v)
                    component.add(v)
                    for nei in g[v]:
                        if nei not in seen:
                            q.append(nei)

                # Compute the max BFS depth for this component
                max_depth = 0
                for v in component:
                    max_depth = max(max_depth, bfs_max_depth(v))

                res += max_depth

        return res
