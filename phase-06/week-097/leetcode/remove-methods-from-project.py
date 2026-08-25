class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for u, v in invocations:
            g[u].append(v)

        sus = set()

        q = deque([k])
        sus.add(k)
        while q:
            for _ in range(len(q)):
                u = q.popleft()

                for v in g[u]:
                    if v in sus:
                        continue

                    q.append(v)
                    sus.add(v)

        g = defaultdict(list)
        for u, v in invocations:
            g[v].append(u)

        seen = set([i for i in sus])
        q = deque(list(seen))

        while q:
            for _ in range(len(q)):
                u = q.popleft()

                for v in g[u]:
                    if v in seen:
                        continue

                    if v not in sus:
                        return [i for i in range(n)]

                    seen.add(v)
                    q.append(v)

        return [i for i in range(n) if i not in sus]

        
