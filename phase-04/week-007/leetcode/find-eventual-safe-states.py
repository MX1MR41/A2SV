class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # solution uses an approach that "peels off" node in a topologically sorted manner.
        # Since terminal nodes are the best case of safe nodes, we start from them and
        # go backwards to parent nodes that have edges towards those terminal nodes
        # and if these parent nodes happen to have an edge only to a terminal node,
        # then it is a safe node. We recursively check the grandparents next and so on.
        g = defaultdict(list)
        deg = [0] * (len(graph)) # out-degree

        for source, edges in enumerate(graph):
            for destination in edges:
                # we store edges in opposite direction
                g[destination].append(source)
                deg[source] += 1


        que = deque()

        for i in range(len(deg)):
            # the terminal nodes
            if deg[i] == 0:
                que.append(i)

        ans = []

        while que:
            for _ in range(len(que)):
                node = que.popleft()
                ans.append(node)
                
                neis = g[node]

                for nei in neis:
                    deg[nei] -= 1
                    # this edge (towards a terminal) was its only outgoing edge
                    # hence it is a safe node
                    if deg[nei] == 0:
                        que.append(nei)

        
        return sorted(ans)

     
        
