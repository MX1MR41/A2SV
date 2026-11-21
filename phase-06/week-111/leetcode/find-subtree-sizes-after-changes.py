class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:

        g = defaultdict(list)
        n = len(parent)
        for i in range(1, n):
            g[parent[i]].append(i)

        sub = [1 for _ in range(n)]

        def modify(node, keys):
            
            char = s[node]
            prev = None
            if char in keys:
                par = keys[char]
                prev = par
                parent[node] = par


            
            keys[char] = node
            for ch in g[node]:
                modify(ch, keys)

            if prev is not None:
                keys[char] = prev
            else:
                del keys[char]

            if parent[node] != -1:
                par = parent[node]
                sub[par] += sub[node]


        modify(0, dict())

        return sub

        



        
