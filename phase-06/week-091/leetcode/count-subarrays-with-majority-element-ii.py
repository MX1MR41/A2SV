class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n))
        self.tree = [0] * (2 * self.n)

    def update(self, i, x):
        i += self.n

        self.tree[i] += x
        
        p = i//2 if not i % 2 else (i - 1)//2

        while p > 0:
            self.tree[p] = self.tree[2 * p] + self.tree[2 * p + 1]
            p = p//2 if not p % 2 else (p - 1)//2

    def query(self, l, r):
        l += self.n
        r += self.n

        res = 0
        while l <= r:
            if l % 2:
                res += self.tree[l]
                l = (l + 1)//2
            else:
                l //=2

            if not r % 2:
                res += self.tree[r]
                r = (r - 2)//2
            else:
                r = (r - 1)//2

        return res




class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # segment tree + prefix sum
        # the problem can be rephrased as such: convert every target into 1 and every non-target into -1
        # then a subarray which has target as a majority element is a subarray that has a sum greater than 0
        # hence, convert the array into 1s and -1s then just find all subarrays with aa positive sum
        # to do that, iterate over every index i and find how many subarrays which end at at i have +ve sum
        # now the problem becomes similar to prefix sum problems where we can find data by deducting 
        # occurences of a previously seen prefix sum. But for this problem we don't need the occurences of 
        # a single value of a prefix sum, rather we need a range of them
        # i.e. if the prefix sum now is P, we need to find all prefix sums x's which when deducted give us 
        # a +ve sum i.e P - x > 0 => x < P, so we need to count how many prefix sums x's we have seen so far
        # that are less that P, because deducting those (separately ofc) yields a net +ve sum subarray
        # i.e. taking the subarray that starts just after the end of an x prefix sum subarray and 
        # ends at our current index i

        arr = []
        for i in nums:
            if i == target:
                arr.append(1)
            else:
                arr.append(-1)

        pre = 0
        min_neg_pre = 0
        max_pos_pre = 0

        for i in arr:
            pre += i
            min_neg_pre = min(min_neg_pre, pre)
            max_pos_pre = max(max_pos_pre, pre)

        m = max_pos_pre + -min_neg_pre 

        tree = SegmentTree(m + 1)


        tree.update(-min_neg_pre, 1)

        res = 0
        pre = 0
        for i in arr:
            pre += i

            subs = tree.query(0, pre + -min_neg_pre - 1)

            res += subs

            tree.update(pre + -min_neg_pre, 1)

        return res



