class UnionFind:
    def __init__(self):
        self.root = dict()
        self.rank = defaultdict(int)

    def find(self, x):
        if x not in self.root:
            self.root[x] = x
            return x

        while x != self.root[x]:
            x = self.root[x]
            self.root[x] = self.root[self.root[x]]

        return self.root[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            rankx, ranky = self.rank[rootx], self.rank[rooty]
            if rankx < ranky:
                self.root[rootx] = rooty
            elif rankx > ranky:
                self.root[rooty] = rootx
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1

        

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # unionfind

        if not nums: return 0

        nums = list(set(nums))

        dsu = UnionFind()

        for num in nums:
            if num - 1 in dsu.root:
                dsu.union(num, num - 1)
            if num + 1 in dsu.root:
                dsu.union(num, num + 1)

            dsu.find(num)


        count = defaultdict(int)

        for num in nums:
            count[dsu.find(num)] += 1

        return max(count.values())

        
