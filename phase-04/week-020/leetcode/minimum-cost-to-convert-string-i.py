class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # simple dijktra's with dp
        g = defaultdict(list)
        
        for i in range(len(cost)):
            o, c, cst = original[i], changed[i], cost[i]
            g[o].append((cst, c))
        
    
        dp = {}

        def dijkstra(src, tar):
            if src == tar:
                return 0

            if (src, tar) in dp:
                return dp[(src, tar)]
            
            visited = set()
            heap = list(g[src])
            heapify(heap)
            
            while heap:
                dist, node = heappop(heap)
                if node in visited:
                    continue
                visited.add(node)
                
                if node == tar:
                    dp[(src, tar)] = dist
                    return dist
                
                for d, nei in g[node]:
                    if nei not in visited:
                        heappush(heap, (dist + d, nei))
            
            dp[(src, tar)] = float('inf')
            return float('inf')
        
        total_cost = 0
        
        for i in range(len(source)):
            src, tar = source[i], target[i]
            if src != tar:
                curr_cost = dijkstra(src, tar)
                if curr_cost == float('inf'):
                    return -1
                total_cost += curr_cost
        
        return total_cost
