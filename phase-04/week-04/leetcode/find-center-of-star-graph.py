class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        g = defaultdict(list)

        for u,v in edges:
            g[u].append(v)
            g[v].append(u)


        for i in g:
            if len(g[i]) == len(g) - 1:
                return i
        
