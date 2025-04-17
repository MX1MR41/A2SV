# Solution 1
# Note: code gives MLE in Python3 but would pass in C++

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # prefix sum + dp
        # precompute and store for every index for every number, the count of elements 
        # less than or equal to that number in a prefix sum manner. Same for suffix too.
        # Iterate over every combination of (j, k) and for each, count the number of 
        # of elements to the left of j less than k, and the number of elements to the 
        # right of k greater than j. Then use that to compute all possible valid
        # combination for that specific (j, k)
        n = len(nums)

        prefix = [[0 for _ in range(n + 1)]]
        suffix = [[0 for _ in range(n + 1)]]

        prefix[0][nums[0]] = 1

        for i in range(1, n):
            row = prefix[-1][::]
            num = nums[i]

            row[num] += 1
            prefix.append(row)

        for pre in prefix:
            for i in range(1, n + 1):
                pre[i] += pre[i - 1]


        suffix[0][nums[-1]] = 1


        for i in range(n - 2, -1, -1):
            row = suffix[-1][::]
            num = nums[i]

            row[num] += 1
            suffix.append(row)

        for suf in suffix:
            for i in range(n - 1, -1, -1):
                suf[i] += suf[i + 1]

        suffix.reverse()


        res = 0


        for i in range(n):
            a = nums[i]


            for j in range(i):
                b = nums[j]

                if b <= a or a == 0 or b == n:
                    continue

                pre_count = prefix[j][a - 1]
                suf_count = suffix[i][b + 1]

                res += pre_count * suf_count

        return res


# Solution 2
# Note: code gives MLE in Python3 but would pass in C++


class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n))
        self.tree = [0] * (2 * self.n)

    def update(self, x, v):
        x += self.n

        self.tree[x] += v

        x = x // 2 if not x % 2 else (x - 1) // 2

        while x > 0:

            self.tree[x] = self.tree[2 * x] + self.tree[2 * x + 1]
            x = x // 2 if not x % 2 else (x - 1) // 2

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
    def countQuadruplets(self, nums: List[int]) -> int:
        # segment tree
        # for every possible combination of (j, k), count the number of elements to the 
        # left of j which are less than k, and the number of elements to the right of k
        # greater than j. Segment tree for quick accumulation and dynamic updates

        n = len(nums)
        m = max(nums)

        suffix = SegmentTree(m + 1)

        for i in nums:
            suffix.update(i, 1)

        res = 0

        for i in range(n):
            a = nums[i]

            suffix.update(a, -1)
            prefix = SegmentTree(m + 1)

            for j in range(i):
                b = nums[j]
                prefix.update(b, 1)

                if b <= a or a == 0 or b == m:
                    continue

                pre = prefix.query(0, max(0, a - 1))
                suff = suffix.query(b + 1, m)

                res += pre * suff

        return res
