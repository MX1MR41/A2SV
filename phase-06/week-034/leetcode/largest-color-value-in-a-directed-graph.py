class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # topological sort
        # for every node, store a frequency array of size 26
        # start from source nodes and for every node you reach, update the frequencies of
        # each of the letters to be the maximum it could be by reaching that node by any path 

        n = len(colors)

        indeg = defaultdict(int)
        g = defaultdict(list)

        for u, v in edges:
            g[u].append(v)
            indeg[v] += 1

        freqs = defaultdict(lambda : [0]*26)
        
        que = deque()
        for i in range(n):
            if indeg[i] == 0:
                col = colors[i]
                freqs[i][ord(col) - 97] += 1
                que.append(i)


        res = 0
        seen = set()
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                freq = freqs[node]

                seen.add(node)

                res = max(res, max(freq))

                for nei in g[node]:
                    new_freq = freq[:]

                    col = colors[nei]

                    new_freq[ord(col) - 97] += 1

                    for j in range(26):
                        freqs[nei][j] = max(freqs[nei][j], new_freq[j])

                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        que.append(nei)

        if len(seen) != n:
            return -1

        return res

                    
