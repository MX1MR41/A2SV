class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n))
        self.tree = [float("inf")] * (2 * self.n)
    
    def update(self, ind, val):
        ind += self.n
        self.tree[ind] = val

        ind = ind//2 if not ind % 2 else (ind - 1)//2

        while ind > 0:
            self.tree[ind] = min(self.tree[2 * ind], self.tree[2 * ind + 1])
            ind = ind//2 if not ind % 2 else (ind - 1)//2

    def query(self, l, r):
        l += self.n
        r += self.n

        res = float("inf")

        while l < r:
            if l % 2:
                res = min(res, self.tree[l])
                l = (l + 1)//2
            else:
                l //= 2

            if not r % 2:
                res = min(res, self.tree[r])
                r = (r - 2)//2
            else:
                r = (r - 1)//2

        if l == r:
            res = min(res, self.tree[l])

        return res

        
            


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # segment tree
        # traverse the rains array day by day; if it rains on a lake that is not empty, 
        # find a zero day (if it exists) that is the closest and after the last day it rained
        # on that lake
        # to find that efficiently, we use a segment tree to store the day indices of when it
        # was a zero day if 

        n = len(rains)
        
        res = [-1] * n

        tree = SegmentTree(n)

        last_seen = dict()

        for i in range(n):
            lake = rains[i]
            if lake == 0:
                tree.update(i, i)
                continue

            if lake in last_seen:
                last_ind = last_seen[lake]
                zero = tree.query(last_ind, i)
                if zero == float("inf"): # no zero in between today and the last lake rain day
                    return []

                res[zero] = lake

                # we can no longer use this zero day, so we remove it
                tree.update(zero, float("inf"))

            last_seen[lake] = i


        # use up any remaining zeros
        while tree.query(0, n - 1) != float("inf"):
            ind = tree.query(0, n - 1)
            res[ind] = 1
            tree.update(ind, float("inf"))

        return res
