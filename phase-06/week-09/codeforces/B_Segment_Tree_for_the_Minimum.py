"""

https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/B

"""

from math import ceil, log2


class SegmentTree:
    def __init__(self, n, arr):
        # Padding the array to the next power of 2
        self.n = 2 ** ceil(log2(n))
        self.tree = [0] * (2 * self.n)
        for i in range(n):
            self.tree[self.n + i] = arr[i]
        self.build()

    def build(self):
        # Build the tree from bottom up
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])

    def set(self, index, value):
        # Update the value at index and propagate changes upwards
        index += self.n
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = min(self.tree[2 * index], self.tree[2 * index + 1])

    def find(self, l, r):
        # Find the min in the range [l, r)
        l += self.n
        r += self.n
        min_ = float("inf")
        while l < r:
            if l % 2 == 1:  # If l is a right child
                min_ = min(min_, self.tree[l])
                l += 1
            if r % 2 == 1:  # If r is a right child
                r -= 1
                min_ = min(min_, self.tree[r])
            l //= 2
            r //= 2
        return min_



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
        print(segment.find(l, r))
