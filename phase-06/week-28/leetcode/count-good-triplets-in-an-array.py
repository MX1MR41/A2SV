class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n))
        self.tree = [0] * (2 * self.n)

    def update(self, x):
        x += self.n

        self.tree[x] += 1

        x = x//2 if x % 2 == 0 else (x - 1)//2

        while x > 0:
            self.tree[x] = self.tree[2*x] + self.tree[2*x + 1]
            x = x//2 if x % 2 == 0 else (x - 1)//2

    def query(self, l, r):
        l += self.n
        r += self.n

        extra = 0
        while l < r:
            if l % 2:
                extra += self.tree[l]
                l = (l + 1)//2
            else:
                l //= 2

            if r % 2 == 0:
                extra += self.tree[r]
                r = (r - 2)//2
            else:
                r = (r - 1)//2

        extra += self.tree[l] if l == r else 0

        return extra



class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # segment tree
        # store the indices of the numbers from nums1 in inds1
        # while iterating on nums2, get the index of each num from inds1
        # query how many nums with indices < inds1[num] have been seen so far
        # do this from both the left and right, then for every num assume it is the 
        # middle num and do left[x] * right[x] because that is the total number of 
        # unique combinations that can be formed with x in the middle

        inds1 = {num: ind for ind, num in enumerate(nums1)}

        prev = defaultdict(int)

        n = len(nums1)

        tree = SegmentTree(n + 1)

        for num in nums2:
            ind = inds1[num]

            count_prev = tree.query(0, ind - 1) if ind != 0 else 0
            prev[num] = count_prev

            tree.update(ind)


        tree = SegmentTree(n + 1)
        nxt = defaultdict(int)

        for num in nums2[::-1]:
            ind = inds1[num]

            nxt_count = tree.query(ind + 1, n)
            nxt[num] = nxt_count

            tree.update(ind)

        res = 0
        for i in range(n):
            res += prev[i] * nxt[i]

        return res
