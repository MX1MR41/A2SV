class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # dfs on a reverse-edged graph
        g = defaultdict(set)
        for source, dest in edges:
            g[dest].add(source)

        res = [set() for _ in range(n)]
        visited = set()

        def dfs(node):
            if node in visited: return
            visited.add(node)
            ances = g[node]
            res[node] = res[node].union(set(ances))

            for anc in ances:
                if anc not in visited:
                    dfs(anc)
                res[node] = res[node].union(res[anc])

        for i in range(n):
            dfs(i)

        return [sorted(list(i)) for i in res]
                    

            


        
