class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # solution works by utilizing an approach the like of peeling an onion
        # we start from leaf nodes and keep "peeling" off them and the next leaf nodes
        # until we are left with one or two nodes, which would effectively be the center(s)
        
        if n == 1: return [0]
        g = defaultdict(list)
        deg = [0] * n
        que = deque()

        for u, v in edges:
            g[u].append(v)
            deg[u] += 1
            g[v].append(u)
            deg[v] += 1

        for i in range(n):
            if deg[i] <= 1:
                que.append(i)

        res = []

        while que:
            res.clear()
            for _ in range(len(que)):
                node = que.popleft()
                res.append(node)
                neis = g[node]

                for nei in neis:
                    deg[nei] -= 1
                    if deg[nei] == 1:
                        que.append(nei)

        return res

                

        

        
        
