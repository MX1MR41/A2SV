class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n))
        self.tree = [0] * (2 * self.n)

    def update(self, ind, val):
        ind += self.n
        self.tree[ind] = val 
        ind = ind//2 if not ind % 2 else (ind - 1)//2
        while ind > 0:
            self.tree[ind] = max(self.tree[2 * ind], self.tree[2 * ind + 1])
            ind = ind//2 if not ind % 2 else (ind - 1)//2

    def search(self, val):
        ind = 1
        while ind < self.n:
            if self.tree[2 * ind] >= val:
                ind = 2 * ind
            else:
                ind = (2 * ind) + 1

        if self.tree[ind] >= val:
            return ind - self.n
        else:
            return -1
            

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # segment tree
        # build a max value segment tree
        # keep moving left down the segment tree to find the leftmost available basket

        n = len(baskets)
        
        tree = SegmentTree(n)

        for i in range(n):
            tree.update(i, baskets[i])

        unplaced = 0

        for i in range(n):
            f = fruits[i]
            ind = tree.search(f)
            if ind == -1:
                unplaced += 1
            else:
                tree.update(ind, 0)

        return unplaced

        
