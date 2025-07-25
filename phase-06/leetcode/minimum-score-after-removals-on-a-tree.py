class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        # topological sort + bfs + bit manipulation
        n = len(nums)

        totxor = 0
        for v in nums:
            totxor ^= v

        g = defaultdict(list)
        deg = defaultdict(int)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            deg[u] += 1
            deg[v] += 1

        children = defaultdict(set)

        level = {}

        xor_sub = {i: nums[i] for i in range(n)}

        q = deque(node for node in range(n) if deg[node] == 1)
        seen = set()
        lev = 0

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node in seen:
                    continue
                seen.add(node)
                level[node] = lev

                for nei in g[node]:
                    if nei in seen:
                        continue

                    children[nei].add(node)
                    children[nei].update(children[node])

                    xor_sub[nei] ^= xor_sub[node]

                    deg[nei] -= 1
                    if deg[nei] == 1:
                        q.append(nei)
            lev += 1

        edge_children = []
        for u, v in edges:

            if u in children[v]:
                edge_children.append(u)
            else:
                edge_children.append(v)

        res = float("inf")
        m = len(edge_children)
        for i in range(m):
            c1 = edge_children[i]
            x1 = xor_sub[c1]
            for j in range(i + 1, m):
                c2 = edge_children[j]
                x2 = xor_sub[c2]

                if c1 in children[c2]:

                    a = x1
                    b = x2 ^ x1
                    c = totxor ^ x2
                elif c2 in children[c1]:

                    a = x2
                    b = x1 ^ x2
                    c = totxor ^ x1
                else:

                    a = x1
                    b = x2
                    c = totxor ^ x1 ^ x2

                lo, mi, hi = sorted((a, b, c))
                res = min(res, hi - lo)

        return res
