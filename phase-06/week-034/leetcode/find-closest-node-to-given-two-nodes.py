class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # bfs
        g = defaultdict(list)
        n = len(edges)
        for i in range(n):
            if edges[i] != -1:
                g[i].append(edges[i])

        def bfs(node, g):
            from_source = dict()

            que = deque([node])
            dist = 0
            seen = set()

            while que:
                for _ in range(len(que)):
                    node = que.popleft()
                    if node in seen:
                        continue
                    seen.add(node)

                    from_source[node] = dist

                    for nei in g[node]:
                        if nei not in seen:
                            que.append(nei)

                dist += 1

            return from_source

        from_node1 = bfs(node1, g)
        from_node2 = bfs(node2, g)

        common = []
        for i in range(n):
            if i in from_node1 and i in from_node2:
                d1 = from_node1[i]
                d2 = from_node2[i]

                common.append([i, max(d1, d2)])


        common.sort(key = lambda x: x[1])
        if not common:
            return -1

        return common[0][0]


        

            
