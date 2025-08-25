class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n))
        self.tree = [0] * (2 * self.n)

    def query_index(self, ind):
        ind += self.n
        val = self.tree[ind]
        ind = ind // 2 if not ind % 2 else (ind - 1) // 2

        while ind > 0:
            val += self.tree[ind]
            ind = ind // 2 if not ind % 2 else (ind - 1) // 2

        return val

    def update_range(self, l, r, val):

        l += self.n
        r += self.n
        while l < r:

            if l % 2:
                self.tree[l] += val
                l = (l + 1) // 2
            else:
                l //= 2

            if not r % 2:
                self.tree[r] += val
                r = (r - 2) // 2
            else:
                r = (r - 1) // 2

        if l == r:
            self.tree[l] += val


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        # segment tree
        # iterate over every index and for every index query the amount to be deducted
        # due to operations from previous indices and deduct that amount from nums[i]
        # then deduct nums[i] from the range i to i + k - 1 i.e. a window of size k
        

        n = len(nums)
        tree = SegmentTree(n)

        for i in range(n):

            num = nums[i]
            deduct = tree.query_index(i)

            num -= deduct

            if num < 0:
                return False

            if num > 0:

                r = i + k - 1
                if r >= n:
                    return False

                tree.update_range(i, r, num)

        return True
