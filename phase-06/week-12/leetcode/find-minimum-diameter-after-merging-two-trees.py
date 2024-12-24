class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # topological sort
        # we can use top sort to count distances from leaves to each node to evaluate if it can
        # be a viable center or root from which we can connect to other tree
        # While top sorting, we can also calculate the maximum diameter of the tree by computing it
        # as the sum of the distance the current node traveled and the maximum distance that 
        # the parent has seen so far

        def calculate_diameters(graph, degree, n):
            queue = deque()
            for node in range(n):
                if degree[node] <= 1:
                    queue.append((node, 0))

            visited = set()
            max_diameter = 0
            distance_from_leaf = defaultdict(int)

            while queue:
                for _ in range(len(queue)):
                    node, dist = queue.popleft()
                    if node in visited:
                        continue

                    visited.add(node)

                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            degree[neighbor] -= 1
                            max_diameter = max(max_diameter, dist + 1 + distance_from_leaf[neighbor])
                            distance_from_leaf[neighbor] = max(distance_from_leaf[neighbor], dist + 1)
                            if degree[neighbor] <= 1:
                                queue.append((neighbor, distance_from_leaf[neighbor]))

            return max_diameter, max(distance_from_leaf.values(), default=0)

        def build_graph(edges, n):
            graph = defaultdict(list)
            degree = defaultdict(int)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
                degree[u] += 1
                degree[v] += 1
            return graph, degree

        n1 = len(edges1) + 1
        n2 = len(edges2) + 1

        g1, deg1 = build_graph(edges1, n1)
        g2, deg2 = build_graph(edges2, n2)

        max_diam1, dist1 = calculate_diameters(g1, deg1, n1)
        max_diam2, dist2 = calculate_diameters(g2, deg2, n2)

        return max(max_diam1, max_diam2, dist1 + 1 + dist2)
