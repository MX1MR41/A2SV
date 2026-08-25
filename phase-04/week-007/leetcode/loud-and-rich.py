class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # solution uses a bfs coupled with topological sort
        # first, construct the DAG and keep track of the in-degree of each node
        # then start from the nodes with in-degree 0 going layer by layer like peeling an onion
        g = defaultdict(list)
        n = len(quiet)
        indeg = [0] * n
        res = [i for i in range(n)]
        
        for rich, poor in richer:
            g[rich].append(poor)
            
            indeg[poor] += 1
    
        que = deque()
            
        for i in range(n):
            if indeg[i] == 0:
                que.append(i)
                
        while que:
            rich = que.popleft()
            curr = quiet[res[rich]]
            neis = g[rich]
            for nei in neis:
                q = quiet[res[nei]]
                indeg[nei] -= 1
                if indeg[nei] == 0 :
                    que.append(nei)
                if curr < q:
                    res[nei] = res[rich]
                    
                    
        return res
                
        
        
