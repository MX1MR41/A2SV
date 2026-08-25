class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        g = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            p = succProb[i]
            g[u].append((v, p))
            g[v].append((u, p))
        
        pq = [(-1, start_node)]  
        probabilities = {i: 0 for i in range(n)}
        probabilities[start_node] = 1

        while pq:
            curr_prob, node = heapq.heappop(pq)
            curr_prob = -curr_prob

            if node == end_node:
                return curr_prob
            
            for nei, prob in g[node]:
                new_prob = curr_prob * prob
                if new_prob > probabilities[nei]:
                    probabilities[nei] = new_prob
                    heapq.heappush(pq, (-new_prob, nei))
        
        return 0.0
