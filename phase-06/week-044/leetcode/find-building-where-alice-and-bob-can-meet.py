class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n))
        self.tree = [(0, 0) for _ in range(2 * self.n)]

    def update(self, ind, val):
        ind += self.n
        self.tree[ind] = (ind - self.n, val)
        ind = ind//2 if not ind % 2 else (ind - 1)//2

        while ind > 0:
            left = 2 * ind
            right = 2 * ind + 1
            if self.tree[left][1] >= self.tree[right][1]:
                self.tree[ind] = self.tree[left]
            else:
                self.tree[ind] = self.tree[right]

            ind = ind//2 if not ind % 2 else (ind - 1)//2

    def search(self, ind, val):
        curr = 1

        while curr < self.n:
            left = 2 * curr
            right = 2 * curr + 1
            if self.tree[left][0] > ind and self.tree[left][1] > val:
                curr = left
            else:
                curr = right


        if self.tree[curr][0] > ind and self.tree[curr][1] > val:
            return self.tree[curr][0]
        else:

            return -1



            

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # segment tree
        # sort each query and then sort all queries by max(a, b)
        # iterate backwards while building the segment tree
        n = len(heights)
        tree = SegmentTree(n)


        height = n - 1


        for q in queries:
            q.sort()

        queries = [(ind, a, b) for ind, (a, b) in enumerate(queries)]
        queries.sort(key = lambda x: [x[2], x[1]])



        res = []
        for index, a, b in queries[::-1]:
            while height >= b and height >= 0:
                tree.update(height, heights[height])
                height -= 1


            if a == b:
                res.append((index, a))
                continue


            if heights[b] > heights[a]:
                res.append((index, b))
            else:
                ind = tree.search(b, max(heights[a], heights[b]))
                res.append((index, ind))

        res.sort(key = lambda x: x[0])
        return [r[1] for r in res]
