class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n))
        # [frequency of x, number of pairs that can be formed by all the x's]
        self.tree = [[0, 0] for _ in range(2 * self.n)]

    def update(self, x, v):
        x += self.n

        self.tree[x][0] += v
        # arithmetic progression formula to count how many pairs could be formed
        # (n*(n + 1))//2 pairs can be formed from n + 1 nums
        # or ((n - 1)*n)//2 pairs can be formed from n nums
        self.tree[x][1] = (self.tree[x][0] * (self.tree[x][0] - 1)) // 2

        x = x // 2 if not x % 2 else (x - 1) // 2

        while x > 0:
            self.tree[x][1] = self.tree[2 * x][1] + self.tree[2 * x + 1][1]
            x = x // 2 if not x % 2 else (x - 1) // 2


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # segment tree
        # use segment tree to calculate the number of pairs over all the nums
        # since nums could get upto 10**9, our segment tree can't be instantiated as
        # large as the biggest num in nums. Instead, since the size of nums won't
        # exceed 10**5, we can sort the nums and assign each of them as an index
        # from 0 to 10**5, that way our segment tree will be small enough but contain
        # all necessary info about all the numbers in nums

        sorted_nums = sorted(nums)
        n = len(nums)
        offset_indices = {}
        for i in range(n):
            num = sorted_nums[i]
            if num not in offset_indices:
                offset_indices[num] = i

        tree = SegmentTree(n + 1)

        res = 0
        l = 0
        for r in range(n):
            rnum = offset_indices[nums[r]]
            tree.update(rnum, 1)

            # we just need to query the top of the segment tree which will have the 
            # total number of pairs
            while tree.tree[1][1] >= k:
                res += n - r
                lnum = offset_indices[nums[l]]
                tree.update(lnum, -1)
                l += 1

        return res
