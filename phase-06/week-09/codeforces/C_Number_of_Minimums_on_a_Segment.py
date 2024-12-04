from math import ceil, log2

class SegmentTree:
    def __init__(self, n, arr):
        # Padding the array to the next power of 2
        self.n = 2 ** ceil(log2(n))
        self.tree = [[float("inf"), 0] for _ in range(2 * self.n)]
        for i in range(n):
            self.tree[self.n + i] = [arr[i], 1]
        self.build()

    def build(self):
        # Build the tree from bottom up
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.merge(self.tree[2 * i], self.tree[2 * i + 1])

    def merge(self, left, right):
        # Combine two nodes
        if left[0] < right[0]:
            return left
        elif left[0] > right[0]:
            return right
        else:  # Equal minimums
            return [left[0], left[1] + right[1]]

    def set(self, index, value):
        # Update the value at index and propagate changes upwards
        index += self.n
        self.tree[index] = [value, 1]
        while index > 1:
            index //= 2
            self.tree[index] = self.merge(self.tree[2 * index], self.tree[2 * index + 1])

    def find_and_count(self, l, r):
        # Find the minimum and its count in the range [l, r)
        l += self.n
        r += self.n
        res = [float("inf"), 0]
        while l < r:
            if l % 2 == 1:  # If l is a right child
                res = self.merge(res, self.tree[l])
                l += 1
            if r % 2 == 1:  # If r is a right child
                r -= 1
                res = self.merge(res, self.tree[r])
            l //= 2
            r //= 2
        return res


n, m = map(int, input().split())
arr = list(map(int, input().split()))

segment = SegmentTree(n, arr)

for _ in range(m):
    op = list(map(int, input().split()))
    if op[0] == 1:  
        i, v = op[1:]
        segment.set(i, v)
    elif op[0] == 2:  
        l, r = op[1:]
        result = segment.find_and_count(l, r)
        print(result[0], result[1])
