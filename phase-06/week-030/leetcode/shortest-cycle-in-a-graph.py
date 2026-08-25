class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        # bfs
        # we perform bfs from every node, keeping track of the distance of every node from the current
        # source node from which we started the bfs. If at any point we come across a nei that was
        # already visited but isn't a direct parent of our current node, then we have reached a 
        # meeting point in a cycle. From then we can calculate the cycle len as 
        # dist[node] + dist[nei] + 1, which guarantees that we compute the shortest length granted that
        # we perform bfs from every node (eventually starting from the node from which cycle "starts")
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        
        min_cycle_len = float('inf')

        for start_node in range(n):

            dist = [-1] * n 
            parent = [-1] * n 

            que = deque()
            
            
            dist[start_node] = 0
            que.append(start_node)
            
            
            while que:
                
                node = que.popleft()
                
                for nei in g[node]:
                    
                    if dist[nei] == -1:
                        
                        dist[nei] = dist[node] + 1
                        parent[nei] = node
                        
                        que.append(nei)

                    
                    elif nei != parent[node]: 

                        cycle_len = dist[node] + dist[nei] + 1
                        
                        min_cycle_len = min(min_cycle_len, cycle_len)

        return min_cycle_len if min_cycle_len != float('inf') else -1
