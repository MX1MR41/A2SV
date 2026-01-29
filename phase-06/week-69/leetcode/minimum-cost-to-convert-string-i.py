class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # shortest path + dynamic programming
        # for every letter from a to z as a source, calculate the shortest path from that
        # source to every other destination letter using dijkstra algorithm (heap bfs)
        # minimizing the result as you go
        # then compute the cost at the end

        g = [[float("inf") for _ in range(26)] for _ in range(26)]
        for i in range(26):
            g[i][i] = 0

        n = len(original)
        for i in range(n):
            u = ord(original[i]) - ord('a')
            v = ord(changed[i]) - ord('a')
            w = cost[i]

            g[u][v] = min(g[u][v], w)

        for i in range(26):
            start = i
            
            heap = [(0, start)]
            seen = set()

            while heap:
                d, node = heappop(heap)
                if node in seen:
                    continue
                seen.add(node)
                g[start][node] = min(g[start][node], d)

                for nei in range(26):
                    if g[node][nei] == float("inf") or nei in seen:
                        continue

                    new_d = d + g[node][nei]
                    heappush(heap, (new_d, nei))


        total = 0
        for i in range(len(source)):
            u = ord(source[i]) - ord('a')
            v = ord(target[i]) - ord('a')
            if g[u][v] == float("inf"):
                return -1

            total += g[u][v]

        return total
                    


