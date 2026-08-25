class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # bfs + topological sort + dp
        # keep track of the parent of every node in a dictionary using bfs from root
        # simulate bob and alice traveling along bob's path until they meet, and update costs
        # perform reverse top sort and travel starting from leaf nodes while keeping track of
        # the maximum profit that a parent could get by moving to any child node
    
        # build graph and degrees
        g = defaultdict(list)
        deg = defaultdict(int)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            deg[u] += 1
            deg[v] += 1

        # build the parent dictionary
        parent = {}
        que = deque([(node, 0) for node in g[0]])
        seen = set([0])
        while que:
            for _ in range(len(que)):
                node, par = que.popleft()
                if node in seen:
                    continue

                seen.add(node)
                parent[node] = par
                for nei in g[node]:
                    que.append((nei, node))

        # build bob's path and use two pointers to simulate alice and bob moving on it
        bob_path = [bob]
        while bob_path[-1] in parent:
            bob_path.append(parent[bob_path[-1]])

        b = 0
        a = len(bob_path) - 1

        while b <= a:
            if b == a:
                amount[bob_path[b]] //= 2
            else:
                amount[bob_path[b]] = 0

            b += 1
            a -= 1

        
        # collect leaf nodes and traverse upwards from them while keeping track of the 
        # maximum extra profit a parent node could get from any of its children
        que = deque()
        for i in deg:
            if deg[i] == 1 and i != 0:
                que.append(i)

        extra = defaultdict(lambda: float("-inf"))

        while que:
            for _ in range(len(que)):
                node = que.popleft()

                amount[node] += extra[node] if extra[node] != float("-inf") else 0

                par = parent[node]
                extra[par] = max(extra[par], amount[node])
                deg[par] -= 1
                if par != 0 and deg[par] == 1:
                    que.append(par)

        return amount[0] + extra[0] if extra[0] != float("-inf") else amount[0]
