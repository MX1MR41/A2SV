class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n))
        self.tree = [0] * (2 * self.n)

    def update(self, ind, val):
        ind += self.n
        self.tree[ind] = val
        parent = ind // 2 if not ind % 2 else (ind - 1) // 2

        while parent:
            self.tree[parent] = max(self.tree[2 * parent], self.tree[2 * parent + 1])
            parent = parent // 2 if not parent % 2 else (parent - 1) // 2

    def query(self, l, r):
        l += self.n
        r += self.n

        res = 0

        while l < r:
            if l % 2:
                res = max(self.tree[l], res)
                l = (l + 1)//2
            else:
                l //= 2

            if not r % 2:
                res = max(self.tree[r], res)
                r = (r - 2)//2
            else:
                r = (r - 1)//2

        if l == r:
            res = max(res, self.tree[l])

        return res



class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        # segment tree + dp
        # the first version can be solved by iterating over every previous indices' dp values
        # but this problem needs optimization since it can't be solved by O(N) ops for every N
        # instead we need O(logN) for every N, that is where segment tree comes, tree[i] = dp[i]
        # For every x = nums[i], we need to find the best (dp) value from the range x - k to x - 1
        # we can initialize a max segment tree of size the max number in nums, then for every num, 
        # we query the segment tree to find the max value from x - k to x - 1, then we add that 
        # value to 1 (our initial dp value for nums[i]), then we update tree[x] to the new value.
        # One key thing to note is that we don't build the tree with initial values, instead we 
        # give it values at every loop iteration so that for every i we will have a tree that
        # has precomputer only the values upto dp[i - 1] and no more
        _max = max(nums)

        tree = SegmentTree(_max + 1)
        res = 1

        for i in nums:
            curr = 1
            l = max(0, i - k)
            r = max(0, i - 1)
            curr += tree.query(l, r)
            tree.update(i, curr)

        return tree.tree[1]
        
