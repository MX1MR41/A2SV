class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # bfs + dp
        # counting dp
        # if there are x ways to get odd sum for n edges, and y ways to get even sum for n edges,
        # then to get odd for n + 1 edges we have two options: one is to add 1 to each even way of n,
        # hence now we have x ways to get odd, another option is to add 2 to each odd way of n,
        # hence now we have additional y ways to get odd for n + 1, so in total x + y ways,
        
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





        
