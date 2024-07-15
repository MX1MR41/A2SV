class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        deg = defaultdict(int)
        for a, b in roads:
            deg[a] += 1
            deg[b] += 1

        country = sorted(list(range(n)), key = lambda x: deg[x])
        importance = defaultdict(list)
        i = 1
        for c in country:
            importance[c] = i
            i += 1

        tot = 0
        for a, b in roads:
            tot += importance[a] + importance[b]

        return tot

        
        
