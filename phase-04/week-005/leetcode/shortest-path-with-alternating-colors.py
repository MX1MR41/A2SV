from collections import defaultdict, deque
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        red, blue = defaultdict(list), defaultdict(list)

        for u, v in redEdges:
            red[u].append(v)

        for u, v in blueEdges:
            blue[u].append(v)

        def bfs(col, q, target):
            path, visited = 0, set()

            while q:
                for _ in range(len(q)):
                    node = q.popleft()

                    if node == target: return path

                    if (col,node) in visited: continue

                    visited.add((col,node))
                    
                    # 0 for red, and 1 for blue
                    if col == 0: nei = red[node]
                    else: nei = blue[node]

                    for new in nei: q.append(new)

                # switch to the other color after queue operations are done
                col = 1 - col
                path += 1

            return -1

        res = [0]
        for i in range(1, n):
            RED = bfs(0, deque([0]), i)
            BLUE = bfs(1, deque([0]), i)

            if RED == -1 and BLUE == -1: # no path exists whether we start from blue or red
                res.append(-1)
            elif RED != -1 and BLUE == -1: 
                res.append(RED)
            elif RED == -1 and BLUE != -1:
                res.append(BLUE)
            else: # choose the shortest one in case both pathes exist
                res.append(min(BLUE, RED))

        return res
