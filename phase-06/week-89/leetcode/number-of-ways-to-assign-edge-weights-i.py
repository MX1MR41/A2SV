class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # bfs + dp
        # counting dp
        MOD = 10**9 + 7
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        max_depth = -1
        que = deque([1])
        seen = set([1])
        
        while que:
            max_depth += 1
            for _ in range(len(que)):
                node = que.popleft()

                for nei in g[node]:
                    if nei not in seen:
                        seen.add(nei)
                        que.append(nei)


        odd = even = 1
        for i in range(1, max_depth):
            new_even = new_odd = 0

            new_even = (even + odd) % MOD

            new_odd += (odd + even) % MOD

            odd = new_odd
            even = new_even

        return odd





        
