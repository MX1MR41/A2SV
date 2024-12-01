class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.g = defaultdict(list)
        for u, v, w in edges:
            self.g[u].append((w, v))

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.g[u].append((w, v))

    def shortestPath(self, node1: int, node2: int) -> int:

        if node1 == node2: 
            return 0

        heap = self.g[node1][::]

        heapify(heap)

        visited = set()

        while heap:

            w, node = heappop(heap)
            if node == node2:
                return w

            if node in visited:
                continue
            visited.add(node)

            for wv, v in self.g[node]:
                heappush(heap, (w + wv, v))

        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
