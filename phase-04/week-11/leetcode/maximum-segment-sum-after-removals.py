class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = defaultdict(int)
        self.tot = defaultdict(int) # self.tot[i] stores size of segment which i belongs to

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x,y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            rankx, ranky = self.rank[rootx], self.rank[rooty]
            totx, toty = self.tot[rootx], self.tot[rooty]

            if rankx < ranky:
                self.root[rootx] = rooty
            elif rankx > ranky:
                self.root[rooty] = rootx

            else:
                self.root[rootx] = rooty
                self.rank[rooty] += 1
            # since merging of segments has occured, their segments sizes should merge too
            tot = totx + toty 
            self.tot[rootx] = self.tot[rooty] = tot

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        # we use unionfind to simulate the inverse of deleting process i.e. insertion
        # we start from the last query and we rebuild the array query by query while
        # keeping track of the biggest segment seen so far
        n = len(nums)
        dsu = UnionFind(n)
        arr = [0] * n
        removeQueries.reverse()
        ans = [0]
        segment = 0

        for i in removeQueries[:-1]:
            num = nums[i]
            if i == 0:
                left, right = 0, arr[i+1]
            elif i == n-1:
                left, right = arr[i-1], 0
            else:
                left, right = arr[i-1], arr[i+1]

            dsu.tot[i] += num
            arr[i] = num

            if not left and not right:
                # no non-zero segment from either side so the size of this segment is num
                segment = max(segment, num)
            elif not left:
                # valid segment present on the right only so union to the right
                dsu.union(i,i+1)
                curr = dsu.tot[dsu.find(i)]
                segment = max(segment, curr)
                
            elif not right:
                dsu.union(i,i-1)
                curr = dsu.tot[dsu.find(i)]
                segment = max(segment, curr)
            else:
                # in case valid segments exist on both sides, union both ways
                dsu.union(i,i+1)
                dsu.union(i,i-1)
                curr = dsu.tot[dsu.find(i)]
                segment = max(segment, curr)
                
            ans.append(segment)

        return ans[::-1] 



        
