class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n))
        self.tree = [0] * (2 * self.n)

    def add(self, index):
        index += self.n

        self.tree[index] += 1

        index = index // 2 if not index % 2 else (index - 1) // 2

        while index > 0:
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]
            index = index // 2 if not index % 2 else (index - 1) // 2

    def cut(self, index):
        index += self.n

        self.tree[index] -= 1

        index = index // 2 if not index % 2 else (index - 1) // 2

        while index > 0:
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]
            index = index // 2 if not index % 2 else (index - 1) // 2

    def query(self, l, r):
        l += self.n
        r += self.n

        extra = 0

        while l < r:
            if l % 2:
                extra += self.tree[l]
                l = (l + 1) // 2
            else:
                l //= 2

            if not r % 2:
                extra += self.tree[r]
                r = (r - 2) // 2

            else:
                r = (r - 1) // 2

        extra += self.tree[l] if l == r else 0

        return extra


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0

        MAX_VAL = 2001

        prefix = SegmentTree(MAX_VAL)

        if c >= a + b:

            suffix = SegmentTree(MAX_VAL)
            for num in arr:
                suffix.add(num)

            for num in arr:

                suffix.cut(num)
                left_count = prefix.query(max(0, num - a), min(MAX_VAL - 1, num + a))
                right_count = suffix.query(max(0, num - b), min(MAX_VAL - 1, num + b))
                res += left_count * right_count
                prefix.add(num)
        else:

            suffix = SegmentTree(MAX_VAL)
            for num in arr:
                suffix.add(num)
            for j, mid in enumerate(arr):
                suffix.cut(mid)

                for i in range(j):
                    if abs(arr[i] - mid) <= a:

                        l_bound = max(mid - b, arr[i] - c)
                        r_bound = min(mid + b, arr[i] + c)
                        if l_bound <= r_bound:
                            res += suffix.query(
                                max(0, l_bound), min(MAX_VAL - 1, r_bound)
                            )
                prefix.add(mid)
        return res
