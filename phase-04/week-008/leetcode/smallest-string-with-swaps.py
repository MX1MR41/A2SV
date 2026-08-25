class UnionFind:
    def __init__(self, n):
        self.root = {i:i for i in range(n)}
        
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            self.root[rootx] = rooty


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # use unionfind to group swappable letters into the same group
        # then reconstruct the string by popping the smallest from the sorted
        # list of letters that are in the same group
        n = len(s)

        dsu = UnionFind(n)

        for u, v in pairs:
            dsu.union(u, v)

        chars = defaultdict(list)

        for x in dsu.root:
            rootx = dsu.find(x)
            chars[rootx].append(s[x])

        for root in chars:
            chars[root].sort(reverse = True)

        # find the root of the index i, then the letters of the group represented 
        # by that root, then pop the smallest letter available
        ans = [chars[dsu.find(i)].pop() for i in range(n)]

        return "".join(ans)

        
